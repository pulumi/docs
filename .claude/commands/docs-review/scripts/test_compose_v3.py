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


# ---- verifier metadata on trail records ------------------------------------

_TRAIL_META_KEYS = ("claim_id", "type", "confidence", "framing", "framing_note",
                    "turn_cap_exhausted", "source_discipline_gate")


def test_trail_metadata_carries_every_field_the_verdict_has():
    got = cr._trail_verdict_metadata({
        "claim_id": "c7", "type": "version", "confidence": "low",
        "framing": "shifted", "framing_note": "  page says GA, source says preview  ",
        "turn_cap_exhausted": True, "source_discipline_gate": "generated-from-data",
        # Verifier bookkeeping the evidence object has no use for.
        "model_usage": {"turns": 4}, "intuition_flag": "smells stale",
    })
    assert got == {
        "claim_id": "c7", "type": "version", "confidence": "low",
        "framing": "shifted", "framing_note": "page says GA, source says preview",
        "turn_cap_exhausted": True, "source_discipline_gate": "generated-from-data",
    }


def test_trail_metadata_drops_malformed_values_instead_of_coercing():
    """A bad optional field must not fail the whole evidence object's schema
    validation — that would cost the review its publish over a debug aid."""
    assert cr._trail_verdict_metadata({
        "claim_id": "", "type": None, "confidence": "certain", "framing": "vibes",
        "framing_note": 3, "turn_cap_exhausted": "yes", "source_discipline_gate": "  ",
    }) == {}
    assert cr._trail_verdict_metadata({"turn_cap_exhausted": False}) == {}
    assert cr._trail_verdict_metadata({}) == {}


def test_trail_metadata_redacts_the_framing_note():
    got = cr._trail_verdict_metadata({"framing_note": "token ghp_" + "a" * 36 + " leaked"})
    assert "ghp_" not in got["framing_note"] and "[REDACTED]" in got["framing_note"]


def test_composed_trail_carries_verdict_metadata(v3_outputs):
    _, _, ev = v3_outputs
    verdicts = json.loads((ART / "verified-claims.json").read_text())["verdicts"]
    by_id = {t["claim_id"]: t for t in ev["trail"]}
    assert set(by_id) == {v["claim_id"] for v in verdicts}
    for v in verdicts:
        assert by_id[v["claim_id"]]["type"] == v["type"]
        assert by_id[v["claim_id"]]["confidence"] == v["confidence"]
    assert by_id["c4"]["framing_note"] == "widened denominator"


def _run_build_evidence(author: str, brief: str, base: dict, tmp_path: Path) -> dict:
    a, b, bj = tmp_path / "a.md", tmp_path / "b.md", tmp_path / "base.json"
    a.write_text(author); b.write_text(brief); bj.write_text(json.dumps(base))
    out = tmp_path / "final.json"
    proc = subprocess.run(
        [sys.executable, str(HERE / "build-evidence.py"),
         "--author-body", str(a), "--brief-body", str(b), "--base", str(bj),
         "--output", str(out),
         "--author-out", str(tmp_path / "a-clean.md"), "--brief-out", str(tmp_path / "b-clean.md")],
        capture_output=True, text=True,
    )
    assert proc.returncode == 0, proc.stderr
    return json.loads(out.read_text())


def _update_round(prior: dict, author: str, brief: str) -> dict:
    """One `#update-review` round: apply-update rebuilds the evidence object
    from the prior record (and validates it before returning)."""
    up = {"schema": 1, "case": "mixed", "history_summary": "round trip",
          "findings": [{"id": "F1", "action": "resolve", "annotation": "fixed in e7e8e9"}]}
    sha = "c" * 40
    a_out, b_out, state, report = au.apply(author, brief, up, head_sha=sha, actor="cam", auto=False)
    return au.assemble_evidence(prior, a_out, b_out, state, up,
                                repo="pulumi/docs", pr=999, head_sha=sha, run_id="t",
                                timestamp=report["timestamp"])


