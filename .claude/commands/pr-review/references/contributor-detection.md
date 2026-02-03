---
user-invocable: false
description: Contributor type detection logic and display formatting
---

# Contributor Detection

## Detection Script

Fetch all PR data and detect contributor type with minimal commands:

```bash
# Fetch PR data once (excluding body to avoid control character parsing issues)
PR_DATA=$(gh pr view {{arg}} --json number,title,author,url,files,additions,deletions,labels,headRefName)

# Extract author
AUTHOR=$(echo "$PR_DATA" | jq -r '.author.login')

# Detect contributor type
if [[ "$AUTHOR" == *"[bot]"* ]] || [[ "$AUTHOR" == "pulumi-bot" ]] || [[ "$AUTHOR" == app/* ]]; then
  CONTRIBUTOR_TYPE="bot"
else
  if gh api orgs/pulumi/members/$AUTHOR --silent 2>/dev/null; then
    CONTRIBUTOR_TYPE="internal"
  else
    CONTRIBUTOR_TYPE="external"
  fi
fi

echo "Author: $AUTHOR"
echo "Contributor type: $CONTRIBUTOR_TYPE"
echo "$PR_DATA" | jq -r '{number, title, url}'

# Display file paths for use in Step 4
echo ""
echo "Files changed:"
echo "$PR_DATA" | jq -r '.files[].path'
```

## Results to Store

- PR data (in PR_DATA variable)
- Contributor type (bot/internal/external)
- File paths (displayed for Step 4 reference)

## Display Format

Display: "[icon] Reviewing PR #{{arg}} from @username ([type] contributor)"

- 🤖 for bot account
- 📝 for internal/external contributors

## Implementation Notes

- Cache PR_DATA for reuse in later steps (test deployment detection, action execution)
- Contributor type determines message templates and action menu options
