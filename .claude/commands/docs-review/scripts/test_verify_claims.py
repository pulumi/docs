#!/usr/bin/env python3
"""Tests for verify-claims.py's advisor-tool integration — tool wiring, beta
header gating, advisor usage accounting, and the pause_turn resume path.

Self-contained: `python3 test_verify_claims.py`. Imports the hyphenated script
by path (its main() is guarded under __main__, so importing has no side effects).
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


vc = _load("verify_claims", "verify-claims.py")

_fails: list[str] = []


def check(cond: bool, msg: str) -> None:
    print(("ok   " if cond else "FAIL ") + msg)
    if not cond:
        _fails.append(msg)


def _verify_claim_block(verdict: str = "verified") -> dict:
    return {"type": "tool_use", "id": "t1", "name": "verify_claim",
            "input": {"verdict": verdict, "confidence": "high",
                      "evidence": "quote", "source": "repo:path"}}


def main() -> int:
    claim = {"__id": "c1", "file": "content/docs/x.md", "line_range": "L1",
             "type": "entity-spec", "text": "pulumi up supports --diff"}

    # --- tools_for_route wiring ---
    t1 = vc.tools_for_route("pass1", "claude-opus-4-8")
    check(any(t.get("name") == "advisor" for t in t1), "pass1 + advisor model carries the advisor tool")
    check(t1[-1]["type"] == "advisor_20260301" and t1[-1]["max_tokens"] == vc.ADVISOR_MAX_TOKENS,
          "advisor tool shape: type + max_tokens cap")
    t3 = vc.tools_for_route("pass3", "claude-opus-4-8")
    check(any(t.get("name") == "advisor" for t in t3), "pass3 + advisor model carries the advisor tool")
    check(not any(t.get("name") == "advisor" for t in vc.tools_for_route("pass2", "claude-opus-4-8")),
          "pass2 never carries the advisor tool")
    check(not any(t.get("name") == "advisor" for t in vc.tools_for_route("pass1", "")),
          "empty advisor model disables the tool")
    check(vc.tools_for_route("pass1") == [vc.GH_QUERY_TOOL, vc.READ_FILE_TOOL, vc.VERIFY_CLAIM_TOOL],
          "pass1 default (no advisor arg) matches the pre-advisor tool list")

    # --- beta header gating ---
    check(vc._betas_for_body({"tools": t1}) == vc.ADVISOR_BETA, "advisor tool in body -> beta header")
    check(vc._betas_for_body({"tools": vc.tools_for_route("pass2")}) == "", "pass2 body -> no beta header")
    check(vc._betas_for_body({}) == "", "toolless body -> no beta header")

    # --- _accumulate_usage: iterations with an advisor_message ---
    agg = vc._zero_usage()
    vc._accumulate_usage(agg, {
        "input_tokens": 412, "output_tokens": 531,
        "cache_read_input_tokens": 0, "cache_creation_input_tokens": 0,
        "iterations": [
            {"type": "message", "input_tokens": 412, "output_tokens": 89,
             "cache_read_input_tokens": 0, "cache_creation_input_tokens": 0},
            {"type": "advisor_message", "model": "claude-opus-4-8",
             "input_tokens": 823, "output_tokens": 612,
             "cache_read_input_tokens": 0, "cache_creation_input_tokens": 0},
            {"type": "message", "input_tokens": 1348, "output_tokens": 442,
             "cache_read_input_tokens": 412, "cache_creation_input_tokens": 0},
        ],
    })
    check(agg["input_tokens"] == 412 + 1348, "executor input summed from iterations only")
    check(agg["output_tokens"] == 89 + 442, "executor output excludes advisor tokens")
    check(agg["advisor_input_tokens"] == 823 and agg["advisor_output_tokens"] == 612,
          "advisor tokens tracked under advisor_* keys")
    check(agg["advisor_calls"] == 1, "advisor call counted")
    check(agg["cache_read_input_tokens"] == 412, "executor cache reads summed")

    # --- _accumulate_usage: legacy shape (no iterations) unchanged ---
    agg2 = vc._zero_usage()
    vc._accumulate_usage(agg2, {"input_tokens": 10, "output_tokens": 20,
                                "cache_read_input_tokens": 3, "cache_creation_input_tokens": 4})
    check(agg2["input_tokens"] == 10 and agg2["output_tokens"] == 20 and agg2["advisor_calls"] == 0,
          "no-iterations usage falls back to top-level fields")

    # --- run_verifier: pause_turn resume, advisor round-trip, verdict finalize ---
    calls: list[dict] = []
    responses = [
        {   # turn 1: executor calls advisor; response pauses with a dangling call
            "stop_reason": "pause_turn",
            "content": [{"type": "text", "text": "consulting"},
                        {"type": "server_tool_use", "id": "srv1", "name": "advisor", "input": {}}],
            "usage": {"input_tokens": 100, "output_tokens": 10,
                      "cache_read_input_tokens": 0, "cache_creation_input_tokens": 0},
        },
        {   # resume: advisor result arrives, executor emits the verdict
            "stop_reason": "end_turn",
            "content": [{"type": "advisor_tool_result", "tool_use_id": "srv1",
                         "content": {"type": "advisor_result", "text": "check the release notes"}},
                        _verify_claim_block()],
            "usage": {"input_tokens": 100, "output_tokens": 50,
                      "cache_read_input_tokens": 0, "cache_creation_input_tokens": 0,
                      "iterations": [
                          {"type": "advisor_message", "model": "claude-opus-4-8",
                           "input_tokens": 900, "output_tokens": 400,
                           "cache_read_input_tokens": 0, "cache_creation_input_tokens": 0},
                          {"type": "message", "input_tokens": 100, "output_tokens": 50,
                           "cache_read_input_tokens": 0, "cache_creation_input_tokens": 0},
                      ]},
        },
    ]

    def fake_post(api_key: str, body: dict) -> dict:
        calls.append(body)
        return responses[len(calls) - 1]

    orig_post = vc._post_messages
    vc._post_messages = fake_post
    try:
        rec = vc.run_verifier("key", dict(claim), "pass1", None, "claude-sonnet-5",
                              HERE, False, advisor_model="claude-opus-4-8")
    finally:
        vc._post_messages = orig_post

    check(rec["verdict"] == "verified", "pause_turn path still finalizes the verdict")
    check(rec["model_usage"]["turns"] == 2, "turns records both API round-trips")
    check(rec["model_usage"]["advisor_calls"] == 1 and rec["model_usage"]["advisor_input_tokens"] == 900,
          "advisor usage lands in model_usage")
    check(len(calls) == 2, "pause_turn resumed with a second request")
    resume_msgs = calls[1]["messages"]
    check(resume_msgs[-1]["role"] == "assistant"
          and any(b.get("type") == "server_tool_use" for b in resume_msgs[-1]["content"]),
          "resume re-sends the dangling assistant turn verbatim (no user nudge)")
    check(any(t.get("name") == "advisor" for t in calls[1]["tools"]),
          "advisor tool stays in tools on the resume request")
    check(vc.ADVISOR_ROUTE_NOTE.strip() in calls[0]["system"][1]["text"],
          "route header carries the advisor guidance")
    check(vc.ADVISOR_BREVITY_NOTE in calls[0]["messages"][0]["content"],
          "user message carries the advisor brevity note")

    # --- run_verifier with advisor disabled: no advisor artifacts ---
    calls.clear()
    responses[:] = [{
        "stop_reason": "end_turn",
        "content": [_verify_claim_block()],
        "usage": {"input_tokens": 50, "output_tokens": 20,
                  "cache_read_input_tokens": 0, "cache_creation_input_tokens": 0},
    }]
    vc._post_messages = fake_post
    try:
        rec2 = vc.run_verifier("key", dict(claim), "pass1", None, "claude-sonnet-5",
                               HERE, False, advisor_model="")
    finally:
        vc._post_messages = orig_post
    check(rec2["verdict"] == "verified", "advisor-disabled run still verifies")
    check(not any(t.get("name") == "advisor" for t in calls[0]["tools"]),
          "advisor disabled -> tool absent from request")
    check(vc._betas_for_body(calls[0]) == "", "advisor disabled -> no beta header")
    check("advisor" not in calls[0]["system"][1]["text"], "advisor disabled -> no route-note text")
    check(vc.ADVISOR_BREVITY_NOTE not in calls[0]["messages"][0]["content"],
          "advisor disabled -> no brevity note")

    # --- dry-run untouched ---
    rec3 = vc.run_verifier("key", dict(claim), "pass1", None, "claude-sonnet-5",
                           HERE, True, advisor_model="claude-opus-4-8")
    check(rec3["source"] == "dry-run" and rec3["model_usage"]["advisor_calls"] == 0,
          "dry-run emits placeholder with zero advisor usage")

    print()
    if _fails:
        print(f"{len(_fails)} failure(s)")
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
