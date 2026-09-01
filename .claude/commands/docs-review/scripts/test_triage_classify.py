#!/usr/bin/env python3
"""Tests for triage-classify.py — the deterministic PR triage classifier.

Self-contained — run with `python3 test_triage_classify.py` (no pytest dep).
Shells out to the script the same way claude-triage.yml does (PR JSON on
argv[1], unified diff on stdin) and asserts on the JSON it emits.
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
CLASSIFY = HERE / "triage-classify.py"

_failures: list[str] = []
_passes = 0


def assert_clean(name: str, before: int) -> None:
    """Fail the *test function* on the check failures it recorded itself.

    This file is run two ways: standalone (`python3 test_triage_classify.py`,
    where main() reads the _failures list) and under pytest via
    `make test-review-pipeline`, which collects the `test_*` functions
    directly. pytest only sees a failure if the function raises, so without
    this call a broken routing rule would record FAILs and still report a
    green suite in CI.

    `before` is `len(_failures)` captured on entry to the test function.
    _failures is module-level and never reset, so without that baseline a
    failure recorded by an earlier test would also fail every later one and
    be counted in *its* message — pointing the reader at the wrong test.
    It is required rather than defaulted so a future test can't silently
    reintroduce that.
    """
    new = _failures[before:]
    if new:
        raise AssertionError(f"{name}: {len(new)} check(s) failed (see FAIL lines above)")


def check(cond: bool, msg: str) -> None:
    global _passes
    if cond:
        _passes += 1
    else:
        _failures.append(msg)
        print(f"  FAIL: {msg}", file=sys.stderr)


def run_classify(pr_data: dict, diff: str = "") -> dict:
    with tempfile.TemporaryDirectory() as td:
        pf = Path(td) / "pr.json"
        pf.write_text(json.dumps(pr_data))
        r = subprocess.run([sys.executable, str(CLASSIFY), str(pf)],
                           input=diff, capture_output=True, text=True)
        assert r.returncode == 0, f"triage-classify.py exited {r.returncode}: {r.stderr}"
        return json.loads(r.stdout)


def _pr(additions: int, deletions: int, paths: list[str]) -> dict:
    return {
        "additions": additions,
        "deletions": deletions,
        "files": [{"path": p, "additions": additions // max(len(paths), 1), "deletions": 0}
                  for p in paths],
        "labels": [],
    }


def test_oversized_threshold() -> None:
    print("test_oversized_threshold")
    before = len(_failures)
    # A generated-corpus monster (the PR #20274 shape) is oversized.
    big = run_classify(_pr(99_664, 1_759, ["data/policy_pack_policies/cis.yaml",
                                           "content/docs/reference/x/_index.md",
                                           "scripts/gen-policy-docs.ts"]))
    check(big["oversized"] is True, f"99K-line PR classifies oversized; got {big['oversized']}")

    # Exactly at the threshold: not oversized (strict >).
    at = run_classify(_pr(10_000, 5_000, ["content/docs/a.md"]))
    check(at["oversized"] is False, f"15,000 changed lines is NOT oversized (strict >); got {at['oversized']}")

    # Just over: oversized. Deletions count toward the total.
    over = run_classify(_pr(1, 15_000, ["content/docs/a.md"]))
    check(over["oversized"] is True, f"15,001 changed lines (deletion-heavy) IS oversized; got {over['oversized']}")

    # A normal hand-written PR is nowhere near it.
    normal = run_classify(_pr(406, 1, ["content/blog/post/index.md"]))
    check(normal["oversized"] is False, "a 407-line PR is not oversized")
    check("oversized" in normal, "oversized field always present")

    # File count is an independent axis (the PR #20560 shape): few lines,
    # many pages. Strict > on 150 files.
    many = run_classify(_pr(2_215, 1_265, [f"content/docs/p{i}/_index.md" for i in range(155)]))
    check(many["oversized"] is True, f"155-file PR classifies oversized; got {many['oversized']}")
    at_files = run_classify(_pr(2_000, 1_000, [f"content/docs/p{i}/_index.md" for i in range(150)]))
    check(at_files["oversized"] is False, f"exactly 150 files is NOT oversized (strict >); got {at_files['oversized']}")
    assert_clean("test_oversized_threshold", before)


def test_domain_routing() -> None:
    print("test_domain_routing")
    before = len(_failures)

    def domains(paths: list[str]) -> list[str]:
        return run_classify(_pr(10, 0, paths))["target_domains"]

    # theme/ is asset-pipeline source (SCSS + TypeScript compiled into the
    # site bundles) and routes to infra like layouts/ and assets/. The gap
    # this closes: PR #21164 touched only theme/src/{scss,ts} and came out
    # of triage with no domain label at all.
    check(domains(["theme/src/ts/consent-manager/index.ts"]) == ["domain:infra"],
          f"theme/src/ts routes to infra; got {domains(['theme/src/ts/consent-manager/index.ts'])}")
    check(domains(["theme/src/scss/_consent-banner.scss"]) == ["domain:infra"],
          "theme/src/scss routes to infra")
    check(domains(["theme/scripts/build-color-theme.mjs"]) == ["domain:infra"],
          "theme/scripts routes to infra")

    # Existing precedence is unchanged by the theme/ rule and the fallback.
    check(domains(["static/programs/aws-ts-s3/index.ts"]) == ["domain:programs"],
          "static/programs beats the static/ infra rule")
    check(domains(["scripts/programs/ignore.txt"]) == ["domain:programs"],
          "scripts/programs beats the scripts/ infra rule")
    check(domains(["content/blog/post/index.md"]) == ["domain:blog"], "blog routes to blog")
    check(domains(["content/docs/a.md"]) == ["domain:docs"], "docs routes to docs")
    check(domains(["content/pricing/_index.md"]) == ["domain:website"],
          "non-docs content markdown routes to website")
    check(domains(["layouts/index.html"]) == ["domain:infra"], "layouts routes to infra")

    # Fallback: a PR where nothing matches still carries one domain signal,
    # so "no domain label" unambiguously means triage never ran.
    check(domains(["data/blog_tags.yaml"]) == ["domain:other"],
          f"unmatched paths fall back to domain:other; got {domains(['data/blog_tags.yaml'])}")
    check(domains(["data/a.yaml", "styles/Pulumi/Terms.yml"]) == ["domain:other"],
          "several unmatched paths still collapse to a single domain:other")
    check(run_classify(_pr(10, 0, ["data/a.yaml"]))["mixed"] is False,
          "the fallback never sets mixed")

    # ...but never alongside a real domain: the unmatched file adds no review
    # lane, so it must not flip `mixed` on a single-domain PR.
    mixed_with_unmatched = run_classify(_pr(10, 0, ["content/docs/a.md", "data/b.yaml"]))
    check(mixed_with_unmatched["target_domains"] == ["domain:docs"],
          f"an unmatched file alongside docs stays docs-only; got {mixed_with_unmatched['target_domains']}")
    check(mixed_with_unmatched["mixed"] is False,
          "docs + an unmatched file is NOT mixed")

    # A genuinely multi-domain PR is still mixed, and never picks up the fallback.
    real_mix = run_classify(_pr(10, 0, ["content/docs/a.md", "theme/src/ts/x.ts"]))
    check(real_mix["target_domains"] == ["domain:docs", "domain:infra"],
          f"docs + theme is a real two-domain PR; got {real_mix['target_domains']}")
    check(real_mix["mixed"] is True, "docs + theme sets mixed")

    # An empty file list yields no domain at all (nothing to label).
    check(run_classify(_pr(0, 0, []))["target_domains"] == [],
          "a PR with no files gets no domain label")

    # The fallback must not open the trivial / frontmatter-only short-circuit
    # to non-content files.
    themed = run_classify(_pr(1, 0, ["theme/src/ts/x.ts"]), "")
    check(themed["trivial"] is False, "a one-line theme/ change is not trivial")
    other = run_classify(_pr(1, 0, ["data/a.yaml"]), "")
    check(other["trivial"] is False, "a one-line unmatched change is not trivial")
    assert_clean("test_domain_routing", before)


def _md_diff(path: str, lines: list[str], old_start: int = 40) -> str:
    """A one-hunk unified diff for `path` whose body is `lines` (each already
    carrying its ` `/`+`/`-` marker)."""
    olds = sum(1 for l in lines if not l.startswith("+"))
    news = sum(1 for l in lines if not l.startswith("-"))
    return (f"diff --git a/{path} b/{path}\n--- a/{path}\n+++ b/{path}\n"
            f"@@ -{old_start},{olds} +{old_start},{news} @@\n" + "\n".join(lines) + "\n")


def test_code_inside_existing_fence_is_not_trivial() -> None:
    """`has_code_block_change` used to fire only when a changed line WAS a
    fence marker, so a docs PR editing the Java/Go/TS inside existing fences
    (+10 lines, one file) classified `review:trivial` and skipped review."""
    print("test_code_inside_existing_fence_is_not_trivial")
    before = len(_failures)
    path = "content/docs/iac/concepts/x.md"

    # Fence marker visible as context, PROSE-shaped body: only the marker can
    # carry the signal, so this pins the fence-tracking half of the fix on
    # its own (the review of PR #21309 noted a Java-bodied fixture here was
    # also caught by the shape heuristic, leaving fence tracking untested).
    # It inverts cleanly against the `prose` fixture below, which is the same
    # shape with no marker and is asserted trivial.
    with_marker = [
        " ```text",
        " Set the region before you deploy.",
        "-Use us-west-2 for the walkthrough.",
        "+Use us-east-1 for the walkthrough.",
        " Then run the deploy command.",
    ]
    r = run_classify(_pr(1, 1, [path]), _md_diff(path, with_marker))
    check(r["trivial"] is False, f"a prose edit under a visible fence marker is not trivial; got {r}")

    # Both signals at once: marker visible AND code-shaped body.
    with_marker_code = [
        " ```java",
        " class AwsS3Website extends ComponentResource {",
        "-    public AwsS3Website(String name) {",
        "+    AwsS3Website(String name) {",
        "         super(\"pkg:index:AwsS3Website\", name);",
        "     }",
    ]
    r = run_classify(_pr(1, 1, [path]), _md_diff(path, with_marker_code))
    check(r["trivial"] is False, f"a code edit under a visible fence marker is not trivial; got {r}")

    # Hunk starts mid-fence: no marker in view, but the lines are code-shaped.
    mid_fence = [
        " import com.pulumi.resources.ComponentResourceOptions;",
        " ",
        "-public class AwsS3Website extends ComponentResource {",
        "+class AwsS3Website extends ComponentResource {",
        "     private final Output<String> url;",
        "     public AwsS3Website(String name, AwsS3WebsiteArgs args) {",
    ]
    r = run_classify(_pr(1, 1, [path]), _md_diff(path, mid_fence))
    check(r["trivial"] is False, f"a hunk that opens mid-fence with code-shaped lines is not trivial; got {r}")

    # Prose with a parenthesis at a line end is still prose — still trivial.
    prose = [
        " Components group resources so a team can reuse them (see below).",
        "-Each child inherits the parent's provider and options.",
        "+Each child inherits the parent's provider options.",
        " Read the next section for the registration step.",
    ]
    r = run_classify(_pr(1, 1, [path]), _md_diff(path, prose))
    check(r["trivial"] is True, f"a prose-only edit stays trivial; got {r}")

    # Deliberately NOT asserted: a hunk whose first context line is a CLOSING
    # fence reads as if it opened one, so a prose edit right after a code
    # block also classifies non-trivial. That is the direction the heuristic
    # is built to fail in — a spurious review run — and it stays that way.
    assert_clean("test_code_inside_existing_fence_is_not_trivial", before)


def main() -> int:
    tests = [test_oversized_threshold, test_domain_routing,
             test_code_inside_existing_fence_is_not_trivial]
    for t in tests:
        try:
            t()
        except AssertionError as e:
            _failures.append(f"{t.__name__}: assertion error: {e}")
            print(f"  FAIL: {t.__name__}: {e}", file=sys.stderr)
        except Exception as e:  # noqa: BLE001
            _failures.append(f"{t.__name__}: {type(e).__name__}: {e}")
            print(f"  FAIL: {t.__name__}: {type(e).__name__}: {e}", file=sys.stderr)

    print(f"\n{_passes} check(s) passed, {len(_failures)} failed.")
    return 1 if _failures else 0


if __name__ == "__main__":
    sys.exit(main())
