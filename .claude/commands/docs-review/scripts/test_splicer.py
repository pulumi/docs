#!/usr/bin/env python3
"""Unit tests for splicer.py.

Self-contained — run with `python3 test_splicer.py` (no pytest dep).
Imports the splicer module directly and exercises `apply_splices()` so the
splice functions are testable in isolation, without shelling out / writing
to disk.

One test per rule_id in SURGICAL_RULES, plus orchestration tests for the
empty / non-surgical / mixed cases.
"""

from __future__ import annotations

import importlib.util
import sys
import traceback
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPLICER_PATH = HERE / "splicer.py"

_spec = importlib.util.spec_from_file_location("splicer", SPLICER_PATH)
splicer = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(splicer)  # type: ignore[union-attr]


def _trail_section(*lines: str) -> str:
    return "### 🔍 Verification trail\n\n" + "\n".join(lines) + "\n"


# ---- Individual rule tests --------------------------------------------------


def test_internal_link_existence_unwraps_markdown_link():
    body = (
        "Some prose with a [broken link](/docs/missing/page/) inline.\n"
        "Another paragraph.\n"
    )
    violation = {
        "rule_id": "internal-link-existence",
        "line_ref": "<body>",
        "expected": "link /docs/missing/page/ resolves to a file or alias under content/",
        "actual": "no matching file or alias",
        "hint": "Either fix the link target, add an alias, or remove the link.",
    }
    new_body, applied, fallback = splicer.apply_splices(body, [violation])
    assert "broken link" in new_body and "(/docs/missing/page/)" not in new_body, new_body
    assert applied == ["internal-link-existence"], applied
    assert fallback == [], fallback


def test_shortcode_existence_deletes_line():
    body = "Before.\n{{< notashortcode foo=\"bar\" >}}\nAfter.\n"
    violation = {
        "rule_id": "shortcode-existence",
        "line_ref": "<body>",
        "expected": "shortcode `{{< notashortcode >}}` has a layout under layouts/shortcodes/",
        "actual": "no matching layout file",
        "hint": "Either fix the shortcode name or add the corresponding layout file.",
    }
    new_body, applied, fallback = splicer.apply_splices(body, [violation])
    assert "notashortcode" not in new_body, new_body
    assert "Before." in new_body and "After." in new_body
    assert applied == ["shortcode-existence"]
    assert fallback == []


def test_mandatory_h3_order_inserts_missing_section():
    body = (
        "### 🔍 Verification trail\n\n"
        "_No verifiable claims._\n\n"
        "### 🚨 Outstanding in this PR\n\n"
        "_No outstanding findings in this PR._\n"
    )
    violation = {
        "rule_id": "mandatory-h3-order",
        "line_ref": "<### 📊 Editorial balance>",
        "expected": "`### 📊 Editorial balance` present after the previously-rendered mandatory section",
        "actual": "missing or out-of-order",
        "hint": "Render `### 📊 Editorial balance` in the spec order.",
    }
    new_body, applied, fallback = splicer.apply_splices(body, [violation])
    assert "📊 Editorial balance" in new_body, new_body
    # Must sit between Verification trail and Outstanding.
    eb_idx = new_body.index("📊 Editorial balance")
    out_idx = new_body.index("🚨 Outstanding")
    trail_idx = new_body.index("🔍 Verification trail")
    assert trail_idx < eb_idx < out_idx
    assert applied == ["mandatory-h3-order"]


def test_mandatory_h3_order_defers_when_already_present():
    """If the section exists but in the wrong position, splicer defers to fallback."""
    body = (
        "### 📊 Editorial balance\n\n_Single-subject post; balance check N/A._\n\n"
        "### 🔍 Verification trail\n\n_No verifiable claims._\n"
    )
    violation = {
        "rule_id": "mandatory-h3-order",
        "line_ref": "<### 📊 Editorial balance>",
        "expected": "out of order",
        "actual": "out of order",
        "hint": "",
    }
    new_body, applied, fallback = splicer.apply_splices(body, [violation])
    assert new_body == body
    assert "mandatory-h3-order" in fallback


