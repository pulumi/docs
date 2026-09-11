"""link-check-diff.py: dead-internal-link detection over a PR diff.

The production probe is mocked everywhere: a local miss is only "dead" when
the probe says 404/410, and the tests must never touch the network.
"""

from __future__ import annotations

import importlib.util
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _load():
    spec = importlib.util.spec_from_file_location("link_check_diff", HERE / "link-check-diff.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


lc = _load()

PROBE_TABLE = {
    "/docs/zzz": "dead-404",
    "/blog/nope": "dead-404",
    "/blog/author/lee-zen": "live-200",
    "/blog/series/platform-engineering-pillars": "live-200",
    "/docs/reference/cloud-rest-api/audit-logs": "live-200",
    "/docs/reference/pkg/aws": "live-200",
    "/blog/tag/neo-things": "live-301",
    "/docs/flaky": "unknown",
}


def fake_probe(path: str) -> str:
    return PROBE_TABLE.get(path, "dead-404")


HEAD_PAGE = """---
title: A
---
[live](/docs/a/page/) [alias](/docs/old-b/#frag) [dead](/docs/zzz/)
`[in code](/docs/nope/)` and a fence:
```
[fenced](/docs/nope2/)
```
[placeholder](/docs/<thing>/) [added](/docs/new/) [blog](/blog/nope/)
"""


def _repo(tmp_path: Path) -> Path:
    """A checkout at the PR head, like the workflow's: files carry the NEW content."""
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    (tmp_path / "content/docs/a").mkdir(parents=True)
    (tmp_path / "content/docs/a/page.md").write_text(HEAD_PAGE)
    (tmp_path / "content/docs/b").mkdir(parents=True)
    (tmp_path / "content/docs/b/_index.md").write_text("---\ntitle: B\naliases:\n- /docs/old-b/\n---\n")
    subprocess.run(["git", "add", "-A"], cwd=tmp_path, check=True)
    return tmp_path


DIFF = """diff --git a/content/docs/a/page.md b/content/docs/a/page.md
--- a/content/docs/a/page.md
+++ b/content/docs/a/page.md
@@ -3,1 +3,7 @@
 ---
+[live](/docs/a/page/) [alias](/docs/old-b/#frag) [dead](/docs/zzz/)
+`[in code](/docs/nope/)` and a fence:
+```
+[fenced](/docs/nope2/)
+```
+[placeholder](/docs/<thing>/) [added](/docs/new/) [blog](/blog/nope/)
-[removed](/docs/removed-dead/)
diff --git a/content/docs/new.md b/content/docs/new.md
new file mode 100644
--- /dev/null
+++ b/content/docs/new.md
@@ -0,0 +1,1 @@
+---
"""


def _one_line_diff(line: str) -> str:
    return f"""diff --git a/content/docs/a/page.md b/content/docs/a/page.md
--- a/content/docs/a/page.md
+++ b/content/docs/a/page.md
@@ -3,1 +3,2 @@
 ---
+{line}
"""


def test_only_dead_links_on_added_lines_are_reported(tmp_path):
    dead = lc.check(DIFF, _repo(tmp_path), fake_probe)
    assert [(e["target"], e["line"]) for e in dead] == [("/docs/zzz/", 4), ("/blog/nope/", 9)]
    assert all(e["file"] == "content/docs/a/page.md" for e in dead)
    assert all(e["resolution"] == "dead-404" for e in dead)


def test_every_resolution_is_recorded(tmp_path):
    entries = lc.classify(DIFF, _repo(tmp_path), fake_probe)
    res = {e["target"]: e["resolution"] for e in entries}
    assert res == {
        "/docs/a/page/": "local",
        "/docs/old-b/#frag": "alias",
        "/docs/zzz/": "dead-404",
        "/docs/<thing>/": "placeholder",
        "/docs/new/": "added-by-pr",
        "/blog/nope/": "dead-404",
    }


def test_image_references_and_asset_targets_are_skipped(tmp_path):
    root = _repo(tmp_path)
    diff = _one_line_diff("![shot](/blog/post/shot.png) [pdf](/docs/guide.pdf) [gif](/docs/x/anim.gif) [page](/docs/zzz/)")
    entries = lc.classify(diff, root, fake_probe)
    assert [e["target"] for e in entries] == ["/docs/zzz/"]


def test_url_spaces_without_a_content_file_are_live_when_production_says_so(tmp_path):
    root = _repo(tmp_path)
    diff = _one_line_diff(
        "[author](/blog/author/lee-zen/) [series](/blog/series/platform-engineering-pillars/) "
        "[adapter](/docs/reference/cloud-rest-api/audit-logs/) [pkg](/docs/reference/pkg/aws/) "
        "[redirected](/blog/tag/neo-things/) [dead](/docs/zzz/)"
    )
    entries = lc.classify(diff, root, fake_probe)
    res = {e["target"]: e["resolution"] for e in entries}
    assert res["/blog/author/lee-zen/"] == "live-200"
    assert res["/blog/series/platform-engineering-pillars/"] == "live-200"
    assert res["/docs/reference/cloud-rest-api/audit-logs/"] == "live-200"
    assert res["/docs/reference/pkg/aws/"] == "live-200"
    assert res["/blog/tag/neo-things/"] == "live-301"
    assert [e["target"] for e in lc.dead_only(entries)] == ["/docs/zzz/"]


def test_unknown_probe_outcome_is_never_reported(tmp_path):
    root = _repo(tmp_path)
    diff = _one_line_diff("[flaky](/docs/flaky/) [dead](/docs/zzz/)")
    entries = lc.classify(diff, root, fake_probe)
    assert {e["target"]: e["resolution"] for e in entries} == {"/docs/flaky/": "unknown", "/docs/zzz/": "dead-404"}
    assert [e["target"] for e in lc.dead_only(entries)] == ["/docs/zzz/"]
    # No probe at all: nothing is dead.
    assert lc.dead_only(lc.classify(diff, root, None)) == []


def test_integrity_line_shape_is_what_the_composer_parses(tmp_path):
    dead = lc.check(DIFF, _repo(tmp_path), fake_probe)
    line = lc.as_integrity_line(dead[0])
    assert line.startswith("content/docs/a/page.md:4: dead internal link /docs/zzz/")
    assert "production answers 404" in line


def test_merge_into_records_a_run_and_keeps_the_skip_stub(tmp_path):
    art = tmp_path / ".hugo-build.json"
    art.write_text(json.dumps({"skipped": True, "link_integrity": [], "stats": {"link_integrity_count": 0}}))
    entries = lc.classify(DIFF, _repo(tmp_path), fake_probe)
    dead = lc.dead_only(entries)
    data = lc.merge_into(art, dead, checked=len(entries), error=None, resolutions=lc._histogram(entries))
    assert data["skipped"] is True
    assert data["link_check"]["ran"] is True
    assert data["link_check"]["checked"] == 6 and data["link_check"]["dead"] == 2
    assert data["link_check"]["unknown"] == 0
    assert data["link_check"]["resolutions"]["dead-404"] == 2
    assert data["stats"]["link_integrity_count"] == 2
    assert len(data["link_integrity"]) == 2


def test_merge_into_names_an_unrun_check(tmp_path):
    art = tmp_path / ".hugo-build.json"
    data = lc.merge_into(art, None, checked=0, error="RuntimeError: gh exploded")
    assert data["link_check"]["ran"] is False
    assert "gh exploded" in data["link_check"]["error"]
    assert data["link_integrity"] == []


def test_non_content_files_are_ignored(tmp_path):
    diff = """diff --git a/layouts/x.html b/layouts/x.html
--- a/layouts/x.html
+++ b/layouts/x.html
@@ -1,1 +1,2 @@
 x
+<a href="/docs/zzz/">[z](/docs/zzz/)</a>
"""
    assert lc.check(diff, _repo(tmp_path), fake_probe) == []


def test_fence_state_comes_from_the_file_at_head(tmp_path):
    """A hunk that opens on the closing fence of a block started above it
    reads inverted on its own (how the first cut missed #21560's dead link)."""
    root = _repo(tmp_path)
    page = tmp_path / "content/docs/c.md"
    page.write_text("---\ntitle: C\n---\n```\nold\n```\n\n[dead](/docs/zzz/)\n")
    diff = """diff --git a/content/docs/c.md b/content/docs/c.md
--- a/content/docs/c.md
+++ b/content/docs/c.md
@@ -6,1 +6,3 @@ old
 ```
+
+[dead](/docs/zzz/)
"""
    assert [(e["target"], e["line"]) for e in lc.check(diff, root, fake_probe)] == [("/docs/zzz/", 8)]
    links_without_file, _ = lc.added_links(diff, None)
    assert links_without_file == []  # the fallback's known blind spot, not a wrong answer


def test_probe_maps_status_codes(monkeypatch):
    import urllib.error

    class _Resp:
        def __init__(self, status):
            self.status = status

        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

    def fake_urlopen(req, timeout=0):
        path = req.full_url.replace(lc.PROBE_BASE, "")
        if path == "/gone/":
            raise urllib.error.HTTPError(req.full_url, 410, "gone", {}, None)
        if path == "/missing/":
            raise urllib.error.HTTPError(req.full_url, 404, "nf", {}, None)
        if path == "/broken/":
            raise urllib.error.HTTPError(req.full_url, 503, "down", {}, None)
        if path == "/timeout/":
            raise urllib.error.URLError("timed out")
        return _Resp(200)

    monkeypatch.setattr(lc.urllib.request, "urlopen", fake_urlopen)
    assert lc.probe("/gone") == "dead-410"
    assert lc.probe("/missing") == "dead-404"
    assert lc.probe("/broken") == "unknown"
    assert lc.probe("/timeout") == "unknown"
    assert lc.probe("/docs/ok") == "live-200"


def test_self_test_passes():
    proc = subprocess.run(["python3", str(HERE / "link-check-diff.py"), "--self-test"], capture_output=True, text=True)
    assert proc.returncode == 0, proc.stderr
