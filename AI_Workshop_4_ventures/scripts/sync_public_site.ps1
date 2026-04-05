[CmdletBinding()]
param(
  [string]$CanonicalSite = "C:\Users\andrew\PROJECTS\Scouter_Jenn\AI_Workshop_4_ventures\web",
  [string]$PublishMirror = "C:\Users\andrew\PROJECTS\Scouter_Jenn\github"
)

$ErrorActionPreference = "Stop"

$projectRoot = "C:\Users\andrew\PROJECTS\Scouter_Jenn\AI_Workshop_4_ventures"
$logsRoot = Join-Path $projectRoot "logs"
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$logPath = Join-Path $logsRoot "sync_public_site_$timestamp.log.txt"
New-Item -ItemType Directory -Force -Path $logsRoot | Out-Null

function Write-Log {
  param([string]$Message)
  $line = "[{0}] {1}" -f (Get-Date -Format "u"), $Message
  $line | Tee-Object -FilePath $logPath -Append | Out-Null
}

Write-Log "Sync started"
New-Item -ItemType Directory -Force -Path $PublishMirror | Out-Null
& robocopy $CanonicalSite $PublishMirror /MIR /R:1 /W:1 /NFL /NDL /NP | Tee-Object -FilePath $logPath -Append | Out-Null
$code = $LASTEXITCODE
Write-Log "Robocopy exit code: $code"
if ($code -ge 8) { throw "Robocopy failed with exit code $code" }

$noJekyll = Join-Path $PublishMirror ".nojekyll"
if (-not (Test-Path $noJekyll)) {
  "" | Set-Content -Path $noJekyll -Encoding UTF8
  Write-Log "Created .nojekyll"
}

$requiredMirrorFiles = @(
  "index.html",
  "participant\index.html",
  "participant\exercises.html",
  "participant\reflections.html",
  "parent\index.html",
  "leader\index.html",
  "facilitator\run-of-show.html",
  "kb\index.html"
)

foreach ($relativePath in $requiredMirrorFiles) {
  $target = Join-Path $PublishMirror $relativePath
  if (-not (Test-Path $target)) {
    throw "Publish mirror is missing required file: $relativePath"
  }
  Write-Log "Verified publish mirror file: $relativePath"
}

Write-Log "Sync completed"
