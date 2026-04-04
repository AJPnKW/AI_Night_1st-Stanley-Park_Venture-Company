[CmdletBinding()]
param()

$ErrorActionPreference = "Stop"
$projectRoot = "C:\Users\andrew\PROJECTS\Scouter_Jenn\AI_Workshop_4_ventures"

powershell -ExecutionPolicy Bypass -File (Join-Path $projectRoot "scripts\archive_rationalization.ps1")
python (Join-Path $projectRoot "scripts\build_delivery_system.py")
powershell -ExecutionPolicy Bypass -File (Join-Path $projectRoot "scripts\readiness_checker.ps1")
powershell -ExecutionPolicy Bypass -File (Join-Path $projectRoot "scripts\sync_public_site.ps1")
powershell -ExecutionPolicy Bypass -File (Join-Path $projectRoot "scripts\validate_delivery_system.ps1")
powershell -ExecutionPolicy Bypass -File (Join-Path $projectRoot "scripts\package_delivery_overlay.ps1")
