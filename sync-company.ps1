param(
    [string]$Message = ""
)

# Change to script root directory
$RepoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $RepoRoot

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "  AI COMPANY - GITHUB AUTO-SYNC SYSTEM    " -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

# 1. Check if git remote exists
$remotes = git remote
if ($remotes -notcontains "origin") {
    Write-Host "[!] No GitHub remote 'origin' detected." -ForegroundColor Yellow
    Write-Host "To link your GitHub repository, run:" -ForegroundColor White
    Write-Host "  git remote add origin https://github.com/<your-username>/<your-repo-name>.git" -ForegroundColor Green
    Write-Host "Then re-run this script." -ForegroundColor Yellow
    exit 1
}

$remoteUrl = git remote get-url origin
Write-Host "[+] Remote: $remoteUrl" -ForegroundColor DarkCyan

# 2. Check current status
$status = git status --porcelain
if (-not $status) {
    Write-Host "[*] No local changes detected. Checking remote updates..." -ForegroundColor Green
    git push origin main
    Write-Host "[✓] GitHub is completely up to date!" -ForegroundColor Green
    exit 0
}

# 3. Stage all changes (guarded by .gitignore)
Write-Host "[*] Staging modified and new files..." -ForegroundColor Cyan
git add .

# 4. Generate commit message
if ([string]::IsNullOrWhiteSpace($Message)) {
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"
    $Message = "update(workspace): sync updates across projects [$timestamp]"
}

# 5. Commit changes
Write-Host "[*] Committing: '$Message'..." -ForegroundColor Cyan
git commit -m "$Message"

# 6. Push to main
Write-Host "[*] Pushing updates to GitHub (branch: main)..." -ForegroundColor Cyan
git push origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host "==========================================" -ForegroundColor Green
    Write-Host " [✓] SUCCESS: All projects synced to GitHub! " -ForegroundColor Green
    Write-Host "==========================================" -ForegroundColor Green
} else {
    Write-Host "[!] Push failed. Please check your GitHub credentials or connection." -ForegroundColor Red
}
