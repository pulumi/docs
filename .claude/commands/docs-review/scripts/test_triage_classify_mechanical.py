#!/usr/bin/env python3
"""Tests for triage-classify.py's v3 `classify_mechanical` — the tightened
"safe to skip the model" bar (see that function's docstring and
scripts/review-v3/README.md).

Self-contained — run with `python3 test_triage_classify_mechanical.py` (no
pytest dep), or collected by pytest via `make test-review-pipeline`. Imports
triage-classify.py by path (its main() is __main__-guarded, so importing has
no side effects) — same pattern test_framing_drift.py uses, and the pattern
`classify_mechanical`'s own docstring documents as the supported way to
consume this module.

A structural note that shapes several tests below: extract-claims.py's Layer
A net is deliberately wider than condition 7's purpose — `URL_RES` fires on
*any* markdown link, and the numeric-range matcher reads an
`updated: YYYY-MM-DD` bump as a numeric range. Unfiltered, that would shadow
the two carve-outs the mechanical lane exists for (link fixes, updated/tags
bumps), so condition 7 exempts url-type claims (condition 5 already forces
added links to be internal and resolve) and claims whose source line is one
of the allowed frontmatter shapes (`MECHANICAL_CLAIMS_EXEMPT_LINE_RE`;
condition 6 already forbids every other key). Prose claims in body text
still disqualify — those tests assert the boolean, not just the reason.
"""

from __future__ import annotations

import importlib.util
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


tc = _load("triage_classify_mech_under_test", "triage-classify.py")

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
    new = _failures[before:]
    if new:
        raise AssertionError(f"{name}: {len(new)} check(s) failed (see FAIL lines above)")


# ---- Fixtures ---------------------------------------------------------------

_REPO_ROOT: Path | None = None


def _repo_root() -> Path:
    """A throwaway content/ tree with one real page, for link-resolution
    tests. Built once and cached — nothing here is mutated by a test."""
    global _REPO_ROOT
    if _REPO_ROOT is None:
        d = Path(tempfile.mkdtemp(prefix="triage-mechanical-fixture-"))
        stacks_dir = d / "content" / "docs" / "iac" / "concepts" / "stacks"
        stacks_dir.mkdir(parents=True)
        (stacks_dir / "_index.md").write_text("Stacks landing page.\n")
        _REPO_ROOT = d
    return _REPO_ROOT


def make_file_diff(path: str, lines: list[str], *, is_new: bool = False,
                    is_delete: bool = False, is_binary: bool = False,
                    rename_from: str | None = None,
                    old_start: int = 40, new_start: int = 40) -> str:
    """Build one file's unified-diff text (the `diff --git ...` chunk
    split_files() expects). `lines` are already unified-diff-format, each
    starting with ' ' (context), '+' (added), or '-' (removed).

    `old_start`/`new_start` default to 40 — past detect_starting_state's
    30-line frontmatter cutoff — so tests that don't care about frontmatter
    land unambiguously in "body" state without needing filler context.
    """
    header = [f"diff --git a/{rename_from or path} b/{path}"]
    if rename_from:
        header.append("similarity index 100%")
        header.append(f"rename from {rename_from}")
        header.append(f"rename to {path}")
    if is_new:
        header.append("new file mode 100644")
    if is_delete:
        header.append("deleted file mode 100644")
    if is_binary:
        header.append("GIT binary patch")
        return "\n".join(header) + "\n"
    old_src = "/dev/null" if is_new else f"a/{rename_from or path}"
    new_src = "/dev/null" if is_delete else f"b/{path}"
    header.append(f"--- {old_src}")
    header.append(f"+++ {new_src}")
    added = sum(1 for l in lines if l.startswith("+"))
    removed = sum(1 for l in lines if l.startswith("-"))
    ctx = sum(1 for l in lines if l.startswith(" "))
    header.append(f"@@ -{old_start},{removed + ctx} +{new_start},{added + ctx} @@")
    return "\n".join(header + lines) + "\n"


def run_mechanical(diff_text: str, files: list[dict] | None = None,
                    additions: int | None = None, deletions: int | None = None,
                    repo_root: Path | None = None) -> tuple[bool, list[str]]:
    """Build pr_data/file_flags the same way main() does and classify."""
    file_diffs = tc.split_files(diff_text)
    if files is None:
        files = [{"path": p} for p, _ in file_diffs]
    if additions is None:
        additions = sum(1 for line in diff_text.splitlines()
                         if line.startswith("+") and not line.startswith("+++"))
    if deletions is None:
        deletions = sum(1 for line in diff_text.splitlines()
                         if line.startswith("-") and not line.startswith("---"))
    pr_data = {"additions": additions, "deletions": deletions, "files": files}
    file_flags = [tc.classify_file(p, d) for p, d in file_diffs]
    return tc.classify_mechanical(pr_data, file_flags, diff_text, repo_root or _repo_root())


