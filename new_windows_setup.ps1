# Powershell Script to setup a new windows installation
#requires -RunAsAdministrator

$policy = Get-ExecutionPolicy
If ($policy -eq 'Restricted') {
    Set-ExecutionPolicy Bypass -Scope Process
}

# Install Chocolatey - a Windows package manager
Write-Host "Installing Chocolatey..."
# Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://Chocolatey.org/install.ps1'))
Write-Host "Done`n"

# Upgrade Chocolatey just in case
Write-Host "Upgrading Chocolatey..."
choco upgrade chocolatey
Write-Host "Done`n"

# Install VS Code
Write-Host "Installing Visual Studio Code..."
choco install visualstudiocode
Write-Host "Done`n"

# Install Python 3
Write-Host "Installing Python 3..."
choco install python
Write-Host "Done`n"

# Install Putty
Write-Host "Installing Putty..."
choco install putty.install
Write-Host "Done`n"

# Install WinSCP
Write-Host "Installing WinSCP..."
choco install winscp.install
Write-Host "Done`n"

# Install Steam
Write-Host "Installing Steam..."
choco install steam
Write-Host "Done`n"

# Install Discord
Write-Host "Installing Discord..."
choco install discord
Write-Host "Done`n"

# Check if Spotify is installed
Write-Host "Checking if Spotify and Slack are installed..."
$spotify = $false
Get-AppxPackage -AllUsers | Foreach {
    If ($_.Name -eq 'SpotifyAB.SpotifyMusic') {
        $spotify = $true
        break
    }
}

# Check if Slack is installed
$slack = $false
Get-AppxPackage -AllUsers | Foreach {
    If ($_.Name -eq '91750D7E.Slack') {
        $slack = $true
        break
    }
}

# Open windows store otherwise
If ($spotify -eq $false -Or $slack -eq $false) {
    If ($spotify -eq $false -And $slack -eq $false) { Write-Host "Install Slack and Spotify from the Windows Store!" }
    ElseIf ($spotify -eq $false) { Write-Host "Install Spotify from the Windows Store!" }
    ElseIf ($slack -eq $false) { Write-Host "Install Slack from the Windows Store!" }
    explorer.exe shell:AppsFolder\Microsoft.WindowsStore_8wekyb3d8bbwe!App
}

