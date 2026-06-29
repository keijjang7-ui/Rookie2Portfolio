#!/bin/zsh

set -u

REPO_DIR="${0:A:h}"
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
export GIT_TERMINAL_PROMPT=1

echo ""
echo "Rookie2Portfolio GitHub Auto Commit + Push"
echo "Repository: $REPO_DIR"
echo ""

if ! cd "$REPO_DIR"; then
  echo "Repository folder was not found."
  exit 1
fi

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "This folder is not a Git repository."
  exit 1
fi

BRANCH="$(git branch --show-current)"

if [[ -z "$BRANCH" ]]; then
  echo "Git is currently in detached HEAD state. Push was not attempted."
  exit 1
fi

echo "Current branch: $BRANCH"
echo ""
git status --short --branch
echo ""

if [[ -n "$(git status --porcelain)" ]]; then
  COMMIT_MESSAGE="Update Rookie2 portfolio $(date '+%Y-%m-%d %H:%M:%S')"

  echo "Staging all changes..."
  git add -A
  ADD_RESULT=$?

  if [[ $ADD_RESULT -ne 0 ]]; then
    echo ""
    echo "Staging failed."
    exit $ADD_RESULT
  fi

  if git diff --cached --quiet; then
    echo "No committable changes after staging."
  else
    echo "Creating commit:"
    echo "$COMMIT_MESSAGE"
    git commit -m "$COMMIT_MESSAGE"
    COMMIT_RESULT=$?

    if [[ $COMMIT_RESULT -ne 0 ]]; then
      echo ""
      echo "Commit failed."
      exit $COMMIT_RESULT
    fi
  fi
else
  echo "No local file changes to commit."
fi

echo ""
echo "Syncing with origin/$BRANCH..."
git pull --rebase origin "$BRANCH"
PULL_RESULT=$?

if [[ $PULL_RESULT -ne 0 ]]; then
  echo ""
  echo "Pull/rebase failed. Resolve the message above, then run this command again."
  exit $PULL_RESULT
fi

echo ""
echo "Pushing to origin/$BRANCH..."
git push origin "$BRANCH"
RESULT=$?

echo ""
if [[ $RESULT -eq 0 ]]; then
  echo "GitHub update completed."
else
  echo "Push failed. Review the message above."
fi

exit $RESULT
