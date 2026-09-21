#!/usr/bin/env python3
"""Render queue.json as the /pr-review board, one PR's detail view, or a
terminal table — three views of the same rows.

    render.py --in .pr-review-queue.json --board .pr-review-board.html
    render.py --in .pr-review-queue.json --detail 21598 --out .pr-review-board.html
    render.py --in .pr-review-queue.json --terminal [--pr 21598]

The board groups rows owner → domain, pins collision clusters at the top,
carries filter chips (owner / domain / verdict / author / since), and its
action buttons are toggles that compose one `/pr-review --act …` command
at the bottom (a stamp row's "approve & merge" starts selected; no
fragment is ever repeated). The page never calls GitHub: everything it shows is inlined
from queue.json (a `<script type="application/json">` block, the
render-evidence-html.py pattern), and the only thing it produces is a
command for the person to run.

Every value that reaches the page goes through `esc()` exactly once,
server-side; the vanilla JS only toggles `hidden` and concatenates
`data-cmd` attributes it never parses. Theme-aware through CSS custom
properties under both `prefers-color-scheme` and `data-theme`, the token
set of the hand-built triage board this queue replaced.

Deterministic, no model calls.
"""

from __future__ import annotations

import argparse
import base64
import html
import json
import re
import sys
import textwrap
from datetime import datetime, timedelta, timezone
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_REPO_ROOT = _HERE.parent.parent
sys.path.insert(0, str(_HERE))
import sentinel  # noqa: E402

_compose = sentinel._compose
SHOTS_DIR = _REPO_ROOT / ".pr-review-shots"
VERDICT_ORDER = ("stamp", "judge", "route", "blocked")
VERDICT_CLASS = {"stamp": "go", "judge": "hold", "route": "route", "blocked": "stop"}
BUCKET_HELP = {
    "outstanding": "A blocking finding: the review thinks this has to be answered before the PR merges.",
    "author-answer": "The review asked the author a question and is waiting for the answer.",
    "reviewer-check": "Something for a human to weigh. It does not block the merge on its own.",
    "low": "A low-confidence finding from the older review format. Same weight as a reviewer check.",
    "style": "A wording suggestion. Never blocks anything.",
    "pre-existing": "Something already true on master, which this PR neither caused nor made worse.",
    "preexisting": "Something already true on master, which this PR neither caused nor made worse.",
}
BUCKET_LABEL = {
    "outstanding": "🚨 Outstanding", "author-answer": "❓ Author answer", "reviewer-check": "⚠️ Reviewer check",
    "low": "⚠️ Low-confidence", "style": "✏️ Style", "pre-existing": "💡 Pre-existing", "preexisting": "💡 Pre-existing",
}
HIDDEN_REASON_PREFIXES = ("owner:", "label:")  # rendered elsewhere on the row
# Chips that change what you'd click stay visible; the rest fold behind "why".
PRIMARY_CODES = ("warnings", "outstanding", "self-accepted", "cluster", "directional", "duplicate", "mergeable", "checks",
                 "review", "scrutiny", "blog", "handed-off", "draft", "route", "merging-over", "link-fixes", "gate",
                 "sent-back", "unblock")
# Whole codes (not families) that change what you'd click: `author:self`
# takes the stamp and the send-back off the row, where `author:internal` is
# background.
PRIMARY_VALUES = ("author:self",)
# A reason code is a vocabulary, not a sentence. These few decide whether a
# row is on your board at all, so they read as words; the code stays in the
# chip's title for anyone grepping the queue.
CHIP_LABEL = {
    "author:self": "your own PR",
    "gate:any-team": "any team can approve this",
    "link-fixes:mine": "link-only sweep: yours",
    "route:no-team": "team missing, routing to a person",
    "route:team-unverified": "team not verifiable from here",
}
ACTION_CLASS = {"stamp": "go", "stamp-merge": "go", "stamp-no-merge": "go", "request-changes": "hold", "route": "route", "unblock": "stop", "refresh": "stop", "rerun": "stop", "rerun-checks": "stop", "close": "stop",
                "chain": "go", "consolidate": "hold", "fix": "", "render": "", "deploy": ""}
INCLUDE_HANDED_OFF = False  # render.py --include-handed-off flips this
# A row takes one decision (what happens to the PR) and any number of side
# actions (things done on the way). The board's toggles enforce that: lighting
# a second decision on a row puts out the first.
SIDE_ACTIONS = {"fix", "render", "deploy"}


def action_kind(pr: dict, action: dict) -> str:
    """`rerun` is the unblock on an errored review (a decision) and an extra
    on a row where no review ran (a side action beside approve/route)."""
    if action["id"] == "rerun":
        blockers = pr.get("blockers") or []
        return "decision" if ("review:error" in blockers or "review:unreadable" in blockers) else "side"
    return "side" if action["id"] in SIDE_ACTIONS else "decision"


def unblock_actions(pr: dict) -> list[dict]:
    """The decisions a blocked row can actually take. A stamp is not one:
    act.py refuses `--stamp` on a blocked row whatever the flags, so a
    blocked row whose only buttons approve has nothing an approver can do
    from here, and the board has to say so rather than show buttons that
    the act layer will bounce."""
    return [a for a in pr.get("actions") or []
            if action_kind(pr, a) == "decision" and not a["id"].startswith("stamp")]


def no_action(pr: dict) -> bool:
    """A blocked row with no unblock: it should never happen (analyze gives
    every verdict an action), and when it does the row says so out loud. A
    row waiting on its author has had its buttons removed on purpose -- it
    is the author's turn -- so it is not one of these."""
    return pr.get("verdict") == "blocked" and not pr.get("waiting_on_author") and not unblock_actions(pr)


def parked(pr: dict) -> bool:
    """A row that leaves the groups for one of the compact lists at the foot
    of the page: waiting on another reviewer, or on its own author."""
    return bool(pr.get("handed_off") or pr.get("waiting_on_author"))


def esc(v) -> str:
    """html.escape every value that reaches the page, in exactly one place."""
    if v is None:
        return ""
    return html.escape(str(v), quote=True)


# ---- pieces --------------------------------------------------------------------


def vscode_url(queue: dict, n: int) -> str:
    """The PR in the VS Code web editor: a real editor over the branch, for
    when reading a diff in a browser tab is not enough."""
    return f"https://vscode.dev/github/{queue.get('repo') or 'pulumi/docs'}/pull/{n}"


def pr_url(queue: dict, n: int) -> str:
    return f"https://github.com/{queue.get('repo') or 'pulumi/docs'}/pull/{n}"


def files_url(queue: dict, n: int) -> str:
    return pr_url(queue, n) + "/files"


def _age_days(pr: dict, now: datetime | None = None) -> int:
    try:
        created = datetime.fromisoformat((pr.get("created_at") or "").replace("Z", "+00:00"))
    except ValueError:
        return 0
    return max((now or datetime.now(timezone.utc)) - created, timedelta()).days


def age_label(pr: dict, now: datetime | None = None) -> str:
    """How long the PR has been open, in at most four characters.

    Age is the one thing a row cannot derive from the diff: two identical
    stampable sweeps read the same until you notice one has been sitting for
    six weeks. It stays this short because it rides in the meta line beside
    six other facts -- days up to two months, then months, so an old PR never
    pushes the rest of the line around."""
    d = _age_days(pr, now)
    if d < 1:
        return "today"
    if d < 60:
        return f"{d}d"
    return f"{d // 30}mo"


def deep_link(queue: dict, pr: dict, item: dict) -> str | None:
    file = item.get("file")
    if not file:
        return None
    return files_url(queue, pr["number"]) + _compose.diff_anchor(file, item.get("anchor") or item.get("ref") or "")


# A tooltip explains THIS chip with THIS value, not the family it belongs to:
# "review:base-merged" has to say what a base merge did to the review, not
# that review codes exist. The raw code rides along in parentheses so the
# queue stays greppable.
RISK_HELP = {
    "typo": "A typo-sized change: a word or two.",
    "minor": "A small change, a few lines of prose.",
    "standard": "An ordinary content change.",
    "major": "A big diff, by line count or file count. Worth reading properly.",
    "infra": "Touches the build or deploy pipeline, so it needs staging evidence before it merges.",
}
REVIEW_HELP = {
    "stale": "The review on this PR describes an older commit. Its findings may already be fixed, or it may have missed what was pushed since: refresh it before trusting it.",
    "absent": "No review has run on this PR at all — no author card, no brief. Nothing has checked this diff.",
    "in-progress": "The review is running right now. Wait for it rather than acting on a half-written card.",
    "error": "The review job failed, so there are no findings. Re-running it is the only way to get a verdict.",
    "triage-prose": "Only the cheap triage prose check ran, not a full review. It catches wording, not correctness.",
    "base-merged": "The head commit moved, but only because master was merged into the branch. The diff the review read is unchanged, so the review still stands and this row is not stale.",
    "unreadable": "The review did not arrive whole. Either a page of a split review is missing, or the card's own tally declares more findings than its sections parsed into. A long review's 🚨 rows are the tail of the document, so what is missing is exactly where they live — the row is blocked rather than approvable, and a fresh review is the way out.",
    "parse-confidence": "The review's body parsed into no findings and nothing corroborates that: a v2 card with no tally table, or a v3 card missing its head sentinel or carrying a broken REVIEW_STATE. Not a blocker — nothing says there are findings — but not stampable either. Read the comment itself.",
}
MERGEABLE_HELP = {
    "dirty": "GitHub says this PR conflicts with its base branch. Merge master in and resolve it before anything else.",
    "behind": "The base branch moved on and this PR has not caught up.",
    "unknown": "GitHub has not finished working out whether this merges cleanly.",
}
CHECKS_HELP = {
    "red": "CI is failing on the head commit.",
    "pending": "CI is still running on the head commit.",
}
SHAPE_HELP = {
    "infra": "Touches layouts/, .github/ or the build, so it needs --include-infra before it can be stamped.",
    "link-only": "A fact about the diff, the same for everyone: every changed line is the same sentence with only a link rewritten, so nothing but link targets moved. On its own it changes nothing; it is what your link_fixes setting acts on.",
}
AUTHOR_HELP = {
    "internal": "Opened by a Pulumi org member.",
    "external": "Opened by someone outside the org, so it gets the external-contributor treatment.",
    "generated": ("Opened by a workflow run, not a person: a changes-requested review would sit unread, because nothing is "
                  "going to come back and revise it. The work itself is still fixable -- push to the branch yourself "
                  "(the edit link opens it in VS Code), apply the drafted fixes, or ask Claude on the PR -- it is only "
                  "the send-back that has no audience. Closing it out is the cheap option when the lane will regenerate "
                  "the page anyway."),
    "self": ("This is your own PR, so you cannot approve it or send it back to yourself. Route it to the lane's team for "
             "the approval, and answer its review findings with /address-review, the author's side of the pipeline."),
}
ROUTE_STATE_HELP = {
    "no-team": "GitHub has no team by the name the routing config gives this lane, so the review request goes to that role's SLA person instead.",
    "team-unverified": "This token cannot read the org's teams, so the team named in the routing config is used without checking it exists.",
}
SIMPLE_HELP = {
    "scrutiny:heightened": "The diff looks AI-written, so this row can never be a plain stamp however clean it looks.",
    "stances:present": "The review recorded editorial judgement calls it made. They only block with --strict-stances.",
    "gate:any-team": "Every changed line differs only in a link, and the routing config lets ANY review team approve one of those: checking a retargeted link needs a careful reader, not a particular lane's reader. So this row is yours to take, and the merge gate agrees.",
    "link-fixes:mine": "YOUR SETTING, not a fact about the PR: link_fixes: mine in ~/.pr-review.yml makes a link-only diff yours to approve whatever lane it belongs to, because a lane owner's review buys nothing on a link swap. Set link_fixes: route and this row would go to its lane owner instead.",
    "blog:new-post": "This PR adds a new blog post, which is never a stamp: somebody reads a new post before it ships.",
    "desc:empty": "The PR description is still the empty template.",
    "not-governed": "The Sentinel merge gate does not apply to this PR.",
    "draft": "A draft PR. It only appears because you asked for it by number.",
    "trust:membership-unreadable": "The token could not read org membership, so the author is treated as external and gets the stricter treatment.",
    "self-accepted": "A finding on this PR was marked answered by the PR's own author. Their call on their own work, so the queue does not count it as answered.",
}


