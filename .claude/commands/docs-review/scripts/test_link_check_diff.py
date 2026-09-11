"""link-check-diff.py: dead-internal-link detection over a PR diff."""

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


def test_only_dead_links_on_added_lines_are_reported(tmp_path):
    dead = lc.check(DIFF, _repo(tmp_path))
    assert [(e["target"], e["line"]) for e in dead] == [("/docs/zzz/", 4), ("/blog/nope/", 9)]
    assert all(e["file"] == "content/docs/a/page.md" for e in dead)


def test_integrity_line_shape_is_what_the_composer_parses(tmp_path):
    dead = lc.check(DIFF, _repo(tmp_path))
    line = lc.as_integrity_line(dead[0])
    assert line.startswith("content/docs/a/page.md:4: dead internal link /docs/zzz/")


def test_merge_into_records_a_run_and_keeps_the_skip_stub(tmp_path):
    art = tmp_path / ".hugo-build.json"
    art.write_text(json.dumps({"skipped": True, "link_integrity": [], "stats": {"link_integrity_count": 0}}))
    dead = lc.check(DIFF, _repo(tmp_path))
    data = lc.merge_into(art, dead, checked=6, error=None)
    assert data["skipped"] is True
    assert data["link_check"] == {"ran": True, "checked": 6, "dead": 2}
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
    assert lc.check(diff, _repo(tmp_path)) == []


def test_self_test_passes():
    proc = subprocess.run(["python3", str(HERE / "link-check-diff.py"), "--self-test"], capture_output=True, text=True)
    assert proc.returncode == 0, proc.stderr


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
    assert [(e["target"], e["line"]) for e in lc.check(diff, root)] == [("/docs/zzz/", 8)]
    links_without_file, _ = lc.added_links(diff, None)
    assert links_without_file == []  # the fallback's known blind spot, not a wrong answer
