# publish_placeholder_pages_and_create_index.ps1
# Version: 1.1.0
# Purpose: Create placeholder summary page, ensure Git remote, commit, and push to GitHub

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$project_root = 'C:\Users\andrew\PROJECTS\Scouter_Jenn\AI_Workshop_4_ventures'
$web_root = Join-Path $project_root 'web'
$participant_root = Join-Path $web_root 'participant'
$leader_root = Join-Path $web_root 'leader'
$project_web_root = Join-Path $web_root 'project'
$logs_root = Join-Path $project_root 'logs'

$repo_url = 'https://github.com/AJPnKW/AI_Night_1st-Stanley-Park_Venture-Company.git'
$public_base_url = 'https://ajpnkw.github.io/AI_Night_1st-Stanley-Park_Venture-Company'

$timestamp = Get-Date -Format 'yyyyMMdd_HHmmss'
$run_name = "publish_placeholder_pages_and_create_index_$timestamp"
$run_folder = Join-Path $logs_root $run_name
$log_file = Join-Path $run_folder "$run_name.log.txt"
$zip_file = Join-Path $run_folder "$run_name.zip"

$site_pages = @(
    @{ Section = 'participant'; FileKey = 'JacobT';     DisplayName = 'JacobT';     RelativeUrl = '/participant/JacobT.html' },
    @{ Section = 'participant'; FileKey = 'MichealK';   DisplayName = 'MichealK';   RelativeUrl = '/participant/MichealK.html' },
    @{ Section = 'participant'; FileKey = 'JaydenB';    DisplayName = 'JaydenB';    RelativeUrl = '/participant/JaydenB.html' },
    @{ Section = 'participant'; FileKey = 'JaydenW';    DisplayName = 'JaydenW';    RelativeUrl = '/participant/JaydenW.html' },
    @{ Section = 'participant'; FileKey = 'Jesse';      DisplayName = 'Jesse';      RelativeUrl = '/participant/Jesse.html' },
    @{ Section = 'participant'; FileKey = 'SebastianJ'; DisplayName = 'SebastianJ'; RelativeUrl = '/participant/SebastianJ.html' },
    @{ Section = 'participant'; FileKey = 'AndrewP';    DisplayName = 'AndrewP';    RelativeUrl = '/participant/AndrewP.html' },
    @{ Section = 'leader';      FileKey = 'JennB';      DisplayName = 'JennB';      RelativeUrl = '/leader/JennB.html' },
    @{ Section = 'leader';      FileKey = 'DeboraW';    DisplayName = 'DeboraW';    RelativeUrl = '/leader/DeboraW.html' },
    @{ Section = 'leader';      FileKey = 'SheldonS';   DisplayName = 'SheldonS';   RelativeUrl = '/leader/SheldonS.html' }
)

function Write-Log {
    param([Parameter(Mandatory = $true)][string]$Message)
    $line = "[{0}] {1}" -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'), $Message
    $line | Tee-Object -FilePath $log_file -Append
}

function Assert-FileExists {
    param([Parameter(Mandatory = $true)][string]$PathToCheck)
    if (-not (Test-Path -LiteralPath $PathToCheck)) {
        throw "Required file not found: $PathToCheck"
    }
}

function Invoke-Git {
    param(
        [Parameter(Mandatory = $true)]
        [string[]]$Arguments
    )
    $output = & git @Arguments 2>&1
    $output | Tee-Object -FilePath $log_file -Append | Out-Null
    if ($LASTEXITCODE -ne 0) {
        throw "git $($Arguments -join ' ') failed."
    }
}

function New-SummaryHtml {
    param(
        [Parameter(Mandatory = $true)]
        [array]$Pages,

        [Parameter(Mandatory = $true)]
        [string]$BaseUrl
    )

    $participant_rows = foreach ($page in ($Pages | Where-Object { $_.Section -eq 'participant' })) {
        $full_url = "$BaseUrl$($page.RelativeUrl)"
@"
<tr>
    <td>$($page.DisplayName)</td>
    <td><a href="$full_url">$full_url</a></td>
</tr>
"@
    }

    $leader_rows = foreach ($page in ($Pages | Where-Object { $_.Section -eq 'leader' })) {
        $full_url = "$BaseUrl$($page.RelativeUrl)"
@"
<tr>
    <td>$($page.DisplayName)</td>
    <td><a href="$full_url">$full_url</a></td>
</tr>
"@
    }

@"
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>AI Workshop Workbook Links</title>
    <style>
        body {
            margin: 0;
            padding: 24px;
            font-family: Arial, Helvetica, sans-serif;
            background: #f5f7fb;
            color: #1f2937;
        }
        .page {
            max-width: 1100px;
            margin: 0 auto;
            background: #ffffff;
            border: 1px solid #d1d5db;
            border-radius: 12px;
            padding: 32px;
            box-shadow: 0 6px 18px rgba(0,0,0,0.08);
        }
        h1, h2 {
            margin-top: 0;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 28px;
        }
        th, td {
            border: 1px solid #d1d5db;
            padding: 10px 12px;
            text-align: left;
            vertical-align: top;
        }
        th {
            background: #f3f4f6;
        }
        a {
            color: #1d4ed8;
            text-decoration: none;
            word-break: break-all;
        }
        a:hover {
            text-decoration: underline;
        }
        .note {
            margin-bottom: 24px;
            padding: 14px 16px;
            background: #f9fafb;
            border-left: 4px solid #2563eb;
            border-radius: 8px;
        }
    </style>
</head>
<body>
    <main class="page">
        <h1>AI Workshop Workbook Links</h1>

        <div class="note">
            Placeholder summary page for workbook and leader links.
        </div>

        <h2>Participant Pages</h2>
        <table>
            <thead>
                <tr>
                    <th>Name Key</th>
                    <th>Public Link</th>
                </tr>
            </thead>
            <tbody>
$($participant_rows -join "`n")
            </tbody>
        </table>

        <h2>Leader Pages</h2>
        <table>
            <thead>
                <tr>
                    <th>Name Key</th>
                    <th>Public Link</th>
                </tr>
            </thead>
            <tbody>
$($leader_rows -join "`n")
            </tbody>
        </table>
    </main>
</body>
</html>
"@
}