def _render_page(evidence: dict, tmp_path: Path) -> str:
    src, out = tmp_path / "render-in.json", tmp_path / "e.html"
    src.write_text(json.dumps(evidence))
    proc = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "review-v3" / "render-evidence-html.py"),
         "--evidence", str(src), "--output", str(out)],
        capture_output=True, text=True,
    )
    assert proc.returncode == 0, proc.stderr
    return out.read_text()


def test_trail_metadata_round_trips_compose_to_update_lane(v3_outputs, tmp_path):
    """compose → build-evidence → validate → apply-update → render: every
    stage that touches the trail keeps the verifier metadata intact."""
    author, brief, base = v3_outputs
    assert any(k in t for t in base["trail"] for k in _TRAIL_META_KEYS)
    final = _run_build_evidence(author, brief, base, tmp_path)
    assert final["trail"] == base["trail"]
    ve = _load("validate_evidence_for_trail_meta", REPO_ROOT / "scripts" / "review-v3" / "validate-evidence.py")
    assert ve.validate_evidence(final) == []
    updated = _update_round(final, author, brief)
    assert updated["trail"] == base["trail"]
    page = _render_page(updated, tmp_path)
    assert "pass3 · statistic · low confidence" in page
    assert "framing: widened denominator" in page


def test_legacy_trail_without_metadata_still_round_trips(v3_outputs, tmp_path):
    """Evidence objects already in S3 pre-date the metadata; an update round
    over one must validate, carry the trail unchanged, and render."""
    author, brief, base = v3_outputs
    legacy = {**base, "trail": [{k: v for k, v in t.items() if k not in _TRAIL_META_KEYS}
                                for t in base["trail"]]}
    final = _run_build_evidence(author, brief, legacy, tmp_path)
    assert final["trail"] == legacy["trail"]
    ve = _load("validate_evidence_for_legacy_trail", REPO_ROOT / "scripts" / "review-v3" / "validate-evidence.py")
    assert ve.validate_evidence(final) == []
    updated = _update_round(final, author, brief)
    assert updated["trail"] == legacy["trail"]
    page = _render_page(updated, tmp_path)
    assert "confidence</span>" not in page
    assert '<span class="trail-route">pass3</span>' in page


def test_empty_checks_sentinel_acknowledges_stances(v3_with_stances, tmp_path):
    """An empty ⚠️ table above a stances H4 must not say nothing needs a human
    eye (pulumi/docs#21369). All three emitters agree: apply-update's
    re-render, build-evidence's collapse, and the composer's helper."""
    author, brief, ev = v3_with_stances
    assert cr.STANCES_HEADING in brief
    # apply-update: every brief row dropped → the stance-aware sentinel.
    rows = au._collect_rows(author, brief)
    author_only = {fid: r for fid, r in rows.items() if r["doc"] == "author"}
    out = au._render_doc(brief, author_only, [], doc="brief")
    assert cr._V3_EMPTY_CHECKS_STANCES in out and cr._V3_EMPTY_CHECKS not in out
    assert out.index(cr._V3_EMPTY_CHECKS_STANCES) < out.index(cr.STANCES_HEADING)
    # build-evidence: a table left with only furniture collapses the same way.
    be = _load("build_evidence_for_sentinel", HERE / "build-evidence.py")
    lines = brief.splitlines()
    span = next((s, e) for b, s, e in be._sections(brief, be.BRIEF_SECTIONS) if b == "reviewer-check")
    furniture = lines[:span[0]] + ["", cr.FINDING_TABLE_HEADER, cr.FINDING_TABLE_SEPARATOR, ""] + lines[span[1]:]
    collapsed = be._collapse_empty_tables("\n".join(furniture), be.BRIEF_SECTIONS)
    assert cr._V3_EMPTY_CHECKS_STANCES in collapsed and cr._V3_EMPTY_CHECKS not in collapsed
    # No stances below → the plain sentinel, unchanged.
    assert cr.empty_checks_sentinel(False) == cr._V3_EMPTY_CHECKS
    h4 = furniture.index(cr.STANCES_HEADING)
    nxt = next(i for i in range(h4 + 1, len(furniture)) if furniture[i].startswith("### "))
    without = "\n".join(furniture[:h4] + furniture[nxt:])
    assert cr._V3_EMPTY_CHECKS in be._collapse_empty_tables(without, be.BRIEF_SECTIONS)


