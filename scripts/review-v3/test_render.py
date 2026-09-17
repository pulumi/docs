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
    # the chain card is `--chain C1`: one command with no row button, so it
    # claims both links rather than pressing anything
    assert 'data-cmd="--chain C1" data-pr="next1" data-claims="1,2" data-extra="--chain C1"' in html
    assert "Approves and squash-merges #1, then merges master into #2 so it can follow." in html


def test_board_rows_carry_verdict_chips_reasons_and_actions():
    html = render.render_board(_queue())
    # (#3 is blocked here, not route; it carries the route action all the same)
    assert 'data-verdict="judge"' in html and 'data-verdict="blocked"' in html
    assert 'class="chip r-cluster"' in html and 'class="chip r-mergeable"' in html
    assert 'data-cmd="--unblock 4"' in html and 'data-cmd="--route 3:@pulumi/docs-marketing-review"' in html
    assert 'class="btn p p-go" data-cmd="--stamp 1 --force"' in html  # judge rows keep approve-as-is, unselected, primary
    assert 'data-cmd="--request-changes 3"' in html and "send back to author" in html   # #3 has open findings to send
    assert '<div class="jbox">' in html and "Keep the widened claim?" in html and 'class="del">- old &lt;b&gt;' in html
    assert 'href="https://github.com/pulumi/docs/pull/3/files#diff-xR95"' in html
    assert "Blocked: mergeable:dirty" in html
    assert '<summary>why · ' in html and 'more reasons for this verdict' in html  # informational chips fold
    assert 'class="chip r-risk"' in html.split('<summary>why · ')[1]  # and risk is one of them


def test_route_chip_keeps_its_model_span_as_markup():
    # A route row proper: someone else's domain, and nothing blocking it. The
    # _queue() blog row carries open 🚨 findings, which make it blocked —
    # blocked outranks route — so this builds its own clean one.
    q = run([stampable(3, title="Blog copy edit", labels=["review:no-blockers", "domain:blog"],
                       files=[_file("content/blog/p/index.md", ["z"], ["p"])],
                       comments=[comment(CLEAN_BRIEF), comment(CLEAN_AUTHOR)])],
            cfg=cfg(me=["docs"]))
    assert row(q, 3)["verdict"] == "route", row(q, 3)["reasons"]
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
    assert "1 finding nobody has ruled on yet" in html and "runs the judge step" in html
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
    # the badge says where the finding stands, in the same slot a judged
    # finding's disposition uses, and the review's own words fold away
    assert "probably not real" in html and "worth a look" in html
    assert "the sentence never claimed that." in html and "the review&#x27;s full note" in html
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
    # a chip has to say what it would keep off the page, lit or not
    assert '<button class="fchip on" data-filter="view" data-value="blocked"' in html
    assert '<button class="fchip" data-filter="since" data-value="7d"' in html
    assert 'blocked <span class="fcount">' in html and 'stampable <span class="fcount">' in html
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
    # a code that carries extra segments still gets its own sentence: the
    # lookup keys off the state and puts the detail in the words
    for r in ("checks:red:sentinel", "checks:pending:build,test", "warnings:2:F6,F7",
              "cluster:C1:overlap:1/3", "owner:docs:docs-guild", "size:88>=40"):
        t = render.chip_title(r)
        assert t != r and len(t.split()) >= 5, f"bare chip: {r}"
        assert "see the reviewer&#x27;s guide" not in t and "see the reviewer's guide" not in t, f"fell through to the catch-all: {r}"
    assert "`sentinel`" in render.chip_title("checks:red:sentinel")


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
    assert 'data-cmd="--request-changes 3" data-pr="3" data-kind="decision"' in jhtml
    # the screenshot button is detail-view only: on the board the row already
    # links every changed page on the preview
    assert 'data-cmd="--render 1"' not in jhtml
    assert 'data-cmd="--render 1"' in render.render_detail(_queue(), 1)
    assert 'data-cmd="--request-changes 3" data-pr="3" data-kind="decision"' in jhtml
    assert 'button.btn.sel[data-kind="decision"][data-pr="\' + pr + \'"]' in html  # one decision per row, via clearRow
    assert "r.querySelector('button.btn.sel[data-kind=\"decision\"]') || r.querySelector('.claimnote')" in html
    assert 'id="cmd">$ /pr-review --act</div>' in html and 'id="copy"' in html
    assert "if (seen[k]) return; seen[k] = true;" in html  # the composer dedupes fragments


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


