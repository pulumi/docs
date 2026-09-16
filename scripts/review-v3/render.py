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
BUCKET_LABEL = {
    "outstanding": "🚨 Outstanding", "author-answer": "❓ Author answer", "reviewer-check": "⚠️ Reviewer check",
    "low": "⚠️ Low-confidence", "style": "✏️ Style", "pre-existing": "💡 Pre-existing", "preexisting": "💡 Pre-existing",
}
HIDDEN_REASON_PREFIXES = ("owner:", "label:")  # rendered elsewhere on the row
# Chips that change what you'd click stay visible; the rest fold behind "why".
PRIMARY_CODES = ("warnings", "outstanding", "self-accepted", "cluster", "directional", "duplicate", "mergeable", "checks",
                 "review", "scrutiny", "blog", "handed-off", "draft", "route", "merging-over", "link-fixes", "gate")
# A reason code is a vocabulary, not a sentence. These few decide whether a
# row is on your board at all, so they read as words; the code stays in the
# chip's title for anyone grepping the queue.
CHIP_LABEL = {
    "gate:none": "no team approval needed",
    "link-fixes:mine": "link-only sweep: yours",
    "route:no-team": "team missing, routing to a person",
    "route:team-unverified": "team not verifiable from here",
}
ACTION_CLASS = {"stamp": "go", "stamp-merge": "go", "stamp-no-merge": "go", "request-changes": "hold", "route": "route", "unblock": "stop", "refresh": "stop", "rerun": "stop", "close": "stop",
                "fix": "", "render": "", "deploy": ""}
INCLUDE_HANDED_OFF = False  # render.py --include-handed-off flips this
# A row takes one decision (what happens to the PR) and any number of side
# actions (things done on the way). The board's toggles enforce that: lighting
# a second decision on a row puts out the first.
SIDE_ACTIONS = {"fix", "render", "deploy"}


def action_kind(pr: dict, action: dict) -> str:
    """`rerun` is the unblock on an errored review (a decision) and an extra
    on a row where no review ran (a side action beside approve/route)."""
    if action["id"] == "rerun":
        return "decision" if "review:error" in (pr.get("blockers") or []) else "side"
    return "side" if action["id"] in SIDE_ACTIONS else "decision"


def esc(v) -> str:
    """html.escape every value that reaches the page, in exactly one place."""
    if v is None:
        return ""
    return html.escape(str(v), quote=True)


# ---- pieces --------------------------------------------------------------------


def pr_url(queue: dict, n: int) -> str:
    return f"https://github.com/{queue.get('repo') or 'pulumi/docs'}/pull/{n}"


