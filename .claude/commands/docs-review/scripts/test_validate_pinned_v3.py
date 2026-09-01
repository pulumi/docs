#!/usr/bin/env python3
"""Tests for validate-pinned.py's v3 surface (schema v21).

The v3 rule set validates the author card + reviewer brief together, with
the verification trail out of scope (machine-owned in the evidence object,
validated by scripts/review-v3/validate-evidence.py). These tests drive the
committed draft fixtures (testdata/v3-fixture-*) through `run_checks` and
`count-buckets`, then break them one invariant at a time.

Draft fixtures are `<TODO>`-laden by design, so every check here skips
`no-todo-tokens` exactly like compose-review.py's self-check does; the
workflow publish path does not skip it.
"""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    # Register before exec: @dataclass resolves cls.__module__ mid-exec.
    sys.modules.setdefault(name, mod)
    spec.loader.exec_module(mod)
    return mod


vp = _load("validate_pinned_v3_under_test", HERE / "validate-pinned.py")

AUTHOR = (HERE / "testdata" / "v3-fixture-author.md").read_text()
BRIEF = (HERE / "testdata" / "v3-fixture-brief.md").read_text()
BASE = json.loads((HERE / "testdata" / "v3-fixture-evidence-base.json").read_text())

SKIP = {"no-todo-tokens"}


def check(author: str = AUTHOR, brief: str = BRIEF, base: dict | None = BASE) -> list:
    ctx = vp.Context(
        body=author,
        body_lines=author.splitlines(),
        pr=None,
        repo=None,
        diff_files=[],
        diff_files_added=set(),
        diff_text="",
        repo_root=HERE.parents[3],
        is_blog=False,
        surface="v3",
        brief=brief,
        evidence_base=base,
    )
    return vp.run_checks(ctx, skip_rules=SKIP)


def rule_ids(violations: list) -> set[str]:
    return {v.rule_id for v in violations}


def test_fixtures_validate_clean() -> None:
    assert check() == []


def test_surface_autodetect() -> None:
    assert vp.V3_AUTHOR_MARKER in AUTHOR
    golden = (HERE / "testdata" / "pr20079-pinned-review.md").read_text()
    assert vp.V3_AUTHOR_MARKER not in golden  # v2 bodies never trip v3 rules


def test_missing_author_marker() -> None:
    broken = AUTHOR.replace("<!-- CLAUDE_REVIEW_AUTHOR -->\n", "")
    assert "v3-markers" in rule_ids(check(author=broken))


def test_concatenated_markers_rejected() -> None:
    broken = AUTHOR.replace(
        "<!-- CLAUDE_REVIEW 1/1 -->\n<!-- CLAUDE_REVIEW_AUTHOR -->",
        "<!-- CLAUDE_REVIEW 1/1 --><!-- CLAUDE_REVIEW_AUTHOR -->",
    )
    assert "v3-markers" in rule_ids(check(author=broken))


def test_brief_must_not_carry_head_marker() -> None:
    polluted = "<!-- CLAUDE_REVIEW_HEAD aaaabbbbccccddddeeeeffff0000111122223333 -->\n" + BRIEF
    violations = check(brief=polluted)
    assert any(v.rule_id == "v3-markers" and "brief" in v.line_ref for v in violations)


def test_missing_section_and_order() -> None:
    no_q = AUTHOR.replace("### ❓ Questions for you", "### something else")
    assert "v3-section-order" in rule_ids(check(author=no_q))


def test_corrupt_review_state_hard_fails() -> None:
    broken = AUTHOR.replace('<!-- REVIEW_STATE {"findings"', '<!-- REVIEW_STATE {"findings')
    ids = rule_ids(check(author=broken))
    assert "v3-review-state" in ids


def test_missing_review_state() -> None:
    stripped = "\n".join(
        line for line in AUTHOR.splitlines() if "REVIEW_STATE" not in line
    )
    assert "v3-review-state" in rule_ids(check(author=stripped))


def test_evidence_link_required() -> None:
    stripped = AUTHOR.replace("%%EVIDENCE_URL%%", "")
    assert "v3-evidence-link" in rule_ids(check(author=stripped))
    substituted = AUTHOR.replace("%%EVIDENCE_URL%%", "https://evidence.example/21300/latest.html")
    assert "v3-evidence-link" not in rule_ids(check(author=substituted))


def test_broken_finding_row() -> None:
    broken = AUTHOR.replace("| **F2** |", "| *F2* |")
    assert "v3-finding-grammar" in rule_ids(check(author=broken))


def test_duplicate_id_across_cards() -> None:
    dup = BRIEF.replace("**F4**", "**F1**")
    assert "v3-finding-grammar" in rule_ids(check(brief=dup))


def test_invented_id_above_high_water() -> None:
    invented = AUTHOR.replace("**F2**", "**F99**")
    assert "v3-finding-grammar" in rule_ids(check(author=invented))