def chip_title(r: str) -> str:  # noqa: C901 — one branch per code, flat on purpose
    """What this chip, with this value, means for this row."""
    code, _, detail = r.partition(":")
    first = detail.split(":")[0] if detail else ""
    text = SIMPLE_HELP.get(r)
    if text is None:
        if code == "risk":
            text = RISK_HELP.get(detail)
        elif code == "review":
            # `review:unreadable:pages:2,3` carries its detail past the key,
            # so the sentence takes the key and names the detail at the end.
            text = REVIEW_HELP.get(detail)
            if text is None and first in ("unreadable", "parse-confidence"):
                text = REVIEW_HELP[first]
                what = detail.partition(":")[2]
                if what:
                    text += f" ({what})"
        elif code == "mergeable":
            text = MERGEABLE_HELP.get(detail)
        elif code == "checks":
            # `checks:red:sentinel,build` names the failing checks, so match on
            # the state and put the names in the sentence rather than dropping
            # the whole tooltip for want of an exact key.
            failing = detail.partition(":")[2]
            named = ", ".join(f"`{f}`" for f in failing.split(",") if f)
            text = CHECKS_HELP.get(first)
            if text and named:
                text += (f" Failing: {named}." if first == "red" else f" Still running: {named}.")
        elif code == "shape":
            text = SHAPE_HELP.get(detail)
        elif code == "author":
            text = AUTHOR_HELP.get(detail)
        elif code == "label":
            text = f"GitHub carries the `{detail}` label on this PR."
        elif code == "ai-suspect":
            text = {"trailer": "A commit trailer or PR body names an AI tool as co-author.",
                    "prose": "The added prose matches the shape of AI-written text.",
                    "manual": "You marked this one AI-suspect by hand."}.get(detail, f"AI-suspect signal: {detail}.")
        elif code == "warnings":
            n = first or "Some"
            ids = detail.partition(":")[2]
            text = (f"{n} reviewer-check finding{'s' if n != '1' else ''} the review raised and nobody has answered"
                    + (f" ({ids})" if ids else "") + ". They do not block a merge, but they are unanswered.")
        elif code == "outstanding" and first == "judged":
            ids = detail.partition(":")[2]
            text = ("Blocking findings the judge step has answered"
                    + (f" ({ids})" if ids else "") + ": approving this row posts their /resolve lines before it merges, "
                    "so they no longer hold it. Change a call to deferred and the row goes back to blocked.")
        elif code == "outstanding":
            n = first or "Some"
            ids = detail.partition(":")[2]
            text = (f"{n} blocking finding{'s' if n != '1' else ''} still open on the author card"
                    + (f" ({ids})" if ids else "") + ". Answer or refute them before this merges.")
        elif code == "self-accepted":
            text = f"{detail} was marked answered by the PR's own author, so the queue does not count it as answered."
        elif code == "cluster":
            cid = first
            rest = detail.partition(":")[2]
            if rest.startswith("overlap"):
                pos = rest.partition(":")[2]
                text = (f"This PR and the rest of cluster {cid} change the same or adjacent lines, so they can only merge in "
                        f"order. It is number {pos} in that order.")
            elif rest == "same-file":
                text = f"Shares files with the rest of cluster {cid}, but no changed lines touch. Any merge order works."
            else:
                text = f"Cluster {cid} is mostly other people's PRs, so its ordering is not yours to drive."
        elif code == "directional":
            if detail.startswith("+"):
                text = f"There are {detail.lstrip('+').split('-')[0]} more conflicts of this kind on this PR."
            else:
                other, _, path = detail.partition(":")
                text = (f"This PR adds links to {path}, a URL that only exists as a Hugo alias, while {other} removes links "
                        "from it. Merge them in the wrong order and those links break.")
        elif code == "duplicate":
            text = f"{detail} looks like the same change as this PR."
        elif code == "blog" and first == "stale-date":
            text = (f"YOUR SETTING: the post is dated {detail.partition(':')[2]}, older than the stale_date_days window in "
                    "~/.pr-review.yml, so publishing it now would look stale.")
        elif code == "brief":
            text = (f"The review's summary says \"{detail.partition(':')[2]}\", which appears nowhere in the diff, so the "
                    "summary may describe an earlier push.")
        elif code == "desc" and first == "stale":
            text = f"The PR description names `{detail.split(':')[-1]}`, which this diff does not touch."
        elif code == "size":
            text = ("YOUR SETTING: the diff is "
                    f"{detail.replace('>=', ' lines against your stamp_max_lines cap of ')}, so it gets read rather than stamped.")
        elif code == "owner":
            dom, _, role = detail.partition(":")
            text = f"Files in this PR belong to the {dom} lane, which {role} owns."
        elif code == "route":
            text = ROUTE_STATE_HELP.get(detail) or f"This PR belongs to the {detail} lane, so that team gets asked for the review."
        elif code == "handed-off":
            text = f"{detail} is already the requested reviewer, so this row is waiting on them, not on you."
        elif code == "merging-over":
            kind, _, who = detail.partition(":")
            text = (f"{who} has already requested changes on this PR; that has to be settled before it merges."
                    if kind == "changes-requested" else
                    f"{who} has already approved this PR, so your approval is not the first.")
        elif code == "sent-back":
            text = (f"You already sent this PR back on {detail or 'an earlier run'} and nothing has been pushed since, so it "
                    "is waiting on its author, not on you. It returns to the board when a new commit lands.")
        elif code == "unblock":
            why = detail.partition(":")[2].replace("-", " ") if first == "refused" else detail.replace("-", " ")
            text = (f"The queue looked for a mechanical unblock on this row and could not offer one: {why or 'no unblock applies'}. "
                    "Whatever moves this PR has to happen on GitHub or on the branch by hand.")
        if text is None and first:
            # A known code carrying an unexpected value: say what is known
            # rather than rendering a bare chip with nothing behind it. The
            # test below fails on this path, so it is a safety net, not a
            # licence to skip writing the real sentence.
            base = SIMPLE_HELP.get(f"{code}:{first}") or globals().get(f"{code.upper().replace('-', '_')}_HELP", {}).get(first)
            text = base or f"The queue flagged this row with `{code}` = `{detail}`; see the reviewer's guide for what that means."
    return f"{text} ({r})" if text else r


# Codes whose presence depends on YOUR ~/.pr-review.yml rather than on the
# PR. They get a marker, because "everyone sees this" and "you see this
# because of a setting you chose" are different claims and the board should
# not blur them.
CONFIG_CODES = ("link-fixes", "size", "blog:stale-date")


def is_config_chip(r: str) -> bool:
    return r.startswith(CONFIG_CODES)


def _chip(r: str) -> str:
    code = r.split(":", 1)[0]
    cls = f"chip r-{esc(code)}" + (" theirs" if r.endswith(":theirs") else "") + (" cfg" if is_config_chip(r) else "")
    text = CHIP_LABEL.get(r) or (r if len(r) <= 48 else r[:45] + "…")
    marker = '<span class="cfgdot" aria-hidden="true">·cfg</span>' if is_config_chip(r) else ""
    return f'<span class="{cls}" title="{esc(chip_title(r))}">{esc(text)}{marker}</span>'


def chips(reasons: list[str]) -> str:
    """Two tiers: actionable chips inline, informational ones behind a
    "why" fold so a row reads as a decision, not a wall of tags."""
    primary, info = [], []
    for r in reasons:
        if r.startswith(HIDDEN_REASON_PREFIXES):
            continue
        code = r.split(":", 1)[0]
        is_primary = (code in PRIMARY_CODES and not (code == "merging-over" and ":approved-by:" in r)) or r in PRIMARY_VALUES
        (primary if is_primary else info).append(r)
    out = "".join(_chip(r) for r in primary)
    if info:
        out += (f'<details class="why" title="{len(info)} more reasons for this verdict that would not change what you click. '
                'Open it to see them.">'
                f'<summary>why · {len(info)}</summary>') + "".join(_chip(r) for r in info) + "</details>"
    return out


def owner_label(pr: dict) -> str:
    if pr.get("is_mine", True):
        return "mine"
    for d in pr.get("domains") or []:
        o = (pr.get("owners") or {}).get(d) or {}
        if o.get("role"):
            return o["role"]
    return "unowned"


VERDICT_HELP = {
    "stamp": "Passed every gate: a current review with nothing open, green CI, no collision, your lane, under your size cap. Approving is the whole job.",
    "judge": "One thing on this PR needs a person. The box below says what it is.",
    "route": "Not your lane per the routing matrix, so the owning team is the one to ask. You can still approve it yourself.",
    "blocked": "Nothing you can do here until something else moves. The box below names the blocker.",
}
ACTION_HELP = {
    "stamp": "Approve this PR, recording a /resolve comment for each judged finding first.",
    "stamp-merge": "Approve and squash-merge, even though the author is a person and would normally merge their own PR.",
    "stamp-no-merge": "Approve without merging, leaving the merge to someone else.",
    "request-changes": "Post a changes-requested review built from this row's findings and label it needs-author-response. Nothing merges; the author's turn.",
    "close": ("Close this PR with a comment carrying the row's findings. A workflow opened it, so nobody is waiting on an "
              "answer and the lane re-queues the page on its next run. Not the only option: you can fix the branch "
              "yourself or ask Claude on the PR instead."),
    "route": "Request a review from the lane's owner and post what the queue flagged as a comment. Nothing merges, and the row moves to 'waiting on others'.",
    "unblock": "Merge master into this branch as a merge commit and push, so it stops conflicting. A conflicted merge is aborted and reported, never resolved blind.",
    "refresh": "Ask the existing review to update itself against the current head (@claude #update-review).",
    "rerun": "Throw the current review away and run a fresh one from scratch (@claude #new-review).",
    "rerun-checks": "Re-run the failed jobs of the head commit's workflow runs (the newest failed run per workflow), without a push, for a CI failure that looks flaky. A red commit status has no run to re-run, and the step says so. Nothing merges, and the review is not touched.",
    "fix": "Apply the drafted description correction and any one-click suggestions, then commit and push.",
    "render": "Every PR gets its own deployed copy of the site. This opens each page this PR changes on that preview and saves a full-page screenshot to .pr-review-shots/, for when you want to see the rendered page rather than the diff. It writes nothing to GitHub.",
    "deploy": "Dispatch the testing deploy workflow for this branch, to pulumi-test.io.",
    "chain": "Approve and merge the first PR of this collision cluster, then merge master into the next so it can follow.",
    "consolidate": "Ask the bot for one consolidated PR instead of this pile of overlapping sweeps. Nothing merges.",
}


def action_help(pr: dict, action: dict) -> str:
    """What this button does to this PR, in a sentence. A stamp says whether
    it merges, because that is the part a label can only hint at."""
    base = action.get("help") or ACTION_HELP.get(action.get("id"), "")
    if action.get("id", "").startswith("stamp") and action["id"] != "stamp-no-merge":
        merges = ":merge" in action.get("cmd", "") or (action["id"] == "stamp" and merges_on_stamp_row(pr))
        base += " Squash-merges it." if merges else " Does not merge it: that is the author's to do."
    if "--force" in action.get("cmd", ""):
        base += " The row is not a clean stamp, so this approves it as it stands."
    return base


def merges_on_stamp_row(pr: dict) -> bool:
    """Mirrors analyze.merges_on_stamp over a rendered row."""
    return (pr.get("author") or {}).get("type") == "bot"


def verdict_chip(pr: dict) -> str:
    v = pr.get("verdict") or "judge"
    extra = ""
    if v == "route":
        act = next((a for a in pr.get("actions") or [] if a["id"] == "route"), None)
        if act:
            # One route action may carry several fragments (a PR in two lanes
            # neither of which is yours), so read every target off it.
            targets = re.findall(r"--route \d+:(\S+)", act["cmd"]) or [act["cmd"].split(":", 1)[1]]
            extra = esc(" → " + " + ".join(targets))
    if pr.get("recommended") and pr["recommended"] != v:
        rec = pr["recommended"]
        extra += (f' <span class="v v-dim" title="{esc(f"The judge pass recommends {rec} for this row. The computed verdict stays {v}: a recommendation never lowers a gate.")}">'
                  f'model: {esc(rec)}</span>')
    return f'<span class="v v-{esc(v)}" title="{esc(VERDICT_HELP.get(v, ""))}">{esc(v)}{extra}</span>'


def meta_line(pr: dict) -> str:
    checks = (pr.get("checks") or {}).get("state") or "?"
    ci = {"green": "CI ✓", "red": "CI ✗", "pending": "CI …"}.get(checks, f"CI {checks}")
    review = pr.get("review") or {}
    reviewed = (review.get("reviewed_sha") or "")[:7]
    head = (pr.get("head") or {}).get("sha", "")[:7]
    fresh = f"reviewed@{reviewed} = head" if reviewed and head.startswith(reviewed[: len(head)]) or (reviewed and reviewed.startswith(head)) else (f"reviewed@{reviewed} ≠ head {head}" if reviewed else f"head {head}")
    parts = [
        ", ".join(pr.get("domains") or []) or "?",
        f"+{pr.get('additions', 0)} −{pr.get('deletions', 0)} · {len(pr.get('files') or [])} file{'s' if len(pr.get('files') or []) != 1 else ''}",
        ci, f"mergeable: {esc(pr.get('mergeable_state'))}", fresh,
        f"risk:{pr.get('risk_tier')}",
        f"@{(pr.get('author') or {}).get('login', '')}",
    ]
    days = _age_days(pr)
    age = (f'<span class="age{" old" if days >= 30 else ""}" title="Opened {esc((pr.get("created_at") or "?")[:10])}'
           f' -- {days} day{"s" if days != 1 else ""} ago. Amber past 30 days.">{esc(age_label(pr))}</span>')
    return "".join(f"<span>{esc(p)}</span>" for p in parts) + age


def diffq(j: dict, *, open_: bool = True) -> str:
    """Quotes start expanded: the lines are the evidence you judge on, so
    reading a row should never cost a click. The summary still folds them."""
    minus = j.get("quote_minus") or []
    plus = j.get("quote_plus") or []
    if isinstance(minus, str):
        minus = [minus]
    if isinstance(plus, str):
        plus = [plus]
    if not minus and not plus:
        return ""
    lines = [f'<span class="del">- {esc(l)}</span>' for l in minus] + [f'<span class="add">+ {esc(l)}</span>' for l in plus]
    return (f'<details class="quote"{" open" if open_ else ""} title="The exact lines this finding is about, straight from '
            'the diff. Click to fold them away."><summary>the lines</summary><div class="diffq">'
            + "\n".join(lines) + "</div></details>")


# The badge answers "why doesn't this finding stop the merge?", in the
# reader's terms, and the title says what approving the row does about it.
# Nothing here is the author speaking: the PR's author has not answered.
DISPOSITION_BADGE = {
    "fixed": ("go", "already fixed", "The diff already addresses this finding. Approving records it as fixed."),
    "refuted": ("go", "not a real issue", "The review got this one wrong. Approving posts `/resolve <id> refuted` with the reason below, and the finding closes."),
    "accepted": ("go", "fair, not blocking", "The finding stands but is not worth holding the PR for. Approving posts `/resolve <id> accepted` with the reason below."),
    "not-applicable": ("go", "doesn't apply", "The finding does not apply to this PR. Approving posts `/resolve <id> not-applicable` with the reason below."),
    "deferred": ("hold", "needs the author", "Not yours to fix. Use the row's send-back button and this becomes the author's to answer."),
}
DEFERRED_NO_AUTHOR = ("hold", "no author to ask",
                      "This one wants a change, and a workflow opened the PR, so a send-back would go unread. Fix it "
                      "yourself on the branch (the edit link opens it in VS Code), ask Claude on the PR, or use the "
                      "row's close button and let the lane re-queue the page.")


def disposition_badge(d: str | None) -> tuple[str, str, str]:
    return DISPOSITION_BADGE.get(d or "", ("dim", d or "?", "Disposition recorded by the judge pass."))


def judgment_footer(pr: dict) -> str:
    """One line under the findings saying what the reader does about them:
    the row's buttons, and nothing per finding. Without it the badges read
    like a form someone still has to fill in."""
    js = pr.get("judgments") or []
    if not js:
        return ""
    held = [j for j in js if j.get("disposition") == "deferred"]
    resolved = [j for j in js if j.get("disposition") in ("fixed", "refuted", "accepted", "not-applicable")]
    sends_back = any(a.get("id") == "request-changes" for a in pr.get("actions") or [])
    bits = []
    if resolved:
        bits.append(f"Approving the row records {'these calls' if len(resolved) != 1 else 'this call'} on the PR, one `/resolve` comment each, then merges if the button says merge.")
    if held:
        bits.append(("Sending it back" if sends_back else "Closing it out")
                    + f" hands {'the ones' if len(held) != 1 else 'the one'} marked "
                    + ("&ldquo;needs the author&rdquo;" if sends_back else "&ldquo;no author to ask&rdquo;")
                    + (" to the author." if sends_back else " to the lane's next run."))
    bits.append("Nothing here needs a click of its own.")
    return '<p class="jfoot">' + " ".join(bits) + "</p>"


