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
poster = _load("weekly_digest_post", HERE / "post-to-slack.py")

POLICY = {"warn_days": 14, "close_days": 21,
          "escalate_to": {"tools": "CamSoper", "docs-guild": "tatcoo-pulumi", "blog": "cnunciato"}}


def pr(n, *, labels=(), draft=False, age=3, checks="green", bot=False, title=None, sentinel="blocked"):
    return {"number": n, "title": title or f"PR {n}", "author": "bot" if bot else "someone",
            "age_days": age, "updated_days": 1, "labels": list(labels), "isDraft": draft,
            "checks": checks, "is_bot": bot, "sentinel": sentinel}


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
                pr(20, labels=["review:no-blockers"], sentinel="ready"), pr(21, age=40), pr(22, draft=True),
                pr(23, bot=True, sentinel="ready"), pr(24, bot=True)],
        "issues": {"all_open_count": 50, "new_this_week": [
            {"number": 900, "title": "Broken link", "author": "x", "age_days": 1, "needs_triage": True}],
            "oldest_open": [{"number": 1, "title": "old", "age_days": 1800}],
            "opened_last_7d": 5, "closed_last_7d": 9},
        "throughput": {"this_week": {"prs_opened": 30, "prs_merged": 28, "prs_closed": 4,
                                     "issues_opened": 5, "issues_closed": 9},
                       "prev_week": {"prs_opened": 25, "prs_merged": 20, "prs_closed": 3,
                                     "issues_opened": 6, "issues_closed": 4}},
        "workflow_failures": {"total_runs": 100, "failing": [
            {"workflow": "Audit Logs", "runs": 4, "failures": 4, "streak": 4, "last_failure_url": "https://x/run/1"},
            {"workflow": "Deploy", "runs": 50, "failures": 2, "streak": 0, "last_failure_url": "https://x/run/2"}]},
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
        "review_queues": [
            {"role": "docs-guild", "team": "pulumi/docs-guild", "count": 13, "url": "https://github.com/pulumi/docs/pulls?q=a"},
            {"role": "tools", "team": "pulumi/docs-tools", "count": None, "url": "https://github.com/pulumi/docs/pulls?q=b"},
        ],
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
    assert sla["policy"] == {"warn_days": 14, "close_days": 21, "escalate_to": POLICY["escalate_to"]}


def test_workflow_failures_sorts_newest_first_and_tracks_the_streak():
    # Two `gh run list` calls are concatenated, so input order isn't time order.
    wf = digest.shape_workflow_failures([
        {"workflowName": "A", "status": "completed", "conclusion": "success", "createdAt": "2026-09-20", "url": "u0"},
        {"workflowName": "A", "status": "completed", "conclusion": "failure", "createdAt": "2026-09-27", "url": "u2"},
        {"workflowName": "A", "status": "completed", "conclusion": "failure", "createdAt": "2026-09-26", "url": "u1"},
        {"workflowName": "B", "status": "completed", "conclusion": "failure", "createdAt": "2026-09-22", "url": "b0"},
        {"workflowName": "B", "status": "completed", "conclusion": "success", "createdAt": "2026-09-25"},
        {"workflowName": "B", "status": "completed", "conclusion": "skipped", "createdAt": "2026-09-26"},
        {"workflowName": "C", "status": "in_progress", "conclusion": "", "createdAt": "2026-09-27"},
    ])
    assert wf["total_runs"] == 5  # the skipped run doesn't count
    a, b = wf["failing"]
    assert (a["workflow"], a["streak"], a["last_failure_url"]) == ("A", 2, "u2")
    assert (b["workflow"], b["streak"], b["failures"], b["runs"]) == ("B", 0, 1, 3)


def test_broken_workflow_promoted_flaky_collapsed():
    msg = render.render(base_digest(), None)
    top = msg.split("*Needs a human*")[1].split("\n\n")[0]
    assert "Audit Logs" in top and "failed its last 4 runs" in top
    line = next(line for line in msg.splitlines() if line.startswith("*Failed runs*"))
    assert line == "*Failed runs* (scheduled + master): 1 flaky (2 of 100 runs)"


# ---- render.py ---------------------------------------------------------------


def test_each_pr_appears_once():
    msg = render.render(base_digest())
    for n in (10, 13, 15, 20, 21, 30, 12):
        assert msg.count(f"/pull/{n}|") == 1, n


def test_multi_role_pr_groups_under_its_worst_breach():
    view = render.build_view(base_digest())
    c = next(c for c in view["candidates"] if c["number"] == 10)
    assert c["role"] == "tools"  # 3 over a 1bd SLA beats 1 over a 3bd SLA
    assert c["facts"] == "tools review 4bd on a 1bd SLA → CamSoper; also overdue: docs-guild → tatcoo-pulumi"


