#!/usr/bin/env python3
"""Tests for sla-sweep.py — author-staleness warn/close, reviewer-SLA
escalation, business-day math, and the degradation/dry-run contracts.

Runs under pytest (make test-review-pipeline) and standalone via
`sla-sweep.py --self-test` (run_standalone below, same convention as
test_sentinel.py). No pytest fixtures are used (no `tmp_path`) so every test
also runs unmodified outside pytest — each test opens its own
`tempfile.TemporaryDirectory()`, matching record-evidence.py's self-test
style.
"""

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


sla_sweep = _load("sla_sweep_under_test", HERE / "sla-sweep.py")
import review_state  # noqa: E402
import routing  # noqa: E402
import sentinel  # noqa: E402

HEAD = "a" * 40
NOW = datetime(2026, 8, 31, 12, 0, tzinfo=timezone.utc)  # a Monday

RAW_CONFIG = {
    "schema": 1,
    "teams": {
        "docs-guild": "pulumi/docs-guild",
        "marketing": "pulumi/docs-marketing-review",
        "tools": "pulumi/docs-tools",
    },
    "bots": ["pulumi-bot"],
    "matrix": {
        "docs": {"mechanical": "none", "substantive": "docs-guild"},
        "blog": {"mechanical": "none", "substantive": "marketing"},
        "website": {"mechanical": "none", "substantive": "marketing"},
        "programs": {"mechanical": "none", "substantive": "docs-guild"},
        "infra": {"mechanical": "tools", "substantive": "tools", "staging_evidence": "required"},
        "other": {"mechanical": "none", "substantive": "docs-guild"},
    },
    "claims_overlay": {"add": "marketing"},
    "external_contributors": {"skip_gates": ["review-ran", "findings-answered"]},
    "sla": {
        "tools": {"business_days": 1, "escalate_to": "TODO-tools-lead"},
        "docs-guild": {"business_days": 3, "escalate_to": "guild-lead"},
        "marketing": {"business_days": 3, "escalate_to": "TODO-named-fallback"},
    },
    "author_staleness": {"warn_days": 14, "close_days": 21},
    "waive": {"label": "review:waived", "log_prefix": "pr-review/waives/"},
}
CONFIG, _errors, _warnings = routing.validate_raw(RAW_CONFIG)
assert CONFIG is not None, _errors


# ---- Stub Gh --------------------------------------------------------------


class StubGh:
    def __init__(self, repo: str = "pulumi/docs"):
        self.repo = repo
        self.open_prs: list[dict] = []
        self._pr_detail: dict[int, dict] = {}
        self._comments: dict[int, list[dict]] = {}
        self._files: dict[int, list[dict]] = {}
        self._reviews: dict[int, list[dict]] = {}
        self._timeline: dict[int, list[dict]] = {}
        self.timeline_errors: set[int] = set()
        self.comments_posted: list[tuple[int, str]] = []
        self.labels_added: list[tuple[int, str]] = []
        self.labels_removed: list[tuple[int, str]] = []
        self.closed: list[tuple[int, str]] = []

    def add_pr(self, number, *, draft=False, author="alice", created_at="2026-08-01T12:00:00Z",
               comments=(), files=(), reviews=(), timeline=(), head_sha=HEAD):
        self.open_prs.append({
            "number": number, "isDraft": draft, "headRefOid": head_sha,
            "createdAt": created_at, "author": {"login": author}, "title": "t",
        })
        self._pr_detail[number] = {
            "head": {"sha": head_sha}, "draft": draft, "user": {"login": author},
            "created_at": created_at, "number": number, "title": "t", "body": "",
        }
        self._comments[number] = list(comments)
        self._files[number] = list(files)
        self._reviews[number] = list(reviews)
        self._timeline[number] = list(timeline)

    def set_timeline(self, number, timeline):
        self._timeline[number] = timeline

    def list_open_prs(self):
        return self.open_prs

    def list_issue_comments(self, pr):
        return self._comments[pr]

    def get_pr(self, pr):
        return self._pr_detail[pr]

    def list_files(self, pr):
        return self._files[pr]

    def list_reviews(self, pr):
        return self._reviews[pr]

    def get_timeline(self, pr):
        if pr in self.timeline_errors:
            raise RuntimeError("gh api timeline failed")
        return self._timeline[pr]

    def create_issue_comment(self, pr, body):
        self.comments_posted.append((pr, body))

    def add_label(self, pr, label):
        self.labels_added.append((pr, label))

    def remove_label(self, pr, label):
        self.labels_removed.append((pr, label))

    def close_pr(self, pr, body):
        self.closed.append((pr, body))