def test_a_row_carries_its_age_without_crowding_the_meta_line():
    from datetime import datetime, timezone  # noqa: PLC0415

    now = datetime(2026, 9, 17, tzinfo=timezone.utc)
    assert render.age_label({"created_at": "2026-09-17T06:00:00Z"}, now) == "today"
    assert render.age_label({"created_at": "2026-09-16T00:00:00Z"}, now) == "1d"
    assert render.age_label({"created_at": "2026-08-04T00:00:00Z"}, now) == "44d"
    assert render.age_label({"created_at": "2026-03-01T00:00:00Z"}, now) == "6mo"  # never longer than four chars
    assert render.age_label({"created_at": ""}, now) == "today"  # a missing date reads as new, never as ancient

    q = run([stampable(7), stampable(8, title="Been sitting a while", created_at="2026-01-05T00:00:00Z")])
    html = render.render_board(q)
    assert f'>{render.age_label(row(q, 7))}</span>' in html
    assert 'class="age old"' in html and 'class="age"' in html  # amber past 30 days, plain before it
    assert "Opened 2026-01-05" in html  # the exact date stays in the tooltip, not the line
    assert f"{'age':>5}" in render.render_terminal(q)


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
    assert 'id="foldall"' in html and "fold.textContent = open ? 'collapse every panel' : 'expand every panel';" in html
    # it lives in the filter bar, where it plainly governs the board, and it
    # moves the report's panels while leaving the manual's own state alone
    assert html.index('id="foldall"') > html.index('class="mock-bar"')
    assert "document.querySelectorAll('details:not(.help)').forEach(function(d){ d.open = open; });" in html
    # and every row carries the same lever for itself alone
    assert 'class="pr rowfold"' in html and "var row = b.closest('.mrow');" in html
    # and the board-wide lever relabels every row button it just moved
    assert "document.querySelectorAll('button.rowfold').forEach(function(b){ setRowFold(b, open); });" in html


def test_the_header_says_what_it_collected_and_where_your_lanes_came_from():
    q = _queue()
    q["config"] = {"owner": "me", "me": ["docs", "infra"], "source": "file"}
    head = render.header_line(q)
    assert "showing: rows in your lanes" in head and "your lanes: docs, infra" in head
    assert "pinned in ~/.pr-review.yml" in head
    # no config and no readable teams: say that, rather than listing every
    # lane as though the approver had chosen them
    q["config"] = {"owner": "me", "me": ["blog", "docs", "frontend"], "source": "defaults"}
    head = render.header_line(q)
    assert "your lanes: every lane (nothing pinned)" in head and "could not\nbe read" not in head
    assert "could not be read" in head.replace("&#x27;", "'")
    q["config"] = {"owner": "any", "me": [], "source": "file"}
    assert "showing: every open PR" in render.header_line(q)


def test_a_flex_summary_draws_its_own_chevron():
    # A `display:flex` summary loses the browser's disclosure marker, so the
    # collisions fold and the manual would look like plain headings.
    q = _queue()
    html = render.render_board(q)
    assert '.clusters summary::before,details.help>summary::before{content:"\\25B8"' in html
    assert ".clusters details[open]>summary::before,details.help[open]>summary::before{transform:rotate(90deg)}" in html


def test_a_workflow_authored_row_says_the_send_back_is_dead_not_the_fix():
    # Nobody will read a changes-requested review on a workflow's PR, but the
    # branch is still editable and closing is not the only move.
    assert "push to the branch yourself" in render.AUTHOR_HELP["generated"]
    assert "closes rather than going back" not in render.AUTHOR_HELP["generated"]
    assert render.DEFERRED_NO_AUTHOR[1] == "no author to ask"
    assert "Fix it yourself" in " ".join(render.DEFERRED_NO_AUTHOR[2].split())


