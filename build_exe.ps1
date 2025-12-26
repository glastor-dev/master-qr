param(
  # Ruta opcional al ejecutable de Python (si no se pasa, se auto-detecta).
  [string]$Python = ""
)

$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $PSCommandPath
Push-Location $ScriptDir
try {
  $PythonExe = $null
  $PythonPrefixArgs = @()

  if ($Python -and $Python.Trim().Length -gt 0) {
    $PythonExe = $Python
  }
  else {
    $VenvPython = Join-Path $ScriptDir ".venv\Scripts\python.exe"
    if (Test-Path $VenvPython) {
      $PythonExe = $VenvPython
    }
    elseif (Get-Command py -ErrorAction SilentlyContinue) {
      $PythonExe = "py"
      $PythonPrefixArgs = @("-3")
    }
    else {
      $PythonExe = "python"
    }
  }

  function Run-Python {
    param(
      [Parameter(ValueFromRemainingArguments = $true)]
      [string[]]$Args
    )
    & $PythonExe @PythonPrefixArgs @Args
  }

  Run-Python -m pip install -r "QR/requirements.txt"
  Run-Python -m pip install -r "QR/requirements-dev.txt"

  # Genera un ejecutable Windows (GUI) en dist/master-qr.exe
  Run-Python -m PyInstaller --noconfirm --clean --onefile --windowed -n "master-qr" "QR/main.py"

  Write-Host "OK: ejecutable en dist/master-qr.exe"
}
finally {
  Pop-Location
}