# ---- Fixture builders (mirrors test_sentinel.py's grammar) ----------------


def docs_file_substantive():
    return {
        "filename": "content/docs/iac/x.md",
        "status": "modified",
        "patch": "@@ -40,2 +40,3 @@\n context\n+Pulumi was founded in 2017 and 90% of teams agree.\n context",
    }


def docs_file_mechanical():
    """A one-word typo fix: inside the tightened mechanical bar, so a PR of
    just this file resolves to no required role (kind None)."""
    return {
        "filename": "content/docs/iac/x.md",
        "status": "modified",
        "patch": "@@ -40,3 +40,3 @@\n context\n-Run teh command.\n+Run the command.\n context",
    }


def infra_file():
    return {
        "filename": "layouts/partials/foo.html",
        "status": "modified",
        "patch": "@@ -1,1 +1,1 @@\n-<b>a</b>\n+<b>b</b>",
    }


def author_card(findings=(), state=None, head=HEAD):
    """findings: list of (fid, section) where section is 'must' or 'answer'."""
    must = [f for f, s in findings if s == "must"]
    answer = [f for f, s in findings if s == "answer"]
    lines = [
        "<!-- CLAUDE_REVIEW 1/1 -->",
        sentinel.AUTHOR_MARKER,
        f"<!-- CLAUDE_REVIEW_HEAD {head} -->",
        "## Review: author action needed — %d items block merge — Last updated x" % (len(must) + len(answer)),
        "",
        "### 🚨 Fix or disagree",
        "",
    ]
    if must:
        lines += ["| | ID | Where | Finding |", "|---|---|---|---|"]
    for fid in must:
        lines.append(f"| **{fid}** | `content/docs/iac/x.md` L10 | a problem |")
    lines += ["", "### ❓ Questions for you", ""]
    if answer:
        lines += ["| | ID | Where | Finding |", "|---|---|---|---|"]
    for fid in answer:
        lines.append(f"| **{fid}** | `content/docs/iac/x.md` L20 | a question |")
    lines += ["", "### ✅ Resolved since last review", "", "_none_", ""]
    body = "\n".join(lines)
    if state is None:
        state = review_state.empty_state()
        state["high_water"] = len(findings)
    body += "\n" + review_state.serialize_block(state) + "\n"
    body += "\n<!-- CLAUDE_REVIEW_FOOTER -->\nfooter text\n"
    return {"id": 111, "body": body, "user": {"login": "github-actions[bot]"}}


def clean_author_card():
    return author_card([], state=review_state.empty_state())


def review(user, state, submitted_at="2026-08-01T00:00:00Z"):
    return {"user": {"login": user, "type": "User"}, "state": state, "submitted_at": submitted_at}


def committed(date):
    return {"event": "committed", "author": {"date": date}}


def commented(login, date):
    return {"event": "commented", "actor": {"login": login}, "created_at": date}


def ready_for_review(date):
    return {"event": "ready_for_review", "created_at": date}


def review_requested(slug, date):
    return {"event": "review_requested", "requested_team": {"slug": slug}, "created_at": date}


def iso(dt: datetime) -> str:
    return dt.isoformat().replace("+00:00", "Z")


# ---- Tests ------------------------------------------------------------------


