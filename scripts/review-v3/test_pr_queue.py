#!/usr/bin/env python3
"""Tests for pr_queue.py — the shared queue's labels and its publish step —
plus the invariants pr-queue.yml has to keep.

Runs under pytest (make test-review-pipeline) and standalone via
`pr_queue.py --self-test`. No pytest fixtures. The end-to-end cases collect
and analyze over the snapshot backend (test_analyze.run), so the label
mapper always sees the record analyze.py writes.
"""

from __future__ import annotations

import json
import re
import sys
import tempfile
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))
import collect  # noqa: E402
import pr_queue  # noqa: E402
import sentinel  # noqa: E402
import test_analyze as ta  # noqa: E402
from gh_client import GhClient, GhError  # noqa: E402
from test_collect import make_snapshot  # noqa: E402

WORKFLOW = REPO_ROOT / ".github" / "workflows" / "pr-queue.yml"


def q_row(n, verdict, roles=("docs-guild",), lines=1):
    return {"number": n, "verdict": verdict, "roles": list(roles), "changed_lines": lines}


def queue_of(rows, clusters=(), directional=(), errors=()):
    return {"prs": list(rows), "clusters": list(clusters), "directional": list(directional), "errors": list(errors)}


def overlap(a, b, kind="overlap"):
    return {"id": "C1", "prs": sorted((a, b)), "pairs": [{"a": min(a, b), "b": max(a, b), "kind": kind, "paths": ["x.md"]}]}


class FakeGh:
    """The four calls pr_queue.py makes, recorded."""

    def __init__(self, labels=(), open_prs=(), fail_on=()):
        self.repo = "pulumi/docs"
        self.labels = [{"name": l} for l in labels]
        self.open = list(open_prs)
        self.fail_on = set(fail_on)
        self.calls = []

    def get(self, path, params=None, *, paginate=False):
        assert path == "repos/pulumi/docs/labels"
        return self.labels

    def list_open_prs(self):
        return self.open

    def post(self, path, body=None):
        if path in self.fail_on:
            raise GhError(f"boom {path}", 500)
        self.calls.append(("POST", path, body))
        return {}

    def delete(self, path, body=None):
        if path in self.fail_on:
            raise GhError(f"boom {path}", 500)
        self.calls.append(("DELETE", path, None))
        return {}


# ---- desired labels --------------------------------------------------------


def test_one_verdict_label_per_row_and_route_labels_only_where_a_team_decides():
    q = queue_of([q_row(1, "stamp"), q_row(2, "judge", roles=("marketing", "tools")), q_row(3, "blocked"),
                  q_row(4, "route", roles=("blog",))])
    want = pr_queue.desired_labels(q)
    assert want[1] == {"queue:stamp", "queue:route:docs-guild"}
    assert want[2] == {"queue:judge", "queue:route:marketing", "queue:route:tools"}
    # a blocked row's next move is the author's or a re-run's, not a team's
    assert want[3] == {"queue:blocked"}
    # `route` never happens on the shared board (--owner any); if it ever
    # does, it gets no verdict label rather than an invented one
    assert want[4] == set()


def test_overlap_labels_only_the_pr_that_waits():
    q = queue_of([q_row(10, "judge", lines=50), q_row(11, "judge", lines=3)], clusters=[overlap(10, 11)])
    want = pr_queue.desired_labels(q)
    # fewest changed lines merges first (analyze.collision_clusters' order)
    assert "queue:collides-with-#11" in want[10]
    assert not any(l.startswith("queue:collides-with-") for l in want[11])


def test_merge_order_ties_break_on_pr_number():
    q = queue_of([q_row(20, "judge", lines=5), q_row(21, "judge", lines=5)], clusters=[overlap(20, 21)])
    want = pr_queue.desired_labels(q)
    assert "queue:collides-with-#20" in want[21] and "queue:collides-with-#21" not in want[20]


