#!/usr/bin/env bash
# ack-request.sh — acknowledge a finished review request on the comment
# that asked for it, instead of adding a comment to the PR timeline.
#
# A successful `#update-review` / `#new-review` used to end with a fresh
# `🤖 Review updated on @<author>'s request.` comment. On a busy PR those
# stacked up (six on pulumi/docs#21871) and buried the cards and the
# re-request button under timeline noise. The card itself is the record of
# what changed; the requester only needs to know their request landed. A
# 🚀 reaction on the triggering comment says that without a new comment.
#
# The fallback keeps the old comment: a submitted review body can't take a
# reaction through the API, and a run dispatched without a target (older
# dispatchers, a manual workflow_dispatch) has nothing to react to. A
# failed reaction call falls back too — the requester must never be left
# without any signal.
#
# Usage:
#   ack-request.sh --pr 123 --target issues/comments/456 --message "…" [--repo owner/repo]
#
# --target is the comment's API path under repos/<repo>/ —
# `issues/comments/<id>` (a PR conversation comment) or
# `pulls/comments/<id>` (an inline review comment). Empty means "no
# reaction target": post --message as a CLAUDE_PROGRESS comment instead.
# An empty --message with an empty --target is a no-op.

set -uo pipefail

PR=""
TARGET=""
MESSAGE=""
REPO="${GITHUB_REPOSITORY:-}"

while [ $# -gt 0 ]; do
  case "$1" in
    --pr) PR="$2"; shift 2 ;;
    --target) TARGET="$2"; shift 2 ;;
    --message) MESSAGE="$2"; shift 2 ;;
    --repo) REPO="$2"; shift 2 ;;
    *) echo "ack-request.sh: unknown argument: $1" >&2; exit 2 ;;
  esac
done

if [ -z "$PR" ] || [ -z "$REPO" ]; then
  echo "ack-request.sh: --pr and --repo (or GITHUB_REPOSITORY) are required" >&2
  exit 2
fi

case "$TARGET" in
  "" ) ;;
  issues/comments/[0-9]*|pulls/comments/[0-9]*) ;;
  *) echo "ack-request.sh: ignoring malformed --target '$TARGET'" >&2; TARGET="" ;;
esac

if [ -n "$TARGET" ]; then
  if gh api -X POST "repos/$REPO/$TARGET/reactions" -f content=rocket >/dev/null 2>&1; then
    echo "acknowledged with a reaction on $TARGET"
    exit 0
  fi
  echo "reaction on $TARGET failed; falling back to a comment" >&2
fi

if [ -n "$MESSAGE" ]; then
  BODY=$(printf '<!-- CLAUDE_PROGRESS -->\n%s' "$MESSAGE")
  gh api "repos/$REPO/issues/$PR/comments" -f body="$BODY" >/dev/null || true
fi
exit 0
