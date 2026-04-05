[CmdletBinding()]
param(
  [string]$ProjectRoot = "C:\Users\andrew\PROJECTS\Scouter_Jenn\AI_Workshop_4_ventures"
)

$ErrorActionPreference = "Stop"

$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$archiveRoot = Join-Path $ProjectRoot "archive"
$logsRoot = Join-Path $ProjectRoot "logs"
$artifactsRoot = Join-Path $ProjectRoot "artifacts"
$reportsRoot = Join-Path $ProjectRoot "reports"
$uploadsRoot = Join-Path $ProjectRoot ".ai_uploads"
$logPath = Join-Path $logsRoot "archive_rationalization_$timestamp.log.txt"
$artifactDir = Join-Path $artifactsRoot "archive_$timestamp"
$reportDir = Join-Path $reportsRoot "archive_$timestamp"

foreach ($path in @($archiveRoot, $logsRoot, $artifactsRoot, $reportsRoot, $artifactDir, $reportDir)) {
  New-Item -ItemType Directory -Force -Path $path | Out-Null
}

function Write-Log {
  param([string]$Message)
  $line = "[{0}] {1}" -f (Get-Date -Format "u"), $Message
  $line | Tee-Object -FilePath $logPath -Append | Out-Null
}

function Move-IntoArchive {
  param(
    [string]$SourcePath,
    [string]$ArchiveName
  )

  if (-not (Test-Path $SourcePath)) {
    Write-Log "Skip missing path: $SourcePath"
    return $null
  }

  $targetPath = Join-Path $archiveRoot $ArchiveName
  if (Test-Path $targetPath) {
    Write-Log "Archive target already present: $targetPath"
    return $targetPath
  }

  Move-Item -Path $SourcePath -Destination $targetPath
  Write-Log "Archived: $SourcePath -> $targetPath"
  return $targetPath
}

Write-Log "Archive rationalization started"

$moved = New-Object System.Collections.Generic.List[object]

$explicitTargets = @(
  @{ source = (Join-Path $ProjectRoot ".downlaoded_ai_packages"); name = "legacy_typo_downloaded_ai_packages" },
  @{ source = (Join-Path $ProjectRoot "reference_catalog"); name = "legacy_reference_catalog" },
  @{ source = (Join-Path $ProjectRoot "VM_Setup\scripts\__pycache__"); name = "legacy_vm_pycache" },
  @{ source = (Join-Path $ProjectRoot "scripts\fix_leading_numbers.bak"); name = "legacy_fix_leading_numbers.bak" },
  @{ source = (Join-Path $ProjectRoot "README.txt"); name = "legacy_project_readme_txt" },
  @{ source = (Join-Path $ProjectRoot "start_here.html"); name = "legacy_start_here_html" },
  @{ source = (Join-Path $ProjectRoot "start_here.zip"); name = "legacy_start_here_zip" }
)

foreach ($target in $explicitTargets) {
  $result = Move-IntoArchive -SourcePath $target.source -ArchiveName $target.name
  if ($result) {
    $moved.Add([ordered]@{
      source = $target.source
      destination = $result
      reason = "Explicit legacy target"
    })
  }
}

$vmTextDocs = @(
  (Join-Path $ProjectRoot "VM_Setup\docs\venture_ai_vm_reference_summary.txt"),
  (Join-Path $ProjectRoot "VM_Setup\docs\venture_ai_status_2026-04-03.txt")
)
$vmArchiveDir = Join-Path $archiveRoot "legacy_vm_text_docs"
New-Item -ItemType Directory -Force -Path $vmArchiveDir | Out-Null
foreach ($file in $vmTextDocs) {
  if (Test-Path $file) {
    $dest = Join-Path $vmArchiveDir ([System.IO.Path]::GetFileName($file))
    if (-not (Test-Path $dest)) {
      Move-Item -Path $file -Destination $dest
      Write-Log "Archived VM text doc: $file -> $dest"
      $moved.Add([ordered]@{ source = $file; destination = $dest; reason = "Legacy VM text doc" })
    }
  }
}

$genericArchiveDir = Join-Path $archiveRoot "final_cleanup"
New-Item -ItemType Directory -Force -Path $genericArchiveDir | Out-Null