def test_same_file_pairs_are_not_labelled():
    q = queue_of([q_row(1, "stamp"), q_row(2, "stamp", lines=9)], clusters=[overlap(1, 2, kind="same-file")])
    want = pr_queue.desired_labels(q)
    assert not any(l.startswith("queue:collides") for ls in want.values() for l in ls)


def test_directional_conflict_makes_the_link_adder_wait():
    q = queue_of([q_row(1, "judge"), q_row(2, "stamp")],
                 directional=[{"path": "/docs/old/", "adds_links_pr": 1, "removes_links_pr": 2, "theirs": False}])
    want = pr_queue.desired_labels(q)
    assert "queue:collides-with-#2" in want[1] and want[2] == {"queue:stamp", "queue:route:docs-guild"}


def test_no_label_set_can_deadlock_two_prs():
    """Overlap says 2 waits on 1 (more lines); a directional conflict says
    1 waits on 2. Labelling both would leave each red until the other
    merged. The directional edge that closes the cycle is dropped and
    reported instead."""
    q = queue_of([q_row(1, "judge", lines=1), q_row(2, "judge", lines=9)], clusters=[overlap(1, 2)],
                 directional=[{"path": "/docs/x/", "adds_links_pr": 1, "removes_links_pr": 2, "theirs": False}])
    edges, dropped = pr_queue.wait_edges(q)
    assert edges == {2: {1}}
    assert dropped == [{"waiter": 1, "blocker": 2, "path": "/docs/x/", "why": "would close a wait cycle"}]
    # two directional edges against each other: the first in sorted order wins
    q = queue_of([q_row(5, "judge"), q_row(6, "judge")],
                 directional=[{"path": "/a/", "adds_links_pr": 6, "removes_links_pr": 5},
                              {"path": "/b/", "adds_links_pr": 5, "removes_links_pr": 6}])
    edges, dropped = pr_queue.wait_edges(q)
    assert edges == {5: {6}} and [(d["waiter"], d["blocker"]) for d in dropped] == [(6, 5)]


def test_wait_graph_is_acyclic_over_a_chain():
    rows = [q_row(n, "judge", lines=n) for n in (1, 2, 3, 4)]
    clusters = [overlap(1, 2), overlap(2, 3), overlap(3, 4), overlap(1, 4)]
    directional = [{"path": "/p/", "adds_links_pr": 1, "removes_links_pr": 4}]
    edges, dropped = pr_queue.wait_edges(queue_of(rows, clusters=clusters, directional=directional))
    for start in edges:
        for nxt in edges[start]:
            assert not pr_queue._reaches(edges, nxt, start), f"cycle through #{start} → #{nxt}"
    assert dropped and dropped[0]["waiter"] == 1


def test_collision_label_round_trips_through_the_sentinel_parser():
    assert pr_queue.COLLIDES_PREFIX == sentinel.COLLIDES_LABEL_PREFIX
    label = f"{pr_queue.COLLIDES_PREFIX}21641"
    assert pr_queue.collides_target(label) == 21641
    assert sentinel.collides_with({label, "queue:judge", "queue:collides-with-#x"}) == [21641]


# ---- the plan ---------------------------------------------------------------


def open_pr(n, *labels):
    return {"number": n, "labels": [{"name": l} for l in labels]}


def test_plan_touches_only_queue_labels_and_diffs_against_live_labels():
    q = queue_of([q_row(1, "stamp"), q_row(2, "blocked")])
    live = [open_pr(1, "domain:docs", "review:no-blockers", "queue:blocked"),
            open_pr(2, "queue:blocked", "needs-author-response")]
    plan = pr_queue.label_plan(q, live)
    assert plan == [{"pr": 1, "add": ["queue:route:docs-guild", "queue:stamp"], "remove": ["queue:blocked"],
                     "collides_changed": False}]


def test_plan_strips_a_pr_that_left_the_queue_and_skips_one_collect_could_not_read():
    q = queue_of([q_row(1, "stamp")], errors=[{"pr": 3, "error": "HTTP 502"}])
    live = [open_pr(1, "queue:stamp", "queue:route:docs-guild"),
            open_pr(2, "queue:judge", "queue:collides-with-#1"),  # converted to draft: not collected
            open_pr(3, "queue:judge")]                             # collect errored: unknown, leave it
    plan = pr_queue.label_plan(q, live)
    assert plan == [{"pr": 2, "add": [], "remove": ["queue:collides-with-#1", "queue:judge"], "collides_changed": True}]


