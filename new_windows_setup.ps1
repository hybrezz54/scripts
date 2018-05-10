# Powershell Script to setup a new windows installation
#requires -RunAsAdministrator

$policy = Get-ExecutionPolicy
If ($policy -eq 'Restricted') {
    Set-ExecutionPolicy Bypass -Scope Process
}

# Install Chocolatey - a Windows package manager
Write-Host "Installing Chocolatey..."
# Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://Chocolatey.org/install.ps1'))
Write-Host "Done`n" -ForegroundColor Green

# Upgrade Chocolatey just in case
Write-Host "Upgrading Chocolatey..."
choco upgrade chocolatey
Write-Host "Done`n" -ForegroundColor Green

# Install Git for Windows
Write-Host "Installing Git for Windows..."
choco install git.install
Write-Host "Done`n" -ForegroundColor Green

# Install VS Code
Write-Host "Installing Visual Studio Code..."
choco install visualstudiocode
Write-Host "Done`n" -ForegroundColor Green

# Install Python 3
Write-Host "Installing Python 3..."
choco install python
Write-Host "Done`n" -ForegroundColor Green

# Install Putty
Write-Host "Installing Putty..."
choco install putty.install
Write-Host "Done`n" -ForegroundColor Green

# Install WinSCP
Write-Host "Installing WinSCP..."
choco install winscp.install
Write-Host "Done`n" -ForegroundColor Green

# Install Steam
Write-Host "Installing Steam..."
choco install steam
Write-Host "Done`n" -ForegroundColor Green

# Install Discord
Write-Host "Installing Discord..."
choco install discord
Write-Host "Done`n" -ForegroundColor Green

# Check if Spotify is installed
Write-Host "Checking if Spotify is installed..."
$spotify = $false
Get-AppxPackage -AllUsers | Foreach {
    If ($_.Name -eq 'SpotifyAB.SpotifyMusic') {
        $spotify = $true
        break
    }
}

# Check if Slack is installed
Write-Host "Checking if Slack is installed..."
$slack = $false
Get-AppxPackage -AllUsers | Foreach {
    If ($_.Name -eq '91750D7E.Slack') {
        $slack = $true
        break
    }
}

# Open windows store otherwise
If ($spotify -eq $false -Or $slack -eq $false) {
    If ($spotify -eq $false -And $slack -eq $false) { Write-Host "Install Slack and Spotify from the Windows Store!" -ForegroundColor Red }
    ElseIf ($spotify -eq $false) { Write-Host "Install Spotify from the Windows Store!" -ForegroundColor Red }
    ElseIf ($slack -eq $false) { Write-Host "Install Slack from the Windows Store!`n" -ForegroundColor Red }
    explorer.exe shell:AppsFolder\Microsoft.WindowsStore_8wekyb3d8bbwe!App
}

# Change working directory to my documents
$dir = [Environment]::GetFolderPath('MyDocuments')
Set-Location -Path $dir

# Clone the scripts repo from Github
Write-Host "Cloning scripts repository..."
git clone https://github.com/hybrezz54/scripts.git
Write-Host "Done`n" -ForegroundColor Green

# Add scripts directory to user's PATH
Write-Host "Adding it to the user's PATH environment variable..."
$path = [Environment]::GetEnvironmentVariable("Path", "User")
[Environment]::SetEnvironmentVariable("Path", $path + $dir + "\scripts", "User")
Write-Host "Done`n" -ForegroundColor Green