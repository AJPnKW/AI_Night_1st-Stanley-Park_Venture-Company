[CmdletBinding()]
param(
  [string]$ProjectRoot = "C:\Users\andrew\PROJECTS\Scouter_Jenn\AI_Workshop_4_ventures"
)

$ErrorActionPreference = "Stop"

$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$uploadsRoot = Join-Path $ProjectRoot ".ai_uploads"
$logsRoot = Join-Path $ProjectRoot "logs"
$logPath = Join-Path $logsRoot "package_delivery_overlay_$timestamp.log.txt"
$zipPath = Join-Path $uploadsRoot "ai_night_delivery_system_overlay_$timestamp.zip"

foreach ($path in @($uploadsRoot, $logsRoot)) {
  New-Item -ItemType Directory -Force -Path $path | Out-Null
}

function Write-Log {
  param([string]$Message)
  $line = "[{0}] {1}" -f (Get-Date -Format "u"), $Message
  $line | Tee-Object -FilePath $logPath -Append | Out-Null
}

Write-Log "Packaging started"
Compress-Archive -Path `
  (Join-Path $ProjectRoot "archive"), `
  (Join-Path $ProjectRoot "docs"), `
  (Join-Path $ProjectRoot "reports"), `
  (Join-Path $ProjectRoot "artifacts"), `
  (Join-Path $ProjectRoot "config"), `
  (Join-Path $ProjectRoot "downloaded_sources"), `
  (Join-Path $ProjectRoot "logs"), `
  (Join-Path $ProjectRoot "scripts"), `
  (Join-Path $ProjectRoot "web"), `
  (Join-Path $ProjectRoot "VM_Setup") `
  -DestinationPath $zipPath -Force
Write-Log "Packaging completed: $zipPath"
Write-Output $zipPath
