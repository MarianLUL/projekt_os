# PowerShell helper: run backend locally on Windows
Set-StrictMode -Version Latest

Write-Host "Starting backend (Windows)"
if (-Not (Test-Path -Path .\backend\venv)) {
    python -m venv .\backend\venv
}
.\backend\venv\Scripts\Activate.ps1
pip install -r .\backend\requirements.txt
Write-Host "Running uvicorn on http://localhost:8000"
uvicorn backend.main:app --reload --port 8000
