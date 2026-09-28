#!/usr/bin/env python3
"""Tests for the weekly digest: digest.py's pure shapers, render.py's
grouping/dedup/fallback, and rank.py's output parsing.

Runs under pytest (make test-review-pipeline) and standalone
(`python3 test_digest.py`). No fixtures, no network, no model.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


digest = _load("weekly_digest_collect", HERE / "digest.py")
render = _load("weekly_digest_render", HERE / "render.py")
rank = _load("weekly_digest_rank", HERE / "rank.py")

POLICY = {"warn_days": 14, "close_days": 21,
          "escalate_to": {"tools": "CamSoper", "docs-guild": "tatcoo-pulumi", "blog": "cnunciato"}}


def pr(n, *, labels=(), draft=False, age=3, checks="green", bot=False, title=None):
    return {"number": n, "title": title or f"PR {n}", "author": "bot" if bot else "someone",
            "age_days": age, "updated_days": 1, "labels": list(labels), "isDraft": draft,
            "checks": checks, "is_bot": bot}


def sweep_record():
    return {"schema": 1, "dry_run": True, "actions": [
        {"pr": 10, "kind": "reviewer", "actions": [
            {"type": "escalate", "role": "tools", "waited_business_days": 4, "sla_business_days": 1},
            {"type": "escalate", "role": "docs-guild", "waited_business_days": 4, "sla_business_days": 3}]},
        {"pr": 11, "kind": "reviewer", "actions": [
            {"type": "none", "role": "docs-guild", "waited_business_days": 2, "sla_business_days": 3}]},
        {"pr": 12, "kind": "reviewer", "actions": [
            {"type": "escalate", "role": "blog", "waited_business_days": 20, "sla_business_days": 3}]},
        {"pr": 13, "kind": "author", "action": {"type": "warn", "idle_days": 17.2, "undecided_count": 9,
                                                "closes_in_days": 7}},
        {"pr": 14, "kind": "author", "action": {"type": "none", "idle_days": 2.0, "undecided_count": 1,
                                                "closes_in_days": 19}},
        {"pr": 15, "kind": "reviewer", "actions": [
            {"type": "escalate", "role": "docs-guild", "waited_business_days": 5, "sla_business_days": 3}]},
    ]}


def base_digest(**over):
    d = {
        "generated_at": "2026-09-28T14:00:00+00:00",
        "window_days": 7,
        "prs": [pr(10), pr(11), pr(12, labels=["domain:blog"]), pr(13), pr(14), pr(15),
                pr(20, labels=["review:no-blockers"]), pr(21, age=40), pr(22, draft=True),
                pr(23, bot=True)],
        "issues": {"all_open_count": 50, "new_this_week": [
            {"number": 900, "title": "Broken link", "author": "x", "age_days": 1, "needs_triage": True}],
            "oldest_open": [{"number": 1, "title": "old", "age_days": 1800}],
            "opened_last_7d": 5, "closed_last_7d": 9},
        "throughput": {"this_week": {"prs_opened": 30, "prs_merged": 28, "prs_closed": 4,
                                     "issues_opened": 5, "issues_closed": 9},
                       "prev_week": {"prs_opened": 25, "prs_merged": 20, "prs_closed": 3,
                                     "issues_opened": 6, "issues_closed": 4}},
        "workflow_failures": {"total_runs": 100, "failing": [
            {"workflow": "Audit Logs", "runs": 4, "failures": 4, "last_failure_url": "https://x/run/1"}]},
        "switches": digest.shape_switches({"REVIEW_V3_SLA": "", "BLOG_REVIEW_COUNT": "0",
                                           "REVIEW_V3_SENTINEL": "1"}),
        "sla": digest.shape_sla(sweep_record(), POLICY, "off"),
        "review_outcomes": {"available": True, "prs_scraped": 40, "prs_no_review_data": 5,
                            "outcomes": {"human": {"fixed": 30, "ignored_outstanding": 2,
                                                   "ignored_low_confidence": 1, "unconfirmed_at_merge": 7}},
                            "disputes": [],
                            "merged_with_outstanding": [{"pr": 30, "title": "Reorg", "url": "https://github.com/pulumi/docs/pull/30",
                                                         "findings": ["a", "b"]}]},
        "v3_ops": {"available": False},
    }
    d.update(over)
    return d


# ---- digest.py shapers -------------------------------------------------------


def test_switch_semantics_match_each_workflow():
    by = {s["var"]: s for s in digest.shape_switches({
        "REVIEW_V3_SLA": "", "REVIEW_V3_SENTINEL": "report", "CONTENT_REVIEW_COUNT": "",
        "GLOWUP_COUNT": "0", "BLOG_REVIEW_COUNT": "0", "CLAIMS_REVERIFY_COUNT": "10",
        "BRAND_SYNC_ENABLED": ""})}
    assert by["REVIEW_V3_SLA"]["state"] == "off"            # == '1' switch: unset is off
    assert by["REVIEW_V3_SENTINEL"]["state"] == "report"
    assert by["CONTENT_REVIEW_COUNT"]["state"] == "on"      # != '0' switch: unset is ON
    assert by["CONTENT_REVIEW_COUNT"]["value"] == "3"       # ...at the workflow's default count
    assert by["GLOWUP_COUNT"]["state"] == "off"
    assert by["CLAIMS_REVERIFY_COUNT"]["value"] == "10"
    assert by["BRAND_SYNC_ENABLED"]["state"] == "on"


def test_switches_unknown_without_vars_never_read_as_off():
    assert {s["state"] for s in digest.shape_switches(None)} == {"unknown"}


def test_shape_sla_keeps_the_sweeps_numbers():
    sla = digest.shape_sla(sweep_record(), POLICY, "off")
    by = {v["pr"]: v for v in sla["verdicts"]}
    assert [r["role"] for r in by[10]["overdue"]] == ["tools", "docs-guild"]
    assert by[11]["overdue"] == []
    assert by[13]["abandoned"] and by[13]["closes_in_days"] == 7
    assert not by[14]["abandoned"]
    assert sla["policy"] == {"warn_days": 14, "close_days": 21}


def test_workflow_failures_counts_only_failed_workflows():
    wf = digest.shape_workflow_failures([
        {"workflowName": "A", "status": "completed", "conclusion": "failure", "url": "u1"},
        {"workflowName": "A", "status": "completed", "conclusion": "failure", "url": "u0"},
        {"workflowName": "A", "status": "completed", "conclusion": "success"},
        {"workflowName": "B", "status": "completed", "conclusion": "skipped"},
        {"workflowName": "C", "status": "in_progress", "conclusion": ""},
    ])
    assert wf["total_runs"] == 4
    assert wf["failing"] == [{"workflow": "A", "runs": 3, "failures": 2, "last_failure_url": "u1"}]


# ---- render.py ---------------------------------------------------------------


def test_each_pr_appears_once():
    msg = render.render(base_digest())
    for n in (10, 13, 15, 20, 21, 30):
        assert msg.count(f"/pull/{n}|") == 1, n


def test_blog_prs_collapse_to_one_line():
    msg = render.render(base_digest())
    assert "/pull/12|" in msg  # only as the blog line's "longest wait"
    blog_line = next(line for line in msg.splitlines() if line.startswith("*Blog/marketing*"))
    assert "1 open · 1 over SLA" in blog_line and "20bd (blog)" in blog_line


def test_multi_role_pr_groups_under_its_worst_breach():
    view = render.build_view(base_digest())
    c = next(c for c in view["candidates"] if c["number"] == 10)
    assert c["role"] == "tools"  # 3 over a 1bd SLA beats 1 over a 3bd SLA


def test_fallback_order_is_priority_then_severity():
    view = render.build_view(base_digest())
    top, source = render.resolve_ranking(view["candidates"], None)
    assert source == "fallback"
    assert [t["ref"] for t in top] == ["pr:30", "pr:13", "pr:10", "pr:15", "pr:20"]


def test_model_ranking_is_validated():
    view = render.build_view(base_digest())
    ranking = {"order": [{"ref": "pr:999", "why": "invented"}, {"ref": "pr:21", "why": "old"},
                         {"ref": "pr:21", "why": "dup"}, {"ref": "issue:900", "why": "triage it"}]}
    top, source = render.resolve_ranking(view["candidates"], ranking)
    assert source == "model"
    assert [t["ref"] for t in top] == ["pr:21", "issue:900"]


def test_empty_or_bad_ranking_falls_back_and_says_so():
    msg = render.render(base_digest(), {})
    assert "model ranking unavailable" in msg
    assert "model ranking unavailable" not in render.render(base_digest(), None)


def test_sweep_off_vs_on_wording():
    # Abandoned context has to survive promotion into the top list, so it
    # rides in the candidate's facts, not only in the section header.
    off = render.render(base_digest(), None)
    assert "would close once the SLA sweep is on" in off and "closes in" not in off
    d = base_digest()
    d["sla"] = digest.shape_sla(sweep_record(), POLICY, "on")
    d["v3_ops"] = {"available": True, "escalations_total": 6, "warns": 1, "closes": 0, "waives": 0}
    on = render.render(d, None)
    assert "closes in 7d" in on and "SLA sweep is on" not in on
    assert "*SLA sweep, last 7d*: 6 escalations · 1 warned · 0 closed · 0 waived" in on


def test_abandoned_section_header_when_not_promoted():
    d = base_digest(review_outcomes={"available": False})
    ranking = {"order": [{"ref": "pr:10", "why": "x"}]}
    msg = render.render(d, ranking)
    assert "*Abandoned* (author idle >14d; the SLA sweep is off, so they'd close 7d after" in msg


def test_sla_unavailable_is_loud():
    msg = render.render(base_digest(sla={"available": False, "enabled": "off"}), None)
    assert ":warning: SLA verdicts unavailable" in msg


def test_switch_line_lists_only_whats_off():
    msg = render.render(base_digest(), None)
    line = next(line for line in msg.splitlines() if line.startswith("*Switches*"))
    assert line == "*Switches*: off: SLA sweep, blog review index"


def test_titles_are_escaped_for_mrkdwn():
    d = base_digest()
    d["prs"][0]["title"] = "Fix <script> & a|b"
    msg = render.render(d, None)
    assert "Fix &lt;script&gt; &amp; a/b" in msg


def test_fits_in_one_slack_message():
    assert len(render.render(base_digest(), None)) < 3500


# ---- rank.py -----------------------------------------------------------------


def test_rank_parses_fenced_output():
    order = rank.parse_order('```json\n{"order": [{"ref": "pr:1", "why": "x"}]}\n```')
    assert order == [{"ref": "pr:1", "why": "x"}]


def test_rank_rejects_wrong_shape():
    for bad in ('{"ranked": []}', "[]", "not json"):
        try:
            rank.parse_order(bad)
        except (ValueError, Exception):
            continue
        raise AssertionError(f"accepted {bad!r}")


def run_standalone() -> int:
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    failures = 0
    for t in tests:
        try:
            t()
            print(f"  ok: {t.__name__}")
        except Exception as exc:  # noqa: BLE001
            failures += 1
            print(f"  FAIL: {t.__name__}: {type(exc).__name__}: {exc}", file=sys.stderr)
    print(f"{len(tests) - failures}/{len(tests)} passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(run_standalone())
