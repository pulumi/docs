#!/usr/bin/env python3
"""Tests for the claim-extraction pre-step: extract-claims.py + merge-claims.py.

Self-contained — run with `python3 test_extract_claims.py` (no pytest dep).
Shells out to the scripts (the same way the workflow does) and asserts on the
JSON they emit. Fixtures in `testdata/` are committed deterministic diffs of
real merged pulumi/docs PRs (#18771, #18743, #18541) — corpus-drawn cases of
the run-to-run-fragile claim shapes the regex floor must guarantee.

(extract-claims-llm.py's API paths need ANTHROPIC_API_KEY and are spike-tested
in CI; its per-file scrutiny resolution and file-cap ordering ARE tested here,
via module import and --dry-run. merge-claims.py is tested against
hand-crafted Layer-B inputs below.)
"""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXTRACT = HERE / "extract-claims.py"
EXTRACT_LLM = HERE / "extract-claims-llm.py"
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


def assert_clean(name: str, before: int) -> None:
    """Fail the *test function* on the check failures it recorded itself.

    Under pytest (`make test-review-pipeline`) a test only fails if it raises;
    `check()` alone would record FAILs and still report green. `before` is
    `len(_failures)` captured on entry, so an earlier test's failure is not
    charged to this one.
    """
    new = _failures[before:]
    if new:
        raise AssertionError(f"{name}: {len(new)} check(s) failed (see FAIL lines above)")


def run_extract(patch_text: str, repo_root: Path | None = None) -> dict:
    """Run the extractor over a patch. `repo_root` defaults to the empty temp
    dir, so a synthetic diff never picks up fence state from a real file."""
    with tempfile.TemporaryDirectory() as td:
        pf = Path(td) / "p.patch"
        pf.write_text(patch_text)
        out = Path(td) / "out.json"
        r = subprocess.run([sys.executable, str(EXTRACT), "--patch-file", str(pf), "--out", str(out),
                            "--repo-root", str(repo_root or td)],
                           capture_output=True, text=True)
        assert r.returncode == 0, f"extract-claims.py exited {r.returncode}: {r.stderr}"
        return json.loads(out.read_text())


