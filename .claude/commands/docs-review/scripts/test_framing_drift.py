#!/usr/bin/env python3
"""Tests for the `framing-drift` (🌀) verdict and the turn-cap escalation /
`turn_cap_exhausted` marker — the verify-claims.py harness side, the
compose-review synthesizer side, and the validate-pinned acceptance side.

Self-contained: `python3 test_framing_drift.py`. Imports the hyphenated scripts
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
sp = _load("splicer_mod", "splicer.py")
vc = _load("verify_claims", "verify-claims.py")

_fails: list[str] = []


def check(cond: bool, msg: str) -> None:
    print(("ok   " if cond else "FAIL ") + msg)
    if not cond:
        _fails.append(msg)


CLAIM = {"__id": "c1", "file": "content/blog/x/index.md", "line_range": "L23",
         "text": "66% of organizations are betting on Kubernetes", "type": "numerical"}


def _mock_messages(script):
    """Return a _post_messages replacement that serves canned responses.

    `script` maps a lane key ("pass1" / "pass3") to a list of content blocks
    returned on successive calls to that lane; the last entry repeats. Lane is
    derived from the request's tool names.
    """
    calls = {"pass1": 0, "pass3": 0, "order": []}

    def fake(api_key, body):
        names = {t.get("name") for t in body.get("tools", [])}
        lane = "pass1" if "gh_query" in names else "pass3"
        seq = script[lane]
        i = min(calls[lane], len(seq) - 1)
        calls[lane] += 1
        calls["order"].append(lane)
        return {"content": seq[i], "usage": {"input_tokens": 1, "output_tokens": 1}}

    return fake, calls


def main() -> int:
    # --- registry constants are in sync across the four scripts ---
    for mod, nm in ((cr, "compose-review"), (vp, "validate-pinned")):
        check("framing-drift" in mod.TRAIL_VERDICT_WORDS, f"{nm}: framing-drift in TRAIL_VERDICT_WORDS")
        check(mod.EXPECTED_TRAIL_EMOJI.get("framing-drift") == "🌀", f"{nm}: framing-drift -> 🌀")
    check(sp.EXPECTED_TRAIL_EMOJI.get("framing-drift") == "🌀", "splicer: framing-drift -> 🌀")
    check("framing-drift" in vc.VERDICT_VALUES, "verify-claims: framing-drift is a verdict value")
    check("framing-drift" not in cr.OUTSTANDING_VERDICTS,
          "compose: framing-drift does NOT stub to 🚨 (⚠️ default; reviewer promotes)")
    check("framing-drift" in vp.OUTSTANDING_VERDICT_WORDS, "validate: framing-drift must surface in a bucket")
    check("framing-drift" in vp.SOFT_PROMOTE_VERDICT_WORDS, "validate: framing-drift accepted in ⚠️")
    check("🌀" in vp.OUTSTANDING_TRAIL_EMOJIS, "validate: 🌀 is an outstanding trail emoji")
    check(vc.FRAMING_DRIFT_SHAPES == {"overclaim-broader", "shifted"}, "verify-claims: drift shapes")

    # --- _finalize_verdict coercion: the harness, not the model, places drift ---
    rec = vc._finalize_verdict(CLAIM, "pass3",
                               {"verdict": "verified", "confidence": "high",
                                "evidence": "figure accurate, framing shifts", "source": "https://cncf.io/x",
                                "framing": "shifted"},
                               vc._zero_usage(), 1)
    check(rec["verdict"] == "framing-drift", "verified + shifted coerces to framing-drift")
    check(rec["framing"] == "shifted" and rec.get("framing_note"), "framing carried; framing_note auto-filled")

    rec = vc._finalize_verdict(CLAIM, "pass3",
                               {"verdict": "verified", "confidence": "high", "evidence": "e", "source": "s",
                                "framing": "entailed-narrower"},
                               vc._zero_usage(), 1)
    check(rec["verdict"] == "verified", "verified + entailed-narrower stays verified")

    rec = vc._finalize_verdict(CLAIM, "pass3",
                               {"verdict": "contradicted", "confidence": "high", "evidence": "e", "source": "s",
                                "framing": "overclaim-broader"},
                               vc._zero_usage(), 1)
    check(rec["verdict"] == "contradicted", "contradicted is never coerced upward")

    # --- turn-cap: pass1 auto-escalates to pass3 instead of dying unverifiable ---
    read_file_turn = [{"type": "tool_use", "id": "t1", "name": "read_file", "input": {"path": "nope.md"}}]
    verify_ok = [{"type": "tool_use", "id": "t9", "name": "verify_claim",
                  "input": {"verdict": "verified", "confidence": "high",
                            "evidence": "found it", "source": "https://example.com"}}]
    fake, calls = _mock_messages({"pass1": [read_file_turn], "pass3": [verify_ok]})
    orig = vc._post_messages
    vc._post_messages = fake
    try:
        rec = vc.run_verifier("k", dict(CLAIM), "pass1", None, "m", HERE, False)
    finally:
        vc._post_messages = orig
    check(calls["pass1"] == vc.MAX_TURNS["pass1"], f"pass1 consumed its full cap ({calls['pass1']} turns)")
    check(rec["route"] == "pass3" and rec["verdict"] == "verified",
          "cap exhaustion escalated to pass3 and converged")
    check(rec["evidence"].startswith("(escalated from pass1 after exhausting"),
          "escalated evidence names the turn-cap hop")

    # --- turn-cap terminal record carries the retryable marker ---
    text_only = [{"type": "text", "text": "hmm"}]
    fake, calls = _mock_messages({"pass1": [text_only], "pass3": [text_only]})
    vc._post_messages = fake
    try:
        rec = vc.run_verifier("k", dict(CLAIM), "pass3", None, "m", HERE, False, allow_escalate=False)
    finally:
        vc._post_messages = orig
    check(rec["verdict"] == "unverifiable" and rec.get("turn_cap_exhausted") is True,
          "terminal cap record carries turn_cap_exhausted: true")
    check("did not converge" in rec["evidence"] and "retryable" in rec["evidence"],
          "terminal cap evidence keeps the canonical phrase and says retryable")

    # --- reverse escalation: pass3 verifier hands a pulumi-behavior claim to pass1 ---
    esc_p3 = [{"type": "tool_use", "id": "t2", "name": "verify_claim",
               "input": {"verdict": "unverifiable", "confidence": "low",
                         "evidence": "web can't read product source", "source": "WebSearch ran query \"x\"",
                         "route_escalation": "pass1"}}]
    p1_ok = [{"type": "tool_use", "id": "t3", "name": "verify_claim",
              "input": {"verdict": "verified", "confidence": "high",
                        "evidence": "defaultMaxAgeDays = 7", "source": "repo:pkg/logging/rotation.go"}}]
    fake, calls = _mock_messages({"pass1": [p1_ok], "pass3": [esc_p3]})
    vc._post_messages = fake
    try:
        rec = vc.run_verifier("k", dict(CLAIM), "pass3", None, "m", HERE, False)
    finally:
        vc._post_messages = orig
    check(rec["route"] == "pass1" and rec["verdict"] == "verified",
          "pass3 -> pass1 escalation reached the gh lane and converged")
    check(rec["evidence"].startswith("(escalated from pass3)"), "reverse-escalation evidence prefix")
    check(calls["order"] == ["pass3", "pass1"], "exactly one hop, no ping-pong")

    # --- composer: framing-drift stubs to ⚠️; turn-cap unverifiable gets retryable TODO ---
    fd = {"verdict": "framing-drift", "confidence": "high", "route": "pass3",
          "file": "content/blog/x/index.md", "line_range": "L23",
          "text": "66% of organizations are betting on Kubernetes",
          "evidence": "source says orgs hosting genAI *use* K8s", "framing_note": "overclaim + shifted"}
    cap_unv = {"verdict": "unverifiable", "confidence": "low", "route": "pass1",
               "file": "content/docs/y.md", "line_range": "L10", "text": "returns 204",
               "evidence": "verification did not converge within 12 turns", "turn_cap_exhausted": True}
    plain_unv = {"verdict": "unverifiable", "confidence": "low", "route": "pass3",
                 "file": "content/docs/y.md", "line_range": "L20", "text": "paywalled stat",
                 "evidence": "page is behind a login wall"}
    outstanding, lowconf = cr.build_stubs([fd, cap_unv, plain_unv])
    check(not outstanding and len(lowconf) == 3, "framing-drift + both unverifiables stub to ⚠️")
    fd_stub = lowconf[0]["bullet"]
    check("framing-drift" in fd_stub and "PROMOTE to 🚨" in fd_stub and "social.*" in fd_stub,
          "framing-drift TODO carries the promotion mandate")
    cap_stub = lowconf[1]["bullet"]
    check("TURN-BUDGET failure" in cap_stub and "out of scope" in cap_stub,
          "turn-cap TODO forbids the out-of-scope narration")
    check("TURN-BUDGET" not in lowconf[2]["bullet"], "ordinary unverifiable keeps the standard TODO")

    # --- trail render + counts: 🌀 glyph; framing-drift counts with contradicted ---
    trail, n, x, y, z = cr.render_trail([fd, cap_unv], None)
    check("🌀 framing-drift" in trail, "trail renders '🌀 framing-drift'")
    check("framing: overclaim + shifted" in trail, "trail pointer leads with the framing note")
    check((n, x, y, z) == (2, 0, 1, 1), f"summary counts framing-drift as contradiction-family (got {(n, x, y, z)})")
    rc = cr.compute_route_counts([fd, cap_unv], None)
    check(rc["pass3_vcu"] == (0, 1, 0), "per-lane V/C/U counts framing-drift under C")

    # --- validator: 🌀 in ⚠️ accepted; hidden 🌀 violates; trail-faithful guards it ---
    def _ctx(body: str, **kw) -> "vp.Context":
        return vp.Context(body=body, body_lines=body.splitlines(), pr=None, repo=None,
                          diff_files=["content/blog/x/index.md"], diff_files_added=set(),
                          diff_text="", repo_root=Path("."), is_blog=True, **kw)

    ok_body = (
        "### 🔍 Verification trail\n\n"
        "- L23 in `content/blog/x/index.md` \"66% of organizations...\" → 🌀 framing-drift (framing: overclaim)\n\n"
        "### 🚨 Outstanding\n\n_No outstanding findings._\n\n"
        "### ⚠️ Low-confidence\n\n"
        "- **[L23]** `content/blog/x/index.md` \"66%...\" — restore the source's framing.\n"
    )
    viols = [f"{v.rule_id}@{v.line_ref}" for v in vp.check_trail_bucket_consistency(_ctx(ok_body))]
    check(not viols, f"validator accepts framing-drift trail + ⚠️ bucket (violations: {viols})")

    hidden_body = (
        "### 🔍 Verification trail\n\n"
        "- L23 in `content/blog/x/index.md` \"66% of organizations...\" → 🌀 framing-drift (framing: overclaim)\n\n"
        "### 🚨 Outstanding\n\n_No outstanding findings._\n\n"
        "### ⚠️ Low-confidence\n\n_No low-confidence findings._\n"
    )
    viols = [v.rule_id for v in vp.check_trail_bucket_consistency(_ctx(hidden_body))]
    check("trail-verdict-bucket-promotion" in viols, "framing-drift with no bucket bullet violates")

    faithful_body = (
        "### 🔍 Verification trail\n\n"
        "- L23 in `content/blog/x/index.md` \"66% of organizations...\" → ✅ verified (all good)\n"
    )
    artifact = [{"claim_id": "c1", "file": "content/blog/x/index.md", "line_range": "L23",
                 "verdict": "framing-drift", "evidence": "e", "route": "pass3"}]
    viols = [v.rule_id for v in vp.check_verified_claims_trail_faithful(_ctx(faithful_body, verified_claims=artifact))]
    check("verified-claims-trail-faithful" in viols,
          "trail hiding an artifact framing-drift behind ✅ is flagged")

    # --- gap 3: the composed header carries the machine-readable head sentinel ---
    hdr = cr.render_header("2026-07-30T00:00:00Z", "abc123def456")
    check("<!-- CLAUDE_REVIEW_HEAD abc123def456 -->" in hdr, "header carries CLAUDE_REVIEW_HEAD sentinel")
    check("CLAUDE_REVIEW_HEAD" not in cr.render_header("2026-07-30T00:00:00Z"),
          "sentinel omitted when the head SHA is unknown")

    print(f"\n{len(_fails)} failure(s)")
    return 1 if _fails else 0


if __name__ == "__main__":
    sys.exit(main())
