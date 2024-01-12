Write-Output "Hello, World!"
Get-Command python.exe -ErrorAction SilentlyContinue
(Get-Command python.exe -ErrorAction SilentlyContinue).Source
