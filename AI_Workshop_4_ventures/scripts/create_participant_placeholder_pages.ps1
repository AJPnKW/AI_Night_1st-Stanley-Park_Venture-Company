# create_participant_placeholder_pages.ps1
# Version: 1.0.0
# Purpose: Create placeholder participant workbook pages for confirmed youth
# Project: C:\Users\andrew\PROJECTS\Scouter_Jenn\AI_Workshop_4_ventures

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$project_root = 'C:\Users\andrew\PROJECTS\Scouter_Jenn\AI_Workshop_4_ventures'
$participant_web_root = Join-Path $project_root 'web\participant'
$logs_root = Join-Path $project_root 'logs'
$timestamp = Get-Date -Format 'yyyyMMdd_HHmmss'
$run_name = "create_participant_placeholder_pages_$timestamp"
$run_folder = Join-Path $logs_root $run_name
$log_file = Join-Path $run_folder "$run_name.log.txt"
$zip_file = Join-Path $run_folder "$run_name.zip"

$participants = @(
    @{ FileKey = 'JacobT';      DisplayName = 'Jacob';      WorkbookTitle = 'JacobT Personal Workbook' },
    @{ FileKey = 'MichealK';    DisplayName = 'Micheal';    WorkbookTitle = 'MichealK Personal Workbook' },
    @{ FileKey = 'JaydenB';     DisplayName = 'Jayden';     WorkbookTitle = 'JaydenB Personal Workbook' },
    @{ FileKey = 'JaydenW';     DisplayName = 'Jayden';     WorkbookTitle = 'JaydenW Personal Workbook' },
    @{ FileKey = 'Jesse';       DisplayName = 'Jesse';      WorkbookTitle = 'Jesse Personal Workbook' },
    @{ FileKey = 'SebastianJ';  DisplayName = 'Sebastian';  WorkbookTitle = 'SebastianJ Personal Workbook' }
)

function Write-Log {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Message
    )
    $line = "[{0}] {1}" -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'), $Message
    $line | Tee-Object -FilePath $log_file -Append
}

function New-PlaceholderHtml {
    param(
        [Parameter(Mandatory = $true)]
        [string]$DisplayName,

        [Parameter(Mandatory = $true)]
        [string]$FileKey,

        [Parameter(Mandatory = $true)]
        [string]$WorkbookTitle
    )

    $safe_title = [System.Net.WebUtility]::HtmlEncode($WorkbookTitle)
    $safe_display_name = [System.Net.WebUtility]::HtmlEncode($DisplayName)
    $safe_file_key = [System.Net.WebUtility]::HtmlEncode($FileKey)

@"
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>$safe_title</title>
    <meta name="robots" content="noindex, nofollow">
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: Arial, Helvetica, sans-serif;
            background: #f5f7fb;
            color: #1f2937;
        }
        .page {
            max-width: 900px;
            margin: 40px auto;
            background: #ffffff;
            border: 1px solid #d1d5db;
            border-radius: 12px;
            padding: 32px;
            box-shadow: 0 6px 18px rgba(0,0,0,0.08);
        }
        .tag {
            display: inline-block;
            padding: 6px 10px;
            border-radius: 999px;
            background: #e5eefc;
            color: #1d4ed8;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 0.04em;
            text-transform: uppercase;
        }
        h1 {
            margin: 16px 0 8px 0;
            font-size: 32px;
            line-height: 1.2;
        }
        h2 {
            margin-top: 28px;
            font-size: 20px;
        }
        p, li {
            font-size: 16px;
            line-height: 1.6;
        }
        .panel {
            margin-top: 20px;
            padding: 18px 20px;
            background: #f9fafb;
            border-left: 4px solid #2563eb;
            border-radius: 8px;
        }
        .meta {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        .meta th,
        .meta td {
            text-align: left;
            border: 1px solid #d1d5db;
            padding: 10px 12px;
            vertical-align: top;
        }
        .meta th {
            width: 220px;
            background: #f3f4f6;
        }
        .footer {
            margin-top: 30px;
            font-size: 14px;
            color: #4b5563;
        }
    </style>
</head>
<body>
    <main class="page">
        <div class="tag">AI Workshop Placeholder</div>
        <h1>Hello $safe_display_name</h1>
        <p>This is your personal workbook page for the AI / ChatGPT session.</p>

        <div class="panel">
            <strong>Your final workbook content is being prepared.</strong><br>
            You reached the correct page for <strong>$safe_file_key</strong>.
        </div>

        <table class="meta" aria-label="Session details">
            <tr>
                <th>Participant Page</th>
                <td>$safe_file_key</td>
            </tr>
            <tr>
                <th>Date</th>
                <td>Wednesday, April 15, 2026</td>
            </tr>
            <tr>
                <th>Time</th>
                <td>7:00 PM to 8:30 PM</td>
            </tr>
            <tr>
                <th>Location</th>
                <td>Hope Lutheran Church / Shaftsbury Dr.</td>
            </tr>
            <tr>
                <th>Bring</th>
                <td>Laptop or Chromebook, optional notebook and pen</td>
            </tr>
            <tr>
                <th>Status</th>
                <td>Placeholder page live. Final workbook content will be added to this same page.</td>
            </tr>
        </table>

        <h2>What to expect</h2>
        <ul>
            <li>Beginner-friendly hands-on AI and ChatGPT activities</li>
            <li>Small practical exercises</li>
            <li>A personal workbook page updated for the session</li>
        </ul>

        <p class="footer">Scouter Andrew Pearen</p>
    </main>
</body>
</html>
"@
}

