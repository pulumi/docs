#!/usr/bin/env python3
"""The two fixes for pulumi/docs#22200's three failed publishes.

That PR documented a feature whose implementing change sits in a private
repo, so 85 claims came back `unverifiable`, each composed as its own ❓ row
and Do-this block, and the 80 KB author card was refused by
pinned-comment.sh's 60,000-byte budget on every retry.

1. The new-feature carve-out: verify-claims.py records which implementing
   refs the review can't read, and compose-review.py asks about the pass1
   unverifiables they explain in one grouped ❓.
2. The card budget: build-evidence.fit_author_card (both lanes) sheds what the
   evidence page also carries until the card fits, and the update lane puts
   it back when there's room again.
"""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[3]


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules.setdefault(name, mod)
    spec.loader.exec_module(mod)
    return mod


cr = _load("compose_review", HERE / "compose-review.py")
be = _load("build_evidence", HERE / "build-evidence.py")
au = _load("apply_update", HERE / "apply-update.py")
vc = _load("verify_claims", HERE / "verify-claims.py")
ve = _load("validate_evidence", REPO_ROOT / "scripts" / "review-v3" / "validate-evidence.py")

UNREADABLE = "pulumi/pulumi-service#49283"
PAGE = "content/docs/esc/providers/login/oidc.md"
BLOG = "content/blog/esc-oidc/index.md"


def _verdict(n: int, *, route="pass1", verdict="unverifiable", file=PAGE, **extra) -> dict:
    v = {
        "claim_id": f"c{n}", "file": file, "line_range": f"L{10 + n}",
        "text": f"The fn::open::oidc provider does thing number {n} for every organization that turns it on",
        "type": "behavior", "route": route, "verdict": verdict, "confidence": "low",
        "evidence": "gh pr diff 49283 -R pulumi/pulumi-service (inaccessible)",
        "source": "gh pr view 49283 -R pulumi/pulumi-service (inaccessible)",
    }
    v.update(extra)
    return v


def _compose(tmp_path: Path, verdicts: list[dict], unreadable: list[str] | None = None,
             links: bool = True) -> tuple[str, str, dict]:
    tmp_path.mkdir(parents=True, exist_ok=True)
    meta = {}
    if unreadable is not None:
        meta = {"impl_refs": list(unreadable), "impl_refs_unreadable": list(unreadable)}
    vcp = tmp_path / "verified-claims.json"
    vcp.write_text(json.dumps({"verdicts": verdicts, "errors": [], "meta": meta}))
    files = sorted({v["file"] for v in verdicts})
    out = tmp_path / "draft"
    cmd = [
        sys.executable, str(HERE / "compose-review.py"), "--surface", "v3",
        "--out", str(out / "unused.md"), "--out-author", str(out / "a.md"),
        "--out-brief", str(out / "b.md"), "--out-evidence", str(out / "e.json"),
        "--timestamp", "2026-10-13T17:02:40Z",
        "--head-sha", "bba3214856759a7ceae83ae88391bac1cca85875",
        "--dry-run", "--repo", "pulumi/docs", "--pr", "22200",
        "--diff-files", ",".join(files),
        "--verified-claims", str(vcp), "--candidate-claims", "/dev/null",
        "--vale-findings", "/dev/null", "--editorial-balance", "/dev/null",
        "--cross-sibling", "/dev/null", "--frontmatter", "/dev/null",
        "--hugo-build", "/dev/null", "--readthrough", "/dev/null",
        "--routed-team", "@pulumi/docs-guild",
    ]
    if links:
        cmd += ["--head-repo", "pulumi/docs", "--head-branch", "dgrove/esc-oidc-v2-docs"]
    out.mkdir(parents=True, exist_ok=True)
    proc = subprocess.run(cmd, capture_output=True, text=True)
    assert proc.returncode == 0, proc.stderr
    return ((out / "a.md").read_text(), (out / "b.md").read_text(),
            json.loads((out / "e.json").read_text()))


