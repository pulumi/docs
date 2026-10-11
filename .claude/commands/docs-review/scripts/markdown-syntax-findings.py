#!/usr/bin/env python3
"""Scan markdown source for syntax-level style issues Vale can't see.

Vale processes markdown to HTML before applying rules, so bracket and
exclamation-mark constructions (`[here](url)`, `![](url)`) are gone before
tokens match. This script scans the *raw* markdown for those constructions
and emits findings in Vale's native JSON shape, so they can be merged into
`.vale-raw.json` before `vale-findings-filter.py` runs.

Detects:
    - Pulumi.EmptyAltText    — `![](...)` or `![ ](...)` (missing alt text)
    - Pulumi.LinkText        — `[here](...)`, `[this](...)`, `[click here](...)`,
                               `[read more](...)`, `[more](...)`,
                               `[click for more](...)` (vague link text)

Lines inside fenced code blocks (``` ... ```) are skipped — code samples
that show these constructions verbatim aren't style violations.

Usage:
    markdown-syntax-findings.py file1.md file2.md ...

Output (stdout, JSON): {"path/to/file.md": [{"Check": ..., "Line": ..., ...}, ...]}

Empty input or no findings produces `{}`. The script does no diff-aware
filtering — that's `vale-findings-filter.py`'s job downstream.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict

# Regexes target raw markdown source. `re.IGNORECASE` for link-text matches
# so "[Click Here]" and "[CLICK HERE]" surface too.
EMPTY_ALT_RE = re.compile(r"!\[\s*\]\(")
LINK_TEXT_RE = re.compile(
    r"\[\s*(?P<text>click\s+here|read\s+more|click\s+for\s+more|here|this|more)\s*\]\(",
    re.IGNORECASE,
)

FENCE_RE = re.compile(r"^\s{0,3}(```|~~~)")


def scan(path: str) -> list[dict]:
    """Return Vale-shaped alerts for syntax-level findings in `path`."""
    alerts: list[dict] = []
    try:
        with open(path, encoding="utf-8") as f:
            lines = f.readlines()
    except (OSError, UnicodeDecodeError):
        return alerts

    in_fence = False
    for lineno, raw in enumerate(lines, start=1):
        if FENCE_RE.match(raw):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        for m in EMPTY_ALT_RE.finditer(raw):
            alerts.append(
                {
                    "Check": "Pulumi.EmptyAltText",
                    "Line": lineno,
                    "Severity": "warning",
                    "Match": m.group(0),
                    "Message": (
                        f"Empty alt text on image ('{m.group(0)}'). "
                        "Provide descriptive alt text for screen readers "
                        "(STYLE-GUIDE.md §Images and Media)."
                    ),
                    "Span": [m.start() + 1, m.end()],
                }
            )

        for m in LINK_TEXT_RE.finditer(raw):
            alerts.append(
                {
                    "Check": "Pulumi.LinkText",
                    "Line": lineno,
                    "Severity": "warning",
                    "Match": m.group(0),
                    "Message": (
                        f"Vague link text ('{m.group('text')}'). "
                        "Use descriptive text that conveys the destination "
                        "(STYLE-GUIDE.md §Links)."
                    ),
                    "Span": [m.start() + 1, m.end()],
                }
            )

    return alerts


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("paths", nargs="+", help="Markdown files to scan")
    args = ap.parse_args()

    result: dict[str, list[dict]] = defaultdict(list)
    for p in args.paths:
        alerts = scan(p)
        if alerts:
            result[p] = alerts

    json.dump(result, sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