def test_the_fold_lever_is_not_a_filter():
    # It wears the chip styling, so a filter loop that selects on `.fchip`
    # alone reads filters[undefined] and throws -- which silently disables
    # every filter on the page, leaving hidden verdicts visible and their
    # chips unlit.
    html = render.render_board(_queue())
    assert 'class="fchip lever" id="foldall"' in html
    assert html.count("document.querySelectorAll('.fchip[data-filter]')") == 2
    assert "document.querySelectorAll('.fchip')" not in html


def test_every_verdict_starts_visible_because_the_command_acts_on_it():
    html = render.render_board(_queue())
    for value in ("judge", "route", "stamp", "blocked"):
        assert f'<button class="fchip on" data-filter="view" data-value="{value}"' in html
    assert "stampable" in html


def test_a_card_adds_only_what_no_row_carries():
    # A Do-next card presses row buttons; the command is read off the rows.
    # What the card itself contributes is `data-extra`: a chain's unblock of
    # a follow-up that has no row button yet, or a consolidation's request,
    # which has no row equivalent at all. Every other card adds nothing, so
    # pressing it can never repeat its rows' fragments.
    html = render.render_board(_queue())
    assert 'data-extra="--chain C1"' in html            # the chain card has no row button: its command is the whole fragment
    assert render.card_extra({"cmd": "--stamp 1,2", "targets": {"1": "--stamp 1", "2": "--stamp 2"}}) == ""
    assert render.card_extra({"cmd": '--request-changes 9 --reason "x"', "claims": [9]}) == '--request-changes 9 --reason "x"'
    assert "function fragment(b){ return isCard(b) ? (b.dataset.extra || '') : b.dataset.cmd; }" in html
    assert "var sel = {}" not in html                    # no shadow list: the lit buttons are the state
    # every --stamp N[:mode][ --force] folds into one list, --force once
    assert "var STAMP = /^--stamp (\\d+(?::(?:no-)?merge)?)( --force)?$/;" in html
    assert "out += ' --stamp ' + stamps.join(',') + (force ? ' --force' : '');" in html
    # the cards settle before the command is drawn, on every click, and the
    # copy button re-reads before it copies
    assert "function settle(){ syncCards(); compose(); composeHand(); progress(); }" in html
    assert html.count("settle();") >= 4 and "compose();   // what goes to the clipboard" in html
    # progress counts a lit decision on any row and every row with one to make
    assert "return r.querySelector('button.btn[data-kind=\"decision\"]');" in html
    assert '.mrow[data-verdict="judge"], .mrow[data-verdict="route"]' not in html


def test_a_reason_names_the_pr_it_is_for():
    # act.py takes `--reason "N=text"`; a bare reason is a global flag, which
    # a batch can't carry. The rewrite happens here, so the script never sees
    # a bare one.
    assert render.scope_reasons('--request-changes 5 --reason "a, b (c)"') == '--request-changes 5 --reason "5=a, b (c)"'
    assert render.scope_reasons('--close 5 --superseded-by 6 --reason "x"') == '--close 5 --reason "5=x"'.replace("--reason", "--superseded-by 6 --reason")
    assert render.scope_reasons('--refresh 7 --reason "x" --rerun 8 --reason "y"') == '--refresh 7 --reason "7=x" --rerun 8 --reason "8=y"'
    assert render.scope_reasons('--reason "x"') == '--reason "x"'                       # nothing to scope it to
    assert render.scope_reasons('--refresh 9 --reason "9=x"') == '--refresh 9 --reason "9=x"'   # already scoped
    q = _queue()
    q["do_next"] = [{"kind": "consolidate", "say": "C1: 3 overlapping sweeps by workprentice.", "does": "Posts one review.",
                     "label": "send #2 back", "claims": [2],
                     "cmd": '--request-changes 2 --reason "These 3 PRs overlap (#1, #2, #3); please consolidate."'}]
    html = render.render_board(q)
    assert 'data-cmd="--request-changes 2 --reason &quot;2=These 3 PRs overlap (#1, #2, #3); please consolidate.&quot;"' in html
    assert 'data-extra="--request-changes 2 --reason &quot;2=These 3 PRs overlap' in html
    assert '--reason &quot;These' not in html


