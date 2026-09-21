#!/usr/bin/env python3
"""Tests for staging-sweep.py — candidate selection, per-SHA verdicts, the
idempotence contract, the Sentinel poke, and the workflow wiring that carries
it.

Runs under pytest (make test-review-pipeline) and standalone via
`staging-sweep.py --self-test` (run_standalone below, same convention as
test_sentinel.py and test_sla_sweep.py). No pytest fixtures are used, so
every test also runs unmodified outside pytest.

The GitHub surface is a hand-written snapshot directory read through
`GhClient`'s snapshot backend — the same seam act.py's tests use. Writes are
recorded on `gh.writes` on every backend, so "did it poke?" and "did it write
a status?" are assertions about a list, not about a mock.
"""

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
REPO_ROOT = HERE.parent.parent


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


staging_sweep = _load("staging_sweep_under_test", HERE / "staging-sweep.py")
from gh_client import GhClient  # noqa: E402

REPO = "pulumi/docs"
NOW = datetime(2026, 9, 21, 23, 30, tzinfo=timezone.utc)
SHA_A = "a" * 40
SHA_B = "b" * 40
BRANCH = "camsoper/some-infra-fix"
BOT = "github-actions[bot]"


def run(sha=SHA_A, *, conclusion="success", event="workflow_dispatch",
        branch=BRANCH, status="completed", updated="2026-09-21T23:00:00Z", rid=1):
    return {"id": rid, "event": event, "status": status, "conclusion": conclusion,
            "head_branch": branch, "head_sha": sha, "updated_at": updated,
            "created_at": updated,
            "html_url": f"https://github.com/{REPO}/actions/runs/{rid}"}


def status_entry(state="success", creator=BOT,
                 context=staging_sweep.STAGING_STATUS_CONTEXT):
    return {"context": context, "state": state, "creator": {"login": creator}}


class Harness:
    """A snapshot dir wired for one sweep, torn down with the test."""

    def __init__(self, runs, statuses=None, prs=None):
        self._tmp = tempfile.TemporaryDirectory()
        root = Path(self._tmp.name)
        self._write(root, "GET", f"repos/{REPO}/actions/workflows/"
                    f"{staging_sweep.STAGING_WORKFLOW_FILE}/runs",
                    {"per_page": 100}, {"workflow_runs": runs})
        for sha, entries in (statuses or {}).items():
            self._write(root, "GET", f"repos/{REPO}/commits/{sha}/statuses",
                        {"per_page": 100}, entries)
        for branch, pr_list in (prs or {}).items():
            self._write(root, "GET", f"repos/{REPO}/pulls",
                        {"state": "open", "head": f"pulumi:{branch}"}, pr_list)
        self.gh = GhClient(REPO, backend="snapshot", snapshot_dir=root)

    @staticmethod
    def _write(root, method, path, params, payload):
        from gh_client import snapshot_path  # noqa: PLC0415
        f = snapshot_path(root, method, path, params)
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(json.dumps(payload))

    def sweep(self, **kw):
        kw.setdefault("default_branch", "master")
        kw.setdefault("now", NOW)
        return staging_sweep.sweep(self.gh, **kw)

    def writes(self, method=None, contains=None):
        out = self.gh.writes
        if method:
            out = [w for w in out if w["method"] == method]
        if contains:
            out = [w for w in out if contains in w["path"]]
        return out

    def close(self):
        self._tmp.cleanup()


def _pr(number=21789, sha=SHA_A, branch=BRANCH):
    return [{"number": number, "head": {"sha": sha, "ref": branch}}]


# ---- candidate selection ------------------------------------------------


