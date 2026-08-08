#!/usr/bin/env python3
"""Unit tests for scrape-review-outcomes.py.

Self-contained — run with `python3 test_scrape_review_outcomes.py` (no pytest
dep). Imports the scraper module directly and exercises the body parsing,
classification, and aggregation paths without shelling out to gh; the gh
paths are covered by monkeypatching the module's run_gh.
"""

from __future__ import annotations

import importlib.util
import json
import sys
import traceback
from pathlib import Path

HERE = Path(__file__).resolve().parent

_spec = importlib.util.spec_from_file_location(
    "scrape_review_outcomes", HERE / "scrape-review-outcomes.py"
)
sro = importlib.util.module_from_spec(_spec)
sys.modules["scrape_review_outcomes"] = sro
_spec.loader.exec_module(sro)  # type: ignore[union-attr]

MERGE_HEAD = "deadbee0000000000000000000000000000000ff"


def body_with(
    outstanding: str = "",
    low_confidence: str = "",
    resolved: str = "",
    trail: str = "",
    history: str = "- 2026-07-01T00:00:00Z — initial review (deadbee)",
    counts: tuple[int, int, int, int] = (0, 0, 0, 0),
) -> str:
    return f"""\
<!-- CLAUDE_REVIEW 1/1 -->
## Pre-merge Review — Last updated 2026-07-01T00:00:00Z

| 🚨 Outstanding | ⚠️ Low-confidence | 💡 Pre-existing | ✅ Resolved |
| :---: | :---: | :---: | :---: |
| **{counts[0]}** | **{counts[1]}** | **{counts[2]}** | **{counts[3]}** |

### 🔍 Verification trail

{trail or '_No verifiable claims extracted from this diff._'}

### 🚨 Outstanding in this PR

{outstanding or '_None._'}

### ⚠️ Low-confidence

{low_confidence or '_None._'}

### ✅ Resolved since last review

{resolved or '_None._'}

### 📜 Review history

{history}
"""


# ---- tests -------------------------------------------------------------------


def test_fixed_vs_conceded():
    body = body_with(
        resolved=(
            "- **[L10]** Version corrected. (resolved in abc1234)\n"
            "\n"
            "- **[L20]** concede: author confirms intentional pattern.\n"
        ),
        counts=(0, 0, 0, 2),
    )
    rec = sro.scrape_body(body, merged=True, head_sha=MERGE_HEAD)
    assert rec["outcomes"]["fixed"] == 1, rec["outcomes"]
    assert rec["outcomes"]["conceded"] == 1, rec["outcomes"]
    concessions = [d for d in rec["disputes"] if d["adjudication"] == "conceded"]
    assert len(concessions) == 1


def test_disputed_held_and_merged_over_outstanding():
    body = body_with(
        outstanding=(
            "*These must be resolved or refuted before merging.*\n"
            "\n"
            "- **[L10]** The flag default is wrong.\n"
            "  🛡️ **Disputed by alice on 2026-06-30, model held.** Docs contradict.\n"
        ),
        trail='- L10 "flag default" → ❌ contradicted (docs say false)',
        counts=(1, 0, 0, 0),
    )
    rec = sro.scrape_body(body, merged=True, head_sha=MERGE_HEAD)
    assert rec["outcomes"]["ignored_outstanding"] == 1, rec["outcomes"]
    held = [d for d in rec["disputes"] if d["adjudication"] == "held"]
    assert held and held[0]["by"] == "alice" and held[0]["on"] == "2026-06-30"
    # The trail verdict word rides along for per-category stats.
    assert rec["findings"][0]["verdict"] == "contradicted"


def test_closed_unmerged_is_abandoned():
    body = body_with(
        outstanding="- **[L10]** Broken instruction.\n",
        counts=(1, 0, 0, 0),
    )
    rec = sro.scrape_body(body, merged=False, head_sha=None)
    assert rec["outcomes"]["abandoned"] == 1
    assert rec["outcomes"]["ignored_outstanding"] == 0


