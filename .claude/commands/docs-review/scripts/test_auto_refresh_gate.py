#!/usr/bin/env python3
"""Unit tests for auto-refresh-gate.py.

Self-contained — run with `python3 test_auto_refresh_gate.py` (no pytest dep).
Imports the gate module directly and exercises the pure functions plus the
CLI entry point end-to-end via temp files, mirroring test_splicer.py.
"""

from __future__ import annotations

import importlib.util
import io
import json
import sys
import tempfile
import traceback
from contextlib import redirect_stdout
from pathlib import Path

HERE = Path(__file__).resolve().parent
GATE_PATH = HERE / "auto-refresh-gate.py"

_spec = importlib.util.spec_from_file_location("auto_refresh_gate", GATE_PATH)
gate = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gate)  # type: ignore[union-attr]


# ---- Fixtures ----------------------------------------------------------------


def pinned_body(*outstanding_bullets: str) -> str:
    bullets = "\n".join(outstanding_bullets)
    return (
        "<!-- CLAUDE_REVIEW 1/1 -->\n"
        "## Docs review\n\n"
        "### 🔍 Verification trail\n\n"
        "- L42 \"claim\" → 🚨 contradicted evidence\n\n"
        "### 🚨 Outstanding in this PR\n\n"
        f"{bullets}\n\n"
        "### ⚠️ Low-confidence\n\n"
        "- **[L200]** something dubious\n\n"
        "### 📜 Review history\n\n"
        "- 2026-07-01T00:00:00Z — initial review (abc1234)\n"
    )


def make_diff(path: str, old_start: int, old_count: int, *,
              added: int = 1, removed: int = 1, new_file: bool = False,
              deleted: bool = False, rename: bool = False) -> str:
    """Build a minimal single-hunk unified diff."""
    old_path = "/dev/null" if new_file else f"a/{path}"
    new_path = "/dev/null" if deleted else f"b/{path}"
    lines = [f"diff --git a/{path} b/{path}"]
    if rename:
        lines += [f"rename from {path}", f"rename to {path}.moved"]
    lines += [
        f"--- {old_path}",
        f"+++ {new_path}",
        f"@@ -{old_start},{old_count} +{old_start},{old_count - removed + added} @@",
    ]
    lines += [f"-old line {i}" for i in range(removed)]
    lines += [f"+new line {i}" for i in range(added)]
    return "\n".join(lines) + "\n"


def run_gate(body: str, diff: str, pr_files: list[str]) -> tuple[int, dict]:
    """Invoke gate.main() through the CLI surface with temp files."""
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        (tdp / "body.md").write_text(body, encoding="utf-8")
        (tdp / "push.diff").write_text(diff, encoding="utf-8")
        (tdp / "files.json").write_text(json.dumps(pr_files), encoding="utf-8")
        argv = sys.argv
        sys.argv = ["auto-refresh-gate.py",
                    "--pinned-body", str(tdp / "body.md"),
                    "--push-diff", str(tdp / "push.diff"),
                    "--pr-files", str(tdp / "files.json")]
        out = io.StringIO()
        try:
            with redirect_stdout(out):
                rc = gate.main()
        finally:
            sys.argv = argv
    payload = json.loads(out.getvalue()) if out.getvalue().strip() else {}
    return rc, payload


FILE = "content/docs/iac/concepts/stacks.md"


def v3_pinned_body(outstanding: str = "", author_answer: str = "") -> str:
    """A minimal v3 author card, marker + findings only (no REVIEW_STATE/footer
    needed — the gate only reads AUTHOR_MARKER and the two finding sections).
    """
    return (
        "<!-- CLAUDE_REVIEW 1/1 -->\n"
        "<!-- CLAUDE_REVIEW_AUTHOR -->\n"
        "<!-- CLAUDE_REVIEW_HEAD aaaabbbbccccddddeeeeffff0000111122223333 -->\n"
        "## Review — action needed\n\n"
        "### 🚨 Must fix or refute (blocks merge)\n\n"
        f"{outstanding}\n\n"
        "### ❓ Only you can answer these (blocks merge)\n\n"
        f"{author_answer}\n\n"
    )


# ---- Tests -------------------------------------------------------------------


def test_exact_overlap_fires():
    body = pinned_body("- **[L40-50]** wrong default value")
    rc, res = run_gate(body, make_diff(FILE, 42, 3), [FILE])
    assert rc == 0 and res["fire"] is True, res


def test_single_line_anchor_fires():
    body = pinned_body("- **[L42]** wrong default value")
    rc, res = run_gate(body, make_diff(FILE, 42, 1), [FILE])
    assert rc == 0 and res["fire"] is True, res


def test_slack_boundary():
    body = pinned_body("- **[L40-50]** wrong default value")
    # Hunk ends exactly SLACK_LINES above the anchor start: 37 >= 40 - 3.
    rc, res = run_gate(body, make_diff(FILE, 37, 1), [FILE])
    assert res["fire"] is True, res
    # One line further out: 36 < 40 - 3 → no fire.
    rc, res = run_gate(body, make_diff(FILE, 36, 1), [FILE])
    assert res["fire"] is False, res


