#!/usr/bin/env python3
"""strip-empty-triaged.py — remove the 📋 Triaged section when it's still empty.

The composer (`compose-review.py:render_triaged`) always emits a 📋 section
wrapped in a collapsed `<details>` block with `_No triaged findings._` as the
placeholder. During the editorial pass the reviewer can move `**Spurious:**`
or `**Mis-sourced:**` bullets out of 🚨 / ⚠️ and into this section, REPLACING
the placeholder. If the reviewer doesn't move any bullets in, the placeholder
survives — and a section that says "I double-checked these…" with nothing
to expand is just visual noise.

This script runs in the post-edit chain between Step D (re-validate) and
Step E (upsert pinned comment). If the section's `<details>` block still
contains the literal `_No triaged findings._` marker, the entire section
(heading through closing `</details>` + trailing blank line) is removed.
If the marker is gone (reviewer added real bullets), the script is a no-op.
Idempotent — running twice is safe.

The 📋 section is NOT in `MANDATORY_H3_SECTIONS` (validate-pinned.py:113),
so stripping it doesn't violate any structural rule. The composer
re-renders it on the next review run.

Usage:
  strip-empty-triaged.py --body-file PATH
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

EMPTY_MARKER = "_No triaged findings._"
HEADING = "### 📋 Triaged verifier findings"

# Match the whole 📋 section: heading + (blank lines + content) up to the
# next H3 heading or end-of-file. The trailing blank line(s) before the
# next heading are absorbed into the match so removal leaves clean output.
SECTION_RE = re.compile(
    r"^### 📋 Triaged verifier findings\n.*?(?=^### |\Z)",
    re.DOTALL | re.MULTILINE,
)


def strip_empty_triaged(body: str) -> tuple[str, bool]:
    """Return (new_body, stripped). `stripped` is True iff the section was removed."""
    m = SECTION_RE.search(body)
    if not m:
        # No 📋 section present — nothing to do.
        return body, False
    section = m.group(0)
    if EMPTY_MARKER not in section:
        # Reviewer moved real bullets in; the section now has content.
        return body, False
    new_body = body[: m.start()] + body[m.end() :]
    # Collapse any double-blank-line left behind by the removal so the
    # body stays tidy.
    new_body = re.sub(r"\n{3,}", "\n\n", new_body)
    return new_body, True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--body-file", required=True, help="Path to the review body to edit in place.")
    args = ap.parse_args()

    path = Path(args.body_file)
    if not path.exists():
        print(f"::error::strip-empty-triaged: body file not found: {path}", file=sys.stderr)
        return 1
    body = path.read_text(encoding="utf-8")
    new_body, stripped = strip_empty_triaged(body)
    if stripped:
        path.write_text(new_body, encoding="utf-8")
        print(f"strip-empty-triaged: 📋 section was empty; removed from {path}")
    else:
        print(f"strip-empty-triaged: 📋 section absent or non-empty; no-op on {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
