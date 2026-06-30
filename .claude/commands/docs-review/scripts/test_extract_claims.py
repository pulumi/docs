#!/usr/bin/env python3
"""Tests for the claim-extraction pre-step: extract-claims.py + merge-claims.py.

Self-contained — run with `python3 test_extract_claims.py` (no pytest dep).
Shells out to the scripts (the same way the workflow does) and asserts on the
JSON they emit. Fixtures in `testdata/` are committed deterministic diffs of
real merged pulumi/docs PRs (#18771, #18743, #18541) — corpus-drawn cases of
the run-to-run-fragile claim shapes the regex floor must guarantee.

(extract-claims-llm.py isn't tested here — it needs ANTHROPIC_API_KEY and is
spike-tested in CI; merge-claims.py is tested against hand-crafted Layer-B
inputs below.)
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXTRACT = HERE / "extract-claims.py"
MERGE = HERE / "merge-claims.py"
TESTDATA = HERE / "testdata"

_failures: list[str] = []
_passes = 0


def check(cond: bool, msg: str) -> None:
    global _passes
    if cond:
        _passes += 1
    else:
        _failures.append(msg)
        print(f"  FAIL: {msg}", file=sys.stderr)


def run_extract(patch_text: str) -> dict:
    with tempfile.TemporaryDirectory() as td:
        pf = Path(td) / "p.patch"
        pf.write_text(patch_text)
        out = Path(td) / "out.json"
        r = subprocess.run([sys.executable, str(EXTRACT), "--patch-file", str(pf), "--out", str(out)],
                           capture_output=True, text=True)
        assert r.returncode == 0, f"extract-claims.py exited {r.returncode}: {r.stderr}"
        return json.loads(out.read_text())


def run_extract_fixture(name: str) -> dict:
    with tempfile.TemporaryDirectory() as td:
        out = Path(td) / "out.json"
        r = subprocess.run([sys.executable, str(EXTRACT), "--patch-file", str(TESTDATA / name), "--out", str(out)],
                           capture_output=True, text=True)
        assert r.returncode == 0, f"extract-claims.py exited {r.returncode}: {r.stderr}"
        return json.loads(out.read_text())


def run_merge(regex: dict, llm_passes: list[dict], repo_root: Path | None = None) -> dict:
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        rp = tdp / "regex.json"
        rp.write_text(json.dumps(regex))
        llm_paths = []
        for i, lp in enumerate(llm_passes, start=1):
            p = tdp / f"llm-{i}.json"
            p.write_text(json.dumps(lp))
            llm_paths.append(str(p))
        out = tdp / "merged.json"
        cmd = [sys.executable, str(MERGE), "--regex", str(rp), "--out", str(out),
               "--repo-root", str(repo_root or tdp)]
        for p in llm_paths:
            cmd += ["--llm", p]
        r = subprocess.run(cmd, capture_output=True, text=True)
        assert r.returncode == 0, f"merge-claims.py exited {r.returncode}: {r.stderr}"
        return json.loads(out.read_text())


def _mk_patch(file_path: str, body_lines: list[str], start_line: int = 10) -> str:
    """Build a minimal unified-diff hunk adding `body_lines` to `file_path`."""
    n = len(body_lines)
    hdr = (
        f"diff --git a/{file_path} b/{file_path}\n"
        f"--- a/{file_path}\n"
        f"+++ b/{file_path}\n"
        f"@@ -{start_line},0 +{start_line},{n} @@\n"
    )
    return hdr + "".join(f"+{ln}\n" for ln in body_lines)


def _texts(doc: dict) -> list[str]:
    return [c["text"] for c in doc["claims"]]


def _types(doc: dict) -> set[str]:
    return {c["type"] for c in doc["claims"]}


# ---- extract-claims.py: synthetic per-category --------------------------------

def test_synthetic_categories() -> None:
    print("test_synthetic_categories")
    d = run_extract(_mk_patch("content/blog/x.md", [
        "The p5.48xlarge instance costs $98.32/hr on-demand.",                       # numerical
        "These programs pin github.com/pulumi/pulumi-gcp/sdk/v8 v8.2.0 in go.mod.",   # version
        "Pulumi recently introduced ESC rotation, now supported for AWS.",            # temporal
        "StrongDM reported roughly $1,000/day per engineer-equivalent.",              # attribution + numerical
        "See [the Trivy docs](https://trivy.dev/latest/) for details.",               # url
        "Llama 3.3 ships as a 32B model variant.",                                    # entity-spec
        "Pulumi is the canonical IaC tool, unlike Terraform.",                        # positioning + comparison
        "Dynamic blocks are not implemented in this provider.",                       # capability
    ]))
    types = _types(d)
    for t in ("numerical", "version", "temporal", "attribution", "url", "entity-spec", "positioning", "comparison", "capability"):
        check(t in types, f"synthetic: expected a `{t}` claim; got types {sorted(types)}")
    # The attributed dollar figure should carry a source_hint of StrongDM.
    attr = [c for c in d["claims"] if c["type"] == "attribution"]
    check(any(c.get("source_hint", "").startswith("StrongDM") for c in attr),
          f"synthetic: attribution claim should have source_hint 'StrongDM'; got {[c.get('source_hint') for c in attr]}")
    # Every regex claim is high-confidence.
    check(all(c["confidence"] == "high" for c in d["claims"]), "synthetic: all regex claims should be confidence=high")


def test_code_context_suppresses_prose() -> None:
    print("test_code_context_suppresses_prose")
    # Inside a fenced code block in a .md file: prose patterns suppressed, but
    # URLs / version pins still extracted.
    d = run_extract(_mk_patch("content/blog/x.md", [
        "```bash",
        "# this is the canonical way, unlike the old approach",   # prose patterns — suppressed in fence
        "pulumi up --stack dev    # see https://example.com/docs", # url — still extracted
        "```",
        "Pulumi is the canonical choice.",                        # prose — extracted (outside fence)
    ]))
    fence_line_claims = [c for c in d["claims"] if c["line_range"] in ("L11", "L12")]
    check(all(c["type"] in ("url", "version", "numerical") for c in fence_line_claims),
          f"fence: expected only url/version/numerical claims inside the fence; got {[(c['line_range'], c['type']) for c in fence_line_claims]}")
    check(any(c["type"] in ("positioning", "comparison") for c in d["claims"] if c["line_range"] == "L14"),
          "fence: the prose line after the fence should yield a positioning/comparison claim")
    # A non-markdown file: only url/version/numerical, even for prose-looking lines.
    d2 = run_extract(_mk_patch("static/programs/x-go/go.mod", [
        "\tgithub.com/pulumi/pulumi-gcp/sdk/v8 v8.2.0",
        "\t// the canonical provider, unlike the deprecated one",  # prose-y comment — suppressed in code file
    ]))
    check(_types(d2) <= {"url", "version", "numerical"},
          f"code file: only url/version/numerical expected; got {sorted(_types(d2))}")
    check("version" in _types(d2), "code file: the go.mod pin should be a version claim")


def test_skip_lines() -> None:
    print("test_skip_lines")
    d = run_extract(_mk_patch("content/blog/x.md", [
        "",                       # blank
        "---",                    # frontmatter delimiter
        "| --- | --- |",          # table separator
        "Just plain prose with nothing checkable in it whatsoever today.",  # has "today" → temporal; that's fine
    ]))
    # The blank / delimiter / separator lines must not produce claims.
    bad = [c for c in d["claims"] if c["line_range"] in ("L11", "L12", "L13")]
    check(not bad, f"skip-lines: blank/delimiter/separator lines yielded claims: {bad}")


# ---- extract-claims.py: real fixtures (the run-to-run-fragile shapes) ---------

def _claims_containing(doc: dict, *needles: str) -> list[dict]:
    return [c for c in doc["claims"] if all(n in c["text"] for n in needles)]


def test_synthetic_whole_file_diff() -> None:
    """`git diff --no-index /dev/null <file>` (whole-file review mode).

    The review-existing-content workflow feeds entire files through the
    claim pipeline as new-file diffs. The parser must accept the
    `--- /dev/null` old side, and claim line anchors must equal real
    1-based file line numbers.
    """
    doc = run_extract_fixture("synthetic-whole-file.diff")
    check(doc["stats"]["files_scanned"] == 1, "synthetic: new-file diff is scanned")
    by_line = {c["line_range"]: c["type"] for c in doc["claims"]}
    check(by_line.get("L5") == "numerical", f"synthetic: $0.20 claim anchored at real file line L5 (got {by_line})")
    check(by_line.get("L6") == "url", "synthetic: URL claim anchored at real file line L6")


def test_extract_urls_patch_file_mode() -> None:
    """extract-urls-and-fetch.py --patch-file reads a diff without `gh`.

    Uses a URL-free patch so the test exercises the new input path without
    any network fetches.
    """
    script = HERE / "extract-urls-and-fetch.py"
    patch = (
        "diff --git a/content/docs/x/plain.md b/content/docs/x/plain.md\n"
        "new file mode 100644\n"
        "index 0000000..1111111\n"
        "--- /dev/null\n"
        "+++ b/content/docs/x/plain.md\n"
        "@@ -0,0 +1,2 @@\n"
        "+---\n"
        "+title: No links here\n"
    )
    with tempfile.TemporaryDirectory() as td:
        pf = Path(td) / "p.patch"
        pf.write_text(patch)
        out = Path(td) / "urls.json"
        r = subprocess.run([sys.executable, str(script), "--patch-file", str(pf), "--out", str(out)],
                           capture_output=True, text=True)
        check(r.returncode == 0, f"extract-urls --patch-file exits 0 (stderr: {r.stderr.strip()[:120]})")
        check(out.is_file() and json.loads(out.read_text()) == [], "extract-urls --patch-file: empty list for URL-free diff")


def test_fixture_pr18771_strongdm_mechanics() -> None:
    print("test_fixture_pr18771_strongdm_mechanics (attribution paragraph: number cluster + third-party attribution)")
    d = run_extract_fixture("pr18771-dark-factory.diff")
    # The holdout-mechanics paragraph: numbers (three times / 90%) attributed to StrongDM's pattern.
    mech = _claims_containing(d, "StrongDM's pattern", "three times")
    check(bool(mech), "pr18771: expected a claim whose text is the StrongDM holdout-mechanics line (\"StrongDM's pattern ... three times\")")
    # And it should be surfaced both as a numerical claim and an attribution claim.
    mech_types = {c["type"] for c in _claims_containing(d, "StrongDM's pattern", "90%")}
    check("numerical" in mech_types, f"pr18771: the StrongDM-mechanics line should yield a numerical claim; got {mech_types}")
    check("attribution" in mech_types, f"pr18771: the StrongDM-mechanics line should yield an attribution claim; got {mech_types}")


def test_fixture_pr18743_price_and_model() -> None:
    print("test_fixture_pr18743_price_and_model (numerical contradiction + entity-spec mislabel on the same PR)")
    d = run_extract_fixture("pr18743-ollama-ec2.diff")
    # The p5.48xlarge $98.32/hr price (R1's catch).
    check(bool(_claims_containing(d, "p5.48xlarge", "98.32")),
          "pr18743: expected a numerical claim whose text contains 'p5.48xlarge' and '$98.32/hr'")
    check(any(c["type"] == "numerical" for c in _claims_containing(d, "p5.48xlarge", "98.32")),
          "pr18743: the p5.48xlarge price claim should be typed numerical")
    # The Llama 3.3 / 32B model-table row (R2's catch).
    llama = _claims_containing(d, "Llama 3.3", "32B")
    check(bool(llama), "pr18743: expected a claim whose text contains 'Llama 3.3' and '32B'")
    check(any(c["type"] == "entity-spec" for c in llama),
          f"pr18743: the Llama-3.3-32B row should yield an entity-spec claim; got {[c['type'] for c in llama]}")


def test_fixture_pr18541_gcp_version_pin() -> None:
    print("test_fixture_pr18541_gcp_version_pin (version-pin in a non-content file — API-currency note)")
    d = run_extract_fixture("pr18541-gcp-programs.diff")
    pin = _claims_containing(d, "pulumi-gcp", "v8.2.0")
    check(bool(pin), "pr18541: expected a version claim whose text contains 'pulumi-gcp' and 'v8.2.0'")
    check(any(c["type"] == "version" for c in pin),
          f"pr18541: the pulumi-gcp pin should be typed version; got {[c['type'] for c in pin]}")


# ---- merge-claims.py ----------------------------------------------------------

def _regex_doc(claims: list[dict]) -> dict:
    out = []
    for c in claims:
        c = dict(c)
        c.setdefault("confidence", "high")
        out.append(c)
    return {"schema_version": 1, "claims": out, "errors": [], "stats": {}}


def _llm_doc(pass_name: str, claims: list[dict], errors: list[str] | None = None) -> dict:
    out = []
    for c in claims:
        c = dict(c)
        c.setdefault("confidence", "medium")
        c.setdefault("found_by", [f"llm-{pass_name}"])
        out.append(c)
    return {"schema_version": 1, "pass": pass_name, "model": "claude-sonnet-5",
            "claims": out, "errors": errors or [],
            "meta": {"input_tokens": 10, "output_tokens": 5, "cache_read_input_tokens": 0, "cache_creation_input_tokens": 0}}


def test_merge_dedup_and_provenance() -> None:
    print("test_merge_dedup_and_provenance")
    f = "content/blog/x.md"
    regex = _regex_doc([
        {"file": f, "line_range": "L11", "text": "The p5.48xlarge instance costs $98.32/hr on-demand.", "type": "numerical"},
        {"file": f, "line_range": "L12", "text": "StrongDM reported roughly $1,000 per day per engineer.", "type": "numerical"},
        {"file": f, "line_range": "L12", "text": "StrongDM reported roughly $1,000 per day per engineer.", "type": "attribution", "source_hint": "StrongDM"},
        {"file": f, "line_range": "L99", "text": "Llama 3.3 ships as a 32B model.", "type": "entity-spec"},
    ])
    atomic = _llm_doc("atomic", [
        {"file": f, "line_range": "L11", "text": "The AWS p5.48xlarge instance costs about $98.32/hr on-demand.", "type": "numerical", "confidence": "high"},
        {"file": f, "line_range": "L12", "text": "StrongDM reported roughly $1,000/day per engineer-equivalent in token spend.", "type": "attribution", "source_hint": "StrongDM", "confidence": "high"},
        {"file": f, "line_range": "L20", "text": "S3 bucket server-side encryption is enabled by default in this example.", "type": "behavior"},
    ])
    holistic = _llm_doc("holistic", [
        {"file": f, "line_range": "L21", "text": "S3 server-side encryption is turned on by default for the bucket in this example.", "type": "behavior"},
        {"file": f, "line_range": "L12", "text": "StrongDM reported about $1,000 per day per engineer-equivalent.", "type": "attribution", "source_hint": "StrongDM (via Willison)", "confidence": "medium"},
    ])
    m = run_merge(regex, [atomic, holistic])
    by_text = {c["text"][:25]: c for c in m["claims"]}
    # 4 + 5 input records → 4 merged (L11 cluster, L12 cluster, L20-21 cluster, L99 solo).
    check(len(m["claims"]) == 4, f"merge: expected 4 merged claims; got {len(m['claims'])}: {[(c['line_range'], c['type']) for c in m['claims']]}")
    # The L11 cluster: regex + llm-atomic, the LLM restatement wins as `text`.
    l11 = next(c for c in m["claims"] if c["line_range"].startswith("L11"))
    check(set(l11["found_by"]) == {"regex", "llm-atomic"}, f"merge: L11 found_by should be {{regex, llm-atomic}}; got {l11['found_by']}")
    check("AWS p5.48xlarge" in l11["text"], f"merge: L11 should keep the LLM restatement as text; got {l11['text']!r}")
    check(l11["confidence"] == "high", "merge: L11 (regex-found) should be confidence=high")
    # The L12 cluster: regex(×2) + both LLM passes → attribution wins over numerical (more specific), source_hint kept, high confidence.
    l12 = next(c for c in m["claims"] if c["line_range"].startswith("L12"))
    check(l12["type"] == "attribution", f"merge: L12 should be typed attribution (more specific than numerical); got {l12['type']}")
    check(l12.get("source_hint", "").startswith("StrongDM"), f"merge: L12 should keep a StrongDM source_hint; got {l12.get('source_hint')}")
    check(set(l12["found_by"]) == {"regex", "llm-atomic", "llm-holistic"}, f"merge: L12 found_by; got {l12['found_by']}")
    # The L20-21 cluster: two LLM passes, adjacent lines → merged range, high confidence (≥2 passes).
    l20 = next(c for c in m["claims"] if c["line_range"] in ("L20-21", "L20", "L21"))
    check(set(l20["found_by"]) == {"llm-atomic", "llm-holistic"}, f"merge: L20-21 found_by; got {l20['found_by']}")
    check(l20["confidence"] == "high", "merge: L20-21 (found by both LLM passes) should be confidence=high")
    # The L99 entity-spec claim: regex-only, untouched.
    l99 = next(c for c in m["claims"] if c["line_range"] == "L99")
    check(l99["found_by"] == ["regex"] and l99["type"] == "entity-spec", f"merge: L99 should be regex-only entity-spec; got {l99}")
    # Token meta propagated from the two LLM passes.
    check(m["meta"]["llm_input_tokens"] == 20 and m["meta"]["regex_claims"] == 4 and m["meta"]["llm_claims"] == 5,
          f"merge: meta should sum LLM tokens / count inputs; got {m['meta']}")


def test_merge_line_anchor_clamps_out_of_bounds() -> None:
    print("test_merge_line_anchor_clamps_out_of_bounds")
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / "content" / "blog").mkdir(parents=True)
        (root / "content" / "blog" / "x.md").write_text("line one\nline two\nline three\n")  # 3 lines
        regex = _regex_doc([])
        atomic = _llm_doc("atomic", [
            {"file": "content/blog/x.md", "line_range": "L2", "text": "an in-bounds claim about line two stuff", "type": "behavior", "confidence": "high"},
            {"file": "content/blog/x.md", "line_range": "L99", "text": "an out-of-bounds claim nobody can find", "type": "numerical", "confidence": "high"},
        ])
        m = run_merge(regex, [atomic], repo_root=root)
        in_b = next(c for c in m["claims"] if "in-bounds" in c["text"])
        check(in_b["line_range"] == "L2" and not in_b.get("line_range_unverified"), f"merge: in-bounds claim should keep L2, no flag; got {in_b}")
        oob = next(c for c in m["claims"] if "out-of-bounds" in c["text"])
        check(oob.get("line_range_unverified") is True, "merge: out-of-bounds line range should be flagged line_range_unverified")
        check(oob["confidence"] == "low", "merge: out-of-bounds-range claim confidence should drop to low")
        # Clamped to the file's last line.
        check(oob["line_range"] == "L3", f"merge: out-of-bounds range should clamp to L3 (file has 3 lines); got {oob['line_range']}")


def test_merge_missing_and_error_inputs() -> None:
    print("test_merge_missing_and_error_inputs")
    # Regex layer reports an error (e.g. safe_main caught a crash), one LLM file absent → still produces a valid artifact.
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        rp = tdp / "regex.json"
        rp.write_text(json.dumps({"schema_version": 1, "claims": [], "errors": ["extract-claims.py failed to start"]}))
        out = tdp / "merged.json"
        r = subprocess.run([sys.executable, str(MERGE), "--regex", str(rp),
                            "--llm", str(tdp / "does-not-exist-1.json"),
                            "--llm", str(tdp / "does-not-exist-2.json"),
                            "--out", str(out), "--repo-root", str(tdp)],
                           capture_output=True, text=True)
        check(r.returncode == 0, f"merge: should exit 0 even with error/missing inputs; exited {r.returncode}")
        m = json.loads(out.read_text())
        check(m["claims"] == [], "merge: no claims when all inputs are empty/missing")
        check(any("failed to start" in e for e in m["errors"]), f"merge: should propagate the regex-layer error; got {m['errors']}")
        check(any("not present" in e for e in m["errors"]), f"merge: should note missing LLM-pass files; got {m['errors']}")
    # LLM-only (regex layer absent): merge falls back to just the LLM claims.
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        out = tdp / "merged.json"
        ap = tdp / "a.json"
        ap.write_text(json.dumps(_llm_doc("atomic", [{"file": "content/blog/x.md", "line_range": "L5", "text": "a solo llm claim", "type": "behavior"}])))
        r = subprocess.run([sys.executable, str(MERGE), "--regex", str(tdp / "nope.json"),
                            "--llm", str(ap), "--out", str(out), "--repo-root", str(tdp)],
                           capture_output=True, text=True)
        check(r.returncode == 0, f"merge: llm-only should exit 0; exited {r.returncode}")
        m = json.loads(out.read_text())
        check(len(m["claims"]) == 1 and m["claims"][0]["found_by"] == ["llm-atomic"],
              f"merge: llm-only should yield the 1 llm claim; got {m['claims']}")


# ---- main ---------------------------------------------------------------------

def main() -> int:
    if not TESTDATA.is_dir():
        print(f"FATAL: testdata dir not found at {TESTDATA}", file=sys.stderr)
        return 2
    for fixture in ("pr18771-dark-factory.diff", "pr18743-ollama-ec2.diff", "pr18541-gcp-programs.diff"):
        if not (TESTDATA / fixture).is_file():
            print(f"FATAL: missing fixture {TESTDATA / fixture}", file=sys.stderr)
            return 2

    tests = [
        test_synthetic_categories,
        test_code_context_suppresses_prose,
        test_skip_lines,
        test_synthetic_whole_file_diff,
        test_extract_urls_patch_file_mode,
        test_fixture_pr18771_strongdm_mechanics,
        test_fixture_pr18743_price_and_model,
        test_fixture_pr18541_gcp_version_pin,
        test_merge_dedup_and_provenance,
        test_merge_line_anchor_clamps_out_of_bounds,
        test_merge_missing_and_error_inputs,
    ]
    for t in tests:
        try:
            t()
        except AssertionError as e:
            _failures.append(f"{t.__name__}: assertion error: {e}")
            print(f"  FAIL: {t.__name__}: {e}", file=sys.stderr)
        except Exception as e:  # noqa: BLE001
            _failures.append(f"{t.__name__}: unexpected {type(e).__name__}: {e}")
            print(f"  ERROR: {t.__name__}: {type(e).__name__}: {e}", file=sys.stderr)

    print(f"\n{_passes} check(s) passed, {len(_failures)} failed.")
    if _failures:
        for f in _failures:
            print(f"  - {f}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
