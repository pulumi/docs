#!/usr/bin/env python3
"""Filter Vale --output=JSON findings to PR-introduced lines only.

Reads Vale's per-file findings, intersects with line numbers added in this
PR's diff (so pre-existing prose isn't surfaced), caps the result, and emits
a flat JSON list the docs-review skill consumes.

Usage:
    vale-findings-filter.py --pr <PR_NUMBER> --in <vale-raw.json> --out <out.json>

Caps:
    - 10 findings per file
    - 50 findings total

Output schema (flat list, sorted by file then line):
    [
      {"file": "content/docs/foo.md", "line": 42, "rule": "Pulumi.Substitutions",
       "severity": "error", "message": "Use 'select' instead of 'click' ..."},
      ...
    ]

Empty input or empty intersection produces an empty list (`[]`), never errors.
The script does not call any APIs except `gh pr diff` to fetch the patch.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict

PER_FILE_CAP = 10
TOTAL_CAP = 50

DIFF_FILE_RE = re.compile(r"^\+\+\+ b/(.+)$")
HUNK_RE = re.compile(r"^@@ -\d+(?:,\d+)? \+(\d+)(?:,(\d+))? @@")


def added_lines_per_file(patch: str) -> dict[str, set[int]]:
    """Parse a unified diff patch into {filename: {added_line_numbers}}.

    Tracks the new-file line cursor across hunks. Lines beginning with '+'
    (but not '+++') are added; '-' lines don't advance the new cursor; ' '
    (context) lines do.
    """
    result: dict[str, set[int]] = defaultdict(set)
    current_file: str | None = None
    new_line: int = 0
    for raw in patch.splitlines():
        m = DIFF_FILE_RE.match(raw)
        if m:
            current_file = m.group(1)
            continue
        if raw.startswith("--- "):
            continue
        m = HUNK_RE.match(raw)
        if m:
            new_line = int(m.group(1))
            continue
        if current_file is None:
            continue
        if raw.startswith("+") and not raw.startswith("+++"):
            result[current_file].add(new_line)
            new_line += 1
        elif raw.startswith("-") and not raw.startswith("---"):
            pass
        else:
            new_line += 1
    return result


def fetch_pr_patch(pr: str) -> str:
    """Fetch the unified diff for the PR via gh."""
    proc = subprocess.run(
        ["gh", "pr", "diff", pr, "--patch"],
        check=True,
        capture_output=True,
        text=True,
    )
    return proc.stdout


def flatten_vale(raw: dict, allowed_lines: dict[str, set[int]]) -> list[dict]:
    """Convert Vale's {file: [alerts]} to a flat list, intersecting with allowed_lines.

    If allowed_lines is empty for a file, NO findings from that file pass
    through. (This is intentional: a PR can only "introduce" findings on
    lines it added.)
    """
    out: list[dict] = []
    for filename, alerts in raw.items():
        added = allowed_lines.get(filename)
        if not added:
            continue
        for alert in alerts:
            line = alert.get("Line")
            if line is None or line not in added:
                continue
            out.append(
                {
                    "file": filename,
                    "line": line,
                    "rule": alert.get("Check", ""),
                    "severity": alert.get("Severity", ""),
                    "message": alert.get("Message", ""),
                }
            )
    return out


def cap(findings: list[dict]) -> list[dict]:
    """Cap to PER_FILE_CAP per file, then TOTAL_CAP overall."""
    findings.sort(key=lambda f: (f["file"], f["line"]))
    by_file: dict[str, list[dict]] = defaultdict(list)
    for f in findings:
        by_file[f["file"]].append(f)
    capped: list[dict] = []
    for filename in sorted(by_file):
        capped.extend(by_file[filename][:PER_FILE_CAP])
    return capped[:TOTAL_CAP]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pr", required=True)
    parser.add_argument("--in", dest="infile", required=True)
    parser.add_argument("--out", dest="outfile", required=True)
    args = parser.parse_args()

    with open(args.infile) as f:
        raw = json.load(f) or {}

    if not raw:
        with open(args.outfile, "w") as f:
            json.dump([], f)
        return 0

    patch = fetch_pr_patch(args.pr)
    allowed = added_lines_per_file(patch)
    findings = cap(flatten_vale(raw, allowed))

    with open(args.outfile, "w") as f:
        json.dump(findings, f, indent=2)
    print(f"vale-findings-filter: wrote {len(findings)} findings to {args.outfile}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
