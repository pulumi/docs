"""Tests for the generated-from-data source-discipline gate (rule 3).

pulumi/docs#20349 put four hard rules in the verifier prompt after a ledger
re-adjudication found 17 of 22 `contradicted` verdicts were false. Rule 3 —
"a generated-from-data page transcribes product metadata; disagreement with the
external framework it cites is upstream feedback, not a doc contradiction" —
turned out to be advisory in practice: a 2026-07-24 model sweep found every Opus
configuration flagged 5-6 of 12 policy-pack claims `contradicted` against
Sonnet's 1 of 12, and the rate did not move with reasoning effort. The gate makes
the downgrade deterministic so the rule survives a model change.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

SPEC = importlib.util.spec_from_file_location(
    "verify_claims", Path(__file__).parent / "verify-claims.py")
vc = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(vc)

REPO_ROOT = Path(__file__).resolve().parents[4]
GENERATED = "content/docs/reference/pre-built-policy-packs/cis-aws.md"
AUTHORED = "content/docs/iac/concepts/stacks/_index.md"


def _finalize(file_path, verdict, repo_root=REPO_ROOT):
    return vc._finalize_verdict(
        {"file": file_path, "text": "t", "line_range": "L1", "type": "numerical"},
        "pass3",
        {"verdict": verdict, "confidence": "high",
         "evidence": "CIS 4.2 says otherwise.", "source": "https://cisecurity.org/x"},
        vc._zero_usage(), 1, repo_root)


def test_marker_discovers_the_generated_sections():
    roots = vc._generated_content_roots(REPO_ROOT)
    assert "content/docs/reference/pre-built-policy-packs" in roots, roots


def test_contradicted_on_generated_page_is_downgraded():
    rec = _finalize(GENERATED, "contradicted")
    assert rec["verdict"] == "unverifiable"
    assert rec["source_discipline_gate"] == "generated-from-data"
    assert rec["confidence"] == "low"
    # The model's reasoning survives so the upstream concern still reaches the
    # reviewer — the gate reclassifies, it does not silence.
    assert "CIS 4.2 says otherwise." in rec["evidence"]
    assert "source-discipline gate" in rec["evidence"]


def test_non_contradicted_verdicts_pass_through_untouched():
    # `mismatch` is how the verifier reports a transcription that disagrees with
    # its OWN data file — a real doc bug the gate must not swallow.
    for verdict in ("verified", "matches", "mismatch", "unverifiable", "not-a-claim"):
        rec = _finalize(GENERATED, verdict)
        assert rec["verdict"] == verdict
        assert "source_discipline_gate" not in rec


def test_authored_pages_keep_contradicted():
    rec = _finalize(AUTHORED, "contradicted")
    assert rec["verdict"] == "contradicted"
    assert "source_discipline_gate" not in rec
    assert not rec["evidence"].startswith("[source-discipline gate")


def test_gate_is_inert_without_a_repo_root():
    # The dry-run / degraded paths finalize without a repo root; the gate must
    # not fire on a path it cannot classify.
    rec = _finalize(GENERATED, "contradicted", repo_root=None)
    assert rec["verdict"] == "contradicted"


def test_unknown_paths_are_not_gated():
    for path in ("", "content/blog/some-post.md", "data/policy_pack_policies/cis-aws.json"):
        assert vc._is_generated_from_data(path, REPO_ROOT) is False


def test_sibling_prefix_does_not_false_match():
    # A path that merely *starts with* a generated root's name is not inside it.
    assert vc._is_generated_from_data(
        "content/docs/reference/pre-built-policy-packs-overview.md", REPO_ROOT) is False
