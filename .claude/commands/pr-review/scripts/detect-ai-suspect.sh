#!/bin/bash
# AI-Suspect Detection
# Usage: ./detect-ai-suspect.sh <PR_NUMBER> [--ai|--no-ai]
#
# Outputs (key=value pairs on stdout):
#   AI_SUSPECT=true|false
#   AI_SUSPECT_REASONS=reason1,reason2,...
#
# Detection signals (any one triggers the flag):
#   1. Local allowlist at ~/.claude/pr-review/ai-suspect-authors.txt
#   2. AI authoring trailers in PR body or commit messages
#   3. AI prose-pattern density on the diff
#   4. Manual override via --ai / --no-ai
#
# See references/trust-and-scrutiny.md for the full spec.

set -e

if [ -z "$1" ]; then
  echo "Error: PR number required" >&2
  echo "Usage: $0 <PR_NUMBER> [--ai|--no-ai]" >&2
  exit 1
fi

PR_NUMBER="$1"
MANUAL_OVERRIDE="${2:-}"

ALLOWLIST_FILE="$HOME/.claude/pr-review/ai-suspect-authors.txt"
REASONS=()

# --- Manual override always wins ---
if [ "$MANUAL_OVERRIDE" = "--no-ai" ]; then
  echo "AI_SUSPECT=false"
  echo "AI_SUSPECT_REASONS=manual:no-ai"
  exit 0
fi

if [ "$MANUAL_OVERRIDE" = "--ai" ]; then
  echo "AI_SUSPECT=true"
  echo "AI_SUSPECT_REASONS=manual"
  exit 0
fi

# --- Fetch PR data once ---
PR_DATA=$(gh pr view "$PR_NUMBER" --json author,body,commits,files 2>/dev/null || echo "{}")
AUTHOR=$(echo "$PR_DATA" | jq -r '.author.login // empty')

# --- Signal 1: Local allowlist ---
if [ -n "$AUTHOR" ] && [ -f "$ALLOWLIST_FILE" ]; then
  # Match author against non-comment, non-blank lines
  if grep -E "^[[:space:]]*${AUTHOR}[[:space:]]*$" "$ALLOWLIST_FILE" >/dev/null 2>&1; then
    REASONS+=("allowlist")
  fi
fi

