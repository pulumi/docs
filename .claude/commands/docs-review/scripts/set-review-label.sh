#!/usr/bin/env bash
# set-review-label.sh — idempotently set one of the mutually-exclusive
# review-state labels on a PR.
#
# The four state labels describe where a review is in its lifecycle:
#   review:in-progress       — workflow is currently running
#   review:outstanding-issues — review done, 🚨 Outstanding > 0
#   review:no-blockers       — review done, 🚨 Outstanding == 0
#   review:stale             — author pushed new commits since the review
#
# Plus a 5th terminal state for workflow failures:
#   review:error             — workflow failed before publishing
#
# These five labels are mutually exclusive. Setting any one removes the
# other four. Skip-reason labels (review:trivial, review:frontmatter-only,
# review:prose-flagged) are informational and live outside this set.
#
# Usage:
#   set-review-label.sh --pr 123 --label review:in-progress [--repo owner/repo]
#
# If --repo is omitted, $GITHUB_REPOSITORY is used; failing that, gh's
# default resolution from the current directory.

set -euo pipefail

PR=""
LABEL=""
REPO="${GITHUB_REPOSITORY:-}"

while [ $# -gt 0 ]; do
  case "$1" in
    --pr) PR="$2"; shift 2 ;;
    --label) LABEL="$2"; shift 2 ;;
    --repo) REPO="$2"; shift 2 ;;
    -h|--help)
      grep '^# ' "$0" | sed 's/^# \{0,1\}//'
      exit 0
      ;;
    *) echo "::error::set-review-label: unknown arg: $1" >&2; exit 2 ;;
  esac
done

if [ -z "$PR" ] || [ -z "$LABEL" ]; then
  echo "::error::set-review-label: --pr and --label are required" >&2
  exit 2
fi

# The mutually-exclusive set. Order doesn't matter; we strip everything
# that isn't the target, then add the target.
STATE_LABELS=(
  "review:in-progress"
  "review:outstanding-issues"
  "review:no-blockers"
  "review:stale"
  "review:error"
)

# Validate the target is in the known set so a typo doesn't silently
# create a one-off label.
known=false
for s in "${STATE_LABELS[@]}"; do
  if [ "$s" = "$LABEL" ]; then known=true; break; fi
done
if [ "$known" = "false" ]; then
  echo "::error::set-review-label: '$LABEL' is not in the mutually-exclusive review-state set (${STATE_LABELS[*]})" >&2
  exit 2
fi

REPO_ARG=()
if [ -n "$REPO" ]; then REPO_ARG=(--repo "$REPO"); fi

# Read current labels so we only touch the ones that need to change.
# Wrap commas so a substring match in the loop below doesn't mis-fire
# on a label that's a prefix of another.
CURRENT=$(gh pr view "$PR" "${REPO_ARG[@]}" --json labels --jq '[.labels[].name] | join(",")') || {
  echo "::error::set-review-label: failed to read current labels for PR $PR" >&2
  exit 1
}

REMOVE_ARGS=()
for s in "${STATE_LABELS[@]}"; do
  if [ "$s" = "$LABEL" ]; then continue; fi
  if [[ ",$CURRENT," == *",$s,"* ]]; then
    REMOVE_ARGS+=(--remove-label "$s")
  fi
done

ADD_ARGS=()
if [[ ",$CURRENT," != *",$LABEL,"* ]]; then
  ADD_ARGS+=(--add-label "$LABEL")
fi

if [ "${#REMOVE_ARGS[@]}" -eq 0 ] && [ "${#ADD_ARGS[@]}" -eq 0 ]; then
  echo "set-review-label: PR $PR already at $LABEL; no-op"
  exit 0
fi

if ! gh pr edit "$PR" "${REPO_ARG[@]}" "${ADD_ARGS[@]}" "${REMOVE_ARGS[@]}"; then
  echo "::error::set-review-label: gh pr edit failed for PR $PR (label=$LABEL)" >&2
  exit 1
fi

echo "set-review-label: PR $PR → $LABEL (removed: ${REMOVE_ARGS[*]:-none})"
