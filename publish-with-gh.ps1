$ErrorActionPreference = "Stop"

if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    throw "GitHub CLI (gh) is not installed. Use GITHUB_PUBLISHING.md Option B instead."
}
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw "Git is not installed or not available in PATH."
}

gh auth status
$GitHubUser = (gh api user --jq .login).Trim()
if (-not $GitHubUser) { throw "Could not determine authenticated GitHub username." }

(Get-Content README.md -Raw).Replace("YOUR_USERNAME", $GitHubUser) | Set-Content README.md -Encoding utf8

if (-not (Test-Path .git)) {
    git init
    git branch -M main
}

git add .
$changes = git status --porcelain
if ($changes) {
    git commit -m "feat: initial vendor-neutral cloud architecture assessment"
}

gh repo create cloud-architecture-check `
    --public `
    --description "Vendor-neutral CLI for assessing cloud architectures across security, reliability, performance, cost, and sustainability." `
    --source . `
    --remote origin `
    --push

Write-Host "Published: https://github.com/$GitHubUser/cloud-architecture-check"