def files_url(queue: dict, n: int) -> str:
    return pr_url(queue, n) + "/files"


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
    "link-only": "Every changed line is the same sentence with only a link rewritten. Nothing else moved.",
}
AUTHOR_HELP = {
    "internal": "Opened by a Pulumi org member.",
    "external": "Opened by someone outside the org, so it gets the external-contributor treatment.",
    "generated": "Opened by a workflow run, not a person. Nobody will ever read a review on it, so it closes rather than going back.",
}
ROUTE_STATE_HELP = {
    "no-team": "GitHub has no team by the name the routing config gives this lane, so the review request goes to that role's SLA person instead.",
    "team-unverified": "This token cannot read the org's teams, so the team named in the routing config is used without checking it exists.",
}
SIMPLE_HELP = {
    "scrutiny:heightened": "The diff looks AI-written, so this row can never be a plain stamp however clean it looks.",
    "stances:present": "The review recorded editorial judgement calls it made. They only block with --strict-stances.",
    "gate:none": "The routing matrix asks for no team approval on a change like this, so nobody is waiting to review it and the row is yours to take.",
    "link-fixes:mine": "A link-only diff. Your config says those are yours to approve whatever lane they belong to, since a lane owner's review buys nothing on a link swap.",
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
            text = REVIEW_HELP.get(detail)
        elif code == "mergeable":
            text = MERGEABLE_HELP.get(detail)
        elif code == "checks":
            text = CHECKS_HELP.get(detail)
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
            text = f"The post is dated {detail.partition(':')[2]}, old enough that publishing it now would look stale."
        elif code == "brief":
            text = (f"The review's summary says \"{detail.partition(':')[2]}\", which appears nowhere in the diff, so the "
                    "summary may describe an earlier push.")
        elif code == "desc" and first == "stale":
            text = f"The PR description names `{detail.split(':')[-1]}`, which this diff does not touch."
        elif code == "size":
            text = f"The diff is {detail.replace('>=', ' lines against your stamp cap of ')}, so it gets read rather than stamped."
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
        elif code == "gate":
            text = SIMPLE_HELP["gate:none"]
    return f"{text} ({r})" if text else r


def _chip(r: str) -> str:
    code = r.split(":", 1)[0]
    cls = f"chip r-{esc(code)}" + (" theirs" if r.endswith(":theirs") else "")
    text = CHIP_LABEL.get(r) or (r if len(r) <= 48 else r[:45] + "…")
    return f'<span class="{cls}" title="{esc(chip_title(r))}">{esc(text)}</span>'


def chips(reasons: list[str]) -> str:
    """Two tiers: actionable chips inline, informational ones behind a
    "why" fold so a row reads as a decision, not a wall of tags."""
    primary, info = [], []
    for r in reasons:
        if r.startswith(HIDDEN_REASON_PREFIXES):
            continue
        code = r.split(":", 1)[0]
        (primary if code in PRIMARY_CODES and not (code == "merging-over" and ":approved-by:" in r) else info).append(r)
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
    "close": "Close this PR with a comment carrying the row's findings. A workflow opened it, so the lane re-queues the page on its next run.",
    "route": "Request a review from the lane's owner and post what the queue flagged as a comment. Nothing merges, and the row moves to 'waiting on others'.",
    "unblock": "Merge master into this branch as a merge commit and push, so it stops conflicting. A conflicted merge is aborted and reported, never resolved blind.",
    "refresh": "Ask the existing review to update itself against the current head (@claude #update-review).",
    "rerun": "Throw the current review away and run a fresh one from scratch (@claude #new-review).",
    "fix": "Apply the drafted description correction and any one-click suggestions, then commit and push.",
    "render": "Screenshot this PR's preview pages into .pr-review-shots/ so you can look at them.",
    "deploy": "Dispatch the testing deploy workflow for this branch, to pulumi-test.io.",
    "chain": "Approve and merge the first PR of this collision cluster, then merge master into the next so it can follow.",
    "consolidate": "Ask the bot for one consolidated PR instead of this pile of overlapping sweeps. Nothing merges.",
}


def action_help(pr: dict, action: dict) -> str:
    """What this button does to this PR, in a sentence. A stamp says whether
    it merges, because that is the part a label can only hint at."""
    base = ACTION_HELP.get(action.get("id"), "")
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
            extra = esc(" → " + act["cmd"].split(":", 1)[1])
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
    return "".join(f"<span>{esc(p)}</span>" for p in parts)


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
DEFERRED_NO_AUTHOR = ("hold", "nobody to fix it",
                      "This needs an author and a workflow opened the PR. Use the row's close button; the lane re-queues the page.")


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
                    + ("&ldquo;needs the author&rdquo;" if sends_back else "&ldquo;nobody to fix it&rdquo;")
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
    rows = []
    for i in items[:8]:
        link = deep_link(queue, pr, i)
        loc = f'<a href="{esc(link)}">{esc(i.get("file") or "")} {esc(i.get("anchor") or "")}</a>' if link else esc(i.get("anchor") or "")
        quote = patch_quote(pr, i.get("file"), i.get("anchor"))
        rows.append(f'<li><b>{esc(i.get("id"))}</b> <span class="v v-dim">{esc(BUCKET_LABEL.get(i.get("bucket"), i.get("bucket")))}</span> '
                    f'{esc(i.get("summary") or i.get("text") or "")} {loc}'
                    + (diffq(quote) if quote else "") + "</li>")
    if len(items) > 8:
        rows.append(f"<li>… {len(items) - 8} more on the PR</li>")
    why = [r for r in pr.get("reasons") or [] if r.split(":")[0] in ("warnings", "outstanding", "self-accepted", "size", "blog", "directional", "duplicate", "collision", "desc", "brief", "scrutiny", "shape", "mergeable", "checks", "review", "merging-over")]
    return ('<div class="jbox pending"><div class="q">Open findings, not yet judged' + (": " + esc(", ".join(why[:4])) if why else "") + "</div>"
            + ("<ul>" + "".join(rows) + "</ul>" if rows else "")
            + '<p class="jfoot">Nobody has decided these yet. Run the judge step (a full <code>/pr-review</code>) '
              "to get a recommendation and a reason for each, or open the PR and read them there.</p>"
            + "</div>")