def run_extract_fixture(name: str, repo_root: Path | None = None) -> dict:
    with tempfile.TemporaryDirectory() as td:
        out = Path(td) / "out.json"
        r = subprocess.run([sys.executable, str(EXTRACT), "--patch-file", str(TESTDATA / name), "--out", str(out),
                            "--repo-root", str(repo_root or td)],
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


def test_fixture_pr21291_hunk_opening_inside_a_fence() -> None:
    """PR #21291 (glow-up run 33518039058): the `@@ -1217` hunk opens inside a
    code block. Read from the diff alone, the first fence the walker meets is
    that block's CLOSING marker, so every prose line that follows is tagged
    in-code and the new "`pulumi convert` is the fastest path …" sentence
    never yields a positioning claim. Seeding the hunk's fence state from the
    checked-out file (21 markers above line 1217 → inside a fence) fixes it;
    the empty-root run documents the diff-only fallback."""
    print("test_fixture_pr21291_hunk_opening_inside_a_fence")
    before = len(_failures)
    head = TESTDATA / "pr21291-head"
    page = head / "content/docs/iac/get-started/terraform/convert-hcl.md"
    lines = page.read_text().splitlines()
    check(sum(1 for ln in lines[:1216] if ln.lstrip().startswith(("```", "~~~"))) % 2 == 1,
          "fixture: an odd number of fence markers precedes line 1217 (the hunk opens in a fence)")

    seeded = run_extract_fixture("pr21291-fence-seed.diff", repo_root=head)
    fastest = [c for c in seeded["claims"] if "fastest path" in c["text"]]
    check(any(c["type"] == "positioning" for c in fastest),
          f"seeded: the 'fastest path' line yields a positioning claim; got {[(c['line_range'], c['type']) for c in fastest]}")
    check(all(c["line_range"] == "L1226" for c in fastest),
          f"seeded: the 'fastest path' claims anchor at L1226; got {[c['line_range'] for c in fastest]}")

    # Lines that really are inside a fence in the new file (the `bash` and
    # `text` blocks later in the hunk) must yield nothing prose-typed — and in
    # this hunk nothing at all.
    in_fence, fenced = False, set()
    for i, ln in enumerate(lines, start=1):
        if ln.lstrip().startswith(("```", "~~~")):
            in_fence = not in_fence
            continue
        if in_fence and 1217 <= i <= 1252:
            fenced.add(f"L{i}")
    check(len(fenced) >= 4, f"fixture: the hunk contains fenced code lines; found {sorted(fenced)}")
    leaked = [c for c in seeded["claims"] if c["line_range"] in fenced]
    check(not leaked, f"seeded: no claim is extracted from the hunk's code blocks; got {[(c['line_range'], c['type']) for c in leaked]}")

    with tempfile.TemporaryDirectory() as empty:
        fallback = run_extract_fixture("pr21291-fence-seed.diff", repo_root=Path(empty))
    fb_fastest = [c for c in fallback["claims"] if "fastest path" in c["text"]]
    check(fb_fastest and all(c["type"] == "url" for c in fb_fastest),
          f"fallback (no checkout): the old diff-only behaviour — only a url claim on the line; got {[c['type'] for c in fb_fastest]}")
    check(len(seeded["claims"]) > len(fallback["claims"]),
          f"seeding recovers claims the diff-only walk suppressed ({len(seeded['claims'])} vs {len(fallback['claims'])})")
    assert_clean("test_fixture_pr21291_hunk_opening_inside_a_fence", before)


def test_no_script_uses_per_commit_pr_patch() -> None:
    """`gh pr diff --patch` is a per-commit mailbox: a sentence one commit adds
    and a later commit removes is still extracted and verified (contradicted
    against a file that no longer contains it). Every pre-step must read the
    NET diff, and this locks it at the source level."""
    print("test_no_script_uses_per_commit_pr_patch")
    before = len(_failures)
    import re as _re
    bad = _re.compile(r'\["gh",\s*"pr",\s*"diff",\s*[^\]]*"--patch"')
    offenders = sorted(p.name for p in HERE.glob("*.py")
                       if p.name != Path(__file__).name and bad.search(p.read_text()))
    check(offenders == [], f"scripts still fetching the per-commit patch: {offenders}")
    assert_clean("test_no_script_uses_per_commit_pr_patch", before)


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


def test_merge_keeps_a_distinct_regex_stance() -> None:
    """PR #21291 (pre-merge run 33519246857): the regex `positioning` record
    for the whole added line clustered (token overlap 0.93 — far above the
    0.34 threshold) with an LLM `capability` claim restating the OTHER
    sentence on that line; the LLM text won as representative and "fastest"
    never reached the verifier. A regex positioning/comparison record must
    survive as its own claim when the representative is typed differently."""
    print("test_merge_keeps_a_distinct_regex_stance")
    before = len(_failures)
    f = "content/docs/iac/get-started/terraform/convert-hcl.md"
    line = ("`pulumi convert` is the fastest path for most configurations, and it's where to start. "
            "For configurations it struggles with — heavy `for_each` and `dynamic` blocks, or a lot of "
            "module indirection — a coding agent can pick up where the converter leaves off. The "
            "[Pulumi MCP (Model Context Protocol) server](/docs/ai/mcp-server/) gives the agent you "
            "already use access to the Pulumi Registry, your stacks, and a `convert-terraform-to-typescript` prompt.")
    llm_text = ("The Pulumi MCP server gives the agent you already use access to the Pulumi Registry, "
                "your stacks, and a convert-terraform-to-typescript prompt.")
    regex = _regex_doc([
        {"file": f, "line_range": "L1226", "text": line, "type": "url", "source_hint": "/docs/ai/mcp-server/"},
        {"file": f, "line_range": "L1226", "text": line, "type": "positioning"},
    ])
    atomic = _llm_doc("atomic", [
        {"file": f, "line_range": "L1226", "text": llm_text, "type": "capability", "confidence": "high"},
    ])
    # Sanity: the two texts overlap far above the cluster threshold, so the
    # old merge absorbed the stance.
    sys.path.insert(0, str(HERE))
    spec = importlib.util.spec_from_file_location("merge_claims", MERGE)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    overlap = mod.token_overlap(line, llm_text)
    check(overlap > 0.9, f"fixture: token overlap between the line and the LLM restatement is > 0.9; got {overlap:.2f}")

    m = run_merge(regex, [atomic])
    # Schema v2: stances are routed to their own list, out of the verifier's
    # input — so the survivor shows up under `stances`, not `claims`.
    all_records = m["claims"] + m["stances"]
    types = sorted(c["type"] for c in all_records)
    check("positioning" in types, f"merge: the regex positioning record survives as its own record; got {types}")
    check("capability" in types, f"merge: the LLM capability claim survives too; got {types}")
    check(len(all_records) == 2, f"merge: exactly two records (stance + capability); got {len(all_records)}: {types}")
    stance = next(c for c in m["stances"] if c["type"] == "positioning")
    check("fastest path" in stance["text"] and stance["found_by"] == ["regex"],
          f"merge: the stance keeps the regex line text and provenance; got {stance}")
    check(all(c["type"] not in ("positioning", "comparison") for c in m["claims"]),
          f"merge: no stance in the verifier's `claims` list; got {[c['type'] for c in m['claims']]}")
    cap = next(c for c in m["claims"] if c["type"] == "capability")
    check("regex" in cap["found_by"] and cap["type"] == "capability",
          f"merge: the url record still merges into the capability claim; got {cap}")

    # Same types on both sides still collapse to one record.
    same = run_merge(_regex_doc([{"file": f, "line_range": "L1226", "text": line, "type": "positioning"}]),
                     [_llm_doc("atomic", [{"file": f, "line_range": "L1226",
                                          "text": "pulumi convert is the fastest path for most configurations.",
                                          "type": "positioning"}])])
    check(len(same["stances"]) == 1 and same["stances"][0]["type"] == "positioning" and not same["claims"],
          f"merge: a regex stance whose representative is ALSO a stance still merges; got {same}")
    assert_clean("test_merge_keeps_a_distinct_regex_stance", before)


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


# ---- extract-claims-llm.py: per-file scrutiny + file-cap ordering -------------

def _llm_mod():
    spec = importlib.util.spec_from_file_location("extract_claims_llm", EXTRACT_LLM)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_llm_scrutiny_per_file() -> None:
    print("test_llm_scrutiny_per_file (blog bump, small-edit pin, ratio bound, override, new file)")
    m = _llm_mod()
    blog = "content/blog/some-post/index.md"
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        f = root / blog
        f.parent.mkdir(parents=True)
        f.write_text("\n".join(f"body line {i}" for i in range(1, 101)) + "\n")

        # A 3-line insert into a 100-line published post: bumped for being blog,
        # then pinned back to standard by the small-edit guard.
        small = _mk_patch(blog, ["{{< blog/cta-card >}}", "Two lines of new prose.", "{{< /blog/cta-card >}}"])
        msg, note = m.build_user_message(root, small, blog, "standard")
        check("scope: standard" in msg, "llm-scrutiny: small blog edit pins to standard scope")
        check(note is not None and "small edit" in note, f"llm-scrutiny: small-edit pin surfaces a note; got {note!r}")

        # 40 added lines: over the absolute bound — stays heightened.
        big = _mk_patch(blog, [f"New prose line {i}." for i in range(40)])
        msg, _ = m.build_user_message(root, big, blog, "standard")
        check("WHOLE file" in msg, "llm-scrutiny: 40-line blog edit stays heightened")

        # 25 added lines: under the absolute bound but >20% of a 100-line file — stays heightened.
        mid = _mk_patch(blog, [f"New prose line {i}." for i in range(25)])
        msg, _ = m.build_user_message(root, mid, blog, "standard")
        check("WHOLE file" in msg, "llm-scrutiny: 25 added lines in a 100-line file (>20%) stays heightened")

        # Global --scrutiny heightened is a force-override: no small-edit pin.
        msg, _ = m.build_user_message(root, small, blog, "heightened")
        check("WHOLE file" in msg, "llm-scrutiny: global heightened override defeats the small-edit pin")

    # A docs file's small edit under standard scrutiny: no blog bump, standard scope.
    docs = "content/docs/x/page.md"
    with tempfile.TemporaryDirectory() as td:
        msg, note = m.build_user_message(Path(td), _mk_patch(docs, ["One new line."]), docs, "standard")
        check("scope: standard" in msg and note is None,
              f"llm-scrutiny: docs small edit is standard scope with no note; got note={note!r}")

    # A brand-new blog file: heightened even though tiny (small-edit pin skips new files).
    new_blog = "content/blog/new-post/index.md"
    new_patch = (
        f"diff --git a/{new_blog} b/{new_blog}\n"
        "new file mode 100644\n"
        "--- /dev/null\n"
        f"+++ b/{new_blog}\n"
        "@@ -0,0 +1,3 @@\n"
        "+---\n"
        "+title: New post\n"
        "+---\n"
    )
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        nf = root / new_blog
        nf.parent.mkdir(parents=True)
        nf.write_text("---\ntitle: New post\n---\n")
        msg, _ = m.build_user_message(root, new_patch, new_blog, "standard")
        check("WHOLE file" in msg, "llm-scrutiny: brand-new blog file stays heightened despite being tiny")


def test_llm_file_cap_prefers_biggest_edits() -> None:
    print("test_llm_file_cap_prefers_biggest_edits")
    files = [f"content/docs/x/f{i:02}.md" for i in range(20)] + ["content/docs/x/big.md"]
    patch = "".join(_mk_patch(f, ["One added line."]) for f in files[:20])
    patch += _mk_patch("content/docs/x/big.md", [f"Added line {i}." for i in range(10)])
    with tempfile.TemporaryDirectory() as td:
        pf = Path(td) / "p.patch"
        pf.write_text(patch)
        out = Path(td) / "out.json"
        # The script loads its system prompt from the repo root before the
        # dry-run short-circuit; give the tmp root a stub copy.
        ref = Path(td) / ".claude/commands/docs-review/references/claim-extraction.md"
        ref.parent.mkdir(parents=True)
        ref.write_text("stub system prompt\n")
        r = subprocess.run([sys.executable, str(EXTRACT_LLM), "--patch-file", str(pf),
                            "--changed-files", ",".join(files), "--repo-root", td,
                            "--pass", "atomic", "--dry-run", "--out", str(out)],
                           capture_output=True, text=True)
        check(r.returncode == 0, f"llm cap: exits 0 (stderr: {r.stderr.strip()[:200]})")
        doc = json.loads(out.read_text())
        kept = {c["file"] for c in doc["claims"]}
        check("content/docs/x/big.md" in kept, "llm cap: the biggest edit survives the file cap")
        check(len(kept) == 20, f"llm cap: exactly FILE_CAP files processed; got {len(kept)}")
        check(any("over file cap" in e for e in doc["errors"]),
              f"llm cap: over-cap skip is surfaced in errors[]; got {doc['errors'][:2]}")


# ---- main ---------------------------------------------------------------------

def main() -> int:
    if not TESTDATA.is_dir():
        print(f"FATAL: testdata dir not found at {TESTDATA}", file=sys.stderr)
        return 2
    for fixture in ("pr18771-dark-factory.diff", "pr18743-ollama-ec2.diff", "pr18541-gcp-programs.diff",
                    "pr21291-fence-seed.diff", "pr21291-head/content/docs/iac/get-started/terraform/convert-hcl.md"):
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
        test_fixture_pr21291_hunk_opening_inside_a_fence,
        test_no_script_uses_per_commit_pr_patch,
        test_merge_dedup_and_provenance,
        test_merge_keeps_a_distinct_regex_stance,
        test_merge_line_anchor_clamps_out_of_bounds,
        test_merge_missing_and_error_inputs,
        test_llm_scrutiny_per_file,
        test_llm_file_cap_prefers_biggest_edits,
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