def filler_lines(n: int, marker: str = "+", start: int = 1) -> list[str]:
    """`n` body lines that never trip extract-claims' Layer-A regexes —
    verified empirically (see the module docstring / sanity check this test
    file's author ran before committing to this template)."""
    return [f"{marker}Filler paragraph number {i} for the mechanical test fixture."
            for i in range(start, start + n)]


BASE_CONTEXT = [" Some existing paragraph text stays here for context.",
                " Another existing paragraph stays here too for context."]


def body_diff(path: str, added: list[str] | None = None, removed: list[str] | None = None) -> str:
    lines = [BASE_CONTEXT[0], *(removed or []), *(added or []), BASE_CONTEXT[1]]
    return make_file_diff(path, lines)


# ---- All conditions pass -----------------------------------------------------


def test_all_pass_is_mechanical() -> None:
    print("test_all_pass_is_mechanical")
    before = len(_failures)
    d = body_diff("content/docs/foo.md",
                   added=["+This section explains how stacks organize resources across environments."])
    ok, reasons = run_mechanical(d)
    check(ok is True, f"clean docs body change is mechanical; reasons={reasons}")
    check(reasons == [], f"no reasons on a clean PR; got {reasons}")

    d_blog = body_diff("content/blog/post/index.md",
                        added=["+This section explains how stacks organize resources across environments."])
    ok2, reasons2 = run_mechanical(d_blog)
    check(ok2 is True, f"clean blog body change is mechanical; reasons={reasons2}")
    assert_clean("test_all_pass_is_mechanical", before)


# ---- Condition 1: domain -----------------------------------------------------


def test_condition_domain() -> None:
    print("test_condition_domain")
    before = len(_failures)
    d = body_diff("data/some_config.yaml", added=["+another: value"])
    ok, reasons = run_mechanical(d, files=[{"path": "data/some_config.yaml"}])
    check(ok is False, "a non docs/blog file is never mechanical")
    check(any("outside domain:docs/domain:blog" in r for r in reasons),
          f"reason names the off-domain file; got {reasons}")
    assert_clean("test_condition_domain", before)


# ---- Condition 2: new/renamed/deleted/binary ---------------------------------


def test_condition_structural() -> None:
    print("test_condition_structural")
    before = len(_failures)

    d_new = make_file_diff("content/docs/newfile.md",
                            ["+Brand new page body line for the fixture."],
                            is_new=True, old_start=1, new_start=1)
    ok, reasons = run_mechanical(d_new)
    check(ok is False, "a new file is never mechanical")
    check(any("new/renamed/deleted/binary" in r for r in reasons), f"got {reasons}")

    d_del = make_file_diff("content/docs/oldfile.md",
                            ["-Some line from the deleted file."],
                            is_delete=True, old_start=1, new_start=1)
    ok2, reasons2 = run_mechanical(d_del)
    check(ok2 is False, "a deleted file is never mechanical")
    check(any("new/renamed/deleted/binary" in r for r in reasons2), f"got {reasons2}")

    d_ren = make_file_diff("content/docs/renamed.md", BASE_CONTEXT,
                            rename_from="content/docs/original.md")
    ok3, reasons3 = run_mechanical(d_ren, files=[{"path": "content/docs/renamed.md"}])
    check(ok3 is False, "a renamed file is never mechanical")
    check(any("new/renamed/deleted/binary" in r for r in reasons3), f"got {reasons3}")

    d_bin = make_file_diff("content/docs/image.png", [], is_binary=True)
    ok4, reasons4 = run_mechanical(d_bin, files=[{"path": "content/docs/image.png"}],
                                    additions=0, deletions=0)
    check(ok4 is False, "a binary file is never mechanical")
    check(any("new/renamed/deleted/binary" in r for r in reasons4), f"got {reasons4}")
    assert_clean("test_condition_structural", before)


# ---- Condition 3: size caps (additions / files / deletions) -----------------