def test_dead_link_entries_are_stubbed_even_when_hugo_was_skipped():
    """link-check-diff.py appends to `link_integrity` on the skip-stub artifact
    (content-only PRs); the composer must still pre-stub them as 🚨 rows."""
    art = {
        "skipped": True,
        "errors": ["ERROR this would be a build error but Hugo did not run"],
        "link_integrity": [
            "content/docs/iac/x.md:114: dead internal link /docs/iac/concepts/stack-references/ — no page, alias, or PR-added file under content/",
        ],
        "link_check": {"ran": True, "checked": 3, "dead": 1},
    }
    verdicts = cr._hugo_synthetic_verdicts(art)
    assert [v["type"] for v in verdicts] == ["hugo-link-integrity"], verdicts
    assert verdicts[0]["file"] == "content/docs/iac/x.md"
    assert verdicts[0]["line_range"] == "L114"
    assert verdicts[0]["route"] == "preflight" and verdicts[0]["verdict"] == "flagged"


def _compose_v3_with_hugo(tmp_path, hugo_obj):
    hugo = tmp_path / "hugo-build.json"
    hugo.write_text(json.dumps(hugo_obj))
    author, brief = tmp_path / "a.md", tmp_path / "b.md"
    cmd = regen_cmd("v3", [
        "--out", str(tmp_path / "unused.md"),
        "--out-author", str(author), "--out-brief", str(brief), "--out-evidence", str(tmp_path / "e.json"),
    ])
    cmd[cmd.index("--hugo-build") + 1] = str(hugo)
    proc = subprocess.run(cmd, capture_output=True, text=True)
    assert proc.returncode == 0, proc.stderr
    return author.read_text(), brief.read_text()


def test_dead_link_stub_reaches_the_v3_author_card(tmp_path):
    author, brief = _compose_v3_with_hugo(tmp_path, {
        "skipped": True, "errors": [],
        "link_integrity": [
            "content/docs/iac/x.md:12: dead internal link /docs/iac/nowhere/ — no page, alias, or PR-added file under content/",
        ],
        "link_check": {"ran": True, "checked": 1, "dead": 1},
    })
    assert "/docs/iac/nowhere/" in author
    assert "1 of 1 added internal link(s) dead" in brief


def test_unrun_link_check_is_named_on_the_brief(tmp_path):
    _author, brief = _compose_v3_with_hugo(tmp_path, {
        "skipped": True, "errors": [], "link_integrity": [],
        "link_check": {"ran": False, "checked": 0, "dead": 0, "error": "boom"},
    })
    assert "internal-link check did not run" in brief


def test_detail_scaffold_is_a_bulleted_list():
    lines = cr.render_detail_scaffold("F7")
    assert lines[0] == "#### F7 · Do this" and lines[1] == ""
    assert [ln[:6] for ln in lines[2:5]] == ["- **Li", "- **Wh", "- **Fi"]
    assert sum(ln.startswith("- **Fix:**") for ln in lines) == 1


def test_trail_metadata_vocabularies_match_the_evidence_validator():
    # The composer filters trail metadata to these values and the validator
    # rejects anything outside its own copy, so the two lists must move together.
    ve = _load("validate_evidence_for_vocab", REPO_ROOT / "scripts" / "review-v3" / "validate-evidence.py")
    assert set(cr._TRAIL_CONFIDENCES) == ve.CONFIDENCES
    assert set(cr._TRAIL_FRAMINGS) == ve.FRAMINGS


# ---- the `[nit]` lane -------------------------------------------------------
# The v3 author card's advisory block is its only non-blocking lane, so it also
# carries the nits the review finds itself (compose-review.NIT_TAG). Before
# that, PR #21787 F3 shipped "Typo: `i. e.` has a stray space … Trivial fix for
# the author" on the reviewer's card, which is headed "not for the author".