def _fill_scaffolds(author: str) -> str:
    """Stand in for the model: fill every Do-this scaffold the way a real
    card does (about 430 bytes a block, measured on #22200's published card)
    and drop the TODOs from the finding cells."""
    out = []
    for line in author.splitlines():
        if line.startswith("- **Line (verbatim):** <TODO"):
            line = ('- **Line (verbatim):** "The fn::open::oidc provider does a thing for every '
                    'organization that turns it on."')
        elif line.startswith("- **Why:** <TODO"):
            line = ("- **Why:** Nothing public confirms this: the Pulumi Cloud change behind it is "
                    "private, and third-party behavior here comes from your test runs rather than "
                    "vendor docs. Only you can vouch for it.")
        elif line.startswith("- **Fix:** <TODO"):
            line = ("- **Fix:** Reply with what confirms it (the service PR, a test run, or a vendor "
                    "doc); if your testing showed otherwise, correct the line instead.")
        elif line.startswith("| **F") and "<TODO" in line:
            line = line[:line.index("<TODO")].rstrip() + " |"
        out.append(line)
    return "\n".join(out) + "\n"


def _build(author: str, brief: str, base: dict) -> tuple[dict, str, str]:
    return be.build(_fill_scaffolds(author), brief, base)


def _row_ids(body: str, bucket: str) -> list[str]:
    return [p["id"] for b, _i, p, _r in be._walk(body, be.AUTHOR_SECTIONS, "author") if b == bucket]


def _validate_card(author: str, brief: str, tmp_path: Path) -> subprocess.CompletedProcess:
    a, b = tmp_path / "card-a.md", tmp_path / "card-b.md"
    a.write_text(author)
    b.write_text(brief)
    # The update lane's own call: no evidence base, so "every row keeps its
    # block" isn't asked — exactly the rule a fitted card relaxes.
    return subprocess.run(
        [sys.executable, str(HERE / "validate-pinned.py"), "check",
         "--body-file", str(a), "--brief-file", str(b), "--pr", "22200", "--repo", "pulumi/docs",
         # The stand-in model above fills only the Do-this blocks.
         "--skip-rule", "no-todo-tokens"],
        capture_output=True, text=True)


# ---- verify-claims: which implementing refs can't be read ------------------

def test_impl_ref_repo_reads_every_ref_shape():
    assert vc.impl_ref_repo("pulumi/pulumi-service#49283") == "pulumi/pulumi-service"
    assert vc.impl_ref_repo("github.com/pulumi/pulumi/pull/123") == "pulumi/pulumi"
    assert vc.impl_ref_repo("github.com/pulumi/esc/commit/abc123") == "pulumi/esc"
    assert vc.impl_ref_repo(
        "github.com/pulumi/pulumi-service/blob/abc/pkg/oidc.go#L10-L20") == "pulumi/pulumi-service"
    assert vc.impl_ref_repo("nonsense") == ""


class _FakeGh:
    def __init__(self, by_repo: dict[str, tuple[int, str] | Exception]):
        self.by_repo = by_repo
        self.calls: list[str] = []

    def __call__(self, cmd, **_kw):
        repo = cmd[2].removeprefix("repos/")
        self.calls.append(repo)
        result = self.by_repo[repo]
        if isinstance(result, Exception):
            raise result
        rc, stderr = result
        return subprocess.CompletedProcess(cmd, rc, "", stderr)


def test_only_a_404_marks_a_ref_unreadable():
    gh = _FakeGh({
        "pulumi/pulumi-service": (1, "gh: Not Found (HTTP 404)"),
        "pulumi/pulumi": (0, ""),
        "pulumi/esc": (1, "gh: Server Error (HTTP 502)"),
        "pulumi/docs": subprocess.TimeoutExpired("gh", 30),
    })
    refs = ["pulumi/pulumi-service#49283", "github.com/pulumi/pulumi-service/pull/49300",
            "pulumi/pulumi#1", "pulumi/esc#2", "pulumi/docs#3"]
    assert vc.probe_unreadable_refs(refs, run=gh) == [
        "pulumi/pulumi-service#49283", "github.com/pulumi/pulumi-service/pull/49300"]
    assert gh.calls.count("pulumi/pulumi-service") == 1, "one probe per repo"


def test_a_404_on_stdout_counts_too():
    gh = _FakeGh({"pulumi/pulumi-service": (1, "")})
    gh_out = lambda cmd, **kw: subprocess.CompletedProcess(cmd, 1, "HTTP 404: Not Found", "")
    assert vc.probe_unreadable_refs([UNREADABLE], run=gh_out) == [UNREADABLE]
    assert vc.probe_unreadable_refs([UNREADABLE], run=gh) == [], "no 404 anywhere → unknown"


