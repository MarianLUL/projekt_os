# PowerShell helper: serve frontend locally on Windows
Set-StrictMode -Version Latest

Write-Host "Serving frontend on http://localhost:8080"
Push-Location .\frontend
python -m http.server 8080
Pop-Location
