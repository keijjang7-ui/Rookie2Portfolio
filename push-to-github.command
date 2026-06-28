#!/bin/zsh

set -u

REPO_DIR="/Users/ad02370561/Desktop/my-workspace/Rookie2Portfolio"

echo ""
echo "Rookie2Portfolio GitHub Push"
echo "Repository: $REPO_DIR"
echo ""

if ! cd "$REPO_DIR"; then
  echo "Repository folder was not found."
  echo ""
  echo "Press any key to close."
  read -k 1
  exit 1
fi

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "This folder is not a Git repository."
  echo ""
  echo "Press any key to close."
  read -k 1
  exit 1
fi

BRANCH="$(git branch --show-current)"

if [[ -z "$BRANCH" ]]; then
  echo "Git is currently in detached HEAD state. Push was not attempted."
  echo ""
  echo "Press any key to close."
  read -k 1
  exit 1
fi

echo "Current branch: $BRANCH"
echo ""
git status --short --branch
echo ""

echo "Pushing to origin/$BRANCH..."
git push origin "$BRANCH"
RESULT=$?

echo ""
if [[ $RESULT -eq 0 ]]; then
  echo "Push completed."
else
  echo "Push failed. Review the message above."
fi

echo ""
echo "Press any key to close."
read -k 1
exit $RESULT