def test_only_dispatched_completed_non_default_branch_runs_are_candidates():
    """A master push deploy is nobody's staging evidence.

    Writing `staging/pulumi-test-io` at a default-branch SHA would invent
    evidence for the production-shaped run, and the existing listener's job
    `if` filters exactly these three things off the live event.
    """
    runs = [
        run(SHA_A, rid=1),                                   # keeper
        run(SHA_B, event="push", branch="master", rid=2),    # master push
        run(SHA_B, branch="master", rid=3),                  # dispatch at master
        run(SHA_B, status="in_progress", conclusion=None, rid=4),
    ]
    got = staging_sweep.candidate_runs(runs, default_branch="master", now=NOW,
                                       lookback_hours=6)
    assert [r["id"] for r in got] == [1]


def test_the_lookback_window_bounds_the_work():
    """The window is what stops a pathological retry from running forever."""
    runs = [run(SHA_A, updated="2026-09-21T23:00:00Z", rid=1),
            run(SHA_B, updated="2026-09-20T01:00:00Z", rid=2)]
    got = staging_sweep.candidate_runs(runs, default_branch="master", now=NOW,
                                       lookback_hours=6)
    assert [r["id"] for r in got] == [1]


def test_a_run_with_no_parsable_timestamp_is_skipped_not_crashed():
    runs = [run(SHA_A, updated="not-a-date", rid=1)]
    assert staging_sweep.candidate_runs(runs, default_branch="master", now=NOW,
                                        lookback_hours=6) == []


# ---- per-SHA verdict ----------------------------------------------------


def test_a_success_anywhere_in_a_shas_group_wins():
    """Two deploys of one SHA are one fact.

    `_staging_evidence` accepts ANY successful run at the head, so a flake
    followed by a green retry is green — and so is a green run followed by a
    cancelled one, which is what a displaced re-dispatch looks like.
    """
    grouped = staging_sweep.group_by_head([
        run(SHA_A, conclusion="failure", updated="2026-09-21T21:00:00Z", rid=1),
        run(SHA_A, conclusion="success", updated="2026-09-21T22:00:00Z", rid=2),
        run(SHA_A, conclusion="cancelled", updated="2026-09-21T23:00:00Z", rid=3),
    ])
    assert grouped[SHA_A]["conclusion"] == "success"
    assert grouped[SHA_A]["run_id"] == 2


def test_without_a_success_the_latest_run_is_the_verdict():
    grouped = staging_sweep.group_by_head([
        run(SHA_A, conclusion="cancelled", updated="2026-09-21T21:00:00Z", rid=1),
        run(SHA_A, conclusion="failure", updated="2026-09-21T22:00:00Z", rid=2),
    ])
    assert grouped[SHA_A]["conclusion"] == "failure"
    assert grouped[SHA_A]["run_id"] == 2


def test_the_three_status_descriptions_are_the_established_contract():
    """Readers and scripts have learned these three strings; a fourth
    spelling is a silent break."""
    assert staging_sweep.verdict_for("success") == ("success", "staging deploy green", True)
    assert staging_sweep.verdict_for("cancelled") == ("error", "staging deploy cancelled", False)
    assert staging_sweep.verdict_for("failure") == ("failure", "staging deploy failed", False)
    assert staging_sweep.verdict_for("timed_out") == ("failure", "staging deploy failed", False)


# ---- the fix: a green deploy re-scores G4 -------------------------------


def test_a_successful_deploy_writes_the_status_and_pokes_the_sentinel():
    """The reported bug, end to end: PR #21789's shape.

    A green deploy lands at the PR's current head and nothing re-reads it.
    After this sweep the status exists AND `review-sentinel.yml` has been
    dispatched with that PR number — the same manual action that cleared
    #21789 at 23:04, automated.
    """
    h = Harness([run(SHA_A)], statuses={SHA_A: []}, prs={BRANCH: _pr(21789, SHA_A)})
    try:
        rec = h.sweep()
        assert rec["finalized"] == [{"sha": SHA_A, "branch": BRANCH, "run_id": 1,
                                     "state": "success", "poked": 21789}]

        pokes = h.writes(contains=f"workflows/{staging_sweep.SENTINEL_WORKFLOW_FILE}")
        assert len(pokes) == 1, "exactly one Sentinel dispatch"
        assert pokes[0]["body"] == {"ref": "master", "inputs": {"pr_number": "21789"}}, \
            "the PR number must be explicit — a workflow_run event cannot supply it"

        statuses = h.writes(contains=f"statuses/{SHA_A}")
        assert len(statuses) == 1
        assert statuses[0]["body"]["state"] == "success"
        assert statuses[0]["body"]["context"] == staging_sweep.STAGING_STATUS_CONTEXT
        assert statuses[0]["body"]["target_url"] == staging_sweep.DEPLOYED_SITE_URL
    finally:
        h.close()


