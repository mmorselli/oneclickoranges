$major = "3"
$minor = "11"
$patch = "6"
$build = "0"

$version = "$major.$minor.$patch.$build"
$pythonUrl = "https://sourceforge.net/projects/winpython/files/WinPython_$major.$minor/$version/Winpython64-$version" + "dot.exe"
$curDir = Get-Location
$downloadsDir = Join-Path -Path $curDir -ChildPath "Downloads"
$pythonDownloadPath = Join-Path -Path $downloadsDir -ChildPath ("Winpython64-$version" + "dot.exe")
$tempDir = Join-Path -Path $curDir -ChildPath "Temp"
$scriptsDir = Join-Path -Path $curDir -ChildPath "Scripts"
$PythonSourcePath = Join-Path -Path $tempDir -ChildPath ("WPy64-$major$minor$patch$build\python-$major.$minor.$patch.amd64")
$pythonInstallDir = Join-Path -Path $curDir -ChildPath "Python"


# Create the directories if they do not exist
if (!(Test-Path -Path $downloadsDir)) { New-Item -ItemType Directory -Path $downloadsDir -ErrorAction SilentlyContinue }
if (!(Test-Path -Path $tempDir)) { New-Item -ItemType Directory -Path $tempDir -ErrorAction SilentlyContinue }

Write-Host "Downloading Python..."

#(New-Object Net.WebClient).DownloadFile($pythonUrl, $pythonDownloadPath)

# Invoke-WebRequest -UserAgent "Wget" -Uri $pythonUrl -OutFile $pythonDownloadPath

# Write-Host "Installing 7Zip4PowerShell..."
# #   Install 7zip module
# [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
# Install-PackageProvider -Name NuGet -MinimumVersion 2.8.5.201 -Scope CurrentUser -Force
# Set-PSRepository -Name 'PSGallery' -InstallationPolicy Trusted

# # Check if 7Zip4PowerShell module is already installed
# if (-not (Get-Module -ListAvailable -Name 7Zip4PowerShell)) {
#     Install-Module -Name 7Zip4PowerShell -Force -Scope CurrentUser
# } else {
#     Write-Host "7Zip4PowerShell module already installed"
# }



Write-Host "Install Python..."

# Expand-7Zip -ArchiveFileName $pythonDownloadPath -TargetPath $tempDir

# Move the folder
# Move-Item -Path $PythonSourcePath -Destination $pythonInstallDir 


Write-Host "Installing/updating pip..."

# # update pip
# Start-Process -FilePath "$pythonInstallDir\python.exe" -ArgumentList "-m pip install --upgrade pip" -Wait

Write-Host "Installing Dependencies..."

$requirementsPath = Join-Path -Path $scriptsDir -ChildPath "requirements.txt"
Start-Process -FilePath "$pythonInstallDir\python.exe" -ArgumentList "-m pip install -r $requirementsPath" -Wait