# ---- verify-claims: don't spend Opus turns on what can't be read -----------

import pytest  # noqa: E402


@pytest.fixture
def unreadable_service():
    vc.set_unreadable_repos([UNREADABLE])
    yield
    vc.set_unreadable_repos([])


@pytest.mark.parametrize("args", [
    ["pr", "diff", "49283", "-R", "pulumi/pulumi-service"],
    ["pr", "view", "49283", "--repo=pulumi/pulumi-service"],
    ["api", "repos/pulumi/pulumi-service/pulls/49283/files"],
    ["api", "repos/Pulumi/Pulumi-Service"],
    ["search", "code", "repo:pulumi/pulumi-service", "openOIDC"],
    ["pr", "view", "https://github.com/pulumi/pulumi-service/pull/49283"],
])
def test_gh_query_refuses_an_unreadable_repo_without_running_gh(unreadable_service, monkeypatch, args):
    def boom(*_a, **_kw):
        raise AssertionError("gh must not run against a repo the probe found unreadable")
    monkeypatch.setattr(vc.subprocess, "run", boom)
    out = vc.exec_gh_query({"args": args})
    assert out.startswith("error: pulumi/pulumi-service is not readable"), out
    assert "Don't query that repository again" in out


@pytest.mark.parametrize("args", [
    ["api", "repos/pulumi/pulumi/contents/sdk/go/common/resource/stack.go"],
    ["api", "repos/pulumi/docs/contents/content/docs/esc/providers/login/oidc.md"],
    ["search", "code", "repo:pulumi/pulumi-service-extras", "x"],
])
def test_gh_query_still_runs_everything_else(unreadable_service, monkeypatch, args):
    ran = []
    monkeypatch.setattr(vc.subprocess, "run", lambda cmd, **_kw: (
        ran.append(cmd), subprocess.CompletedProcess(cmd, 0, "ok", ""))[1])
    assert vc.exec_gh_query({"args": args}) == "ok"
    assert ran == [["gh", *args]]


def test_no_guard_until_a_probe_finds_something(monkeypatch):
    vc.set_unreadable_repos([])
    monkeypatch.setattr(vc.subprocess, "run",
                        lambda cmd, **_kw: subprocess.CompletedProcess(cmd, 0, "ok", ""))
    assert vc.exec_gh_query({"args": ["pr", "diff", "1", "-R", "pulumi/pulumi-service"]}) == "ok"


def test_the_prompt_names_the_unreadable_ref_instead_of_asking_for_it(unreadable_service):
    claim = {"file": PAGE, "line_range": "L10", "type": "behavior", "text": "x does y"}
    refs = [UNREADABLE, "pulumi/esc#12"]
    msg = vc.build_user_message(claim, "pass1", None, impl_refs=refs)
    read_list = msg.split("This docs PR cites product source")[1].split("This docs PR also cites")[0]
    assert "- pulumi/esc#12" in read_list and UNREADABLE not in read_list
    assert f"This docs PR also cites {UNREADABLE}, which this review can't read" in msg
    assert "return `unverifiable` now" in msg
    # Only the unreadable ref cited: no read list at all, just the note.
    only = vc.build_user_message(claim, "pass1", None, impl_refs=[UNREADABLE])
    assert "cites product source" not in only and "which this review can't read" in only
    # pass2 reads a pre-fetched page and never gets either block.
    assert "can't read" not in vc.build_user_message(claim, "pass2", None, impl_refs=refs)


# ---- compose: the new-feature group ----------------------------------------

def _carve_out_verdicts() -> list[dict]:
    vs = [_verdict(n) for n in range(1, 7)]                                    # grouped
    vs.append(_verdict(7, file=BLOG))                                           # grouped, 2nd file
    vs.append(_verdict(8, route="pass3", source='WebSearch ran query "aembit oidc"'))  # own row
    vs.append(_verdict(9, turn_cap_exhausted=True))                             # own row
    vs.append(_verdict(10, source_discipline_gate="self-reference"))           # own row
    vs.append(_verdict(11, verdict="contradicted", confidence="high"))          # 🚨
    vs.append(_verdict(12, route="pass2"))                                      # own row
    return vs