def test_the_poke_is_sent_before_the_status_is_written():
    """The status is the idempotence key, so it must be written last.

    Sealing it first would make a poke that failed permanent: the next sweep
    would see "already recorded" and skip the PR forever, which is the exact
    failure this whole workflow exists to prevent.
    """
    h = Harness([run(SHA_A)], statuses={SHA_A: []}, prs={BRANCH: _pr(21789, SHA_A)})
    try:
        h.sweep()
        paths = [w["path"] for w in h.gh.writes]
        poke = next(i for i, p in enumerate(paths) if "review-sentinel" in p)
        status = next(i for i, p in enumerate(paths) if "/statuses/" in p)
        assert poke < status, f"poke must precede the status write: {paths}"
    finally:
        h.close()


def test_a_second_sweep_of_the_same_deploy_does_nothing():
    """Idempotence. This runs every few minutes over an overlapping window;
    re-poking the Sentinel each cycle would be a self-inflicted DoS on the
    merge gate."""
    h = Harness([run(SHA_A)], statuses={SHA_A: [status_entry("success")]},
                prs={BRANCH: _pr(21789, SHA_A)})
    try:
        rec = h.sweep()
        assert rec["finalized"] == []
        assert rec["skipped"] == [{"sha": SHA_A, "reason": "already-recorded",
                                   "state": "success"}]
        assert h.gh.writes == [], "a finalized SHA is not touched again"
    finally:
        h.close()


def test_a_failure_status_does_not_seal_off_a_later_green_retry():
    """The idempotence key is the VERDICT, not the presence of a status.

    A deploy that failed, was retried, and went green must flip the recorded
    state — otherwise the first flake would block the gate permanently.
    """
    h = Harness([run(SHA_A, conclusion="failure", updated="2026-09-21T21:00:00Z", rid=1),
                 run(SHA_A, conclusion="success", updated="2026-09-21T22:00:00Z", rid=2)],
                statuses={SHA_A: [status_entry("failure")]},
                prs={BRANCH: _pr(21789, SHA_A)})
    try:
        rec = h.sweep()
        assert [e["state"] for e in rec["finalized"]] == ["success"]
        assert rec["finalized"][0]["poked"] == 21789
    finally:
        h.close()


def test_an_unauthorized_status_is_not_treated_as_finalized():
    """A commit status needs only push access to write.

    If any author's hand-written status counted as "already recorded", a PR
    could stop the sweep from ever recording the real verdict. sentinel.py
    applies the same writer allowlist when it reads one as evidence.
    """
    h = Harness([run(SHA_A)],
                statuses={SHA_A: [status_entry("success", creator="some-contributor")]},
                prs={BRANCH: _pr(21789, SHA_A)})
    try:
        rec = h.sweep()
        assert [e["state"] for e in rec["finalized"]] == ["success"]
    finally:
        h.close()


def test_a_status_in_another_context_is_ignored():
    h = Harness([run(SHA_A)],
                statuses={SHA_A: [status_entry("success", context="Update Changelog")]},
                prs={BRANCH: _pr(21789, SHA_A)})
    try:
        assert len(h.sweep()["finalized"]) == 1
    finally:
        h.close()


# ---- when NOT to poke ---------------------------------------------------


