#!/usr/bin/env python3
"""Tests for render.py — escaping, no network, grouping, clusters pinned
first, the command composer, detail deep links, both theme selectors, and
the terminal table.

Runs under pytest and standalone via `render.py --self-test`. No pytest
fixtures; the queue is built with test_analyze.run() so the renderer sees
exactly what analyze.py writes.
"""

from __future__ import annotations

import inspect
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
    assert html.index("Do next") < html.index('class="grp"') < html.index("Collisions · 1 cluster")  # clusters fold at the bottom
    heads = re.findall(r'<div class="sec-head"><h2>([^<]+)</h2><span class="dlabel">([^<]+)</span>', html)
    assert heads[0][0] == "mine" and ("marketing", "blog") in heads
    assert "C1 · 2 of 2 PRs mine · overlap" in html and "Merge order:" in html
    assert "#1 and 1 other edit the same lines in the same files" in html
    assert 'data-cmd="--stamp 1 --force --unblock 2"' in html or 'data-cmd="--stamp 1 --unblock 2"' in html
    assert "Approves and squash-merges #1, then merges master into #2 so it can follow." in html


def test_board_rows_carry_verdict_chips_reasons_and_actions():
    html = render.render_board(_queue())
    assert 'data-verdict="judge"' in html and 'data-verdict="route"' in html and 'data-verdict="blocked"' in html
    assert 'class="chip r-cluster"' in html and 'class="chip r-mergeable"' in html
    assert 'data-cmd="--unblock 4"' in html and 'data-cmd="--route 3:@pulumi/docs-marketing-review"' in html
    assert 'class="btn p p-go" data-cmd="--stamp 1 --force"' in html  # judge rows keep approve-as-is, unselected, primary
    assert 'data-cmd="--request-changes 1"' in html and "send back to author" in html
    assert '<div class="jbox">' in html and "Keep the widened claim?" in html and 'class="del">- old &lt;b&gt;' in html
    assert 'href="https://github.com/pulumi/docs/pull/3/files#diff-xR95"' in html
    assert "Blocked: mergeable:dirty" in html
    assert '<summary>why · ' in html and 'more reasons for this verdict' in html  # informational chips fold
    assert 'class="chip r-risk"' in html.split('<summary>why · ')[1]  # and risk is one of them


def test_route_chip_keeps_its_model_span_as_markup():
    q = _queue()
    row(q, 3)["recommended"] = "stamp"  # what a judgments file carried before a re-analyze turned the row into a route
    html = render.render_board(q)
    assert '>route → @pulumi/docs-marketing-review <span class="v v-dim" title="The judge pass recommends stamp' in html
    assert 'model: stamp</span></span>' in html
    assert "&lt;span" not in html.split('data-pr="3"')[1].split("</h4>")[0]


def test_filter_chips_are_literal_and_an_empty_board_says_so():
    html = render.render_board(_queue())
    assert 'id="empty" hidden>' in html and 'id="reset-filters"' in html
    assert "function has(kind, val)" in html and "anyOn(" not in html
    assert "has('view', r.dataset.verdict)" in html


def test_rerun_is_the_unblock_on_an_errored_row_and_a_side_action_elsewhere():
    q = run([stampable(8, labels=["review:error", "domain:docs"]), stampable(9, labels=["review:trivial", "domain:docs"], comments=[])])
    html = render.render_board(q)
    assert 'class="btn p p-stop" data-cmd="--rerun 8" data-pr="8" data-kind="decision"' in html
    assert 'data-cmd="--rerun 9" data-pr="9" data-kind="side"' in html and "run a full review" in html


def test_an_unjudged_row_still_shows_the_diff():
    # Before the judge step runs, a finding is still a claim about a line of
    # the diff: the box quotes that line rather than describing it.
    q = _queue()
    p = row(q, 1)              # a judge row, with the judge step not yet run
    p["judgments"] = []
    p["review"] = {**(p.get("review") or {}), "items": [
        {"id": "F1", "bucket": "reviewer-check", "file": "content/docs/iac/x.md", "anchor": "L95",
         "summary": "Does this sentence still say what the link says?"}]}
    p["files"] = [{"path": "content/docs/iac/x.md", "status": "modified", "additions": 1, "deletions": 1,
                   "patch": "@@ -93,3 +93,3 @@\n ctx\n-the old sentence\n+the new sentence\n ctx2"}]
    html = render.render_board(q)
    assert "1 open finding, not yet judged" in html and "adds a recommended disposition" in html
    # the box no longer repeats the row's chips, and the finding is whole
    assert "not yet judged: " not in html
    assert "Does this sentence still say what the link says?" in html
    box = html.split('data-pr="1"')[1].split('class="acts"')[0]
    assert 'class="diffq"' in box and "the new sentence" in box and "the old sentence" in box
    # the quote comes out of the patch at the finding's own line, and says
    # nothing when it can't
    quote = render.patch_quote(p, "content/docs/iac/x.md", "L95")
    assert quote == {"quote_minus": ["the old sentence"], "quote_plus": ["the new sentence"]}
    assert render.patch_quote(p, "content/docs/iac/x.md", "L400") is None
    assert render.patch_quote(p, "content/docs/iac/x.md", None) is None
    assert render.patch_quote(p, "no/such/file.md", "L3") is None


