#!/usr/bin/env python3
"""Tests for apply-update.py — the v3 update lane's deterministic renderer.

The heavy truth-table lives in the script's own `--self-test` (every action,
the /resolve race, auto-mode drops, demotion/unknown-id rejection, evidence
carry-forward + degraded path); this file makes pytest collection run it and
adds the cases that read better as separate tests.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod  # before exec — @dataclass needs the module registered
    spec.loader.exec_module(mod)
    return mod


au = _load("apply_update", HERE / "apply-update.py")

AUTHOR = (HERE / "testdata" / "v3-fixture-author.md").read_text()
BRIEF = (HERE / "testdata" / "v3-fixture-brief.md").read_text()
SHA = "c" * 40


def _update(findings, case="mixed"):
    return {"schema": 1, "case": case, "history_summary": "test", "findings": findings}


def test_self_test_suite():
    assert au._self_test() == 0


def test_retext_preserves_id_and_anchor():
    up = _update([{"id": "F3", "action": "retext", "text": "sharper question for the author"}])
    a_out, _, state, _ = au.apply(AUTHOR, BRIEF, up, head_sha=SHA, actor="cam", auto=False)
    assert "sharper question for the author" in a_out
    assert "| **F3** | `content/docs/iac/x.md` L61 |" in a_out
    assert "F3" not in state["findings"], "retext writes no disposition"


def test_resolve_without_annotation_rejected():
    up = _update([{"id": "F1", "action": "resolve"}])
    try:
        au.apply(AUTHOR, BRIEF, up, head_sha=SHA, actor="cam", auto=False)
    except au.UpdateError as exc:
        assert "annotation" in str(exc)
    else:
        raise AssertionError("resolve without annotation must be rejected")


def test_emptied_section_gets_placeholder():
    up = _update([
        {"id": "F1", "action": "resolve", "annotation": "fixed in d4d5d6"},
        {"id": "F2", "action": "resolve", "annotation": "fixed in d4d5d6"},
    ])
    a_out, _, _, report = au.apply(AUTHOR, BRIEF, up, head_sha=SHA, actor="cam", auto=False)
    assert au.SECTION_EMPTY["outstanding"] in a_out
    assert report["blocking"] == 1  # F3 still open in ❓


def test_assembled_evidence_passes_validator():
    base = json.loads((HERE / "testdata" / "v3-fixture-evidence-base.json").read_text())
    up = _update([{"id": "F1", "action": "resolve", "annotation": "fixed in e7e8e9"}])
    a_out, b_out, state, report = au.apply(AUTHOR, BRIEF, up, head_sha=SHA, actor="cam", auto=False)
    ev = au.assemble_evidence(base, a_out, b_out, state, up,
                              repo="pulumi/docs", pr=999, head_sha=SHA, run_id="t",
                              timestamp=report["timestamp"])
    assert au.validate_evidence_mod.validate_evidence(ev) == []


def test_malformed_update_json_is_exit_2_shape():
    up = {"schema": 2, "case": "nope", "findings": "not-a-list"}
    try:
        au.apply(AUTHOR, BRIEF, up, head_sha=SHA, actor="cam", auto=False)
    except au.UpdateError as exc:
        msg = str(exc)
        assert "schema" in msg and "case" in msg and "findings" in msg
    else:
        raise AssertionError("malformed update must be rejected")


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print(f"  ok: {name}")
    print("test_apply_update: all passed")


def _open_author_ids(a_out: str) -> set[str]:
    return {r["parsed"]["id"] for r in au._collect_rows(a_out, "").values()}


def test_last_section_rerender_keeps_evidence_line_and_hint():
    # Regression: the first live #update-review (fork PR 242, 2026-09-01) lost
    # the 📎 line — the ❓ section's detail block swallowed the browser hint and
    # the section span ran through the 📎 line behind it.
    up = _update([{"id": "F3", "action": "retext", "text": "*\"x\"* — sharper, still open"}])
    a_out, b_out, _, _ = au.apply(AUTHOR, BRIEF, up, head_sha=SHA, actor="cam", auto=False,
                                  head_repo="example/docs-fork", head_branch="fix/component-doc")
    assert a_out.count("📎 **Full evidence:**") == 1
    assert a_out.count(au.cr.V3_BROWSER_HINT_PREFIX) == 1
    _spans, texts = au.be.collect_detail_blocks(a_out)
    assert set(texts) == {"F1", "F2", "F3"}
    assert not any("Editing in the browser" in t for t in texts.values()), "hint never inside a block"
    assert a_out.index(au.cr.V3_BROWSER_HINT_PREFIX) < a_out.index("📎 **Full evidence:**")


def test_hold_moves_row_to_brief_and_records_refuted():
    up = _update([{"id": "F3", "action": "hold", "reason": "no published source; reviewer's call"}],
                 case="dispute")
    a_out, b_out, state, report = au.apply(AUTHOR, BRIEF, up, head_sha=SHA, actor="cam", auto=False)
    assert "F3" not in _open_author_ids(a_out)
    assert "**F3**" in b_out and "model held.** no published source" in b_out
    assert state["findings"]["F3"]["disposition"] == "refuted"
    assert state["findings"]["F3"]["actor"] == "cam"
    assert report["blocking"] == 2
    assert "**F3**" not in b_out.split("<!-- AUTHOR_STATE_END -->")[0], "held row left the Waiting table"
    assert au.SECTION_EMPTY["author-answer"] in a_out


def test_retext_detail_rebuilds_block_keeping_verbatim_line():
    up = _update([{"id": "F1", "action": "retext", "text": "*\"q\"* — narrowed",
                   "detail": {"why": "new why", "fix": "Attribute it inline.",
                              "keep": "cite the study"}}])
    a_out, _, _, _ = au.apply(AUTHOR, BRIEF, up, head_sha=SHA, actor="cam", auto=False)
    _spans, texts = au.be.collect_detail_blocks(a_out)
    block = texts["F1"]
    assert block.startswith("**Line (verbatim):**")
    assert "**Why:** new why" in block and "**Fix:** Attribute it inline." in block
    assert "**If you'd rather keep it:** cite the study" in block
    assert block.count("**Fix:**") == 1


def test_retext_detail_shape_is_validated():
    bad = _update([{"id": "F1", "action": "retext", "text": "t", "detail": {"why": "w"}}])
    try:
        au.apply(AUTHOR, BRIEF, bad, head_sha=SHA, actor="cam", auto=False)
    except au.UpdateError as e:
        assert "detail.fix" in str(e)
    else:
        raise AssertionError("missing detail.fix accepted")


def test_accept_moves_row_to_brief_and_records_accepted_bulk():
    up = _update([{"id": "F3", "action": "accept", "reason": "shipping as-is", "bulk": True}],
                 case="dispute")
    a_out, b_out, state, report = au.apply(AUTHOR, BRIEF, up, head_sha=SHA, actor="cam", auto=False)
    assert "F3" not in _open_author_ids(a_out)
    assert "**F3**" in b_out and "✋ **Accepted as-is by cam on " in b_out and "shipping as-is" in b_out
    d = state["findings"]["F3"]
    assert d["disposition"] == "accepted" and d["bulk"] is True and d["note"] == "shipping as-is"
    assert report["blocking"] == 2
    ev = au.assemble_evidence(None, a_out, b_out, state, up, repo="pulumi/docs", pr=999,
                              head_sha=SHA, run_id="t", timestamp=report["timestamp"])
    f3 = next(f for f in ev["findings"] if f["id"] == "F3")
    assert f3["status"] == "accepted-as-is" and f3["bucket"] == "reviewer-check"
    assert au.validate_evidence_mod.validate_evidence(ev) == []


def test_header_excludes_rows_dispositioned_by_resolve_lane():
    from datetime import datetime, timezone
    live = au.review_state.set_disposition(
        au.review_state.parse_state(AUTHOR), "F2", "accepted", actor="alice", note="ok",
        now=datetime(2026, 9, 1, 20, 0, tzinfo=timezone.utc))
    author_live = au.review_state.replace_block(AUTHOR, live)
    up = _update([{"id": "F1", "action": "retext", "text": "*\"q\"* — still open"}])
    a_out, b_out, _, report = au.apply(author_live, BRIEF, up, head_sha=SHA, actor="cam", auto=False)
    assert "— 2 items block merge" in a_out and report["blocking"] == 2
    assert "✋ accepted as-is by the author" in b_out


def test_refresh_facts_line_recounts_from_findings():
    brief = ("x\n- **Facts:** 3 factual claims checked — 1 verified clean, "
             "2 open on the author's card (\"Waiting on the author\" above).\ny\n")
    findings = [
        {"id": "F1", "bucket": "outstanding", "status": "open", "origin": "verdict:contradicted", "text": "*\"a\"* — bad"},
        {"id": "F2", "bucket": "outstanding", "status": "conceded", "origin": "model", "text": "*\"b\"* — concede: fine"},
    ]
    out = au.refresh_facts_line(brief, findings)
    assert ("- **Facts:** 3 factual claims checked — 1 verified clean, "
            "1 open on the author's card (\"Waiting on the author\" above), "
            "1 settled — see the evidence page.") in out
    findings[0]["bucket"] = "reviewer-check"
    out = au.refresh_facts_line(brief, findings)
    assert "1 flagged in the ⚠️ list, 1 settled — see the evidence page." in out
    assert au.refresh_facts_line("no facts line", findings) == "no facts line"


def test_envelope_slips_are_normalized():
    # The exact shape the model wrote on fork PR 242 (2026-09-01): correct
    # adjudication, wrong envelope.
    slipped = {"history_summary": "F1 verified fixed.",
               "actions": [{"action": "resolve", "id": "F1", "annotation": "fixed in b42ef052"}]}
    a_out, _, state, report = au.apply(AUTHOR, BRIEF, slipped, head_sha=SHA, actor="cam", auto=False)
    assert state["findings"]["F1"]["disposition"] == "fixed" and report["blocking"] == 2
    norm, notes = au.normalize_update(slipped)
    assert norm["schema"] == 1 and norm["case"] == "fix-response" and "findings" in norm
    assert len(notes) == 3
    norm2, _ = au.normalize_update({"findings": [{"action": "hold", "id": "F1", "reason": "r"}]})
    assert norm2["case"] == "dispute"
    # a genuinely broken patch still fails
    try:
        au.apply(AUTHOR, BRIEF, {"findings": "nope"}, head_sha=SHA, actor="cam", auto=False)
    except au.UpdateError:
        pass
    else:
        raise AssertionError("non-list findings accepted")


def test_browser_hint_follows_author_rows():
    up_all = _update([{"id": f, "action": "resolve", "annotation": "fixed in a1a1a1"} for f in ("F1", "F2", "F3")])
    a_out, _, _, _ = au.apply(AUTHOR, BRIEF, up_all, head_sha=SHA, actor="cam", auto=False,
                              head_repo="example/docs-fork", head_branch="fix/component-doc")
    assert au.cr.V3_BROWSER_HINT_PREFIX not in a_out, "no rows left → no hint"
    up_one = _update([{"id": "F1", "action": "resolve", "annotation": "fixed in a1a1a1"}])
    a_out, _, _, _ = au.apply(AUTHOR, BRIEF, up_one, head_sha=SHA, actor="cam", auto=False,
                              head_repo="example/docs-fork", head_branch="fix/component-doc")
    assert a_out.count(au.cr.V3_BROWSER_HINT_PREFIX) == 1
    assert a_out.index(au.cr.V3_BROWSER_HINT_PREFIX) < a_out.index("📎 **Full evidence:**")


def test_add_ref_collapses_single_line_and_evidence_url_rewrites():
    up = _update([{"action": "add", "bucket": "reviewer-check", "file": "content/docs/iac/x.md",
                   "lines": [1158, 1158], "text": "same line twice", "origin": "model"}])
    _, b_out, _, _ = au.apply(AUTHOR, BRIEF, up, head_sha=SHA, actor="cam", auto=False,
                              repo="pulumi/docs", pr=999)
    assert "` L1158](" in b_out and "L1158-1158" not in b_out
    body = "x\n📎 **Full evidence:** [verification trail](https://old.example/1).\n"
    assert "(https://new.example/2)" in au.set_evidence_url(body, "https://new.example/2")
    assert au.set_evidence_url(body, "") == body
    tok = "📎 **Full evidence:** %%EVIDENCE_URL%%\n"
    assert au.set_evidence_url(tok, "https://n/3") == "📎 **Full evidence:** https://n/3\n"


def test_refresh_strips_the_auto_refresh_banner():
    banner = "> 🔄 **Re-review in progress** for your push `abc1234` — this card is out of date until it refreshes.\n\n"
    marker = "<!-- CLAUDE_REVIEW_HEAD "
    at = AUTHOR.index(marker)
    at = AUTHOR.index("\n", at) + 1
    stamped = AUTHOR[:at] + banner + AUTHOR[at:]
    up = _update([{"id": "F1", "action": "resolve", "annotation": "fixed in a1a1a1"}])
    a_out, _, _, _ = au.apply(stamped, BRIEF, up, head_sha=SHA, actor="auto-refresh", auto=True)
    assert "Re-review in progress" not in a_out
    assert "## Author action guide v2" in a_out


def test_no_script_uses_per_commit_pr_patch():
    # `gh pr diff --patch` is a per-commit mailbox: lines an early commit added
    # and a later one removed still get extracted (stale F-rows on fork PR 242).
    import re as _re
    bad = _re.compile(r'\["gh",\s*"pr",\s*"diff",\s*[^\]]*"--patch"')
    offenders = [p.name for p in HERE.glob("*.py") if p.name != Path(__file__).name and bad.search(p.read_text())]
    assert offenders == [], offenders
