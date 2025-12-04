# Simple preview script using Python's http.server
$pwd = Get-Location
Write-Host "Serving $pwd on http://localhost:8000"
# Use the Python executable available in the environment
python -m http.server 8000