def test_stale_review_at_merge():
    body = body_with(
        outstanding="- **[L10]** Broken instruction.\n",
        low_confidence="- **[L20]** Please cite a source.\n",
        history="- 2026-07-01T00:00:00Z — initial review (0123abc)",
        counts=(1, 1, 0, 0),
    )
    rec = sro.scrape_body(body, merged=True, head_sha=MERGE_HEAD)
    assert rec["review_current_at_merge"] is False
    assert rec["outcomes"]["unconfirmed_at_merge"] == 2
    assert rec["outcomes"]["ignored_outstanding"] == 0
    assert rec["outcomes"]["ignored_low_confidence"] == 0


def test_style_findings_counted_not_classified():
    # Deliberately uses the pre-2026-08-03 "Style findings" heading: this
    # reader parses historical merged PRs, which carry the old spelling.
    body = body_with(
        low_confidence=(
            "- **[L20]** Please cite a source.\n"
            "\n"
            "#### Style findings\n"
            "\n"
            "*Optional polish from pattern-based linting.*\n"
            "\n"
            "- **line 42:** [style] _substitution_ — Use 'select' instead of 'click'.\n"
            "- **line 87:** [style] _passive voice_ — Use active voice.\n"
        ),
        counts=(0, 3, 0, 0),
    )
    rec = sro.scrape_body(body, merged=True, head_sha=MERGE_HEAD)
    assert rec["style_findings"] == 2
    assert rec["outcomes"]["ignored_low_confidence"] == 1


def test_multi_comment_overflow():
    # ✅ Resolved spills into a 2/2 comment; scrape over the joined bodies.
    first = body_with(
        outstanding="- **[L10]** Broken instruction.\n",
        counts=(1, 0, 0, 1),
    )
    # The overflow page carries the spilled section only (no table, no history).
    second = (
        "<!-- CLAUDE_REVIEW 2/2 -->\n"
        "### ✅ Resolved since last review\n"
        "\n"
        "- **[L30]** Version corrected. (resolved in abc1234)\n"
    )
    # find_section returns the FIRST matching heading, so drop the 1/1 page's
    # empty ✅ section the way the real overflow splitter does: page 1 ends at 📜.
    first = first.replace(
        "### ✅ Resolved since last review\n\n_None._\n\n", ""
    )
    rec = sro.scrape_body(first + "\n" + second, merged=True, head_sha=MERGE_HEAD)
    assert rec["outcomes"]["fixed"] == 1, rec["outcomes"]
    assert rec["outcomes"]["ignored_outstanding"] == 1


def test_legacy_unparseable_degrades():
    legacy = (
        "<!-- CLAUDE_REVIEW 1/1 -->\n"
        "Thanks! I reviewed this PR and found two issues, listed below.\n\n"
        "1. The link is broken.\n2. The version is wrong.\n"
    )
    rec = sro.scrape_body(legacy, merged=True, head_sha=None)
    assert rec["parse_confidence"] == "none"
    assert sum(rec["outcomes"].values()) == 0

    # History but no count table -> "low": partial signal, counted not rated.
    partial = "### 📜 Review history\n\n- 2026-07-01 — initial review (abc1234)\n"
    rec = sro.scrape_body(partial, merged=True, head_sha=None)
    assert rec["parse_confidence"] == "low"


def test_fetch_pinned_bodies_filters_and_orders():
    def fake_run_gh(args):
        rows = [
            {"id": 3, "body": "<!-- CLAUDE_REVIEW 2/2 -->\nsecond"},
            {"id": 1, "body": "just a human comment"},
            {"id": 2, "body": "<!-- CLAUDE_REVIEW 1/2 -->\nfirst"},
            {"id": 4, "body": "<!-- CLAUDE_PROGRESS -->\nprogress note"},
        ]
        return "\n".join(json.dumps(json.dumps(r)) for r in rows) + "\n"

    original = sro.run_gh
    sro.run_gh = fake_run_gh
    try:
        bodies = sro.fetch_pinned_bodies("pulumi/docs", 1)
    finally:
        sro.run_gh = original
    assert len(bodies) == 2
    assert bodies[0].endswith("first") and bodies[1].endswith("second")


