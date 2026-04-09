#!/bin/bash
# Fact-check gating decision
# Usage: ./should-fact-check.sh <PR_NUMBER> <CONTRIBUTOR_TYPE> <AI_SUSPECT> <RISK_TIER>
#
# Outputs (key=value pairs on stdout):
#   FACT_CHECK=run|skip
#   FACT_CHECK_REASON=<short explanation>
#
# Decision tree:
#   1. AI_SUSPECT=true       -> always RUN (AI hallucinations show up everywhere)
#   2. RISK_TIER=typo        -> SKIP (nothing to fact-check on a 5-line typo fix)
#   3. dependabot/bot PR     -> SKIP unless content paths are touched
#   4. Any content/{docs,blog,tutorials,learn,what-is}/ path in diff -> RUN
#   5. Otherwise -> SKIP
#
# See references/trust-and-scrutiny.md and references/fact-check.md for the spec.

set -e

if [ -z "$1" ] || [ -z "$2" ] || [ -z "$3" ] || [ -z "$4" ]; then
  echo "Error: missing arguments" >&2
  echo "Usage: $0 <PR_NUMBER> <CONTRIBUTOR_TYPE> <AI_SUSPECT> <RISK_TIER>" >&2
  exit 1
fi

PR_NUMBER="$1"
CONTRIBUTOR_TYPE="$2"
AI_SUSPECT="$3"
RISK_TIER="$4"

# AI-suspect always wins
if [ "$AI_SUSPECT" = "true" ]; then
  echo "FACT_CHECK=run"
  echo "FACT_CHECK_REASON=AI-suspect override (heightened scrutiny)"
  exit 0
fi

# Typo tier skips
if [ "$RISK_TIER" = "typo" ]; then
  echo "FACT_CHECK=skip"
  echo "FACT_CHECK_REASON=typo-tier PR (no factual content to verify)"
  exit 0
fi

# Fetch changed files
FILES=$(gh pr view "$PR_NUMBER" --json files --jq '.files[].path' 2>/dev/null || echo "")

# Check for content paths
CONTENT_HIT=$(echo "$FILES" | grep -E '^content/(docs|blog|tutorials|learn|what-is)/' || true)
CONTENT_COUNT=$(echo "$CONTENT_HIT" | grep -c . || true)
CONTENT_COUNT=${CONTENT_COUNT:-0}

# Bot PRs only run if they actually touch content
if [ "$CONTRIBUTOR_TYPE" = "bot" ]; then
  if [ "$CONTENT_COUNT" -gt 0 ]; then
    echo "FACT_CHECK=run"
    echo "FACT_CHECK_REASON=bot PR but $CONTENT_COUNT content file(s) changed"
  else
    echo "FACT_CHECK=skip"
    echo "FACT_CHECK_REASON=bot PR with no content changes"
  fi
  exit 0
fi

# Human PRs run if any content path is touched
if [ "$CONTENT_COUNT" -gt 0 ]; then
  echo "FACT_CHECK=run"
  echo "FACT_CHECK_REASON=$CONTENT_COUNT content file(s) changed"
else
  echo "FACT_CHECK=skip"
  echo "FACT_CHECK_REASON=no content paths in diff"
fi
