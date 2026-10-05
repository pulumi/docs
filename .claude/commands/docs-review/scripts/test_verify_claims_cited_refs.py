"""Tests for author-cited product-source refs in a docs PR body.

`parse_impl_refs` used to capture only implementing changes (`pulumi/<repo>#<n>`
and pull/commit URLs), so a PR that cited the source file backing each claim
(pulumi/docs#22056: five `blob/<sha>/<path>#L<a>-L<b>` links) handed the
verifier nothing. And a blob read through `gh_query` was cut at GH_OUTPUT_CAP,
which in that PR's env.go fell before the cited lines — so the `lines` slice
is part of the same fix.
"""

from __future__ import annotations

import importlib.util
import json
import subprocess
from pathlib import Path

SPEC = importlib.util.spec_from_file_location(
    "verify_claims", Path(__file__).parent / "verify-claims.py")
vc = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(vc)

SHA = "fb0efa39bc56d373178cab2bd92ffe661852bc61"
ENV_GO = f"https://github.com/pulumi/pulumi/blob/{SHA}/sdk/go/common/env/env.go#L224-L264"
TEMPLATES_GO = f"https://github.com/pulumi/pulumi/blob/{SHA}/pkg/cmd/pulumi/templates/project_templates.go#L47-L123"
CHANGELOG = f"https://github.com/pulumi/pulumi/blob/{SHA}/changelog/v3.199.0.md"

PR_22056_BODY = f"""Source of truth in pulumi/pulumi:
- [`sdk/go/common/env/env.go`]({ENV_GO}): variable definitions
- [`pkg/cmd/pulumi/templates/project_templates.go`]({TEMPLATES_GO}): compile-time defaults
- Changelogs: [v3.199.0]({CHANGELOG}) (repository and branch overrides)
"""


def _strip_scheme(url: str) -> str:
    return url.removeprefix("https://")


def test_blob_links_in_markdown_are_captured_whole():
    refs = vc.parse_impl_refs(PR_22056_BODY)
    assert refs == [_strip_scheme(ENV_GO), _strip_scheme(TEMPLATES_GO), _strip_scheme(CHANGELOG)]


def test_implementing_changes_come_before_source_files():
    body = f"See {ENV_GO}. Ships in pulumi/pulumi#23691 and github.com/pulumi/pulumi/commit/abc123."
    refs = vc.parse_impl_refs(body)
    assert refs[:2] == ["pulumi/pulumi#23691", "github.com/pulumi/pulumi/commit/abc123"]
    assert refs[2] == _strip_scheme(ENV_GO)


def test_trailing_sentence_punctuation_and_duplicates_are_dropped():
    body = f"Defined in {CHANGELOG}. Also {CHANGELOG}, again."
    assert vc.parse_impl_refs(body) == [_strip_scheme(CHANGELOG)]


def test_refs_are_capped():
    body = "\n".join(f"https://github.com/pulumi/pulumi/blob/{SHA}/f{i}.go" for i in range(20))
    assert len(vc.parse_impl_refs(body)) == vc.MAX_IMPL_REFS


def test_bare_issue_numbers_and_other_orgs_are_ignored():
    body = "Fixes #123. See https://github.com/hashicorp/terraform/blob/main/main.go#L1."
    assert vc.parse_impl_refs(body) == []


def test_read_hint_for_anchored_blob_pads_the_range():
    hint = vc.impl_ref_read_hint(_strip_scheme(ENV_GO))
    args = json.loads(hint.split("gh_query args ", 1)[1].split(", lines", 1)[0])
    assert args == ["api", "-H", "Accept: application/vnd.github.raw",
                    f"repos/pulumi/pulumi/contents/sdk/go/common/env/env.go?ref={SHA}"]
    assert hint.endswith('lines "219-269"')


def test_read_hint_without_anchor_has_no_lines():
    hint = vc.impl_ref_read_hint(_strip_scheme(CHANGELOG))
    assert "contents/changelog/v3.199.0.md?ref=" in hint and "lines" not in hint


def test_read_hint_is_empty_for_non_blob_refs():
    assert vc.impl_ref_read_hint("pulumi/pulumi#23691") == ""
    assert vc.impl_ref_read_hint(f"github.com/pulumi/pulumi/tree/{SHA}/sdk") == ""


def test_user_message_lists_refs_with_read_hint_in_pass1_only():
    claim = {"file": "content/docs/iac/cli/environment-variables.md", "line_range": "10",
             "type": "default", "text": "PULUMI_TEMPLATE_BRANCH defaults to master."}
    refs = vc.parse_impl_refs(PR_22056_BODY)
    pass1 = vc.build_user_message(claim, "pass1", None, impl_refs=refs)
    assert "cites product source" in pass1
    assert f"- {_strip_scheme(ENV_GO)} — read with gh_query args" in pass1
    pass3 = vc.build_user_message(claim, "pass3", None, impl_refs=refs)
    assert f"- {_strip_scheme(ENV_GO)}\n" in pass3 + "\n" and "gh_query args" not in pass3
    assert "cites product source" not in vc.build_user_message(claim, "pass2", None, impl_refs=refs)


def test_slice_lines_numbers_the_requested_range():
    text = "\n".join(f"line {i}" for i in range(1, 11))
    assert vc.slice_lines(text, "3-4") == "3: line 3\n4: line 4"
    assert vc.slice_lines(text, "10") == "10: line 10"
    assert vc.slice_lines(text, "9-50") == "9: line 9\n10: line 10"
    assert "past the end" in vc.slice_lines(text, "40-50")
    assert vc.slice_lines(text, "nope").startswith("(ignored malformed")


def test_gh_query_slices_before_the_output_cap(monkeypatch):
    # The cited range sits past GH_OUTPUT_CAP chars, as env.go#L224 did.
    filler = "x" * 200
    raw = "\n".join(f"{filler} {i}" for i in range(1, 301))
    assert len(raw) > vc.GH_OUTPUT_CAP

    def fake_run(cmd, **kw):
        return subprocess.CompletedProcess(cmd, 0, stdout=raw, stderr="")

    monkeypatch.setattr(vc.subprocess, "run", fake_run)
    whole = vc.exec_gh_query({"args": ["api", "repos/pulumi/pulumi/contents/x.go"]})
    assert f"{filler} 250" not in whole
    sliced = vc.exec_gh_query({"args": ["api", "repos/pulumi/pulumi/contents/x.go"], "lines": "249-251"})
    assert sliced == f"249: {filler} 249\n250: {filler} 250\n251: {filler} 251"


def test_gh_query_does_not_slice_an_error(monkeypatch):
    def fake_run(cmd, **kw):
        return subprocess.CompletedProcess(cmd, 1, stdout="", stderr="HTTP 404: Not Found")

    monkeypatch.setattr(vc.subprocess, "run", fake_run)
    out = vc.exec_gh_query({"args": ["api", "repos/pulumi/pulumi/contents/nope.go"], "lines": "1-5"})
    assert "HTTP 404" in out