def test_author_stalled_warn_fires_once():
    with tempfile.TemporaryDirectory() as d:
        state_dir = Path(d)
        gh = StubGh()
        idle_start = NOW - timedelta(days=16)  # > warn_days(14), < close_days(21)
        gh.add_pr(1, comments=[author_card([("F1", "must")])], files=[docs_file_substantive()],
                  timeline=[committed(iso(idle_start))])

        record1 = sla_sweep.sweep(gh, CONFIG, now=NOW, dry_run=False, state_dir=state_dir, evidence_uri="")
        assert len(gh.comments_posted) == 1
        pr, body = gh.comments_posted[0]
        assert pr == 1 and "waiting on you: 1 finding(s)" in body and "closes in 7 days" in body
        assert gh.labels_added == [(1, sla_sweep.AUTHOR_STALLED_LABEL)]
        state = json.loads((state_dir / "state" / "1.json").read_text())
        assert len(state["warns"]) == 1
        assert record1["actions"][0]["action"]["type"] == "warn"

        # second sweep, same state on disk, no new activity -> no-op
        sla_sweep.sweep(gh, CONFIG, now=NOW, dry_run=False, state_dir=state_dir, evidence_uri="")
        assert len(gh.comments_posted) == 1  # unchanged
        assert len(gh.labels_added) == 1


def test_close_only_after_warn_aged_enough():
    with tempfile.TemporaryDirectory() as d:
        state_dir = Path(d)
        gh = StubGh()
        idle_start = NOW - timedelta(days=25)  # > close_days(21)
        gh.add_pr(1, comments=[author_card([("F1", "must")])], files=[docs_file_substantive()],
                  timeline=[committed(iso(idle_start))])
        # warn recorded only 3 days ago -- gap needed is (21-14)=7 days
        recent_warn_state = sla_sweep.empty_sweep_state()
        recent_warn_state["warns"] = [{"at": iso(NOW - timedelta(days=3)), "head_sha": HEAD}]
        sla_sweep.save_state(1, recent_warn_state, "", state_dir)

        sla_sweep.sweep(gh, CONFIG, now=NOW, dry_run=False, state_dir=state_dir, evidence_uri="")
        assert gh.closed == []  # warn not aged enough yet

        # age the warn past the gap and re-run
        aged_warn_state = sla_sweep.empty_sweep_state()
        aged_warn_state["warns"] = [{"at": iso(NOW - timedelta(days=8)), "head_sha": HEAD}]
        sla_sweep.save_state(1, aged_warn_state, "", state_dir)

        sla_sweep.sweep(gh, CONFIG, now=NOW, dry_run=False, state_dir=state_dir, evidence_uri="")
        assert len(gh.closed) == 1 and gh.closed[0][0] == 1
        assert "Closing this PR as stale" in gh.closed[0][1]


def test_activity_clears_warn_and_label():
    with tempfile.TemporaryDirectory() as d:
        state_dir = Path(d)
        gh = StubGh()
        recent_activity = NOW - timedelta(days=1)  # fresh -- well under warn_days
        gh.add_pr(1, comments=[author_card([("F1", "must")])], files=[docs_file_substantive()],
                  timeline=[committed(iso(recent_activity))])
        seeded = sla_sweep.empty_sweep_state()
        seeded["warns"] = [{"at": iso(NOW - timedelta(days=10)), "head_sha": HEAD}]
        sla_sweep.save_state(1, seeded, "", state_dir)

        record = sla_sweep.sweep(gh, CONFIG, now=NOW, dry_run=False, state_dir=state_dir, evidence_uri="")
        assert gh.labels_removed == [(1, sla_sweep.AUTHOR_STALLED_LABEL)]
        assert record["actions"][0]["action"]["type"] == "clear"
        state = json.loads((state_dir / "state" / "1.json").read_text())
        assert state["warns"] == []