def test_the_payload_cannot_end_the_script_early():
    # Inside <script type="application/json">, `<!--<script>` in a title or
    # path flips the HTML parser into double-escaped script data and the JSON
    # block swallows the page's real <script> to end of file: every button on
    # the board goes dead. Escaping only `</` did not cover it.
    q = run([stampable(1, title="Add guest post <!--<script>", files=[_file("content/docs/a <!--<script>.md", ["x"], ["o"])])],
            cfg=cfg(me=["docs"]))
    for html in (render.render_board(q), render.render_board(q, artifact=True), render.render_detail(q, 1)):
        assert "<!--<script>" not in html
        assert html.count("<script") == 2                           # the JSON payload and the page script, nothing else
        payload = html.split('id="queue">')[1].split("</script>")[0]
        assert "<" not in payload and ">" not in payload and "&" not in payload
        assert json.loads(payload)["prs"][0]["title"] == "Add guest post <!--<script>"   # still the same JSON


def test_the_help_says_the_command_is_the_yes():
    # SKILL.md §5 and reading-the-board.md: invoking the command is the
    # go-ahead; act.py plans, previews and executes without asking again.
    html = render.render_board(_queue())
    assert "Invoking it <i>is</i> the yes" in html and "nothing asks you to confirm a second time" in html
    assert "waits for a yes" not in html
    # another lane's PR is a full row under its owner; only handed-off PRs sit at the foot
    assert "still takes a full row, grouped under that owner" in render.SHOWING_HELP["me"]
    assert "listed at the foot of the page instead" not in render.SHOWING_HELP["me"]


def test_the_detail_view_lists_cluster_membership():
    html = render.render_detail(_queue(), 1)
    assert "<h5>Cross-PR</h5>" in html
    cross = html.split("<h5>Cross-PR</h5>")[1].split("</ul>")[0]
    assert "cluster:C1:overlap:" in cross


def test_the_composer_reads_the_lit_buttons():
    """The board's script under jsdom: the click sequences an audit found
    broken -- a card doubling its rows' fragments, the bar a click behind the
    cards, several --stamp flags, refresh / re-run not counting. Runs when
    node and the repo's jsdom devDependency are present, else says so."""
    import shutil  # noqa: PLC0415
    import subprocess  # noqa: PLC0415
    import tempfile  # noqa: PLC0415
    repo = HERE.parent.parent
    node = shutil.which("node")
    if not node or not (repo / "node_modules" / "jsdom" / "package.json").is_file():
        print("  skip: test_the_composer_reads_the_lit_buttons (needs node and jsdom from `make ensure`)")
        return
    q = run([
        stampable(11, files=[_file("content/docs/a.md", ["x"], ["o"])]),                                        # stamp, bot
        stampable(12, files=[_file("content/docs/b.md", ["x"], ["o"])], author="sean1588", author_type="User"),  # stamp, human (not the approver)
        stampable(13, labels=["review:trivial", "domain:docs"], comments=[], files=[_file("content/docs/c.md", ["x"], ["o"])]),  # judge
        stampable(14, labels=["review:no-blockers", "domain:blog"], files=[_file("content/blog/p/index.md", ["z"], ["p"])]),    # route
        stampable(15, labels=["review:no-blockers", "domain:blog"], files=[_file("content/blog/q/index.md", ["z"], ["p"])]),    # route
        stampable(16, head_sha="f" * 40, files=[_file("content/docs/d.md", ["x"], ["o"])]),                      # blocked: refresh
        stampable(17, labels=["review:error", "domain:docs"], files=[_file("content/docs/e.md", ["x"], ["o"])]),  # blocked: rerun
        stampable(18, comments=[comment(CLEAN_BRIEF), comment(V3_AUTHOR)], author="pulumi-bot", author_type="User",
                  files=[_file("content/docs/f.md", ["x"], ["o"])]),                                             # blocked: close + a hand fix
    ], cfg=cfg(me=["docs"]))
    prs = {"stamp": [11, 12], "judge": 13, "route": [14, 15], "refresh": 16, "rerun": 17, "handfix": 18,
           "team": "@pulumi/docs-marketing-review"}
    with tempfile.TemporaryDirectory() as td:
        board = Path(td) / "board.html"
        board.write_text(render.render_board(q))
        res = subprocess.run([node, str(HERE / "test_render_composer.js"), str(board), json.dumps(prs)],
                             cwd=repo, capture_output=True, text=True, timeout=120)
    assert res.returncode == 0, res.stdout + res.stderr



