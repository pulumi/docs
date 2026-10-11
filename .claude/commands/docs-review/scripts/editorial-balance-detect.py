#!/usr/bin/env python3
"""editorial-balance-detect.py — Tier 1 deterministic detector for blog editorial balance.

Architectural mirror of `vale-findings-filter.py` and `extract-urls-and-fetch.py`:
a workflow pre-step that pre-computes the mechanical parts of the editorial-
balance pass so the model can render rich-form / empty-form deterministically
instead of computing stats inline.

Tier split (per `docs-review:references:blog` §Priority 2.5):

    Tier 1 (this script): listicle / FAQ trigger; section-depth stats; outlier
                          flag (section ≥3× median); arithmetic threshold flags.
    Tier 2 (model-side):  comparison trigger via canonical entity list, whole-
                          word entity counting, recommendation-steering verbs,
                          FAQ-answer voting.
    Tier 3 (model-side):  don't-flag exceptions ("single-subject feature
                          announcement w/ parenthetical competitor mention,"
                          "intentionally asymmetric framing").

Usage:
    editorial-balance-detect.py --pr <PR_NUMBER> --out <out.json>

Output schema (JSON object, single file or aggregated when multiple files):
    {
      "trigger": "listicle" | "faq" | null,   # comparison stays Tier 2
      "files": [
        {
          "file": "content/blog/foo/index.md",
          "sections": [{"heading": "Item 1: Foo", "lines": 87}, ...],
          "stats": {"mean": 54.5, "median": 31.0, "std": 60.5},
          "outliers": [{"heading": "Part 2", "lines": 219, "ratio": 7.1}],
          "threshold_flags": [
            {"type": "section-depth-3x-median",
             "heading": "Part 2",
             "lines": 219, "ratio": 7.1}
          ]
        }
      ]
    }

Empty input (no PR-changed `content/blog/**/*.md`) produces `{"trigger": null,
"files": []}`. The script does not call any APIs except `gh pr diff` (for the
PR-changed file list) and reads `content/blog/**` from the local filesystem.
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import subprocess
import sys
from pathlib import Path

OUTLIER_RATIO = 3.0  # section ≥ 3× median

# Listicle: H2s of the form "## item N:" / "## 1. ..." / "## Item N: ..."
LISTICLE_H2_RE = re.compile(r"^##\s+(?:[Ii]tem\s+\d+\b|\d+\.\s)", re.MULTILINE)
# FAQ: H2 named "Frequently asked questions" (case-insensitive)
FAQ_H2_RE = re.compile(r"^##\s+frequently\s+asked\s+questions\s*$",
                       re.MULTILINE | re.IGNORECASE)


def fetch_pr_files(pr: str) -> list[str]:
    """Return list of PR-changed files under content/blog/**/*.md."""
    try:
        proc = subprocess.run(
            ["gh", "pr", "diff", pr, "--name-only"],
            check=True, capture_output=True, text=True, timeout=30,
        )
    except (subprocess.SubprocessError, OSError):
        return []
    return [
        f.strip() for f in proc.stdout.splitlines()
        if f.strip().startswith("content/blog/") and f.strip().endswith(".md")
    ]


def repo_root() -> Path:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, check=True, timeout=10,
        )
        return Path(result.stdout.strip())
    except (subprocess.SubprocessError, OSError):
        return Path.cwd()


def strip_frontmatter(text: str) -> str:
    """Strip a leading `---\\n...\\n---\\n` Hugo frontmatter block."""
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[end + 5:]
    return text


def split_h2_sections(body: str) -> list[tuple[str, int]]:
    """Return [(heading_text, body_line_count), ...].

    body_line_count excludes blank lines and the heading itself.
    Sub-headings (### / ####) and code-fence content count toward the section.
    """
    lines = body.splitlines()
    sections: list[tuple[str, int]] = []
    current_heading: str | None = None
    current_count = 0
    for raw in lines:
        if raw.startswith("## ") and not raw.startswith("### "):
            if current_heading is not None:
                sections.append((current_heading, current_count))
            current_heading = raw[3:].strip()
            current_count = 0
            continue
        if current_heading is None:
            continue
        if not raw.strip():
            continue
        current_count += 1
    if current_heading is not None:
        sections.append((current_heading, current_count))
    return sections


def detect_trigger(body: str, sections: list[tuple[str, int]]) -> str | None:
    """Tier 1 trigger: listicle / FAQ. Comparison stays Tier 2 (model-side)."""
    if FAQ_H2_RE.search(body):
        return "faq"
    listicle_count = 0
    for heading, _ in sections:
        if LISTICLE_H2_RE.match(f"## {heading}"):
            listicle_count += 1
    if listicle_count >= 3:
        return "listicle"
    return None


def compute_stats(sections: list[tuple[str, int]]) -> dict:
    if not sections:
        return {"mean": 0.0, "median": 0.0, "std": 0.0}
    lengths = [s[1] for s in sections]
    return {
        "mean": round(statistics.mean(lengths), 1),
        "median": round(statistics.median(lengths), 1),
        "std": round(statistics.pstdev(lengths) if len(lengths) > 1 else 0.0, 1),
    }


def find_outliers(sections: list[tuple[str, int]],
                  median: float) -> list[dict]:
    if median <= 0:
        return []
    out = []
    for heading, lines in sections:
        ratio = round(lines / median, 1)
        if ratio >= OUTLIER_RATIO:
            out.append({"heading": heading, "lines": lines, "ratio": ratio})
    return out


def analyze_file(path: Path) -> dict | None:
    """Return a single-file analysis record, or None if not analyzable."""
    if not path.is_file():
        return None
    try:
        text = path.read_text(errors="replace")
    except OSError:
        return None
    body = strip_frontmatter(text)
    sections = split_h2_sections(body)
    if not sections:
        return None
    stats = compute_stats(sections)
    outliers = find_outliers(sections, stats["median"])
    threshold_flags = [
        {
            "type": "section-depth-3x-median",
            "heading": o["heading"],
            "lines": o["lines"],
            "ratio": o["ratio"],
        }
        for o in outliers
    ]
    return {
        "sections": [{"heading": h, "lines": n} for h, n in sections],
        "stats": stats,
        "outliers": outliers,
        "threshold_flags": threshold_flags,
        "trigger_local": detect_trigger(body, sections),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pr", required=True, help="PR number")
    parser.add_argument("--out", dest="outfile", required=True)
    args = parser.parse_args()

    out_path = Path(args.outfile)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    files = fetch_pr_files(args.pr)
    if not files:
        out_path.write_text(json.dumps({"trigger": None, "files": []}))
        print("editorial-balance-detect: no PR-changed blog files; skipping",
              file=sys.stderr)
        return 0

    root = repo_root()
    file_records: list[dict] = []
    for rel in files:
        record = analyze_file(root / rel)
        if record is None:
            continue
        record["file"] = rel
        file_records.append(record)

    # Aggregate trigger: any file's trigger wins (faq > listicle by precedence
    # if both fire on different files; faq is the more specific signal).
    triggers = [r["trigger_local"] for r in file_records if r.get("trigger_local")]
    if "faq" in triggers:
        agg = "faq"
    elif "listicle" in triggers:
        agg = "listicle"
    else:
        agg = None

    out = {
        "trigger": agg,
        "files": [{k: v for k, v in r.items() if k != "trigger_local"}
                  for r in file_records],
    }
    out_path.write_text(json.dumps(out, indent=2))
    print(
        f"editorial-balance-detect: trigger={agg}, "
        f"{len(file_records)} file(s) analyzed → {out_path}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