def action_bar(pr: dict, queue: dict) -> str:
    actions = list(pr.get("actions") or [])
    # The primary is what the judge recommended when it recommended an
    # action, else the row's first action. It renders last, right-aligned,
    # colored by what it does; everything else stays grey on the left.
    rec = pr.get("recommended")
    primary = next((a for a in actions if a["id"] == rec), None) or (actions[0] if actions else None)
    btns = [f'<a class="btn" href="{esc(pr_url(queue, pr["number"]))}" title="Open this pull request on GitHub, in a new tab.">open PR</a>']
    for a in actions:
        if a is primary:
            continue
        btns.append(f'<button class="btn" data-cmd="{esc(a["cmd"])}" data-pr="{pr["number"]}" data-kind="{action_kind(pr, a)}" '
                    f'title="{esc(action_help(pr, a))}" aria-pressed="false">{esc(a["label"])}</button>')
    if primary:
        # A stamp row starts with its stamp selected: the composed command
        # merges the whole stamp set unless the approver deselects one.
        selected = " sel" if (primary["id"] == "stamp" and pr.get("verdict") == "stamp") else ""
        btns.append(f'<button class="btn p p-{esc(ACTION_CLASS.get(primary["id"], ""))}{selected}" data-cmd="{esc(primary["cmd"])}" data-pr="{pr["number"]}" '
                    f'data-kind="{action_kind(pr, primary)}" data-decision="{"1" if pr.get("verdict") in ("judge", "route") else "0"}" '
                    f'title="{esc(action_help(pr, primary))}" aria-pressed="{"true" if selected else "false"}">{esc(primary["label"])}</button>')
    return '<div class="acts">' + "".join(btns) + "</div>"


def row_html(queue: dict, pr: dict, *, expanded: bool = False) -> str:
    n = pr["number"]
    v = pr.get("verdict") or "judge"
    author = (pr.get("author") or {}).get("norm") or ""
    created = (pr.get("created_at") or "")[:10]
    body = [
        f'<div class="mrow {VERDICT_CLASS.get(v, "hold")}" data-pr="{n}" data-verdict="{esc(v)}" data-owner="{esc(owner_label(pr))}" '
        f'data-domains="{esc(" ".join(pr.get("domains") or []))}" data-author="{esc(author)}" data-created="{esc(created)}" '
        f'data-mine="{"1" if pr.get("is_mine", True) else "0"}">',
        f'<a class="pr" href="{esc(pr_url(queue, n))}">#{n}</a>',
        "<div>",
        f'<h4>{esc(pr.get("title"))} {verdict_chip(pr)}</h4>',
        f'<div class="meta">{meta_line(pr)}</div>',
        f'<div class="chips">{chips(pr.get("reasons") or [])}</div>',
        f'<p class="sum">{esc(pr.get("summary") or "")}</p>' if pr.get("summary") else "",
    ]
    if v in ("judge",) or pr.get("judgments") or expanded:
        body.append(judgment_boxes(queue, pr))
    if v == "blocked":
        body.append(f'<div class="jbox stop"><div class="q">Blocked: {esc(", ".join(pr.get("blockers") or []))}</div></div>')
    body.append(action_bar(pr, queue))
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
    cross = [r for r in pr.get("reasons") or [] if r.split(":")[0] in ("collision", "directional", "duplicate")]
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
    return (f'<section class="clusters"><details><summary><h2>Collisions · {len(cl)} cluster{"s" if len(cl) != 1 else ""}'
            f'{" · " + str(len(by_path)) + " directional" if by_path else ""}</h2><span class="note">the files, the pairs, the merge orders</span></summary>'
            '<div class="two">' + "".join(all_cards) + "</div></details></section>")