def test_the_terminal_carries_everything_the_board_shows():
    # --terminal used to cut each row at 110 characters, print blockers
    # nowhere, print actions for judge rows only, hide open findings on an
    # unjudged row, and print an empty merge order for a cluster whose every
    # member is handed off. A terminal reader has to be able to compose the
    # same act command the board would, so all of it is here now.
    q = _queue()
    p = row(q, 1)
    p["judgments"] = []
    p["review"] = {**(p.get("review") or {}), "items": [
        {"id": "F1", "bucket": "reviewer-check", "file": "content/docs/iac/x.md", "anchor": "L95",
         "summary": "Does this sentence still say what the link says?"}]}
    p["reasons"] += [f"brief:stale-summary:token-{i}" for i in range(12)]
    text = render.render_terminal(q)
    assert "blocked: mergeable:dirty" in text                                     # why a row is blocked
    for cmd in ("--unblock 4", "--route 3:@pulumi/docs-marketing-review", "--request-changes 3",
                "--stamp 1 --force", "--stamp 1:no-merge --force", "--render 1"):
        assert f"]  {cmd}" in text, cmd                                             # every row's actions, blocked and route rows included
    assert "open: F1 Does this sentence still say what the link says? [nobody has ruled] @ content/docs/iac/x.md" in text
    assert " ".join(text.split()).count("@ content/docs/iac/x.md L95") == 1                  # wrapped, not cut
    assert "judged: F4 Keep the widened claim? → refuted https://github.com/pulumi/docs/pull/3/files#diff-xR95" in text
    assert "do next" in text and "$ /pr-review --act --unblock 4" in text          # the Do-next moves carry their commands
    assert "$ /pr-review --act --chain C1" in text                                 # the chain card too
    for r in p["reasons"]:
        if not r.startswith(render.HIDDEN_REASON_PREFIXES):
            assert r in text, r                                                    # nothing is truncated: it wraps
    assert "…" not in text.split("do next")[0].replace("… ", "")                   # no cut marker on any row line
    assert all(len(line) <= 110 or " " not in line.strip() for line in text.splitlines())
    # a cluster whose members are all handed off has no merge order to print;
    # the members are the news, and the line says why there is no order
    a = stampable(1, title="A", requested_users=["cnunciato"], files=[_file("content/docs/a.md", ["x"], ["o"], old_start=10)])
    b = stampable(2, title="B", requested_users=["cnunciato"], files=[_file("content/docs/a.md", ["y"], ["o"], old_start=10)])
    q2 = run([a, b])
    assert q2["clusters"][0]["merge_order"] == []
    t2 = render.render_terminal(q2)
    assert "C1 overlap: #1, #2 (all waiting on others)" in t2 and "merge \n" not in t2 and "merge →" not in t2