def test_the_row_carries_the_reviewers_guide():
    q = _queue()
    p = row(q, 1)
    p["review"] = {**(p.get("review") or {}),
                   "brief_summary_bullets": ["`a.md`: the stacks link moves to `/docs/iac/concepts/stacks/`."],
                   "rubber_stamp": ["**Facts:** 12 claims checked, 7 verified clean."],
                   "brief_comment_id": 42, "author_comment_id": 41,
                   "evidence_url": "https://review-evidence.invalid/1/latest.html"}
    box = render.render_board(q).split('data-pr="1"')[1].split('class="acts"')[0]
    assert "<summary>reviewer&#x27;s guide</summary>" in box
    assert "What this PR changes" in box and "the stacks link moves" in box
    assert "Already checked, so you needn&#x27;t" in box and "12 claims checked" in box
    assert "#issuecomment-42" in box and "#issuecomment-41" in box
    assert 'href="https://review-evidence.invalid/1/latest.html"' in box
    # nothing from the guide, nothing rendered
    p["review"] = {"brief_summary_bullets": [], "rubber_stamp": [], "evidence_url": None}
    assert "reviewer&#x27;s guide</summary>" not in render.render_board(q).split('data-pr="1"')[1].split('class="acts"')[0]


def test_a_row_links_both_the_pr_and_its_diff():
    html = render.render_board(_queue())
    assert '<a class="pr" href="https://github.com/pulumi/docs/pull/1" title="Open pull request #1' in html
    assert '<a class="pr diff" href="https://github.com/pulumi/docs/pull/1/files"' in html
    assert "straight to the diff" in html
    # and into a real editor, for when a browser diff is not enough
    assert '<a class="pr diff" href="https://vscode.dev/github/pulumi/docs/pull/1"' in html
    assert render.vscode_url({"repo": "pulumi/docs"}, 9) == "https://vscode.dev/github/pulumi/docs/pull/9"


def test_a_row_links_the_preview_pages():
    q = _queue()
    p = row(q, 1)
    p["preview"] = {"status": "ready", "url": "http://preview.invalid",
                    "pages": [{"file": "content/docs/a.md", "url": "/docs/a/", "title": "Page A",
                               "preview_url": "http://preview.invalid/docs/a/"}]}
    box = render.render_board(q).split('data-pr="1"')[1].split('class="acts"')[0]
    assert "<summary>preview · 1 page</summary>" in box
    assert 'href="http://preview.invalid/docs/a/">Page A</a>' in box
    assert 'href="http://preview.invalid">the whole preview site' in box
    # nothing to link, nothing rendered
    p["preview"] = {"status": "none", "pages": []}
    assert "preview ·" not in render.render_board(q).split('data-pr="1"')[1].split('class="acts"')[0]


def test_the_reviews_own_stance_rides_on_the_finding():
    q = _queue()
    p = row(q, 1)
    p["judgments"] = []
    p["review"] = {**(p.get("review") or {}), "items": [
        {"id": "F1", "bucket": "reviewer-check", "file": "content/docs/iac/x.md", "anchor": "L95",
         "text": "| **F1** | [x](u) | **Spurious:** the sentence never claimed that. |"},
        {"id": "F2", "bucket": "reviewer-check", "file": "content/docs/iac/x.md", "anchor": "L95",
         "text": "| **F2** | [x](u) | Worth a look before you approve: the target moved. |"}]}
    html = render.render_board(q).split('data-pr="1"')[1].split('class="acts"')[0]
    assert "the review calls this spurious" in html and "the review says: worth a look" in html
    assert render.review_stance("nothing notable here") is None


def test_a_row_with_nothing_open_says_so():
    # A judge row whose review found nothing still needs a call. Saying
    # "not yet judged" over an empty list implies findings that don't exist.
    q = _queue()
    p = row(q, 1)
    p["judgments"] = []
    p["review"] = {**(p.get("review") or {}), "items": []}
    p["reasons"] = ["risk:typo", "review:absent"]
    p["labels"] = ["review:frontmatter-only"]
    html = render.render_board(q)
    box = html.split('data-pr="1"')[1].split('class="acts"')[0]
    assert "Nothing reviewed this diff" in box
    assert "This row still needs a call: No review has run on this PR at all" in box
    # and it says WHY nothing reviewed it, rather than leaving that a mystery
    assert "It was skipped because the diff only touches frontmatter" in box
    assert "not yet judged" not in box
    # a small diff is shown in place; a big one links out instead
    assert "the whole diff · 2 lines in 1 file" in box
    p["files"] = [{"path": f"content/docs/p{i}.md", "additions": 30, "deletions": 30,
                   "patch": "@@ -1,2 +1,2 @@\n-a\n+b"} for i in range(6)]
    box = render.render_board(q).split('data-pr="1"')[1].split('class="acts"')[0]
    assert "the whole diff" not in box and "Read the diff on GitHub" in box


