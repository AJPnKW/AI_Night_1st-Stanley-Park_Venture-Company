# create_all_placeholder_pages.ps1
# Version: 1.1.0
# Purpose: Create placeholder participant, leader, and Andrew workbook pages
# Project: C:\Users\andrew\PROJECTS\Scouter_Jenn\AI_Workshop_4_ventures

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$project_root = 'C:\Users\andrew\PROJECTS\Scouter_Jenn\AI_Workshop_4_ventures'
$participant_web_root = Join-Path $project_root 'web\participant'
$leader_web_root = Join-Path $project_root 'web\leader'
$logs_root = Join-Path $project_root 'logs'
$timestamp = Get-Date -Format 'yyyyMMdd_HHmmss'
$run_name = "create_all_placeholder_pages_$timestamp"
$run_folder = Join-Path $logs_root $run_name
$log_file = Join-Path $run_folder "$run_name.log.txt"
$zip_file = Join-Path $run_folder "$run_name.zip"

$pages = @(
    @{ Section = 'participant'; FileKey = 'JacobT';      DisplayName = 'Jacob';      PageTitle = 'JacobT Personal Workbook' },
    @{ Section = 'participant'; FileKey = 'MichealK';    DisplayName = 'Micheal';    PageTitle = 'MichealK Personal Workbook' },
    @{ Section = 'participant'; FileKey = 'JaydenB';     DisplayName = 'Jayden';     PageTitle = 'JaydenB Personal Workbook' },
    @{ Section = 'participant'; FileKey = 'JaydenW';     DisplayName = 'Jayden';     PageTitle = 'JaydenW Personal Workbook' },
    @{ Section = 'participant'; FileKey = 'Jesse';       DisplayName = 'Jesse';      PageTitle = 'Jesse Personal Workbook' },
    @{ Section = 'participant'; FileKey = 'SebastianJ';  DisplayName = 'Sebastian';  PageTitle = 'SebastianJ Personal Workbook' },

    @{ Section = 'leader';      FileKey = 'JennB';       DisplayName = 'Jenn';       PageTitle = 'JennB Leader Page' },
    @{ Section = 'leader';      FileKey = 'DeboraW';     DisplayName = 'Debora';     PageTitle = 'DeboraW Leader Page' },
    @{ Section = 'leader';      FileKey = 'SheldonS';    DisplayName = 'Sheldon';    PageTitle = 'SheldonS Leader Page' },

    @{ Section = 'participant'; FileKey = 'AndrewP';     DisplayName = 'Andrew';     PageTitle = 'AndrewP Personal Workbook' }
)

function Write-Log {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Message
    )
    $line = "[{0}] {1}" -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'), $Message
    $line | Tee-Object -FilePath $log_file -Append
}

function Get-TargetRoot {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Section
    )

    switch ($Section) {
        'participant' { return $participant_web_root }
        'leader'      { return $leader_web_root }
        default       { throw "Unsupported section: $Section" }
    }
}

function Get-RelativeUrl {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Section,

        [Parameter(Mandatory = $true)]
        [string]$FileKey
    )

    return "/$Section/$FileKey.html"
}

function New-PlaceholderHtml {
    param(
        [Parameter(Mandatory = $true)]
        [string]$DisplayName,

        [Parameter(Mandatory = $true)]
        [string]$FileKey,

        [Parameter(Mandatory = $true)]
        [string]$PageTitle,

        [Parameter(Mandatory = $true)]
        [string]$Section
    )

    $safe_title = [System.Net.WebUtility]::HtmlEncode($PageTitle)
    $safe_display_name = [System.Net.WebUtility]::HtmlEncode($DisplayName)
    $safe_file_key = [System.Net.WebUtility]::HtmlEncode($FileKey)
    $safe_section = [System.Net.WebUtility]::HtmlEncode($Section)

    if ($Section -eq 'leader') {
        $role_label = 'Leader Page'
        $status_text = 'Placeholder leader page live. Final session support content will be added to this same page.'
        $expectation_1 = 'Leader-facing overview and support notes'
        $expectation_2 = 'Session flow, links, and coordination support'
        $expectation_3 = 'This same page will be updated with final content'
    }
    else {
        $role_label = 'Personal Workbook'
        $status_text = 'Placeholder page live. Final workbook content will be added to this same page.'
        $expectation_1 = 'Beginner-friendly hands-on AI and ChatGPT activities'
        $expectation_2 = 'Small practical exercises'
        $expectation_3 = 'This same page will be updated with final content'
    }

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
        <p>This is your $role_label for the AI / ChatGPT session.</p>

        <div class="panel">
            <strong>Your final page content is being prepared.</strong><br>
            You reached the correct page for <strong>$safe_file_key</strong>.
        </div>

        <table class="meta" aria-label="Session details">
            <tr>
                <th>Page Key</th>
                <td>$safe_file_key</td>
            </tr>
            <tr>
                <th>Page Type</th>
                <td>$safe_section</td>
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
                <td>$status_text</td>
            </tr>
        </table>

        <h2>What to expect</h2>
        <ul>
            <li>$expectation_1</li>
            <li>$expectation_2</li>
            <li>$expectation_3</li>
        </ul>

        <p class="footer">Scouter Andrew Pearen</p>
    </main>
</body>
</html>
"@
}

New-Item -ItemType Directory -Path $participant_web_root -Force | Out-Null
New-Item -ItemType Directory -Path $leader_web_root -Force | Out-Null
New-Item -ItemType Directory -Path $run_folder -Force | Out-Null

Write-Log "Run started."
Write-Log "Project root: $project_root"
Write-Log "Participant web root: $participant_web_root"
Write-Log "Leader web root: $leader_web_root"

$total = $pages.Count
$index = 0
$created_files = New-Object System.Collections.Generic.List[string]

foreach ($page in $pages) {
    $index++
    $percent_complete = [int](($index / $total) * 100)
    Write-Progress -Activity 'Creating placeholder pages' -Status $page.FileKey -PercentComplete $percent_complete

    $target_root = Get-TargetRoot -Section $page.Section
    $file_name = '{0}.html' -f $page.FileKey
    $file_path = Join-Path $target_root $file_name
    $html = New-PlaceholderHtml -DisplayName $page.DisplayName -FileKey $page.FileKey -PageTitle $page.PageTitle -Section $page.Section

    Set-Content -Path $file_path -Value $html -Encoding UTF8
    $created_files.Add($file_path) | Out-Null
    Write-Log "Created: $file_path"
}

$manifest_path = Join-Path $run_folder 'placeholder_pages_manifest.csv'
$manifest_rows = foreach ($page in $pages) {
    [pscustomobject]@{
        section = $page.Section
        file_key = $page.FileKey
        display_name = $page.DisplayName
        local_file = (Join-Path (Get-TargetRoot -Section $page.Section) ('{0}.html' -f $page.FileKey))
        relative_url = (Get-RelativeUrl -Section $page.Section -FileKey $page.FileKey)
    }
}
$manifest_rows | Export-Csv -Path $manifest_path -NoTypeInformation -Encoding UTF8
Write-Log "Created manifest: $manifest_path"

Compress-Archive -Path $run_folder -DestinationPath $zip_file -Force
Write-Log "Created zip: $zip_file"
Write-Log "Run completed successfully."

Write-Host ''
Write-Host 'Created placeholder pages:' -ForegroundColor Green
$created_files | ForEach-Object { Write-Host $_ }
Write-Host ''
Write-Host "Manifest: $manifest_path" -ForegroundColor Cyan
Write-Host "Zip: $zip_file" -ForegroundColor Cyan
Write-Host ''
Read-Host 'Press Enter to close'
