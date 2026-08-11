#!/usr/bin/env python3
"""Unit tests for splice-spine.py.

Self-contained — run with `python3 test_splice_spine.py` or under pytest.

The cases that matter most are the NEGATIVE ones. This code runs immediately
before publication on a body nobody has seen, so a spurious restore corrupts a
good review; "leaves a healthy body byte-identical" is the property under test
as much as "puts a dropped trail back".
"""

from __future__ import annotations

import importlib.util
import sys
import traceback
from pathlib import Path

HERE = Path(__file__).resolve().parent

_spec = importlib.util.spec_from_file_location("splice_spine", HERE / "splice-spine.py")
ss = importlib.util.module_from_spec(_spec)
sys.modules["splice_spine"] = ss
_spec.loader.exec_module(ss)  # type: ignore[union-attr]

TRAIL = ss.TRAIL_HEADING
BALANCE = ss.BALANCE_HEADING

LOG_BLOCK = """<details>
<summary>Investigation log</summary>

- **Cross-sibling reads:** not run (not in a templated section)
- **External claim verification:** 4 of 4 claims verified
- **Cited-claim spot-checks:** not run (no cited claims)
- **Frontmatter sweep:** not run (no frontmatter in diff)
- **Temporal-trigger sweep:** not run (no trigger words)
- **Code execution:** not run (no `static/programs/` change)
- **Code-examples checks:** not run (no fenced code blocks)
- **Editorial-balance pass:** ran

</details>"""


def body(trail_lines: int = 3, log: bool = True, balance: bool = True,
         resolved: str = "_None._") -> str:
    trail = "\n".join(
        f'- L{10 + i} in `content/a.md` "claim {i}" → ✅ verified (evidence: e{i}; source: s{i})'
        for i in range(trail_lines)
    )
    parts = ["<!-- CLAUDE_REVIEW 1/1 -->", "## Pre-merge Review — Last updated 2026-08-10T00:00:00Z", ""]
    if log:
        parts += [LOG_BLOCK, ""]
    parts += [
        "| 🚨 Outstanding | ⚠️ Low-confidence | 💡 Pre-existing | ✅ Resolved |",
        "| :---: | :---: | :---: | :---: |",
        "| **1** | **0** | **0** | **0** |",
        "",
        f"### {TRAIL}",
        "",
        "<details>",
        "<summary><strong>3 claims extracted</strong></summary>",
        "",
        trail,
        "",
        "</details>",
        "",
    ]
    if balance:
        parts += [f"### {BALANCE}", "",
                  "Vendor mentions: 4 Pulumi / 2 Terraform. Tone: balanced.",
                  "No unsourced superlatives found in the diff.", ""]
    parts += [
        "### 🚨 Outstanding in this PR", "", "- **[L10]** `content/a.md` — Something is wrong.", "",
        "### ⚠️ Low-confidence", "", "_None._", "",
        "### ✅ Resolved since last review", "", resolved, "",
        "### 📜 Review history", "", "- 2026-08-10T00:00:00Z — initial review (abc1234)", "",
    ]
    return "\n".join(parts) + "\n"


def published(*bodies: str) -> str:
    """Wrap logical bodies the way `pinned-comment.sh fetch` emits them."""
    footer = f"\n{ss.FOOTER_SENTINEL}\n\n---\n\n- **Refresh this review** — comment `@claude`.\n"
    return f"\n{ss.PART_DELIMITER}\n".join(b + footer for b in bodies)


# ---- reassembly ---------------------------------------------------------------


def test_reassemble_strips_marker_and_footer():
    out = ss.reassemble(published(body()))
    assert ss.FOOTER_SENTINEL not in out
    assert "<!-- CLAUDE_REVIEW" not in out
    assert len(ss.extract_trail_records_of(out)) == 3


def test_reassemble_rejoins_a_split_details_block():
    """A <details> spilling across parts must not read as two blocks."""
    part1 = ("<!-- CLAUDE_REVIEW 1/2 -->\n"
             f"### {TRAIL}\n\n<details>\n<summary><strong>2 claims</strong></summary>\n\n"
             '- L10 in `a.md` "one" → ✅ verified (evidence: e; source: s)\n'
             "</details>\n")
    part2 = ("<!-- CLAUDE_REVIEW 2/2 -->\n"
             "<details>\n<summary><em>continued from previous comment</em></summary>\n\n"
             '- L20 in `a.md` "two" → ✅ verified (evidence: e; source: s)\n\n</details>\n')
    footer = f"\n{ss.FOOTER_SENTINEL}\n\nfooter text\n"
    out = ss.reassemble(part1 + footer + f"\n{ss.PART_DELIMITER}\n" + part2 + footer)
    assert "continued from previous comment" not in out
    assert out.count("</details>") == 1, out
    assert len(ss.extract_trail_records_of(out)) == 2


# ---- the negative cases (a healthy body must come through untouched) ----------


def test_identical_bodies_are_untouched():
    b = body()
    drops = ss.assess(ss.reassemble(published(b)), b)
    assert drops == []


def test_growth_is_allowed():
    prior, new = body(trail_lines=3), body(trail_lines=9)
    assert ss.assess(ss.reassemble(published(prior)), new) == []