def test_rows_waiting_on_the_author_and_rows_with_no_unblock_are_never_silent():
    q = _queue()
    stuck = row(q, 4)                       # blocked on a conflict; pretend the unblock was refused
    stuck["actions"] = []
    stuck["reasons"].append("unblock:refused:dependabot-branch")
    back = row(q, 2)                        # already sent back by this approver, nothing pushed since
    back["waiting_on_author"] = True
    back["reasons"].append("sent-back:2026-09-10")
    own = row(q, 1)                         # the approver's own PR
    own["reasons"].append("author:self")
    html = render.render_board(q)
    # a blocked row with nothing to click says so, and the tally counts it
    assert "Blocked: mergeable:dirty" in html and ">no action available</span>" in html
    assert "<b>1</b><span>blocked, no action</span>" in html
    # the sent-back row leaves the groups for its own compact list, with the date
    assert 'data-pr="2"' not in html and "<h2>Waiting on the author</h2>" in html and "sent back 2026-09-10" in html
    assert "<b>1</b><span>waiting on the author</span>" in html
    full = render.render_board(q, include_handed_off=True)
    assert 'data-pr="2"' in full and "<h2>Waiting on the author</h2>" not in full
    back["verdict"], back["blockers"], back["actions"] = "blocked", ["outstanding:1"], []   # what analyze emits for one
    full = render.render_board(q, include_handed_off=True)
    assert ">waiting on the author</span>" in full and full.count(">no action available</span>") == 1   # #4 only
    assert "<b>1</b><span>blocked, no action</span>" in full
    assert "judged blocking finding" not in render.chip_title("outstanding:judged:F1,F2")
    assert "approving this row posts their /resolve lines" in render.chip_title("outstanding:judged:F1,F2")
    # the new chips read as words, stay out of the fold, and explain themselves
    row1 = html.split('data-pr="1"')[1].split('class="acts"')[0]
    assert ">your own PR<" in row1.split("<summary>why")[0]
    assert "cannot approve it or send it back to yourself" in render.chip_title("author:self")
    t = render.chip_title("sent-back:2026-09-10")
    assert "waiting on its author, not on you" in t and "2026-09-10" in t
    assert "could not offer one: dependabot branch" in render.chip_title("unblock:refused:dependabot-branch")
    # the re-run-checks action, on a row and as a Do-next batch card
    stuck["actions"] = [{"id": "rerun-checks", "label": "re-run the failed checks", "cmd": "--rerun-checks 4"}]
    q["do_next"] = [{"kind": "rerun-checks", "say": "#4 is red on a check that looks flaky.",
                     "does": "Re-runs the failed checks on each. Nothing merges.", "cmd": "--rerun-checks 4",
                     "label": "re-run the failed checks", "targets": {"4": "--rerun-checks 4"}}]
    html = render.render_board(q)
    assert 'class="btn p p-stop" data-cmd="--rerun-checks 4" data-pr="4" data-kind="decision"' in html
    assert "Re-run the failed jobs of the head commit" in html
    assert '<li class="next stop">' in html and 'data-targets="{&quot;4&quot;: &quot;--rerun-checks 4&quot;}"' in html
    assert ">no action available</span>" not in html and "blocked, no action" not in html
    text = render.render_terminal(q)
    assert "1 waiting on the author" in text and "waiting on the author (1):" in text and "sent back 2026-09-10" in text
    assert "[re-run the failed checks]  --rerun-checks 4" in text and "     2  " not in text.split("waiting on the author (1)")[0]
    stuck["actions"] = []
    assert "blocked: mergeable:dirty (no action available)" in render.render_terminal(q)


def test_a_fenced_block_in_a_finding_renders_as_pre():
    # A ```markdown block inside a finding note came out as ``<code>markdown:
    # the inline pass saw the fence as one code span and a half.
    out = render.md_inline("See:\n```markdown\n- [x](https://e.invalid) `y` <b>\n```\nthen `code` and **b**")
    assert "<pre>- [x](https://e.invalid) `y` &lt;b&gt;</pre>" in out
    assert "<code>code</code>" in out and "<b>b</b>" in out
    assert "``<code>" not in out and "<code>markdown" not in out and "<a href" not in out
    assert render.md_inline("```bash $ pulumi up ```") == "<pre>$ pulumi up </pre>"
    assert render.md_inline("no fence `here`") == "no fence <code>here</code>"
    q = _queue()
    p = row(q, 1)
    p["judgments"] = []
    p["review"] = {**(p.get("review") or {}), "items": [
        {"id": "F1", "bucket": "reviewer-check", "summary": "Use the shortcode",
         "text": "Use:\n```markdown\n{{< notes type=\"info\" >}}\n```\nhere, not `<div>`."}]}
    html = render.render_board(q)
    assert "<pre>{{&lt; notes type=&quot;info&quot; &gt;}}</pre>" in html
    assert "``<code>" not in html and "<code>markdown" not in html and "<code>&lt;div&gt;</code>" in html


