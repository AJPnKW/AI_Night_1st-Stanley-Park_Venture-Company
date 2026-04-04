[CmdletBinding()]
param(
  [string]$ProjectRoot = "C:\Users\andrew\PROJECTS\Scouter_Jenn\AI_Workshop_4_ventures"
)

$ErrorActionPreference = "Stop"

$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$logsRoot = Join-Path $ProjectRoot "logs"
$reportsRoot = Join-Path $ProjectRoot "reports"
$artifactsRoot = Join-Path $ProjectRoot "artifacts"
$logPath = Join-Path $logsRoot "readiness_checker_$timestamp.log.txt"
$reportDir = Join-Path $reportsRoot "readiness_$timestamp"
$artifactDir = Join-Path $artifactsRoot "readiness_$timestamp"

foreach ($path in @($logsRoot, $reportsRoot, $artifactsRoot, $reportDir, $artifactDir)) {
  New-Item -ItemType Directory -Force -Path $path | Out-Null
}

function Write-Log {
  param([string]$Message)
  $line = "[{0}] {1}" -f (Get-Date -Format "u"), $Message
  $line | Tee-Object -FilePath $logPath -Append | Out-Null
}

Write-Log "Readiness checker started"

$osInfo = Get-CimInstance Win32_OperatingSystem
$cpu = Get-CimInstance Win32_Processor | Select-Object -First 1
$computer = Get-CimInstance Win32_ComputerSystem
$disk = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='C:'"
$architecture = if ($env:PROCESSOR_ARCHITECTURE) { $env:PROCESSOR_ARCHITECTURE } else { "unknown" }
$isArm = $architecture -match "ARM"
$isX64 = $architecture -match "64" -and -not $isArm
function Test-BrowserPresent {
  $paths = @(
    "C:\Program Files\Google\Chrome\Application\chrome.exe",
    "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "C:\Program Files\Mozilla Firefox\firefox.exe",
    "C:\Program Files (x86)\Mozilla Firefox\firefox.exe"
  )

  foreach ($path in $paths) {
    if (Test-Path $path) { return $true }
  }

  foreach ($command in @("msedge", "chrome", "firefox")) {
    if (Get-Command $command -ErrorAction SilentlyContinue) { return $true }
  }

  return $false
}

$browserFound = Test-BrowserPresent
$totalMemoryGb = [math]::Round($computer.TotalPhysicalMemory / 1GB, 2)
$freeDiskGb = if ($disk) { [math]::Round($disk.FreeSpace / 1GB, 2) } else { 0 }
$virtualizationCapable = [bool]($cpu.VMMonitorModeExtensions -or $cpu.VirtualizationFirmwareEnabled -or $computer.HypervisorPresent)

$assignment = "browser-first"
$reason = "Browser-based participant sessions are the default path."

if (-not $browserFound) {
  $assignment = "no-install-fallback"
  $reason = "No supported browser was detected in PATH, so use a presenter-hosted or spare-device fallback."
}
elseif ($isArm) {
  $assignment = "browser-first"
  $reason = "ARM or Apple Silicon style systems route to browser-first because no validated local VM path exists."
}
elseif ($isX64 -and $virtualizationCapable -and $totalMemoryGb -ge 16 -and $freeDiskGb -ge 80) {
  $assignment = "browser-first"
  $reason = "This host could support the optional VM path, but browser-first remains the default participant assignment."
}

$result = [ordered]@{
  timestamp = $timestamp
  computerName = $env:COMPUTERNAME
  osCaption = $osInfo.Caption
  osVersion = $osInfo.Version
  architecture = $architecture
  cpuName = $cpu.Name
  totalMemoryGb = $totalMemoryGb
  freeDiskGbC = $freeDiskGb
  browserFound = $browserFound
  virtualizationCapable = $virtualizationCapable
  optionalVmCapable = ($isX64 -and $virtualizationCapable -and $totalMemoryGb -ge 16 -and $freeDiskGb -ge 80)
  assignment = $assignment
  reason = $reason
  nextAction = switch ($assignment) {
    "no-install-fallback" { "Use a presenter-hosted, paired, or spare-device fallback." }
    default { "Proceed with the browser-first participant path." }
  }
}

$jsonPath = Join-Path $artifactDir "readiness_result.json"
$htmlPath = Join-Path $reportDir "readiness_result.html"
$result | ConvertTo-Json -Depth 5 | Set-Content -Path $jsonPath -Encoding UTF8

$statusClass = if ($assignment -eq "no-install-fallback") { "bad" } else { "good" }
$html = @"
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Readiness Result</title>
  <style>
    body { margin: 0; background: #f4f7fb; color: #1f2937; font: 16px/1.6 "Segoe UI", Arial, sans-serif; }
    .wrap { max-width: 980px; margin: 0 auto; padding: 28px 18px 44px; }
    .hero { background: linear-gradient(135deg, #123152, #0f4c81, #1d7a85); color: #fff; border-radius: 22px; padding: 24px; }
    .section { margin-top: 22px; background: #fff; border: 1px solid #d8e0ea; border-radius: 18px; padding: 20px; }
    table { width: 100%; border-collapse: collapse; }
    th, td { text-align: left; vertical-align: top; padding: 10px 12px; border-bottom: 1px solid #d8e0ea; }
    th { background: #eef4fb; }
    .good, .bad { display: inline-block; padding: 5px 10px; border-radius: 999px; color: #fff; font-weight: 600; }
    .good { background: #146c43; }
    .bad { background: #b42318; }
  </style>
</head>
<body>
  <div class="wrap">
    <section class="hero">
      <h1>Readiness Result</h1>
      <p><span class="$statusClass">$assignment</span></p>
      <p>$reason</p>
    </section>
    <section class="section">
      <h2>Machine Summary</h2>
      <table>
        <tr><th>Computer</th><td>$($result.computerName)</td></tr>
        <tr><th>OS</th><td>$($result.osCaption) ($($result.osVersion))</td></tr>
        <tr><th>Architecture</th><td>$($result.architecture)</td></tr>
        <tr><th>CPU</th><td>$($result.cpuName)</td></tr>
        <tr><th>Total memory</th><td>$($result.totalMemoryGb) GB</td></tr>
        <tr><th>Free disk on C:</th><td>$($result.freeDiskGbC) GB</td></tr>
        <tr><th>Browser found</th><td>$($result.browserFound)</td></tr>
        <tr><th>Optional VM capable</th><td>$($result.optionalVmCapable)</td></tr>
      </table>
    </section>
    <section class="section">
      <h2>Next Action</h2>
      <p>$($result.nextAction)</p>
    </section>
  </div>
</body>
</html>
"@

$html | Set-Content -Path $htmlPath -Encoding UTF8
Write-Log "Readiness outputs written"
Write-Log "Readiness checker completed"