def test_reviewer_sla_escalates_once_per_clock_epoch():
    with tempfile.TemporaryDirectory() as d:
        state_dir = Path(d)
        gh = StubGh()
        created = NOW - timedelta(days=10)  # well past docs-guild's 3 business days
        gh.add_pr(1, comments=[clean_author_card()], files=[docs_file_substantive()],
                  created_at=iso(created), timeline=[])

        sla_sweep.sweep(gh, CONFIG, now=NOW, dry_run=False, state_dir=state_dir, evidence_uri="")
        assert len(gh.comments_posted) == 1
        assert "guild-lead" in gh.comments_posted[0][1]
        assert "docs-guild" in gh.comments_posted[0][1]
        state = json.loads((state_dir / "state" / "1.json").read_text())
        assert len(state["escalations"]) == 1

        # same clock epoch (no new review_requested/commit) -> no second escalation
        sla_sweep.sweep(gh, CONFIG, now=NOW, dry_run=False, state_dir=state_dir, evidence_uri="")
        assert len(gh.comments_posted) == 1


def test_new_push_review_cycle_rearms():
    with tempfile.TemporaryDirectory() as d:
        state_dir = Path(d)
        gh = StubGh()
        created = NOW - timedelta(days=10)
        gh.add_pr(1, comments=[clean_author_card()], files=[docs_file_substantive()],
                  created_at=iso(created), timeline=[])

        sla_sweep.sweep(gh, CONFIG, now=NOW, dry_run=False, state_dir=state_dir, evidence_uri="")
        assert len(gh.comments_posted) == 1

        # a fresh review-request 6 days ago starts a NEW clock epoch, still
        # past the 3-business-day SLA measured against `now`
        gh.set_timeline(1, [review_requested("docs-guild", iso(NOW - timedelta(days=6)))])
        sla_sweep.sweep(gh, CONFIG, now=NOW, dry_run=False, state_dir=state_dir, evidence_uri="")
        assert len(gh.comments_posted) == 2
        state = json.loads((state_dir / "state" / "1.json").read_text())
        assert len(state["escalations"]) == 2


def test_business_days_fri_to_monday():
    friday = datetime(2026, 8, 28, 17, 0, tzinfo=timezone.utc)
    monday = datetime(2026, 8, 31, 9, 0, tzinfo=timezone.utc)
    next_friday = datetime(2026, 9, 4, 9, 0, tzinfo=timezone.utc)
    assert friday.weekday() == 4 and monday.weekday() == 0
    assert sla_sweep.business_days_between(friday, monday) == 1
    assert sla_sweep.business_days_between(monday, monday) == 0
    assert sla_sweep.business_days_between(monday, next_friday) == 4
    assert sla_sweep.business_days_between(next_friday, monday) == 0  # end before start


def test_legacy_pr_untouched():
    """No v3 author card AND no v2 pinned review -- never touched, fail-safe."""
    with tempfile.TemporaryDirectory() as d:
        state_dir = Path(d)
        gh = StubGh()
        gh.add_pr(1, comments=[], files=[docs_file_substantive()])

        record = sla_sweep.sweep(gh, CONFIG, now=NOW, dry_run=False, state_dir=state_dir, evidence_uri="")
        assert record["actions"] == []
        assert gh.comments_posted == [] and gh.labels_added == [] and gh.closed == []
        assert not (state_dir / "state" / "1.json").exists()


def test_draft_skipped():
    with tempfile.TemporaryDirectory() as d:
        state_dir = Path(d)
        gh = StubGh()
        gh.add_pr(1, draft=True, comments=[author_card([("F1", "must")])])

        record = sla_sweep.sweep(gh, CONFIG, now=NOW, dry_run=False, state_dir=state_dir, evidence_uri="")
        assert record["actions"] == []
        assert gh.comments_posted == []


def test_todo_escalate_to_records_but_doesnt_mention():
    with tempfile.TemporaryDirectory() as d:
        state_dir = Path(d)
        gh = StubGh()
        created = NOW - timedelta(days=5)  # well past tools' 1 business day
        gh.add_pr(1, comments=[clean_author_card()], files=[infra_file()],
                  created_at=iso(created), timeline=[])

        record = sla_sweep.sweep(gh, CONFIG, now=NOW, dry_run=False, state_dir=state_dir, evidence_uri="")
        assert gh.comments_posted == []  # TODO placeholder -> no @-mention posted
        state = json.loads((state_dir / "state" / "1.json").read_text())
        assert len(state["escalations"]) == 1
        assert state["escalations"][0]["role"] == "tools"
        action = record["actions"][0]["actions"][0]
        assert action["type"] == "escalate" and action["mentioned"] is False