def test_a_failed_deploy_records_the_status_but_never_pokes():
    """G4 is already red and stays red; re-scoring tells the PR nothing."""
    h = Harness([run(SHA_A, conclusion="failure")], statuses={SHA_A: []},
                prs={BRANCH: _pr(21789, SHA_A)})
    try:
        rec = h.sweep()
        assert rec["finalized"][0]["state"] == "failure"
        assert rec["finalized"][0]["poked"] is None
        assert h.writes(contains="review-sentinel") == []
        body = h.writes(contains=f"statuses/{SHA_A}")[0]["body"]
        assert body["target_url"] == f"https://github.com/{REPO}/actions/runs/1", \
            "a failed deploy has no deployed site to link to"
    finally:
        h.close()


def test_a_moved_head_records_the_status_but_never_pokes():
    """G4 asks about the CURRENT head.

    The push that moved it already re-ran the Sentinel and already triggered
    a fresh deploy, so a poke for the superseded SHA re-scores a head nobody
    is waiting on.
    """
    h = Harness([run(SHA_A)], statuses={SHA_A: []},
                prs={BRANCH: _pr(21789, sha=SHA_B)})
    try:
        rec = h.sweep()
        assert rec["finalized"][0]["poked"] == "stale-head"
        assert h.writes(contains="review-sentinel") == []
        assert len(h.writes(contains=f"statuses/{SHA_A}")) == 1
    finally:
        h.close()


def test_no_open_pr_still_records_the_status():
    """The status belongs to the SHA, not to the PR — a closed or renamed
    branch still gets its verdict recorded. Same rule staging-status.yml
    states."""
    h = Harness([run(SHA_A)], statuses={SHA_A: []}, prs={BRANCH: []})
    try:
        rec = h.sweep()
        assert rec["finalized"][0]["poked"] == "no-open-pr"
        assert len(h.writes(contains=f"statuses/{SHA_A}")) == 1
    finally:
        h.close()


def test_no_poke_flag_writes_statuses_only():
    h = Harness([run(SHA_A)], statuses={SHA_A: []}, prs={BRANCH: _pr(21789, SHA_A)})
    try:
        h.sweep(poke_sentinel=False)
        assert h.writes(contains="review-sentinel") == []
        assert len(h.writes(contains=f"statuses/{SHA_A}")) == 1
    finally:
        h.close()


def test_dry_run_resolves_everything_and_sends_nothing():
    h = Harness([run(SHA_A)], statuses={SHA_A: []}, prs={BRANCH: _pr(21789, SHA_A)})
    try:
        dry = h.gh.dry()
        rec = staging_sweep.sweep(dry, default_branch="master", now=NOW)
        assert rec["finalized"][0]["poked"] == 21789
        assert len(dry.writes) == 2, "recorded, not sent"
        assert not (Path(h.gh.snapshot_dir) / "writes.jsonl").exists()
    finally:
        h.close()


# ---- degradation --------------------------------------------------------


def test_unreadable_run_history_is_one_skipped_cycle_not_a_failure():
    h = Harness([])
    try:
        h.gh.snapshot_dir = Path(tempfile.mkdtemp())  # every GET now 404s
        rec = h.sweep()
        assert rec["finalized"] == [] and "error" in rec
    finally:
        h.close()


def test_unreadable_statuses_skip_that_sha_rather_than_guessing():
    """Writing a verdict without reading the existing one would re-poke every
    cycle."""
    h = Harness([run(SHA_A)], statuses={}, prs={BRANCH: _pr(21789, SHA_A)})
    try:
        rec = h.sweep()
        assert rec["skipped"] == [{"sha": SHA_A, "reason": "statuses-unreadable"}]
        assert h.gh.writes == []
    finally:
        h.close()


# ---- workflow wiring ----------------------------------------------------


