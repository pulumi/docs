#!/usr/bin/env python3
"""Tests for the v3 review surface: compose_v3, the finding-line grammar, and
build-evidence.py — plus the regression pin that `--surface v2` (the default)
still renders byte-identically from the same artifact set.

The checked-in fixtures under testdata/ are generated, not hand-written:
regenerate with the command in regen_cmd() below after an intentional surface
change, and review the diff like any other golden-file update.
"""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
TESTDATA = HERE / "testdata"
ART = TESTDATA / "v3-artifacts"
REPO_ROOT = HERE.parents[3]


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules.setdefault(name, mod)
    spec.loader.exec_module(mod)
    return mod


cr = _load("compose_review", HERE / "compose-review.py")
review_state = _load("review_state", REPO_ROOT / "scripts" / "review-v3" / "review_state.py")


def regen_cmd(surface: str, out_args: list[str]) -> list[str]:
    return [
        sys.executable, str(HERE / "compose-review.py"),
        "--surface", surface, *out_args,
        "--timestamp", "2026-08-31T18:00:00Z",
        "--head-sha", "aaaabbbbccccddddeeeeffff0000111122223333",
        "--head-sha-short", "aaaabbbb",
        "--diff-files", "content/docs/iac/x.md",
        "--dry-run", "--repo", "pulumi/docs", "--pr", "999",
        "--verified-claims", str(ART / "verified-claims.json"),
        "--candidate-claims", "/dev/null",
        "--vale-findings", str(ART / "vale-findings.json"),
        "--editorial-balance", str(ART / "editorial-balance.json"),
        "--cross-sibling", str(ART / "cross-sibling-discovery.json"),
        "--frontmatter", str(ART / "frontmatter-validation.json"),
        "--hugo-build", str(ART / "hugo-build.json"),
        "--readthrough", "/dev/null",
        "--head-repo", "example/docs-fork", "--head-branch", "fix/component-doc",
        "--routed-team", "@pulumi/docs-guild",
    ]


@pytest.fixture(scope="module")
def v3_outputs(tmp_path_factory):
    tmp = tmp_path_factory.mktemp("v3")
    author, brief, evidence = tmp / "a.md", tmp / "b.md", tmp / "e.json"
    cmd = regen_cmd("v3", [
        "--out", str(tmp / "unused.md"),
        "--out-author", str(author), "--out-brief", str(brief), "--out-evidence", str(evidence),
    ])
    proc = subprocess.run(cmd, capture_output=True, text=True)
    assert proc.returncode == 0, proc.stderr
    return author.read_text(), brief.read_text(), json.loads(evidence.read_text())


def test_v2_golden_unchanged(tmp_path):
    out = tmp_path / "v2.md"
    cmd = regen_cmd("v2", ["--out", str(out)]) + ["--no-validate"]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    assert proc.returncode == 0, proc.stderr
    assert out.read_text() == (ART / "golden-v2.md.txt").read_text(), (
        "v2 surface output changed — the default surface must stay byte-identical"
    )


def test_v3_fixtures_current(v3_outputs):
    author, brief, evidence = v3_outputs
    assert author == (TESTDATA / "v3-fixture-author.md.txt").read_text()
    assert brief == (TESTDATA / "v3-fixture-brief.md.txt").read_text()
    assert evidence == json.loads((TESTDATA / "v3-fixture-evidence-base.json").read_text())


def test_markers_on_own_lines(v3_outputs):
    author, brief, _ = v3_outputs
    lines = author.splitlines()
    assert lines[0] == "<!-- CLAUDE_REVIEW 1/1 -->"
    assert lines[1] == "<!-- CLAUDE_REVIEW_AUTHOR -->"
    assert lines[2].startswith("<!-- CLAUDE_REVIEW_HEAD ")
    assert brief.splitlines()[0] == "<!-- CLAUDE_REVIEW_BRIEF -->"


def test_single_head_carrier(v3_outputs):
    author, brief, _ = v3_outputs
    assert author.count("CLAUDE_REVIEW_HEAD") == 1
    assert "CLAUDE_REVIEW_HEAD" not in brief, "brief must carry a display-only sha"


def test_review_state_parses(v3_outputs):
    author, _, evidence = v3_outputs
    state = review_state.parse_state(author)
    assert state is not None and state["findings"] == {}
    assert state["high_water"] == evidence["high_water"]