$genericPatterns = @(
  @{ filter = "__pycache__"; directory = $true; reason = "Python cache directory" },
  @{ filter = "*.bak"; directory = $false; reason = "Backup artifact" }
)

foreach ($pattern in $genericPatterns) {
  $items = Get-ChildItem -Path $ProjectRoot -Recurse -Force -ErrorAction SilentlyContinue | Where-Object {
    if ($pattern.directory) {
      $_.PSIsContainer -and $_.Name -eq $pattern.filter
    } else {
      -not $_.PSIsContainer -and $_.Name -like $pattern.filter
    }
  }

  foreach ($item in $items) {
    if ($item.FullName -like "$archiveRoot*") { continue }
    $safeName = ($item.FullName.Substring($ProjectRoot.Length).TrimStart('\') -replace '[\\/:*?""<>|]', '_')
    $dest = Join-Path $genericArchiveDir $safeName
    if (Test-Path $dest) {
      Write-Log "Skip already archived cleanup item: $dest"
      continue
    }
    Move-Item -Path $item.FullName -Destination $dest
    Write-Log "Archived cleanup item: $($item.FullName) -> $dest"
    $moved.Add([ordered]@{ source = $item.FullName; destination = $dest; reason = $pattern.reason })
  }
}

if (Test-Path $uploadsRoot) {
  $overlayZips = Get-ChildItem -Path $uploadsRoot -Filter "ai_night_delivery_system_overlay_*.zip" -ErrorAction SilentlyContinue | Sort-Object LastWriteTime
  if ($overlayZips.Count -gt 1) {
    $archiveUploadsDir = Join-Path $archiveRoot "old_upload_overlays"
    New-Item -ItemType Directory -Force -Path $archiveUploadsDir | Out-Null
    $toMove = $overlayZips | Select-Object -First ($overlayZips.Count - 1)
    foreach ($zip in $toMove) {
      $dest = Join-Path $archiveUploadsDir $zip.Name
      if (Test-Path $dest) {
        Write-Log "Skip already archived overlay: $dest"
        continue
      }
      Move-Item -Path $zip.FullName -Destination $dest
      Write-Log "Archived old overlay: $($zip.FullName) -> $dest"
      $moved.Add([ordered]@{ source = $zip.FullName; destination = $dest; reason = "Superseded overlay package" })
    }
  }
}

$summary = [ordered]@{
  timestamp = $timestamp
  archiveRoot = $archiveRoot
  movedCount = $moved.Count
  moved = $moved
}

$jsonPath = Join-Path $artifactDir "archive_rationalization.json"
$htmlPath = Join-Path $reportDir "archive_rationalization.html"
$summary | ConvertTo-Json -Depth 6 | Set-Content -Path $jsonPath -Encoding UTF8

$itemsHtml = if ($moved.Count -eq 0) {
  "<li>No new archive moves were needed in this run.</li>"
} else {
  ($moved | ForEach-Object { "<li><code>$($_.source)</code> -> <code>$($_.destination)</code> ($($_.reason))</li>" }) -join ""
}

$html = @"
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Archive Rationalization</title>
  <style>
    body { margin: 0; background: #f4f7fb; color: #1f2937; font: 16px/1.6 "Segoe UI", Arial, sans-serif; }
    .wrap { max-width: 980px; margin: 0 auto; padding: 28px 18px 44px; }
    .hero { background: linear-gradient(135deg, #123152, #0f4c81, #1d7a85); color: #fff; border-radius: 22px; padding: 24px; }
    .section { margin-top: 22px; background: #fff; border: 1px solid #d8e0ea; border-radius: 18px; padding: 20px; }
  </style>
</head>
<body>
  <div class="wrap">
    <section class="hero">
      <h1>Archive Rationalization</h1>
      <p>Moved $($moved.Count) legacy or superseded items into archive storage.</p>
    </section>
    <section class="section">
      <h2>Archived items</h2>
      <ul>$itemsHtml</ul>
    </section>
  </div>
</body>
</html>
"@

$html | Set-Content -Path $htmlPath -Encoding UTF8
Write-Log "Archive rationalization completed"