def test_apply_creates_missing_labels_first_and_encodes_names():
    gh = FakeGh(labels=["queue:stamp", "queue:collides-with-#7"], open_prs=[open_pr(5), open_pr(9)])
    gh._pr_queue_open = gh.open
    plan = [{"pr": 5, "add": ["queue:collides-with-#9", "queue:stamp"], "remove": ["queue:judge"], "collides_changed": True}]
    res = pr_queue.apply_plan(gh, plan, apply=True)
    assert res["created"] == ["queue:collides-with-#9"]
    first = gh.calls[0]
    assert first[0] == "POST" and first[1] == "repos/pulumi/docs/labels" and first[2]["name"] == "queue:collides-with-#9"
    assert first[2]["color"] == "d93f0b" and "#9" in first[2]["description"]
    assert ("POST", "repos/pulumi/docs/issues/5/labels", {"labels": ["queue:collides-with-#9", "queue:stamp"]}) in gh.calls
    assert ("DELETE", "repos/pulumi/docs/issues/5/labels/queue%3Ajudge", None) in gh.calls
    # #7 is not open any more: its label definition is pruned, encoded
    assert res["pruned"] == ["queue:collides-with-#7"]
    assert ("DELETE", "repos/pulumi/docs/labels/" + urllib.parse.quote("queue:collides-with-#7", safe=""), None) in gh.calls
    assert "%23" in gh.calls[-1][1]  # a raw '#' would cut the path at a URL fragment


def test_dry_run_writes_nothing_and_reports_the_same_plan():
    gh = FakeGh(labels=[], open_prs=[open_pr(5)])
    gh._pr_queue_open = gh.open
    plan = [{"pr": 5, "add": ["queue:stamp"], "remove": [], "collides_changed": False}]
    res = pr_queue.apply_plan(gh, plan, apply=False)
    assert gh.calls == [] and res["created"] == ["queue:stamp"] and res["applied"] == plan


def test_one_failed_pr_does_not_stop_the_rest():
    gh = FakeGh(labels=["queue:stamp"], open_prs=[open_pr(1), open_pr(2)], fail_on={"repos/pulumi/docs/issues/1/labels"})
    gh._pr_queue_open = gh.open
    plan = [{"pr": 1, "add": ["queue:stamp"], "remove": [], "collides_changed": True},
            {"pr": 2, "add": ["queue:stamp"], "remove": [], "collides_changed": True}]
    res = pr_queue.apply_plan(gh, plan, apply=True)
    assert [f["pr"] for f in res["failed"]] == [1] and [s["pr"] for s in res["applied"]] == [2]


def test_cli_writes_changed_prs_only_when_applying():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        snap = root / "snap"
        (snap / "GET" / "repos" / "pulumi" / "docs").mkdir(parents=True)
        (snap / "GET" / "repos" / "pulumi" / "docs" / "pulls__state=open.json").write_text(
            json.dumps([open_pr(10), open_pr(11)]))
        (snap / "GET" / "repos" / "pulumi" / "docs" / "labels.json").write_text("[]")
        qf = root / "q.json"
        qf.write_text(json.dumps({**queue_of([q_row(10, "judge", lines=50), q_row(11, "judge", lines=3)],
                                             clusters=[overlap(10, 11)]), "repo": "pulumi/docs"}))
        changed = root / "changed.txt"
        base = ["labels", "--in", str(qf), "--backend", "snapshot", "--snapshot-dir", str(snap), "--changed-out", str(changed)]
        assert pr_queue.main(base) == 0
        assert changed.read_text() == "" and not (snap / "writes.jsonl").exists()
        assert pr_queue.main(base + ["--apply"]) == 0
        assert changed.read_text() == "10\n"
        writes = [json.loads(l) for l in (snap / "writes.jsonl").read_text().splitlines()]
        assert {"method": "POST", "path": "repos/pulumi/docs/issues/10/labels",
                "body": {"labels": ["queue:collides-with-#11", "queue:judge", "queue:route:docs-guild"]}} in writes


