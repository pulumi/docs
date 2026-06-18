#!/usr/bin/env python3
"""Tests for the `flagged` (🚩) detector verdict — the compose-review synthesizer
side and the validate-pinned acceptance side.

Self-contained: `python3 test_flagged_verdict.py`. Imports the hyphenated scripts
by path (their main() is guarded under __main__, so importing has no side effects).
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod  # so dataclasses can resolve annotations
    spec.loader.exec_module(mod)
    return mod


cr = _load("compose_review", "compose-review.py")
vp = _load("validate_pinned", "validate-pinned.py")

_fails: list[str] = []


def check(cond: bool, msg: str) -> None:
    print(("ok   " if cond else "FAIL ") + msg)
    if not cond:
        _fails.append(msg)


def main() -> int:
    # --- registry constants are in sync across both scripts ---
    for mod, nm in ((cr, "compose-review"), (vp, "validate-pinned")):
        check("flagged" in mod.TRAIL_VERDICT_WORDS, f"{nm}: flagged in TRAIL_VERDICT_WORDS")
        check(mod.EXPECTED_TRAIL_EMOJI.get("flagged") == "🚩", f"{nm}: flagged -> 🚩")
    check("flagged" in cr.OUTSTANDING_VERDICTS, "compose: flagged promotes")
    check("flagged" in vp.OUTSTANDING_VERDICT_WORDS, "validate: flagged promotes")
    check("🚩" in vp.OUTSTANDING_TRAIL_EMOJIS, "validate: 🚩 is an outstanding trail emoji")

    # --- readthrough synthesizer ---
    art = {"ran": True, "findings": [
        {"file": "content/docs/x.md", "line_range": "L40-58",
         "anchor_quote": "uses ESC before defining it",
         "failure_mode": "prerequisite-inversion", "fix_class": "local_repair",
         "proposed_fix": "move the definition above first use",
         "rationale": "reader hits ESC undefined"},
        {"file": "content/docs/x.md", "line_range": "L1-200",
         "anchor_quote": "tutorial and reference mixed",
         "failure_mode": "purpose-mismatch", "fix_class": "reconception",
         "proposed_fix": "split into two pages", "rationale": "page tries to be two things"},
    ]}
    sv = cr._readthrough_synthetic_verdicts(art)
    check(len(sv) == 2, "two synthetic readthrough verdicts")
    check(all(v["verdict"] == "flagged" and v["route"] == "preflight" for v in sv),
          "readthrough verdicts are flagged + preflight")
    check(sv[0]["type"] == "readthrough-prerequisite-inversion", "type carries the failure mode")
    check([v["fix_class"] for v in sv] == ["local_repair", "reconception"], "fix_class carried through")

    # --- Hugo + frontmatter retrofitted onto flagged ---
    hugo = cr._hugo_synthetic_verdicts({"errors": ["content/docs/y.md:12:3: bad shortcode"], "link_integrity": []})
    check(bool(hugo) and hugo[0]["verdict"] == "flagged", "hugo synthetic retrofit -> flagged")
    fm = cr._frontmatter_synthetic_verdicts(
        [{"file": "content/docs/z.md", "alias_collisions": [{"alias": "/a/", "collides_with": "/b/"}]}])
    check(bool(fm) and fm[0]["verdict"] == "flagged", "frontmatter synthetic retrofit -> flagged")

    # --- trail + stubs ---
    trail, *_ = cr.render_trail(sv, None)
    check("🚩 flagged" in trail, "trail renders '🚩 flagged'")
    # Preflight detectors render a `detector: subtype` token, not an evidence pointer.
    check("🚩 flagged (readthrough: prerequisite-inversion)" in trail,
          "trail parenthetical is the detector:subtype token, not (evidence: …)")
    check("evidence:" not in trail and "source:" not in trail,
          "preflight trail line carries no fact-check evidence/source pointer")
    outstanding, _low = cr.build_stubs(sv)
    check(len(outstanding) == 2, "readthrough findings stub to 🚨 Outstanding")
    joined = "\n".join(str(o) for o in outstanding)
    check("apply the structural fix" in joined and "reconception" in joined,
          "local_repair and reconception TODOs both present")
    check("NOT a fact-check claim" in joined,
          "stub TODO frames flagged as a detector finding (no fact-check verdict framing)")

    # --- detector findings excluded from the fact-check claim counts ---
    mixed = [{"verdict": "verified", "route": "pass1"},
             {"verdict": "contradicted", "route": "pass1"}] + sv
    log = cr.render_investigation_log(
        cross_sibling=[], verdicts=mixed, route_counts=cr.compute_route_counts(mixed, None),
        frontmatter=[], has_temporal_trigger=False, diff_files=[],
        has_fenced_code_in_content=False, editorial_balance=None, is_blog=False,
        diff_unavailable=False)
    check("1 of 2 claims verified" in log, "claim count excludes the 2 detector findings")
    check("routed: 0 inline, 2 Pass 1" in log, "route counts exclude preflight (sum to 2)")

    # --- validate-pinned accepts a flagged trail line + its bucket bullet ---
    body = (
        "### 🔍 Verification trail\n\n"
        "- L40-58 \"uses ESC before defining it\" → 🚩 flagged (readthrough: prerequisite-inversion)\n\n"
        "### 🚨 Outstanding\n\n"
        "- **[L40-58]** `content/docs/x.md` \"uses ESC...\" — move the definition above first use.\n\n"
        "### ⚠️ Low-confidence\n\n_No low-confidence findings._\n"
    )
    ctx = vp.Context(body=body, body_lines=body.splitlines(), pr=None, repo=None,
                     diff_files=["content/docs/x.md"], diff_files_added=set(),
                     diff_text="", repo_root=Path("."), is_blog=False)
    viols = [f"{v.rule_id}@{v.line_ref}" for v in vp.check_trail_bucket_consistency(ctx)]
    check(not viols, f"validator accepts flagged trail+bucket (violations: {viols})")

    # --- a NON-BLOCKING flagged finding may live in ⚠️ Low-confidence (schema 17).
    # Opus triages a recommended/reconception readthrough finding down to ⚠️; the
    # promotion rule must accept ⚠️ for `flagged` (but NOT for contradicted). ---
    def _viols(trail_verdict_line: str, bucket: str) -> list[str]:
        b = (
            "### 🔍 Verification trail\n\n"
            f"{trail_verdict_line}\n\n"
            "### 🚨 Outstanding\n\n_No outstanding findings._\n\n"
            f"### ⚠️ Low-confidence\n\n{bucket}\n"
        )
        c = vp.Context(body=b, body_lines=b.splitlines(), pr=None, repo=None,
                       diff_files=["content/docs/x.md"], diff_files_added=set(),
                       diff_text="", repo_root=Path("."), is_blog=False)
        return [f"{v.rule_id}@{v.line_ref}" for v in vp.check_trail_bucket_consistency(c)]

    flagged_low = _viols(
        "- L10 \"theory before the task\" → 🚩 flagged (readthrough: purpose-mismatch)",
        "- **[L10]** `content/docs/x.md` \"theory before the task\" — recommend splitting; routed to a follow-up.")
    check("trail-verdict-bucket-promotion@L10" not in flagged_low,
          f"flagged in ⚠️ Low-confidence is accepted (violations: {flagged_low})")

    contra_low = _viols(
        "- L10 \"costs $5\" → ❌ contradicted (source says $9)",
        "- **[L10]** `content/docs/x.md` \"costs $5\" — source says $9.")
    check("trail-verdict-bucket-promotion@L10" in contra_low,
          f"contradicted in ⚠️ Low-confidence still violates (violations: {contra_low})")

    print(f"\n{len(_fails)} failure(s)")
    return 1 if _fails else 0


if __name__ == "__main__":
    sys.exit(main())