New-Item -ItemType Directory -Path $run_folder -Force | Out-Null
New-Item -ItemType Directory -Path $project_web_root -Force | Out-Null

Write-Log "Run started."
Write-Log "Project root: $project_root"
Write-Log "Repo URL: $repo_url"
Write-Log "Public base URL: $public_base_url"

foreach ($page in $site_pages) {
    if ($page.Section -eq 'participant') {
        Assert-FileExists -PathToCheck (Join-Path $participant_root "$($page.FileKey).html")
    }
    else {
        Assert-FileExists -PathToCheck (Join-Path $leader_root "$($page.FileKey).html")
    }
}

$summary_full_path = Join-Path $project_web_root 'workbook_links.html'
$summary_html = New-SummaryHtml -Pages $site_pages -BaseUrl $public_base_url
Set-Content -Path $summary_full_path -Value $summary_html -Encoding UTF8
Write-Log "Created summary page: $summary_full_path"

$manifest_path = Join-Path $run_folder 'published_pages_manifest.csv'
$manifest_rows = foreach ($page in $site_pages) {
    [pscustomobject]@{
        section = $page.Section
        file_key = $page.FileKey
        local_file = if ($page.Section -eq 'participant') { Join-Path $participant_root "$($page.FileKey).html" } else { Join-Path $leader_root "$($page.FileKey).html" }
        public_url = "$public_base_url$($page.RelativeUrl)"
        summary_page_url = "$public_base_url/project/workbook_links.html"
    }
}
$manifest_rows | Export-Csv -Path $manifest_path -NoTypeInformation -Encoding UTF8
Write-Log "Created manifest: $manifest_path"

Push-Location $project_root
try {
    if (-not (Test-Path -LiteralPath (Join-Path $project_root '.git'))) {
        Write-Log 'Initializing git repository.'
        Invoke-Git -Arguments @('init')
    }

    $remote_output = (& git remote get-url origin 2>$null)
    if ($LASTEXITCODE -ne 0) {
        Write-Log 'Adding origin remote.'
        Invoke-Git -Arguments @('remote', 'add', 'origin', $repo_url)
    }
    elseif ($remote_output.Trim() -ne $repo_url) {
        Write-Log 'Updating origin remote.'
        Invoke-Git -Arguments @('remote', 'set-url', 'origin', $repo_url)
    }

    Write-Log 'Git status before add.'
    Invoke-Git -Arguments @('status', '--short')

    Write-Log 'Staging files.'
    Invoke-Git -Arguments @('add',
        'web/participant/JacobT.html',
        'web/participant/MichealK.html',
        'web/participant/JaydenB.html',
        'web/participant/JaydenW.html',
        'web/participant/Jesse.html',
        'web/participant/SebastianJ.html',
        'web/participant/AndrewP.html',
        'web/leader/JennB.html',
        'web/leader/DeboraW.html',
        'web/leader/SheldonS.html',
        'web/project/workbook_links.html'
    )

    $changes_output = (& git diff --cached --name-only)
    $changes_output | Tee-Object -FilePath $log_file -Append | Out-Null

    if ([string]::IsNullOrWhiteSpace(($changes_output -join ''))) {
        Write-Log 'No staged changes detected. Skipping commit.'
    }
    else {
        Write-Log 'Committing changes.'
        $commit_output = (& git commit -m 'Add AI workshop placeholder pages and summary links' 2>&1)
        $commit_output | Tee-Object -FilePath $log_file -Append | Out-Null
        if ($LASTEXITCODE -ne 0) {
            throw 'git commit failed.'
        }
    }

    $branch_name = (& git branch --show-current).Trim()
    if ([string]::IsNullOrWhiteSpace($branch_name)) {
        Write-Log 'Creating main branch.'
        Invoke-Git -Arguments @('checkout', '-B', 'main')
        $branch_name = 'main'
    }

    Write-Log "Pushing branch: $branch_name"
    Invoke-Git -Arguments @('push', '-u', 'origin', $branch_name)
}
finally {
    Pop-Location
}

Compress-Archive -Path $run_folder -DestinationPath $zip_file -Force
Write-Log "Created zip: $zip_file"
Write-Log 'Run completed successfully.'

Write-Host ''
Write-Host "Summary page: $public_base_url/project/workbook_links.html" -ForegroundColor Green
Write-Host "JacobT: $public_base_url/participant/JacobT.html"
Write-Host "MichealK: $public_base_url/participant/MichealK.html"
Write-Host "JaydenB: $public_base_url/participant/JaydenB.html"
Write-Host "JaydenW: $public_base_url/participant/JaydenW.html"
Write-Host "Jesse: $public_base_url/participant/Jesse.html"
Write-Host "SebastianJ: $public_base_url/participant/SebastianJ.html"
Write-Host "AndrewP: $public_base_url/participant/AndrewP.html"
Write-Host "JennB: $public_base_url/leader/JennB.html"
Write-Host "DeboraW: $public_base_url/leader/DeboraW.html"
Write-Host "SheldonS: $public_base_url/leader/SheldonS.html"
Write-Host ''
Write-Host "Manifest: $manifest_path" -ForegroundColor Cyan
Write-Host "Zip: $zip_file" -ForegroundColor Cyan
Write-Host ''
Read-Host 'Press Enter to close'