HELP_SECTIONS = [
    ("What this page is", [
        "A worksheet, not a control panel. Nothing here talks to GitHub.",
        "Every button is a toggle that adds a fragment to the command at the bottom. Click freely and change your mind; nothing happens until you run that command.",
    ]),
    ("The four verdicts", [
        "<b>stamp</b> — passed every gate: current review, no open findings, green CI, no collisions, your lane, small enough.",
        "<b>judge</b> — one thing needs a person: an open finding, a new blog post, a diff over your size cap.",
        "<b>route</b> — not your lane per the routing matrix. Ask the owning team, or approve anyway.",
        "<b>blocked</b> — nothing to do until something else moves: a conflict, red CI, a stale or running review.",
    ]),
    ("Do next", [
        "Each card states a fact naming its PRs, says what pressing the button does, and then presses those rows' buttons for you.",
        "A card is a shortcut for the rows, not a separate instruction: pick a different decision on one of its PRs and the card goes out, so the command can never contradict itself.",
        "<b>Start the chain</b> approves and merges the first PR of a collision cluster, then merges master into the next so it can follow. One link per run.",
    ]),
    ("A row", [
        "Chips are the reasons for the verdict; the ones that change what you'd click stay out, the rest fold behind <b>why</b>. Hover any chip for a sentence explaining it.",
        "One decision per row (approve, send back, close it out, route, unblock, refresh, re-run). Side actions like <i>apply fixes</i> ride along with it.",
        "The button says whether approving merges: a bot row leads with <i>approve &amp; merge</i>, a person's row with <i>approve, no merge</i>, because merging their PR is their call.",
    ]),
    ("Judgment badges", [
        "A badge says why a finding does not stop the merge. It is never the author's answer: nobody has answered anything here.",
        "<b>not a real issue</b>, <b>fair, not blocking</b> and <b>doesn't apply</b> are recorded on the PR as <code>/resolve</code> comments when you approve the row, before it merges.",
        "<b>needs the author</b> goes back with the send-back button; <b>nobody to fix it</b> means a workflow opened the PR, so close it out and the lane re-queues the page.",
    ]),
    ("Filters", [
        "Chips are literal: a row shows only while its value is lit in every group, so turning a whole group off empties the board and says so.",
        "<i>since</i> is the one threshold rather than a set of values. <i>Reset chips</i> restores the defaults.",
    ]),
    ("The command at the bottom", [
        "Copy it and run it, or hand it to Claude. It plans, previews every write, and waits for a yes.",
        "Each approval re-checks the PR immediately before merging: head unchanged, mergeable, CI green, no changes-requested review. A PR that fails is skipped and the batch continues.",
    ]),
]


def help_html() -> str:
    """The manual, folded, on the page it describes. Same content as
    `pr-review:references:reading-the-board`, kept short enough to read
    standing up."""
    out = []
    for heading, points in HELP_SECTIONS:
        out.append(f"<div><h4>{esc(heading)}</h4><ul>" + "".join(f"<li>{p}</li>" for p in points) + "</ul></div>")
    return ('<details class="help"><summary>How to read this board</summary>'
            '<div class="helpgrid">' + "".join(out) + "</div></details>")


def do_next_html(queue: dict) -> str:
    """The opening: one sentence and one button per move, most leverage
    first. Nothing else on the page competes with it for the first look."""
    cards = queue.get("do_next") or []
    if not cards:
        return ""
    out = []
    for i, d in enumerate(cards, 1):
        cls = ACTION_CLASS.get(d["kind"], "") or ("hold" if d["kind"] == "consolidate" else "route" if d["kind"] == "chain" else "")
        # `targets` are the row buttons this card presses; `claims` are rows it
        # covers without a row button of its own (a chain, a consolidation).
        data = ""
        if d.get("targets"):
            data += f' data-targets="{esc(json.dumps(d["targets"], sort_keys=True))}"'
        if d.get("claims"):
            data += f' data-claims="{esc(",".join(str(n) for n in d["claims"]))}"'
        tip = d.get("does") or ACTION_HELP.get(d["kind"], "")
        btn = (f'<button class="btn p p-{esc(cls)}" data-cmd="{esc(d["cmd"])}" data-pr="next{i}"{data} '
               f'title="{esc(tip)}" aria-pressed="false">{esc(d["label"])}</button>'
               if d.get("cmd") else "")
        does = f'<span class="does">{esc(d["does"])}</span>' if d.get("does") else ""
        out.append(f'<li class="next {esc(cls)}"><span class="n">{i}</span>'
                   f'<span class="say">{esc(d["say"])}{does}</span>{btn}</li>')
    return f'<section class="donext"><div class="sec-head"><h2>Do next</h2><span class="count">{len(cards)}</span></div><ol>' + "".join(out) + "</ol></section>"


def filter_bar(queue: dict) -> str:
    prs = queue.get("prs") or []
    owners = sorted({owner_label(p) for p in prs})
    domains = sorted({d for p in prs for d in p.get("domains") or []})
    authors = sorted({(p.get("author") or {}).get("norm") or "" for p in prs})
    counts = queue.get("counts") or {}

    GROUP_HELP = {"view": "verdict", "owner": "owner", "domain": "domain", "author": "author"}

    def chip(kind, val, label=None, on=True):
        if kind == "since":
            tip = f"Hide rows opened more than {val.rstrip('d')} days ago. This one is a threshold, not a set: the longest lit window wins."
        else:
            tip = (f"Lit: rows whose {GROUP_HELP.get(kind, kind)} is {val} are shown. Unlit: they are hidden. "
                   "A row shows only while its value is lit in every group, so turning a whole group off empties the board.")
        return (f'<button class="fchip{" on" if on else ""}" data-filter="{esc(kind)}" data-value="{esc(val)}" '
                f'title="{esc(tip)}">{esc(label or val)}</button>')

    parts = ['<div class="mock-bar">']
    parts += [chip("view", "judge", "needs a decision", on=True), chip("view", "route", "route", on=True),
              chip("view", "stamp", "stamp set", on=False), chip("view", "blocked", "blocked", on=False)]
    parts.append('<span class="sep"></span>')
    parts += [chip("owner", o, f"owner: {o}") for o in owners]
    parts.append('<span class="sep"></span>')
    parts += [chip("domain", d) for d in domains]
    parts.append('<span class="sep"></span>')
    parts += [chip("author", a, f"author: {a}") for a in authors]
    parts.append('<span class="sep"></span>')
    parts += [chip("since", s, f"since: {s}", on=False) for s in ("1d", "7d", "30d")]
    parts.append("</div>")
    parts.append('<p class="empty" id="empty" hidden>No rows match these chips. Every lit chip is a row you want to see; a group with nothing lit hides everything. <button class="btn" id="reset-filters" type="button">reset chips</button></p>')
    return "".join(parts)