def test_same_age_batch_compresses():
    d = base_digest()
    d["sla"]["verdicts"] += [{"pr": 40 + i, "kind": "reviewer", "roles": [],
                              "overdue": [{"role": "docs-guild", "waited": 5, "sla": 3, "escalate_to": "t"}]}
                             for i in range(6)]
    d["prs"] += [pr(40 + i) for i in range(6)]
    msg = render.render(d, {"order": [{"ref": "pr:30", "why": "x"}]})
    line = next(line for line in msg.splitlines() if line.startswith("• docs-guild"))
    assert line.startswith("• docs-guild → tatcoo-pulumi (SLA 3bd): 7 PRs at 5bd: ") and "+3 more" in line


def test_red_ci_pr_is_named_not_hidden():
    d = base_digest()
    d["sla"]["verdicts"] += [{"pr": 40 + i, "kind": "reviewer", "roles": [],
                              "overdue": [{"role": "docs-guild", "waited": 5, "sla": 3, "escalate_to": "t"}]}
                             for i in range(6)]
    d["prs"] += [pr(40 + i, checks="red" if i == 5 else "green") for i in range(6)]
    msg = render.render(d, {"order": [{"ref": "pr:30", "why": "x"}]})
    line = next(line for line in msg.splitlines() if line.startswith("• docs-guild"))
    assert line.split(": ", 2)[2].startswith("<https://github.com/pulumi/docs/pull/45|#45> red CI")


def test_fallback_order_is_priority_then_severity():
    view = render.build_view(base_digest())
    top, source = render.resolve_ranking(view["candidates"], None)
    assert source == "fallback"
    assert [t["ref"] for t in top] == ["pr:30", "workflow:Audit Logs", "pr:13", "pr:12", "pr:10"]


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
    assert "close or rescue it by hand" in off and "closes in" not in off
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
    assert "*Abandoned* (author idle >14d)" in msg and "close or rescue it by hand" in msg


def test_sentinel_state_reads_the_gate():
    run = lambda concl, title, at="2026-09-28T10:00:00Z": {
        "name": "Sentinel", "status": "completed", "conclusion": concl,
        "completed_at": at, "output": {"title": title}}
    assert digest.sentinel_state([]) == "none"
    assert digest.sentinel_state([run("success", "All gates green")]) == "ready"
    assert digest.sentinel_state([run("neutral", "Preview — would be: success (not enforced yet)")]) == "ready"
    assert digest.sentinel_state([run("neutral", "Preview — would be: failure (not enforced yet)")]) == "blocked"
    # the newest run wins
    assert digest.sentinel_state([
        run("neutral", "Preview — would be: success", "2026-09-28T09:00:00Z"),
        run("neutral", "Preview — would be: failure", "2026-09-28T11:00:00Z")]) == "blocked"
    assert digest.sentinel_state([{"name": "sentinel", "status": "completed", "conclusion": "success"}]) == "none"


def test_ready_line_lists_humans_and_counts_bots():
    msg = render.render(base_digest(), None)
    line = next(l for l in msg.splitlines() if l.startswith("*Ready to merge*"))
    assert line == "*Ready to merge* (1, Sentinel green): <https://github.com/pulumi/docs/pull/20|#20> · +1 bot PR"


def test_ready_line_none_and_unreadable():
    d = base_digest()
    for p in d["prs"]:
        p["sentinel"] = "blocked"
    assert "*Ready to merge*: none\n" in render.render(d, None)
    for p in d["prs"]:
        p["sentinel"] = "unknown"
    assert ":warning: *Ready to merge*: Sentinel verdicts unreadable" in render.render(d, None)


def test_ready_pr_is_not_also_overdue():
    d = base_digest()
    d["prs"][0]["sentinel"] = "ready"  # PR 10: overdue for tools per the sweep
    msg = render.render(d, None)
    assert msg.count("/pull/10|") == 1
    assert "*Ready to merge* (2, Sentinel green)" in msg


def test_review_queue_links_carry_their_counts():
    msg = render.render(base_digest(), None)
    line = next(l for l in msg.splitlines() if l.startswith("*Awaiting review*"))
    assert line == ("*Awaiting review* (no blockers, team requested): "
                    "<https://github.com/pulumi/docs/pulls?q=a|docs-guild 13> · "
                    "<https://github.com/pulumi/docs/pulls?q=b|tools ?>")


