#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "Usage: ./publish.sh <github-username>"
  exit 1
fi

USER_NAME="$1"

python - "$USER_NAME" <<'PY'
from pathlib import Path
import sys
p = Path("README.md")
p.write_text(p.read_text(encoding="utf-8").replace("YOUR_USERNAME", sys.argv[1]), encoding="utf-8")
PY

git init
git branch -M main
git add .
git commit -m "feat: initial vendor-neutral cloud architecture assessment"
git remote add origin "https://github.com/${USER_NAME}/cloud-architecture-check.git"
git push -u origin main

echo "Published: https://github.com/${USER_NAME}/cloud-architecture-check"