def test_trail_per_verdict_emoji_replaces_legacy_glyph():
    body = _trail_section(
        '- L42 in `content/foo.md` "Some claim text" → ⚠️ unverifiable (source: ...)',
    )
    violation = {
        "rule_id": "trail-per-verdict-emoji",
        "line_ref": "L42",
        "expected": "trail line for L42 renders `🤷` for verdict `unverifiable`",
        "actual": "renders `⚠️` (legacy bucket emoji)",
        "hint": "Render `🤷 unverifiable` on this trail line.",
    }
    new_body, applied, fallback = splicer.apply_splices(body, [violation])
    assert "→ 🤷 unverifiable" in new_body, new_body
    assert "⚠️ unverifiable" not in new_body, new_body
    assert applied == ["trail-per-verdict-emoji"]


def test_trail_canonical_verdict_word_replaces_freelanced_token():
    body = _trail_section(
        '- L7 "Quoted claim" → ✅ author-claim (evidence pointer here)',
    )
    violation = {
        "rule_id": "trail-canonical-verdict-word",
        "line_ref": "L7",
        "expected": "trail verdict is one of the canonical six",
        "actual": "renders non-canonical verdict token `author-claim` (after `✅`)",
        "hint": "Replace the verdict token `author-claim` with `verified`.",
    }
    new_body, applied, fallback = splicer.apply_splices(body, [violation])
    assert "→ ✅ verified" in new_body, new_body
    assert "author-claim" not in new_body, new_body
    assert applied == ["trail-canonical-verdict-word"]


def test_verified_claims_trail_faithful_restores_artifact_verdict():
    body = _trail_section(
        '- L42-58 in `content/foo.md` "Claim X" → ✅ verified (source: ...)',
    )
    violation = {
        "rule_id": "verified-claims-trail-faithful",
        "line_ref": "L42-L58",
        "expected": "trail matches artifact verdict `contradicted`",
        "actual": "trail says `verified`; artifact says `contradicted` — evidence: ...",
        "hint": "Render the trail line for L42-L58 as `❌ contradicted` with the artifact's...",
    }
    new_body, applied, fallback = splicer.apply_splices(body, [violation])
    assert "→ ❌ contradicted" in new_body, new_body
    assert "→ ✅ verified" not in new_body, new_body
    # Claim text and source pointer must remain.
    assert '"Claim X"' in new_body
    assert "(source: ...)" in new_body
    assert applied == ["verified-claims-trail-faithful"]


def test_verified_claims_trail_faithful_matches_by_range_overlap():
    """Artifact says L42-L58, trail anchor is L42 — overlap, not exact match."""
    body = _trail_section(
        '- L42 in `content/foo.md` "Claim Y" → ✅ verified (source: ...)',
    )
    violation = {
        "rule_id": "verified-claims-trail-faithful",
        "line_ref": "L42-L58",  # range; trail anchor is single-line L42
        "expected": "trail matches artifact verdict `contradicted`",
        "actual": "trail says `verified`; artifact says `contradicted` — evidence: ...",
        "hint": "Render the trail line for L42-L58 as `❌ contradicted` with the artifact's...",
    }
    new_body, applied, fallback = splicer.apply_splices(body, [violation])
    assert "→ ❌ contradicted" in new_body, new_body
    assert applied == ["verified-claims-trail-faithful"]


