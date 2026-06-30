#!/usr/bin/env python3
"""Tests for render-provenance.py (deterministic "Why this page" block)."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    "render_provenance", Path(__file__).resolve().parent / "render-provenance.py"
)
rp = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rp)

failures: list[str] = []


def check(name: str, cond: bool) -> None:
    if cond:
        print(f"ok: {name}")
    else:
        failures.append(name)
        print(f"FAIL: {name}", file=sys.stderr)


def _entry(**over):
    base = {
        "path": "content/docs/iac/concepts/projects/stack-settings-file.md",
        "url": "/docs/iac/concepts/projects/stack-settings-file/",
        "slug": "docs-iac-concepts-projects-stack-settings-file",
        "lane": "priority",
        "tier": 1,
        "no_retire": True,
        "monthly_visits": 1639,
        "last_reviewed": None,
        "attempts": 0,
        "score": 294.9144,
    }
    base.update(over)
    return base


# Traffic available + page has a visit figure -> real number, not "unavailable".
q = {
    "traffic": {
        "source": "CLICKSTREAM.FCT_PAGEVIEWS",
        "period": {"start": "2025-12-22", "end": "2026-06-22"},
        "available": True,
    },
    "articles": [_entry()],
}
out = rp.render(q)
check("renders the canonical heading", out.startswith("## Why this page"))
check("formats visits with a thousands separator", "1,639 monthly visits" in out)
check("includes the report period", "2025-12-22 to 2026-06-22" in out)
check("never narrates 'unavailable' when traffic is present", "unavailable" not in out)
check("surfaces tier + no_retire", "**Strategic tier:** 1 (`no_retire: true`)" in out)
check("surfaces the score", "294.9144" in out)
check("marks the block machine-composed", "composed deterministically" in out)

# Snapshot present but this page absent from it -> distinct from snapshot-missing.
q_missing_page = {
    "traffic": {"available": True, "period": "2026-06"},
    "articles": [_entry(monthly_visits=None)],
}
check(
    "page absent from snapshot reads distinctly",
    "not in the traffic snapshot" in rp.render(q_missing_page),
)

# No snapshot at all (worker --paths fallback) -> says so, doesn't invent a number.
q_no_traffic = {
    "traffic": {"available": False},
    "articles": [_entry(monthly_visits=None, last_reviewed="2026-05-01", attempts=1, score=None)],
}
out2 = rp.render(q_no_traffic)
check("snapshot-unavailable stated plainly", "snapshot unavailable this run" in out2)
check("last_reviewed date rendered when present", "2026-05-01 (`attempts: 1`)" in out2)
check("missing score degrades gracefully", "n/a (explicit dispatch)" in out2)

if failures:
    print(f"\n{len(failures)} failure(s)", file=sys.stderr)
    sys.exit(1)
print("\nall render-provenance tests passed")