def test_unparsable_timeline_skips():
    with tempfile.TemporaryDirectory() as d:
        state_dir = Path(d)
        gh = StubGh()
        gh.add_pr(1, comments=[author_card([("F1", "must")])], files=[docs_file_substantive()])
        gh.timeline_errors.add(1)

        record = sla_sweep.sweep(gh, CONFIG, now=NOW, dry_run=False, state_dir=state_dir, evidence_uri="")
        assert record["actions"] == []
        assert gh.comments_posted == []
        assert not (state_dir / "state" / "1.json").exists()


def test_dry_run_writes_nothing():
    with tempfile.TemporaryDirectory() as d:
        state_dir = Path(d)
        gh = StubGh()
        idle_start = NOW - timedelta(days=16)
        gh.add_pr(1, comments=[author_card([("F1", "must")])], files=[docs_file_substantive()],
                  timeline=[committed(iso(idle_start))])

        record = sla_sweep.sweep(gh, CONFIG, now=NOW, dry_run=True, state_dir=state_dir, evidence_uri="")
        assert record["actions"][0]["action"]["type"] == "warn"  # intended action is visible
        assert gh.comments_posted == [] and gh.labels_added == []
        assert not (state_dir / "state").exists()
        assert not (state_dir / "runs").exists()


def test_degradation_local_state_no_uri():
    with tempfile.TemporaryDirectory() as d:
        state_dir = Path(d)
        gh = StubGh()
        idle_start = NOW - timedelta(days=16)
        gh.add_pr(1, comments=[author_card([("F1", "must")])], files=[docs_file_substantive()],
                  timeline=[committed(iso(idle_start))])

        sla_sweep.sweep(gh, CONFIG, now=NOW, dry_run=False, state_dir=state_dir, evidence_uri="")
        assert (state_dir / "state" / "1.json").is_file()
        run_files = list((state_dir / "runs" / NOW.date().isoformat()).glob("sweep-*.json"))
        assert len(run_files) == 1


# ---- Standalone harness --------------------------------------------------

def test_changes_requested_only_clocks_from_the_review_not_the_old_push():
    """A standing CHANGES_REQUESTED on a branch last pushed 20 days ago is
    author-time, but the idle clock starts at the review, and the nudge
    must not say "0 finding(s)"."""
    with tempfile.TemporaryDirectory() as d:
        state_dir = Path(d)
        gh = StubGh()
        old_push = NOW - timedelta(days=20)
        gh.add_pr(1, comments=[clean_author_card()], files=[docs_file_substantive()],
                  timeline=[committed(iso(old_push))],
                  reviews=[review("bob", "CHANGES_REQUESTED", iso(NOW - timedelta(days=2)))])
        record = sla_sweep.sweep(gh, CONFIG, now=NOW, dry_run=False, state_dir=state_dir, evidence_uri="")
        assert record["actions"][0]["kind"] == "author"
        assert record["actions"][0]["action"]["type"] == "none"  # 2 idle days, not 20
        assert gh.comments_posted == [] and gh.labels_added == []

        # Now let the review itself age past warn_days: the nudge fires and
        # names the reason rather than a zero count.
        later = NOW + timedelta(days=13)
        record = sla_sweep.sweep(gh, CONFIG, now=later, dry_run=False, state_dir=state_dir, evidence_uri="")
        assert record["actions"][0]["action"]["type"] == "warn"
        assert len(gh.comments_posted) == 1
        body = gh.comments_posted[0][1]
        assert "a reviewer has requested changes" in body and "0 finding(s)" not in body


def test_committer_date_beats_author_date():
    """A rebase keeps the author date; the push is what resets the clock."""
    ev = {"event": "committed",
          "author": {"date": iso(NOW - timedelta(days=40))},
          "committer": {"date": iso(NOW - timedelta(days=1))}}
    got = sla_sweep.last_author_activity([ev], "alice", iso(NOW - timedelta(days=60)))
    assert got == sla_sweep._parse_ts(iso(NOW - timedelta(days=1)))