def test_review_queue_search_matches_the_link():
    q = "is:pr is:open -is:draft label:review:no-blockers team-review-requested:pulumi/docs-guild"
    assert digest.search_url(q) == (
        "https://github.com/pulumi/docs/pulls?q=is%3Apr+is%3Aopen+-is%3Adraft+label%3Areview%3Ano-blockers"
        "+team-review-requested%3Apulumi%2Fdocs-guild")


def test_blog_prs_are_no_longer_collapsed():
    msg = render.render(base_digest(), None)
    assert "Blog/marketing" not in msg
    assert "/pull/12|" in msg and "blog review 20bd on a 3bd SLA → cnunciato" in msg


def test_no_verdicts_never_says_merge_it():
    # C&C review F1: with SLA verdicts missing, every green no-blockers PR
    # looked verdict-free and was offered as "merge it".
    d = base_digest(sla={"available": False, "enabled": "on"})
    kinds = {c["kind"] for c in render.build_view(d)["candidates"]}
    assert "keep-or-kill" not in kinds
    assert "merge it" not in render.render(d, None)


def test_close_without_projection_reads_next_sweep():
    d = base_digest()
    rec = sweep_record()
    rec["actions"][3]["action"] = {"type": "close", "idle_days": 23.0}
    d["sla"] = digest.shape_sla(rec, POLICY, "on")
    msg = render.render(d, None)
    assert "closes at the next sweep" in msg and "None" not in msg


def test_unknown_sweep_state_never_reads_as_off():
    d = base_digest(switches=digest.shape_switches(None))
    d["sla"] = digest.shape_sla(sweep_record(), POLICY, "unknown")
    msg = render.render(d, None)
    assert "closes on its own only if the SLA sweep is on" in msg
    assert "off:" not in msg and "unknown: SLA sweep" in msg


def test_missing_ledger_is_flagged():
    d = base_digest()
    d["sla"]["ledger"] = False
    assert ":warning: *Review ledger unreadable*" in render.render(d, None)
    d["sla"]["ledger"] = True
    assert "Review ledger unreadable" not in render.render(d, None)


def test_sweep_off_said_once():
    msg = render.render(base_digest(), None)
    assert msg.count("sweep is off") == 0 and msg.count("SLA sweep") == 1  # the Switches line


def test_no_candidates_no_fallback_footer_and_no_delta_suffix_without_data():
    d = base_digest(prs=[], review_outcomes={"available": False}, throughput={},
                    workflow_failures={"total_runs": 5, "failing": []})
    d["issues"]["new_this_week"] = []
    msg = render.render(d, {})
    assert "Nothing this week." in msg and "model ranking unavailable" not in msg
    assert "vs last week" not in msg


def test_sla_unavailable_is_loud():
    msg = render.render(base_digest(sla={"available": False, "enabled": "off"}), None)
    assert ":warning: SLA verdicts unavailable" in msg
    assert "overdue and abandoned lists are missing" in msg
    # Ready to merge comes from Sentinel, not the sweep, so it survives.
    assert "*Ready to merge* (1, Sentinel green)" in msg


def test_sla_unavailable_never_claims_within_sla():
    # Without verdicts nothing is known to be within SLA; the footer must
    # not reassure about PRs that may be the most overdue in the queue.
    for ranking in (None, {}):
        msg = render.render(base_digest(sla={"available": False, "enabled": "off"}), ranking)
        assert "within SLA" not in msg and "other open" in msg
    assert "in progress within SLA" in render.render(base_digest(), None)


def test_switch_line_lists_only_whats_off():
    msg = render.render(base_digest(), None)
    line = next(line for line in msg.splitlines() if line.startswith("*Switches*"))
    assert line.startswith("*Switches*: off: SLA sweep, blog review index; unknown: content review")
    assert "ledger" not in line


def test_titles_are_escaped_for_mrkdwn():
    d = base_digest()
    d["prs"][0]["title"] = "Fix <script> & a|b"
    msg = render.render(d, None)
    assert "Fix &lt;script&gt; &amp; a/b" in msg


def test_fits_in_one_slack_message():
    assert len(render.render(base_digest(), None)) < 3500


# ---- thread reply -------------------------------------------------------------


def _many_overdue(d, count=7):
    d["sla"]["verdicts"] += [{"pr": 40 + i, "kind": "reviewer", "roles": [],
                              "overdue": [{"role": "docs-guild", "waited": 5, "sla": 3, "escalate_to": "t"}]}
                             for i in range(count)]
    d["prs"] += [pr(40 + i, title=f"HCL tabs part {i}") for i in range(count)]
    return d


