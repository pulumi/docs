#!/usr/bin/env bash
#
# assert-head-tag.sh — CI guard for inject-version-switcher.sh.
#
# inject-version-switcher.sh inserts the selector loader before the first </head>
# (falling back to </body>). This assertion keeps that invariant honest across the four
# generator dialects: every generated HTML page must offer an injection point. It fails
# if any page has neither </head> nor </body>, and reports how many pages lack </head>
# so a silent template change in any generator is visible in CI.
#
# Usage: assert-head-tag.sh <generated-html-dir>
#
set -euo pipefail

SRC="${1:-}"
[[ -d "$SRC" ]] || { echo "assert-head-tag: dir not found: $SRC" >&2; exit 2; }

total=0; no_head=0; no_anchor=0
while IFS= read -r -d '' f; do
  total=$((total + 1))
  if ! grep -iqo '</head>' "$f"; then
    no_head=$((no_head + 1))
    if ! grep -iqo '</body>' "$f"; then
      echo "assert-head-tag: NO INJECTION POINT (no </head> or </body>): $f" >&2
      no_anchor=$((no_anchor + 1))
    fi
  fi
done < <(find "$SRC" -type f -name '*.html' -print0)

echo "assert-head-tag: checked=$total without_head=$no_head without_any_anchor=$no_anchor"
[[ "$total" -gt 0 ]]     || { echo "assert-head-tag: FAILED — no HTML files found under $SRC" >&2; exit 1; }
[[ "$no_anchor" -eq 0 ]] || { echo "assert-head-tag: FAILED — $no_anchor file(s) have no injection point" >&2; exit 1; }