def test_pass3_unverifiable_evidence_inserts_pointer():
    body = _trail_section(
        '- L88 "Some Pass 3 claim" → 🤷 unverifiable (framing: ok; evidence: insufficient)',
    )
    violation = {
        "rule_id": "pass-3-unverifiable-evidence",
        "line_ref": "<🔍 Verification trail: L88 in `content/foo.md`>",
        "expected": "trail line carries a search-was-run negative-evidence pointer",
        "actual": "trail line lacks pointer — ...",
        "hint": (
            'Find the trail line under ### 🔍 Verification trail starting with `- L88 ...` '
            'that quotes the claim text beginning `Some Pass 3 claim` (the line\'s verdict is 🤷 unverifiable). '
            "The line ends with a `)` ... Insert `; WebSearch ran query for source: ...` "
            "immediately before that closing `)` — preserve the rest of the parenthetical verbatim."
        ),
    }
    new_body, applied, fallback = splicer.apply_splices(body, [violation])
    assert "WebSearch ran query for source:" in new_body, new_body
    # Pointer must sit before the closing `)`.
    assert new_body.rstrip().endswith(")")
    assert applied == ["pass-3-unverifiable-evidence"]


def test_external_claim_state_format_defers_to_fallback():
    """No deterministic source for V/N/M integers — splicer defers."""
    body = (
        "<details>\n"
        "<summary>Investigation log</summary>\n\n"
        "- **External claim verification:** ran (some non-canonical state)\n"
        "</details>\n"
    )
    violation = {
        "rule_id": "external-claim-state-format",
        "line_ref": "<investigation log: External claim verification>",
        "expected": "canonical `X of Y claims verified` state form",
        "actual": "- **External claim verification:** ran (some non-canonical state)",
        "hint": "Render the bullet as `X of Y claims verified (N unverifiable, M contradicted) ...`",
    }
    new_body, applied, fallback = splicer.apply_splices(body, [violation])
    assert new_body == body
    assert "external-claim-state-format" in fallback


def test_external_claim_dispatch_metadata_appends_segment():
    body = (
        "- **External claim verification:** 3 of 5 claims verified (1 unverifiable, 1 contradicted).\n"
    )
    violation = {
        "rule_id": "external-claim-dispatch-metadata",
        "line_ref": "<investigation log: External claim verification>",
        "expected": "line includes specialists segment",
        "actual": "- **External claim verification:** 3 of 5 claims verified (1 unverifiable, 1 contradicted).",
        "hint": (
            "Append the extraction dispatch metadata to the External claim verification bullet: "
            "e.g., `· 4 specialists (numerical, cross-reference, capability, framing); 2 cross-specialist corroborations`."
        ),
    }
    new_body, applied, fallback = splicer.apply_splices(body, [violation])
    assert "4 specialists" in new_body
    assert "cross-specialist corroborations" in new_body, new_body
    assert applied == ["external-claim-dispatch-metadata"]


def test_external_claim_routed_metadata_appends_segment():
    body = (
        "- **External claim verification:** 3 of 5 claims verified (1 unverifiable, 1 contradicted) "
        "· 4 specialists (numerical, cross-reference, capability, framing); 2 cross-specialist corroborations.\n"
    )
    violation = {
        "rule_id": "external-claim-routed-metadata",
        "line_ref": "<investigation log: External claim verification>",
        "expected": "line includes routed-verification segment",
        "actual": body.strip(),
        "hint": (
            "Append the routed-verification metadata to the External claim verification bullet: "
            "e.g., `· routed: 2 inline, 1 Pass 1, 2 Pass 2`."
        ),
    }
    new_body, applied, fallback = splicer.apply_splices(body, [violation])
    assert "routed: 2 inline, 1 Pass 1, 2 Pass 2" in new_body, new_body
    assert applied == ["external-claim-routed-metadata"]