def test_rows_are_in_pr_number_order_inside_their_group():
    """Verdict is already on the row, in the tally, on a filter chip and in
    the Do-next cards. Sorting the rows by it too meant finding #21598 on the
    page required knowing its verdict first; a number is the one thing about
    a row you always already have."""
    q = run([stampable(31, title="Page 31", files=[_file("content/docs/p31.md", ["x"])]),
             stampable(12, title="Conflicted", mergeable_state="dirty", files=[_file("content/docs/p12.md", ["x"])]),
             stampable(27, title="Page 27", files=[_file("content/docs/p27.md", ["x"])]),
             stampable(5, title="Errored", labels=["review:error", "domain:docs"], files=[_file("content/docs/p5.md", ["x"])])],
            cfg=cfg(me=["docs"]))
    html = render.render_board(q)
    assert re.findall(r'<div class="mrow [^"]*" data-pr="(\d+)"', html) == ["5", "12", "27", "31"]
    # mixed verdicts, so this is number order and not verdict order wearing a disguise
    assert {row(q, n)["verdict"] for n in (5, 12, 27, 31)} == {"blocked", "stamp"}
    assert re.findall(r"^\s+(\d+)\s+(?:stamp|judge|route|blocked)", render.render_terminal(q), re.M) == ["5", "12", "27", "31"]


def test_a_card_says_how_many_of_its_rows_still_carry_its_decision():
    """A card that goes out because one row was decided differently used to
    paint exactly like a card nobody had touched -- "the button does
    nothing". It carries a live tally and a partial state now."""
    q = run([stampable(n, title=f"Page {n}", files=[_file(f"content/docs/p{n}.md", ["x"])]) for n in (7, 8, 9)],
            cfg=cfg(me=["docs"]))
    html = render.render_board(q)
    assert '<span class="cnt" data-total="3">3/3</span>' in html
    assert "c.classList.toggle('part', part);" in html and ".btn.p.part{" in html
    # one row per target, and every target resolvable to a row button on the page
    targets = json.loads(re.search(r'data-targets="([^"]+)"', html).group(1).replace("&quot;", '"'))
    assert set(targets) == {"7", "8", "9"}
    for n, cmd in targets.items():
        assert f'data-cmd="{cmd}" data-pr="{n}"' in html, (n, cmd)
    # a single-row card has nothing to tally
    one = render.render_board(run([stampable(7, files=[_file("content/docs/p7.md", ["x"])])], cfg=cfg(me=["docs"])))
    assert 'class="cnt"' not in one


def test_a_stuck_workflow_row_offers_an_interactive_fix_off_the_act_command():
    """The row of a PR no author will ever answer carries "fix it yourself".
    It is a run, not a write, so it composes on its own line at the foot of
    the page and never reaches the --act command."""
    q = run([stampable(18, comments=[comment(CLEAN_BRIEF), comment(V3_AUTHOR)], author="pulumi-bot", author_type="User",
                       files=[_file("content/docs/f.md", ["x"], ["o"])])], cfg=cfg(me=["docs"]))
    html = render.render_board(q)
    assert '<button class="btn hand" data-run="/address-review 18" data-pr="18"' in html
    assert ">fix it yourself</button>" in html
    # no data-cmd on it: the composer reads --act fragments off data-cmd alone
    hand = html.split('class="btn hand"')[1].split("</button>")[0]
    assert "data-cmd" not in hand and "data-kind" not in hand
    assert 'id="handwrap" hidden' in html and 'id="handcmd"' in html
    assert "/address-review 18" in render.render_terminal(q)
    assert "(an interactive run, not part of --act)" in render.render_terminal(q)