def test_findings_moving_to_resolved_does_not_trip_it():
    """Normal refresh churn: a finding resolves, the trail is unchanged."""
    prior = body(trail_lines=4)
    new = body(trail_lines=4, resolved="- **[L10]** Fixed. (resolved in def5678)")
    assert ss.assess(ss.reassemble(published(prior)), new) == []


def test_no_prior_is_a_noop():
    assert ss.reassemble("") == ""


# ---- the positive cases --------------------------------------------------------


def test_dropped_trail_is_restored_verbatim():
    prior, new = body(trail_lines=40), body(trail_lines=0)
    p = ss.reassemble(published(prior))
    drops = ss.assess(p, new)
    assert [d["section"] for d in drops] == [TRAIL]
    out, applied = ss.restore(p, new, drops)
    assert len(applied) == 1
    assert len(ss.extract_trail_records_of(out)) == 40
    # ...and nothing else moved.
    assert "- **[L10]** `content/a.md` — Something is wrong." in out
    assert out.count(f"### {TRAIL}") == 1


def test_prose_pointer_collapse_is_caught():
    """The measured failure: heading kept, 40 records replaced by a pointer."""
    prior = body(trail_lines=40)
    # Replace ONLY the trail section's contents — the rest of the body, balance
    # section included, renders normally. That is what the failure looks like.
    lines = prior.splitlines()
    start, end = ss._vp.find_section(prior, TRAIL)
    lines[start:end] = [
        f"### {TRAIL}", "",
        "The full 40-claim extraction/verification trail from the initial review is",
        "unchanged by this push — see 🚨 Outstanding and ✅ Resolved below.", "",
    ]
    new = "\n".join(lines) + "\n"
    p = ss.reassemble(published(prior))
    drops = ss.assess(p, new)
    assert [d["section"] for d in drops] == [TRAIL]
    assert drops[0]["prior"] == 40 and drops[0]["new"] == 0
    out, _ = ss.restore(p, new, drops)
    assert len(ss.extract_trail_records_of(out)) == 40
    assert "unchanged by this push" not in out


def test_section_missing_entirely_is_reinserted_in_h3_order():
    prior = body(trail_lines=5)
    new = body(trail_lines=5).replace(
        f"### {TRAIL}\n\n<details>\n<summary><strong>3 claims extracted</strong></summary>\n", "")
    # Strip the whole section so the heading is gone.
    lines, keep, drop_mode = new.splitlines(), [], False
    for ln in lines:
        if ln.startswith(f"### {TRAIL}"):
            drop_mode = True
            continue
        if drop_mode and ln.startswith("### "):
            drop_mode = False
        if not drop_mode:
            keep.append(ln)
    new = "\n".join(keep) + "\n"
    assert TRAIL not in new
    p = ss.reassemble(published(prior))
    out, applied = ss.restore(p, new, ss.assess(p, new))
    assert applied and TRAIL in out
    # Reinserted BEFORE 🚨 Outstanding, per MANDATORY_H3_SECTIONS.
    assert out.index(f"### {TRAIL}") < out.index("### 🚨 Outstanding")


def test_gutted_investigation_log_is_restored():
    prior, new = body(), body(log=False)
    p = ss.reassemble(published(prior))
    drops = ss.assess(p, new)
    assert any(d["section"] == "Investigation log" for d in drops)
    out, applied = ss.restore(p, new, drops)
    assert ss._log_bullet_count(ss._investigation_log(out)) == 8


def test_gutted_editorial_balance_is_restored():
    prior, new = body(), body(balance=False)
    p = ss.reassemble(published(prior))
    drops = ss.assess(p, new)
    assert any(d["section"] == BALANCE for d in drops)
    out, _ = ss.restore(p, new, drops)
    assert "Vendor mentions: 4 Pulumi" in out
    assert out.index(f"### {BALANCE}") > out.index(f"### {TRAIL}")


def test_balance_reflow_does_not_trip_the_byte_threshold():
    prior = body()
    new = body().replace("Vendor mentions: 4 Pulumi / 2 Terraform. Tone: balanced.",
                         "Vendor mentions: 4 Pulumi / 2 Terraform.\nTone: balanced.")
    assert not any(d["section"] == BALANCE for d in ss.assess(ss.reassemble(published(prior)), new))


# ---- real fixture --------------------------------------------------------------


def test_real_47kb_body_roundtrips_untouched():
    """The published review from pulumi/docs#20779 — 40 trail records."""
    fixture = Path("/workspaces/src/scratch/2026-08-08-opus-update-lane-bench/"
                   "fixtures/prior-pinned-body.md")
    if not fixture.is_file():
        return  # optional: the benchmark run folder is not part of the repo
    real = fixture.read_text()
    p = ss.reassemble(published(real))
    assert len(ss.extract_trail_records_of(p)) == 40
    assert ss.assess(p, real) == []


# ---- runner --------------------------------------------------------------------


def _run():
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    failed = 0
    for t in tests:
        try:
            t()
            print(f"  ok  {t.__name__}")
        except Exception:
            failed += 1
            print(f"FAIL  {t.__name__}")
            traceback.print_exc()
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(_run())