def test_scrape_pr_no_review_data():
    def fake_meta(repo, pr):
        return {
            "number": pr, "title": "t", "url": "u", "state": "MERGED",
            "mergedAt": "2026-07-01T00:00:00Z", "closedAt": None,
            "headRefOid": MERGE_HEAD, "headRefName": "feature",
            "author": {"login": "alice"}, "labels": [],
        }

    originals = (sro.fetch_pr_meta, sro.fetch_pinned_bodies)
    sro.fetch_pr_meta = fake_meta
    sro.fetch_pinned_bodies = lambda repo, pr: []
    try:
        rec = sro.scrape_pr("pulumi/docs", 42)
    finally:
        sro.fetch_pr_meta, sro.fetch_pinned_bodies = originals
    assert rec["status"] == "no_review_data"
    assert rec["author_kind"] == "human"


def test_author_kind_bot_detection():
    assert sro.author_kind({"author": {"login": "pulumi-bot"}, "headRefName": "x"}) == "bot"
    assert sro.author_kind({"author": {"login": "octo[bot]"}, "headRefName": "x"}) == "bot"
    assert sro.author_kind({"author": {"login": "alice"}, "headRefName": "content-review/foo"}) == "bot"
    assert sro.author_kind({"author": {"login": "alice"}, "headRefName": "fix-typo"}) == "human"


def test_aggregate_and_stats_render():
    body = body_with(
        outstanding=(
            "- **[L10]** The flag default is wrong.\n"
            "  🛡️ **Disputed by alice on 2026-06-30, model held.**\n"
        ),
        resolved="- **[L30]** concede: author is right.\n",
        trail=(
            '- L10 "flag" → ❌ contradicted (docs)\n'
            '- L30 "claim" → 🤷 unverifiable (no source)'
        ),
        counts=(1, 0, 0, 1),
    )
    scraped = sro.scrape_body(body, merged=True, head_sha=MERGE_HEAD)
    records = [
        {"status": "scraped", "pr": 7, "title": "T", "url": "u",
         "author_kind": "human", "parse_confidence": "high", **scraped},
        {"status": "no_review_data", "pr": 8},
    ]
    agg = sro.aggregate(records)
    assert agg["prs_scraped"] == 1 and agg["prs_no_review_data"] == 1
    assert agg["outcomes"]["human"]["ignored_outstanding"] == 1
    assert agg["outcomes"]["human"]["conceded"] == 1
    assert agg["merged_with_outstanding"][0]["pr"] == 7
    assert {d["adjudication"] for d in agg["disputes"]} == {"held", "conceded"}
    assert agg["by_verdict"]["contradicted"]["ignored_outstanding"] == 1

    report = sro.render_stats(agg, "2026-04-01")
    assert "Merged over 🚨 Outstanding findings" in report
    assert "| contradicted |" in report
    assert "@alice" in report


def test_real_pinned_review_pr20079():
    """Regression fixture captured from pulumi/docs#20079's actual pinned review."""
    body = (HERE / "testdata" / "pr20079-pinned-review.md").read_text()
    # #20079 merged at head d0c76f0…; the last 📜 history SHA matches it.
    rec = sro.scrape_body(body, merged=True, head_sha="d0c76f07aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    assert rec["parse_confidence"] == "high"
    assert rec["counts_table"] == {"outstanding": 0, "low_confidence": 0, "pre_existing": 1, "resolved": 2}
    assert rec["review_current_at_merge"] is True
    assert rec["outcomes"]["fixed"] == 2, rec["outcomes"]
    assert rec["outcomes"]["conceded"] == 0
    assert sum(rec["outcomes"].values()) == 2
    assert rec["pre_existing"] == 1
    assert rec["review_events"] == 2
    assert rec["disputes"] == []


def main() -> int:
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    failures = 0
    for test in tests:
        try:
            test()
            print(f"  ok  {test.__name__}")
        except Exception:
            failures += 1
            print(f"  FAIL {test.__name__}")
            traceback.print_exc()
    print(f"{len(tests) - failures}/{len(tests)} passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
