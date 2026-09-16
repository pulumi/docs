#!/usr/bin/env python3
"""Tests for gh_client.py — backend selection, the snapshot layout, REST
pagination, and the GitHub-App author rewrite.

Runs under pytest (make test-review-pipeline) and standalone via
`gh_client.py --self-test` (run_standalone below, the test_sla_sweep.py
convention: no pytest fixtures, each test opens its own tempdir).
"""

from __future__ import annotations

import io
import json
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import gh_client  # noqa: E402
from gh_client import GhClient, GhNotFound, norm_login, search_author_q, snapshot_path  # noqa: E402


def test_search_author_q_rewrites_apps():
    assert search_author_q("workprentice[bot]") == "author:app/workprentice"
    assert search_author_q("app/workprentice") == "author:app/workprentice"
    assert search_author_q("pulumi-bot") == "author:pulumi-bot"
    assert search_author_q("CamSoper") == "author:CamSoper"


def test_norm_login_collapses_app_forms():
    assert norm_login("workprentice[bot]") == norm_login("app/workprentice") == norm_login("WorkPrentice")
    assert norm_login(None) == ""


def test_snapshot_path_is_stable_and_readable():
    p = snapshot_path(Path("/s"), "get", "repos/pulumi/docs/pulls", {"state": "open", "per_page": 100})
    assert p == Path("/s/GET/repos/pulumi/docs/pulls__per_page=100&state=open.json")
    assert snapshot_path(Path("/s"), "GET", "/repos/x/y/pulls/1", None) == Path("/s/GET/repos/x/y/pulls/1.json")


def test_pick_backend_prefers_snapshot_then_gh_then_rest():
    assert gh_client.pick_backend(snapshot_dir=Path("/x"), token="t") == "snapshot"
    saved = gh_client.shutil.which
    try:
        gh_client.shutil.which = lambda _: "/usr/bin/gh"
        assert gh_client.pick_backend(token=None) == "gh"
        gh_client.shutil.which = lambda _: None
        assert gh_client.pick_backend(token="t") == "rest"
        try:
            gh_client.pick_backend(token=None)
            raise AssertionError("expected GhError")
        except gh_client.GhError:
            pass
    finally:
        gh_client.shutil.which = saved


def test_snapshot_reads_and_records_writes():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        f = snapshot_path(root, "GET", "repos/pulumi/docs/pulls/7", None)
        f.parent.mkdir(parents=True)
        f.write_text(json.dumps({"number": 7, "head": {"sha": "a" * 40}}))
        # paginated list fixture named without per_page: the slim retry finds it
        lst = snapshot_path(root, "GET", "repos/pulumi/docs/pulls/7/files", None)
        lst.parent.mkdir(parents=True)
        lst.write_text(json.dumps([{"filename": "content/docs/a.md"}]))
        gh = GhClient("pulumi/docs", "snapshot", snapshot_dir=root)
        assert gh.pr(7)["number"] == 7
        assert gh.pr_files(7)[0]["filename"] == "content/docs/a.md"
        try:
            gh.pr(8)
            raise AssertionError("expected GhNotFound")
        except GhNotFound:
            pass
        gh.comment(7, "hello")
        gh.merge(7, "a" * 40)
        lines = [json.loads(l) for l in (root / "writes.jsonl").read_text().splitlines()]
        assert [l["method"] for l in lines] == ["POST", "PUT"]
        assert lines[1]["body"] == {"sha": "a" * 40, "merge_method": "squash"}
        assert len(gh.writes) == 2


def test_contents_decodes_base64_and_none_on_404():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        f = snapshot_path(root, "GET", "repos/pulumi/docs/contents/content/blog/x/index.md", {"ref": "abc"})
        f.parent.mkdir(parents=True)
        import base64
        f.write_text(json.dumps({"encoding": "base64", "content": base64.b64encode(b"---\ndate: 2026-09-01\n---\n").decode()}))
        gh = GhClient("pulumi/docs", "snapshot", snapshot_dir=root)
        assert gh.contents("content/blog/x/index.md", "abc").startswith("---\ndate:")
        assert gh.contents("content/blog/missing.md", "abc") is None


class _FakeResp(io.BytesIO):
    def __init__(self, payload, headers):
        super().__init__(json.dumps(payload).encode())
        self.headers = headers
        self.status = 200

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


def test_rest_pagination_follows_link_header():
    calls = []

    def fake_urlopen(req, timeout=0):
        calls.append(req.full_url)
        assert req.get_header("Authorization") == "Bearer tok"
        if "page=2" in req.full_url:
            return _FakeResp([{"number": 2}], {})
        return _FakeResp([{"number": 1}], {"Link": '<https://api.github.com/repos/pulumi/docs/pulls?page=2>; rel="next"'})

    saved = gh_client.urllib.request.urlopen
    try:
        gh_client.urllib.request.urlopen = fake_urlopen
        gh = GhClient("pulumi/docs", "rest", token="tok")
        assert [p["number"] for p in gh.list_open_prs()] == [1, 2]
        assert len(calls) == 2
    finally:
        gh_client.urllib.request.urlopen = saved


def test_record_dir_mirrors_live_responses():
    def fake_urlopen(req, timeout=0):
        return _FakeResp({"number": 5}, {})

    saved = gh_client.urllib.request.urlopen
    try:
        gh_client.urllib.request.urlopen = fake_urlopen
        with tempfile.TemporaryDirectory() as td:
            gh = GhClient("pulumi/docs", "rest", token="tok", record_dir=td)
            assert gh.pr(5)["number"] == 5
            replay = GhClient("pulumi/docs", "snapshot", snapshot_dir=td)
            assert replay.pr(5)["number"] == 5
    finally:
        gh_client.urllib.request.urlopen = saved


def test_concat_json_docs_flattens_gh_paginate_output():
    assert gh_client._concat_json_docs('[1,2]\n[3]') == [1, 2, 3]
    assert gh_client._concat_json_docs('{"a":1}') == {"a": 1}
    assert gh_client._concat_json_docs("") is None


def run_standalone() -> int:
    """The --self-test harness; test list bound at call time (test_sentinel.py)."""
    import inspect  # noqa: PLC0415
    all_tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    failures = 0
    for t in all_tests:
        if inspect.signature(t).parameters:
            print(f"  skip: {t.__name__} (pytest fixtures; run via pytest)")
            continue
        try:
            t()
            print(f"  ok: {t.__name__}")
        except AssertionError as exc:
            failures += 1
            print(f"  FAIL: {t.__name__}: {exc}", file=sys.stderr)
        except Exception as exc:  # noqa: BLE001
            failures += 1
            print(f"  FAIL: {t.__name__}: {type(exc).__name__}: {exc}", file=sys.stderr)
    if failures:
        print(f"{failures} gh_client test(s) failed", file=sys.stderr)
        return 1
    print("all gh_client self-tests passed")
    return 0


if __name__ == "__main__":
    sys.exit(run_standalone())
