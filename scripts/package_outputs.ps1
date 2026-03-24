# package_outputs.ps1
# Version: 1.0.0
# Purpose: Create a timestamped zip package from reports and logs after manual review.

[CmdletBinding()]
param()

$ErrorActionPreference = "Stop"
$projectRoot = Split-Path -Parent $PSScriptRoot
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$outDir = Join-Path $projectRoot "out\$timestamp"
$zipPath = Join-Path $outDir "project_package_$timestamp.zip"

New-Item -ItemType Directory -Force -Path $outDir | Out-Null
Compress-Archive -Path (Join-Path $projectRoot "docs"), (Join-Path $projectRoot "reports"), (Join-Path $projectRoot "web"), (Join-Path $projectRoot "github") -DestinationPath $zipPath -Force
Write-Output "Package written to $zipPath"
