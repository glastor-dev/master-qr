param(
  [string]$Version = ""
)

$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
$ExePath = Join-Path $Root "dist\master-qr.exe"
$ReadmePath = Join-Path $Root "README.md"
$LicensePath = Join-Path $Root "LICENSE"

if (-not (Test-Path $ExePath)) {
  throw "No existe $ExePath. Primero genera el .exe (PyInstaller)."
}

if (-not $Version) {
  $PyProject = Join-Path $Root "pyproject.toml"
  if (Test-Path $PyProject) {
    $content = Get-Content -LiteralPath $PyProject -Raw
    $m = [regex]::Match($content, '(^|\r?\n)version\s*=\s*"(?<v>[^"]+)"', 'Multiline')
    if ($m.Success) {
      $Version = $m.Groups['v'].Value
    }
  }
}

if (-not $Version) {
  $Version = (Get-Date).ToString("yyyyMMdd_HHmmss")
}

$OutDir = Join-Path $Root "release"
$StageDir = Join-Path $OutDir "master-qr-$Version"
$ZipPath = Join-Path $OutDir "master-qr-$Version-win64.zip"

if (Test-Path $StageDir) { Remove-Item -Recurse -Force $StageDir }
if (Test-Path $ZipPath) { Remove-Item -Force $ZipPath }

New-Item -ItemType Directory -Force -Path $StageDir | Out-Null

Copy-Item -Force $ExePath (Join-Path $StageDir "master-qr.exe")
if (Test-Path $ReadmePath) { Copy-Item -Force $ReadmePath $StageDir }
if (Test-Path $LicensePath) { Copy-Item -Force $LicensePath $StageDir }

Compress-Archive -Path (Join-Path $StageDir "*") -DestinationPath $ZipPath -Force

Write-Output "OK: $ZipPath"
