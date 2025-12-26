param(
  [Parameter(Mandatory = $false)]
  [string]$Owner = "glastor-dev",

  [Parameter(Mandatory = $false)]
  [string]$Repo = "master-qr",

  [Parameter(Mandatory = $false)]
  [string]$Tag = "v1.0.0",

  [Parameter(Mandatory = $false)]
  [string]$Name = "v1.0.0",

  [Parameter(Mandatory = $false)]
  [string]$AssetPath = "release/master-qr-1.0.0-win64.zip",

  [Parameter(Mandatory = $false)]
  [switch]$ReplaceAsset,

  [Parameter(Mandatory = $false)]
  [switch]$Draft,

  [Parameter(Mandatory = $false)]
  [switch]$Prerelease
)

$ErrorActionPreference = "Stop"

# Mejora compatibilidad de encoding en PowerShell (acentos/ñ)
try {
  $OutputEncoding = [System.Text.Encoding]::UTF8
  [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
} catch { }

function Get-GitHubToken {
  $token = $env:GH_TOKEN
  if (-not $token) { $token = $env:GH_TOKEN }
  if (-not $token) {
    throw "No se encontró token. Define GH_TOKEN o GITHUB_TOKEN (PAT con scope 'repo' para repos privados, o 'public_repo' para públicos)."
  }
  return $token
}

function Get-ReleaseNotesFromChangelog {
  param(
    [string]$ChangelogPath = "CHANGELOG.md",
    [string]$VersionTag = "1.0.0"
  )

  if (-not (Test-Path -LiteralPath $ChangelogPath)) {
    return ""
  }

  $text = Get-Content -LiteralPath $ChangelogPath -Raw
  $pattern = "(?ms)^## \[$([regex]::Escape($VersionTag))\].*?(?=^## \[|\z)"
  $m = [regex]::Match($text, $pattern)
  if (-not $m.Success) { return "" }

  return $m.Value.Trim()
}

$token = Get-GitHubToken

if (-not (Test-Path -LiteralPath $AssetPath)) {
  throw "No existe el asset: $AssetPath"
}

$apiBase = "https://api.github.com"
$headers = @{
  "Accept" = "application/vnd.github+json"
  "X-GitHub-Api-Version" = "2022-11-28"
  "Authorization" = "Bearer $token"
  "User-Agent" = "master-qr-release-script"
}

$versionForNotes = $Tag
if ($versionForNotes.StartsWith("v")) { $versionForNotes = $versionForNotes.Substring(1) }
$body = Get-ReleaseNotesFromChangelog -VersionTag $versionForNotes

$release = $null
$releaseId = $null
$uploadUrl = $null

Write-Host "Buscando release por tag $Tag..."
try {
  $release = Invoke-RestMethod -Method Get -Uri "$apiBase/repos/$Owner/$Repo/releases/tags/$Tag" -Headers $headers
}
catch {
  $status = $null
  if ($_.Exception.Response) {
    try { $status = [int]$_.Exception.Response.StatusCode } catch {}
  }

  if ($status -ne 404) {
    throw
  }
}

if (-not $release) {
  Write-Host "No existe. Creando release $Name ($Tag)..."
  $payload = @{
    tag_name   = $Tag
    name       = $Name
    body       = $body
    draft      = [bool]$Draft
    prerelease = [bool]$Prerelease
  } | ConvertTo-Json -Depth 5

  $release = Invoke-RestMethod -Method Post -Uri "$apiBase/repos/$Owner/$Repo/releases" -Headers $headers -ContentType "application/json" -Body $payload
}

$releaseId = $release.id
$uploadUrl = $release.upload_url
if (-not $releaseId -or -not $uploadUrl) {
  throw "No se pudo obtener id/upload_url de la release."
}

$assetName = Split-Path -Leaf $AssetPath

if ($ReplaceAsset) {
  Write-Host "Buscando asset existente '$assetName' para reemplazar..."
  $assets = Invoke-RestMethod -Method Get -Uri "$apiBase/repos/$Owner/$Repo/releases/$releaseId/assets" -Headers $headers
  $existing = $assets | Where-Object { $_.name -eq $assetName } | Select-Object -First 1
  if ($existing) {
    Write-Host "Eliminando asset existente (id=$($existing.id))..."
    Invoke-RestMethod -Method Delete -Uri "$apiBase/repos/$Owner/$Repo/releases/assets/$($existing.id)" -Headers $headers | Out-Null
  }
}

$uploadBase = $uploadUrl.Split('{')[0]
$uploadUri = "$uploadBase?name=$([uri]::EscapeDataString($assetName))"

Write-Host "Subiendo asset: $AssetPath -> $uploadUri"
Invoke-RestMethod -Method Post -Uri $uploadUri -Headers $headers -ContentType "application/zip" -InFile $AssetPath | Out-Null

Write-Host "OK: Release publicada y asset subido."
Write-Host "URL: $($release.html_url)"
