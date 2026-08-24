#!/usr/bin/env python3
"""Sentence-case check for front-matter titles, via Vale itself.

The site's H1s come from front matter (`title:`, and `h1:` on overview
pages), which Vale never sees — it skips YAML front matter entirely. But the
brand standard (Names & terminology: "Pulumi has no title-case convention")
applies to page titles too, and Pulumi.HeadingSentenceCase already encodes
the sentence-case check plus the curated proper-noun exceptions list.

Rather than duplicate that logic (a second implementation would drift from
the rule, and the rule drifts from the brand guide — see
styles/Pulumi/BRAND-SYNC.yaml), this script extracts each file's title
fields, writes them as `# <title>` headings in synthetic one-line docs, runs
Vale's Pulumi.HeadingSentenceCase over them, and maps findings back to the
real file and line. Same rule, same exceptions, one source of truth.

Advisory only: exits 0 always, like the rest of `make lint-prose`.

Usage:
    python3 scripts/lint/frontmatter-title-case.py FILE [FILE ...]

Callers (scripts/lint-prose.sh) pass the changed-file list, so the Title
Case backlog surfaces incrementally as pages are touched rather than as one
un-actionable wall of findings.
"""

import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

# Mirrors the .vale.ini per-path exemption: generated from `pulumi gen-docs`,
# so title casing there follows upstream pulumi/pulumi, not this repo.
# (Synthetic temp files can't inherit .vale.ini's [content/...] sections,
# which match on the real paths, so the exemption is re-applied here.)
EXEMPT_PREFIXES = ("content/docs/iac/cli/commands/",)

TITLE_KEYS = ("title", "h1")


def extract_titles(path):
    """Yield (line_number, key, title_text) for top-level title-ish keys."""
    try:
        lines = path.read_text(encoding="utf-8").split("\n")
    except (OSError, UnicodeDecodeError):
        return
    if not lines or lines[0].strip() != "---":
        return
    for i, line in enumerate(lines[1:], start=2):
        if line.strip() in ("---", "..."):
            break
        m = re.match(r"^(title|h1):\s+(.+?)\s*$", line)
        if not m:
            continue
        key, raw = m.groups()
        if key not in TITLE_KEYS:
            continue
        text = raw.strip()
        # Unquote; skip block scalars, templates, and empty values.
        if text in ("|", ">", "") or text.startswith(("|", ">")):
            continue
        if (text[0], text[-1]) in (('"', '"'), ("'", "'")) and len(text) > 1:
            text = text[1:-1]
        if text:
            yield i, key, text


def main(argv):
    targets = []
    for a in argv:
        p = Path(a)
        if p.is_dir():
            targets.extend(p.rglob("*.md"))
        elif a.endswith(".md"):
            targets.append(p)
    targets = [
        t
        for t in targets
        if t.is_file() and not str(t).startswith(EXEMPT_PREFIXES)
    ]
    if not targets:
        return 0

    with tempfile.TemporaryDirectory() as tmp:
        tmpdir = Path(tmp)
        index = {}  # synthetic filename -> (real path, real line, title)
        for t in targets:
            for line_no, key, title in extract_titles(t):
                name = f"t{len(index)}.md"
                (tmpdir / name).write_text(f"# {title}\n", encoding="utf-8")
                index[name] = (t, line_no, title)
        if not index:
            return 0

        # The repo .vale.ini (found from the CWD) supplies StylesPath; the
        # findings are filtered to the one rule below rather than via
        # --filter, which in Vale 3.x takes a filter *file*, not an inline
        # expression.
        result = subprocess.run(
            [
                "vale",
                "--no-exit",
                "--output=JSON",
                *(str(tmpdir / n) for n in index),
            ],
            capture_output=True,
            text=True,
        )
        try:
            findings = json.loads(result.stdout or "{}")
        except json.JSONDecodeError:
            print(
                f"frontmatter-title-case: could not parse Vale output: "
                f"{result.stderr.strip() or result.stdout[:200]}",
                file=sys.stderr,
            )
            return 0

        if not isinstance(findings, dict) or "Code" in findings:
            print(
                f"frontmatter-title-case: Vale error: {findings}",
                file=sys.stderr,
            )
            return 0

        count = 0
        for synth, items in findings.items():
            real, line_no, title = index[Path(synth).name]
            for item in items:
                if item.get("Check") != "Pulumi.HeadingSentenceCase":
                    continue
                count += 1
                print(
                    f"{real}:{line_no}: front-matter title '{title}' should "
                    f"use sentence case (Pulumi.HeadingSentenceCase; "
                    f"brand guide: writing style, headings and titles)."
                )
        if count:
            print(
                f"frontmatter-title-case: {count} title(s) to migrate "
                f"(advisory; sentence-case them as you touch these pages)."
            )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
