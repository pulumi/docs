#!/usr/bin/env python3
"""Editorial stances get a home: extracted, never verified, listed verdict-free.

PR #21291 (2026-09-01) shipped "`pulumi convert` is the fastest path for most
configurations, and it's where to start" — an agent-written positioning
claim — and nothing in the pre-merge review surfaced the word. Positioning /
comparison records now leave the verifier's input (`merge-claims.py` schema
v2 `stances`), render under ⚠️ as "Editorial stances introduced by this PR"
with no verdict (`compose-review.py`), and `validate-pinned.py`'s
`editorial-stances-coverage` holds that list to the artifact both ways.

Self-contained: `python3 test_editorial_stances.py`, also collected by pytest.
"""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


cr = _load("compose_review", "compose-review.py")
vp = _load("validate_pinned", "validate-pinned.py")

_fails: list[str] = []


def check(cond: bool, msg: str) -> None:
    print(("ok   " if cond else "FAIL ") + msg)
    if not cond:
        _fails.append(msg)


FILE = "content/docs/iac/guides/migration/convert-hcl.md"
LINE = ("`pulumi convert` is the fastest path for most configurations, and it's where to start. "
        "The [Pulumi MCP server](/docs/ai/mcp-server/) gives the agent access to the Pulumi Registry.")