def test_pass1_unverifiables_become_one_group_question(tmp_path):
    author, brief, base = _compose(tmp_path, _carve_out_verdicts(), [UNREADABLE])
    groups = [f for f in base["findings"] if f.get("members")]
    assert len(groups) == 1
    group = groups[0]
    assert group["bucket"] == "author-answer" and group["origin"] == "verdict:unverifiable"
    assert group["file"] == cr.GROUP_FILE
    assert [m["lines"][0] for m in group["members"]] == [11, 12, 13, 14, 15, 16, 17]
    assert {m["file"] for m in group["members"]} == {PAGE, BLOG}
    assert UNREADABLE in group["text"] and group["text"].startswith("7 claims")
    # Its row has no Where (the members span files) and its block is composed
    # in full: one Fix, no TODO, every member named.
    gid = group["id"]
    assert f"| **{gid}** | — | 7 claims" in author
    spans, texts = be.collect_detail_blocks(author)
    block = texts[gid]
    assert "<TODO" not in block
    assert sum(1 for ln in block.splitlines() if ln.startswith("- **Fix:**")) == 1
    assert f"`/update-review {gid}: <what you checked them against>`" in block
    assert f"<summary>The 7{cr.GROUP_LIST_SUMMARY_SUFFIX}" in block
    assert f"**`{BLOG}`**" in block and "- L17 — " in block
    # The group leads ❓; the other unverifiables keep their own rows.
    q_ids = _row_ids(author, "author-answer")
    assert q_ids[0] == gid and len(q_ids) == 5, q_ids  # group + pass3, turn-cap, source-gate, pass2
    assert len(_row_ids(author, "outstanding")) == 1
    assert ve.validate_evidence(base) == [], ve.validate_evidence(base)


def test_no_group_without_an_unreadable_implementing_change(tmp_path):
    _a, _b, base = _compose(tmp_path, _carve_out_verdicts(), None)
    assert not any(f.get("members") for f in base["findings"])
    _a, _b, base = _compose(tmp_path / "readable", _carve_out_verdicts(), [])
    assert not any(f.get("members") for f in base["findings"])


def test_two_claims_are_not_a_group(tmp_path):
    vs = [_verdict(1), _verdict(2), _verdict(3, route="pass3")]
    author, _b, base = _compose(tmp_path, vs, [UNREADABLE])
    assert not any(f.get("members") for f in base["findings"])
    assert len(_row_ids(author, "author-answer")) == 3


def test_group_survives_build_evidence_and_counts_every_member(tmp_path):
    author, brief, base = _compose(tmp_path, _carve_out_verdicts(), [UNREADABLE])
    ev, a_out, b_out = _build(author, brief, base)
    group = next(f for f in ev["findings"] if f.get("members"))
    assert len(group["members"]) == 7 and group.get("detail"), group
    # 7 grouped + 4 lone ❓ + 1 🚨 open: the group counts as its members, not
    # as one with six more "settled".
    assert "12 open on the author's card" in b_out, [ln for ln in b_out.splitlines() if "Facts" in ln]
    assert "settled" not in next(ln for ln in b_out.splitlines() if ln.startswith("- **Facts:**"))
    assert ve.validate_evidence(ev) == [], ve.validate_evidence(ev)
    proc = _validate_card(a_out, b_out, tmp_path)
    assert proc.returncode == 0, proc.stdout + proc.stderr


# ---- the card budget -------------------------------------------------------

def test_a_card_under_budget_is_untouched(tmp_path):
    author, brief, base = _compose(tmp_path, _carve_out_verdicts(), [UNREADABLE])
    _ev, a_out, _b = _build(author, brief, base)
    assert be.fit_author_card(a_out) == (a_out, [])


def _big(tmp_path: Path, n: int = 90, unreadable=None) -> tuple[str, str, dict]:
    """A #22200-shaped card: n ❓ unverifiables (pass2, so never grouped),
    each with Files-view and ✏️ links, plus two 🚨 contradictions."""
    vs = [_verdict(i, route="pass2", file=PAGE if i % 2 else BLOG) for i in range(1, n + 1)]
    vs += [_verdict(n + 1, verdict="contradicted", confidence="high"),
           _verdict(n + 2, verdict="contradicted", confidence="high", file=BLOG)]
    return _compose(tmp_path, vs, unreadable)


