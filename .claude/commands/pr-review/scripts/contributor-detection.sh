#!/bin/bash
# Contributor Detection Script
# Usage: ./contributor-detection.sh <PR_NUMBER> [--ai|--no-ai]
#
# Outputs:
# - Author username
# - Contributor type (bot/internal/external)
# - Etiquette trust (low/standard/high)
# - Content scrutiny (standard/heightened)
# - AI-suspect flag and reasons
# - Risk tier (typo/minor/standard/major/infra)
# - PR metadata
# - Changed file paths
#
# See references/trust-and-scrutiny.md for the trust model spec.

set -e

if [ -z "$1" ]; then
  echo "Error: PR number required"
  echo "Usage: $0 <PR_NUMBER> [--ai|--no-ai]"
  exit 1
fi

PR_NUMBER="$1"
MANUAL_AI_OVERRIDE="${2:-}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

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

# --- Etiquette trust ---
# Controls tone/welcome language/merge defaults. Independent of content scrutiny.
case "$CONTRIBUTOR_TYPE" in
  internal)
    ETIQUETTE_TRUST="high"
    ;;
  bot)
    # Strip "app/" prefix that gh returns for GitHub Apps so the match works
    BOT_NAME="${AUTHOR#app/}"
    BOT_NAME="${BOT_NAME%\[bot\]}"
    # Known good bots get high; unknown bots get low
    case "$BOT_NAME" in
      dependabot*|pulumi-bot|renovate*|copilot*|github-actions*)
        ETIQUETTE_TRUST="high"
        ;;
      *)
        ETIQUETTE_TRUST="low"
        ;;
    esac
    ;;
  external)
    # Has the author had any prior merged PRs to this repo?
    PRIOR_MERGED=$(gh pr list --repo pulumi/docs --author "$AUTHOR" --state merged --limit 1 --json number 2>/dev/null | jq 'length')
    if [ "${PRIOR_MERGED:-0}" -ge 1 ]; then
      ETIQUETTE_TRUST="standard"
    else
      ETIQUETTE_TRUST="low"
    fi
    ;;
esac

# --- AI-suspect detection ---
AI_SUSPECT_OUTPUT=$("$SCRIPT_DIR/detect-ai-suspect.sh" "$PR_NUMBER" "$MANUAL_AI_OVERRIDE" 2>/dev/null || echo "AI_SUSPECT=false")
AI_SUSPECT=$(echo "$AI_SUSPECT_OUTPUT" | grep '^AI_SUSPECT=' | head -1 | cut -d= -f2)
AI_SUSPECT_REASONS=$(echo "$AI_SUSPECT_OUTPUT" | grep '^AI_SUSPECT_REASONS=' | head -1 | cut -d= -f2-)

# --- Content scrutiny ---
# Standard for everyone unless AI-suspect, in which case heightened.
if [ "$AI_SUSPECT" = "true" ]; then
  CONTENT_SCRUTINY="heightened"
else
  CONTENT_SCRUTINY="standard"
fi

# --- Risk tier ---
# Computed from diff shape. Used to scope review depth.
ADDITIONS=$(echo "$PR_DATA" | jq -r '.additions')
DELETIONS=$(echo "$PR_DATA" | jq -r '.deletions')
TOTAL_CHANGED=$((ADDITIONS + DELETIONS))
FILE_COUNT=$(echo "$PR_DATA" | jq -r '.files | length')
FILES_LIST=$(echo "$PR_DATA" | jq -r '.files[].path')

# Detect infra paths first (they win over size-based tiers)
INFRA_HIT=$(echo "$FILES_LIST" | grep -E '^(scripts/|\.github/workflows/|Makefile$|infrastructure/|package\.json$|webpack\.config\.js$)' || true)

# Detect new files
NEW_FILE_COUNT=$(echo "$PR_DATA" | jq -r '[.files[] | select(.additions > 0 and .deletions == 0)] | length')

# Heuristic for "only prose, no code blocks touched": cheap proxy is "no static/programs/ files
# and the diff doesn't contain ``` markers". We approximate by checking file paths only here;
# the diff-content check happens in Step 4.
HAS_PROGRAM_CHANGES=$(echo "$FILES_LIST" | grep -E '^static/programs/' || true)

if [ -n "$INFRA_HIT" ]; then
  RISK_TIER="infra"
elif [ "$TOTAL_CHANGED" -gt 300 ] || [ "$NEW_FILE_COUNT" -gt 0 ]; then
  RISK_TIER="major"
elif [ "$TOTAL_CHANGED" -le 5 ] && [ "$FILE_COUNT" -le 1 ] && [ -z "$HAS_PROGRAM_CHANGES" ]; then
  RISK_TIER="typo"
elif [ "$TOTAL_CHANGED" -le 30 ] && [ "$FILE_COUNT" -le 1 ] && [ -z "$HAS_PROGRAM_CHANGES" ]; then
  RISK_TIER="minor"
else
  RISK_TIER="standard"
fi

# --- Output results ---
echo "AUTHOR=$AUTHOR"
echo "CONTRIBUTOR_TYPE=$CONTRIBUTOR_TYPE"
echo "ETIQUETTE_TRUST=$ETIQUETTE_TRUST"
echo "CONTENT_SCRUTINY=$CONTENT_SCRUTINY"
echo "AI_SUSPECT=$AI_SUSPECT"
echo "AI_SUSPECT_REASONS=$AI_SUSPECT_REASONS"
echo "RISK_TIER=$RISK_TIER"
echo ""
echo "PR_METADATA:"
echo "$PR_DATA" | jq -r '{number, title, url}'
echo ""
echo "FILES_CHANGED:"
echo "$PR_DATA" | jq -r '.files[].path'
echo ""
echo "PR_DATA_JSON:"
echo "$PR_DATA"