def test_filter_chips_carry_their_counts():
    html = render.render_board(_queue())
    # an unlit chip has to say what it is keeping off the page
    assert '<button class="fchip" data-filter="view" data-value="blocked"' in html
    assert 'blocked <span class="fcount">' in html and 'stamp set <span class="fcount">' in html
    assert "row in this group. Lit: they are shown. Unlit: they are hidden." in html


def test_every_tooltip_explains_rather_than_echoes():
    """A title that repeats its own element's text teaches nothing. Every
    tooltip on the board has to say something the label doesn't."""
    import html as _html
    import re as _re
    q = _queue()
    row(q, 3)["recommended"] = "request-changes"
    from analyze import do_next
    q["do_next"] = do_next(q["prs"], q.get("clusters") or [], q.get("directional") or [])
    page = render.render_board(q)
    pairs = _re.findall(r'title="([^"]*)"[^>]*>([^<]*)<', page)
    assert len(pairs) > 20, "the board should be thoroughly tooltipped"
    for title, text in pairs:
        t, x = _html.unescape(title).strip(), _html.unescape(text).strip()
        assert t, f"empty tooltip on {x!r}"
        assert t != x, f"tooltip echoes its own text: {x!r}"
        assert len(t.split()) >= 5, f"tooltip too thin to help: {t!r} on {x!r}"
    # and a reason chip's tooltip describes its own value, not its family
    assert render.chip_title("review:absent").startswith("No review has run on this PR at all")
    assert "only because master was merged" in render.chip_title("review:base-merged")
    assert render.chip_title("review:stale") != render.chip_title("review:absent")


def test_the_board_carries_its_own_manual():
    html = render.render_board(_queue())
    assert '<details class="help"><summary>How to read this board</summary>' in html
    for heading in ("The four verdicts", "Do next", "Judgment badges", "Filters"):
        assert f"<h4>{heading}</h4>" in html
    assert "A worksheet, not a control panel" in html


def test_do_next_cards_press_the_rows_they_name():
    q = _queue()
    row(q, 3)["recommended"] = "request-changes"
    from analyze import do_next
    q["do_next"] = do_next(q["prs"], q.get("clusters") or [], q.get("directional") or [])
    html = render.render_board(q)
    # the card names its PRs, says what pressing it does, and carries the row
    # buttons it would press
    assert "#3 needs its author, not you." in html
    assert "Posts a changes-requested review on each" in html
    assert 'data-targets="{&quot;3&quot;: &quot;--request-changes 3&quot;}"' in html
    # and the script keeps a card and a contrary row decision from both being lit
    assert "function syncCards()" in html and "a chain: the rows it covers defer to it" in html
    # a card with no row button of its own (a consolidation) still marks the
    # rows it covers
    assert "function markClaimed(card, on)" in html and "covered by Do next" in html


def test_ownership_chips_read_as_words():
    tags = [_file("content/blog/p/index.md", ["tags: [kubernetes, aws]"], ["tags: [kubernetes]"])]
    q = run([stampable(9, labels=["review:no-blockers", "domain:blog"], files=tags)], cfg=cfg(me=["docs"]))
    html = render.render_board(q)
    # the code stays greppable in the title; the chip itself says why the row is here
    # the chip says why the row is here; the tooltip explains, never echoes
    assert '>no team approval needed</span>' in html
    assert 'title="The routing matrix asks for no team approval on a change like this, so nobody is waiting to review it and the row is yours to take. (gate:none)"' in html


def test_a_generated_row_offers_close_where_others_offer_send_back():
    q = run([stampable(8, labels=["review:trivial", "domain:docs"], author="pulumi-bot", author_type="User")])
    html = render.render_board(q)
    assert "send back to author" not in html
    assert 'data-cmd="--close 8" data-pr="8" data-kind="decision"' in html and "close it out" in html