def judgment_boxes(queue: dict, pr: dict) -> str:
    js = pr.get("judgments") or []
    if not js:
        return pending_judgment(queue, pr)
    out = []
    # A row with no author to answer a review says "close it out" on its
    # button; the badge has to agree with the button.
    sends_back = any(a.get("id") == "request-changes" for a in pr.get("actions") or [])
    for j in js:
        link = j.get("deep_link")
        where = f'<a href="{esc(link)}">{esc(j.get("file") or "")} L{esc(j.get("line") or "?")} ↗</a>' if link else '<a href="' + esc(pr_url(queue, pr["number"])) + '">open the PR ↗</a>'
        cls, label, why = disposition_badge(j.get("disposition"))
        if j.get("disposition") == "deferred" and not sends_back:
            cls, label, why = DEFERRED_NO_AUTHOR
        out.append(
            '<div class="jbox">'
            f'<div class="qrow"><div class="q">{esc(j.get("finding_id") or "")} {esc(j.get("decision") or j.get("question") or "")}</div>'
            f'<span class="v v-{cls}" title="{esc(why)}">{esc(label)}</span></div>'
            + (f'<div class="jnote">{esc(j["note"])}</div>' if j.get("note") else "")
            + diffq(j)
            + f'<div class="jmeta">{where}</div></div>'
        )
    return "".join(out) + judgment_footer(pr)