def test_out_of_range_hunk_fails():
    body = pinned_body("- **[L40-50]** wrong default value")
    rc, res = run_gate(body, make_diff(FILE, 300, 2), [FILE])
    assert rc == 0 and res["fire"] is False, res
    assert "outside outstanding finding lines" in res["reason"], res


def test_pure_insertion_adjacent_to_anchor_fires():
    body = pinned_body("- **[L40-50]** missing caveat")
    diff = (
        f"diff --git a/{FILE} b/{FILE}\n"
        f"--- a/{FILE}\n"
        f"+++ b/{FILE}\n"
        "@@ -50,0 +51,2 @@\n"
        "+a new caveat line\n"
        "+another line\n"
    )
    rc, res = run_gate(body, diff, [FILE])
    assert rc == 0 and res["fire"] is True, res


def test_file_outside_pr_fails():
    body = pinned_body("- **[L40-50]** wrong default value")
    rc, res = run_gate(body, make_diff(FILE, 42, 3), ["content/docs/other.md"])
    assert res["fire"] is False and "outside the PR's reviewed files" in res["reason"], res


def test_new_file_fails():
    body = pinned_body("- **[L40-50]** wrong default value")
    rc, res = run_gate(body, make_diff(FILE, 42, 3, new_file=True), [FILE])
    assert res["fire"] is False and res["reason"] == "push adds a new file", res


def test_deleted_file_fails():
    body = pinned_body("- **[L40-50]** wrong default value")
    rc, res = run_gate(body, make_diff(FILE, 42, 3, deleted=True), [FILE])
    assert res["fire"] is False and res["reason"] == "push deletes a file", res


def test_renamed_file_fails():
    body = pinned_body("- **[L40-50]** wrong default value")
    rc, res = run_gate(body, make_diff(FILE, 42, 3, rename=True), [FILE])
    assert res["fire"] is False and res["reason"] == "push renames a file", res


def test_size_cap_fails():
    body = pinned_body("- **[L1-500]** sprawling finding")
    over = gate.MAX_CHANGED_LINES + 1
    rc, res = run_gate(body, make_diff(FILE, 10, over, added=over, removed=over), [FILE])
    assert res["fire"] is False and "too large" in res["reason"], res


def test_empty_diff_fails():
    body = pinned_body("- **[L40-50]** wrong default value")
    rc, res = run_gate(body, "", [FILE])
    assert rc == 0 and res["fire"] is False and res["reason"] == "empty push diff", res


def test_empty_pinned_body_fails():
    rc, res = run_gate("", make_diff(FILE, 42, 3), [FILE])
    assert rc == 0 and res["fire"] is False and res["reason"] == "no pinned review found", res


def test_no_outstanding_bucket_fails():
    body = pinned_body().replace("### 🚨 Outstanding in this PR\n\n\n\n", "")
    rc, res = run_gate(body, make_diff(FILE, 42, 3), [FILE])
    assert res["fire"] is False and "no outstanding findings" in res["reason"], res


def test_unparsable_anchor_fails_closed():
    # Legacy bullet format without the canonical [L...] prefix.
    body = pinned_body("- **content/docs/foo.md L40-50** wrong default value")
    rc, res = run_gate(body, make_diff(FILE, 42, 3), [FILE])
    assert res["fire"] is False and "no parseable" in res["reason"], res


def test_multi_page_outstanding_union():
    page1 = pinned_body("- **[L40-50]** first finding")
    page2 = (
        "<!-- CLAUDE_REVIEW 2/2 -->\n"
        "### 🚨 Outstanding in this PR\n\n"
        "- **[L300-310]** overflow-page finding\n"
    )
    body = page1 + "\n----- PINNED-COMMENT-DELIMITER -----\n" + page2
    rc, res = run_gate(body, make_diff(FILE, 305, 2), [FILE])
    assert rc == 0 and res["fire"] is True, res


def test_multi_hunk_one_outside_fails():
    body = pinned_body("- **[L40-50]** wrong default value")
    diff = make_diff(FILE, 42, 3) + make_diff(FILE, 400, 2)
    rc, res = run_gate(body, diff, [FILE])
    assert res["fire"] is False and "outside outstanding finding lines" in res["reason"], res


def test_binary_file_fails():
    body = pinned_body("- **[L40-50]** wrong default value")
    diff = (
        "diff --git a/static/images/x.png b/static/images/x.png\n"
        "Binary files a/static/images/x.png and b/static/images/x.png differ\n"
    )
    rc, res = run_gate(body, diff, ["static/images/x.png"])
    assert res["fire"] is False and "binary" in res["reason"], res


def test_missing_input_file_exits_2():
    argv = sys.argv
    sys.argv = ["auto-refresh-gate.py",
                "--pinned-body", "/nonexistent/body.md",
                "--push-diff", "/nonexistent/push.diff",
                "--pr-files", "/nonexistent/files.json"]
    try:
        rc = gate.main()
    finally:
        sys.argv = argv
    assert rc == 2, rc


