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


def test_fix_mode_returns_every_finding_uncapped():
    """The fix consumer clears a backlog; the caps are a comment budget.

    Regression guard for the churn loop: a single-file run capped at
    PER_FILE_CAP fixes 10 findings and leaves the rest to resurface on the
    next review as fresh PR churn (observed on #21456).
    """
    mod = _filter_module()
    findings = [
        {
            "file": "content/docs/a.md",
            "line": n,
            "category": "wordiness",
            "message": f"'phrase {n}' is too wordy",
            "blocker": False,
        }
        for n in range(1, 31)
    ]
    out = mod.cap(findings, fix_mode=True)
    assert len(out) == 30, (
        f"fix mode dropped {30 - len(out)} findings -- the per-file cap is a "
        "readability budget for the pinned comment and must not truncate the "
        "backlog a fixing consumer is here to clear"
    )
    assert mod.cap(findings) != out, "review mode should still cap"


def test_fix_mode_keeps_every_occurrence_of_a_repeated_message():
    """Dedup is sound for a reader, wrong for a fixer.

    A rule whose message names a *shape* rather than a term emits the same
    message for every occurrence (Pulumi.NarrativeWe: one message per
    "we will"). Deduped, a fixer sees one line and silently leaves the rest.
    """
    mod = _filter_module()
    findings = [
        {
            "file": "content/docs/a.md",
            "line": n,
            "category": "narrative voice",
            "message": "Narrative walkthrough voice ('we will')",
            "blocker": False,
        }
        for n in (10, 40, 90)
    ]
    out = mod.cap(findings, fix_mode=True)
    assert [f["line"] for f in out] == [10, 40, 90], (
        "fix mode de-duplicated distinct occurrences; each needs its own "
        "editorial rewrite, so hiding two of three leaves the page half-fixed"
    )
    assert len(mod.cap(findings)) == 1, "review mode should still dedup"


def test_fix_mode_sorts_by_file_then_line():
    mod = _filter_module()
    findings = [
        {"file": "content/docs/b.md", "line": 5, "category": "x",
         "message": "m", "blocker": False},
        {"file": "content/docs/a.md", "line": 9, "category": "x",
         "message": "m", "blocker": False},
        {"file": "content/docs/a.md", "line": 2, "category": "x",
         "message": "m", "blocker": False},
    ]
    out = mod.cap(findings, fix_mode=True)
    assert [(f["file"], f["line"]) for f in out] == [
        ("content/docs/a.md", 2),
        ("content/docs/a.md", 9),
        ("content/docs/b.md", 5),
    ]


def test_review_mode_is_the_default():
    """--fix-mode must be opt-in: a review surface that forgets it should
    still get the readable, capped list rather than 200 nags."""
    mod = _filter_module()
    findings = [
        {
            "file": "content/docs/a.md",
            "line": n,
            "category": "wordiness",
            "message": f"'phrase {n}' is too wordy",
            "blocker": False,
        }
        for n in range(1, 31)
    ]
    assert len(mod.cap(findings)) == mod.PER_FILE_CAP