# ---- end to end over analyze.py ---------------------------------------------


def test_end_to_end_over_a_shared_collect():
    """The workflow's own shape: collect --shared (no approver), analyze
    --owner any. Two overlapping PRs and one clean one."""
    a = ta.fresh(1, files=[ta._file("content/docs/a.md", ["x"], ["o"], old_start=10)])
    b = ta.fresh(2, files=[ta._file("content/docs/a.md", ["y", "z"], ["o"], old_start=10)])
    c = ta.fresh(3)
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        make_snapshot(root, [a, b, c])
        gh = GhClient("pulumi/docs", "snapshot", snapshot_dir=root)
        q = collect.collect(gh, cache_dir=None, repo_root=root, workers=1, shared=True)
    assert q["approver"] is None and q["shared"] is True
    q = ta.analyze.analyze(q, ta.cfg(), config=ta.CONFIG, repo_root=REPO_ROOT, owner="any", aliases=set(), today=ta.TODAY)
    assert {p["verdict"] for p in q["prs"]} <= {"stamp", "judge", "blocked"}  # never route on the shared board
    want = pr_queue.desired_labels(q)
    assert "queue:collides-with-#1" in want[2] and not any(l.startswith("queue:collides") for l in want[1])
    assert want[3] == {"queue:stamp", "queue:route:docs-guild"}


def test_collect_shared_never_asks_the_token_who_it_is():
    class NoMe(GhClient):
        def me(self):
            raise AssertionError("shared collect must not call GET /user")
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        make_snapshot(root, [ta.fresh(1)])
        q = collect.collect(NoMe("pulumi/docs", "snapshot", snapshot_dir=root), cache_dir=None, repo_root=root,
                            workers=1, shared=True)
    assert q["approver"] is None and q["my_teams"] == {}


# ---- publish ----------------------------------------------------------------


def test_publish_without_a_bucket_writes_local_files_and_never_fails():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / "q.json").write_text('{"prs": []}')
        (root / "b.html").write_text("<html></html>")
        calls = []
        res = pr_queue.publish(root / "q.json", root / "b.html", out_dir=root / "out", uri=None,
                               uploader=lambda *a: calls.append(a))
        assert calls == [] and res["uploaded"] == []
        assert (root / "out" / "queue.json").read_text() == '{"prs": []}'
        assert (root / "out" / "board.html").exists()


def test_publish_keys_and_a_failed_upload_is_a_warning():
    now = datetime(2026, 10, 19, 14, 17, 3, tzinfo=timezone.utc)
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / "q.json").write_text('{"prs": []}')
        (root / "b.html").write_text("<html></html>")
        seen = []

        def up(path, dest, ctype):
            seen.append((dest, ctype))
            if dest.endswith("board.html"):
                raise RuntimeError("AccessDenied")
        res = pr_queue.publish(root / "q.json", root / "b.html", out_dir=root / "out",
                               uri="s3://ledger/pr-review/", now=now, uploader=up)
    assert [d for d, _ in seen] == ["s3://ledger/pr-review/queue/queue.json",
                                    "s3://ledger/pr-review/queue/runs/2026-10-19/20261019T141703Z.json",
                                    "s3://ledger/pr-review/queue/board.html"]
    assert dict(seen)["s3://ledger/pr-review/queue/board.html"].startswith("text/html")
    assert res["failed"] == ["s3://ledger/pr-review/queue/board.html"] and len(res["uploaded"]) == 2


def test_publish_refuses_a_corrupt_queue():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / "q.json").write_text("{not json")
        try:
            pr_queue.publish(root / "q.json", None, out_dir=root / "out", uri=None)
        except json.JSONDecodeError:
            pass
        else:
            raise AssertionError("a corrupt queue must not publish")
        assert not (root / "out" / "queue.json").exists()


