#!/usr/bin/env python3
"""Deterministic retirement veto for the content-review worker.

The selection queue stamps `no_retire` per article (from
`.claude/commands/review-existing-content/references/strategic-tiers.yaml`),
but until this gate existed the veto was honored only by the review model
reading the skill — nothing programmatically blocked a
`content-review/retire-<slug>` branch for a protected page (issue #20078
§3.1). This script is the code-enforced backstop: given the article's repo
path, it answers "may this page be retired?" from the tiers file alone. It
never consults the queue or the verdict sentinel — both pass through the
model's hands and are therefore model-writable; the workflow passes the
article path from the trusted `workflow_dispatch` input instead.

Semantics match selection exactly (the logic is imported from
`select-articles.py`, the single source of truth): longest prefix wins, and
`no_retire = rule.no_retire or tier == 1`. Tier 0 (generated content) is also
vetoed — the bot must never touch those trees, retirement included.

The workflow runs this in the credentialed publish job, against that job's
own clean checkout of strategic-tiers.yaml — the model's patch is not yet
applied there (and the handoff export strips dot-paths, so a patch can never
carry a tiers edit), which is what makes the tiers file trustworthy input.

Usage:
    check-retire-veto.py --path content/docs/iac/concepts/state.md \
        [--tiers <strategic-tiers.yaml>]
    check-retire-veto.py --self-test

Prints a one-line JSON verdict {"path", "tier", "no_retire", "matched_prefix"}
to stdout. Exit 0 = retirement allowed; exit 2 = vetoed (with a `::error::`
line naming the matching rule); exit 1 = usage/input error.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

# Reuse the tier semantics from select-articles.py (single source of truth).
# Its filename is hyphenated, so import it by path; its main() is guarded
# under __main__, so importing has no side effects.
_spec = importlib.util.spec_from_file_location(
    "select_articles", HERE / "select-articles.py"
)
_select = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_select)
load_tiers = _select.load_tiers
tier_for = _select.tier_for
policy_for = _select.policy_for
DEFAULT_TIERS = _select.DEFAULT_TIERS


def verdict_for(path: str, rules: list[dict]) -> dict:
    """Tier facts for one repo path: tier, no_retire, and the winning prefix."""
    policy = policy_for(path, rules)
    matched = next(
        (r.get("prefix") for r in rules if path.startswith(r.get("prefix", ""))),
        None,
    )
    # A page a generator owns is never retired by this pipeline either — the
    # generator would recreate it, and the report-only lane visits some of
    # these pages now (pulumi/docs#20996), so the veto keys on `editable`
    # rather than on tier 0. Selection already excludes retirement for them;
    # this gate is deliberately defensive.
    return {
        "path": path,
        "tier": policy.tier,
        "no_retire": policy.no_retire or not policy.editable,
        "matched_prefix": matched,
    }


def run(args) -> int:
    tiers_file = Path(args.tiers) if args.tiers else DEFAULT_TIERS
    if not tiers_file.is_file():
        print(f"::error::check-retire-veto: tiers file not found: {tiers_file}",
              file=sys.stderr)
        return 1
    v = verdict_for(args.path, load_tiers(tiers_file))
    print(json.dumps(v, sort_keys=True))
    if v["no_retire"]:
        rule = v["matched_prefix"] or "(tier default)"
        print(f"::error::check-retire-veto: retirement of {v['path']} is vetoed "
              f"(tier {v['tier']}, matching rule prefix: {rule})", file=sys.stderr)
        return 2
    return 0


def self_test() -> int:
    import tempfile

    failures = []

    def check(name, cond):
        print(("ok: " if cond else "FAIL: ") + name,
              file=sys.stdout if cond else sys.stderr)
        if not cond:
            failures.append(name)

    # Against the real shipped tiers file: pins the protection promises the
    # repo currently makes (mirrors test_select_articles.py validating the
    # generated trees' lanes).
    real = load_tiers(DEFAULT_TIERS)
    check("real: tier-1 page vetoed (iac/concepts implies no_retire)",
          verdict_for("content/docs/iac/concepts/state.md", real)["no_retire"])
    check("real: explicit no_retire tier-2 vetoed (iac/)",
          verdict_for("content/docs/iac/languages-sdks/python.md", real)["no_retire"])
    check("real: pinned tier-3 vetoed (reference/)",
          verdict_for("content/docs/reference/cloud-rest-api/_index.md", real)["no_retire"])
    # The CLI reference is `editable: false, reviewable: true` since #20996 —
    # the report-only lane visits it, so the veto must come from `editable`
    # and not from the tier alone (its tier is 3).
    cli = verdict_for("content/docs/iac/cli/commands/pulumi_up.md", real)
    check("real: generated CLI tree vetoed despite being tier 3 and reviewable",
          cli["no_retire"] and cli["tier"] == 3)
    check("real: tier-0 generated tree vetoed",
          verdict_for("content/docs/reference/pkg/python/pulumi/_index.md", real)["no_retire"])
    check("real: unmatched tier-3 page allowed",
          not verdict_for("content/docs/support/faq.md", real)["no_retire"])

    # Against a synthetic file: the matching semantics themselves.
    synthetic = """
tiers:
  - prefix: content/docs/a/
    tier: 2
    no_retire: true
  - prefix: content/docs/a/deep/
    tier: 3
  - prefix: content/docs/flag/
    tier: 1
"""
    with tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False) as f:
        f.write(synthetic)
        synth_path = Path(f.name)
    try:
        rules = load_tiers(synth_path)
        v = verdict_for("content/docs/a/page.md", rules)
        check("synthetic: explicit no_retire vetoes", v["no_retire"] and v["tier"] == 2)
        v = verdict_for("content/docs/a/deep/page.md", rules)
        check("synthetic: longest prefix wins (deeper tier-3 overrides no_retire)",
              not v["no_retire"] and v["matched_prefix"] == "content/docs/a/deep/")
        v = verdict_for("content/docs/flag/x.md", rules)
        check("synthetic: tier 1 implies no_retire", v["no_retire"])
        v = verdict_for("content/docs/other/x.md", rules)
        check("synthetic: unmatched path defaults to allowed",
              not v["no_retire"] and v["tier"] == 3 and v["matched_prefix"] is None)
    finally:
        synth_path.unlink()

    if failures:
        print(f"\n{len(failures)} failure(s)", file=sys.stderr)
        return 1
    print("\nall check-retire-veto self-tests passed")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(
        description="Code-enforced no_retire veto for content-review retirement branches."
    )
    p.add_argument("--path", help="article repo path (content/docs/...)")
    p.add_argument("--tiers",
                   help="strategic-tiers.yaml to read (default: the in-repo file; "
                        "the workflow passes its pre-model snapshot)")
    p.add_argument("--self-test", action="store_true", help="run built-in checks")
    args = p.parse_args()

    if args.self_test:
        return self_test()
    if not args.path:
        p.error("--path is required (or use --self-test)")
    return run(args)


if __name__ == "__main__":
    sys.exit(main())