def test_model_added_placeholder_row_is_legal() -> None:
    added = AUTHOR.replace(
        "### ✅ Resolved since last review",
        "| | ID | Where | Finding |\n|---|---|---|---|\n"
        "| **F?** | `content/docs/iac/x.md` L200 | new issue the model found |\n\n"
        "### ✅ Resolved since last review",
    )
    ids = rule_ids(check(author=added))
    assert "v3-finding-grammar" not in ids
    # header (3) no longer equals total (4) but equals the numbered count (3)
    assert "v3-blocking-count" not in ids


def test_blocking_count_mismatch() -> None:
    wrong = AUTHOR.replace("guide v1 — 3 items block merge", "guide v1 — 7 items block merge")
    assert "v3-blocking-count" in rule_ids(check(author=wrong))


def test_bucket_demotion_rejected() -> None:
    # F1 is `outstanding` in the base; render it in ❓ instead of 🚨.
    lines = AUTHOR.splitlines()
    f1 = next(line for line in lines if line.startswith("| **F1** |"))
    demoted = AUTHOR.replace(f1 + "\n", "").replace(
        "### ❓ Questions for you\n",
        "### ❓ Questions for you\n\n"
        "| | ID | Where | Finding |\n|---|---|---|---|\n" + f1 + "\n",
    )
    assert "bucket-split-faithful" in rule_ids(check(author=demoted))


def test_vanished_finding_rejected_and_rewrite_accepted() -> None:
    f3 = next(line for line in AUTHOR.splitlines() if line.startswith("| **F3** |"))
    vanished = AUTHOR.replace(f3 + "\n", "")
    assert "bucket-split-faithful" in rule_ids(check(author=vanished))
    rewritten = AUTHOR.replace(
        f3, "| **F3** | `content/docs/iac/x.md` L61 | **Spurious:** verifier compared a paraphrase |"
    )
    assert "bucket-split-faithful" not in rule_ids(check(author=rewritten))


def test_promotion_is_legal() -> None:
    # F4 is `reviewer-check` in the base; promoting it into the author ❓ is fine.
    f4 = next(line for line in BRIEF.splitlines() if line.startswith("| **F4** |"))
    brief_without = BRIEF.replace(f4 + "\n", "")
    author_with = AUTHOR.replace(
        "#### Style suggestions",
        f4 + "\n\n#### Style suggestions",
    )
    ids = rule_ids(check(author=author_with, brief=brief_without))
    assert "bucket-split-faithful" not in ids


def _count_buckets(body_text: str) -> dict[str, int]:
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
        f.write(body_text)
        path = f.name
    r = subprocess.run(
        [sys.executable, str(HERE / "validate-pinned.py"), "count-buckets", "--body-file", path],
        capture_output=True, text=True,
    )
    assert r.returncode == 0, r.stderr
    return {k: int(v) for k, v in (line.split("=") for line in r.stdout.strip().splitlines())}


def test_count_buckets_v3() -> None:
    joined = AUTHOR + "\n\n" + BRIEF
    counts = _count_buckets(joined)
    assert counts["outstanding"] == 3  # F1, F2, F3 — none dispositioned
    assert counts["low_confidence"] == 1  # F4 in ⚠️


def test_count_buckets_v3_dispositions_unblock() -> None:
    rs = _load("rs_for_cb_test", HERE.parents[3] / "scripts" / "review-v3" / "review_state.py")
    state = rs.empty_state()
    state["high_water"] = 4
    for fid in ("F1", "F2", "F3"):
        state = rs.set_disposition(state, fid, "refuted", actor="author", note="")
    answered = rs.replace_block(AUTHOR, state)
    counts = _count_buckets(answered + "\n\n" + BRIEF)
    assert counts["outstanding"] == 0


def test_brief_advisory_prose_note_allowed() -> None:
    # The exact shape from the first live fork battery (PR 243): a plain
    # prose note in ⚠️ is advisory, not a tracked finding, and must not
    # fail the grammar rule. A prose bullet in a BLOCKING section still does.
    note = "- **One editorial call:** the new clause repeats the info note below; judgment call, not a defect."
    brief = BRIEF.replace(
        "### ⚠️ Check these before approving\n",
        "### ⚠️ Check these before approving\n\n" + note + "\n",
    )
    assert not [v for v in check(brief=brief) if v.rule_id == "v3-finding-grammar"]

    author = AUTHOR.replace(
        "### 🚨 Fix or disagree\n",
        "### 🚨 Fix or disagree\n\n- **A stray thought:** untracked prose in a blocking section.\n",
    )
    assert [v for v in check(author=author) if v.rule_id == "v3-finding-grammar"]


def test_count_buckets_v3_corrupt_state_counts_all() -> None:
    corrupt = AUTHOR.replace('<!-- REVIEW_STATE {"findings"', '<!-- REVIEW_STATE {"findings')
    counts = _count_buckets(corrupt + "\n\n" + BRIEF)
    assert counts["outstanding"] == 3  # conservative: unreadable state blocks


if __name__ == "__main__":
    failures = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print(f"  ok: {name}")
            except AssertionError as e:
                failures += 1
                print(f"  FAIL: {name}: {e}", file=sys.stderr)
    sys.exit(1 if failures else 0)