def test_condition_additions_boundary() -> None:
    print("test_condition_additions_boundary")
    before = len(_failures)
    d10 = make_file_diff("content/docs/foo.md", filler_lines(10))
    ok10, r10 = run_mechanical(d10)
    check(ok10 is True, f"exactly 10 additions is mechanical (strict >); reasons={r10}")

    d11 = make_file_diff("content/docs/foo.md", filler_lines(11))
    ok11, r11 = run_mechanical(d11)
    check(ok11 is False, "11 additions exceeds the mechanical cap")
    check(any("additions" in r and "exceed" in r for r in r11), f"got {r11}")
    assert_clean("test_condition_additions_boundary", before)


def test_condition_deletions_boundary() -> None:
    print("test_condition_deletions_boundary")
    before = len(_failures)
    d30 = make_file_diff("content/docs/foo.md", filler_lines(30, marker="-"))
    ok30, r30 = run_mechanical(d30)
    check(ok30 is True, f"exactly 30 deletions is mechanical (strict >); reasons={r30}")

    d31 = make_file_diff("content/docs/foo.md", filler_lines(31, marker="-"))
    ok31, r31 = run_mechanical(d31)
    check(ok31 is False, "31 deletions exceeds the mechanical cap")
    check(any("deletions" in r and "exceed" in r for r in r31), f"got {r31}")
    assert_clean("test_condition_deletions_boundary", before)


def test_condition_files_boundary() -> None:
    print("test_condition_files_boundary")
    before = len(_failures)
    two = "".join(make_file_diff(f"content/docs/p{i}.md", ["+One filler line for the fixture."])
                   for i in range(2))
    ok2, r2 = run_mechanical(two, files=[{"path": f"content/docs/p{i}.md"} for i in range(2)])
    check(ok2 is True, f"exactly 2 files is mechanical (strict >); reasons={r2}")

    three = "".join(make_file_diff(f"content/docs/p{i}.md", ["+One filler line for the fixture."])
                     for i in range(3))
    ok3, r3 = run_mechanical(three, files=[{"path": f"content/docs/p{i}.md"} for i in range(3)])
    check(ok3 is False, "3 files exceeds the mechanical cap of 2")
    check(any("file count" in r and "exceeds" in r for r in r3), f"got {r3}")
    assert_clean("test_condition_files_boundary", before)


# ---- Condition 4: code fence / shortcode -------------------------------------


def test_condition_code_and_shortcode() -> None:
    print("test_condition_code_and_shortcode")
    before = len(_failures)
    d_fence = body_diff("content/docs/foo.md", added=["+```python"])
    ok, reasons = run_mechanical(d_fence)
    check(ok is False, "an added code fence is never mechanical")
    check(any("code fence or shortcode" in r for r in reasons), f"got {reasons}")

    d_sc = body_diff("content/docs/foo.md", added=['+{{< notes type="tip" >}}'])
    ok2, reasons2 = run_mechanical(d_sc)
    check(ok2 is False, "an added shortcode is never mechanical")
    check(any("code fence or shortcode" in r for r in reasons2), f"got {reasons2}")
    assert_clean("test_condition_code_and_shortcode", before)


# ---- Condition 5: links -------------------------------------------------------


def test_condition_links() -> None:
    print("test_condition_links")
    before = len(_failures)

    # Removed/modified link: cleanly isolated (no accompanying claims hit —
    # the replacement text carries no URL).
    d_removed = body_diff(
        "content/docs/foo.md",
        removed=["-See [Stacks](/docs/iac/concepts/stacks/) for details."],
        added=["+See details in the stacks guide."],
    )
    ok, reasons = run_mechanical(d_removed)
    check(ok is False, "a removed/modified link is never mechanical")
    check(reasons == ["modified or removed link in: content/docs/foo.md"],
          f"isolated removed-link reason only; got {reasons}")

    # Added external link: fails condition 5 (url-type claims are exempt
    # from condition 7, so this is the only reason).
    d_ext = body_diff("content/docs/foo.md",
                       added=["+See [Kubernetes](https://kubernetes.io/docs/) for details."])
    ok2, reasons2 = run_mechanical(d_ext)
    check(ok2 is False, "an added external link is never mechanical")
    check(any("external/non-internal link added" in r for r in reasons2), f"got {reasons2}")

    # Added internal link that doesn't resolve.
    d_unresolved = body_diff("content/docs/foo.md",
                              added=["+See [Ghost](/docs/does/not/exist/) for details."])
    ok3, reasons3 = run_mechanical(d_unresolved)
    check(ok3 is False, "an added internal link that doesn't resolve is never mechanical")
    check(any("does not resolve" in r for r in reasons3), f"got {reasons3}")

    # Added internal link that DOES resolve: fully mechanical — the exact
    # "link fix" shape the lane exists for. Condition 5 passes it and the
    # url-type claims exemption keeps condition 7 out of the way.
    d_resolved = body_diff("content/docs/foo.md",
                            added=["+See [Stacks](/docs/iac/concepts/stacks/) for details."])
    ok4, reasons4 = run_mechanical(d_resolved)
    check(ok4 is True, f"a resolved internal link addition is mechanical; reasons={reasons4}")
    check(reasons4 == [], f"no reasons for a clean link fix; got {reasons4}")
    assert_clean("test_condition_links", before)