def test_mutation_failure_does_not_abort_the_sweep():
    with tempfile.TemporaryDirectory() as d:
        state_dir = Path(d)
        gh = StubGh()
        idle_start = NOW - timedelta(days=16)
        for n in (1, 2):
            gh.add_pr(n, comments=[author_card([("F1", "must")])], files=[docs_file_substantive()],
                      timeline=[committed(iso(idle_start))])
        calls = []
        real_add = gh.add_label
        def flaky_add(pr, label):
            calls.append(pr)
            if pr == 1:
                raise RuntimeError("label not found")
            return real_add(pr, label)
        gh.add_label = flaky_add
        record = sla_sweep.sweep(gh, CONFIG, now=NOW, dry_run=False, state_dir=state_dir, evidence_uri="")
        by_pr = {a["pr"]: a for a in record["actions"]}
        # A label failure is best-effort: the warn still counts, its record
        # is saved, PR 2 is processed as usual …
        assert by_pr[1]["action"]["type"] == "warn" and by_pr[2]["action"]["type"] == "warn"
        assert (state_dir / "state" / "1.json").exists()
        assert [pr for pr, _ in gh.comments_posted] == [1, 2]
        # … and — the review's second-order case — the nudge is NOT re-posted
        # on the next sweep while add_label keeps failing.
        sla_sweep.sweep(gh, CONFIG, now=NOW + timedelta(hours=2), dry_run=False, state_dir=state_dir, evidence_uri="")
        assert [pr for pr, _ in gh.comments_posted] == [1, 2]
        assert calls.count(1) == 1  # no retry storm either


def test_comment_failure_is_fatal_for_that_pr_only():
    """Comments stay fatal (never retried blind); the sweep continues."""
    with tempfile.TemporaryDirectory() as d:
        state_dir = Path(d)
        gh = StubGh()
        idle_start = NOW - timedelta(days=16)
        for n in (1, 2):
            gh.add_pr(n, comments=[author_card([("F1", "must")])], files=[docs_file_substantive()],
                      timeline=[committed(iso(idle_start))])
        real_comment = gh.create_issue_comment
        def flaky_comment(pr, body):
            if pr == 1:
                raise RuntimeError("502")
            return real_comment(pr, body)
        gh.create_issue_comment = flaky_comment
        record = sla_sweep.sweep(gh, CONFIG, now=NOW, dry_run=False, state_dir=state_dir, evidence_uri="")
        by_pr = {a["pr"]: a for a in record["actions"]}
        assert "error" in by_pr[1] and by_pr[1]["changed"] is False
        assert not (state_dir / "state" / "1.json").exists()
        assert by_pr[2]["action"]["type"] == "warn"


def test_stale_author_warn_cleared_on_no_clock_branch():
    """Warned PR whose findings got answered and which now resolves to
    'mechanical, no required role': the label must not leak."""
    with tempfile.TemporaryDirectory() as d:
        state_dir = Path(d)
        gh = StubGh()
        gh.add_pr(1, comments=[clean_author_card()], files=[docs_file_mechanical()],
                  timeline=[committed(iso(NOW - timedelta(days=1)))])
        warned = sla_sweep.empty_sweep_state()
        warned["warns"] = [{"at": iso(NOW - timedelta(days=3)), "head_sha": HEAD}]
        sla_sweep.save_state(1, warned, "", state_dir)
        record = sla_sweep.sweep(gh, CONFIG, now=NOW, dry_run=False, state_dir=state_dir, evidence_uri="")
        assert gh.labels_removed == [(1, sla_sweep.AUTHOR_STALLED_LABEL)]
        assert json.loads((state_dir / "state" / "1.json").read_text())["warns"] == []
        assert record["actions"][0]["kind"] is None


