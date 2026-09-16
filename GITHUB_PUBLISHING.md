# Publishing to GitHub

## Recommended repository

- Name: `cloud-architecture-check`
- Visibility: **Public**
- Description: `Vendor-neutral CLI for assessing cloud architectures across security, reliability, performance, cost, and sustainability.`
- Topics: `cloud-architecture`, `well-architected`, `cloud-security`, `reliability`, `finops`, `sustainability`, `python`, `devops`, `multicloud`

## Option A — GitHub CLI (recommended)

1. Install GitHub CLI and authenticate with `gh auth login`.
2. Extract this project and open a terminal in its directory.
3. Run:

```powershell
./publish-with-gh.ps1
```

The script creates a public repository, updates the README badge with your GitHub username, creates the first commit, and pushes `main`.

## Option B — Git + GitHub website

1. Create an empty **public** repository named `cloud-architecture-check` on GitHub. Do not initialize it with a README, license, or `.gitignore` because those files already exist here.
2. Extract this project and open a terminal in its directory.
3. Run:

```powershell
./publish.ps1 -GitHubUser YOUR_GITHUB_USERNAME
```

Git will use your existing Git identity and authentication.

## After publishing

Check that:

- the repository is public;
- the commit appears under your GitHub identity;
- the GitHub Actions test workflow passes;
- the README renders correctly;
- the repository description and topics are set;
- your GitHub profile shows the repository/activity publicly.

Do not fabricate stars, forks, downloads, users, or dependents. Let the repository establish genuine public activity and improve it over time through issues, commits, releases, and contributions.
