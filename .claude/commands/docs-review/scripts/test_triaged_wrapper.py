#!/usr/bin/env python3
"""Tests for the `triaged-details-wrapper` rule (validate-pinned side).

The splicer side lives in test_splicer.py. Self-contained:
`python3 test_triaged_wrapper.py`, and it also collects under pytest.

The negative cases carry the weight. This rule fires on a section that is
OPTIONAL, so a false positive would soft-floor a perfectly good review over
cosmetics — worse than the defect it catches.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod  # so dataclasses resolve their defining module
    spec.loader.exec_module(mod)
    return mod


vp = _load("validate_pinned", "validate-pinned.py")

SUMMARY = ("<summary><em>I double-checked these and realized they weren't real "
           "findings — click to expand</em></summary>")
BULLETS = (
    "- **[L107]** `a.md` — *\"claim one\"* — **Spurious:** wrong sibling compared.\n\n"
    "- **[L60]** `b.md` — *\"claim two\"* — **Mis-sourced:** cited URL unrelated.\n"
)


def body_with(triaged: str) -> str:
    return (
        "### ⚠️ Low-confidence\n\n_No low-confidence findings._\n\n"
        f"{triaged}"
        "### 💡 Pre-existing issues in touched files (optional)\n\n"
        "_No pre-existing issues in touched files._\n"
    )


def viols(body: str) -> list[str]:
    ctx = vp.Context(body=body, body_lines=body.splitlines(), pr=None, repo=None,
                     diff_files=[], diff_files_added=set(), diff_text="",
                     repo_root=Path("."), is_blog=False)
    return [v.rule_id for v in vp.check_triaged_details_wrapper(ctx)]


WRAPPED = f"### 📋 Triaged verifier findings\n\n<details>\n{SUMMARY}\n\n{BULLETS}\n</details>\n\n"
UNWRAPPED = f"### 📋 Triaged verifier findings\n\n{BULLETS}\n"
EMPTY_WRAPPED = (f"### 📋 Triaged verifier findings\n\n<details>\n{SUMMARY}\n\n"
                 "_No triaged findings._\n\n</details>\n\n")


def test_wrapped_section_is_clean():
    assert viols(body_with(WRAPPED)) == []


def test_unwrapped_section_with_bullets_is_flagged():
    assert viols(body_with(UNWRAPPED)) == ["triaged-details-wrapper"]


def test_absent_section_is_clean():
    """📋 is optional and not in MANDATORY_H3_SECTIONS — absence is not a defect."""
    assert viols(body_with("")) == []


def test_empty_placeholder_section_is_clean():
    """An empty-but-wrapped section is strip-empty-triaged.py's business."""
    assert viols(body_with(EMPTY_WRAPPED)) == []


def test_unwrapped_but_bulletless_is_clean():
    """No bullets means nothing to wrap; don't manufacture a violation."""
    assert viols(body_with(
        "### 📋 Triaged verifier findings\n\n_No triaged findings._\n\n")) == []


def test_details_present_but_summary_missing_is_flagged():
    assert viols(body_with(
        f"### 📋 Triaged verifier findings\n\n<details>\n\n{BULLETS}\n</details>\n\n"
    )) == ["triaged-details-wrapper"]


def test_quoted_heading_in_a_bullet_does_not_create_a_section():
    """A docs-review meta PR quotes the review format in its own findings.

    pulumi/docs#19777 does exactly this, and a substring search for the heading
    matches inside the quote — which is how this defect's rate was initially
    over-counted. `find_section` requires a real column-0 H3, so the rule must
    stay silent here.
    """
    body = (
        "### 🚨 Outstanding in this PR\n\n"
        "- **[L57]** `STYLE-GUIDE.md` — *\"### 📋 Triaged verifier findings is rendered "
        "collapsed\"* — the guide is out of date.\n"
    )
    assert viols(body) == []


def test_rule_is_registered_with_a_hint():
    rule = next((r for r in vp.RULES if r["id"] == "triaged-details-wrapper"), None)
    assert rule is not None, "rule must be in RULES or it never runs"
    assert rule["hint"], "validator refuses to start without a hint"
    assert rule["check"] is vp.check_triaged_details_wrapper


def main() -> int:
    tests = [v for k, v in sorted(globals().items())
             if k.startswith("test_") and callable(v)]
    failed = 0
    for t in tests:
        try:
            t()
            print(f"  ok  {t.__name__}")
        except Exception as exc:  # noqa: BLE001
            failed += 1
            print(f"FAIL  {t.__name__}: {exc}")
    print(f"\n{len(tests) - failed}/{len(tests)} tests passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