def group_rows(prs: list[dict]) -> list[tuple[str, str, list[dict]]]:
    groups: dict[tuple[str, str], list[dict]] = {}
    for p in prs:
        key = (owner_label(p), ", ".join(p.get("domains") or []) or "other")
        groups.setdefault(key, []).append(p)
    order = lambda k: (0 if k[0] == "mine" else 1, k[0], k[1])  # noqa: E731
    return [(o, d, sorted(rows, key=lambda p: (VERDICT_ORDER.index(p.get("verdict") or "judge"), -p["number"])))
            for (o, d), rows in sorted(groups.items(), key=lambda kv: order(kv[0]))]


# ---- pages --------------------------------------------------------------------

PAYLOAD_DROP = {"patch", "author_body", "brief_body", "body", "triage_prose", "one_click_suggestions"}


def slim(obj):
    """The inlined copy of the queue minus the bulk (patches, comment
    bodies): what a viewer might copy out, not a second render source."""
    if isinstance(obj, dict):
        return {k: slim(v) for k, v in obj.items() if k not in PAYLOAD_DROP}
    if isinstance(obj, list):
        return [slim(x) for x in obj]
    return obj



def _age_days(pr: dict, now: datetime | None = None) -> int:
    try:
        created = datetime.fromisoformat((pr.get("created_at") or "").replace("Z", "+00:00"))
    except ValueError:
        return 0
    return max((now or datetime.now(timezone.utc)) - created, timedelta()).days


def waiting_html(prs: list[dict]) -> str:
    """The compact 'waiting on others' list: one line per handed-off PR,
    for awareness only. Nothing here is actionable by the approver."""
    rows = [p for p in prs if p.get("handed_off")]
    if not rows:
        return ""
    rows.sort(key=lambda p: (", ".join(p.get("handed_off_to") or []), -_age_days(p)))
    items = []
    for p in rows:
        who = esc(", ".join(p.get("handed_off_to") or []))
        title = p.get("title") or ""
        title = title if len(title) <= 72 else title[:69] + "…"
        state = (p.get("checks") or {}).get("state")
        flag = " ✗" if state == "red" else (" ⚠" if p.get("mergeable_state") == "dirty" else "")
        items.append(f'<li><a class="pr" href="{esc(pr_url({"repo": "pulumi/docs"}, p["number"]))}">#{p["number"]}</a> '
                     f'<span class="wt">{esc(title)}</span> <span class="who">{who}</span> <span class="age">{_age_days(p)}d{flag}</span></li>')
    return (f'<section class="waiting"><div class="sec-head"><h2>Waiting on others</h2><span class="count">{len(rows)}</span>'
            '<span class="note">requested reviewer isn\'t you · ✗ red CI · ⚠ conflict · hidden from the groups above; render with --include-handed-off to act on them</span></div>'
            '<ul>' + "".join(items) + "</ul></section>")


def render_board(queue: dict, *, artifact: bool = False, include_handed_off: bool = False) -> str:
    all_prs = queue.get("prs") or []
    prs = all_prs if include_handed_off else [p for p in all_prs if not p.get("handed_off")]
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
    payload = json.dumps(slim(queue), sort_keys=True).replace("</", "<\\/")
    return (FRAGMENT if artifact else PAGE).format(
        title="PR review queue",
        style=STYLE,
        eyebrow=esc(f"{queue.get('repo')} · queue · {queue.get('analyzed_at') or queue.get('generated_at')} · owner: {cfg.get('owner', 'me')} · me: {', '.join(cfg.get('me') or [])}"),
        h1="PR review queue",
        dek=esc(f"{len(prs)} open PRs sorted into stamp / judge / route / blocked. Stamp rows start selected; every button is a toggle that adds to the command at the bottom — the page never talks to GitHub. A badge beside a finding says why it does not stop the merge; the author has not answered anything here."),
        tally=f'<div class="tally">{tally}</div>' + help_html() + '<div class="progress" id="progress"></div>' + do_next_html(queue),
        filters=filter_bar({**queue, "prs": prs}),
        clusters="",
        body=("".join(sections) or '<p class="empty">Nothing to adjudicate.</p>') + clusters_html(queue) + ("" if include_handed_off else waiting_html(all_prs)),
        cmd=cmd_footer(),
        payload=payload,
        script=SCRIPT,
    )