# ---- Condition 6: frontmatter keys -------------------------------------------


def test_condition_frontmatter_keys() -> None:
    print("test_condition_frontmatter_keys")
    before = len(_failures)

    # A disallowed key (title) changing — isolated from claims by avoiding
    # "new" and other trigger words in the value.
    d_title = make_file_diff("content/docs/foo.md", [
        "-title: Old title",
        "+title: Renamed title",
        " meta_desc: Something",
        " ---",
        " ",
    ], old_start=5, new_start=5)
    ok, reasons = run_mechanical(d_title)
    check(ok is False, "a disallowed frontmatter key change is never mechanical")
    check(reasons == ["frontmatter key(s) outside {updated, tags} changed: content/docs/foo.md (title)"],
          f"isolated bad-key reason only; got {reasons}")

    # Only `tags` changing (one of the two allowed keys) — mechanical,
    # with no frontmatter-condition reason at all.
    d_tags = make_file_diff("content/docs/foo.md", [
        " title: Something",
        " tags:",
        "-  - iac",
        "+  - iac",
        "+  - stacks",
        " ---",
        " ",
    ], old_start=5, new_start=5)
    ok2, reasons2 = run_mechanical(d_tags)
    check(ok2 is True, f"a tags-only frontmatter change is mechanical; reasons={reasons2}")
    check(reasons2 == [], f"no reasons for a clean tags-only change; got {reasons2}")
    assert_clean("test_condition_frontmatter_keys", before)


# ---- Condition 7: claims signal (pricing-sensitive paths + Layer A) ---------


def test_condition_claims_signal() -> None:
    print("test_condition_claims_signal")
    before = len(_failures)

    d = body_diff("content/docs/foo.md",
                   added=["+This is the recommended approach for managing state."])
    ok, reasons = run_mechanical(d)
    check(ok is False, "a Layer-A claim trigger on an added line is never mechanical")
    check(any("claim-extraction signal" in r for r in reasons), f"got {reasons}")

    d_pricing = make_file_diff("data/pulumi_pricing.yaml", [" some: value", "+another: value"])
    ok2, reasons2 = run_mechanical(d_pricing, files=[{"path": "data/pulumi_pricing.yaml"}])
    check(ok2 is False, "a pricing-sensitive file change is never mechanical")
    check(any("pricing-sensitive" in r for r in reasons2), f"got {reasons2}")

    # The exemptions: an `updated:` date bump and a tags list item are the
    # condition-6-governed shapes and must not trip the claims signal.
    d_updated = make_file_diff("content/docs/foo.md", [
        " title: Something",
        "-updated: 2025-01-15",
        "+updated: 2026-08-31",
        " ---",
        " ",
    ], old_start=5, new_start=5)
    ok3, reasons3 = run_mechanical(d_updated)
    check(ok3 is True, f"an updated:-only bump is mechanical; reasons={reasons3}")

    # A prose claim with real claim shape (a price) still disqualifies even
    # in an otherwise-clean tiny diff.
    d_price = body_diff("content/docs/foo.md",
                         added=["+The Team edition costs $50 per month for 10 members."])
    ok4, reasons4 = run_mechanical(d_price)
    check(ok4 is False and any("claim-extraction signal" in r for r in reasons4),
          f"a prose pricing claim is never mechanical; got {reasons4}")
    assert_clean("test_condition_claims_signal", before)


def main() -> int:
    tests = [
        test_all_pass_is_mechanical,
        test_condition_domain,
        test_condition_structural,
        test_condition_additions_boundary,
        test_condition_deletions_boundary,
        test_condition_files_boundary,
        test_condition_code_and_shortcode,
        test_condition_links,
        test_condition_frontmatter_keys,
        test_condition_claims_signal,
    ]
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
