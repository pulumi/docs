#!/usr/bin/env python3
"""Assemble the glow-up worker's backlog from logged content-review feedback.

The fix lane banks its judgment-level material instead of applying it: the
"Findings not applied" section of each review PR, the flag-only "Screenshot
check" and "Rendered content" observations, and the ledger's `clarity_flag` /
`skipped_findings` counters. This deterministic pre-step (run by the workflow
BEFORE the model, like the claim pipeline) collects that record for one page
into `.glowup-backlog.json`, so the glow-up skill starts from the accumulated
backlog rather than a cold read:

    {"schema_version": 1, "slug": ..., "path": ..., "generated": ...,
     "clarity_flag": bool, "skipped_findings": int,
     "source_prs": [{"number": 123, "url": ...}, ...],
     "banked": [{"id": "pr123-findings-1", "section": "Findings not applied",
                 "source_pr": 123, "text": "<the row/bullet>"}, ...],
     "notes": ["<degradation notes, if any>"]}

Sources: the page's ledger entry (`--ledger-dir`) carries the latest review's
`pr_number`; earlier PRs for the same page are discovered via `gh pr list`
over the page's canonical branch names is NOT possible (branches are reused),
so the backlog reads the PRs the ledger knows about — currently the latest —
plus any extras passed via `--pr` (the workflow may pass several). Section
extraction is heading-based and tolerant: a PR body without the section, an
unreachable PR, or no PRs at all degrade to an empty `banked` list with a
note — the skill then runs its taxonomy-only sweep.

`--pr-json <file|->` injects PR view fixtures for tests (a JSON list of
{number, url, body}), replacing every `gh` call.

Self-contained smoke checks: `python3 build-glowup-backlog.py --self-test`.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

SCHEMA_VERSION = 1

# The banked sections, in the order they appear in the fix-lane PR body
# (compose-pr-body.py). "Fixes applied" is deliberately absent — those landed.
BANKED_SECTIONS = ("Findings not applied", "Screenshot check", "Rendered content")

# Section content that means "nothing banked here" — composer pre-fills and
# reviewer boilerplate, not findings.
NOISE_LINES = {
    "no images.", "skipped.", "none.", "n/a", "-", "—",
}


def log(msg: str) -> None:
    print(f"build-glowup-backlog: {msg}", file=sys.stderr)


def warn(msg: str) -> None:
    print(f"::warning::build-glowup-backlog: {msg}", file=sys.stderr)


def extract_sections(body: str) -> dict[str, list[str]]:
    """Per banked section, the non-noise content lines (rows/bullets/prose)."""
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for raw in (body or "").splitlines():
        line = raw.strip()
        m = re.match(r"^##\s+(.*)$", line)
        if m:
            title = m.group(1).strip()
            current = title if title in BANKED_SECTIONS else None
            continue
        if current is None or not line:
            continue
        if line.startswith("<!--"):
            continue
        # Table chrome (header/separator rows) is structure, not a finding.
        if re.fullmatch(r"\|?[\s|:-]+\|?", line):
            continue
        if line.lower().rstrip("_* ").lstrip("_* ") in NOISE_LINES:
            continue
        sections.setdefault(current, []).append(line)
    return sections


def fetch_pr(number: int) -> dict | None:
    proc = subprocess.run(
        ["gh", "pr", "view", str(number), "--json", "number,url,body"],
        capture_output=True, text=True, check=False,
    )
    if proc.returncode != 0:
        warn(f"gh pr view {number} failed: {proc.stderr.strip()[:200]}")
        return None
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError:
        warn(f"gh pr view {number} returned unparseable JSON")
        return None


def load_entry(ledger_dir: Path, slug: str) -> dict:
    f = ledger_dir / f"{slug}.json"
    if not f.is_file():
        return {}
    try:
        entry = json.loads(f.read_text())
        return entry if isinstance(entry, dict) else {}
    except (OSError, json.JSONDecodeError) as e:
        warn(f"ledger entry {f} unreadable ({e})")
        return {}


def build(article: dict, entry: dict, prs: list[dict]) -> dict:
    backlog = {
        "schema_version": SCHEMA_VERSION,
        "slug": article.get("slug"),
        "path": article.get("path"),
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "clarity_flag": bool(entry.get("clarity_flag") or article.get("clarity_flag")),
        "skipped_findings": int(entry.get("skipped_findings")
                                or article.get("skipped_findings") or 0),
        "source_prs": [],
        "banked": [],
        "notes": [],
    }
    for pr in prs:
        number = int(pr.get("number") or 0)
        backlog["source_prs"].append({"number": number, "url": pr.get("url")})
        sections = extract_sections(pr.get("body") or "")
        for section in BANKED_SECTIONS:
            for i, text in enumerate(sections.get(section, []), start=1):
                backlog["banked"].append({
                    "id": f"pr{number}-{section.lower().split()[0]}-{i}",
                    "section": section,
                    "source_pr": number,
                    "text": text,
                })
    if not prs:
        backlog["notes"].append(
            "no prior review PRs reachable; run the taxonomy-only sweep")
    elif not backlog["banked"]:
        backlog["notes"].append(
            "prior PR bodies carried no banked findings; run the taxonomy-only sweep")
    return backlog


def run(args) -> int:
    queue = json.loads(Path(args.queue).read_text())
    articles = queue.get("articles") or []
    if len(articles) != 1:
        warn(f"queue must carry exactly one article, found {len(articles)}")
        return 1
    article = articles[0]
    entry = load_entry(Path(args.ledger_dir), article.get("slug") or "")

    numbers: list[int] = []
    # Ledger entry when a cache is present (dispatcher-side runs); the queue
    # article's carried pointer otherwise (the worker has no ledger cache —
    # select-glowup.py stamps source_pr_number for exactly this).
    for n in (entry.get("pr_number"), article.get("source_pr_number")):
        if n and int(n) not in numbers:
            numbers.append(int(n))
    for extra in args.pr or []:
        n = int(extra)
        if n not in numbers:
            numbers.append(n)

    if args.pr_json:
        raw = sys.stdin.read() if args.pr_json == "-" else Path(args.pr_json).read_text()
        fixtures = {int(p["number"]): p for p in json.loads(raw)}
        prs = [fixtures[n] for n in numbers if n in fixtures]
    else:
        prs = [pr for n in numbers if (pr := fetch_pr(n))]

    backlog = build(article, entry, prs)
    Path(args.out).write_text(json.dumps(backlog, indent=2) + "\n")
    log(f"{len(backlog['banked'])} banked finding(s) from "
        f"{len(backlog['source_prs'])} PR(s) -> {args.out}")
    return 0


def self_test() -> int:
    failures = []

    def check(name, cond):
        if not cond:
            failures.append(name)
            print(f"FAIL: {name}", file=sys.stderr)
        else:
            print(f"ok: {name}")

    body = "\n".join([
        "> [!IMPORTANT]",
        "> notice",
        "",
        "## Why this page",
        "Selected by score.",
        "",
        "## Fixes applied",
        "| link | L88 | fixed |",
        "",
        "## Findings not applied",
        "| claim | L42 | needs interpretation |",
        "| ---- | --- | --- |",
        "- Consider restructuring the intro (readthrough L10-30)",
        "",
        "## Screenshot check",
        "No images.",
        "",
        "## Rendered content",
        "Skipped.",
        "",
        "## Verification",
        "- `make lint`: passed",
    ])
    sections = extract_sections(body)
    check("findings section extracted",
          len(sections.get("Findings not applied", [])) == 2)
    check("table separator rows dropped",
          all("----" not in t for t in sections["Findings not applied"]))
    check("pre-filled noise sections empty",
          not sections.get("Screenshot check") and not sections.get("Rendered content"))
    check("fixes/verification never banked",
          "Fixes applied" not in sections and "Verification" not in sections)

    article = {"slug": "docs-x", "path": "content/docs/x.md"}
    entry = {"skipped_findings": 2, "clarity_flag": True, "pr_number": 123}
    prs = [{"number": 123, "url": "https://example.test/123", "body": body}]
    backlog = build(article, entry, prs)
    check("banked items carry section + source PR",
          all(b["section"] == "Findings not applied" and b["source_pr"] == 123
              for b in backlog["banked"]))
    check("ids are stable and unique",
          len({b["id"] for b in backlog["banked"]}) == len(backlog["banked"]) == 2)
    check("ledger counters carried", backlog["clarity_flag"] is True
          and backlog["skipped_findings"] == 2)

    empty = build(article, entry, [])
    check("no PRs degrades to a noted empty backlog",
          empty["banked"] == [] and any("taxonomy-only" in n for n in empty["notes"]))
    blank = build(article, entry, [{"number": 5, "url": "u", "body": "## Why this page\nx"}])
    check("PR without banked sections degrades with a note",
          blank["banked"] == [] and any("taxonomy-only" in n for n in blank["notes"]))

    if failures:
        print(f"\n{len(failures)} failure(s)", file=sys.stderr)
        return 1
    print("\nall build-glowup-backlog self-tests passed")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--queue", help="single-article glow-up queue JSON")
    p.add_argument("--ledger-dir", default=".ledger-cache",
                   help="synced ledger cache (source of pr_number / counters)")
    p.add_argument("--pr", action="append",
                   help="extra PR number(s) to read bodies from (repeatable)")
    p.add_argument("--pr-json",
                   help="PR view fixtures (JSON list of {number,url,body}; '-' = stdin) "
                        "— replaces gh calls (testing)")
    p.add_argument("--out", default=".glowup-backlog.json")
    p.add_argument("--self-test", action="store_true", help="run built-in smoke checks")
    args = p.parse_args()
    if args.self_test:
        return self_test()
    if not args.queue:
        p.error("--queue is required (or --self-test)")
    return run(args)


if __name__ == "__main__":
    sys.exit(main())