# ---- pr-queue.yml invariants --------------------------------------------------


def _wf() -> str:
    return WORKFLOW.read_text()


def test_workflow_runs_the_phase_one_scripts_not_a_fork_of_them():
    wf = _wf()
    assert "scripts/review-v3/collect.py" in wf and "--shared" in wf
    assert "scripts/review-v3/analyze.py --in .pr-review-queue.json --owner any" in wf
    assert "scripts/review-v3/render.py" in wf and "scripts/review-v3/pr_queue.py" in wf
    # the judge step is a model call and stays out of CI
    assert "--judgments" not in wf and "claude-code-action" not in wf


def test_workflow_never_checks_out_pr_code():
    wf = _wf()
    for forbidden in ("github.event.pull_request.head", "github.head_ref", "refs/pull/", "merge_commit_sha"):
        assert forbidden not in wf, forbidden
    assert wf.count("actions/checkout@") == 1
    assert "ref: ${{ github.event.repository.default_branch }}" in wf


def test_pr_events_only_poke_and_the_heavy_job_never_runs_on_them():
    import yaml  # noqa: PLC0415
    doc = yaml.safe_load(_wf())
    jobs = doc["jobs"]
    poke_steps = jobs["poke"]["steps"]
    assert len(poke_steps) == 1 and "uses" not in poke_steps[0]
    assert "gh workflow run pr-queue.yml" in poke_steps[0]["run"]
    assert "pull_request_target" in jobs["poke"]["if"]
    assert "pull_request_target" not in jobs["queue"]["if"]
    assert jobs["queue"]["concurrency"] == {"group": "pr-queue", "cancel-in-progress": True}
    assert "concurrency" not in jobs["poke"]  # a cancelled poke would show on the PR


def test_switches_compare_against_literals():
    wf = _wf()
    assert "vars.PR_QUEUE != " not in wf and "vars.REVIEW_V3_SENTINEL != " not in wf
    assert re.search(r"vars\.PR_QUEUE == '1'", wf) and re.search(r"vars\.PR_QUEUE == 'report'", wf)
    # labels are written only on '1' or an explicit dispatch input
    assert 'if [ "$PR_QUEUE" = "1" ]; then' in wf and '"$INPUT_APPLY" = "true"' in wf


def test_sentinel_workflow_re_reads_collision_labels_and_has_its_own_switch():
    wf = (REPO_ROOT / ".github" / "workflows" / "review-sentinel.yml").read_text()
    assert f"startsWith(github.event.label.name, '{sentinel.COLLIDES_LABEL_PREFIX}')" in wf
    assert "vars.REVIEW_V3_COLLISION_GATE == '1'" in wf and "--collision-gate" in wf


def test_label_taxonomy_documents_the_queue_family():
    doc = (REPO_ROOT / ".github" / "labels-pr-review.md").read_text()
    for name in ("queue:stamp", "queue:judge", "queue:blocked", "queue:route:", "queue:collides-with-#"):
        assert f"`{name}" in doc, name


def run_standalone() -> int:
    """The --self-test harness; test list bound at call time (test_sentinel.py)."""
    import inspect  # noqa: PLC0415
    all_tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    failures = 0
    for t in all_tests:
        if inspect.signature(t).parameters:
            print(f"  skip: {t.__name__} (pytest fixtures; run via pytest)")
            continue
        try:
            t()
            print(f"  ok: {t.__name__}")
        except AssertionError as exc:
            failures += 1
            print(f"  FAIL: {t.__name__}: {exc}", file=sys.stderr)
        except Exception as exc:  # noqa: BLE001
            failures += 1
            print(f"  FAIL: {t.__name__}: {type(exc).__name__}: {exc}", file=sys.stderr)
    if failures:
        print(f"{failures} pr_queue test(s) failed", file=sys.stderr)
        return 1
    print("all pr_queue self-tests passed")
    return 0


if __name__ == "__main__":
    sys.exit(run_standalone())
