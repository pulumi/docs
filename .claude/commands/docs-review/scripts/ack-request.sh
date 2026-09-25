#!/usr/bin/env bash
# ack-request.sh — acknowledge a review request on the comment that asked
# for it, instead of adding comments to the PR timeline.
#
# A requested refresh used to cost the timeline two comments: a "Working on
# it" spinner while the run went, then a `🤖 Review updated on @<author>'s
# request.` when it finished. On a busy PR those stacked up (six on
# pulumi/docs#21871) and buried the cards and the re-request button, and
# the spinner notified every subscriber even though it was deleted minutes
# later. The card itself is the record of what changed; the requester only
# needs to know their request was picked up and then landed. Reactions on
# the triggering comment say both without a comment:
#
#   --start   👀 while the run works. Exits 1 when there is nothing to react
#             to or the call failed, so the caller posts its spinner
#             comment instead — the requester must see *something*.
#   --clear   remove this token's 👀 (a run that errored, was superseded,
#             or was skipped). The caller posts any error message itself.
#   (default) done: remove the 👀, add 🚀. Falls back to posting --message
#             as a comment when there's no target or the reaction fails.
#
# The fallbacks exist because a submitted review body can't take a reaction
# through the API, and a run dispatched without a target (a manual
# workflow_dispatch) has nothing to react to.
#
# Usage:
#   ack-request.sh [--start|--clear] --pr 123 --target issues/comments/456 \
#     [--message "…"] [--repo owner/repo]
#
# --target is the comment's API path under repos/<repo>/ —
# `issues/comments/<id>` (a PR conversation comment) or
# `pulls/comments/<id>` (an inline review comment). Empty means "no
# reaction target". An empty --message with an empty --target is a no-op.
#
# Only this token's own 👀 is removed: ACK_BOT_LOGIN (default
# github-actions[bot], the GITHUB_TOKEN identity) names it. A human's 👀 on
# the same comment is left alone.

set -uo pipefail

MODE=done
PR=""
TARGET=""
MESSAGE=""
REPO="${GITHUB_REPOSITORY:-}"
BOT_LOGIN="${ACK_BOT_LOGIN:-github-actions[bot]}"

while [ $# -gt 0 ]; do
  case "$1" in
    --start) MODE=start; shift ;;
    --clear) MODE=clear; shift ;;
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

clear_eyes() {
  [ -n "$TARGET" ] || return 0
  local ids rid
  ids=$(gh api "repos/$REPO/$TARGET/reactions?content=eyes" \
    --jq ".[] | select(.user.login == \"$BOT_LOGIN\") | .id" 2>/dev/null) || return 0
  for rid in $ids; do
    gh api -X DELETE "repos/$REPO/$TARGET/reactions/$rid" >/dev/null 2>&1 || true
  done
}

case "$MODE" in
  start)
    if [ -n "$TARGET" ] \
       && gh api -X POST "repos/$REPO/$TARGET/reactions" -f content=eyes >/dev/null 2>&1; then
      echo "marked $TARGET as picked up"
      exit 0
    fi
    exit 1
    ;;
  clear)
    clear_eyes
    exit 0
    ;;
esac

clear_eyes
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
