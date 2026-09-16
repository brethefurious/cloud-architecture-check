param(
    [Parameter(Mandatory=$true)]
    [string]$GitHubUser
)

$ErrorActionPreference = "Stop"

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw "Git is not installed or not available in PATH."
}

(Get-Content README.md -Raw).Replace("YOUR_USERNAME", $GitHubUser) | Set-Content README.md -Encoding utf8

git init
git branch -M main
git add .
git commit -m "feat: initial vendor-neutral cloud architecture assessment"
git remote add origin "https://github.com/$GitHubUser/cloud-architecture-check.git"

git push -u origin main

Write-Host "Published: https://github.com/$GitHubUser/cloud-architecture-check"