def test_verdict_split(v3_outputs):
    author, brief, evidence = v3_outputs
    by_bucket = {}
    for f in evidence["findings"]:
        by_bucket.setdefault(f["bucket"], []).append(f)
    # fixture artifacts: contradicted → outstanding, vale blocker → outstanding,
    # unverifiable → author-answer, framing-drift → reviewer-check
    assert {f["origin"] for f in by_bucket["outstanding"]} == {"verdict:contradicted", "style-blocker"}
    assert [f["origin"] for f in by_bucket["author-answer"]] == ["verdict:unverifiable"]
    assert [f["origin"] for f in by_bucket["reviewer-check"]] == ["verdict:framing-drift"]
    author_sections = author.split("### ❓")
    assert all(f["id"] in author_sections[0] for f in by_bucket["outstanding"])
    assert all(f["id"] in author_sections[1] for f in by_bucket["author-answer"])
    assert all(f["id"] in brief for f in by_bucket["reviewer-check"])


def test_no_stale_v2_vocabulary(v3_outputs):
    author, brief, _ = v3_outputs
    for tok in cr._V3_STALE_TOKENS:
        assert tok not in author, tok
        assert tok not in brief, tok


def test_evidence_base_schema_shape(v3_outputs):
    _, _, ev = v3_outputs
    for key in ("schema_version", "repo", "pr", "head_sha", "run_id", "generated_at",
                "findings", "trail", "investigation_log", "history", "high_water"):
        assert key in ev, key
    assert ev["schema_version"] == 1
    ids = [f["id"] for f in ev["findings"]]
    assert len(ids) == len(set(ids))
    assert all(fid.startswith("F") and fid[1:].isdigit() for fid in ids)
    assert ev["high_water"] >= max(int(fid[1:]) for fid in ids)
    for f in ev["findings"]:
        assert f["bucket"] in ("outstanding", "author-answer", "reviewer-check", "preexisting")
        assert f["file"] and f["text"]
    for t in ev["trail"]:
        assert t["verdict"] in cr.TRAIL_VERDICT_WORDS
        assert t["file"] and t["claim"]
    assert ev["history"] and all(h.get("sha") for h in ev["history"])


def test_evidence_url_token_present(v3_outputs):
    author, brief, _ = v3_outputs
    assert cr.EVIDENCE_URL_TOKEN in author
    assert cr.EVIDENCE_URL_TOKEN in brief


@pytest.mark.parametrize("fid,bullet", [
    ("F1", "- **[L12-14]** `content/docs/x.md` — *\"claim\"* — verdict: contradicted <TODO: fix>"),
    ("F7", "- **[L95]** `a.md` — body text"),
    ("F12", "- **[L1]** file-less detector finding body"),
    ("F?", "- plain body, no anchor, no file"),
])
def test_finding_line_round_trip(fid, bullet):
    rendered = cr.render_finding_line(fid, bullet)
    parsed = cr.parse_finding_line(rendered)
    assert parsed is not None, rendered
    assert parsed["id"] == fid
    # the body survives: strip the structural prefix the parser consumed
    assert parsed["body"] in rendered


def test_parse_rejects_non_findings():
    assert cr.parse_finding_line("_No open questions for you._") is None
    assert cr.parse_finding_line("- **line 33:** [style] _wordiness_ — msg") is None
    assert cr.parse_finding_line("- [ ] *F1* broken emphasis") is None


