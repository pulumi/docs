"""Consistency tests between the Vale rule files and the tier lists.

The tier lists in vale-deterministic-fixes.yaml name rules as bare strings, and
vale-findings-filter.py maps rule names to the reader-facing `category` label.
Nothing connected those to the actual rule files, so a rule could be renamed,
deleted, or added without any test noticing -- and a blocker with no category
entry silently renders as the generic "style", which is the only rule identity
a reader ever sees (the `rule` field is deliberately never surfaced).
"""

import importlib.util
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parents[4]
SCRIPTS = REPO / ".claude/commands/docs-review/scripts"
TIERS = SCRIPTS / "vale-deterministic-fixes.yaml"
STYLES = REPO / "styles"


def _filter_module():
    spec = importlib.util.spec_from_file_location(
        "vale_findings_filter", SCRIPTS / "vale-findings-filter.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


TIER_DATA = yaml.safe_load(TIERS.read_text())
BLOCKERS = TIER_DATA.get("blocker") or []
FIXES = TIER_DATA.get("deterministic_fix") or []
ALL_TIERED = sorted(set(BLOCKERS) | set(FIXES))


def _rule_path(rule: str) -> Path:
    package, _, name = rule.partition(".")
    return STYLES / package / f"{name}.yml"


@pytest.mark.parametrize("rule", ALL_TIERED)
def test_tiered_rule_file_exists(rule):
    assert _rule_path(rule).is_file(), (
        f"{rule} is on a tier list in {TIERS.name} but {_rule_path(rule)} "
        "does not exist. A renamed or deleted rule silently stops being "
        "tiered -- Vale emits findings under the new name and the filter "
        "never matches them."
    )


@pytest.mark.parametrize("rule", BLOCKERS)
def test_every_blocker_has_a_category(rule):
    mod = _filter_module()
    assert rule in mod.RULE_CATEGORIES, (
        f"{rule} is a blocker but has no RULE_CATEGORIES entry, so it renders "
        f'as "[style-blocker] _style_". `category` is the only rule identity '
        "the reader sees; the rule name is never surfaced."
    )
    assert mod.category_for(rule) != "style"


@pytest.mark.parametrize("rule", ALL_TIERED)
def test_tiered_rules_are_not_globally_disabled(rule):
    """A rule switched off in .vale.ini's global block can never fire."""
    ini = (REPO / ".vale.ini").read_text()
    disabled = []
    for line in ini.splitlines():
        if line.startswith("[") and not line.startswith("[*.md]"):
            break  # past the global block, into path-scoped sections
        stripped = line.split("#", 1)[0].strip()
        if stripped.endswith("= NO"):
            disabled.append(stripped.split("=")[0].strip())
    assert rule not in disabled, f"{rule} is tiered but disabled in .vale.ini"


def test_blocker_rules_are_error_level():
    """Blockers should agree with their own Vale severity.

    The pipeline tiers off the rule name, not `level:`, so a mismatch is inert
    today -- but the emitted `severity` field would contradict the 🚨 bucket,
    and raising MinAlertLevel would silently drop the finding.
    """
    mismatched = []
    for rule in BLOCKERS:
        data = yaml.safe_load(_rule_path(rule).read_text())
        if data.get("level") != "error":
            mismatched.append((rule, data.get("level")))
    assert not mismatched, f"blocker rules not at level: error -> {mismatched}"


def test_advisory_dedup_keeps_one_bullet_per_repeated_finding():
    """One repeated defect is one thing to fix, not ten cap slots."""
    mod = _filter_module()
    findings = [
        {
            "file": "content/docs/a.md",
            "line": n,
            "category": "misspelling",
            "message": "'widgetization' isn't in the dictionary",
            "blocker": False,
        }
        for n in range(1, 31)
    ]
    findings.append(
        {
            "file": "content/docs/a.md",
            "line": 40,
            "category": "heading capitalization",
            "message": "Heading 'Getting Started' should use sentence case",
            "blocker": False,
        }
    )
    out = mod.cap(findings)
    categories = [f["category"] for f in out]
    assert categories.count("misspelling") == 1
    assert "heading capitalization" in categories, (
        "the repeated finding consumed the per-file cap and starved a "
        "distinct finding -- the exact regression dedup exists to prevent"
    )


def test_blockers_bypass_the_caps():
    mod = _filter_module()
    findings = [
        {
            "file": "content/docs/a.md",
            "line": n,
            "category": "retired product name",
            "message": f"msg {n}",
            "blocker": True,
        }
        for n in range(1, 26)
    ]
    out = mod.cap(findings)
    assert len(out) == 25, "a blocker was silently dropped by a cap"
