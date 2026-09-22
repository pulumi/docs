"""Tests for the style-advisory-provenance rule and the `[nit]` lane it guards.

The v3 author card's advisory block is its only non-blocking lane. Until
2026-09-22 it carried Vale's output and nothing else, so a nit the review found
itself — a typo, a stray space — had no author-facing home: 🚨 blocks merge, ❓
is the composer's `unverifiable` lane, and a hand-written `[style]` bullet
desynced the brief's Vale-derived count. PR #21787 F3 is the result: "Typo:
`i. e.` has a stray space … Trivial fix for the author", shipped on the
reviewer's card, which is headed "not for the author".

Opening the block recreates one tier down the bypass `style-blocker-provenance`
exists to close, so the two tags split by provenance and this rule holds each
to its own: `[style]` asserts Vale produced the finding, `[nit]` says the review
did.
"""

from __future__ import annotations

import importlib.util
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent


def _load(name: str, path: pathlib.Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


vp = _load("validate_pinned", HERE / "validate-pinned.py")
cr = _load("compose_review", HERE / "compose-review.py")

FILE = "content/docs/support/provider-support-policy.md"

VALE = [
    {"file": FILE, "line": 97, "rule": "write-good.TooWordy",
     "category": "wordiness", "blocker": False},
    {"file": FILE, "line": 30, "rule": "Pulumi.DeprecatedProductNames",
     "category": "deprecated product name", "blocker": True},
]


def ctx_for(body: str, findings, surface: str = "v3"):
    return vp.Context(
        body=body, body_lines=body.splitlines(), pr=None, repo=None,
        diff_files=[], diff_files_added=set(), diff_text="",
        repo_root=pathlib.Path("."), is_blog=False, vale_findings=findings,
        surface=surface)


def block(*bullets: str) -> str:
    joined = "\n".join(bullets)
    return ("#### Style suggestions\n\n"
            "*Optional polish from pattern-based linting and the review's own read.*\n\n"
            f"##### {FILE}\n\n{joined}\n\n"
            "📎 **Full evidence:** [trail](https://example.invalid).\n")


STYLE_97 = "- **line 97:** [style] _wordiness_ — 'benefit from' is too wordy."
NIT_72 = "- **line 72:** [nit] _typo_ — `i. e.` has a stray space; use `i.e.`"


def test_vale_backed_style_bullet_passes():
    assert vp.check_style_advisory_provenance(ctx_for(block(STYLE_97), VALE)) == []


def test_model_written_style_bullet_is_flagged():
    """The bypass this rule closes: a model finding dressed as linter output."""
    fake = "- **line 72:** [style] _typo_ — `i. e.` has a stray space."
    v = vp.check_style_advisory_provenance(ctx_for(block(fake), VALE))
    assert len(v) == 1
    assert v[0].rule_id == "style-advisory-provenance"
    assert "[nit]" in v[0].hint


def test_blocker_line_does_not_authorize_an_advisory_bullet():
    """Line 30 is a Vale BLOCKER — it renders in 🚨, not here."""
    fake = "- **line 30:** [style] _deprecated product name_ — message."
    assert len(vp.check_style_advisory_provenance(ctx_for(block(fake), VALE))) == 1


def test_nit_bullet_passes_on_v3():
    assert vp.check_style_advisory_provenance(ctx_for(block(NIT_72), VALE)) == []


def test_nit_bullet_rejected_on_v2():
    """v2's monolith is read by author and reviewer both — its ⚠️ section
    already reaches the author, so the lane doesn't exist there."""
    v = vp.check_style_advisory_provenance(ctx_for(block(NIT_72), VALE, surface="v2"))
    assert len(v) == 1
    assert "v3" in v[0].expected


def test_missing_artifact_skips():
    fake = "- **line 72:** [style] _typo_ — message."
    assert vp.check_style_advisory_provenance(ctx_for(block(fake), None)) == []


def test_bullets_outside_the_block_are_ignored():
    body = ("### ⚠️ Check these before approving\n\n"
            "- **line 72:** [style] _typo_ — not in the advisory block.\n")
    assert vp.check_style_advisory_provenance(ctx_for(body, VALE)) == []


# ---- the shared walker the rule, the recount, and the annotator all read ----

def test_walk_attributes_bullets_to_their_file_heading():
    body = ("#### Style suggestions\n\n"
            "##### a.md\n\n- **line 1:** [style] _wordiness_ — x.\n\n"
            "##### b.md\n\n- **line 2:** [nit] _typo_ — y.\n")
    assert cr.walk_style_bullets(body) == [
        {"file": "a.md", "line": 1, "tag": "style", "text": "_wordiness_ — x."},
        {"file": "b.md", "line": 2, "tag": "nit", "text": "_typo_ — y."},
    ]


def test_walk_stops_at_the_next_section():
    body = (f"{block(STYLE_97)}\n### ✅ Resolved since last review\n\n"
            "- **line 5:** [style] _wordiness_ — already gone.\n")
    assert [b["line"] for b in cr.walk_style_bullets(body)] == [97]


def test_walk_tolerates_a_bullet_with_no_heading():
    """A split review's later part carries bullets whose `##### <path>` heading
    stayed on the previous page — the same degradation annotate_text allows."""
    body = "#### Style suggestions\n\n- **line 9:** [nit] _typo_ — orphan.\n"
    assert cr.walk_style_bullets(body) == [
        {"file": "", "line": 9, "tag": "nit", "text": "_typo_ — orphan."}]


# ---- interop with the block's other readers ---------------------------------

def test_nit_bullet_can_carry_a_suggestion_mark():
    """`post-style-suggestions.annotate_text` keys ✏️ marks off `- **line N:**`
    and the `##### <path>` heading, not the tag — so a staged `[nit]` gets its
    button like any advisory bullet."""
    psm = _load("post_style_suggestions", HERE / "post-style-suggestions.py")
    body = f"#### Style suggestions\n\n##### {FILE}\n\n{NIT_72}\n"
    out, marked = psm.annotate_text(body, [{"file": FILE, "line": 72}])
    assert marked == 1 and psm.SUGGESTION_MARK in out


def test_nits_are_not_counted_as_v3_findings():
    """v3 counts blocking findings as TABLE ROWS, so a `[nit]` bullet can never
    reach a bucket cell or the merge gate — even when the block renders inside
    a finding section. (`extract_bucket_bullets` returns `- **line N:**` lines
    by design; it is the v2 counter, and its callers filter on that prefix.)"""
    body = ("### 🚨 Fix or disagree\n\n| ID | Where | Finding |\n|---|---|---|\n"
            f"| **F1** | `{FILE}` L30 | a real finding |\n\n"
            f"{block(NIT_72)}")
    rows = vp.v3_finding_rows(body, "🚨 Fix or disagree")
    assert [r[2]["id"] for r in rows if r[2]] == ["F1"]
    assert not any(NIT_72 in raw for _ln, raw, _p in rows)


def test_style_render_mode_reaches_the_v3_author_card():
    """Regression: the rule scoped its scan to a `⚠️ Low-confidence` section,
    which the v3 author card doesn't have — so it silently passed every v3
    body while the rules table advertised it as running there."""
    collapsed = ("#### Style suggestions\n\n<details>\n<summary>x</summary>\n\n"
                 f"##### {FILE}\n\n{STYLE_97}\n</details>\n")
    v = vp.check_style_render_mode(ctx_for(collapsed, VALE))
    assert len(v) == 1 and v[0].rule_id == "style-render-mode"
    assert vp.check_style_render_mode(ctx_for(block(STYLE_97), VALE)) == []