def test_stamp_rows_start_selected_and_there_are_no_checkboxes():
    q = run([stampable(7)])
    html = render.render_board(q)
    assert 'class="btn p p-go sel" data-cmd="--stamp 7" data-pr="7" data-kind="decision" data-decision="0" title="Approve this PR' in html
    assert 'Squash-merges it." aria-pressed="true"' in html
    assert 'type="checkbox"' not in html
    # the other way to approve is a decision too, so picking it puts out the default
    assert 'data-cmd="--stamp 7:no-merge" data-pr="7" data-kind="decision"' in html and "approve, don&#x27;t merge" in html
    # One decision per row, side actions ride along: the script puts out the
    # other lit decision on the same PR, and only decisions count as made.
    jhtml = render.render_board(_queue())
    assert 'data-cmd="--request-changes 1" data-pr="1" data-kind="decision"' in jhtml
    # the screenshot button is detail-view only: on the board the row already
    # links every changed page on the preview
    assert 'data-cmd="--render 1"' not in jhtml
    assert 'data-cmd="--render 1"' in render.render_detail(_queue(), 1)
    assert 'data-cmd="--request-changes 1" data-pr="1" data-kind="decision"' in jhtml
    assert 'button.btn.sel[data-kind="decision"][data-pr="\' + pr + \'"]' in html  # one decision per row, via clearRow
    assert 'button.btn.sel[data-kind="decision"]\')) done++' in html
    assert 'id="cmd">$ /pr-review --act</div>' in html and 'id="copy"' in html
    assert "if (!c || seen[c]) return;" in html  # the composer dedupes fragments


def test_fixed_disposition_reads_as_already_done():
    q = _queue()
    row(q, 3)["judgments"].append({"finding_id": "F9", "file": "content/docs/iac/x.md", "line": 3,
                                  "decision": "Anchor right?", "disposition": "fixed", "deep_link": "https://x/y#z"})
    html = render.render_board(q)
    assert "already fixed</span>" in html and "recommend <b>fixed</b>" not in html
    # A badge says why the finding doesn't stop the merge, never what the
    # author answered, and the title says what approving does about it.
    assert "not a real issue</span>" in html
    assert "title=\"The review got this one wrong. Approving posts `/resolve &lt;id&gt; refuted`" in html
    assert "the author has not answered anything here" in html
    # and the row says what the reader actually clicks
    assert "Approving the row records these calls on the PR" in html and "Nothing here needs a click of its own." in html


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


def test_handed_off_rows_collapse_into_the_waiting_list():
    from test_analyze import _file  # noqa: PLC0415
    q = run([stampable(7), stampable(8, title="Chris has this one", requested_users=["cnunciato"],
                                     files=[_file("content/docs/b.md", ["x"])])])
    html = render.render_board(q)
    assert 'data-pr="8"' not in html  # no full row
    assert "Waiting on others" in html and "Chris has this one" in html and "@cnunciato" in html
    assert "<b>1</b><span>waiting on others</span>" in html
    full = render.render_board(q, include_handed_off=True)
    assert 'data-pr="8"' in full and "Waiting on others" not in full
    text = render.render_terminal(q)
    assert "waiting on others (1):" in text and "     8  " not in text.split("waiting on others")[0]
    assert "     8  " in render.render_terminal(q, include_handed_off=True)


def test_mostly_theirs_cluster_has_no_do_next_card():
    from test_analyze import _file  # noqa: PLC0415
    mine = stampable(1, title="Mine", files=[_file("content/docs/a.md", ["x"], ["o"], old_start=10)])
    theirs = stampable(2, title="Theirs", requested_users=["cnunciato"], files=[_file("content/docs/a.md", ["y"], ["o"], old_start=10)])
    q = run([mine, theirs])
    html = render.render_board(q)
    assert "1 of 2 PRs mine" in html and "+1 waiting on others" in html
    assert not any(d["cluster"] == "C1" for d in q["do_next"] if "cluster" in d)  # theirs: nothing to do next
    assert 'class="chip r-cluster theirs"' in html


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


def test_a_decision_is_one_selection_wherever_it_appears():
    # The same decision renders twice (compact row and expanded card), and a
    # chain's lead row button is the chain card pressed from the row, so both
    # halves have to light and unlight together.
    q = _queue()
    html = render.render_board(q)
    assert "function twins(b)" in html and "o.classList.toggle('sel', on)" in html
    assert "function leadCard(b)" in html and "c.dataset.lead === b.dataset.pr" in html


def test_the_panels_worth_reading_start_open_and_one_lever_moves_them_all():
    q = _queue()
    html = render.render_board(q)
    pr = {"number": 7, "preview": {"url": "https://p.example", "pages": [
        {"file": "content/docs/a.md", "url": "/docs/a/", "title": "A", "preview_url": "https://p.example/docs/a/"}]}}
    assert render.preview_links(pr).startswith('<details class="preview" open')
    assert '<details class="guide" open' in inspect.getsource(render.guide_block)
    # the manual and the folded reasons stay closed; nothing opens them for you
    assert '<details class="help">' in html
    assert 'id="foldall"' in html and "fold.textContent = open ? 'collapse all' : 'expand all';" in html