NIT_BULLET = "- **line 73:** [nit] _typo_ — `i. e.` has a stray space; use `i.e.`"


def _append_nit(author: str, bullet: str = NIT_BULLET) -> str:
    """Drop a bullet under the last `##### <path>` group, the way the
    editorial pass does."""
    lines = author.splitlines()
    last = max(i for i, ln in enumerate(lines) if ln.startswith("- **line "))
    lines.insert(last + 1, bullet)
    return "\n".join(lines) + "\n"


def _compose_v3_without_vale(tmp_path) -> tuple[str, str, dict]:
    vale = tmp_path / "vale-empty.json"
    vale.write_text("[]")
    author, brief, ev = tmp_path / "a.md", tmp_path / "b.md", tmp_path / "e.json"
    cmd = regen_cmd("v3", [
        "--out", str(tmp_path / "unused.md"), "--out-author", str(author),
        "--out-brief", str(brief), "--out-evidence", str(ev),
    ])
    cmd[cmd.index("--vale-findings") + 1] = str(vale)
    proc = subprocess.run(cmd, capture_output=True, text=True)
    assert proc.returncode == 0, proc.stderr
    return author.read_text(), brief.read_text(), json.loads(ev.read_text())


def test_style_block_is_always_composed_on_v3(tmp_path):
    """The model needs a stable anchor to append a `[nit]` under; asking it to
    author the H4 and caption verbatim is how you get a malformed block."""
    author, _brief, _ev = _compose_v3_without_vale(tmp_path)
    assert cr.STYLE_HEADING in author
    assert cr._V3_EMPTY_STYLE in author


def test_empty_style_block_is_dropped_at_publish(tmp_path):
    """...but an empty one never reaches the published card."""
    author, brief, base = _compose_v3_without_vale(tmp_path)
    be_mod = _load("build_evidence_for_style", HERE / "build-evidence.py")
    _ev, author_out, _brief_out = be_mod.build(author, brief, base)
    assert cr.STYLE_HEADING not in author_out
    assert cr._V3_EMPTY_STYLE not in author_out
    assert "\n\n\n" not in author_out, "collapsing the block left a gap"


def test_model_added_nit_keeps_the_block(tmp_path):
    author, brief, base = _compose_v3_without_vale(tmp_path)
    lines = author.splitlines()
    i = lines.index(cr._V3_EMPTY_STYLE)
    lines[i:i + 1] = ["##### content/docs/iac/x.md", "", NIT_BULLET]
    be_mod = _load("build_evidence_for_style2", HERE / "build-evidence.py")
    ev, author_out, brief_out = be_mod.build("\n".join(lines) + "\n", brief, base)
    assert NIT_BULLET in author_out
    assert ev["style_suggestions_count"] == 1
    assert "0 from linting, 1 found by the review" in brief_out


def test_nit_moves_the_briefs_rubber_stamp_count(v3_outputs, tmp_path):
    """The reviewer is asked to rubber-stamp this number, so it has to be the
    number on the card — not the one Vale produced before the model read the
    diff."""
    author, brief, base = v3_outputs
    assert "- **Style:** 1 advisory suggestion left" in brief
    final = _run_build_evidence(_append_nit(author), brief, base, tmp_path)
    assert final["style_suggestions_count"] == 2
    published = (tmp_path / "b-clean.md").read_text()
    assert "- **Style:** 2 advisory suggestions (1 from linting, 1 found by the review)" in published


def test_update_lane_recounts_nits(v3_outputs):
    """A refresh re-renders the block; carrying the prior count forward would
    pin the brief to whatever Vale said on the first run."""
    author, brief, base = v3_outputs
    ev = _update_round(base, _append_nit(author), brief)
    assert ev["style_suggestions_count"] == 2


