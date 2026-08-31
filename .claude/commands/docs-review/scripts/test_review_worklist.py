#!/usr/bin/env python3
"""Unit tests for review-worklist.py.

Self-contained — run with `python3 test_review_worklist.py` (no pytest dep),
also pytest-collectible. Imports the module directly and exercises the v3
extraction/seeding/build_report paths against the checked-in fixtures
(testdata/v3-fixture-author.md, testdata/v3-fixture-brief.md). The v2 path is
covered by the module's own --self-test (review-worklist.py's self_test());
this file focuses on the v3 surface per the migration task.
"""

from __future__ import annotations

import importlib.util
import sys
import traceback
from pathlib import Path

HERE = Path(__file__).resolve().parent
TESTDATA = HERE / "testdata"

_spec = importlib.util.spec_from_file_location("review_worklist", HERE / "review-worklist.py")
rw = importlib.util.module_from_spec(_spec)
sys.modules["review_worklist"] = rw
_spec.loader.exec_module(rw)  # type: ignore[union-attr]

AUTHOR_FIXTURE = (TESTDATA / "v3-fixture-author.md").read_text(encoding="utf-8")
BRIEF_FIXTURE = (TESTDATA / "v3-fixture-brief.md").read_text(encoding="utf-8")


def answered_author_body(dispositions: dict[str, tuple[str, str]]) -> str:
    """Return AUTHOR_FIXTURE with a REVIEW_STATE block carrying `dispositions`.

    `dispositions` maps finding id -> (disposition, note).
    """
    state = rw._rs.empty_state()
    for fid, (disp, note) in dispositions.items():
        state = rw._rs.set_disposition(state, fid, disp, actor="cam", note=note)
    return rw._rs.replace_block(AUTHOR_FIXTURE, state)


# ---- extraction ----------------------------------------------------------


def test_v3_marker_detected():
    assert rw._cr.AUTHOR_MARKER in AUTHOR_FIXTURE


def test_extract_items_v3_ids_and_buckets():
    items = rw.extract_items_v3(AUTHOR_FIXTURE, BRIEF_FIXTURE)
    by_id = {it["id"]: it for it in items if it["id"].startswith("F")}
    assert set(by_id) == {"F1", "F2", "F3", "F4"}
    assert by_id["F1"]["bucket"] == "outstanding" and by_id["F1"]["blocking"] is True
    assert by_id["F2"]["bucket"] == "outstanding" and by_id["F2"]["blocking"] is True
    assert by_id["F3"]["bucket"] == "author-answer" and by_id["F3"]["blocking"] is True
    assert by_id["F4"]["bucket"] == "reviewer-check" and by_id["F4"]["blocking"] is False


def test_extract_items_v3_style_block_not_f_tagged():
    items = rw.extract_items_v3(AUTHOR_FIXTURE, BRIEF_FIXTURE)
    style_items = [it for it in items if it["bucket"] == "style"]
    assert len(style_items) == 1
    assert style_items[0]["id"] == "style:content/docs/iac/x.md:L33"
    assert style_items[0]["blocking"] is False
    assert style_items[0]["optional"] is False


def test_extract_items_v3_file_and_anchor_captured():
    items = rw.extract_items_v3(AUTHOR_FIXTURE, BRIEF_FIXTURE)
    f1 = next(it for it in items if it["id"] == "F1")
    assert f1["file"] == "content/docs/iac/x.md"
    assert f1["anchor"] == "L80-82"


def test_extract_items_v3_no_brief_still_gets_author_items():
    items = rw.extract_items_v3(AUTHOR_FIXTURE, "")
    ids = {it["id"] for it in items}
    assert {"F1", "F2", "F3"} <= ids
    assert "F4" not in ids  # F4 only lives on the brief


# ---- REVIEW_STATE seeding --------------------------------------------------


def test_seed_from_review_state_populates_f_ids_only():
    items = rw.extract_items_v3(AUTHOR_FIXTURE, BRIEF_FIXTURE)
    state = rw._rs.set_disposition(rw._rs.empty_state(), "F1", "fixed", actor="cam")
    rw.seed_from_review_state(items, state)
    f1 = next(it for it in items if it["id"] == "F1")
    style = next(it for it in items if it["bucket"] == "style")
    assert f1["disposition"] == "fixed"
    assert "disposition" not in style  # untouched -- no F-id to match


# ---- build_report: clean / undecided / REVIEW_STATE-answered --------------


def test_build_report_v3_undecided_is_not_clean():
    report = rw.build_report(AUTHOR_FIXTURE, [], {}, 999, rw.DEFAULT_REPO, brief_body=BRIEF_FIXTURE)
    assert report["surface"] == "v3"
    assert report["summary"]["clean"] is False
    assert report["summary"]["resolved"] == 0
    assert report["parse_confidence"] == "high"
    assert report["reviewed_sha"] == "aaaabbbbccccddddeeeeffff0000111122223333"


