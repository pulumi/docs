#!/bin/bash
# Auto-apply deterministic trivial fixes to changed content files
# Usage: ./auto-trivials.sh <AI_SUSPECT> <file1> [file2 ...]
#
# Outputs (key=value pairs on stderr; modifies files in place):
#   AUTO_TRIVIALS=applied|skipped|none
#   AUTO_TRIVIALS_SUMMARY=<one-line summary>
#   AUTO_TRIVIALS_COUNT_TRAILING_WS=N
#   AUTO_TRIVIALS_COUNT_EOF_NEWLINE=N
#   AUTO_TRIVIALS_COUNT_HEADING_CASE=N
#
# Refuses to run if AI_SUSPECT=true.
#
# Trivial fix set (deterministic, reversible):
#   - Trailing whitespace removal (.md only)
#   - Missing EOF newlines (.md only)
#   - Sentence-case H2/H3/H4 (per STYLE-GUIDE.md)
#
# More sophisticated fixes (typo correction, missing aliases, language specifiers)
# require either an oracle word list or git-history inspection — they live in the
# main pr-review workflow rather than this deterministic script.

set -e

if [ -z "$1" ]; then
  echo "Error: AI_SUSPECT flag required" >&2
  echo "Usage: $0 <AI_SUSPECT> <file1> [file2 ...]" >&2
  exit 1
fi

AI_SUSPECT="$1"
shift

if [ "$AI_SUSPECT" = "true" ]; then
  echo "AUTO_TRIVIALS=skipped" >&2
  echo "AUTO_TRIVIALS_SUMMARY=auto-trivials disabled (AI-suspect — manual review required)" >&2
  exit 0
fi

if [ "$#" -eq 0 ]; then
  echo "AUTO_TRIVIALS=none" >&2
  echo "AUTO_TRIVIALS_SUMMARY=no files supplied" >&2
  exit 0
fi

TRAILING_WS=0
EOF_NEWLINE=0
HEADING_CASE=0

# Title-case → sentence-case detector for H2/H3/H4.
# Heuristic: if every word in the heading except articles/prepositions starts uppercase,
# downcase all but the first word. Skip if heading contains acronyms (3+ consecutive uppercase
# letters), code, links, or already starts with a lowercase word.
fix_heading_case() {
  local file="$1"
  python3 - "$file" <<'PYEOF'
import re
import sys

path = sys.argv[1]
with open(path, 'r', encoding='utf-8') as fh:
    lines = fh.readlines()

heading_re = re.compile(r'^(#{2,4})\s+(.+?)\s*$')
acronym_re = re.compile(r'[A-Z]{3,}')
code_re = re.compile(r'`[^`]+`')
link_re = re.compile(r'\[[^\]]+\]\([^)]+\)')

# Words that should remain lowercase mid-heading in sentence case.
SMALL = {'a','an','and','as','at','but','by','for','if','in','nor','of','on','or','per','the','to','vs','via','with'}

changes = 0
out = []
for line in lines:
    m = heading_re.match(line)
    if not m:
        out.append(line)
        continue
    hashes, text = m.group(1), m.group(2)

    # Skip protected headings
    if acronym_re.search(text) or code_re.search(text) or link_re.search(text):
        out.append(line)
        continue

    words = text.split()
    if len(words) < 2:
        out.append(line)
        continue

    # Detect title case: first letter of every "significant" word is uppercase
    significant = [w for w in words if w.lower() not in SMALL]
    if not significant or not all(w[0:1].isupper() for w in significant):
        out.append(line)
        continue

    # Already sentence case if only the first word is capitalized and the rest are lower
    rest = words[1:]
    rest_significant = [w for w in rest if w.lower() not in SMALL]
    if all(w[0:1].islower() for w in rest_significant):
        out.append(line)
        continue

    # Convert to sentence case: capitalize first word, lowercase rest (preserving small-word rule which is lowercase anyway)
    new_words = [words[0][0:1].upper() + words[0][1:]]
    for w in words[1:]:
        new_words.append(w.lower())

    new_line = f"{hashes} {' '.join(new_words)}\n"
    if new_line != line:
        changes += 1
        out.append(new_line)
    else:
        out.append(line)

if changes > 0:
    with open(path, 'w', encoding='utf-8') as fh:
        fh.writelines(out)

print(changes)
PYEOF
}

for file in "$@"; do
  # Only operate on .md files that exist
  if [ ! -f "$file" ]; then
    continue
  fi
  case "$file" in
    *.md) ;;
    *) continue ;;
  esac

  # --- Trailing whitespace ---
  WS_BEFORE=$(grep -c '[[:space:]]$' "$file" 2>/dev/null || true)
  WS_BEFORE=${WS_BEFORE:-0}
  if [ "$WS_BEFORE" -gt 0 ]; then
    sed -i 's/[[:space:]]*$//' "$file"
    TRAILING_WS=$((TRAILING_WS + WS_BEFORE))
  fi

  # --- Missing EOF newline ---
  if [ -s "$file" ] && [ "$(tail -c 1 "$file" | wc -l)" -eq 0 ]; then
    printf '\n' >> "$file"
    EOF_NEWLINE=$((EOF_NEWLINE + 1))
  fi

  # --- Sentence-case H2/H3/H4 ---
  if command -v python3 >/dev/null 2>&1; then
    HC=$(fix_heading_case "$file")
    HC=${HC:-0}
    HEADING_CASE=$((HEADING_CASE + HC))
  fi
done

TOTAL=$((TRAILING_WS + EOF_NEWLINE + HEADING_CASE))

echo "AUTO_TRIVIALS_COUNT_TRAILING_WS=$TRAILING_WS" >&2
echo "AUTO_TRIVIALS_COUNT_EOF_NEWLINE=$EOF_NEWLINE" >&2
echo "AUTO_TRIVIALS_COUNT_HEADING_CASE=$HEADING_CASE" >&2

if [ "$TOTAL" -eq 0 ]; then
  echo "AUTO_TRIVIALS=none" >&2
  echo "AUTO_TRIVIALS_SUMMARY=no trivial fixes needed" >&2
else
  PARTS=()
  [ "$TRAILING_WS" -gt 0 ] && PARTS+=("$TRAILING_WS trailing-ws")
  [ "$EOF_NEWLINE" -gt 0 ] && PARTS+=("$EOF_NEWLINE EOF newlines")
  [ "$HEADING_CASE" -gt 0 ] && PARTS+=("$HEADING_CASE heading-case")
  # Join parts with " · " (IFS only takes the first character, so build manually)
  SUMMARY="${PARTS[0]}"
  for p in "${PARTS[@]:1}"; do
    SUMMARY="$SUMMARY · $p"
  done
  echo "AUTO_TRIVIALS=applied" >&2
  echo "AUTO_TRIVIALS_SUMMARY=$TOTAL trivial fixes: $SUMMARY" >&2
fi