def test_external_claim_pass2_outcome_drops_zero_parenthetical():
    body = (
        "- **External claim verification:** 1 of 3 claims verified (1 unverifiable, 1 contradicted) "
        "· 4 specialists (numerical, cross-reference, capability, framing); 0 cross-specialist corroborations "
        "· routed: 2 inline, 1 Pass 1, 0 Pass 2 (verified 0, contradicted 0, unverifiable 0).\n"
    )
    violation = {
        "rule_id": "external-claim-pass2-outcome",
        "line_ref": "<investigation log: External claim verification>",
        "expected": "omit `(verified V, contradicted C, unverifiable U)` when Pass 2 count is 0",
        "actual": body.strip(),
        "hint": "Drop the V/C/U parenthetical from `0 Pass 2`.",
    }
    new_body, applied, fallback = splicer.apply_splices(body, [violation])
    assert "0 Pass 2 (verified" not in new_body
    assert "0 Pass 2" in new_body
    assert applied == ["external-claim-pass2-outcome"]


def test_external_claim_pass2_outcome_defers_when_f_positive():
    body = (
        "- **External claim verification:** 3 of 5 claims verified (1 unverifiable, 1 contradicted) "
        "· 4 specialists (...); 2 cross-specialist corroborations "
        "· routed: 2 inline, 1 Pass 1, 2 Pass 2.\n"
    )
    violation = {
        "rule_id": "external-claim-pass2-outcome",
        "line_ref": "<investigation log: External claim verification>",
        "expected": "`Pass 2` segment carries `(verified V, contradicted C, unverifiable U)` when F > 0 (here F = 2)",
        "actual": body.strip(),
        "hint": "Append the Pass 2 outcome attribution: e.g., `2 Pass 2 (verified V, contradicted C, unverifiable U)` where V + C + U = 2.",
    }
    new_body, applied, fallback = splicer.apply_splices(body, [violation])
    assert new_body == body
    assert "external-claim-pass2-outcome" in fallback


def test_bucket_bullet_line_range_prefix_prepends_anchor():
    body = (
        "### 🔍 Verification trail\n\n"
        '- L42 in `content/foo.md` "The disputed phrase" → ❌ contradicted (source: ...)\n\n'
        "### 🚨 Outstanding in this PR\n\n"
        "- **Spurious:** The author wrote \"The disputed phrase\" which we flagged.\n"
    )
    violation = {
        "rule_id": "bucket-bullet-line-range-prefix",
        "line_ref": "<🚨 Outstanding bullet>",
        "expected": "bullet starts with `- **[L<start>-<end>]**`",
        "actual": "- **Spurious:** The author wrote \"The disputed phrase\" which we flagged.",
        "hint": "Add the `**[L<start>-<end>]**` prefix matching the corresponding 🔍 Verification trail record.",
    }
    new_body, applied, fallback = splicer.apply_splices(body, [violation])
    assert "**[L42]**" in new_body, new_body
    # Original bold prefix `**Spurious:**` should be replaced. Pick the bucket
    # bullet (the line that has "The author wrote") to avoid colliding with the
    # trail line, which quotes the same phrase.
    bullet_line = next(ln for ln in new_body.splitlines() if "The author wrote" in ln)
    assert bullet_line.lstrip().startswith("- **[L42]**"), bullet_line
    assert "Spurious" not in bullet_line, bullet_line
    assert applied == ["bucket-bullet-line-range-prefix"]


# ---- Orchestration tests ---------------------------------------------------


def test_empty_violations_no_op():
    body = "anything"
    new_body, applied, fallback = splicer.apply_splices(body, [])
    assert new_body == body
    assert applied == []
    assert fallback == []


def test_non_surgical_only_passes_through():
    body = "anything"
    violations = [
        {"rule_id": "candidate-claims-coverage", "line_ref": "<body>", "expected": "", "actual": "", "hint": ""},
        {"rule_id": "summary-paragraph-present", "line_ref": "<body>", "expected": "", "actual": "", "hint": ""},
    ]
    new_body, applied, fallback = splicer.apply_splices(body, violations)
    assert new_body == body
    assert applied == []
    assert fallback == []