def test_the_22200_shape_now_publishes(tmp_path):
    author, brief, base = _big(tmp_path)
    filled = _fill_scaffolds(author)
    assert be.card_bytes(filled) > be.CARD_MAX_BYTES, "the fixture must reproduce the failure"
    ev, a_out, b_out = be.build(filled, brief, base)
    assert be.card_bytes(a_out) <= be.CARD_BUDGET
    # Every row stays; only ❓'s links and blocks went, in that order.
    assert len(_row_ids(a_out, "author-answer")) == 90
    assert len(_row_ids(a_out, "outstanding")) == 2
    spans, _texts = be.collect_detail_blocks(a_out)
    assert set(spans) == set(_row_ids(a_out, "outstanding")), "🚨 blocks kept, ❓ blocks shed"
    assert be.fit_note("questions") in a_out
    assert "/pull/22200/files#diff-" in a_out.split("### ❓")[0], "🚨 rows keep their links"
    assert "/pull/22200/files#diff-" not in a_out.split("### ❓")[1].split("**Full evidence:**")[0]
    # The evidence still has every block the card dropped.
    blocking = [f for f in ev["findings"] if f["bucket"] in ("outstanding", "author-answer")]
    assert all(f.get("detail") for f in blocking)
    proc = _validate_card(a_out, b_out, tmp_path)
    assert proc.returncode == 0, proc.stdout + proc.stderr
    # pinned-comment.sh's own check, after the publish-time URL substitution.
    published = a_out.replace(
        cr.EVIDENCE_URL_TOKEN, "https://review-evidence-d1a6b84.s3.us-west-2.amazonaws.com/22200/latest.html")
    assert be.card_bytes(published) <= be.CARD_MAX_BYTES


def test_the_ladder_stops_at_the_first_step_that_fits(tmp_path):
    author, brief, base = _big(tmp_path)
    _ev, full, _b = be.build(_fill_scaffolds(author), brief, dict(base))
    # Re-run the fit on the unfitted card with a budget only link-stripping needs.
    unfitted = _fill_scaffolds(author)
    unlinked = be._unlink_rows(unfitted, "author-answer")
    out, steps = be.fit_author_card(unfitted, budget=be.card_bytes(unlinked))
    assert steps == ["question-links"] and out == unlinked
    assert be.fit_note("questions") not in out


def test_a_group_block_outlasts_the_question_blocks(tmp_path):
    vs = [_verdict(i) for i in range(1, 40)] + [_verdict(i, route="pass2") for i in range(40, 80)]
    author, brief, base = _compose(tmp_path, vs, [UNREADABLE])
    filled = _fill_scaffolds(author)
    gid = next(f["id"] for f in base["findings"] if f.get("members"))
    # Budget that needs the ❓ blocks gone but not the claim list.
    no_q = be._drop_blocks(be._unlink_rows(be._unlink_rows(filled, "author-answer"), "resolved"),
                           "author-answer", "questions")
    out, steps = be.fit_author_card(filled, budget=be.card_bytes(no_q))
    _spans, texts = be.collect_detail_blocks(out)
    assert steps == ["question-links", "question-details"]
    assert set(texts) == {gid} | set(_row_ids(out, "outstanding")), "only the group's ❓ block stays"
    assert cr.GROUP_LIST_SUMMARY_SUFFIX in texts[gid]
    # The group's </details> keeps the blank line that ends its HTML block, or
    # the line after it (the browser hint) would render as raw text.
    kept = out.splitlines()
    assert kept[kept.index("</details>") + 1] == ""
    # Squeeze harder and the claim list becomes a pointer, keeping Why/Fix.
    out2, steps2 = be.fit_author_card(filled, budget=1)
    # No 🚨 rows here, so the blocker steps find nothing to shed and aren't listed.
    assert steps2 == ["question-links", "question-details", "group-claims"], steps2
    _spans, texts2 = be.collect_detail_blocks(out2)
    assert set(texts2) == {gid}
    assert be.group_pointer(39) in texts2[gid] and "- **Fix:**" in texts2[gid]
    assert cr.GROUP_LIST_SUMMARY_SUFFIX not in out2


