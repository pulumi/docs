#!/usr/bin/env python3
"""Rebuild the blog-review index summary from the per-post index entries.

The record job syncs the S3 `blog-review/index/` prefix to a local directory,
runs this script over it, and uploads the result back as
`blog-review/index/_summary.json`. The summary is the artifact the future
noindex decision process (and humans, and the warehouse) read first: corpus
totals by issue category and severity, plus the current list of
`candidate` / `strong-candidate` posts with the signals a threshold-based
decision needs.

This script is a pure function of the index directory (plus the --today test
hook); it consults no network and makes no judgment calls — thresholds and
decisions belong to the consumer.

Usage:
    build-summary.py --index-dir .index-cache --out _summary.json [--today YYYY-MM-DD]
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

SCHEMA_VERSION = 1


def load_entries(index_dir: Path) -> list[dict]:
    entries = []
    for f in sorted(index_dir.glob("*.json")):
        if f.name == "_summary.json":
            continue
        try:
            entry = json.loads(f.read_text())
        except (OSError, json.JSONDecodeError):
            print(f"build-summary: unreadable index entry {f}", file=sys.stderr)
            continue
        if isinstance(entry, dict) and entry.get("slug"):
            entries.append(entry)
    return entries


def candidate_row(entry: dict) -> dict:
    """The fields a threshold-based noindex decision needs, nothing more."""
    return {
        "slug": entry["slug"],
        "url": entry.get("url"),
        "path": entry.get("path"),
        "post_date": entry.get("post_date"),
        "reviewed_at": entry.get("reviewed_at"),
        "assessment": (entry.get("noindex_signal") or {}).get("assessment"),
        "rationale": (entry.get("noindex_signal") or {}).get("rationale"),
        "issue_counts": entry.get("issue_counts"),
        "signals": entry.get("signals"),
    }


def build_summary(entries: list[dict], today: str | None = None) -> dict:
    by_severity: dict[str, int] = {}
    by_category: dict[str, int] = {}
    clean = 0
    with_issues = 0
    candidates = []
    for e in entries:
        counts = e.get("issue_counts") or {}
        for k, v in (counts.get("by_severity") or {}).items():
            by_severity[k] = by_severity.get(k, 0) + int(v)
        for k, v in (counts.get("by_category") or {}).items():
            by_category[k] = by_category.get(k, 0) + int(v)
        if e.get("clean"):
            clean += 1
        elif counts.get("total"):
            with_issues += 1
        assessment = (e.get("noindex_signal") or {}).get("assessment")
        if assessment in ("candidate", "strong-candidate"):
            candidates.append(candidate_row(e))

    candidates.sort(key=lambda r: (r["assessment"] != "strong-candidate", r["slug"]))
    return {
        "schema_version": SCHEMA_VERSION,
        "generated": today or datetime.now(timezone.utc).date().isoformat(),
        "posts_indexed": len(entries),
        "posts_clean": clean,
        "posts_with_issues": with_issues,
        "issues_by_severity": dict(sorted(by_severity.items())),
        "issues_by_category": dict(sorted(by_category.items())),
        "noindex_candidates": candidates,
    }


def self_test() -> int:
    entries = [
        {"slug": "a", "url": "/blog/a/", "clean": False,
         "issue_counts": {"total": 2, "by_severity": {"major": 1, "minor": 1},
                          "by_category": {"dead-link": 2}},
         "noindex_signal": {"assessment": "strong-candidate", "rationale": "r"}},
        {"slug": "b", "url": "/blog/b/", "clean": True,
         "issue_counts": {"total": 0, "by_severity": {}, "by_category": {}},
         "noindex_signal": {"assessment": "keep", "rationale": "r"}},
        {"slug": "c", "url": "/blog/c/", "clean": False,
         "issue_counts": {"total": 1, "by_severity": {"minor": 1},
                          "by_category": {"seo-thin": 1}},
         "noindex_signal": {"assessment": "candidate", "rationale": "r"}},
    ]
    s = build_summary(entries, today="2026-07-15")
    ok = (
        s["posts_indexed"] == 3
        and s["posts_clean"] == 1
        and s["posts_with_issues"] == 2
        and s["issues_by_severity"] == {"major": 1, "minor": 2}
        and s["issues_by_category"] == {"dead-link": 2, "seo-thin": 1}
        and [c["slug"] for c in s["noindex_candidates"]] == ["a", "c"]
        and s["generated"] == "2026-07-15"
    )
    print("all build-summary self-tests passed" if ok else "FAIL", file=sys.stderr)
    return 0 if ok else 1


def main() -> int:
    p = argparse.ArgumentParser(description="Rebuild the blog-review index summary.")
    p.add_argument("--index-dir", help="local sync of the S3 index/ prefix")
    p.add_argument("--out", help="summary JSON output path")
    p.add_argument("--today", help="Override the generated date YYYY-MM-DD (testing)")
    p.add_argument("--self-test", action="store_true", help="run built-in smoke checks")
    args = p.parse_args()

    if args.self_test:
        return self_test()
    if not args.index_dir or not args.out:
        p.error("--index-dir and --out are required")

    summary = build_summary(load_entries(Path(args.index_dir)), today=args.today)
    Path(args.out).write_text(json.dumps(summary, indent=2) + "\n")
    print(
        f"build-summary: {summary['posts_indexed']} post(s), "
        f"{len(summary['noindex_candidates'])} noindex candidate(s) → {args.out}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