def _pipeline(tmp: Path) -> dict:
    """extract-claims -> merge-claims over a diff introducing the sentence."""
    patch = (f"diff --git a/{FILE} b/{FILE}\n--- a/{FILE}\n+++ b/{FILE}\n"
             f"@@ -1226,0 +1226,1 @@\n+{LINE}\n")
    (tmp / "p.patch").write_text(patch)
    regex = tmp / "regex.json"
    r = subprocess.run([sys.executable, str(HERE / "extract-claims.py"), "--patch-file", str(tmp / "p.patch"),
                        "--out", str(regex)], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    llm = tmp / "llm.json"
    llm.write_text(json.dumps({"schema_version": 1, "pass": "atomic", "model": "x", "claims": [
        {"file": FILE, "line_range": "L1226", "type": "capability", "confidence": "medium",
         "found_by": ["llm-atomic"],
         "text": "The Pulumi MCP server gives the agent access to the Pulumi Registry."}],
        "errors": [], "meta": {"input_tokens": 1, "output_tokens": 1,
                               "cache_read_input_tokens": 0, "cache_creation_input_tokens": 0}}))
    out = tmp / "merged.json"
    r = subprocess.run([sys.executable, str(HERE / "merge-claims.py"), "--regex", str(regex), "--llm", str(llm),
                        "--out", str(out), "--repo-root", str(tmp)], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    return json.loads(out.read_text())


def _clean(name: str, before: int) -> None:
    new = _fails[before:]
    assert not new, f"{name}: {new}"


def test_stances_leave_the_verifier_input() -> None:
    before = len(_fails)
    with tempfile.TemporaryDirectory() as td:
        merged = _pipeline(Path(td))
    check(merged["schema_version"] == 2, "merge-claims writes schema v2")
    check(all(c["type"] not in ("positioning", "comparison") for c in merged["claims"]),
          f"no positioning/comparison record in `claims` (verifier input); got {[c['type'] for c in merged['claims']]}")
    stances = merged["stances"]
    check(len(stances) == 1 and stances[0]["type"] == "positioning" and "fastest path" in stances[0]["text"],
          f"the 'fastest path' sentence is one positioning stance; got {stances}")
    check(stances[0]["line_range"] == "L1226" and stances[0]["found_by"] == ["regex"],
          f"the stance keeps its anchor and provenance; got {stances[0]}")
    check(any("regex" in c.get("found_by", []) for c in merged["claims"]),
          "the same line's url record still reaches the verifier (merged into the capability claim)")
    check(merged["meta"]["stances"] == 1, "meta counts the stances")
    _clean("test_stances_leave_the_verifier_input", before)


def test_verifier_skips_stances() -> None:
    before = len(_fails)
    src = (HERE / "verify-claims.py").read_text()
    check("STANCE_TYPES" in src and 'not in STANCE_TYPES' in src,
          "verify-claims.py filters positioning/comparison out of its input")
    _clean("test_verifier_skips_stances", before)


def test_composer_lists_stances_without_a_verdict() -> None:
    before = len(_fails)
    stances = [{"file": FILE, "line_range": "L1226", "text": LINE, "type": "positioning",
                "confidence": "high", "found_by": ["regex"]}]
    block = cr.render_lowconfidence([], [], "", stances)
    check(cr.STANCES_HEADING in block, "the stances H4 renders under ⚠️")
    check("- L1226 `" + FILE + "`" in block and "fastest path" in block and "— positioning (found by regex)" in block,
          f"bullet shape is `- L<n> file — text — type`; got {block!r}")
    for tok in ("✅", "❌", "➖", "🤷", "verdict:", "not-a-claim"):
        check(tok not in block, f"stance rows carry no verdict marker {tok!r}")
    check("**[L" not in block, "stance rows never use the counted bucket-bullet prefix")
    check(not vp.extract_bucket_bullets("### ⚠️ Low-confidence\n\n" + block.split("\n", 1)[1], "⚠️ Low-confidence"),
          "the validator's bucket-bullet counter ignores stance rows")
    # Explicit-empty vs. omitted.
    empty = cr.render_lowconfidence([], [], "", [])
    check(cr.STANCES_EMPTY in empty, "an empty stances list renders the explicit-empty form")
    check(cr.render_lowconfidence([], [], "", None) == "### ⚠️ Low-confidence\n\n_No low-confidence findings._",
          "a pre-v2 artifact (None) leaves the ⚠️ empty form untouched")
    # Ordering: stances before style suggestions.
    both = cr.render_lowconfidence([], [{"file": FILE, "line": 3, "category": "wordiness", "message": "x"}], "", stances)
    check(both.index(cr.STANCES_HEADING) < both.index(cr.STYLE_HEADING),
          "the stances block precedes #### Style suggestions")
    _clean("test_composer_lists_stances_without_a_verdict", before)


def _ctx(body: str, stances) -> "vp.Context":
    return vp.Context(body=body, body_lines=body.splitlines(), pr=None, repo=None, diff_files=[FILE],
                      diff_files_added=set(), diff_text="", repo_root=Path("."), is_blog=False,
                      candidate_stances=stances)


def test_validator_holds_the_list_to_the_artifact() -> None:
    before = len(_fails)
    stances = [{"file": FILE, "line_range": "L1226", "text": LINE, "type": "positioning", "found_by": ["regex"]}]
    good = ("### ⚠️ Low-confidence\n\n*note*\n\n" + cr.render_stances(stances) + "\n\n### 📋 Triaged verifier findings\n")
    check(vp.check_editorial_stances_coverage(_ctx(good, stances)) == [],
          "a body listing every stance verdict-free passes")
    missing = "### ⚠️ Low-confidence\n\n_No low-confidence findings._\n\n### 📋 Triaged verifier findings\n"
    v = vp.check_editorial_stances_coverage(_ctx(missing, stances))
    check(len(v) == 1 and "block absent" in v[0].actual, f"a dropped stance block is a violation; got {v}")
    dropped = good.replace("- L1226", "- L1300")
    v = vp.check_editorial_stances_coverage(_ctx(dropped, stances))
    check(any("no stance bullet covers" in x.actual for x in v)
          and any("has no record" in x.actual for x in v),
          f"a bullet moved off its record is both a dropped record and an unbacked bullet; got {[x.actual for x in v]}")
    verdicted = good.replace("— positioning (found by regex)", "— positioning → ❌ contradicted")
    v = vp.check_editorial_stances_coverage(_ctx(verdicted, stances))
    check(any("carries a verdict marker" in x.actual for x in v), f"a verdict on a stance row is a violation; got {v}")
    # A glyph INSIDE the quoted stance text (a comparison-table row) is the
    # composer rendering the page faithfully, not a verdict.
    table_stances = [{"file": FILE, "line_range": "L40", "text": "| Unlike Terraform | ✅ | ❌ |",
                      "type": "comparison", "found_by": ["regex"]}]
    table_body = ("### ⚠️ Low-confidence\n\n*note*\n\n" + cr.render_stances(table_stances)
                  + "\n\n### 📋 Triaged verifier findings\n")
    check("✅" in table_body and vp.check_editorial_stances_coverage(_ctx(table_body, table_stances)) == [],
          "verdict glyphs inside the quoted stance text are not a verdict on the row")
    # The crash-fallback artifact carries the same meta keys as the success path.
    src = (HERE / "merge-claims.py").read_text()
    check('"merged_claims": 0, "stances": 0,' in src, "merge-claims crash fallback meta carries the stances count")
    check(vp.check_editorial_stances_coverage(_ctx(missing, None)) == [],
          "a pre-v2 artifact (None) skips the rule")
    check(vp.check_editorial_stances_coverage(_ctx(missing, [])) == [],
          "no stances and no block on the body is fine")
    empty_block = ("### ⚠️ Low-confidence\n\n*note*\n\n" + cr.render_stances([]) + "\n\n### 📋 Triaged verifier findings\n")
    check(vp.check_editorial_stances_coverage(_ctx(empty_block, [])) == [],
          "the explicit-empty block with no stances passes")
    check(any(r["id"] == "editorial-stances-coverage" for r in vp.RULES), "the rule is registered")
    _clean("test_validator_holds_the_list_to_the_artifact", before)


def main() -> int:
    for t in (test_stances_leave_the_verifier_input, test_verifier_skips_stances,
              test_composer_lists_stances_without_a_verdict, test_validator_holds_the_list_to_the_artifact):
        print(t.__name__)
        try:
            t()
        except AssertionError as e:
            print(f"FAIL {t.__name__}: {e}", file=sys.stderr)
    if _fails:
        print(f"\n{len(_fails)} failure(s)", file=sys.stderr)
        return 1
    print("\nall editorial-stances tests passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