def test_every_cut_list_lands_in_the_thread():
    d = _many_overdue(base_digest())
    msg, thread = render.render_parts(d, {"order": [{"ref": "pr:30", "why": "x"}]})
    line = next(l for l in msg.splitlines() if l.startswith("• docs-guild"))
    assert line.endswith("· +4 more in thread")
    assert "*Over review SLA*: docs-guild → tatcoo-pulumi (SLA 3bd)" in thread
    for i in range(7):
        assert f"/pull/{40 + i}|#{40 + i} HCL tabs part {i}> — 5bd" in thread


def test_needs_a_human_says_top_n_and_continues_in_thread():
    msg, thread = render.render_parts(base_digest(), None)
    total = len(render.build_view(base_digest())["candidates"])
    assert f"*Needs a human* (top 5 of {total})" in msg
    assert f"_+{total - 5} more in thread_" in msg
    assert f"*Needs a human*, 6–{total} (fixed priority order)" in thread
    assert "\n6. <" in thread


def test_no_cuts_no_thread():
    d = base_digest(review_outcomes={"available": False})
    d["issues"]["new_this_week"] = []
    d["workflow_failures"] = {"total_runs": 5, "failing": []}
    d["prs"] = [pr(20, labels=["review:no-blockers"], sentinel="ready")]
    d["sla"]["verdicts"] = []
    msg, thread = render.render_parts(d, None)
    assert thread == "" and "in thread" not in msg


def test_poster_args():
    assert poster.parse_args(["m.txt"]) == ("m.txt", None, False)
    assert poster.parse_args(["m.txt", "--thread", "t.txt", "--dry-run"]) == ("m.txt", "t.txt", True)


def test_poster_threads_replies_under_the_first_message(monkeypatch, tmp_path):
    msg, thr = tmp_path / "m.txt", tmp_path / "t.txt"
    msg.write_text("digest")
    thr.write_text("full lists")
    calls = []

    def fake_post(token, channel, text, retries=3, thread_ts=None):
        calls.append((channel, text, thread_ts))
        return {"ok": True, "ts": "111.222", "channel": "C123"}

    monkeypatch.setattr(poster, "post_chunk", fake_post)
    monkeypatch.setattr(poster, "_force_ipv4", lambda: None)
    monkeypatch.setenv("SLACK_ACCESS_TOKEN", "x")
    monkeypatch.setattr(sys, "argv", ["post", str(msg), "--thread", str(thr)])
    poster.main()
    assert calls == [("#docs-ops", "digest", None), ("C123", "full lists", "111.222")]


def test_poster_skips_empty_thread(monkeypatch, tmp_path):
    msg, thr = tmp_path / "m.txt", tmp_path / "t.txt"
    msg.write_text("digest")
    thr.write_text("")
    calls = []
    monkeypatch.setattr(poster, "post_chunk", lambda *a, **k: calls.append(k) or {"ok": True, "ts": "1"})
    monkeypatch.setattr(poster, "_force_ipv4", lambda: None)
    monkeypatch.setenv("SLACK_ACCESS_TOKEN", "x")
    monkeypatch.setattr(sys, "argv", ["post", str(msg), "--thread", str(thr)])
    poster.main()
    assert len(calls) == 1


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


def test_rank_main_is_never_fatal():
    # C&C review F4: an exception outside the old except list
    # (IncompleteRead, AttributeError on a malformed body) must still print
    # {} and exit 0, or `set -euo pipefail` fails the whole digest job.
    import io
    import json
    import os
    import tempfile

    def boom(*_a, **_k):
        raise AttributeError("'NoneType' object has no attribute 'get'")

    saved = (rank.rank, sys.argv, sys.stdout, sys.stderr, os.environ.get("ANTHROPIC_API_KEY"))
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump([{"ref": "pr:1", "kind": "overdue", "title": "t", "facts": "f"}], f)
    try:
        rank.rank, sys.argv, sys.stdout, sys.stderr = boom, ["rank.py", f.name], io.StringIO(), io.StringIO()
        os.environ["ANTHROPIC_API_KEY"] = "test"
        rc = rank.main()
        out = sys.stdout.getvalue()
    finally:
        rank.rank, sys.argv, sys.stdout, sys.stderr = saved[:4]
        if saved[4] is None:
            os.environ.pop("ANTHROPIC_API_KEY", None)
        else:
            os.environ["ANTHROPIC_API_KEY"] = saved[4]
        os.unlink(f.name)
    assert rc == 0 and out.strip() == "{}"


def run_standalone() -> int:
    import inspect  # noqa: PLC0415
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)
             and not inspect.signature(v).parameters]  # fixture tests run under pytest only
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
