#!/usr/bin/env python3
"""Tests for render.py — escaping, no network, grouping, clusters pinned
first, the command composer, detail deep links, both theme selectors, and
the terminal table.

Runs under pytest and standalone via `render.py --self-test`. No pytest
fixtures; the queue is built with test_analyze.run() so the renderer sees
exactly what analyze.py writes.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import render  # noqa: E402
from test_analyze import CLEAN_AUTHOR, CLEAN_BRIEF, HEAD_V3, _file, cfg, comment, row, run, stampable  # noqa: E402
from test_collect import V3_AUTHOR, V3_BRIEF  # noqa: E402


def _queue() -> dict:
    a = stampable(1, title="Fix the intro <script>alert(1)</script>", files=[_file("content/docs/a.md", ["x"], ["o"], old_start=10)])
    b = stampable(2, title="Reword the intro", files=[_file("content/docs/a.md", ["y"], ["o"], old_start=10)])
    c = stampable(3, title="Blog copy edit", labels=["review:no-blockers", "domain:blog"],
                  files=[_file("content/blog/p/index.md", ["z"], ["p"])], comments=[comment(V3_BRIEF), comment(V3_AUTHOR)])
    d = stampable(4, title="Dirty one", mergeable_state="dirty")
    q = run([a, b, c, d], cfg=cfg(me=["docs"]))
    row(q, 3)["judgments"] = [{"finding_id": "F4", "file": "content/docs/iac/x.md", "line": 95,
                              "quote_minus": ["old <b>"], "quote_plus": ["new"], "decision": "Keep the widened claim?",
                              "disposition": "refuted", "deep_link": "https://github.com/pulumi/docs/pull/3/files#diff-xR95"}]
    return q


def test_board_escapes_everything_and_never_calls_github():
    html = render.render_board(_queue())
    assert "<script>alert(1)</script>" not in html and "&lt;script&gt;alert(1)&lt;/script&gt;" in html
    assert "api.github.com" not in html and "fetch(" not in html and "XMLHttpRequest" not in html
    assert 'id="queue"' in html and "<\\/script>" not in html.split('id="queue">')[1].split("</script>")[0].replace("<\\/", "")


def test_board_groups_owner_then_domain_and_pins_clusters_first():
    html = render.render_board(_queue())
    assert html.index("Collisions first") < html.index('class="grp"')
    heads = re.findall(r'<div class="sec-head"><h2>([^<]+)</h2><span class="dlabel">([^<]+)</span>', html)
    assert heads[0][0] == "mine" and ("marketing", "blog") in heads
    assert "C1 · 2 PRs · overlap" in html and "Merge order:" in html


def test_board_rows_carry_verdict_chips_reasons_and_actions():
    html = render.render_board(_queue())
    assert 'data-verdict="judge"' in html and 'data-verdict="route"' in html and 'data-verdict="blocked"' in html
    assert 'class="chip r-collision"' in html and 'class="chip r-mergeable"' in html
    assert 'data-cmd="--unblock 4"' in html and 'data-cmd="--route 3:@TODO-named-fallback"' in html
    assert 'data-cmd="--stamp 1 --force"' in html  # judge rows keep approve-as-is
    assert '<div class="jbox">' in html and "Keep the widened claim?" in html and 'class="del">- old &lt;b&gt;' in html
    assert 'href="https://github.com/pulumi/docs/pull/3/files#diff-xR95"' in html
    assert "Blocked: mergeable:dirty" in html


def test_stamp_rows_are_prechecked_and_command_footer_exists():
    q = run([stampable(7)])
    html = render.render_board(q)
    assert 'data-cmd="--stamp 7" data-pr="7" checked' in html
    assert 'id="cmd">$ /pr-review --act</div>' in html and 'id="copy"' in html


def test_theme_selectors_present_in_both_forms():
    html = render.render_board(_queue())
    assert '@media (prefers-color-scheme:dark){:root:not([data-theme="light"])' in html
    assert ':root[data-theme="dark"]' in html
    assert "--go:" in html and "--route:" in html


def test_detail_view_has_findings_deep_links_files_and_preview():
    q = _queue()
    pr = row(q, 3)
    pr["preview"] = {"url": "http://x", "status": "ready", "pages": [{"file": "content/blog/p/index.md", "title": "P", "url": "/blog/p/", "preview_url": "http://x/blog/p/"}], "non_content_files": []}
    html = render.render_detail(q, 3)
    assert "<h5>Findings (" in html and "#diff-" in html and 'href="http://x/blog/p/"' in html
    assert "<h5>Files</h5>" in html and "content/blog/p/index.md" in html
    try:
        render.render_detail(q, 999)
        raise AssertionError("expected SystemExit")
    except SystemExit:
        pass


def test_payload_is_slimmed():
    q = _queue()
    html = render.render_board(q)
    payload = json.loads(html.split('id="queue">')[1].split("</script>")[0].replace("<\\/", "</"))
    assert "patch" not in payload["prs"][0]["files"][0] and "author_body" not in payload["prs"][0]["review"]
    assert payload["prs"][0]["verdict"] in render.VERDICT_ORDER


def test_terminal_table_and_stamp_command():
    q = run([stampable(7), stampable(8, title="Another page", mergeable_state="dirty",
                                     files=[_file("content/docs/b.md", ["x"], ["o"])])])
    text = render.render_terminal(q)
    assert "2 rows" in text and "     7  stamp" in text and "     8  blocked" in text
    assert text.rstrip().endswith("$ /pr-review --act --stamp 7")
    one = render.render_terminal(q, 8)
    assert "1 rows" in one and "     7  stamp" not in one


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
        print(f"{failures} render test(s) failed", file=sys.stderr)
        return 1
    print("all render self-tests passed")
    return 0


if __name__ == "__main__":
    sys.exit(run_standalone())