def render_detail(queue: dict, n: int, *, artifact: bool = False) -> str:
    pr = next((p for p in queue.get("prs") or [] if p["number"] == n), None)
    if pr is None:
        raise SystemExit(f"#{n} is not in the queue (drafts and filtered rows are not collected)")
    payload = json.dumps(slim({**queue, "prs": [pr]}), sort_keys=True).replace("</", "<\\/")
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
    return ('<div class="cmdwrap"><div class="cmd" id="cmd">$ /pr-review --act</div>'
            '<button class="btn" id="copy">copy</button><button class="btn" id="clear">clear</button></div>')


def render_terminal(queue: dict, n: int | None = None, width: int = 110, include_handed_off: bool = False) -> str:
    all_prs = queue.get("prs") or []
    prs = all_prs if (include_handed_off or n is not None) else [p for p in all_prs if not p.get("handed_off")]
    if n is not None:
        prs = [p for p in prs if p["number"] == n]
    counts = queue.get("counts") or {}
    lines = [f"PR review queue · {queue.get('repo')} · {len(prs)} rows · " + " · ".join(f"{counts.get(v, 0)} {v}" for v in VERDICT_ORDER)
             + (f" · {counts['handed-off']} waiting on others" if counts.get("handed-off") else ""), ""]
    hdr = f"{'#':>6}  {'verdict':<8} {'owner':<11} {'domain':<14} {'size':>9} {'CI':<4} reasons"
    lines += [hdr, "-" * len(hdr)]
    for owner, domain, rows in group_rows(prs):
        for p in rows:
            reasons = [r for r in p.get("reasons") or [] if not r.startswith(HIDDEN_REASON_PREFIXES)]
            ci = {"green": "✓", "red": "✗", "pending": "…"}.get((p.get("checks") or {}).get("state"), "?")
            size = f"+{p.get('additions', 0)}/−{p.get('deletions', 0)}"
            line = f"{p['number']:>6}  {p.get('verdict'):<8} {owner[:11]:<11} {domain[:14]:<14} {size:>9} {ci:<4} " + " ".join(reasons)
            lines.append(line[:width] + ("…" if len(line) > width else ""))
    cl = queue.get("clusters") or []
    if cl:
        lines += ["", "collisions:"]
        for c in cl:
            lines.append(f"  {c['id']} {c['kind']}: merge " + " → ".join(f"#{x}" for x in c["merge_order"]))
    for d in queue.get("directional") or []:
        lines.append(f"  directional {d['path']}: #{d['adds_links_pr']} adds links, #{d['removes_links_pr']} removes them")
    judge = [p for p in prs if p.get("verdict") == "judge"]
    if judge:
        lines += ["", "judge rows (AskUserQuestion each in --terminal mode):"]
        for p in judge:
            lines.append(f"  #{p['number']} {p.get('title')}")
            for j in p.get("judgments") or []:
                lines.append(f"      {j.get('finding_id') or ''} {j.get('decision') or ''} → {j.get('disposition') or '?'} {j.get('deep_link') or ''}")
            for a in p.get("actions") or []:
                lines.append(f"      [{a['label']}]  {a['cmd']}")
    waiting = [p for p in all_prs if p.get("handed_off")] if not include_handed_off and n is None else []
    if waiting:
        lines += ["", f"waiting on others ({len(waiting)}):"]
        for p in waiting:
            lines.append(f"  #{p['number']} {(p.get('title') or '')[:60]:<60} {', '.join(p.get('handed_off_to') or [])} {_age_days(p)}d")
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
.fchip.on{background:var(--accent-soft);color:var(--accent);border-color:var(--accent)}
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
.mrow h4{font-size:14.5px;font-weight:600;margin:0 0 3px;line-height:1.35}
.meta{font-size:12.5px;color:var(--ink-3);margin-bottom:4px}.meta span{margin-right:10px}
.chips{display:flex;flex-wrap:wrap;gap:4px;margin:2px 0 6px}
.chip{font-size:10.5px;border:1px solid var(--line-2);border-radius:2px;padding:1px 6px;color:var(--ink-2);background:var(--surface-2);white-space:nowrap}
.chip.r-collision,.chip.r-directional,.chip.r-duplicate,.chip.r-self-accepted,.chip.r-checks,.chip.r-mergeable{border-color:var(--stop);color:var(--stop)}
.empty{margin:1rem 0;color:var(--ink-2);font-size:.95rem}.empty .btn{margin-left:.5rem}
.chip.r-warnings,.chip.r-outstanding,.chip.r-scrutiny,.chip.r-blog,.chip.r-size,.chip.r-shape,.chip.r-review{border-color:var(--hold);color:var(--hold)}
.chip.r-route{border-color:var(--route);color:var(--route)}
.chip.theirs{opacity:.55;border-style:dashed}
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
details.help>summary{cursor:pointer;padding:9px 14px;font-family:"IBM Plex Mono",monospace;font-size:12px;letter-spacing:.04em;color:var(--ink-2)}
details.help[open]>summary{border-bottom:1px solid var(--line)}
.helpgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px 24px;padding:12px 16px 16px}
.helpgrid h4{font-size:12.5px;text-transform:uppercase;letter-spacing:.07em;color:var(--ink-3);margin:0 0 4px}
.helpgrid ul{margin:0;padding-left:16px}
.helpgrid li{font-size:13px;color:var(--ink-2);margin:3px 0;line-height:1.45}
.donext{margin:6px 0 18px;background:var(--surface);border:1px solid var(--line-2);border-radius:4px;padding:12px 16px;box-shadow:var(--shadow)}
.donext ol{list-style:none;margin:8px 0 0;padding:0;display:grid;gap:8px}
.donext .next{display:flex;gap:12px;align-items:center;padding:8px 10px;border-left:3px solid var(--line-2);background:var(--surface-2);border-radius:3px}
.donext .next.hold{border-left-color:var(--hold)}.donext .next.route{border-left-color:var(--route)}.donext .next.go{border-left-color:var(--go)}.donext .next.stop{border-left-color:var(--stop)}
.donext .n{font-family:Archivo,sans-serif;font-weight:700;font-size:15px;color:var(--ink-3);width:18px}
.donext .say{flex:1;font-size:14px;color:var(--ink)}
.donext .does{display:block;font-size:12.5px;color:var(--ink-3);margin-top:2px}
.donext .btn.p{margin-left:auto;white-space:nowrap}
.clusters{margin-top:28px}.clusters summary{cursor:pointer;display:flex;gap:10px;align-items:baseline;flex-wrap:wrap}.clusters summary h2{display:inline}.clusters .note{font-size:12px;color:var(--ink-3)}
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
.diffq .del{color:var(--stop)}.diffq .add{color:var(--go)}
.btn{font-size:11.5px;font-weight:600;border:1px solid var(--line-2);border-radius:3px;padding:3px 9px;background:var(--surface);color:var(--ink-2);cursor:pointer;text-decoration:none}
.btn.p{background:var(--accent);color:#fff;border-color:var(--accent)}.btn.sel{outline:2px solid var(--go);outline-offset:1px}.btn.sel::before{content:"✓ "}
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
.cmdwrap{position:fixed;left:0;right:0;bottom:0;background:var(--ground);border-top:1px solid var(--line-2);padding:10px 16px calc(10px + env(safe-area-inset-bottom,0px));display:flex;gap:8px;align-items:center;z-index:3}
.wrap{padding-inline:16px}
.cmd{flex:1;background:var(--ink);color:var(--ground);border-radius:3px;padding:8px 12px;font-size:12.5px;overflow-x:auto;white-space:nowrap}
.empty{color:var(--ink-3)}
@media (max-width:600px){.mrow{grid-template-columns:1fr}.mrow>div:last-child{grid-column:1/-1}}
"""

SCRIPT = r"""
(function(){
  var sel = {};   // 'pr:cmd' -> cmd; one entry per selected button
  var cmdEl = document.getElementById('cmd');
  function compose(){
    var seen = {}, stamps = [], others = [];
    Object.keys(sel).sort().forEach(function(k){
      var c = sel[k]; if (!c || seen[c]) return; seen[c] = true;   // never the same fragment twice
      var m = c.match(/^--stamp (\d+)$/); if (m) stamps.push(m[1]); else others.push(c);
    });
    var out = '$ /pr-review --act';
    if (stamps.length) out += ' --stamp ' + stamps.join(',');
    if (others.length) out += ' ' + others.join(' ');
    cmdEl.textContent = out;
  }
  function setSel(b, on){
    var k = b.dataset.pr + ':' + b.dataset.cmd;
    if (on) { sel[k] = b.dataset.cmd; b.classList.add('sel'); } else { delete sel[k]; b.classList.remove('sel'); }
    b.setAttribute('aria-pressed', on ? 'true' : 'false');
  }
  // A Do-next card is the same decisions as the rows it names, pressed
  // together: `data-targets` maps a PR to the row button it presses, and
  // `data-claims` marks rows a card covers with no row button of its own (a
  // chain, a consolidation). Either way a card and a contrary row decision
  // can never both be lit, so the command at the bottom cannot contradict
  // itself.
  var cards = [].slice.call(document.querySelectorAll('button.btn[data-targets], button.btn[data-claims]'));
  function cardTargets(c){ return c.dataset.targets ? JSON.parse(c.dataset.targets) : {}; }
  function cardPrs(c){
    if (c.dataset.claims) return c.dataset.claims.split(',');
    return Object.keys(cardTargets(c));
  }
  function rowButton(pr, cmd){
    return document.querySelector('button.btn[data-pr="' + pr + '"][data-cmd="' + cmd.replace(/"/g, '\\"') + '"]');
  }
  function clearRow(pr, keep){
    document.querySelectorAll('button.btn.sel[data-kind="decision"][data-pr="' + pr + '"]').forEach(function(o){ if (o !== keep) setSel(o, false); });
  }
  function syncCards(){
    cards.forEach(function(c){
      var t = cardTargets(c), prs = Object.keys(t), lit;
      if (prs.length) {
        lit = prs.every(function(pr){ var b = rowButton(pr, t[pr]); return b && b.classList.contains('sel'); });
      } else {   // claims-only: any decision lit on a claimed row is a contradiction
        lit = c.classList.contains('sel') && !cardPrs(c).some(function(pr){
          return document.querySelector('button.btn.sel[data-kind="decision"][data-pr="' + pr + '"]');
        });
      }
      if (lit !== c.classList.contains('sel')) setSel(c, lit);
    });
  }
  document.querySelectorAll('button.btn[data-cmd]').forEach(function(b){
    if (b.classList.contains('sel')) setSel(b, true);
    b.addEventListener('click', function(){
      var on = !b.classList.contains('sel');
      var t = b.dataset.targets ? JSON.parse(b.dataset.targets) : null;
      if (t) {                                   // a batch card: press its rows
        Object.keys(t).forEach(function(pr){
          var row = rowButton(pr, t[pr]);
          if (!row) return;
          if (on) clearRow(pr, row);
          setSel(row, on);
        });
        setSel(b, on); compose(); syncCards(); return;
      }
      if (on && b.dataset.claims) {              // a chain: the rows it covers defer to it
        b.dataset.claims.split(',').forEach(function(pr){ clearRow(pr, null); });
      }
      if (on && b.dataset.kind === 'decision') {   // one decision per row; side actions ride along
        clearRow(b.dataset.pr, b);
      }
      setSel(b, on); compose(); syncCards();
    });
  });
  syncCards();
  document.getElementById('clear').addEventListener('click', function(){
    document.querySelectorAll('button.btn.sel').forEach(function(b){ setSel(b, false); }); compose(); syncCards();
  });
  document.getElementById('copy').addEventListener('click', function(){
    var t = cmdEl.textContent.replace(/^\$ /, '');
    if (navigator.clipboard) navigator.clipboard.writeText(t);
  });
  var filters = { owner: {}, domain: {}, verdict: {}, author: {}, since: {}, view: {} };
  document.querySelectorAll('.fchip').forEach(function(f){
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
    document.querySelectorAll('.fchip').forEach(function(f){
      var on = f.dataset.filter !== 'since' && !(f.dataset.filter === 'view' && (f.dataset.value === 'stamp' || f.dataset.value === 'blocked'));
      f.classList.toggle('on', on); filters[f.dataset.filter][f.dataset.value] = on;
    });
    apply();
  });
  function progress(){
    var el = document.getElementById('progress'); if (!el) return;
    var rows = document.querySelectorAll('.mrow[data-verdict="judge"], .mrow[data-verdict="route"]');
    var done = 0; rows.forEach(function(r){ if (r.querySelector('button.btn.sel[data-kind="decision"]')) done++; });
    el.textContent = rows.length ? done + ' of ' + rows.length + ' decisions made' : '';
  }
  document.querySelectorAll('button.btn[data-cmd]').forEach(function(b){ b.addEventListener('click', progress); });
  document.getElementById('clear').addEventListener('click', progress);
  apply(); progress(); compose();
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