def test_the_sweep_runs_on_a_schedule_because_no_cascade_can_be_trusted():
    """The trigger is the fix.

    `workflow_run` is dead here for two independent reasons — GitHub emits no
    cascade for a run dispatched with GITHUB_TOKEN (#21696), and a dispatched
    run's event carries no PR number — and an in-run job is dead for branch
    age (#21676). A `schedule` is immune to all three.
    """
    import yaml as _y  # noqa: PLC0415

    data = _y.safe_load((REPO_ROOT / ".github" / "workflows" / "staging-status.yml").read_text())
    on = data[True]  # `on:` is YAML 1.1 True once parsed — do not "fix" this
    assert "schedule" in on, "a cascade cannot be the only trigger"
    assert on["schedule"] and all("cron" in s for s in on["schedule"])
    # The listener and the backfill entry stay: when a cascade DOES fire it is
    # free latency, and the backfill is how one run gets replayed by hand.
    assert on["workflow_run"]["workflows"] == ["Build and deploy testing"]
    assert "run_id" in on["workflow_dispatch"]["inputs"]

    sweep_job = data["jobs"]["sweep"]
    assert "staging-sweep.py" in json.dumps(sweep_job)
    gate = sweep_job["if"]
    assert "vars.REVIEW_V3_SENTINEL == 'report' || vars.REVIEW_V3_SENTINEL == '1'" in gate, \
        "no Sentinel means no gate to feed"
    assert "concurrency" not in data and "concurrency" not in sweep_job, \
        "a displaced pending run is a CANCELLED run"


def test_the_sweep_never_touches_pr_code():
    """It holds `statuses: write` and `actions: write` over PR-controlled
    heads, exactly like the listener beside it."""
    wf = (REPO_ROOT / ".github" / "workflows" / "staging-status.yml").read_text()
    for forbidden in ("head.ref", "head.sha", "refs/pull/", "merge_commit_sha"):
        assert forbidden not in wf, f"the sweep must never reference PR code: {forbidden}"
    assert wf.count("ref: ${{ github.event.repository.default_branch }}") >= 1, \
        "any checkout here must be pinned to the default branch"


def test_adding_the_deploy_to_the_sentinels_workflow_run_list_is_not_the_fix():
    """The tempting one-liner is a silent no-op, and a silent no-op that looks
    like a fix is worse than the bug.

    Two independent reasons it cannot work, both already paid for here:
    GitHub emits no `workflow_run` cascade for a run dispatched with
    GITHUB_TOKEN (#21696 — measured again 2026-09-21: 28 dispatched PR-branch
    deploys, 0 cascades), and the Sentinel resolves a PR from
    `workflow_run.pull_requests[0]`, which a dispatched run's event does not
    populate. This test exists so the no-op cannot be re-landed as a fix.
    """
    import yaml as _y  # noqa: PLC0415

    data = _y.safe_load((REPO_ROOT / ".github" / "workflows" / "review-sentinel.yml").read_text())
    listed = data[True]["workflow_run"]["workflows"]
    assert "Build and deploy testing" not in listed, (
        "a workflow_run trigger for the staging deploy never fires (dispatched with "
        "GITHUB_TOKEN) and could not resolve a PR if it did — staging-status.yml's "
        "scheduled sweep is what re-scores G4"
    )


def test_g4s_remedy_text_accounts_for_a_deploy_that_already_succeeded():
    """The gate's own message used to describe only two worlds — the deploy
    never ran, or it failed — so an author whose deploy was green and whose
    gate was red was told to retry something that had already worked."""
    sentinel_src = (HERE / "sentinel.py").read_text()
    assert "staging-status.yml" in sentinel_src, \
        "G4's remedy must name what picks a finished deploy up"


def run_standalone() -> int:
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
        except Exception as exc:  # noqa: BLE001 — a crash is a failure, not a harness abort
            failures += 1
            print(f"  FAIL: {t.__name__}: {type(exc).__name__}: {exc}", file=sys.stderr)
    if failures:
        print(f"{failures} staging-sweep test(s) failed", file=sys.stderr)
        return 1
    print("all staging-sweep self-tests passed")
    return 0


if __name__ == "__main__":
    sys.exit(run_standalone())
