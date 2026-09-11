#!/usr/bin/env bash
# Poll PR 21563 until its v3 author card lands (exit 0), review:error (1), or timeout (2).
pr="${1:-21563}"
want="${2:-}"
for i in $(seq 1 9); do
  sleep 60
  labels=$(gh pr view "$pr" --repo pulumi/docs --json labels --jq '[.labels[].name] | join(",")')
  header=$(gh api "repos/pulumi/docs/issues/$pr/comments" --jq '.[] | select(.body | test("CLAUDE_REVIEW_AUTHOR")) | .body' | grep -m1 '^## Author')
  echo "$i: $labels | $header"
  case "$labels" in *review:error*) exit 1 ;; esac
  if [ -n "$header" ]; then
    if [ -z "$want" ] || echo "$header" | grep -q -- "$want"; then exit 0; fi
  fi
done
exit 2
