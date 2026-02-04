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

## Bot Detection Patterns

A PR author is classified as a bot if it matches any of these patterns:

1. **Username ends with `[bot]`**
   - Examples: `github-copilot[bot]`, `dependabot[bot]`, `renovate[bot]`
   - Pattern: `*[bot]*`

1. **Username matches known bot accounts**
   - `pulumi-bot`
   - Pattern: Exact string match

1. **Username starts with `app/`**
   - GitHub Apps use this prefix
   - Pattern: `app/*`

Detection code (from Step 2):

```bash
if [[ "$AUTHOR" == *"[bot]"* ]] || [[ "$AUTHOR" == "pulumi-bot" ]] || [[ "$AUTHOR" == app/* ]]; then
  CONTRIBUTOR_TYPE="bot"
fi
```

The workflow in `.github/workflows/claude-code-review.yml` uses similar detection to determine if a PR should be auto-reviewed:

```bash
AUTHOR="${{ github.event.pull_request.user.login }}"

# GitHub Copilot bot is whitelisted (exact match only for security)
if [[ "$AUTHOR" == "github-copilot[bot]" ]]; then
  echo "has_write_access=true"
fi
```

## Implementation Notes

- Cache PR_DATA for reuse in later steps (test deployment detection, action execution)
- Contributor type determines message templates and action menu options