def test_build_report_v3_review_state_answered_still_needs_style():
    body = answered_author_body({
        "F1": ("fixed", ""),
        "F2": ("fixed", ""),
        "F3": ("refuted", "verified against 3.261 changelog"),
        "F4": ("accepted", "framing looks fine in context"),
    })
    report = rw.build_report(body, [], {}, 999, rw.DEFAULT_REPO, brief_body=BRIEF_FIXTURE)
    dispositions = {it["id"]: it["disposition"] for it in report["items"] if it["id"].startswith("F")}
    assert dispositions == {"F1": "fixed", "F2": "fixed", "F3": "refuted", "F4": "accepted"}
    assert report["summary"]["clean"] is False
    remaining = report["summary"]["remaining_ids"]
    assert remaining == ["style:content/docs/iac/x.md:L33"]


def test_build_report_v3_clean_once_style_dispositioned():
    body = answered_author_body({
        "F1": ("fixed", ""),
        "F2": ("fixed", ""),
        "F3": ("refuted", "verified against 3.261 changelog"),
        "F4": ("accepted", "framing looks fine in context"),
    })
    state = {"style:content/docs/iac/x.md:L33": {"disposition": "accepted", "note": "term of art"}}
    report = rw.build_report(body, [], state, 999, rw.DEFAULT_REPO, brief_body=BRIEF_FIXTURE)
    assert report["summary"]["clean"] is True


def test_build_report_v3_state_file_overrides_review_state_seed():
    body = answered_author_body({"F1": ("fixed", "")})
    override = {"F1": {"disposition": "accepted", "note": "shipping as-is"}}
    report = rw.build_report(body, [], override, 999, rw.DEFAULT_REPO, brief_body=BRIEF_FIXTURE)
    f1 = next(it for it in report["items"] if it["id"] == "F1")
    assert f1["disposition"] == "accepted"
    assert f1["note"] == "shipping as-is"


def test_build_report_v3_note_required_disposition_without_note_is_a_problem():
    # accepted/deferred/not-applicable need a note; review_state.set_disposition
    # itself refuses to write one without a note, so drive this through --state.
    state = {"F4": {"disposition": "accepted", "note": ""}}
    report = rw.build_report(AUTHOR_FIXTURE, [], state, 999, rw.DEFAULT_REPO, brief_body=BRIEF_FIXTURE)
    f4 = next(it for it in report["items"] if it["id"] == "F4")
    assert f4.get("problem") is not None
    assert "F4" in report["summary"]["remaining_ids"]


def test_build_report_v3_corrupt_review_state_degrades_to_low():
    corrupt = AUTHOR_FIXTURE.replace(
        '<!-- REVIEW_STATE {"findings":{},"high_water":4,"schema":1} -->',
        '<!-- REVIEW_STATE {broken -->',
    )
    report = rw.build_report(corrupt, [], {}, 999, rw.DEFAULT_REPO, brief_body=BRIEF_FIXTURE)
    assert report["parse_confidence"] == "low"
    assert report["summary"]["clean"] is False


def test_build_report_v3_missing_head_sentinel_degrades_to_low():
    no_head = AUTHOR_FIXTURE.replace(
        "<!-- CLAUDE_REVIEW_HEAD aaaabbbbccccddddeeeeffff0000111122223333 -->", ""
    )
    report = rw.build_report(no_head, [], {}, 999, rw.DEFAULT_REPO, brief_body=BRIEF_FIXTURE)
    assert report["parse_confidence"] == "low"


def test_build_report_v2_path_unaffected_by_v3_wiring():
    # Regression pin: a v2 body (no AUTHOR_MARKER) must still route through
    # the original extract_items path and report surface "v2".
    body = rw.join_pages(rw._FIXTURE)
    report = rw.build_report(body, [], {}, 20123, rw.DEFAULT_REPO)
    assert report["surface"] == "v2"
    assert report["counts_table"] is not None


def test_render_markdown_v3_report():
    report = rw.build_report(AUTHOR_FIXTURE, [], {}, 999, rw.DEFAULT_REPO, brief_body=BRIEF_FIXTURE)
    md = rw.render_markdown(report)
    assert "❓ Only you can answer" in md
    assert "👀 Reviewer check" in md


# ---- runner ----------------------------------------------------------------


def main() -> int:
    tests = [(name, fn) for name, fn in sorted(globals().items())
             if name.startswith("test_") and callable(fn)]
    failures = 0
    for name, fn in tests:
        try:
            fn()
            print(f"  ok  {name}")
        except Exception:
            failures += 1
            print(f"  FAIL {name}")
            traceback.print_exc()
    print(f"{len(tests) - failures}/{len(tests)} passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
