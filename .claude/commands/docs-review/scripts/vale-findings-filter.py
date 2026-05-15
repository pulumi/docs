#!/usr/bin/env python3
"""Filter Vale --output=JSON findings to PR-introduced lines only.

Reads Vale's per-file findings, intersects with line numbers added in this
PR's diff (so pre-existing prose isn't surfaced), caps the result, and emits
a flat JSON list the docs-review skill consumes.

Usage:
    vale-findings-filter.py --pr <PR_NUMBER> --in <vale-raw.json> --out <out.json>
    vale-findings-filter.py --in <vale-raw.json> --out <out.json>     # local mode

CI passes --pr to intersect with PR-added lines. Interactive `/docs-review`
omits --pr; the filter then categorizes and caps without diff filtering.

Caps:
    - 10 findings per file
    - 50 findings total

Output schema (flat list, sorted by file then line):
    [
      {"file": "content/docs/foo.md", "line": 42,
       "rule": "Pulumi.Substitutions", "category": "substitution",
       "severity": "error", "message": "Use 'select' instead of 'click' ..."},
      ...
    ]

`rule` is retained for CI logs / debugging. PR-facing surfaces (pinned
review, TRIAGE_PROSE comment) render `category` instead — keeps the linter
implementation out of user-facing prose. `category` is derived from
`RULE_CATEGORIES`; unmapped rules fall back to "style".

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

# Maps Vale rule names to tool-agnostic categories rendered in PR-facing
# copy. The single source of truth — both CI (--pr) and interactive (no --pr)
# pipe through this filter, so the model never has to know the rules.
# Unmapped rules fall back to "style".
RULE_CATEGORIES: dict[str, str] = {
    "Pulumi.Substitutions": "substitution",
    "Pulumi.Nomenclature": "nomenclature",
    "Pulumi.BannedWords": "inclusive language",
    "Pulumi.Difficulty": "difficulty qualifier",
    "Pulumi.PoliciesSingular": "agreement",
    "Pulumi.SetPieceTransitions": "set-piece transition",
    "Pulumi.EmDashDensity": "em-dash density",
    "Pulumi.ListicleH2Headings": "listicle heading",
    "Pulumi.HedgeThenPivot": "hedge-then-pivot",
    "Pulumi.DirectionalReferences": "directional reference",
    "Pulumi.LinkText": "vague link text",
    "Pulumi.EmptyAltText": "empty alt text",
    "Pulumi.CommandBackticks": "unbacked CLI command",
    "Pulumi.Repetition": "repeated word",
    "Google.Acronyms": "acronym",
    "Google.Contractions": "contractions",
    "Google.Ellipses": "punctuation",
    "Google.Exclamation": "tone",
    "Google.FirstPerson": "first person",
    "Google.GenderBias": "inclusive language",
    "Google.Latin": "latinism",
    "Google.LyHyphens": "hyphenation",
    "Google.OptionalPlurals": "plurals",
    "Google.OxfordComma": "punctuation",
    "Google.Passive": "passive voice",
    "Google.Periods": "punctuation",
    "Google.Quotes": "punctuation",
    "Google.Ranges": "ranges",
    "Google.Semicolons": "punctuation",
    "Google.Slang": "tone",
    "Google.Spacing": "spacing",
    "Google.Spelling": "spelling",
    "Google.Units": "units",
    "write-good.Cliches": "cliché",
    "write-good.So": "filler",
    "write-good.ThereIs": "filler",
    "write-good.TooWordy": "wordiness",
    "write-good.Weasel": "weasel word",
}


def category_for(rule: str) -> str:
    return RULE_CATEGORIES.get(rule, "style")

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


def flatten_vale(raw: dict, allowed_lines: dict[str, set[int]] | None) -> list[dict]:
    """Convert Vale's {file: [alerts]} to a flat, categorized list.

    `allowed_lines=None` means "accept all findings" — used by the interactive
    `/docs-review` path that has no PR diff. With a dict, only findings on
    PR-added lines pass through; an empty set for a file drops all of its
    findings (a PR can only "introduce" findings on lines it added).
    """
    out: list[dict] = []
    for filename, alerts in raw.items():
        if allowed_lines is not None:
            added = allowed_lines.get(filename)
            if not added:
                continue
        else:
            added = None
        for alert in alerts:
            line = alert.get("Line")
            if line is None:
                continue
            if added is not None and line not in added:
                continue
            rule = alert.get("Check", "")
            out.append(
                {
                    "file": filename,
                    "line": line,
                    "rule": rule,
                    "category": category_for(rule),
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
    parser.add_argument(
        "--pr",
        help="PR number for line-intersection. Omit for local mode "
        "(interactive /docs-review): all findings pass through, categorized "
        "and capped, no PR diff fetched.",
    )
    parser.add_argument("--in", dest="infile", required=True)
    parser.add_argument("--out", dest="outfile", required=True)
    args = parser.parse_args()

    with open(args.infile) as f:
        raw = json.load(f) or {}

    if not raw:
        with open(args.outfile, "w") as f:
            json.dump([], f)
        return 0

    if args.pr:
        patch = fetch_pr_patch(args.pr)
        allowed = added_lines_per_file(patch)
    else:
        allowed = None
    findings = cap(flatten_vale(raw, allowed))

    with open(args.outfile, "w") as f:
        json.dump(findings, f, indent=2)
    print(f"vale-findings-filter: wrote {len(findings)} findings to {args.outfile}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