def _compose_v3_clean(tmp_path) -> tuple[str, str, dict]:
    """A v3 compose with nothing to report: no Vale findings, no verdicts,
    no detector artifacts."""
    empty = tmp_path / "empty.json"
    empty.write_text("[]")
    author, brief, ev = tmp_path / "a.md", tmp_path / "b.md", tmp_path / "e.json"
    cmd = regen_cmd("v3", [
        "--out", str(tmp_path / "unused.md"), "--out-author", str(author),
        "--out-brief", str(brief), "--out-evidence", str(ev),
    ])
    for flag in ("--vale-findings", "--verified-claims"):
        cmd[cmd.index(flag) + 1] = str(empty)
    for flag in ("--frontmatter", "--hugo-build", "--editorial-balance", "--cross-sibling"):
        cmd[cmd.index(flag) + 1] = "/dev/null"
    proc = subprocess.run(cmd, capture_output=True, text=True)
    assert proc.returncode == 0, proc.stderr
    return author.read_text(), brief.read_text(), json.loads(ev.read_text())


def test_clean_card_publishes_without_the_empty_blocking_sections(tmp_path):
    """The composer keeps both sections so the model has somewhere to add a
    finding; with none added, the published card is just the NOTE."""
    author, brief, base = _compose_v3_clean(tmp_path)
    assert "\n### 🚨 Fix or disagree\n" in author and "\n### ❓ Questions for you\n" in author
    be_mod = _load("build_evidence_for_clean", HERE / "build-evidence.py")
    _ev, author_out, brief_out = be_mod.build(author, brief, base)
    assert "— nothing blocks merge" in author_out
    assert "\n### 🚨" not in author_out and "\n### ❓" not in author_out
    assert "\n\n\n" not in author_out.split("<!-- CLAUDE_REVIEW_FOOTER -->")[0]
    import test_validate_pinned_v3 as tv
    assert [v.rule_id for v in tv.check(author_out, brief_out, _ev)] == []


LONG_CLAIM = ("The GitHub repository at https://github.com/pulumi/examples/tree/master/"
              "aws-ts-awsx-vpc-state-migration contains all three example programs (v1, v2, v3) "
              "and the migration code shown in this post")
FRAMING = "The page loads, but the fetched body says nothing about the directory's contents."


def test_author_cell_names_the_claim_and_the_block_carries_the_reason(tmp_path):
    """pulumi/docs#21871: each ❓ row quoted its claim in the cell, then the
    Do-this block quoted the line again, and the framing note in the cell
    said what the Why bullet then said again."""
    art = json.loads((ART / "verified-claims.json").read_text())
    art["verdicts"][1] = dict(art["verdicts"][1], text=LONG_CLAIM, framing_note=FRAMING)
    vc = tmp_path / "vc.json"
    vc.write_text(json.dumps(art))
    author = tmp_path / "a.md"
    cmd = regen_cmd("v3", ["--out", str(tmp_path / "u.md"), "--out-author", str(author),
                           "--out-brief", str(tmp_path / "b.md"), "--out-evidence", str(tmp_path / "e.json")])
    cmd[cmd.index("--verified-claims") + 1] = str(vc)
    proc = subprocess.run(cmd, capture_output=True, text=True)
    assert proc.returncode == 0, proc.stderr
    card = author.read_text()
    row = next(ln for ln in card.splitlines() if ln.startswith("| **F3** |"))
    parsed = cr.parse_finding_line(row)
    assert parsed is not None and "— verdict: unverifiable" in parsed["body"]
    quoted = parsed["body"].split('"')[1]
    assert quoted.endswith("…") and len(quoted) <= cr.AUTHOR_CELL_TRUNC
    assert LONG_CLAIM.startswith(quoted[:-1].rstrip())
    assert "framing:" not in row, "the note moved to the Why prompt"
    block = card.split("#### F3 · Do this", 1)[1]
    why = next(ln for ln in block.splitlines() if ln.startswith("- **Why:**"))
    assert FRAMING in why
    evidence = json.loads((tmp_path / "e.json").read_text())
    f3 = next(f for f in evidence["findings"] if f["id"] == "F3")
    assert len(f3["text"]) > len(quoted), "the evidence record keeps the longer claim text"
