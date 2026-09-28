#!/usr/bin/env bash
# with-pr-files.sh — swap a PR JSON's `files` for the full, paginated list.
#
# Usage: gh pr view N --json ... | with-pr-files.sh --repo OWNER/NAME --pr N > out.json
#
# `gh pr view --json files` is one GraphQL page: 100 files, silently. On
# #21936 (1,156 files) that made triage's oversized comment say "100 files",
# left the classifier's 150-file axis unreachable, and classified domains from
# the first 100 paths. The REST list pages (up to 3,000); this swaps it in,
# same {path, additions, deletions} shape.
#
# The list never travels through argv. Linux caps a single argument at
# 128 KiB (MAX_ARG_STRLEN), and `jq --argjson f "$FILES"` over ~1,000 files
# fails with "Argument list too long" — which, under `set -e` and
# `continue-on-error`, left triage green with no `review:oversized` label.
# The list goes to a temp file and into jq with --slurpfile.
#
# Degrades to the input unchanged when the REST read fails or comes back
# empty, so a caller is never worse off than with the 100-file page.
set -euo pipefail

REPO="" PR=""
while [ $# -gt 0 ]; do
  case "$1" in
    --repo) REPO="$2"; shift 2 ;;
    --pr) PR="$2"; shift 2 ;;
    *) echo "with-pr-files.sh: unknown argument $1" >&2; exit 2 ;;
  esac
done
[ -n "$REPO" ] && [ -n "$PR" ] || { echo "with-pr-files.sh: --repo and --pr are required" >&2; exit 2; }

IN=$(mktemp)
FILES=$(mktemp)
trap 'rm -f "$IN" "$FILES"' EXIT
cat > "$IN"

if gh api --paginate "repos/$REPO/pulls/$PR/files" \
     --jq '.[] | {path: .filename, additions, deletions}' 2>/dev/null \
   | jq -s . > "$FILES" 2>/dev/null \
   && [ "$(jq 'length' "$FILES" 2>/dev/null || echo 0)" -gt 0 ]; then
  jq --slurpfile f "$FILES" '.files = $f[0]' "$IN"
else
  echo "with-pr-files.sh: paginated file list unavailable for #$PR; keeping gh pr view's files" >&2
  cat "$IN"
fi