def test_mixed_surgical_and_nonsurgical_applies_surgical():
    body = "A [broken](/docs/x/) link.\n"
    violations = [
        {
            "rule_id": "internal-link-existence",
            "line_ref": "<body>",
            "expected": "link /docs/x/ resolves to a file or alias under content/",
            "actual": "no matching file or alias",
            "hint": "",
        },
        {"rule_id": "candidate-claims-coverage", "line_ref": "<body>", "expected": "", "actual": "", "hint": ""},
    ]
    new_body, applied, fallback = splicer.apply_splices(body, violations)
    assert "(/docs/x/)" not in new_body
    assert "broken" in new_body
    assert applied == ["internal-link-existence"]
    assert fallback == []


def test_apply_order_processes_trail_faithful_before_per_verdict_emoji():
    """If both verified-claims-trail-faithful and trail-per-verdict-emoji target
    the same line, the artifact-faithful splice should run first; the per-verdict-
    emoji splice then finds the emoji already correct."""
    body = _trail_section(
        '- L10 "Claim text" → ✅ verified (source: ...)',
    )
    violations = [
        {
            "rule_id": "trail-per-verdict-emoji",
            "line_ref": "L10",
            "expected": "trail line for L10 renders `❌` for verdict `contradicted`",
            "actual": "renders `✅` (legacy bucket emoji)",
            "hint": "",
        },
        {
            "rule_id": "verified-claims-trail-faithful",
            "line_ref": "L10",
            "expected": "trail matches artifact verdict `contradicted`",
            "actual": "trail says `verified`; artifact says `contradicted` — evidence: ...",
            "hint": "Render the trail line for L10 as `❌ contradicted` with the artifact's...",
        },
    ]
    new_body, applied, fallback = splicer.apply_splices(body, violations)
    # Final state: emoji+word are ❌ contradicted (artifact verdict).
    assert "→ ❌ contradicted" in new_body, new_body
    # Both rules ran; the second one was a no-op against the already-correct
    # emoji but counts as applied because the splicer's "applied" set is
    # per-rule based on success across violations.
    assert "verified-claims-trail-faithful" in applied


# ---- Test runner -----------------------------------------------------------


TESTS = [
    test_internal_link_existence_unwraps_markdown_link,
    test_shortcode_existence_deletes_line,
    test_mandatory_h3_order_inserts_missing_section,
    test_mandatory_h3_order_defers_when_already_present,
    test_trail_per_verdict_emoji_replaces_legacy_glyph,
    test_trail_canonical_verdict_word_replaces_freelanced_token,
    test_verified_claims_trail_faithful_restores_artifact_verdict,
    test_verified_claims_trail_faithful_matches_by_range_overlap,
    test_pass3_unverifiable_evidence_inserts_pointer,
    test_external_claim_state_format_defers_to_fallback,
    test_external_claim_dispatch_metadata_appends_segment,
    test_external_claim_routed_metadata_appends_segment,
    test_external_claim_pass2_outcome_drops_zero_parenthetical,
    test_external_claim_pass2_outcome_defers_when_f_positive,
    test_bucket_bullet_line_range_prefix_prepends_anchor,
    test_empty_violations_no_op,
    test_non_surgical_only_passes_through,
    test_mixed_surgical_and_nonsurgical_applies_surgical,
    test_apply_order_processes_trail_faithful_before_per_verdict_emoji,
]


def main() -> int:
    failures: list[tuple[str, str]] = []
    for t in TESTS:
        name = t.__name__
        try:
            t()
            print(f"  ok  {name}")
        except AssertionError as e:
            failures.append((name, str(e) or "assertion failed"))
            print(f"  FAIL {name}: {e}")
        except Exception:
            failures.append((name, traceback.format_exc()))
            print(f"  ERROR {name}:\n{traceback.format_exc()}")
    print()
    if failures:
        print(f"{len(failures)}/{len(TESTS)} tests failed")
        return 1
    print(f"{len(TESTS)}/{len(TESTS)} tests passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
