"""normalize-v3-draft.py — the deterministic repair pass that runs before
`validate-pinned.py check` on the two v3 cards.

Fixtures are the real model output that errored on the first repo-wide
weekend (2026-09-11 → 09-14): PR 21603 (❓ row kept, its detail block
deleted) and PR 21585 (a four-column table hand-built in an empty brief
section), plus PR 21748 (2026-09-19: the one ⚠️ row never closed). Each
test asserts three things: the validator refuses the draft as shipped,
accepts it after normalization, and a second normalization is a no-op.
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
NORMALIZER = HERE / "normalize-v3-draft.py"
VALIDATOR = HERE / "validate-pinned.py"


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules.setdefault(name, mod)
    spec.loader.exec_module(mod)
    return mod


nv = _load("test_nv_normalize", NORMALIZER)


def _fixture(tmp_path: Path, pr: str) -> tuple[Path, Path, Path]:
    author = tmp_path / ".review-draft-author.md"
    brief = tmp_path / ".review-draft-brief.md"
    base = tmp_path / ".review-evidence-base.json"
    author.write_text((TESTDATA / f"normalize-pr{pr}-author.md.txt").read_text())
    brief.write_text((TESTDATA / f"normalize-pr{pr}-brief.md.txt").read_text())
    base.write_text((TESTDATA / f"normalize-pr{pr}-evidence-base.json").read_text())
    return author, brief, base


def _validate(author: Path, brief: Path, base: Path) -> tuple[int, str]:
    r = subprocess.run(
        [sys.executable, str(VALIDATOR), "check", "--body-file", str(author),
         "--brief-file", str(brief), "--evidence-base", str(base)],
        capture_output=True, text=True, env={"PATH": "/usr/bin:/bin", "HOME": str(author.parent)},
    )
    return r.returncode, r.stdout + r.stderr


def _normalize(author: Path, brief: Path, base: Path, summary: Path | None = None) -> tuple[int, str]:
    cmd = [sys.executable, str(NORMALIZER), "--author-file", str(author),
           "--brief-file", str(brief), "--evidence-base", str(base)]
    if summary:
        cmd += ["--summary", str(summary)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


@pytest.mark.parametrize("pr, rule", [("21603", "v3-detail-blocks"),
                                     ("21585", "v3-finding-grammar"),
                                     ("21748", "v3-finding-grammar")])
def test_fixture_refused_then_accepted_then_idempotent(tmp_path, pr, rule):
    author, brief, base = _fixture(tmp_path, pr)
    rc, out = _validate(author, brief, base)
    assert rc == 1 and rule in out, out

    summary = tmp_path / "summary.json"
    rc, out = _normalize(author, brief, base, summary)
    assert rc == 0
    assert "::warning::normalize-v3-draft:" in out
    repairs = json.loads(summary.read_text())["repairs"]
    assert repairs, out

    rc, out = _validate(author, brief, base)
    assert rc == 0, out

    before = (author.read_text(), brief.read_text())
    rc, out = _normalize(author, brief, base)
    assert rc == 0 and "0 repair(s)" in out
    assert (author.read_text(), brief.read_text()) == before


def test_21603_block_regenerated_from_row(tmp_path):
    author, brief, base = _fixture(tmp_path, "21603")
    _normalize(author, brief, base)
    text = author.read_text()
    block = text.split("#### F1 · Do this", 1)[1].split("\n\n_Editing", 1)[0]
    assert "- **Line (verbatim):** You can configure a custom domain name" in block
    assert "- **Why:** verdict: unverifiable" in block
    assert block.count("- **Fix:**") == 1
    assert "<TODO" not in text
    # The block sits between the ❓ table and the browser hint, where the
    # composer puts it.
    assert text.index("| **F1** |") < text.index("#### F1 · Do this") < text.index("_Editing in the browser?")


def test_21748_long_finding_row_closed_in_place(tmp_path):
    author, brief, base = _fixture(tmp_path, "21748")
    _normalize(author, brief, base)
    lines = brief.read_text().splitlines()
    row = next(l for l in lines if l.startswith("| **F?** |"))
    assert row.endswith("whether the strip still exists. |")
    # Closed, not rewritten: the Finding cell reaches build-evidence intact.
    assert "Three comments the PR leaves behind" in row
    assert nv.cr.parse_finding_line(row) is not None


def test_21585_header_and_separator_rewritten(tmp_path):
    author, brief, base = _fixture(tmp_path, "21585")
    _normalize(author, brief, base)
    lines = brief.read_text().splitlines()
    i = lines.index("### ⚠️ Check these before approving")
    assert lines[i + 2] == "| ID | Where | Finding |"
    assert lines[i + 3] == "|---|---|---|"
    assert lines[i + 4].startswith("| **F?** | `content/docs/reference/cloud-rest-api")


# ---------------------------------------------------------- unit rules ----

def _author_card(rows_outstanding: list[str], rows_questions: list[str],
                 blocks: list[str]) -> str:
    def table(rows):
        if not rows:
            return "_Nothing to fix — this section is empty._"
        return "\n".join(["| ID | Where | Finding |", "|---|---|---|", *rows])
    return "\n".join([
        "<!-- CLAUDE_REVIEW 1/1 -->",
        "<!-- CLAUDE_REVIEW_AUTHOR -->",
        "## Author action guide v1 — 2 items block merge",
        "",
        "### 🚨 Fix or disagree",
        "",
        table(rows_outstanding),
        "",
        "### ❓ Questions for you",
        "",
        table(rows_questions),
        "",
        *blocks,
        "",
        "📎 **Full evidence:** [x](%%EVIDENCE_URL%%).",
        "",
        '<!-- REVIEW_STATE {"findings":{},"high_water":3,"schema":1} -->',
        "",
    ])


def test_leading_status_cell_dropped_only_when_row_parses():
    rep = nv.Repairs()
    lines = ["### 🚨 Fix or disagree", "",
             "| ID | Where | Finding |", "|---|---|---|",
             "| ⬜ | **F1** | `a.md` L3 | bad |",
             "| | **F?** | `b.md` L4 | new |",
             "| **F2** | `c.md` L5 | fine |",
             "| ⬜ | **F3** | too | many | cells |",
             "", "### ❓ Questions for you", ""]
    out = nv._normalize_tables(lines, nv.AUTHOR_SECTIONS, "author", rep)
    assert out[4] == "| **F1** | `a.md` L3 | bad |"
    assert out[5] == "| **F?** | `b.md` L4 | new |"
    assert out[6] == "| **F2** | `c.md` L5 | fine |"      # untouched
    assert out[7] == lines[7]                              # five cells: left alone
    assert [r["rule"] for r in rep.items] == ["row-leading-cell", "row-leading-cell"]


def test_header_variants_normalized_and_canonical_untouched():
    rep = nv.Repairs()
    lines = ["### ⚠️ Check these before approving", "",
             "|  | id | WHERE | Finding |", "| --- | --- | --- | --- |",
             "| **F?** | `a.md` L1 | x |", ""]
    out = nv._normalize_tables(lines, nv.BRIEF_SECTIONS, "brief", rep)
    assert out[2] == "| ID | Where | Finding |" and out[3] == "|---|---|---|"
    rep2 = nv.Repairs()
    again = nv._normalize_tables(out, nv.BRIEF_SECTIONS, "brief", rep2)
    assert again == out and rep2.items == []


def test_prose_bullet_in_brief_left_alone():
    rep = nv.Repairs()
    lines = ["### ⚠️ Check these before approving", "",
             "- **One editorial call:** keep the hedge.", ""]
    assert nv._normalize_tables(lines, nv.BRIEF_SECTIONS, "brief", rep) == lines
    assert rep.items == []


def test_missing_block_inserted_in_row_order():
    rows = ["| **F1** | `a.md` L1 | *\"first line\"* — wrong |",
            "| **F2** | `a.md` L2 | second |",
            "| **F3** | `a.md` L3 | third |"]
    blocks = ["#### F1 · Do this", "", "- **Line (verbatim):** first line",
              "- **Why:** w", "- **Fix:** f", "",
              "#### F3 · Do this", "", "- **Line (verbatim):** third line",
              "- **Why:** w", "- **Fix:** f"]
    # Rows and their blocks share a section (composer layout): ❓ here.
    card = _author_card([], rows, blocks)
    rep = nv.Repairs()
    out = nv._restore_blocks(card.splitlines(), {"F2": {"text": "second line"}}, rep)
    text = "\n".join(out)
    assert [r["where"] for r in rep.items] == ["F2"]
    i1, i2, i3 = (text.index(f"#### F{n} · Do this") for n in (1, 2, 3))
    assert i1 < i2 < i3
    assert "- **Line (verbatim):** second line" in text
    assert "- **Fix:** Reply with the source" in text
    assert text.count("- **Fix:**") == 3


def test_rewritten_and_fquestion_rows_get_no_block():
    rows = ["| **F1** | `a.md` L1 | **Spurious:** not a claim |",
            "| **F?** | `a.md` L2 | new one |"]
    card = _author_card(rows, [], [])
    rep = nv.Repairs()
    out = nv._restore_blocks(card.splitlines(), {}, rep)
    assert rep.items == [] and "\n".join(out) == card.rstrip("\n")


def test_block_after_table_when_section_has_none():
    rows = ["| **F2** | `a.md` L2 | *\"quoted\"* — needs a source |"]
    card = _author_card([], rows, [])
    rep = nv.Repairs()
    out = nv._restore_blocks(card.splitlines(), {}, rep)
    text = "\n".join(out)
    assert text.index("| **F2** |") < text.index("#### F2 · Do this") < text.index("📎 **Full evidence")
    assert "- **Fix:** Reply with the source" in text


def test_script_exits_zero_on_unreadable_input(tmp_path):
    r = subprocess.run([sys.executable, str(NORMALIZER), "--author-file", str(tmp_path / "missing.md"),
                        "--summary", str(tmp_path / "s.json")], capture_output=True, text=True)
    assert r.returncode == 0
    assert "::warning::normalize-v3-draft: skipped" in r.stdout
    assert json.loads((tmp_path / "s.json").read_text())["repairs"][0]["rule"] == "error"


def test_unclosed_rows_closed_only_when_the_result_parses():
    rep = nv.Repairs()
    lines = ["### ⚠️ Check these before approving", "",
             "| ID | Where | Finding",
             "|---|---|---",
             "| **F1** | `a.md` L3 | ran off the end",
             "| ⬜ | **F2** | `b.md` L4 | glyph cell and no close",
             "| **F3** | `c.md` L5 | already closed |",
             "| not a finding row at all",
             ""]
    out = nv._normalize_tables(lines, nv.BRIEF_SECTIONS, "brief", rep)
    assert out[2] == "| ID | Where | Finding |"
    assert out[3] == "|---|---|---|"
    assert out[4] == "| **F1** | `a.md` L3 | ran off the end |"
    assert out[5] == "| **F2** | `b.md` L4 | glyph cell and no close |"
    assert out[6] == lines[6]                                  # untouched
    assert out[7] == lines[7]                                  # not closeable
    assert [r["rule"] for r in rep.items] == [
        "row-unclosed", "row-unclosed", "row-unclosed", "row-unclosed", "row-leading-cell"]
    rep2 = nv.Repairs()
    assert nv._normalize_tables(out, nv.BRIEF_SECTIONS, "brief", rep2) == out
    assert rep2.items == []


def test_close_row_refuses_what_it_cannot_prove():
    assert nv._close_row("| **F1** | `a.md` L3 | fine |") is None      # already closed
    assert nv._close_row("- **One editorial call:** keep it") is None  # not a row
    assert nv._close_row("| two | cells") is None                      # wouldn't parse
    assert nv._close_row("| a | b | c | d | e") is None                # too many cells
    assert nv._close_row("|") is None
    # A cell ending in an escaped pipe is unclosed, not closed.
    assert nv._close_row(r"| **F1** | `a.md` L3 | a \| b") == r"| **F1** | `a.md` L3 | a \| b |"