HUNK_RE = re.compile(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@")


def patch_quote(pr: dict, path: str | None, anchor: str | None) -> dict | None:
    """The diff lines a finding sits on, read out of `files[].patch`.

    An un-judged finding is a claim about a line of the diff, so the box that
    shows it should show that line — the same evidence a judged one carries,
    minus the reasoning nobody has written yet."""
    if not path or not anchor:
        return None
    m = re.search(r"(\d+)", anchor)
    if not m:
        return None
    target = int(m.group(1))
    patch = next((f.get("patch") for f in pr.get("files") or [] if f.get("path") == path), None)
    if not patch:
        return None
    new_no, minus, plus = 0, [], []
    for line in patch.splitlines():
        h = HUNK_RE.match(line)
        if h:
            if plus or minus:
                break                      # the hunk holding the target has ended
            new_no = int(h.group(3)) - 1
            continue
        in_range = abs(new_no + 1 - target) <= 1
        if line.startswith("+"):
            new_no += 1
            if abs(new_no - target) <= 1:
                plus.append(line[1:])
        elif line.startswith("-"):
            if in_range:
                minus.append(line[1:])
        elif line.startswith(" "):
            new_no += 1
    if not (minus or plus):
        return None
    return {"quote_minus": minus[:3], "quote_plus": plus[:3]}


MD_LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")
# A fenced block: the opening fence with an optional info string, then
# everything up to the closing fence. The info string is dropped; the body
# is rendered verbatim, escaped, in a <pre>. Without this the inline pass
# saw the three backticks as one inline code span and a half, and a
# ```markdown block came out as ``<code>markdown</code>.
FENCE_RE = re.compile(r"```[A-Za-z0-9_+.-]*[ \t]*\n?(.*?)```", re.S)


def _md_span(text: str) -> str:
    out = esc(text)
    out = MD_LINK_RE.sub(r'<a href="\2">\1</a>', out)
    out = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", out)
    out = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", out)
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", out)


def md_inline(text: str) -> str:
    """The review writes findings in markdown. Escape first, then put back
    the four inline forms it actually uses, so a finding reads as written.
    A fenced code block becomes a <pre>, escaped and untouched by the
    inline pass, so the backticks inside it are never mistaken for spans."""
    text = text or ""
    out, pos = [], 0
    for m in FENCE_RE.finditer(text):
        out.append(_md_span(text[pos:m.start()]))
        out.append(f"<pre>{esc(m.group(1).strip(chr(10)))}</pre>")
        pos = m.end()
    out.append(_md_span(text[pos:]))
    return "".join(out)


FINDING_CLAIM = re.compile(r'^\s*\*"(.+?)"\*', re.S)
FINDING_VERDICT = re.compile(r"verdict:\s*([a-z-]+)", re.I)


def one_sentence(text: str, limit: int = 240) -> str:
    """The first sentence, or a clean cut. A finding's reasoning runs to a
    paragraph; the row needs the top of it and a fold for the rest."""
    t = " ".join((text or "").split())
    if len(t) <= limit:
        return t
    cut = t.rfind(". ", 0, limit)
    return (t[:cut + 1] if cut > 60 else t[:limit].rsplit(" ", 1)[0] + "…")


def split_finding(body: str) -> dict:
    """The parts of a composer-written finding: the claim it quotes, the
    verdict word, and the review's own take where it took one. Anything it
    cannot find comes back empty, and the caller falls back to the whole
    body."""
    out = {"claim": "", "verdict": "", "take": "", "stance": None}
    m = FINDING_CLAIM.search(body or "")
    if m:
        out["claim"] = " ".join(m.group(1).split())
    m = FINDING_VERDICT.search(body or "")
    if m:
        out["verdict"] = m.group(1).replace("-", " ")
    for marker, cls, label, why in REVIEW_STANCE:
        plain = marker.strip("*").rstrip(":")
        idx = (body or "").lower().find(plain.lower())
        if idx >= 0:
            out["stance"] = (cls, label, why)
            out["take"] = " ".join(body[idx + len(plain):].lstrip(" :*").split())
            break
    return out


def finding_body(item: dict) -> str:
    """The whole finding, not the card's one-line excerpt. The review stores
    each one as a markdown table row — id, location, body — so the body is
    everything after the first two cells; `summary` is the fallback."""
    text = (item.get("text") or "").strip()
    if text.startswith("|"):
        cells = [c.strip() for c in text.strip().strip("|").split("|")]
        body = " ".join(c for c in cells[2:] if c) if len(cells) > 2 else ""
        if body:
            return body
    return text or item.get("summary") or ""


# The review states its own position on a finding before anyone judges it:
# the composer tells the model to lead a body with `**Spurious:**` when the
# finding does not hold, and "Worth a look before you approve" when it does.
# Surfacing that is the difference between "nobody decided this" and "the
# review already said what it thinks".
REVIEW_STANCE = (
    ("**Spurious:**", "go", "probably not real",
     "A checker flagged this, and the review looked at it and thinks it does not hold. Nobody has ruled on it yet, "
     "so it is your call -- but it is not asking you for a fix."),
    ("Worth a look before you approve", "hold", "worth a look",
     "A checker flagged this and the review kept it deliberately: it wants a person to look before the PR merges."),
)
NO_STANCE = ("dim", "nobody has ruled", "A checker raised this and the review did not take a position on it. "
                                        "Nothing has decided it either way, so it is yours to weigh.")


def review_stance(body: str) -> tuple[str, str, str] | None:
    for marker, cls, label, why in REVIEW_STANCE:
        if marker.lower() in body.lower():
            return cls, label, why
    return None


# Why the review pipeline skipped a PR, keyed by the label it acts on. The
# ladder is claude-code-review.yml's: draft, trivial, frontmatter-only,
# oversized, bot author, already reviewed.
SKIP_REASON = {
    "review:trivial": "triage classified the diff as trivial, so the review pipeline short-circuited",
    "review:frontmatter-only": "the diff only touches frontmatter, so the review pipeline short-circuited",
    "review:oversized": "the diff is too big to review inside the pipeline's budget",
    "review:prose-flagged": "only triage's cheap prose check ran, not a full review",
}
SMALL_DIFF_LINES = 40
SMALL_DIFF_FILES = 4


def why_no_review(pr: dict) -> str:
    for label in pr.get("labels") or []:
        if label in SKIP_REASON:
            return SKIP_REASON[label]
    if pr.get("draft"):
        return "the PR is a draft, and drafts are not reviewed"
    if (pr.get("author") or {}).get("type") == "bot":
        return "a bot opened it and the pipeline skips most bot PRs"
    return ""


def small_diff_html(queue: dict, pr: dict) -> str:
    """A diff small enough to read in place, rendered in place. When a row
    has no findings to show, the diff IS the thing to look at, and making
    someone open GitHub for ten lines is the wrong trade."""
    files = pr.get("files") or []
    changed = sum((f.get("additions") or 0) + (f.get("deletions") or 0) for f in files)
    if not files or changed > SMALL_DIFF_LINES or len(files) > SMALL_DIFF_FILES:
        return ""
    if any(f.get("patch") is None for f in files):
        return ""
    out = []
    for f in files:
        lines = []
        for line in (f.get("patch") or "").splitlines():
            if line.startswith("+"):
                lines.append(f'<span class="add">{esc(line)}</span>')
            elif line.startswith("-"):
                lines.append(f'<span class="del">{esc(line)}</span>')
            elif line.startswith("@@"):
                lines.append(f'<span class="hunk">{esc(line)}</span>')
            else:
                lines.append(esc(line))
        out.append(f'<div class="dfile"><a href="{esc(files_url(queue, pr["number"]))}">{esc(f["path"])}</a>'
                   f'<div class="diffq">' + "\n".join(lines) + "</div></div>")
    return ('<details class="quote" open title="The whole diff, because it is small enough to read here. '
            'Click to fold it away."><summary>the whole diff · '
            f'{changed} line{"s" if changed != 1 else ""} in {len(files)} file{"s" if len(files) != 1 else ""}</summary>'
            + "".join(out) + "</details>")


def guide_block(queue: dict, pr: dict) -> str:
    """What the reviewer's guide says beyond its findings: what the PR
    changes, what the review already checked so you needn't, and the links
    to the guide itself and its evidence page. The guide is written for an
    approver, so the board should not make you go and find it."""
    r = pr.get("review") or {}
    bullets = r.get("brief_summary_bullets") or []
    checked = r.get("rubber_stamp") or []
    links = []
    if r.get("brief_comment_id"):
        links.append(f'<a href="{esc(pr_url(queue, pr["number"]))}#issuecomment-{esc(r["brief_comment_id"])}">'
                     "the reviewer&#x27;s guide ↗</a>")
    if r.get("author_comment_id"):
        links.append(f'<a href="{esc(pr_url(queue, pr["number"]))}#issuecomment-{esc(r["author_comment_id"])}">'
                     "the author card ↗</a>")
    if r.get("evidence_url"):
        links.append(f'<a href="{esc(r["evidence_url"])}">the evidence page ↗</a>')
    if not (bullets or checked or links):
        return ""
    parts = []
    if bullets:
        parts.append("<h5>What this PR changes</h5><ul>"
                     + "".join(f"<li>{md_inline(b)}</li>" for b in bullets[:12]) + "</ul>")
    if checked:
        parts.append("<h5>Already checked, so you needn&#x27;t</h5><ul>"
                     + "".join(f"<li>{md_inline(c)}</li>" for c in checked[:6]) + "</ul>")
    if links:
        parts.append('<p class="jmeta">' + " · ".join(links) + "</p>")
    return ('<details class="guide" open title="The reviewer\'s guide in short: what the PR changes, what the review '
            'already verified, and links to the guide, the author card and the evidence page.">'
            f'<summary>reviewer&#x27;s guide</summary>{"".join(parts)}</details>')


def preview_links(pr: dict) -> str:
    """The pages this PR changes, on its own deployed preview, as links.

    pulumi-bot posts the same list in a pinned comment; repeating it on the
    row means looking at a rendered page costs one click instead of a trip
    to GitHub and back."""
    prev = pr.get("preview") or {}
    pages = [p for p in prev.get("pages") or [] if p.get("preview_url")]
    if not pages:
        return ""
    rows = "".join(
        f'<li><a href="{esc(p["preview_url"])}">{esc(p.get("title") or p.get("url") or p["file"])}</a>'
        f' <span class="jmeta">{esc(p.get("url") or "")}</span></li>' for p in pages[:20])
    more = f"<li>… {len(pages) - 20} more on the PR</li>" if len(pages) > 20 else ""
    site = (f'<p class="jmeta"><a href="{esc(prev["url"])}">the whole preview site ↗</a></p>'
            if prev.get("url") else "")
    return ('<details class="preview" open title="Each page this PR changes, on the deployed preview of the site. '
            'The same list pulumi-bot pins on the PR, so you can look at a rendered page without leaving this board.">'
            f'<summary>preview · {len(pages)} page{"s" if len(pages) != 1 else ""}</summary>'
            f"<ul>{rows}{more}</ul>{site}</details>")


def pending_judgment(queue: dict, pr: dict) -> str:
    """Before the judge step runs: the open findings, each with the diff
    lines it is about, and what the row asks."""
    review = pr.get("review") or {}
    items = [i for i in review.get("items") or [] if not i.get("disposition") and i.get("bucket") not in ("style", "pre-existing", "preexisting")]
    if pr.get("triage_prose"):
        bullets = [l.strip("- ").strip() for l in pr["triage_prose"].splitlines() if l.startswith("- [")]
        items += [{"id": f"triage:{i + 1}", "summary": b, "bucket": "reviewer-check"} for i, b in enumerate(bullets)]
    if not items and pr.get("verdict") != "judge":
        return ""
    # Same shape as a judged finding: the claim on top, a badge for where it
    # stands, one sentence of why, the lines, and the rest folded. A wall of
    # the review's prose is what this box used to be, and it buried the one
    # thing the approver has to do.
    rows = []
    for i in items[:8]:
        link = deep_link(queue, pr, i)
        loc = (f'<a href="{esc(link)}">{esc(i.get("file") or "")} {esc(i.get("anchor") or "")} ↗</a>' if link
               else f'<a href="{esc(pr_url(queue, pr["number"]))}">open the PR ↗</a>')
        quote = patch_quote(pr, i.get("file"), i.get("anchor"))
        body = finding_body(i)
        parts = split_finding(body)
        cls, label, why = parts["stance"] or NO_STANCE
        head = parts["claim"] or one_sentence(body, 140)
        note = parts["take"] or parts["verdict"] and f"The checker called this {parts['verdict']}." or ""
        rows.append(
            '<div class="jbox pending">'
            f'<div class="qrow"><div class="q">{esc(i.get("id") or "")} {esc(one_sentence(head, 150))}</div>'
            f'<span class="v v-{cls}" title="{esc(why)}">{esc(label)}</span></div>'
            + (f'<div class="jnote">{md_inline(one_sentence(note))}</div>' if note else "")
            + (diffq(quote) if quote else "")
            + ('<details class="why" title="Everything the review wrote about this finding, including the checker\'s '
               'own wording and the verdict it assigned."><summary>the review&#x27;s full note</summary>'
               f'<div class="jnote">{md_inline(body)}</div></details>' if body else "")
            + f'<div class="jmeta">{loc}</div></div>')
    if len(items) > 8:
        rows.append(f'<div class="jnote">… {len(items) - 8} more on the PR</div>')
    # No reason codes here: the chips above the summary already carry them,
    # and repeating them makes the box look like a second, disagreeing list.
    if not items:
        # Nothing open on the review, but the row still needs a call. Say what
        # is asking for one instead of implying findings nobody can see.
        why = next((r for r in pr.get("reasons") or []
                    if r.split(":")[0] in ("review", "scrutiny", "blog", "size", "shape", "self-accepted",
                                           "directional", "duplicate", "desc", "brief", "merging-over")), None)
        because = chip_title(why).rsplit(" (", 1)[0] if why else "The queue could not clear every stamp gate on this row."
        skipped = why_no_review(pr) if (why or "").startswith("review:absent") else ""
        diff = small_diff_html(queue, pr)
        return ('<div class="jbox pending"><div class="q">'
                + ("Nothing reviewed this diff" if skipped else "No open findings on the review") + "</div>"
                + f'<p class="jfoot">This row still needs a call: {esc(because)}'
                + (f" It was skipped because {esc(skipped)}." if skipped else "")
                + (" The diff is small enough to read here, so it is below."
                   if diff else f' <a href="{esc(files_url(queue, pr["number"]))}">Read the diff on GitHub ↗</a>')
                + "</p>" + diff + "</div>")
    return ("".join(rows)
            + f'<p class="jfoot">{len(items)} finding{"s" if len(items) != 1 else ""} nobody has ruled on yet. '
              "A full <code>/pr-review</code> runs the judge step, which turns each badge into a recommended call "
              "with its reasoning and picks this row&#x27;s button; until then they are yours to weigh.</p>")


_REASON_RE = re.compile(r'--reason "((?:[^"\\]|\\.)*)"')
_REASON_STEP_RE = re.compile(r"--(?:request-changes|close|refresh|rerun) (\d+)\b")


def scope_reasons(cmd: str) -> str:
    """A `--reason "text"` that follows a `--request-changes N` / `--close N`
    / `--refresh N` / `--rerun N` in the same fragment becomes act.py's
    per-PR form, `--reason "N=text"`. The composer only ever concatenates
    fragments, so a reason has to name its PR before it leaves the page: a
    bare one is a global flag, and act.py refuses that once a second step
    could consume it. An already-scoped reason is left alone."""
    def sub(m: re.Match) -> str:
        text = m.group(1)
        steps = _REASON_STEP_RE.findall(cmd[:m.start()])
        if not steps or re.match(r"^\d+=", text):
            return m.group(0)
        return f'--reason "{steps[-1]}={text}"'
    return _REASON_RE.sub(sub, cmd)


def action_bar(pr: dict, queue: dict, *, expanded: bool = False) -> str:
    actions = list(pr.get("actions") or [])
    # The row already links every changed page on the deployed preview, so a
    # screenshot button there is a second, slower way to see the same thing.
    # It earns its place only where the shots get embedded: the detail view.
    if not expanded:
        actions = [a for a in actions if a["id"] != "render"]
    # The primary is what the judge recommended when it recommended an
    # action, else the row's first action. It renders last, right-aligned,
    # colored by what it does; everything else stays grey on the left.
    rec = pr.get("recommended")
    primary = next((a for a in actions if a["id"] == rec), None) or (actions[0] if actions else None)
    # The chain is an approval too -- the same one, through the same gates,
    # plus the unblock of the next link -- so on a chain lead it outranks a
    # bare "approve" recommendation for the coloured slot.
    chain = next((a for a in actions if a["id"] == "chain"), None)
    if chain and (primary is None or primary["id"].startswith("stamp")):
        primary = chain
    btns = [f'<a class="btn" href="{esc(pr_url(queue, pr["number"]))}" title="Open this pull request on GitHub, in a new tab.">open PR</a>']
    # A handoff is not an `act.py` fragment and never joins the --act
    # command: it is a separate, interactive run, composed on its own line
    # at the foot of the page. It is a toggle like everything else here, so
    # the page stays a worksheet.
    for h in pr.get("handoffs") or []:
        btns.append(f'<button class="btn hand" data-run="{esc(h["run"])}" data-pr="{pr["number"]}" '
                    f'title="{esc(h.get("why") or "")}" aria-pressed="false">{esc(h["label"])}</button>')
    for a in actions:
        if a is primary:
            continue
        btns.append(f'<button class="btn" data-cmd="{esc(scope_reasons(a["cmd"]))}" data-pr="{pr["number"]}" data-kind="{action_kind(pr, a)}"{covers_attr(a)} '
                    f'title="{esc(action_help(pr, a))}" aria-pressed="false">{esc(a["label"])}</button>')
    if primary:
        # A stamp row starts with its stamp selected: the composed command
        # merges every stampable row unless the approver deselects one.
        selected = " sel" if (primary["id"] == "stamp" and pr.get("verdict") == "stamp") else ""
        btns.append(f'<button class="btn p p-{esc(ACTION_CLASS.get(primary["id"], ""))}{selected}" data-cmd="{esc(scope_reasons(primary["cmd"]))}" data-pr="{pr["number"]}" '
                    f'data-kind="{action_kind(pr, primary)}" data-decision="{"1" if pr.get("verdict") in ("judge", "route") else "0"}"{covers_attr(primary)} '
                    f'title="{esc(action_help(pr, primary))}" aria-pressed="{"true" if selected else "false"}">{esc(primary["label"])}</button>')
    return '<div class="acts">' + "".join(btns) + "</div>"


def covers_attr(action: dict) -> str:
    """A chain button acts on a second row (the next link gets master
    merged in), so it says which: the script marks that row as covered
    while the button is lit, and puts the button out if a decision is
    picked there instead."""
    covers = action.get("covers") or []
    return f' data-covers="{esc(",".join(str(n) for n in covers))}"' if covers else ""


def row_html(queue: dict, pr: dict, *, expanded: bool = False) -> str:
    n = pr["number"]
    v = pr.get("verdict") or "judge"
    author = (pr.get("author") or {}).get("norm") or ""
    created = (pr.get("created_at") or "")[:10]
    body = [
        f'<div class="mrow {VERDICT_CLASS.get(v, "hold")}" data-pr="{n}" data-verdict="{esc(v)}" data-owner="{esc(owner_label(pr))}" '
        f'data-domains="{esc(" ".join(pr.get("domains") or []))}" data-author="{esc(author)}" data-created="{esc(created)}" '
        f'data-mine="{"1" if pr.get("is_mine", True) else "0"}">',
        # The number goes to the PR; the diff is one more click from there,
        # and the diff is what an approver actually wants to look at.
        (f'<div class="prcell"><a class="pr" href="{esc(pr_url(queue, n))}" title="Open pull request #{n} on GitHub.">#{n}</a>'
         f'<a class="pr diff" href="{esc(files_url(queue, n))}" title="Open this PR\'s Files changed tab, straight to the diff.">diff ↗</a>'
         f'<a class="pr diff" href="{esc(vscode_url(queue, n))}" title="Open this PR in the VS Code web editor, where you can read it with a real editor and edit the branch in place.">edit ↗</a>'
         # One row's worth of the board-wide lever: fold this row down to its
         # headline when you have finished with it, without touching the rest.
         f'<button class="pr rowfold" type="button" aria-pressed="true" title="Fold this row\'s panels -- its guide, preview links and diff quotes -- down to the headline, or open them all back up. Only this row.">fold ▴</button></div>'),
        "<div>",
        f'<h4>{esc(pr.get("title"))} {verdict_chip(pr)}</h4>',
        f'<div class="meta">{meta_line(pr)}</div>',
        f'<div class="chips">{chips(pr.get("reasons") or [])}</div>',
        f'<p class="sum">{esc(pr.get("summary") or "")}</p>' if pr.get("summary") else "",
        guide_block(queue, pr),
        preview_links(pr),
    ]
    if v in ("judge",) or pr.get("judgments") or expanded:
        body.append(judgment_boxes(queue, pr))
    if v == "blocked":
        # A blocked row names its blocker; one with no unblock says that too,
        # so a row can never sit silent with nothing to click and no word why.
        tail = (' <span class="v v-dim" title="Every action the queue knows for this blocker is refused or absent on this row, so '
                'nothing here changes it. Whatever moves it happens on GitHub or on the branch by hand.">no action available</span>'
                if no_action(pr) else "")
        if pr.get("waiting_on_author"):
            when = sent_back_on(pr)
            tail = (f' <span class="v v-dim" title="You sent this PR back{" on " + esc(when) if when else ""} and nothing has been '
                    'pushed since, so its buttons are off: it is the author\'s turn, not yours.">waiting on the author</span>')
        body.append(f'<div class="jbox stop"><div class="q">Blocked: {esc(", ".join(pr.get("blockers") or []) or "no blocker named")}{tail}</div></div>')
    body.append(action_bar(pr, queue, expanded=expanded))
    if expanded:
        body.append(detail_sections(queue, pr))
    body.append("</div></div>")
    return "".join(body)


def detail_sections(queue: dict, pr: dict) -> str:
    n = pr["number"]
    review = pr.get("review") or {}
    parts = ['<div class="detail">']
    # findings
    items = review.get("items") or []
    if items:
        rows = []
        for i in items:
            link = deep_link(queue, pr, i)
            where = f'<a href="{esc(link)}">{esc(i.get("file") or "")} {esc(i.get("anchor") or "")}</a>' if link else esc(i.get("anchor") or "")
            disp = i.get("disposition") or ("open" if i.get("blocking") or i.get("bucket") in ("low", "reviewer-check") else "advisory")
            rows.append(f"<tr><td>{esc(i.get('id'))}</td><td>{esc(BUCKET_LABEL.get(i.get('bucket'), i.get('bucket')))}</td>"
                        f"<td>{where}</td><td>{esc(i.get('summary') or '')}</td><td>{esc(disp)}</td></tr>")
        parts.append(f'<h5>Findings ({len(items)}) · review {esc(review.get("status"))} · {esc(review.get("surface"))}</h5>'
                     "<table><tr><th>id</th><th>bucket</th><th>where</th><th>finding</th><th>state</th></tr>" + "".join(rows) + "</table>")
    elif pr.get("triage_prose"):
        parts.append("<h5>Triage prose check (no full review ran)</h5><pre>" + esc(pr["triage_prose"]) + "</pre>")
    else:
        parts.append(f'<h5>No review findings · review {esc(review.get("status"))}</h5>')
    if review.get("stances"):
        parts.append('<p class="note">The brief lists editorial stances (advisory unless --strict-stances).</p>')
    # cross-PR
    cross = [r for r in pr.get("reasons") or [] if r.split(":")[0] in ("cluster", "directional", "duplicate")]
    if cross:
        parts.append("<h5>Cross-PR</h5><ul>" + "".join(f"<li>{esc(c)}</li>" for c in cross) + "</ul>")
    # preview
    prev = pr.get("preview") or {}
    if prev.get("pages"):
        li = []
        for pg in prev["pages"]:
            href = pg.get("preview_url") or pg.get("url")
            li.append(f'<li><a href="{esc(href)}">{esc(pg.get("title"))}</a> <code>{esc(pg.get("url"))}</code>' + shot_img(n, pg) + "</li>")
        parts.append(f'<h5>Preview · {esc(prev.get("status"))}</h5><ul class="pages">' + "".join(li) + "</ul>")
    # files
    parts.append("<h5>Files</h5><ul class=\"files\">" + "".join(
        f'<li><a href="{esc(files_url(queue, n) + _compose.diff_anchor(f["path"], ""))}"><code>{esc(f["path"])}</code></a> '
        f'<span class="v v-dim">{esc(f.get("status"))}</span> +{f.get("additions", 0)} −{f.get("deletions", 0)}</li>'
        for f in pr.get("files") or []) + "</ul>")
    # fix draft / description
    if pr.get("fix_draft"):
        fd = pr["fix_draft"]
        parts.append(f'<h5>Drafted fix ({esc(fd.get("kind"))})</h5><pre>{esc(fd.get("body") or fd.get("patch") or "")}</pre>')
    if pr.get("body"):
        parts.append("<details><summary>PR description</summary><pre>" + esc(pr["body"]) + "</pre></details>")
    parts.append("</div>")
    return "".join(parts)


def shot_img(n: int, page: dict, max_bytes: int = 1_500_000) -> str:
    slug = (page.get("url") or "").strip("/").replace("/", "_") or "index"
    f = SHOTS_DIR / str(n) / f"{slug}.png"
    if not f.is_file():
        return ""
    data = f.read_bytes()
    if len(data) > max_bytes:
        return f' <span class="v v-dim">screenshot at {esc(f)}</span>'
    return f'<br><img class="shot" alt="preview of {esc(page.get("url"))}" src="data:image/png;base64,{base64.b64encode(data).decode()}">'


def clusters_html(queue: dict) -> str:
    cl = queue.get("clusters") or []
    dr = queue.get("directional") or []
    du = queue.get("duplicates") or []
    if not (cl or dr or du):
        return ""
    cards = []
    demoted = []
    for c in cl:
        theirs = set(c.get("handed_off") or [])
        mine = [n for n in c["prs"] if n not in theirs]
        by_path: dict[str, set] = {}
        for p in c["pairs"]:
            for path in p["paths"]:
                by_path.setdefault(path, set()).update((p["a"], p["b"]))
        top = sorted(by_path.items(), key=lambda kv: -len(kv[1]))[:6]
        paths = "".join(f'<li><code>{esc(path)}</code> — {" ".join(f"#{x}" for x in sorted(prs))}</li>' for path, prs in top)
        more = f"<li>… {len(by_path) - 6} more paths</li>" if len(by_path) > 6 else ""
        order = " → ".join(f'<a href="{esc(pr_url(queue, x))}">#{x}</a>' for x in c["merge_order"])
        kind_cls = "no" if c["kind"] == "overlap" else "mid"
        theirs_note = f' <span class="v v-dim">+{len(theirs)} waiting on others</span>' if theirs else ""
        card = (
            f'<div class="card {kind_cls}"><h4>{esc(c["id"])} · {len(mine)} of {len(c["prs"])} PRs mine · {esc(c["kind"])}{theirs_note}</h4>'
            + (f"<p>Merge order: {order}</p>" if len(c["merge_order"]) > 1 else "")
            + f"<ul>{paths}{more}</ul></div>"
        )
        # A cluster with at most one of my PRs in it is somebody else's merge
        # problem; it stays available but doesn't take a pinned slot.
        (cards if len(mine) > 1 else demoted).append(card)
    by_path: dict[str, tuple[set, set]] = {}
    for d in dr:
        adds, rems = by_path.setdefault(d["path"], (set(), set()))
        adds.add(d["adds_links_pr"])
        rems.add(d["removes_links_pr"])
    handed = {p["number"] for p in queue.get("prs") or [] if p.get("handed_off")}
    for path, (adds, rems) in sorted(by_path.items(), key=lambda kv: -len(kv[1][0]) - len(kv[1][1])):
        link = lambda x: f'<a href="{esc(pr_url(queue, x))}">#{x}</a>'  # noqa: E731
        target = cards if (adds | rems) - handed and len((adds | rems) - handed) > 1 or (adds - handed and rems - handed) else demoted
        target.append(f'<div class="card no"><h4>Directional · <code>{esc(path)}</code></h4>'
                     f'<p>Alias-only URL. Adding links: {", ".join(link(x) for x in sorted(adds))}. Removing links: {", ".join(link(x) for x in sorted(rems))}. '
                     "Merge the removers first, then repoint the adders.</p></div>")
    for d in du:
        cards.append(f'<div class="card mid"><h4>Duplicate? #{d["newer"]} vs #{d["older"]}</h4>'
                     f'<p>Titles {int(d["title_ratio"] * 100)}% alike, opened {esc(d["minutes_apart"])} min apart, sharing {esc(", ".join(d["shared_files"][:3]))}.</p></div>')
    all_cards = cards + demoted
    return (f'<section class="clusters"><details open><summary><h2>Collisions · {len(cl)} cluster{"s" if len(cl) != 1 else ""}'
            f'{" · " + str(len(by_path)) + " directional" if by_path else ""}</h2><span class="note">the files, the pairs, the merge orders</span></summary>'
            '<div class="two">' + "".join(all_cards) + "</div></details></section>")


HELP_SECTIONS = [
    ("What this page is", [
        "A worksheet, not a control panel. Nothing here talks to GitHub.",
        "Every button is a toggle that adds a fragment to the command at the bottom. Click freely and change your mind; nothing happens until you run that command.",
    ]),
    ("The four verdicts", [
        "One per PR. It says what kind of move the row needs, not how good the PR is — and it is not the row order: rows sit in PR number order inside their group.",
        "<b>stamp</b> — passed every gate: current review, no open findings, green CI, no collisions, your lane, small enough.",
        "<b>judge</b> — one thing needs a person: an open finding, a new blog post, a diff over your size cap, a collision with another PR.",
        "<b>route</b> — not your lane per the routing matrix. Ask the owning team, or approve anyway.",
        "<b>blocked</b> — nothing to do until something else moves: an open 🚨 finding, a conflict, red CI, a stale or running review, someone else's changes requested. A row with no unblock says <i>no action available</i>.",
    ]),
    ("A row", [
        "Chips are the reasons for the verdict; the ones that change what you'd click stay out, the rest fold behind <b>why</b>. Hover any chip for a sentence explaining it.",
        "One decision per row (approve, send back, close it out, route, unblock, refresh, re-run the review, re-run the failed checks). Side actions like <i>apply fixes</i> ride along with it, and only decisions count toward the progress line.",
        "Every decision is on its row, next to the evidence for it. There is no batch strip: the stampable rows arrive already selected, and everything else is one button on the row it concerns.",
        "A collision cluster's move sits on the row it belongs to. <b>approve &amp; merge, then unblock #N</b> is on the chain's lead, and only where the collision is the one thing holding it back: it merges the lead through the stamp gates, then merges master into #N so it can follow, so it marks #N <i>covered</i> while it is lit. <b>ask … for one consolidated PR</b> is on the newest of a bot's overlapping sweeps.",
        "<b>your own PR</b> has no approve or send-back button: route it, and answer its findings with <code>/address-review</code>. A PR you already sent back waits under <i>Waiting on the author</i> until a commit lands.",
        "<b>fix it yourself</b> (amber, dashed) is on a PR a workflow opened that still has open findings: nobody will ever answer its review, so this is the way out that isn't closing it. It composes <code>/address-review N</code> on its own line above the command — an interactive run, never part of the batch.",
        "The button says whether approving merges: a bot row leads with <i>approve &amp; merge</i>, a person's row with <i>approve, no merge</i>, because merging their PR is their call.",
    ]),
    ("Judgment badges", [
        "A badge says why a finding does not stop the merge. It is never the author's answer: nobody has answered anything here.",
        "<b>not a real issue</b>, <b>fair, not blocking</b> and <b>doesn't apply</b> are recorded on the PR as <code>/resolve</code> comments when you approve the row, before it merges.",
        "<b>needs the author</b> goes back with the send-back button; <b>no author to ask</b> means a workflow opened the PR, so a send-back would go unread — fix the branch yourself, ask Claude on the PR, or close it out and let the lane re-queue the page.",
    ]),
    ("Where a row came from", [
        "A chip with a dotted border and a <b>·cfg</b> mark is there because of <i>your</i> ~/.pr-review.yml, not because of the PR. Everything else is the same for every approver.",
        "<b>shape:link-only</b> is a fact: every changed line differs only in a link. <b>link-only sweep: yours</b> is your <code>link_fixes: mine</code> setting acting on that fact, which is what pulls the row into your lane; <code>link_fixes: route</code> would send it to the lane owner.",
        "Your size cap (<code>stamp_max_lines</code>) and your stale-date window (<code>stale_date_days</code>) are the other two settings that put chips on a row.",
    ]),
    ("Filters", [
        "Chips are literal: a row shows only while its value is lit in every group, so turning a whole group off empties the board and says so.",
        "<i>since</i> is the one threshold rather than a set of values. <i>Reset chips</i> restores the defaults.",
    ]),
    ("The command at the bottom", [
        "Copy it and run it, or hand it to Claude. Invoking it <i>is</i> the yes: act.py plans it, prints a preview of every write with its exact body, and executes, so nothing asks you to confirm a second time. <code>--dry-run</code> runs the preflights and lists every write without sending one.",
        "Every approve button folds into one <code>--stamp</code> list (<code>--force</code> said once); a reason is scoped to its PR as <code>--reason \"N=…\"</code>; no fragment repeats.",
        "Every write re-reads the PR first (open, head unchanged); an approval also checks mergeable, CI green, and no changes-requested review from anyone but you. A PR that fails is skipped and the batch continues.",
    ]),
]


SHOWING_HELP = {
    "me": ("Which rows this run collected: the ones whose owning lane is yours, plus anything the routing matrix "
           "leaves ungated. A PR owned by another lane still takes a full row, grouped under that owner, with a route action; "
           "only PRs already waiting on another reviewer drop to the foot of the page. "
           "`--owner any` collects every open PR."),
    "any": "Which rows this run collected: every open PR, whoever owns it (`--owner any`).",
}

LANES_HELP = {
    "file": "The lanes you pinned in ~/.pr-review.yml. A row is yours when the routing matrix puts its change in one of them.",
    "github-teams": ("You have no ~/.pr-review.yml, so these are the lanes of the GitHub teams you are actually on. "
                     "Pin them in ~/.pr-review.yml if that is not the split you want."),
    "defaults": ("Nothing narrowed the board: you have no ~/.pr-review.yml and your GitHub team memberships could not "
                 "be read, so every lane counts as yours and nothing is filtered out by ownership. Create "
                 "~/.pr-review.yml with `me: [docs, infra]` to see only your own."),
}


def header_line(queue: dict) -> str:
    """The eyebrow, in words rather than in flag names. Two of its facts --
    what got collected and which lanes count as yours -- decide what the
    whole board shows, so each one says where it came from."""
    cfg = queue.get("config") or {}
    owner = cfg.get("owner", "me")
    when = queue.get("analyzed_at") or queue.get("generated_at") or ""
    lanes = cfg.get("me") or []
    source = cfg.get("source") or "defaults"
    shown = "every open PR" if owner == "any" else ("rows in your lanes" if owner == "me" else f"rows owned by {owner}")
    lane_text = "every lane (nothing pinned)" if source == "defaults" else ", ".join(lanes)
    return (f'{esc(queue.get("repo") or "")} · queue · {esc(when)} · '
            f'<span title="{esc(SHOWING_HELP.get(owner, SHOWING_HELP["me"]))}">showing: {esc(shown)}</span> · '
            f'<span title="{esc(LANES_HELP.get(source, LANES_HELP["defaults"]))}">your lanes: {esc(lane_text)}</span>')


def help_html() -> str:
    """The manual, folded, on the page it describes. Same content as
    `pr-review:references:reading-the-board`, kept short enough to read
    standing up."""
    out = []
    for heading, points in HELP_SECTIONS:
        out.append(f"<div><h4>{esc(heading)}</h4><ul>" + "".join(f"<li>{p}</li>" for p in points) + "</ul></div>")
    return ('<details class="help"><summary>How to read this board</summary>'
            '<div class="helpgrid">' + "".join(out) + "</div></details>")


def filter_bar(queue: dict) -> str:
    prs = queue.get("prs") or []
    owners = sorted({owner_label(p) for p in prs})
    domains = sorted({d for p in prs for d in p.get("domains") or []})
    authors = sorted({(p.get("author") or {}).get("norm") or "" for p in prs})
    counts = queue.get("counts") or {}

    GROUP_HELP = {"view": "verdict", "owner": "owner", "domain": "domain", "author": "author"}

    def rows_matching(kind, val):
        if kind == "view":
            return sum(1 for p in prs if p.get("verdict") == val)
        if kind == "owner":
            return sum(1 for p in prs if owner_label(p) == val)
        if kind == "domain":
            return sum(1 for p in prs if val in (p.get("domains") or []))
        if kind == "author":
            return sum(1 for p in prs if ((p.get("author") or {}).get("norm") or "") == val)
        return None

    def chip(kind, val, label=None, on=True):
        # The count rides on the chip so an unlit one still says what it is
        # keeping off the page: "stampable · 5" is a fact you can act on,
        # "stampable" is a question.
        n = rows_matching(kind, val)
        if kind == "since":
            tip = f"Hide rows opened more than {val.rstrip('d')} days ago. This one is a threshold, not a set: the longest lit window wins."
        else:
            tip = (f"{n} row{'s' if n != 1 else ''} in this group. Lit: they are shown. Unlit: they are hidden. "
                   "A row shows only while its value is lit in every group, so turning a whole group off empties the board.")
        shown = esc(label or val) + (f' <span class="fcount">{n}</span>' if n is not None else "")
        return (f'<button class="fchip{" on" if on else ""}" data-filter="{esc(kind)}" data-value="{esc(val)}" '
                f'title="{esc(tip)}">{shown}</button>')

    parts = ['<div class="mock-bar">']
    # All four lit: the composed command already acts on the stampable rows,
    # so hiding them would mean the default command merges PRs the page never
    # showed you. Turn a group off yourself when you want a shorter board.
    parts += [chip("view", "judge", "needs a decision", on=True), chip("view", "route", "route", on=True),
              chip("view", "stamp", "stampable", on=True), chip("view", "blocked", "blocked", on=True)]
    parts.append('<span class="sep"></span>')
    parts += [chip("owner", o, f"owner: {o}") for o in owners]
    parts.append('<span class="sep"></span>')
    parts += [chip("domain", d) for d in domains]
    parts.append('<span class="sep"></span>')
    parts += [chip("author", a, f"author: {a}") for a in authors]
    parts.append('<span class="sep"></span>')
    parts += [chip("since", s, f"since: {s}", on=False) for s in ("1d", "7d", "30d")]
    parts.append('<span class="sep"></span>')
    parts.append('<button class="fchip lever" id="foldall" type="button" aria-pressed="false" '
                 'title="Open every folded panel on the whole board at once -- reviewer&#x27;s guides, preview links, '
                 'diff quotes, the reasons behind a verdict, this manual, the collisions section -- or close them all '
                 'back down. Each panel still opens and closes on its own.">expand every panel</button>')
    parts.append("</div>")
    parts.append('<p class="empty" id="empty" hidden>No rows match these chips. Every lit chip is a row you want to see; a group with nothing lit hides everything. <button class="btn" id="reset-filters" type="button">reset chips</button></p>')
    return "".join(parts)


def group_rows(prs: list[dict]) -> list[tuple[str, str, list[dict]]]:
    """Grouped owner -> domain, and inside a group strictly by PR number,
    ascending. Verdict is on the row, in the tally and on a filter chip;
    sorting by it as well only meant that finding #21598 on the page
    required knowing its verdict first. A number is the one thing about a
    row you always already have."""
    groups: dict[tuple[str, str], list[dict]] = {}
    for p in prs:
        key = (owner_label(p), ", ".join(p.get("domains") or []) or "other")
        groups.setdefault(key, []).append(p)
    order = lambda k: (0 if k[0] == "mine" else 1, k[0], k[1])  # noqa: E731
    return [(o, d, sorted(rows, key=lambda p: p["number"]))
            for (o, d), rows in sorted(groups.items(), key=lambda kv: order(kv[0]))]


# ---- pages --------------------------------------------------------------------

PAYLOAD_DROP = {"patch", "author_body", "brief_body", "body", "triage_prose", "one_click_suggestions"}


def slim(obj):
    """The inlined copy of the queue minus the bulk (patches, comment
    bodies): what a viewer might copy out, not a second render source."""
    if isinstance(obj, dict):
        # `_`-prefixed keys are the analyzer's private scratch (live config
        # objects, not JSON): never part of what a viewer might copy out.
        return {k: slim(v) for k, v in obj.items() if k not in PAYLOAD_DROP and not str(k).startswith("_")}
    if isinstance(obj, list):
        return [slim(x) for x in obj]
    return obj


def payload_json(obj) -> str:
    """The slimmed queue as JSON that is inert inside
    `<script type="application/json">`. Escaping only `</` is not enough:
    the HTML parser has a double-escaped script state, and a title or path
    carrying `<!--<script>` puts it there, after which the JSON block
    swallows the page's real `<script>` up to end of file and every button
    goes dead. Every `<`, `>` and `&` leaves as a JSON escape instead, which
    is still the same JSON to any reader."""
    return (json.dumps(slim(obj), sort_keys=True)
            .replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026"))



def _wait_flag(p: dict) -> str:
    state = (p.get("checks") or {}).get("state")
    return " ✗" if state == "red" else (" ⚠" if p.get("mergeable_state") == "dirty" else "")


def sent_back_on(p: dict) -> str:
    """The date the approver sent this PR back, off its `sent-back:<date>`
    reason code; empty when the row carries none."""
    return next((r.partition(":")[2] for r in p.get("reasons") or [] if r.startswith("sent-back:")), "")


def _waiting_items(queue: dict, rows: list[dict], who_of) -> str:
    items = []
    for p in rows:
        title = p.get("title") or ""
        title = title if len(title) <= 72 else title[:69] + "…"
        items.append(f'<li><a class="pr" href="{esc(pr_url(queue, p["number"]))}">#{p["number"]}</a> '
                     f'<span class="wt">{esc(title)}</span> <span class="who">{esc(who_of(p))}</span> '
                     f'<span class="age">{_age_days(p)}d{_wait_flag(p)}</span></li>')
    return "".join(items)


def waiting_html(prs: list[dict], queue: dict | None = None) -> str:
    """The compact 'waiting on others' list: one line per handed-off PR,
    for awareness only. Nothing here is actionable by the approver."""
    queue = queue or {"repo": "pulumi/docs"}
    rows = [p for p in prs if p.get("handed_off")]
    if not rows:
        return ""
    rows.sort(key=lambda p: (", ".join(p.get("handed_off_to") or []), -_age_days(p)))
    items = _waiting_items(queue, rows, lambda p: ", ".join(p.get("handed_off_to") or []))
    return (f'<section class="waiting"><div class="sec-head"><h2>Waiting on others</h2><span class="count">{len(rows)}</span>'
            '<span class="note">requested reviewer isn\'t you · ✗ red CI · ⚠ conflict · hidden from the groups above; render with --include-handed-off to act on them</span></div>'
            '<ul>' + items + "</ul></section>")


def waiting_on_author_html(prs: list[dict], queue: dict | None = None) -> str:
    """The compact 'waiting on the author' list: rows the approver already
    sent back (`waiting_on_author`, with a `sent-back:<date>` chip) and
    nothing has been pushed since. Same shape as the handed-off list: who
    it waits on is the author, and the date is when you asked."""
    queue = queue or {"repo": "pulumi/docs"}
    rows = [p for p in prs if p.get("waiting_on_author") and not p.get("handed_off")]
    if not rows:
        return ""
    rows.sort(key=lambda p: (sent_back_on(p), -_age_days(p)))

    def who(p: dict) -> str:
        login = (p.get("author") or {}).get("login") or "author"
        when = sent_back_on(p)
        return f"@{login} · sent back {when}" if when else f"@{login} · sent back"

    items = _waiting_items(queue, rows, who)
    return (f'<section class="waiting"><div class="sec-head"><h2>Waiting on the author</h2><span class="count">{len(rows)}</span>'
            '<span class="note">you sent these back and nothing has been pushed since · ✗ red CI · ⚠ conflict · '
            'they return to the groups above when a commit lands; render with --include-handed-off to act on one now</span></div>'
            '<ul>' + items + "</ul></section>")


def render_board(queue: dict, *, artifact: bool = False, include_handed_off: bool = False) -> str:
    all_prs = queue.get("prs") or []
    prs = all_prs if include_handed_off else [p for p in all_prs if not parked(p)]
    counts = queue.get("counts") or {}
    cfg = queue.get("config") or {}
    sections = []
    for owner, domain, rows in group_rows(prs):
        sections.append(f'<section class="grp"><div class="sec-head"><h2>{esc(owner)}</h2><span class="dlabel">{esc(domain)}</span><span class="count">{len(rows)}</span></div>'
                        + "".join(row_html(queue, p) for p in rows) + "</section>")
    tally = "".join(f'<div class="t-{VERDICT_CLASS[v]}" title="{esc(VERDICT_HELP.get(v, ""))}">'
                    f'<b>{counts.get(v, 0)}</b><span>{v}</span></div>' for v in VERDICT_ORDER)
    if counts.get("handed-off"):
        tally += (f'<div class="t-dim" title="PRs whose requested reviewer is someone other than you. They are waiting on that person, '
                  f'so they are listed at the foot of the page instead of taking a row.">'
                  f'<b>{counts["handed-off"]}</b><span>waiting on others</span></div>')
    on_author = sum(1 for p in all_prs if p.get("waiting_on_author") and not p.get("handed_off"))
    if on_author:
        tally += (f'<div class="t-dim" title="PRs you already sent back to their author, with nothing pushed since. They are waiting '
                  f'on the author, so they are listed at the foot of the page instead of taking a row.">'
                  f'<b>{on_author}</b><span>waiting on the author</span></div>')
    stuck = sum(1 for p in prs if no_action(p))
    if stuck:
        tally += (f'<div class="t-stop" title="Blocked rows that carry no unblock at all: nothing on this page changes them, so '
                  f'each one says so on its row. They are counted here so a silent row can never hide in the blocked tally.">'
                  f'<b>{stuck}</b><span>blocked, no action</span></div>')
    payload = payload_json(queue)
    return (FRAGMENT if artifact else PAGE).format(
        title="PR review queue",
        style=STYLE,
        eyebrow=header_line(queue),
        h1="PR review queue",
        dek=esc(f"{len(prs)} open PRs, one verdict each (stamp / judge / route / blocked), grouped by owner and domain and listed in PR number order. Stamp rows start selected; every other decision is a button on the row it concerns, and every button is a toggle that adds to the command at the bottom — the page never talks to GitHub. A badge beside a finding says why it does not stop the merge; the author has not answered anything here."),
        tally=f'<div class="tally">{tally}</div>' + help_html() + '<div class="progress" id="progress"></div>',
        filters=filter_bar({**queue, "prs": prs}),
        clusters="",
        body=("".join(sections) or '<p class="empty">Nothing to adjudicate.</p>') + clusters_html(queue)
             + ("" if include_handed_off else waiting_html(all_prs, queue) + waiting_on_author_html(all_prs, queue)),
        cmd=cmd_footer(),
        payload=payload,
        script=SCRIPT,
    )


def render_detail(queue: dict, n: int, *, artifact: bool = False) -> str:
    pr = next((p for p in queue.get("prs") or [] if p["number"] == n), None)
    if pr is None:
        raise SystemExit(f"#{n} is not in the queue (drafts and filtered rows are not collected)")
    payload = payload_json({**queue, "prs": [pr]})
    return (FRAGMENT if artifact else PAGE).format(
        title=f"#{n} · {esc(pr.get('title'))}",
        style=STYLE,
        eyebrow=esc(f"{queue.get('repo')} · #{n} · {queue.get('analyzed_at') or queue.get('generated_at')}"),
        h1=esc(pr.get("title")),
        dek=verdict_chip(pr) + " " + esc(pr.get("summary") or ""),
        tally="",
        filters="",
        clusters="",
        body=row_html(queue, pr, expanded=True),
        cmd=cmd_footer(),
        payload=payload,
        script=SCRIPT,
    )


def cmd_footer() -> str:
    """Two lines, because there are two kinds of move. The `--act` command is
    the batch of writes `act.py` makes. The line above it, which appears only
    when a "fix it yourself" is lit, is one interactive run per PR — a
    different thing entirely, so it is never folded into the same command."""
    return ('<div class="cmdwrap">'
            '<div class="cmdrow hand" id="handwrap" hidden>'
            '<span class="handlabel" title="Each of these is its own interactive run: /address-review walks the PR\'s open '
            'findings with you and pushes the fixes to the branch. They are not part of the --act command below, and '
            'nothing here runs until you invoke it.">then, one at a time</span>'
            '<div class="cmd" id="handcmd"></div>'
            '<button class="btn" id="copyhand">copy</button></div>'
            '<div class="cmdrow"><div class="cmd" id="cmd">$ /pr-review --act</div>'
            '<button class="btn" id="copy">copy</button><button class="btn" id="clear">clear</button></div>'
            '</div>')


def open_items(pr: dict) -> list[dict]:
    """The findings nobody has ruled on: the review's open rows (style and
    pre-existing aside) plus triage's prose bullets. What `pending_judgment`
    boxes on the board, and what the terminal lists under `open:`."""
    review = pr.get("review") or {}
    items = [i for i in review.get("items") or []
             if not i.get("disposition") and i.get("bucket") not in ("style", "pre-existing", "preexisting")]
    if pr.get("triage_prose"):
        bullets = [l.strip("- ").strip() for l in pr["triage_prose"].splitlines() if l.startswith("- [")]
        items += [{"id": f"triage:{i + 1}", "summary": b, "bucket": "reviewer-check"} for i, b in enumerate(bullets)]
    return items


def _wrap(text: str, width: int, first: str, rest: str) -> list[str]:
    """Wrap without ever cutting: a reason code or a command is only useful
    whole, so a token longer than the line gets a line to itself."""
    return textwrap.wrap(text, width=width, initial_indent=first, subsequent_indent=rest,
                         break_long_words=False, break_on_hyphens=False) or [first.rstrip()]


def render_terminal(queue: dict, n: int | None = None, width: int = 110, include_handed_off: bool = False) -> str:
    """The board as text: the same rows, blockers, findings, actions and
    Do-next moves, so a terminal reader can compose the same command the
    page would. Nothing is cut short; long lines wrap under their row."""
    all_prs = queue.get("prs") or []
    prs = all_prs if (include_handed_off or n is not None) else [p for p in all_prs if not parked(p)]
    if n is not None:
        prs = [p for p in prs if p["number"] == n]
    counts = queue.get("counts") or {}
    on_author = [p for p in all_prs if p.get("waiting_on_author") and not p.get("handed_off")]
    stuck = [p for p in prs if no_action(p)]
    head = (f"PR review queue · {queue.get('repo')} · {len(prs)} rows · "
            + " · ".join(f"{counts.get(v, 0)} {v}" for v in VERDICT_ORDER)
            + (f" · {counts['handed-off']} waiting on others" if counts.get("handed-off") else "")
            + (f" · {len(on_author)} waiting on the author" if on_author else "")
            + (f" · {len(stuck)} blocked with no action" if stuck else ""))
    lines = [head, ""]
    hdr = f"{'#':>6}  {'verdict':<8} {'owner':<11} {'domain':<14} {'size':>9} {'age':>5} {'CI':<4} reasons"
    lines += [hdr, "-" * len(hdr)]
    sub = " " * 8      # continuation lines sit under the verdict column
    for owner, domain, rows in group_rows(prs):
        for p in rows:
            reasons = [r for r in p.get("reasons") or [] if not r.startswith(HIDDEN_REASON_PREFIXES)]
            ci = {"green": "✓", "red": "✗", "pending": "…"}.get((p.get("checks") or {}).get("state"), "?")
            size = f"+{p.get('additions', 0)}/−{p.get('deletions', 0)}"
            prefix = (f"{p['number']:>6}  {p.get('verdict'):<8} {owner[:11]:<11} {domain[:14]:<14} {size:>9} "
                      f"{age_label(p):>5} {ci:<4} ")
            lines += _wrap(" ".join(reasons), width, prefix, sub + "  ")
            if p.get("verdict") == "blocked":
                blocked = ", ".join(p.get("blockers") or []) or "no blocker named"
                lines += _wrap(blocked + (" (no action available)" if no_action(p) else ""), width, sub + "blocked: ", sub + "         ")
            if not p.get("judgments"):
                items = open_items(p)
                for i in items[:6]:
                    body = finding_body(i)
                    parts = split_finding(body)
                    stance = parts["stance"] or NO_STANCE
                    claim = one_sentence(parts["claim"] or body or i.get("summary") or "", 160)
                    where = f" @ {i['file']} {i.get('anchor') or ''}".rstrip() if i.get("file") else ""
                    lines += _wrap(f"{i.get('id') or ''} {claim} [{stance[1]}]{where}", width, sub + "open: ", sub + "      ")
                if len(items) > 6:
                    lines.append(f"{sub}      … {len(items) - 6} more on the PR")
            for j in p.get("judgments") or []:
                lines += _wrap(f"{j.get('finding_id') or ''} {j.get('decision') or ''} → {j.get('disposition') or '?'}"
                               + (f" ({j['note']})" if j.get("note") else "") + (f" {j['deep_link']}" if j.get("deep_link") else ""),
                               width, sub + "judged: ", sub + "        ")
            for a in p.get("actions") or []:
                lines += _wrap(f"[{a['label']}]  {scope_reasons(a['cmd'])}", width, sub, sub + "    ")
            for h in p.get("handoffs") or []:
                lines += _wrap(f"[{h['label']}]  $ {h['run']}  (an interactive run, not part of --act)", width, sub, sub + "    ")
    cards = queue.get("do_next") or [] if n is None else []
    if cards:
        lines += ["", "do next (the row actions above, batched into one command each):"]
        for i, d in enumerate(cards, 1):
            lines += _wrap(d.get("say") or "", width, f"  {i}. ", "     ")
            if d.get("does"):
                lines += _wrap(d["does"], width, "     ", "     ")
            if d.get("cmd"):
                lines += _wrap(f"$ /pr-review --act {scope_reasons(d['cmd'])}", width, "     ", "         ")
    cl = queue.get("clusters") or []
    if cl:
        lines += ["", "collisions:"]
        for c in cl:
            order = c.get("merge_order") or []
            if order:
                lines += _wrap(f"{c['id']} {c['kind']}: merge " + " → ".join(f"#{x}" for x in order), width, "  ", "      ")
            else:
                # Every member is handed off: analyze strips them from the
                # order, so the order is empty and the members are the news.
                lines += _wrap(f"{c['id']} {c['kind']}: " + ", ".join(f"#{x}" for x in c.get("prs") or []) + " (all waiting on others)",
                               width, "  ", "      ")
            rec = c.get("recommendation") or {}
            if rec.get("say"):
                lines += _wrap(rec["say"] + (f"  → {scope_reasons(rec['cmd'])}" if rec.get("cmd") else ""), width, "      ", "      ")
    for d in queue.get("directional") or []:
        lines.append(f"  directional {d['path']}: #{d['adds_links_pr']} adds links, #{d['removes_links_pr']} removes them")
    judge = [p for p in prs if p.get("verdict") == "judge"]
    if judge:
        lines += ["", "judge rows (AskUserQuestion each in --terminal mode):"]
        for p in judge:
            lines.append(f"  #{p['number']} {p.get('title')}")
    waiting = [p for p in all_prs if p.get("handed_off")] if not include_handed_off and n is None else []
    if waiting:
        lines += ["", f"waiting on others ({len(waiting)}):"]
        for p in waiting:
            lines.append(f"  #{p['number']} {(p.get('title') or '')[:60]:<60} {', '.join(p.get('handed_off_to') or [])} {_age_days(p)}d{_wait_flag(p)}")
    if on_author and not include_handed_off and n is None:
        lines += ["", f"waiting on the author ({len(on_author)}):"]
        for p in on_author:
            when = sent_back_on(p)
            lines.append(f"  #{p['number']} {(p.get('title') or '')[:60]:<60} @{(p.get('author') or {}).get('login') or '?'}"
                         f" sent back {when or '?'} {_age_days(p)}d{_wait_flag(p)}")
    stamps = [a["cmd"].split()[1] for p in prs for a in p.get("actions") or [] if a["id"] == "stamp" and p.get("verdict") == "stamp"]
    if stamps:
        lines += ["", f"$ /pr-review --act --stamp {','.join(stamps)}"]
    return "\n".join(lines) + "\n"


# ---- template ---------------------------------------------------------------------

STYLE = r"""
:root{--ground:#f7f5fa;--surface:#fff;--surface-2:#f1eef6;--ink:#191622;--ink-2:#4a4358;--ink-3:#736b82;--line:#e3deec;--line-2:#cfc7dd;--accent:#6b3fa0;--accent-soft:#efe8f8;--go:#1c6b45;--go-soft:#e2f2ea;--hold:#94530c;--hold-soft:#fbeedb;--stop:#a32219;--stop-soft:#fbe6e4;--route:#1f5c8a;--route-soft:#e3eef8;--shadow:0 1px 2px rgba(25,22,34,.05),0 8px 24px -16px rgba(25,22,34,.3)}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--ground:#131119;--surface:#1b1824;--surface-2:#231f2f;--ink:#f0ecf6;--ink-2:#bdb5cc;--ink-3:#8e86a0;--line:#2e2839;--line-2:#443c54;--accent:#c4a2ee;--accent-soft:#2a2138;--go:#7fd6a9;--go-soft:#16281f;--hold:#f0bd76;--hold-soft:#2e2316;--stop:#f5a099;--stop-soft:#301816;--route:#8fc1ee;--route-soft:#172433;--shadow:0 1px 2px rgba(0,0,0,.4),0 8px 24px -16px rgba(0,0,0,.8)}}
:root[data-theme="dark"]{--ground:#131119;--surface:#1b1824;--surface-2:#231f2f;--ink:#f0ecf6;--ink-2:#bdb5cc;--ink-3:#8e86a0;--line:#2e2839;--line-2:#443c54;--accent:#c4a2ee;--accent-soft:#2a2138;--go:#7fd6a9;--go-soft:#16281f;--hold:#f0bd76;--hold-soft:#2e2316;--stop:#f5a099;--stop-soft:#301816;--route:#8fc1ee;--route-soft:#172433;--shadow:0 1px 2px rgba(0,0,0,.4),0 8px 24px -16px rgba(0,0,0,.8)}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);font-family:"IBM Plex Sans",ui-sans-serif,system-ui,sans-serif;font-size:15px;line-height:1.55;-webkit-font-smoothing:antialiased}
.wrap{max-width:1120px;margin:0 auto;padding:32px 16px 120px}
h1,h2,h3,h4,h5{font-family:Archivo,"IBM Plex Sans",sans-serif;margin:0;text-wrap:balance}
code,.mono,pre,.cmd,.chip,.v,.pr,.btn,.fchip{font-family:"IBM Plex Mono",ui-monospace,monospace}
code{font-size:.92em;background:var(--surface-2);padding:1px 5px;border-radius:2px}
pre{background:var(--surface-2);border:1px solid var(--line);border-radius:3px;padding:12px 14px;font-size:12.5px;line-height:1.5;overflow-x:auto;white-space:pre-wrap;margin:8px 0}
a{color:var(--accent)}
.mast{border-bottom:2px solid var(--ink);padding-bottom:18px;margin-bottom:22px}
.eyebrow{font-family:"IBM Plex Mono",monospace;font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-3);margin-bottom:8px}
h1{font-size:clamp(26px,4.6vw,40px);font-weight:800;letter-spacing:-.022em;line-height:1.05}
.dek{color:var(--ink-2);max-width:72ch;margin:10px 0 0;font-size:15.5px}
.tally{display:flex;flex-wrap:wrap;gap:10px;margin:18px 0 6px}
.tally div{flex:1 1 120px;background:var(--surface);border:1px solid var(--line);border-radius:3px;padding:10px 14px;box-shadow:var(--shadow)}
.tally b{display:block;font-family:Archivo,sans-serif;font-size:28px;font-weight:700;line-height:1.1}
.tally span{font-size:12px;color:var(--ink-3)}
.t-go b{color:var(--go)}.t-hold b{color:var(--hold)}.t-stop b{color:var(--stop)}.t-route b{color:var(--route)}
.mock-bar{display:flex;gap:6px;flex-wrap:wrap;align-items:center;padding:12px 0;border-bottom:1px solid var(--line);margin-bottom:8px;position:sticky;top:env(safe-area-inset-top,0px);background:var(--ground);z-index:2}
.sep{width:1px;height:18px;background:var(--line-2);margin:0 4px}
.fchip{font-size:11.5px;border:1px solid var(--line-2);border-radius:99px;padding:2px 10px;color:var(--ink-2);background:var(--surface-2);cursor:pointer}
.fchip.lever{margin-left:auto}
.fchip.on{background:var(--accent-soft);color:var(--accent);border-color:var(--accent)}
.fcount{font-size:10px;opacity:.75;margin-left:3px}
.grp{margin-top:26px}
.sec-head{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap;margin-bottom:4px}
h2{font-size:21px;font-weight:700;letter-spacing:-.015em}
.dlabel{font-family:"IBM Plex Mono",monospace;font-size:12.5px;font-weight:600;background:var(--accent-soft);color:var(--accent);padding:2px 9px;border-radius:3px}
.count{font-family:"IBM Plex Mono",monospace;font-size:12px;color:var(--ink-3);border:1px solid var(--line-2);border-radius:99px;padding:1px 9px}
.mrow{display:grid;grid-template-columns:74px 1fr;gap:12px;padding:12px 0 12px 10px;border-bottom:1px solid var(--line);border-left:3px solid transparent}
.mrow.go{border-left-color:var(--go)}.mrow.hold{border-left-color:var(--hold)}.mrow.stop{border-left-color:var(--stop)}.mrow.route{border-left-color:var(--route)}
.mrow[hidden]{display:none}
.mrow>div{min-width:0}
.jmeta,.sum,.card p,.jbox li,.detail td{overflow-wrap:anywhere}
.pr{font-size:12px;font-weight:600;background:var(--surface-2);border:1px solid var(--line-2);border-radius:3px;padding:2px 7px;color:var(--ink);text-decoration:none;white-space:nowrap;align-self:start;justify-self:start}
.prcell{display:flex;flex-direction:column;gap:4px;align-items:flex-start}
button.pr.rowfold{cursor:pointer;color:var(--ink-3);font-weight:500;font-size:11px}
.pr.diff{font-weight:500;font-size:11px;color:var(--accent);background:none;border-color:var(--accent-soft)}
.mrow h4{font-size:14.5px;font-weight:600;margin:0 0 3px;line-height:1.35}
.meta{font-size:12.5px;color:var(--ink-3);margin-bottom:4px}.meta span{margin-right:10px}.meta .age{font-family:"IBM Plex Mono",monospace;font-size:11px;margin-right:0}.meta .age.old{color:var(--hold)}
.chips{display:flex;flex-wrap:wrap;gap:4px;margin:2px 0 6px}
.chip{font-size:10.5px;border:1px solid var(--line-2);border-radius:2px;padding:1px 6px;color:var(--ink-2);background:var(--surface-2);white-space:nowrap}
.chip.r-collision,.chip.r-directional,.chip.r-duplicate,.chip.r-self-accepted,.chip.r-checks,.chip.r-mergeable{border-color:var(--stop);color:var(--stop)}
.empty{margin:1rem 0;color:var(--ink-2);font-size:.95rem}.empty .btn{margin-left:.5rem}
.chip.r-warnings,.chip.r-outstanding,.chip.r-scrutiny,.chip.r-blog,.chip.r-size,.chip.r-shape,.chip.r-review{border-color:var(--hold);color:var(--hold)}
.chip.r-route{border-color:var(--route);color:var(--route)}
.chip.theirs{opacity:.55;border-style:dashed}
.chip.cfg{border-style:dotted}
.cfgdot{font-size:8.5px;opacity:.65;margin-left:3px;vertical-align:super}
.chip.r-cluster{border-color:var(--route);color:var(--route)}
details.why{display:inline-block;margin-left:4px}details.why>summary{font-family:"IBM Plex Mono",monospace;font-size:10.5px;color:var(--ink-3);cursor:pointer;list-style:none;border:1px dashed var(--line-2);border-radius:2px;padding:1px 6px}
details.why[open]>summary{margin-bottom:4px}details.why .chip{opacity:.8}
.qrow{display:flex;gap:10px;align-items:flex-start;justify-content:space-between}
.jnote{font-size:12.5px;color:var(--ink-2);margin:2px 0 4px}
details.quote>summary{font-family:"IBM Plex Mono",monospace;font-size:11px;color:var(--ink-3);cursor:pointer}
details.quote[open]>summary{margin-bottom:3px}
.acts{margin-top:8px;display:flex;gap:6px;flex-wrap:wrap;align-items:center}
.acts .btn.p{margin-left:auto;padding:5px 12px;font-size:12px}
.btn.p-go{background:var(--go);border-color:var(--go)}.btn.p-hold{background:var(--hold);border-color:var(--hold)}.btn.p-route{background:var(--route);border-color:var(--route)}.btn.p-stop{background:var(--stop);border-color:var(--stop)}
.progress{font-family:"IBM Plex Mono",monospace;font-size:12px;color:var(--ink-3);margin:6px 0 10px}
details.help{margin:10px 0 4px;border:1px solid var(--line-2);border-radius:4px;background:var(--surface);box-shadow:var(--shadow)}
details.help>summary{cursor:pointer;list-style:none;padding:9px 14px;font-family:"IBM Plex Mono",monospace;font-size:12px;letter-spacing:.04em;color:var(--ink-2)}
details.help[open]>summary{border-bottom:1px solid var(--line)}
.helpgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px 24px;padding:12px 16px 16px}
.helpgrid h4{font-size:12.5px;text-transform:uppercase;letter-spacing:.07em;color:var(--ink-3);margin:0 0 4px}
.helpgrid ul{margin:0;padding-left:16px}
.helpgrid li{font-size:13px;color:var(--ink-2);margin:3px 0;line-height:1.45}
.claimnote{font-family:"IBM Plex Mono",monospace;font-size:11px;color:var(--go);border:1px dashed var(--go);border-radius:3px;padding:2px 7px}
.clusters{margin-top:28px}.clusters summary{cursor:pointer;display:flex;gap:10px;align-items:baseline;flex-wrap:wrap;list-style:none}
/* a flex summary drops the browser's own marker, so these folds draw their own */
.clusters summary::-webkit-details-marker,details.help>summary::-webkit-details-marker{display:none}
.clusters summary::before,details.help>summary::before{content:"\25B8";display:inline-block;margin-right:6px;color:var(--ink-3);transition:transform .12s ease}
.clusters details[open]>summary::before,details.help[open]>summary::before{transform:rotate(90deg)}.clusters summary h2{display:inline}.clusters .note{font-size:12px;color:var(--ink-3)}
.chip.r-handed-off{border-color:var(--ink-3);color:var(--ink-3)}
.t-dim b{color:var(--ink-3)}
.waiting{margin-top:30px;border-top:1px solid var(--line-2);padding-top:14px}
.waiting .note{flex:1 1 100%;font-size:12px;color:var(--ink-3)}
.waiting ul{list-style:none;margin:6px 0 0;padding:0;columns:2;column-gap:24px}
.waiting li{break-inside:avoid;font-size:12.5px;display:flex;gap:8px;align-items:baseline;padding:2px 0;min-width:0}
.waiting .wt{flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;color:var(--ink-2)}
.waiting .who{font-family:"IBM Plex Mono",monospace;font-size:11px;color:var(--route);white-space:nowrap}
.waiting .age{font-family:"IBM Plex Mono",monospace;font-size:11px;color:var(--ink-3);white-space:nowrap}
@media (max-width:800px){.waiting ul{columns:1}}
.sum{font-size:13.5px;color:var(--ink-2);margin:0 0 4px}
.v{font-size:10.5px;font-weight:600;letter-spacing:.07em;text-transform:uppercase;padding:2px 7px;border-radius:2px;white-space:nowrap;display:inline-block;vertical-align:middle}
.v-stamp{background:var(--go-soft);color:var(--go)}.v-judge{background:var(--hold-soft);color:var(--hold)}.v-route{background:var(--route-soft);color:var(--route)}.v-blocked{background:var(--stop-soft);color:var(--stop)}.v-dim{background:var(--surface-2);color:var(--ink-3);text-transform:none;letter-spacing:0}
.jbox{margin-top:8px;background:var(--hold-soft);border-radius:3px;padding:9px 11px;font-size:13px}
.jbox.stop{background:var(--stop-soft)}.jbox.pending{background:var(--surface-2)}
.jbox .q{font-weight:600;color:var(--ink);margin-bottom:5px}
.jbox ul{margin:0;padding-left:18px}.jbox li{margin:2px 0}
.jmeta{margin-top:5px;color:var(--ink-2)}
.jfoot{font-size:12.5px;color:var(--ink-3);margin:6px 0 0;font-style:italic}
.jfoot code{font-style:normal}
.diffq{font-family:"IBM Plex Mono",monospace;font-size:12px;background:var(--surface);border:1px solid var(--line);border-radius:3px;padding:6px 9px;margin:6px 0;overflow-x:auto;white-space:pre}
.diffq .del{color:var(--stop)}.diffq .add{color:var(--go)}.diffq .hunk{color:var(--ink-3)}
.dfile{margin-top:6px}.dfile>a{font-family:"IBM Plex Mono",monospace;font-size:11.5px}
details.guide{margin:2px 0}
details.guide>summary{font-family:"IBM Plex Mono",monospace;font-size:11px;color:var(--ink-3);cursor:pointer}
details.guide h5{font-size:11.5px;text-transform:uppercase;letter-spacing:.06em;color:var(--ink-3);margin:6px 0 2px}
details.guide ul{margin:0;padding-left:18px}
details.guide li{font-size:13px;color:var(--ink-2);margin:2px 0}
details.preview{margin:2px 0 6px}
details.preview>summary{font-family:"IBM Plex Mono",monospace;font-size:11px;color:var(--ink-3);cursor:pointer}
details.preview ul{margin:4px 0 0;padding-left:18px}
details.preview li{font-size:13px;margin:2px 0}
details.preview .jmeta{font-family:"IBM Plex Mono",monospace;font-size:11px}
.btn{font-size:11.5px;font-weight:600;border:1px solid var(--line-2);border-radius:3px;padding:3px 9px;background:var(--surface);color:var(--ink-2);cursor:pointer;text-decoration:none}
.btn.p{background:var(--accent);color:#fff;border-color:var(--accent)}.btn.sel{outline:2px solid var(--go);outline-offset:1px}.btn.sel::before{content:"✓ "}
.btn.hand{border-color:var(--hold);color:var(--hold);border-style:dashed}
.btn.hand.sel{outline-color:var(--hold);background:var(--hold-soft)}
.two{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:12px;margin:12px 0}
.card{background:var(--surface);border:1px solid var(--line);border-radius:3px;padding:12px 14px}
.card h4{margin:0 0 6px;font-size:14px}.card p{font-size:13.5px;color:var(--ink-2);margin:0 0 6px}.card ul{margin:0;padding-left:18px;font-size:13px;color:var(--ink-2)}
.card.no{border-left:3px solid var(--stop)}.card.mid{border-left:3px solid var(--hold)}
.clusters{margin-top:18px}
.detail{margin-top:14px;border-top:1px dashed var(--line-2);padding-top:10px}
.detail h5{font-size:13px;margin:14px 0 6px;text-transform:uppercase;letter-spacing:.06em;color:var(--ink-3)}
table{width:100%;border-collapse:collapse;font-size:13px}
th{font-family:"IBM Plex Mono",monospace;font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3);text-align:left;padding:6px 8px;border-bottom:1px solid var(--line-2)}
td{padding:6px 8px;border-bottom:1px solid var(--line);vertical-align:top;color:var(--ink-2)}
.pages li,.files li{margin:3px 0;font-size:13.5px}
.shot{max-width:100%;border:1px solid var(--line-2);border-radius:3px;margin-top:6px}
.note{font-size:13px;color:var(--ink-3)}
.cmdwrap{position:fixed;left:0;right:0;bottom:0;background:var(--ground);border-top:1px solid var(--line-2);padding:10px 16px calc(10px + env(safe-area-inset-bottom,0px));display:flex;flex-direction:column;gap:6px;z-index:3}
.cmdrow{display:flex;gap:8px;align-items:center}
.cmdrow[hidden]{display:none}
.handlabel{font-family:"IBM Plex Mono",monospace;font-size:10.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--hold);white-space:nowrap}
#handcmd{background:var(--hold-soft);color:var(--ink);border:1px solid var(--hold);white-space:pre;line-height:1.5}
.wrap{padding-inline:16px}
.cmd{flex:1;background:var(--ink);color:var(--ground);border-radius:3px;padding:8px 12px;font-size:12.5px;overflow-x:auto;white-space:nowrap}
.empty{color:var(--ink-3)}
@media (max-width:600px){.mrow{grid-template-columns:1fr}.mrow>div:last-child{grid-column:1/-1}}
"""

SCRIPT = r"""
(function(){
  var cmdEl = document.getElementById('cmd');
  // The command is read off the lit buttons themselves, never off a shadow
  // list, so what the bar shows can't lag a click. Every button is a row
  // button: there is no batch strip, so nothing on the page can carry a
  // fragment a row does not.
  function fragment(b){ return b.dataset.cmd; }
  // Every `--stamp N[:mode][ --force]` folds into the one --stamp list, with
  // --force said once for the batch: a second --stamp would be a second flag,
  // and an act.py that read it single-valued would drop every PR but the last.
  var STAMP = /^--stamp (\d+(?::(?:no-)?merge)?)( --force)?$/;
  function compose(){
    var seen = {}, stamps = [], others = [], force = false;
    // by PR number, so the command reads the same however it was clicked
    var lit = [].slice.call(document.querySelectorAll('button.btn.sel[data-cmd]')).map(function(b, i){
      return { b: b, n: parseInt(b.dataset.pr, 10), i: i };
    }).sort(function(x, y){ return (isNaN(x.n) ? 1e9 : x.n) - (isNaN(y.n) ? 1e9 : y.n) || x.i - y.i; });
    lit.forEach(function(e){
      var b = e.b, c = fragment(b); if (!c) return;
      var k = b.dataset.pr + ':' + c; if (seen[k]) return; seen[k] = true;   // twins are one selection
      var m = c.match(STAMP);
      if (m) { if (stamps.indexOf(m[1]) < 0) stamps.push(m[1]); if (m[2]) force = true; }
      else if (others.indexOf(c) < 0) others.push(c);                        // never the same fragment twice
    });
    stamps.sort(function(a, b){ return parseInt(a, 10) - parseInt(b, 10); });
    var out = '$ /pr-review --act';
    if (stamps.length) out += ' --stamp ' + stamps.join(',') + (force ? ' --force' : '');
    if (others.length) out += ' ' + others.join(' ');
    cmdEl.textContent = out;
  }
  // The same decision can be on the board twice -- once on the compact row,
  // once in the expanded card -- and the two must never disagree, so a
  // selection is painted on every button carrying the same PR and command.
  function twins(b){
    return [].slice.call(document.querySelectorAll('button.btn[data-pr="' + b.dataset.pr + '"]')).filter(function(o){
      return o.dataset.cmd === b.dataset.cmd;
    });
  }
  function paint(o, on){
    o.classList.toggle('sel', on);
    o.setAttribute('aria-pressed', on ? 'true' : 'false');
  }
  function setSel(b, on){
    if (b.dataset.run) { paint(b, on); return; }   // a handoff is its own line, with no twin and no fragment
    twins(b).forEach(function(o){ paint(o, on); });
  }
  function clearRow(pr, keep){
    document.querySelectorAll('button.btn.sel[data-kind="decision"][data-pr="' + pr + '"]').forEach(function(o){ if (o !== keep) setSel(o, false); });
  }
  // A chain button acts on a second row: once the lead lands, the next link
  // gets master merged in. That row has no button for it, so it is marked
  // covered while the chain is lit, and a decision picked there instead
  // puts the chain out -- the command can never carry both.
  function coveredBy(b){ return b.dataset.covers ? b.dataset.covers.split(',') : []; }
  function markCovered(b, on){
    coveredBy(b).forEach(function(pr){
      var r = document.querySelector('.mrow[data-pr="' + pr + '"]');
      if (!r) return;
      var acts = r.querySelector('.acts');
      var note = r.querySelector('.claimnote');
      if (on && acts && !note) {
        note = document.createElement('span');
        note.className = 'claimnote';
        note.textContent = '✓ covered by the chain from #' + b.dataset.pr;
        note.title = 'The chain button on #' + b.dataset.pr + ' merges master into this PR once that one lands, so there is nothing to pick here. Pick something anyway and the chain goes out.';
        acts.insertBefore(note, acts.firstChild);
      } else if (!on && note) { note.remove(); }
    });
  }
  function syncCovers(){
    document.querySelectorAll('button.btn[data-covers]').forEach(function(b){
      var lit = b.classList.contains('sel');
      var contradicted = coveredBy(b).some(function(pr){
        return !!document.querySelector('button.btn.sel[data-kind="decision"][data-pr="' + pr + '"]');
      });
      if (lit && contradicted) { setSel(b, false); lit = false; }
      markCovered(b, lit);
    });
  }
  // "Fix it yourself" is a run, not a write. It composes on its own line
  // above the --act command and never joins it: one `/address-review N` per
  // PR, because each is a separate interactive session.
  var handEl = document.getElementById('handcmd'), handWrap = document.getElementById('handwrap');
  function composeHand(){
    if (!handEl || !handWrap) return;
    var runs = [].slice.call(document.querySelectorAll('button.btn.hand.sel[data-run]')).map(function(b){
      return { run: b.dataset.run, n: parseInt(b.dataset.pr, 10) };
    }).sort(function(x, y){ return x.n - y.n; }).map(function(e){ return '$ ' + e.run; });
    handEl.textContent = runs.join('\n');
    handWrap.hidden = !runs.length;
  }
  document.querySelectorAll('button.btn.hand[data-run]').forEach(function(b){
    b.addEventListener('click', function(){ setSel(b, !b.classList.contains('sel')); composeHand(); });
  });
  var copyHand = document.getElementById('copyhand');
  if (copyHand) copyHand.addEventListener('click', function(){
    composeHand();
    if (navigator.clipboard) navigator.clipboard.writeText(handEl.textContent.replace(/^\$ /gm, ''));
  });
  // Every click ends here: the covered rows settle first, then the command
  // is read off whatever is lit, so the bar never shows one click ago.
  function settle(){ syncCovers(); compose(); composeHand(); progress(); }
  document.querySelectorAll('button.btn[data-cmd]').forEach(function(b){
    if (b.classList.contains('sel')) setSel(b, true);
    b.addEventListener('click', function(){
      var on = !b.classList.contains('sel');
      if (on && b.dataset.kind === 'decision') {   // one decision per row; side actions ride along
        clearRow(b.dataset.pr, b);
      }
      // Lighting a chain clears whatever was picked on the row it covers, so
      // the covered mark is that row's only state.
      if (on) coveredBy(b).forEach(function(pr){ clearRow(pr, null); });
      setSel(b, on);
      settle();
    });
  });
  document.getElementById('clear').addEventListener('click', function(){
    document.querySelectorAll('button.btn.sel').forEach(function(b){ setSel(b, false); }); settle();
  });
  // One lever for every fold on the board. The per-panel defaults are the
  // reading order (a guide and its preview links open, the reasons behind a
  // verdict and this manual closed); this is for the pass where you want
  // everything, or nothing, at once.
  // A row's fold button says what pressing it does next, so it has to
  // follow the row's state however the row got there -- including when the
  // board-wide lever moves every row at once.
  function setRowFold(b, open){
    b.setAttribute('aria-pressed', open ? 'true' : 'false');
    b.textContent = open ? 'fold ▴' : 'open ▾';
  }
  document.querySelectorAll('button.rowfold').forEach(function(b){
    b.addEventListener('click', function(){
      var row = b.closest('.mrow');
      if (!row) return;
      var open = b.getAttribute('aria-pressed') !== 'true';
      row.querySelectorAll('details').forEach(function(d){ d.open = open; });
      setRowFold(b, open);
    });
  });
  (function(){
    var fold = document.getElementById('foldall');
    if (!fold) return;
    fold.addEventListener('click', function(){
      var open = fold.getAttribute('aria-pressed') !== 'true';
      // The manual is not part of the report, so it keeps its own state.
      document.querySelectorAll('details:not(.help)').forEach(function(d){ d.open = open; });
      document.querySelectorAll('button.rowfold').forEach(function(b){ setRowFold(b, open); });
      fold.setAttribute('aria-pressed', open ? 'true' : 'false');
      fold.classList.toggle('on', open);
      fold.textContent = open ? 'collapse every panel' : 'expand every panel';
    });
  })();
  document.getElementById('copy').addEventListener('click', function(){
    compose();   // what goes to the clipboard is what is lit now, not what was last drawn
    var t = cmdEl.textContent.replace(/^\$ /, '');
    if (navigator.clipboard) navigator.clipboard.writeText(t);
  });
  var filters = { owner: {}, domain: {}, verdict: {}, author: {}, since: {}, view: {} };
  // `[data-filter]` on purpose: the fold lever wears the chip's styling but
  // is not a filter, and reading filters[undefined] here threw, which left
  // apply() unreached and every row visible whatever the chips said.
  document.querySelectorAll('.fchip[data-filter]').forEach(function(f){
    filters[f.dataset.filter][f.dataset.value] = f.classList.contains('on');
    f.addEventListener('click', function(){ f.classList.toggle('on'); filters[f.dataset.filter][f.dataset.value] = f.classList.contains('on'); apply(); });
  });
  function sinceCut(){
    var days = null; Object.keys(filters.since).forEach(function(k){ if (filters.since[k]) { var d = parseInt(k, 10); if (days === null || d > days) days = d; } });
    if (days === null) return null; var t = new Date(); t.setDate(t.getDate() - days); return t.toISOString().slice(0, 10);
  }
  // Chips are literal: a row shows only while its value is lit in every
  // group, so turning a whole group off empties the board (and says so)
  // instead of silently meaning "no filter". `since` is the one threshold.
  function has(kind, val){ return kind in filters && val in filters[kind] ? filters[kind][val] : true; }
  function apply(){
    var cut = sinceCut(), shown = 0;
    document.querySelectorAll('.mrow').forEach(function(r){
      var ok = has('owner', r.dataset.owner) && has('view', r.dataset.verdict) && has('author', r.dataset.author);
      var ds = r.dataset.domains.split(' ').filter(Boolean);
      if (ds.length && !ds.some(function(d){ return has('domain', d); })) ok = false;
      if (cut && r.dataset.created < cut) ok = false;
      r.hidden = !ok; if (ok) shown++;
    });
    document.querySelectorAll('.grp').forEach(function(g){ g.hidden = !g.querySelector('.mrow:not([hidden])'); });
    var empty = document.getElementById('empty'); if (empty) empty.hidden = shown > 0;
  }
  var reset = document.getElementById('reset-filters');
  if (reset) reset.addEventListener('click', function(){
    document.querySelectorAll('.fchip[data-filter]').forEach(function(f){
      var on = f.dataset.filter !== 'since';
      f.classList.toggle('on', on); filters[f.dataset.filter][f.dataset.value] = on;
    });
    apply();
  });
  // A decision is any lit decision button -- approve, send back, close,
  // route, unblock, refresh, re-run -- on any row on the page, blocked rows
  // included; a row a lit chain covers has had its decision made on the
  // lead's row. The denominator is every row that has a decision to make.
  function progress(){
    var el = document.getElementById('progress'); if (!el) return;
    var rows = [].slice.call(document.querySelectorAll('.mrow')).filter(function(r){
      return r.querySelector('button.btn[data-kind="decision"]');
    });
    var done = rows.filter(function(r){
      return r.querySelector('button.btn.sel[data-kind="decision"]') || r.querySelector('.claimnote');
    }).length;
    el.textContent = rows.length ? done + ' of ' + rows.length + ' decisions made' : '';
  }
  apply(); settle();
})();
"""

# The page comes in two wrappings from one body: a standalone document
# (what render.py writes to disk and screenshot.mjs opens), and the
# fragment form the Artifact tool publishes — it supplies the document
# skeleton itself and wants only the title, styles and content.
FRAGMENT = """<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<style>{style}</style>
<div class="wrap">
<header class="mast"><div class="eyebrow">{eyebrow}</div><h1>{h1}</h1><p class="dek">{dek}</p></header>
{tally}
{filters}
{clusters}
{body}
</div>
{cmd}
<script type="application/json" id="queue">{payload}</script>
<script>{script}</script>
"""

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
""" + FRAGMENT.replace("<style>{style}</style>\n", "<style>{style}</style>\n</head>\n<body>\n") + """</body>
</html>
"""


# ---- CLI --------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--in", dest="inp", default=str(_REPO_ROOT / ".pr-review-queue.json"))
    ap.add_argument("--board", metavar="OUT.html", help="write the board page")
    ap.add_argument("--detail", type=int, metavar="N", help="write one PR's detail page (with --out)")
    ap.add_argument("--out", help="output path for --detail")
    ap.add_argument("--terminal", action="store_true", help="print the table to stdout")
    ap.add_argument("--artifact", action="store_true", help="emit the fragment form the Artifact tool wraps (no html/head/body)")
    ap.add_argument("--include-handed-off", action="store_true", help="show PRs waiting on another reviewer as full rows")
    ap.add_argument("--pr", type=int, help="with --terminal: one row")
    ap.add_argument("--self-test", action="store_true")
    return ap


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.self_test:
        import test_render  # noqa: PLC0415 — the pytest file doubles as the harness
        return test_render.run_standalone()
    queue = json.loads(Path(args.inp).read_text())
    did = False
    if args.board:
        Path(args.board).write_text(render_board(queue, artifact=args.artifact, include_handed_off=args.include_handed_off))
        print(f"board → {args.board}", file=sys.stderr)
        did = True
    if args.detail is not None:
        out = args.out or str(_REPO_ROOT / ".pr-review-board.html")
        Path(out).write_text(render_detail(queue, args.detail, artifact=args.artifact))
        print(f"detail #{args.detail} → {out}", file=sys.stderr)
        did = True
    if args.terminal or not did:
        sys.stdout.write(render_terminal(queue, args.pr, include_handed_off=args.include_handed_off))
    return 0


if __name__ == "__main__":
    sys.exit(main())