def test_build_evidence_self_test():
    proc = subprocess.run(
        [sys.executable, str(HERE / "build-evidence.py"), "--self-test"],
        capture_output=True, text=True,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr


def test_build_evidence_on_fixtures(v3_outputs, tmp_path):
    """The unedited composer drafts round-trip through build-evidence: same
    findings, same buckets — the base case every model edit builds on."""
    author, brief, ev = v3_outputs
    a, b, base = tmp_path / "a.md", tmp_path / "b.md", tmp_path / "base.json"
    a.write_text(author)
    b.write_text(brief)
    base.write_text(json.dumps(ev))
    out = tmp_path / "final.json"
    proc = subprocess.run(
        [sys.executable, str(HERE / "build-evidence.py"),
         "--author-body", str(a), "--brief-body", str(b), "--base", str(base),
         "--output", str(out),
         "--author-out", str(tmp_path / "a-clean.md"), "--brief-out", str(tmp_path / "b-clean.md")],
        capture_output=True, text=True,
    )
    assert proc.returncode == 0, proc.stderr
    final = json.loads(out.read_text())
    assert {f["id"]: f["bucket"] for f in final["findings"]} == {f["id"]: f["bucket"] for f in ev["findings"]}
    assert (tmp_path / "a-clean.md").read_text().count("CLAUDE_REVIEW_HEAD") == 1


def test_row_pipe_escaping_round_trips():
    row = cr.render_finding_row("F7", ref="L4", file="a.md",
                                body="use `a | b` in the shell, not a\\|b")
    assert row.count("|") >= 5  # cell pipes escaped, structure intact
    parsed = cr.parse_finding_line(row)
    assert parsed is not None
    assert parsed["body"] == "use `a | b` in the shell, not a\\|b"


def test_row_diff_link():
    row = cr.render_finding_row(
        "F1", ref="L12-14", file="content/docs/x.md", body="x",
        link_base="https://github.com/pulumi/docs/pull/999/files")
    import hashlib
    anchor = hashlib.sha256(b"content/docs/x.md").hexdigest()
    assert f"/pull/999/files#diff-{anchor}R12)" in row
    parsed = cr.parse_finding_line(row)
    assert parsed is not None and parsed["ref"] == "L12-14" and parsed["file"] == "content/docs/x.md"
    bare = cr.render_finding_row("F1", ref="L12-14", file="content/docs/x.md", body="x")
    assert cr.parse_finding_line(bare)["ref"] == "L12-14"


def test_table_furniture_recognized():
    assert cr.is_table_furniture(cr.FINDING_TABLE_HEADER)
    assert cr.is_table_furniture(cr.FINDING_TABLE_SEPARATOR)
    assert cr.is_table_furniture("| --- | --- | --- |")
    assert not cr.is_table_furniture(cr.render_finding_row("F1", body="x"))


# ---- editorial stances on the v3 surface ------------------------------------
#
# Master's #21312 gave positioning/comparison language a verdict-free home
# under ⚠️ on the v2 monolith. On v3 the same H4 rides the reviewer brief's
# ⚠️ section, the evidence object carries the records, and the coverage rule
# holds the brief to the artifact.

vp = _load("validate_pinned_for_stances", HERE / "validate-pinned.py")
au = _load("apply_update_for_stances", HERE / "apply-update.py")
STANCE_ART = ART / "candidate-claims-stances.json"


@pytest.fixture(scope="module")
def v3_with_stances(tmp_path_factory):
    tmp = tmp_path_factory.mktemp("v3s")
    author, brief, evidence = tmp / "a.md", tmp / "b.md", tmp / "e.json"
    cmd = regen_cmd("v3", [
        "--out", str(tmp / "unused.md"),
        "--out-author", str(author), "--out-brief", str(brief), "--out-evidence", str(evidence),
    ])
    cmd[cmd.index("--candidate-claims") + 1] = str(STANCE_ART)
    proc = subprocess.run(cmd, capture_output=True, text=True)
    assert proc.returncode == 0, proc.stderr
    return author.read_text(), brief.read_text(), json.loads(evidence.read_text())


def _stance_ctx(author: str, brief: str, base: dict, stances):
    return vp.Context(
        body=author, body_lines=author.splitlines(), pr=None, repo=None,
        diff_files=[], diff_files_added=set(), diff_text="", repo_root=REPO_ROOT,
        is_blog=False, surface="v3", brief=brief, evidence_base=base,
        candidate_stances=stances,
    )


def test_stances_render_on_the_brief_not_the_author_card(v3_with_stances):
    author, brief, ev = v3_with_stances
    assert cr.STANCES_HEADING not in author
    assert cr.STANCES_HEADING in brief
    check_at = brief.index("### ⚠️ Check these before approving")
    stamp_at = brief.index("### ✅ What you can rubber-stamp")
    h4_at = brief.index(cr.STANCES_HEADING)
    assert check_at < h4_at < stamp_at
    bullet = next(ln for ln in brief.splitlines() if ln.startswith("- L12"))
    assert "fastest path" in bullet and "positioning (found by regex+llm)" in bullet
    # verdict-free: no finding id, no emoji verdict
    assert "**F" not in bullet and "✅" not in bullet


def test_stances_recorded_in_evidence(v3_with_stances):
    _, _, ev = v3_with_stances
    assert ev["stances"] == [{
        "file": "content/docs/iac/x.md", "line": 12,
        "text": "`pulumi convert` is the fastest path for most configurations, and it's where to start.",
        "type": "positioning", "found_by": ["regex", "llm"],
    }]
    ve = _load("validate_evidence_for_stances", REPO_ROOT / "scripts" / "review-v3" / "validate-evidence.py")
    assert ve.validate_evidence(ev) == []


def test_stances_absent_when_artifact_predates_split(v3_outputs):
    _, brief, ev = v3_outputs
    assert cr.STANCES_HEADING not in brief
    assert "stances" not in ev


def test_stances_are_not_findings(v3_with_stances):
    """The sub-list sits under an H4, so every row walker stops before it:
    no F-ids assigned, nothing in REVIEW_STATE, nothing in findings[]."""
    author, brief, ev = v3_with_stances
    assert all("fastest path" not in f["text"] for f in ev["findings"])
    rows = au._collect_rows(author, brief)
    assert all("fastest path" not in r["parsed"]["body"] for r in rows.values())


def test_stances_coverage_rule_on_v3(v3_with_stances):
    author, brief, ev = v3_with_stances
    stances = json.loads(STANCE_ART.read_text())["stances"]
    skip = {"no-todo-tokens"}
    ids = lambda vs: {v.rule_id for v in vs}  # noqa: E731
    assert "editorial-stances-coverage" not in ids(vp.run_checks(_stance_ctx(author, brief, ev, stances), skip_rules=skip))
    # dropping the bullet is a violation …
    dropped = "\n".join(ln for ln in brief.splitlines() if not ln.startswith("- L12"))
    assert "editorial-stances-coverage" in ids(vp.run_checks(_stance_ctx(author, dropped, ev, stances), skip_rules=skip))
    # … so is decorating it with a verdict …
    graded = brief.replace("positioning (found by regex+llm)", "positioning (found by regex+llm) ✅ verified")
    assert "editorial-stances-coverage" in ids(vp.run_checks(_stance_ctx(author, graded, ev, stances), skip_rules=skip))
    # … and so is a block the artifact doesn't back.
    assert "editorial-stances-coverage" in ids(vp.run_checks(_stance_ctx(author, brief, ev, []), skip_rules=skip))
    # No artifact at all: nothing to hold the brief to.
    assert "editorial-stances-coverage" not in ids(vp.run_checks(_stance_ctx(author, brief, ev, None), skip_rules=skip))


def test_stances_survive_update_lane_rerender(v3_with_stances):
    """apply-update re-renders the ⚠️ table from rows; the H4 below it is
    outside the section span and comes through verbatim."""
    author, brief, ev = v3_with_stances
    rows = au._collect_rows(author, brief)
    out = au._render_doc(brief, rows, [], doc="brief")
    assert cr.STANCES_HEADING in out
    assert any(ln.startswith("- L12") and "fastest path" in ln for ln in out.splitlines())
    assert out.index("### ⚠️ Check these before approving") < out.index(cr.STANCES_HEADING) < out.index("### ✅ What you can rubber-stamp")


def test_stances_survive_build_evidence(v3_with_stances, tmp_path):
    author, brief, ev = v3_with_stances
    a, b, base = tmp_path / "a.md", tmp_path / "b.md", tmp_path / "base.json"
    a.write_text(author); b.write_text(brief); base.write_text(json.dumps(ev))
    out = tmp_path / "final.json"
    proc = subprocess.run(
        [sys.executable, str(HERE / "build-evidence.py"),
         "--author-body", str(a), "--brief-body", str(b), "--base", str(base),
         "--output", str(out),
         "--author-out", str(tmp_path / "a-clean.md"), "--brief-out", str(tmp_path / "b-clean.md")],
        capture_output=True, text=True,
    )
    assert proc.returncode == 0, proc.stderr
    final = json.loads(out.read_text())
    assert final["stances"] == ev["stances"]
    assert cr.STANCES_HEADING in (tmp_path / "b-clean.md").read_text()
    html = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "review-v3" / "render-evidence-html.py"),
         "--evidence", str(out), "--output", str(tmp_path / "e.html")],
        capture_output=True, text=True,
    )
    assert html.returncode == 0, html.stderr
    page = (tmp_path / "e.html").read_text()
    assert 'id="stances"' in page and "fastest path" in page
