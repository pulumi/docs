#!/bin/bash
# Contributor Detection Script
# Usage: ./contributor-detection.sh <PR_NUMBER>
#
# Outputs:
# - Contributor type (bot/internal/external)
# - Author username
# - PR metadata
# - Changed file paths

set -e

if [ -z "$1" ]; then
  echo "Error: PR number required"
  echo "Usage: $0 <PR_NUMBER>"
  exit 1
fi

PR_NUMBER="$1"

# Fetch PR data once (excluding body to avoid control character parsing issues)
PR_DATA=$(gh pr view "$PR_NUMBER" --json number,title,author,url,files,additions,deletions,labels,headRefName)

# Extract author
AUTHOR=$(echo "$PR_DATA" | jq -r '.author.login')

# Detect contributor type
if [[ "$AUTHOR" == *"[bot]"* ]] || [[ "$AUTHOR" == "pulumi-bot" ]] || [[ "$AUTHOR" == app/* ]]; then
  CONTRIBUTOR_TYPE="bot"
else
  if gh api orgs/pulumi/members/"$AUTHOR" --silent 2>/dev/null; then
    CONTRIBUTOR_TYPE="internal"
  else
    CONTRIBUTOR_TYPE="external"
  fi
fi

# Output results
echo "AUTHOR=$AUTHOR"
echo "CONTRIBUTOR_TYPE=$CONTRIBUTOR_TYPE"
echo ""
echo "PR_METADATA:"
echo "$PR_DATA" | jq -r '{number, title, url}'
echo ""
echo "FILES_CHANGED:"
echo "$PR_DATA" | jq -r '.files[].path'
echo ""
echo "PR_DATA_JSON:"
echo "$PR_DATA"
