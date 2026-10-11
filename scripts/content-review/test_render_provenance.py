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

# No reader_signals block (pre-export runs) -> body identical to before the
# feature existed: no Search / Reader feedback lines at all.
check("no reader_signals -> no Search line", "**Search:**" not in out)
check("no reader_signals -> no feedback line", "**Reader feedback:**" not in out)

# Reader signals available + page has figures -> Search and feedback lines.
q_signals = {
    "traffic": {"available": False},
    "reader_signals": {
        "available": True,
        "gsc": {"available": True, "source": "google-search-console",
                "period": {"start": "2026-03-14", "end": "2026-06-11"},
                "pages_matched": 612, "median_ctr": 0.031, "max_impressions": 88012},
        "feedback": {"available": True, "pages_matched": 214},
    },
    "articles": [_entry(signals={
        "gsc": {"impressions": 15234, "ctr": 0.0205, "opportunity": 0.41,
                "multiplier": 1.1025, "low_ctr_flag": True},
        "feedback": {"yes": 4, "no": 9, "neg_rate": 0.6923, "multiplier": 1.27},
    })],
}
out3 = rp.render(q_signals)
check("Search line renders impressions + CTR",
      "**Search:** 15,234 impressions, 2.05% CTR" in out3)
check("Search line includes the corpus median", "corpus median 3.10%" in out3)
check("Search line includes the period", "period 2026-03-14 to 2026-06-11" in out3)
check("low-CTR flag surfaces", "**low-CTR flag**" in out3)
check("feedback line renders votes + negativity",
      "**Reader feedback:** 4 yes / 9 no (69% negative)" in out3)

# Signals export available but this page has no rows -> distinct wording, no numbers.
q_signals_absent = {
    "traffic": {"available": False},
    "reader_signals": {
        "available": True,
        "gsc": {"available": True, "median_ctr": 0.031},
        "feedback": {"available": True},
    },
    "articles": [_entry(signals={"gsc": None, "feedback": None})],
}
out4 = rp.render(q_signals_absent)
check("page absent from GSC reads distinctly", "no Search Console data for this page" in out4)
check("page absent from feedback reads distinctly", "**Reader feedback:** none recorded" in out4)
check("no flag when no data", "low-CTR flag" not in out4)

# Unflagged page renders the Search line without the flag suffix.
q_no_flag = {
    "traffic": {"available": False},
    "reader_signals": {"available": True,
                       "gsc": {"available": True, "median_ctr": 0.031},
                       "feedback": {"available": False}},
    "articles": [_entry(signals={
        "gsc": {"impressions": 2000, "ctr": 0.05, "opportunity": 0.0,
                "multiplier": 1.0, "low_ctr_flag": False}})],
}
out5 = rp.render(q_no_flag)
check("healthy page has Search line but no flag",
      "**Search:** 2,000 impressions" in out5 and "low-CTR flag" not in out5)
check("feedback section absent when that signal is unavailable",
      "**Reader feedback:**" not in out5)

if failures:
    print(f"\n{len(failures)} failure(s)", file=sys.stderr)
    sys.exit(1)
print("\nall render-provenance tests passed")