def test_the_brief_sheds_its_check_links(tmp_path):
    brief = "\n".join([
        "### ⚠️ Check these before approving", "",
        cr.FINDING_TABLE_HEADER, cr.FINDING_TABLE_SEPARATOR,
        cr.render_finding_row("F1", ref="L3", file=PAGE, body="maybe wrong",
                              link_base="https://github.com/pulumi/docs/pull/1/files"),
        "", "### ✅ What you can rubber-stamp", "",
    ]) + "\n"
    out, steps = be.fit_brief_card(brief, budget=1)
    assert steps == ["check-links"]
    assert f"| **F1** | `{PAGE}` L3 | maybe wrong |" in out


# ---- the update lane: shed again, and restore when there's room ------------

def _update(actions) -> dict:
    return {"schema": 1, "case": "mixed", "history_summary": "test", "findings": actions}


def test_update_lane_keeps_a_fitted_card_under_budget(tmp_path):
    author, brief, base = _big(tmp_path)
    ev, a_card, b_card = be.build(_fill_scaffolds(author), brief, base)
    assert be.was_fitted(a_card)
    q_ids = _row_ids(a_card, "author-answer")
    a_out, b_out, state, _report = au.apply(
        a_card, b_card, _update([{"id": q_ids[0], "action": "resolve", "annotation": "fixed in abc1234"}]),
        head_sha="c" * 40, actor="author", auto=False, repo="pulumi/docs", pr=22200,
        head_repo="pulumi/docs", head_branch="dgrove/esc-oidc-v2-docs", prior=ev)
    # apply() re-renders every row with its links and restores every block…
    assert be.card_bytes(a_out) > be.CARD_BUDGET
    # …and main()'s fit sheds again, the way it does before publishing.
    fitted = be.fit_and_report("author", a_out, be.fit_author_card)
    assert be.card_bytes(fitted) <= be.CARD_BUDGET
    assert len(_row_ids(fitted, "author-answer")) == 89
    proc = _validate_card(fitted, b_out, tmp_path)
    assert proc.returncode == 0, proc.stdout + proc.stderr


def test_update_lane_restores_blocks_once_the_card_shrinks(tmp_path):
    author, brief, base = _big(tmp_path)
    ev, a_card, b_card = be.build(_fill_scaffolds(author), brief, base)
    q_ids = _row_ids(a_card, "author-answer")
    keep = q_ids[:5]
    actions = [{"id": fid, "action": "resolve", "annotation": "fixed in abc1234"}
               for fid in q_ids if fid not in keep]
    a_out, b_out, _state, _r = au.apply(
        a_card, b_card, _update(actions), head_sha="d" * 40, actor="author", auto=False,
        repo="pulumi/docs", pr=22200, head_repo="pulumi/docs",
        head_branch="dgrove/esc-oidc-v2-docs", prior=ev)
    fitted = be.fit_and_report("author", a_out, be.fit_author_card)
    spans, texts = be.collect_detail_blocks(fitted)
    assert set(keep) <= set(spans), "the remaining questions got their blocks back"
    for fid in keep:
        assert texts[fid] == next(f for f in ev["findings"] if f["id"] == fid)["detail"]
    assert not be.was_fitted(fitted)
    proc = _validate_card(fitted, b_out, tmp_path)
    assert proc.returncode == 0, proc.stdout + proc.stderr


def test_update_lane_rebuilds_a_collapsed_claim_list(tmp_path):
    vs = [_verdict(i) for i in range(1, 6)]
    author, brief, base = _compose(tmp_path, vs, [UNREADABLE])
    ev, a_card, b_card = be.build(_fill_scaffolds(author), brief, base)
    gid = next(f["id"] for f in ev["findings"] if f.get("members"))
    collapsed = be._collapse_group_lists(a_card)
    assert be.group_pointer(5) in collapsed and be.was_fitted(collapsed)
    a_out, _b, _s, _r = au.apply(
        collapsed, b_card, _update([]), head_sha="e" * 40, actor="author", auto=False,
        repo="pulumi/docs", pr=22200, prior=ev)
    _spans, texts = be.collect_detail_blocks(a_out)
    assert f"<summary>The 5{cr.GROUP_LIST_SUMMARY_SUFFIX}" in texts[gid]
    # …and the evidence the update lane assembles keeps the members.
    ev2 = au.assemble_evidence(ev, a_out, _b, _s, _update([]), repo="pulumi/docs", pr=22200,
                               head_sha="e" * 40, run_id="t", timestamp="2026-10-14T00:00:00Z")
    assert len(next(f for f in ev2["findings"] if f["id"] == gid)["members"]) == 5