New-Item -ItemType Directory -Path $participant_web_root -Force | Out-Null
New-Item -ItemType Directory -Path $run_folder -Force | Out-Null

Write-Log "Run started."
Write-Log "Project root: $project_root"
Write-Log "Participant web root: $participant_web_root"

$total = $participants.Count
$index = 0
$created_files = New-Object System.Collections.Generic.List[string]

foreach ($participant in $participants) {
    $index++
    $percent_complete = [int](($index / $total) * 100)
    Write-Progress -Activity 'Creating placeholder participant pages' -Status $participant.FileKey -PercentComplete $percent_complete

    $file_name = '{0}.html' -f $participant.FileKey
    $file_path = Join-Path $participant_web_root $file_name
    $html = New-PlaceholderHtml -DisplayName $participant.DisplayName -FileKey $participant.FileKey -WorkbookTitle $participant.WorkbookTitle

    Set-Content -Path $file_path -Value $html -Encoding UTF8
    $created_files.Add($file_path) | Out-Null
    Write-Log "Created: $file_path"
}

$manifest_path = Join-Path $run_folder 'participant_placeholder_pages_manifest.csv'
$manifest_rows = foreach ($participant in $participants) {
    [pscustomobject]@{
        file_key = $participant.FileKey
        display_name = $participant.DisplayName
        local_file = (Join-Path $participant_web_root ('{0}.html' -f $participant.FileKey))
        relative_url = ('/participant/{0}.html' -f $participant.FileKey)
    }
}
$manifest_rows | Export-Csv -Path $manifest_path -NoTypeInformation -Encoding UTF8
Write-Log "Created manifest: $manifest_path"

Compress-Archive -Path $run_folder -DestinationPath $zip_file -Force
Write-Log "Created zip: $zip_file"
Write-Log "Run completed successfully."

Write-Host ''
Write-Host 'Created participant placeholder pages:' -ForegroundColor Green
$created_files | ForEach-Object { Write-Host $_ }
Write-Host ''
Write-Host "Manifest: $manifest_path" -ForegroundColor Cyan
Write-Host "Zip: $zip_file" -ForegroundColor Cyan
Write-Host ''
Read-Host 'Press Enter to close'
