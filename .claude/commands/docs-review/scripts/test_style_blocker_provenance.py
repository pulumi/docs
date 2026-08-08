"""Tests for the style-blocker-provenance validator rule.

Regression: on 2026-08-03 (fork PR CamSoper/pulumi.docs#227) a review authored
its own `[style-blocker] _misspelling_` bullet for a typo Vale never reported.
The finding was real, but `[style-blocker]` exempts a bullet from
trail-matching, so an authored one routes an unverified finding into 🚨 past
that check.
"""

from __future__ import annotations

import importlib.util
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("validate_pinned", HERE / "validate-pinned.py")
vp = importlib.util.module_from_spec(_spec)
sys.modules["validate_pinned"] = vp
_spec.loader.exec_module(vp)

FILE = "content/docs/iac/concepts/secrets/_index.md"

REAL_FINDINGS = [
    {"file": FILE, "line": 797, "rule": "Pulumi.DeprecatedProductNames",
     "category": "deprecated product name", "blocker": True},
    {"file": FILE, "line": 797, "rule": "Pulumi.Substitutions",
     "category": "substitution", "blocker": True},
    {"file": FILE, "line": 767, "rule": "write-good.Weasel",
     "category": "weasel word", "blocker": False},
]


def ctx_for(body: str, findings):
    return vp.Context(
        body=body, body_lines=body.splitlines(), pr=None, repo=None,
        diff_files=[], diff_files_added=set(), diff_text="",
        repo_root=pathlib.Path("."), is_blog=False, vale_findings=findings)


def bullet(line: int, category: str) -> str:
    return (f"- **[L{line}]** `{FILE}` — [style-blocker] _{category}_ — message text.")


def body_with(*bullets: str) -> str:
    joined = "\n\n".join(bullets)
    return ("### 🚨 Outstanding in this PR\n\n"
            "*These must be resolved or refuted before merging.*\n\n"
            f"{joined}\n\n### ⚠️ Low-confidence\n")


def test_composer_rendered_blockers_pass():
    body = body_with(bullet(797, "deprecated product name"), bullet(797, "substitution"))
    assert vp.check_style_blocker_provenance(ctx_for(body, REAL_FINDINGS)) == []


def test_authored_blocker_is_flagged():
    body = body_with(bullet(771, "misspelling"), bullet(797, "substitution"))
    v = vp.check_style_blocker_provenance(ctx_for(body, REAL_FINDINGS))
    assert len(v) == 1
    assert v[0].rule_id == "style-blocker-provenance"
    assert "L771" in v[0].line_ref


def test_advisory_line_does_not_authorize_a_blocker():
    """A non-blocker Vale finding on the line must not launder a [style-blocker]."""
    body = body_with(bullet(767, "weasel word"))
    assert len(vp.check_style_blocker_provenance(ctx_for(body, REAL_FINDINGS))) == 1


def test_missing_artifact_skips():
    body = body_with(bullet(771, "misspelling"))
    assert vp.check_style_blocker_provenance(ctx_for(body, None)) == []


def test_ordinary_bullets_ignored():
    body = body_with(f"- **[L771]** `{FILE}` — *\"a claim\"* — verdict: contradicted; fix it.")
    assert vp.check_style_blocker_provenance(ctx_for(body, REAL_FINDINGS)) == []