def test_an_unfitted_card_is_left_alone_by_the_update_lane(tmp_path):
    author, brief, base = _compose(tmp_path, _carve_out_verdicts(), [UNREADABLE])
    ev, a_card, b_card = be.build(_fill_scaffolds(author), brief, base)
    assert not be.was_fitted(a_card)
    assert be.restore_shed_blocks({}, ["F1"], {}) == {}


def test_the_budget_matches_pinned_comment():
    sh = (HERE / "pinned-comment.sh").read_text()
    assert f"DEFAULT_MAX_BYTES={be.CARD_MAX_BYTES}\n" in sh, \
        "build-evidence.CARD_MAX_BYTES and pinned-comment.sh DEFAULT_MAX_BYTES must agree"


# ---- the group block is composer-owned -------------------------------------

nv = _load("normalize_v3_draft", HERE / "normalize-v3-draft.py")


def _group_draft(tmp_path):
    author, brief, base = _compose(tmp_path, [_verdict(i) for i in range(1, 6)], [UNREADABLE])
    gid = next(f["id"] for f in base["findings"] if f.get("members"))
    return author, brief, base, gid


def test_the_base_carries_the_composed_group_block(tmp_path):
    author, _brief, base, gid = _group_draft(tmp_path)
    _spans, texts = be.collect_detail_blocks(author)
    assert next(f for f in base["findings"] if f["id"] == gid)["detail"] == texts[gid]


def test_normalize_reverts_a_model_edit_to_the_group_block(tmp_path):
    author, brief, base, gid = _group_draft(tmp_path)
    composed = be.collect_detail_blocks(author)[1][gid]
    # The two edits that would fail validation: a second **Fix:**, and the
    # claim list gone.
    mangled = author.replace(
        f"<summary>The 5{cr.GROUP_LIST_SUMMARY_SUFFIX}",
        "<summary>stuff</summary>").replace(
        "- **Fix:** Check them", "- **Fix:** Reply once.\n- **Fix:** Check them", 1)
    rep = nv.Repairs()
    fixed, _b = nv.normalize(mangled, brief, base, rep)
    assert be.collect_detail_blocks(fixed)[1][gid] == composed
    assert [r["rule"] for r in rep.items] == ["group-block"]
    # Untouched, it's left alone.
    rep2 = nv.Repairs()
    same, _b = nv.normalize(author, brief, base, rep2)
    assert same == author and not rep2.items


def test_normalize_regenerates_a_deleted_group_block_as_composed(tmp_path):
    author, brief, base, gid = _group_draft(tmp_path)
    spans, texts = be.collect_detail_blocks(author)
    s, e = spans[gid]
    lines = author.splitlines()
    deleted = "\n".join(lines[:s] + lines[e:]) + "\n"
    assert f"#### {gid} · Do this" not in deleted
    fixed, _b = nv.normalize(deleted, brief, base, nv.Repairs())
    assert be.collect_detail_blocks(fixed)[1][gid] == texts[gid]


def test_a_retext_keeps_the_group_claim_list(tmp_path):
    author, brief, base, gid = _group_draft(tmp_path)
    ev, a_card, b_card = be.build(_fill_scaffolds(author), brief, base)
    a_out, _b, _s, _r = au.apply(
        a_card, b_card,
        _update([{"id": gid, "action": "retext", "text": "5 claims, still unchecked — verdict: unverifiable",
                  "detail": {"why": "Still private.", "fix": "Answer once."}}]),
        head_sha="f" * 40, actor="author", auto=False, repo="pulumi/docs", pr=22200, prior=ev)
    block = be.collect_detail_blocks(a_out)[1][gid]
    assert "- **Why:** Still private." in block and "- **Fix:** Answer once." in block
    assert f"<summary>The 5{cr.GROUP_LIST_SUMMARY_SUFFIX}" in block and block.endswith("</details>")
    # …and the pointer a fit leaves survives a retext the same way.
    collapsed = be._collapse_group_lists(a_card)
    start, end = be.collect_detail_blocks(collapsed)[0][gid]
    assert au._group_list_tail(collapsed.splitlines()[start:end]) == [be.group_pointer(5)]