# --- Signal 2: Trailer detection ---
# Concatenate PR body + all commit messages, search for known AI markers
HAYSTACK=$(echo "$PR_DATA" | jq -r '
  (.body // "") + "\n" +
  ((.commits // []) | map(.messageHeadline + "\n" + (.messageBody // "")) | join("\n"))
' 2>/dev/null || echo "")

trailer_check() {
  local pattern="$1"
  local label="$2"
  if echo "$HAYSTACK" | grep -qiE "$pattern"; then
    REASONS+=("trailer:$label")
    return 0
  fi
  return 1
}

trailer_check 'Co-Authored-By:[[:space:]]*Claude' 'claude' || true
trailer_check 'Generated with[[:space:]]*\[?Claude Code' 'claude-code' || true
trailer_check 'noreply@anthropic\.com' 'anthropic' || true
trailer_check 'Co-Authored-By:[[:space:]]*Cursor' 'cursor' || true
trailer_check 'Co-Authored-By:[[:space:]]*(GitHub )?Copilot' 'copilot' || true
trailer_check '🤖 Generated with' 'robot-emoji' || true

# Dedupe trailer reasons (a PR with multiple Claude trailers shouldn't list it 5 times)
if [ ${#REASONS[@]} -gt 0 ]; then
  IFS=$'\n' REASONS=($(printf '%s\n' "${REASONS[@]}" | awk '!seen[$0]++'))
  unset IFS
fi

# --- Signal 3: Prose pattern density on the diff ---
# Skip if we've already flagged via signals 1 or 2 (saves a diff fetch)
if [ ${#REASONS[@]} -eq 0 ]; then
  DIFF=$(gh pr diff "$PR_NUMBER" 2>/dev/null || echo "")

  # Extract added prose lines from .md files only.
  # Filter out:
  #   - diff/file headers
  #   - frontmatter blocks (between --- markers, only at file start)
  #   - fenced code block contents
  #
  # The frontmatter tracker is gated on `seen_content`: it only counts the first
  # pair of `---` markers, before any other content has been seen for the file.
  # Otherwise a Markdown horizontal rule (`---`) mid-file would flip the state
  # and cause us to drop real prose lines.
  ADDED_PROSE=$(echo "$DIFF" | awk '
    /^diff --git/ {
      in_md = ($0 ~ /\.md b\/.*\.md$/)
      in_fence = 0
      in_frontmatter = 0
      seen_content = 0
      next
    }
    !in_md { next }
    /^@@/ { next }
    /^\+\+\+/ || (/^---/ && !/^---[[:space:]]*$/) { next }

    # Track fenced code blocks (only on added/context lines)
    /^[+ ]```/ {
      in_fence = !in_fence
      seen_content = 1
      next
    }
    in_fence { next }

    # Track frontmatter — only the very first --- pair, before any content
    /^[+ ]---[[:space:]]*$/ {
      if (!seen_content) {
        in_frontmatter = !in_frontmatter
        if (!in_frontmatter) seen_content = 1
        next
      }
    }
    in_frontmatter { next }

    # Added prose line
    /^\+/ {
      sub(/^\+/, "")
      seen_content = 1
      print
    }

    # Mark non-blank context lines as content too
    /^ [^[:space:]]/ { seen_content = 1 }
  ')

  if [ -n "$ADDED_PROSE" ]; then
    LINE_COUNT=$(echo "$ADDED_PROSE" | wc -l)
    WORD_COUNT=$(echo "$ADDED_PROSE" | wc -w)

    # Need at least 10 added prose lines to avoid false positives on tiny diffs
    if [ "$LINE_COUNT" -ge 10 ] && [ "$WORD_COUNT" -gt 50 ]; then
      # Em-dash density: count of — divided by word count
      EM_DASH_COUNT=$(echo "$ADDED_PROSE" | grep -o '—' | wc -l)
      EM_DASH_DENSITY=$(awk -v c="$EM_DASH_COUNT" -v w="$WORD_COUNT" 'BEGIN { printf "%.6f", c/w }')
      EM_DASH_THRESHOLD=0.015
      if awk -v d="$EM_DASH_DENSITY" -v t="$EM_DASH_THRESHOLD" 'BEGIN { exit !(d > t) }'; then
        REASONS+=("prose-pattern:em-dash")
      fi

      # Contrastive constructions: "not X — Y", "not X, but Y", "It's not X, it's Y"
      CONTRASTIVE_COUNT=$(echo "$ADDED_PROSE" | grep -ciE "(not [a-z]+,? (but|—|it's))" || true)
      # Approximate paragraph count (blank-line separated). Diffs lose blank-line structure
      # so we approximate as "every 4 lines = a paragraph".
      PARA_COUNT=$(( LINE_COUNT / 4 ))
      [ "$PARA_COUNT" -lt 1 ] && PARA_COUNT=1
      if [ "$CONTRASTIVE_COUNT" -gt 0 ] && [ "$(( CONTRASTIVE_COUNT * 3 ))" -gt "$PARA_COUNT" ]; then
        REASONS+=("prose-pattern:contrastive")
      fi

      # Hedge density
      HEDGE_COUNT=$(echo "$ADDED_PROSE" | grep -ciE '\b(generally|typically|tends to|can often|may sometimes|in many cases|it.{1,3}s worth noting|it.{1,3}s important to note)\b' || true)
      HEDGE_DENSITY=$(awk -v c="$HEDGE_COUNT" -v w="$WORD_COUNT" 'BEGIN { printf "%.6f", c/w }')
      HEDGE_THRESHOLD=0.012
      if awk -v d="$HEDGE_DENSITY" -v t="$HEDGE_THRESHOLD" 'BEGIN { exit !(d > t) }'; then
        REASONS+=("prose-pattern:hedge")
      fi
    fi
  fi
fi

# --- Final output ---
if [ ${#REASONS[@]} -gt 0 ]; then
  echo "AI_SUSPECT=true"
  # Join reasons with commas
  printf 'AI_SUSPECT_REASONS='
  printf '%s' "${REASONS[0]}"
  for r in "${REASONS[@]:1}"; do
    printf ',%s' "$r"
  done
  printf '\n'
else
  echo "AI_SUSPECT=false"
  echo "AI_SUSPECT_REASONS="
fi