def test_no_durable_state_forces_dry_run():
    """A CI runner's local state dies with the job; mutating without a
    durable URI re-issues every warn/escalation each sweep. So: no URI and
    no explicit --allow-local-state ⇒ dry-run, loudly."""
    dry, why = sla_sweep.resolve_mutation_mode("", False, False)
    assert dry is True and "DRY-RUN" in why
    assert sla_sweep.resolve_mutation_mode("s3://b/pr-review", False, False) == (False, None)
    assert sla_sweep.resolve_mutation_mode("", False, True) == (False, None)
    assert sla_sweep.resolve_mutation_mode("", True, False) == (True, None)


def test_cli_without_uri_does_not_mutate(monkeypatch, capsys):
    """End to end through main(): stalled PR, no URI, no override → the
    sweep runs but posts nothing, and the record says why."""
    gh = StubGh()
    gh.add_pr(1, comments=[author_card([("F1", "must")])], files=[docs_file_substantive()],
              timeline=[committed(iso(NOW - timedelta(days=16)))])
    monkeypatch.setattr(sla_sweep, "Gh", lambda repo: gh)
    monkeypatch.delenv(sla_sweep.EVIDENCE_URI_ENV, raising=False)
    with tempfile.TemporaryDirectory() as d:
        import yaml  # noqa: PLC0415
        cfg = Path(d) / "review-routing.yml"
        cfg.write_text(yaml.safe_dump(RAW_CONFIG))
        monkeypatch.setattr(sys, "argv", ["sla-sweep.py", "--repo", "pulumi/docs",
                                          "--config", str(cfg), "--state-dir", d])
        assert sla_sweep.main() == 0
    out = json.loads(capsys.readouterr().out)
    assert out["dry_run"] is True and "DRY-RUN" in out["forced_dry_run"]
    assert gh.comments_posted == [] and gh.labels_added == []


def test_failed_state_upload_is_recorded_not_dropped(monkeypatch):
    """Live bucket, upload fails: the run record must say the state did
    not persist (the digest/human signal), not claim the warn stuck."""
    with tempfile.TemporaryDirectory() as d:
        state_dir = Path(d)
        gh = StubGh()
        gh.add_pr(1, comments=[author_card([("F1", "must")])], files=[docs_file_substantive()],
                  timeline=[committed(iso(NOW - timedelta(days=16)))])
        monkeypatch.setattr(sla_sweep._record_evidence, "upload", lambda record, key: False)
        monkeypatch.setattr(sla_sweep, "_s3_read_json", lambda key: None)
        record = sla_sweep.sweep(gh, CONFIG, now=NOW, dry_run=False, state_dir=state_dir,
                                 evidence_uri="s3://bucket/pr-review")
        a = record["actions"][0]
        assert a["action"]["type"] == "warn" and a["state_persisted"] is False


def test_probe_write_gates_real_runs(monkeypatch):
    """A URI that resolves but can't be written forces dry-run before any
    mutation; a URI that round-trips a probe does not."""
    assert sla_sweep.resolve_mutation_mode("s3://b/pr-review", False, False, durable_ok=False)[0] is True
    assert sla_sweep.resolve_mutation_mode("s3://b/pr-review", False, False, durable_ok=True) == (False, None)
    store = {}
    monkeypatch.setattr(sla_sweep._record_evidence, "upload", lambda record, key: store.__setitem__(key, record) or True)
    monkeypatch.setattr(sla_sweep, "_s3_read_json", lambda key: store.get(key))
    assert sla_sweep.durable_state_writable("s3://b/pr-review", NOW) is True
    monkeypatch.setattr(sla_sweep._record_evidence, "upload", lambda record, key: False)
    assert sla_sweep.durable_state_writable("s3://b/pr-review", NOW) is False
    assert sla_sweep.durable_state_writable("", NOW) is False


def run_standalone() -> int:
    """The --self-test harness. Bound at call time (a module-level binding
    only saw the tests defined above it — 12 of 19 at one point). Tests that
    take pytest fixtures are pytest-only and are skipped here by name; the
    merge-gating path (`pytest scripts/review-v3/`) collects everything."""
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
        print(f"{failures} sla-sweep test(s) failed", file=sys.stderr)
        return 1
    print("all sla-sweep self-tests passed")
    return 0


if __name__ == "__main__":
    sys.exit(run_standalone())
