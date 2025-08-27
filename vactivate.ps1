# Define the root directory to search for activate.ps1
$searchRoot = Get-Location # Replace with your project's root directory

# Find the activate.ps1 script
$scriptPath = Get-ChildItem -Path $searchRoot -Filter "activate.ps1" -Recurse | Select-Object -First 1 | ForEach-Object { $_.FullName }

# Check if the script was found
if ($scriptPath) {
    Write-Host "Found activate.ps1 at: $scriptPath"

    # Set execution policy if needed (consider the security implications)
    # Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force

    # Execute the activate.ps1 script
    & $scriptPath
    Write-Host "activate.ps1 executed."
} else {
    Write-Host "Error: activate.ps1 not found in $searchRoot or its subdirectories."
}