def test_malformed_pr_files_exits_2():
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        (tdp / "body.md").write_text(pinned_body("- **[L40-50]** x"), encoding="utf-8")
        (tdp / "push.diff").write_text(make_diff(FILE, 42, 3), encoding="utf-8")
        (tdp / "files.json").write_text('{"not": "a list"}', encoding="utf-8")
        argv = sys.argv
        sys.argv = ["auto-refresh-gate.py",
                    "--pinned-body", str(tdp / "body.md"),
                    "--push-diff", str(tdp / "push.diff"),
                    "--pr-files", str(tdp / "files.json")]
        try:
            rc = gate.main()
        finally:
            sys.argv = argv
    assert rc == 2, rc


# ---- v3 surface ----------------------------------------------------------


def test_v3_outstanding_fires():
    body = v3_pinned_body(outstanding="| **F1** | `content/docs/iac/x.md` L40-50 | wrong default |")
    rc, res = run_gate(body, make_diff(FILE, 42, 3), [FILE])
    assert rc == 0 and res["fire"] is True, res


def test_v3_author_answer_section_also_fires():
    # The promoted ❓ bucket must not break auto-refresh: a push fixing a ❓
    # item is just as refresh-eligible as one fixing a 🚨 item.
    body = v3_pinned_body(
        author_answer="| **F3** | `content/docs/iac/x.md` L61 | unverifiable claim |"
    )
    rc, res = run_gate(body, make_diff(FILE, 61, 1), [FILE])
    assert rc == 0 and res["fire"] is True, res


def test_v3_both_sections_union():
    body = v3_pinned_body(
        outstanding="| **F1** | `content/docs/iac/x.md` L40-50 | wrong default |",
        author_answer="| **F3** | `content/docs/iac/x.md` L61 | unverifiable claim |",
    )
    rc, res = run_gate(body, make_diff(FILE, 61, 1), [FILE])
    assert rc == 0 and res["fire"] is True, res
    rc, res = run_gate(body, make_diff(FILE, 42, 3), [FILE])
    assert rc == 0 and res["fire"] is True, res


def test_v3_out_of_range_hunk_fails():
    body = v3_pinned_body(outstanding="| **F1** | `content/docs/iac/x.md` L40-50 | wrong default |")
    rc, res = run_gate(body, make_diff(FILE, 300, 2), [FILE])
    assert res["fire"] is False, res
    assert "outside outstanding finding lines" in res["reason"], res


def test_v3_finding_without_anchor_fails_closed():
    # A v3 finding row with no `[L…]` ref (file-less detector finding) can't
    # be located, so the whole gate must fail closed.
    body = v3_pinned_body(outstanding="| **F1** | — | no line anchor on this one |")
    rc, res = run_gate(body, make_diff(FILE, 42, 3), [FILE])
    assert res["fire"] is False and "no parseable" in res["reason"], res


def test_v3_no_findings_at_all_fails():
    body = v3_pinned_body()
    rc, res = run_gate(body, make_diff(FILE, 42, 3), [FILE])
    assert res["fire"] is False and "no outstanding findings" in res["reason"], res


def test_v3_style_bullet_is_not_an_anchor():
    # A style-suggestion bullet (`- **line N:**`, no F-id) inside the same
    # section span must not be mistaken for a finding row.
    body = v3_pinned_body(
        outstanding="| **F1** | `content/docs/iac/x.md` L40-50 | wrong default |\n"
                    "- **line 88:** not a real finding row"
    )
    rc, res = run_gate(body, make_diff(FILE, 42, 3), [FILE])
    assert rc == 0 and res["fire"] is True, res


def test_v3_multi_ref_finding_unions_all_ranges():
    # A collapsed frontmatter-sweep ref carries several comma-separated
    # L-ranges; every one of them must anchor a refresh-eligible hunk.
    body = v3_pinned_body(
        outstanding="| **F1** | `content/docs/iac/x.md` L12, L80-82 | collapsed entry |"
    )
    rc, res = run_gate(body, make_diff(FILE, 81, 1), [FILE])
    assert rc == 0 and res["fire"] is True, res
    rc, res = run_gate(body, make_diff(FILE, 12, 1), [FILE])
    assert rc == 0 and res["fire"] is True, res


# ---- Runner ------------------------------------------------------------------


def main() -> int:
    tests = [(name, fn) for name, fn in sorted(globals().items())
             if name.startswith("test_") and callable(fn)]
    failures = 0
    for name, fn in tests:
        try:
            fn()
            print(f"PASS {name}")
        except Exception:
            failures += 1
            print(f"FAIL {name}")
            traceback.print_exc()
    print(f"\n{len(tests) - failures}/{len(tests)} passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())


def test_v3_linked_where_cell_still_yields_anchors():
    """The composer deep-links the Where cell to the blob at head; the
    L-range text lives inside the link text, and anchor extraction must see
    it identically to the bare form (Josh-round grammar change)."""
    body = (HERE / "testdata" / "v3-fixture-author.md").read_text()
    assert "](https://github.com/pulumi/docs/blob/" in body  # fixture is linked
    ranges = gate.parse_anchor_ranges(body)
    assert (80, 82) in ranges and (61, 61) in ranges
