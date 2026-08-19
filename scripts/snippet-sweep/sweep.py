#!/usr/bin/env python3
"""Nightly deterministic snippet-parse sweep (issue #20078 §4.3).

Extracts every inline fenced code block on tier-1/2 pages under
`content/docs/` and runs a per-language *parse floor* — no execution, no
AI model. Findings are written as a signal file consumed by the content
review selector (`scripts/content-review/select-articles.py
--signal-file`) as queue-priority boosts; the sweep itself never opens
PRs or notifies on findings.

Precision over recall: a block that can't be checked with near-certainty
is skipped, not flagged (see `checkers.py`), and residual false positives
are suppressed via `ignore.txt` (path + content-hash entries that
auto-expire when the block changes).

Usage:
    sweep.py [--tiers <yaml>] [--max-tier 2] [--out .snippet-sweep.json]
             [--paths content/docs/a.md,content/docs/b.md] [--all-tiers]
             [--dry-run] [--explain-ignores] [--root <repo>]

Exit code is 0 even when findings exist — findings are a signal, not a
failure. Non-zero (2) means the sweep itself broke (missing toolchain,
unreadable tiers file): the workflow must fail loudly rather than upload
a garbage signal.

Signal schema (`.snippet-sweep.json`):

    {"schema_version": 1, "tool_version": "...", "generated": "<ISO>",
     "tier_scope": [1, 2],
     "stats": {"pages_scanned": N, "blocks_checked": N,
               "blocks_skipped": N, "suppressed": N},
     "pages": {"content/docs/...md": {"errors": N, "samples": [
        {"lang": ..., "line": ..., "block_index": ..., "check": "syntax",
         "message": ..., "hash": ...}]}}}

`samples` is capped at MAX_SAMPLES per page; `hash` is the suppression
key, copy-pasteable into `ignore.txt`.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]
DEFAULT_IGNORE = HERE / "ignore.txt"
CONTENT_DIR = "content/docs"

SCHEMA_VERSION = 1
TOOL_VERSION = "1.0"
MAX_SAMPLES = 5

sys.path.insert(0, str(HERE))
from checkers import CHECKERS, SKIP, TS_LANGS, check_ts_batch, pre_skip  # noqa: E402
from extract import extract_blocks  # noqa: E402


def load_selector():
    """Import load_tiers/policy_for/is_draft from select-articles.py.

    Reused, not copied, so the sweep can never drift from the selector's
    longest-prefix tier semantics (the hyphenated filename rules out a
    normal import).
    """
    path = REPO_ROOT / "scripts/content-review/select-articles.py"
    spec = importlib.util.spec_from_file_location("select_articles", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ---- Suppressions -------------------------------------------------------------


def block_hash(content: str) -> str:
    """sha256[:12] of whitespace-normalized block content.

    Trailing whitespace per line and leading/trailing blank lines are
    stripped, so cosmetic edits don't rotate the hash — but any content
    edit re-exposes a suppressed block (suppressions can't silently rot
    into blanket immunity).
    """
    lines = [line.rstrip() for line in content.split("\n")]
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    normalized = "\n".join(lines)
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()[:12]


def load_ignores(ignore_file: Path) -> tuple[list[tuple[str, str]], list[re.Pattern]]:
    """Parse ignore.txt into (path, hash) pairs and path regexes.

    Line formats (comments with `#`, inline or full-line):
        <content-path><TAB><hash12>    suppress one block
        <regex over content-path>      suppress a whole page/subtree
    """
    pairs: list[tuple[str, str]] = []
    patterns: list[re.Pattern] = []
    if not ignore_file.exists():
        return pairs, patterns
    for raw in ignore_file.read_text().split("\n"):
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        if "\t" in line:
            path, block = line.split("\t", 1)
            pairs.append((path.strip(), block.strip()))
        else:
            patterns.append(re.compile(line.strip()))
    return pairs, patterns


# ---- Sweep --------------------------------------------------------------------


def checkable(block: dict) -> bool:
    return block["lang"] in CHECKERS or block["lang"] in TS_LANGS


def sweep(pages: list[str], root: Path, ignore_file: Path) -> dict:
    """Run the sweep over `pages` (repo-relative paths); return the signal."""
    pairs, patterns = load_ignores(ignore_file)
    used_ignores: set = set()

    stats = {"pages_scanned": 0, "blocks_checked": 0, "blocks_skipped": 0,
             "suppressed": 0}
    findings: dict[str, list[dict]] = {}
    ts_pending: list[tuple[str, dict]] = []  # (path, block) for the batch

    def suppressed(path: str, content: str) -> bool:
        for pat in patterns:
            if pat.search(path):
                used_ignores.add(pat.pattern)
                return True
        h = block_hash(content)
        if (path, h) in pairs:
            used_ignores.add((path, h))
            return True
        return False

    def record(path: str, block: dict, error: dict) -> None:
        findings.setdefault(path, []).append(
            {
                "lang": block["lang"],
                "line": block["start_line"] + error["line_offset"],
                "block_index": block["block_index"],
                "check": "syntax",
                "message": error["message"],
                "hash": block_hash(block["content"]),
            }
        )

    for path in pages:
        stats["pages_scanned"] += 1
        try:
            text = (root / path).read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for block in extract_blocks(text, path):
            if not checkable(block):
                continue
            if pre_skip(block["content"]):
                stats["blocks_skipped"] += 1
                continue
            if suppressed(path, block["content"]):
                stats["suppressed"] += 1
                continue
            if block["lang"] in TS_LANGS:
                ts_pending.append((path, block))
                continue
            result = CHECKERS[block["lang"]](block["content"])
            if result == SKIP:
                stats["blocks_skipped"] += 1
                continue
            stats["blocks_checked"] += 1
            if result is not None:
                record(path, block, result)

    ts_results = check_ts_batch([b for _, b in ts_pending])
    for i, (path, block) in enumerate(ts_pending):
        result = ts_results.get(i)
        if result == SKIP:
            stats["blocks_skipped"] += 1
            continue
        stats["blocks_checked"] += 1
        if result is not None:
            record(path, block, result)

    signal_pages = {
        path: {"errors": len(samples), "samples": samples[:MAX_SAMPLES]}
        for path, samples in sorted(findings.items())
    }
    unused = [
        entry for entry in ([p.pattern for p in patterns] + pairs)
        if entry not in used_ignores
    ]
    return {"stats": stats, "pages": signal_pages, "unused_ignores": unused}


# ---- CLI ----------------------------------------------------------------------


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--tiers", type=Path, default=None,
                   help="strategic-tiers.yaml (default: the selector's)")
    p.add_argument("--max-tier", type=int, default=2)
    p.add_argument("--all-tiers", action="store_true",
                   help="scan every non-tier-0 page (local audits)")
    p.add_argument("--out", type=Path, default=Path(".snippet-sweep.json"))
    p.add_argument("--paths", help="comma-separated content paths (subset run)")
    p.add_argument("--dry-run", action="store_true",
                   help="print findings as a table; write nothing")
    p.add_argument("--explain-ignores", action="store_true",
                   help="list ignore.txt entries that no longer match anything")
    p.add_argument("--ignore-file", type=Path, default=DEFAULT_IGNORE)
    p.add_argument("--root", type=Path, default=REPO_ROOT,
                   help="repo root override (tests)")
    args = p.parse_args()

    selector = load_selector()
    tiers_file = args.tiers or (
        args.root / ".claude/commands/review-existing-content/references/strategic-tiers.yaml"
    )
    try:
        rules = selector.load_tiers(tiers_file)
    except OSError as e:
        print(f"error: cannot read tiers file: {e}", file=sys.stderr)
        return 2

    for tool, langs in (("node", "TypeScript/JavaScript"), ("gofmt", "Go")):
        if shutil.which(tool) is None:
            print(f"error: `{tool}` not found — required for {langs} checks",
                  file=sys.stderr)
            return 2

    if args.paths:
        pages = [s.strip() for s in args.paths.split(",") if s.strip()]
    else:
        pages = sorted(
            str(f.relative_to(args.root))
            for f in (args.root / CONTENT_DIR).rglob("*.md")
        )

    scoped: list[str] = []
    tier_scope = list(range(1, args.max_tier + 1))
    for path in pages:
        policy = selector.policy_for(path, rules)
        tier = policy.tier
        # The sweep edits snippets in place, so a page a generator owns is out
        # of scope however reviewable it is (pulumi/docs#20996).
        if not policy.editable:
            continue
        if not args.all_tiers and tier > args.max_tier:
            continue
        if selector.is_draft(args.root / path):
            continue
        scoped.append(path)

    result = sweep(scoped, args.root, args.ignore_file)

    if args.explain_ignores:
        if result["unused_ignores"]:
            print("ignore.txt entries that no longer match anything:")
            for entry in result["unused_ignores"]:
                print(f"  {entry}")
        else:
            print("all ignore.txt entries are live")
        return 0

    if args.dry_run:
        total = sum(pg["errors"] for pg in result["pages"].values())
        print(f"{result['stats']} | findings: {total}")
        for path, page in result["pages"].items():
            for s in page["samples"]:
                print(f"{path}:{s['line']}\t{s['lang']}\t{s['hash']}\t{s['message']}")
        return 0

    signal = {
        "schema_version": SCHEMA_VERSION,
        "tool_version": TOOL_VERSION,
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "tier_scope": tier_scope if not args.all_tiers else "all",
        "stats": result["stats"],
        "pages": result["pages"],
    }
    args.out.write_text(json.dumps(signal, indent=2) + "\n")
    total = sum(pg["errors"] for pg in result["pages"].values())
    print(f"wrote {args.out}: {total} finding(s) across "
          f"{len(result['pages'])} page(s); stats={result['stats']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
