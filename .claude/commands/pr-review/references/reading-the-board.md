---
user-invocable: false
description: How to read the /pr-review board — every element on the page, what it means, and what clicking it does
---

# Reading the board

The board is a **worksheet, not a control panel**. Nothing on the page talks to GitHub. Every button is a toggle that adds a fragment to the command at the bottom; when you are happy with that command you copy it, or ask Claude to run it. Until then you can click anything and change your mind. Claude stops when the page is published and does nothing further until you hand a command back, so a board you never read can't approve anything.

One run of `/pr-review` renders one board. Re-running re-renders it, and publishing updates the same page.

## The four verdicts

Every open PR you can act on gets exactly one verdict. It says what kind of move the row needs, not how good the PR is — and it is *not* the row order: rows sit in PR number order inside their owner/domain group, so a number you already have finds its row without your having to guess its verdict first. The verdict is on the row, in the tally and on a filter chip.

| Verdict | Means | The usual move |
|---|---|---|
| **stamp** | Passed every gate: current review, no open findings, green CI, no collisions, your lane, small enough. | Approve. Bot PRs merge; a person's PR is theirs to merge. |
| **judge** | One thing needs a person: an open finding, a stale-looking summary, a new blog post, a diff over your size cap. | Read the judgment boxes, then approve as-is or send it back. |
| **route** | Not your lane per `.github/review-routing.yml`. | Request review from the owning team, or approve anyway if you're confident. |
| **blocked** | Nothing you can do until something else moves: an unanswered 🚨 finding, a conflict, red CI, a stale, errored or **unreadable** review (one that didn't arrive whole — see below), a review still running, someone else's changes requested, or your own PR. | Use the unblock the row offers (merge base, refresh, re-run the review, re-run the failed checks, send back or close for open findings, route), or leave it. A row with no unblock says **Blocked: … no action available** and is counted on its own tally tile, so it can never sit silent. |

## No batch strip

Every decision is on its row, next to the evidence for it. The board used to open with a "Do next" strip — one card per batch (approve the set, send back, route, each unblock) naming PRs as text, plus the chain and the consolidation, which had no row button at all. Every card was the row buttons it named, pressed together, and it sat where you could not see the rows it was talking about; judging a batch meant scrolling down to find each row and back up to the card. It is gone. What it did is covered without it:

- **Approve the set** was the stampable rows, which arrive with their approve button already selected — the default command merges them whether or not a strip says so.
- **Send back / close / route / re-run** batches were each row's own button, pressed for several rows at once. Press them on the rows.
- **Start the chain** and **consolidate** were the two moves with no row button. They are row buttons now: see "Cluster moves" under "A row".

The tally and the progress line stay at the top, because they are read-only: neither asks you to decide anything about a PR you are not looking at. (`--terminal` still prints the batch list after its table, as `$ /pr-review --act …` commands, because a terminal has no buttons to press.)

## A row

```
#21622  Fix stale fully-qualified /docs/ links in 6 blog posts        [judge]
diff ↗
edit ↗
        blog · +7 −7 · 6 files · CI ✓ · reviewed@50f87c3 ≠ head 95358f6 · @workprentice[bot] 12d
        [link-only sweep: yours] [review:base-merged] [warnings:2:F6,F7]  ▸ why · 4
        One-line summary of what the PR does.
        <judgment boxes>
        [open PR] [send back to author] [screenshot the preview]   [approve as-is & merge]
```

- **The three links on the left** are the PR, its Files changed tab (the diff), and the PR in the VS Code web editor, which gives you a real editor over the branch.
- **The reviewer's guide fold** carries what the guide says beyond its findings: what the PR changes, what the review already verified so you needn't, and links to the guide, the author card and the evidence page.
- **The preview fold** lists every page this PR changes on its own deployed copy of the site, the same list pulumi-bot pins on the PR. One click to a rendered page, without a trip to GitHub. Because those links exist, the screenshot action only appears in the detail view (`/pr-review N`), where the images embed in the page.
- **The age** is the last thing on the meta line: how long the PR has been open, in at most four characters (`today`, `12d`, `4mo`), and amber once it passes 30 days. It is there because it is the one fact a row cannot show you any other way — two identical sweeps read the same until you notice one has been sitting since June. Hover it for the exact date.
- **The chips** are the reasons for the verdict. The ones that change what you would click stay visible; the rest fold behind **why · N**. Hover any chip for a sentence explaining it; the raw code is in the tooltip too, so the queue stays greppable.
- **The judgment boxes** are the open findings, each with the question that was decided, the reasoning, the diff lines, and a badge saying why it does not stop the merge. See below.
- **The buttons**: one decision per row (approve, send back, close it out, route, unblock, refresh, re-run the review, re-run the failed checks, start the chain, ask for a consolidated PR). Picking a second decision puts the first out. Side actions (apply fixes, screenshot the preview, deploy to the test site) ride along with whichever decision is lit. The right-aligned coloured button is the recommended one.
- **Cluster moves** sit on the row they belong to. **approve & merge, then unblock #N** is on the lead of a collision chain: `--chain C1` approves and squash-merges the lead through the same gates as a stamp (approval alone on a person's PR: "approve, then unblock #N"), then merges master into #N so it can follow — one link per run, and the next waits on CI. It is only offered where the collision is the *only* thing holding the lead back, because `--chain` approves that lead with `--force`; a lead with anything else against it (an open ⚠️ row, a judged 🚨, a stale review, a new blog post, a diff over your size cap) just keeps its approve-as-is button, next to the findings, and that is a call to make on the row. While the chain is lit, #N's row reads **✓ covered by the chain from #lead** and counts as decided; pick anything on #N and the chain goes out, so the command can never carry both. **ask … for one consolidated PR** is on the newest of a bot author's overlapping sweeps: it posts one changes-requested review asking for a single PR instead of N serial merges, and nothing merges.
- **fix it yourself** is the amber dashed button on a PR a workflow opened that still has open findings. See "Fixing one yourself" below.
- **Your own PR** wears a **your own PR** chip (`author:self`) and no approve or send-back button, because you cannot answer your own review or approve your own work from here: route it, and answer its findings with `/address-review`.
- **Approving says whether it merges.** A bot row leads with "approve & merge"; a person's row leads with "approve, no merge", because merging their PR is their call. The other choice is the second button.

## Judgment badges

A badge beside a finding says **why that finding does not stop the merge**. It is never something the PR's author answered — the author has not answered anything on this board.

| Badge | Means | Approving the row does |
|---|---|---|
| already fixed | The diff already addresses it. | Records it as fixed. |
| not a real issue | The review got this one wrong. | Posts `/resolve F<n> refuted` with the reason shown. |
| fair, not blocking | Real, but not worth holding the PR. | Posts `/resolve F<n> accepted` with the reason. |
| doesn't apply | Out of scope for this PR. | Posts `/resolve F<n> not-applicable` with the reason. |
| needs the author | Not yours to fix. | Nothing — use send back, which puts it to the author. |
| no author to ask | Wants a change, but a workflow opened the PR, so a send-back goes unread. | Nothing — fix the branch yourself, ask Claude on the PR, or close it out and let the lane re-queue the page. |

Approving a judged row posts those `/resolve` comments **before** it approves, so the review's own state records why each finding closed rather than the merge walking over them.

Before the judge step has run, a finding wears the same shape with a different badge — where it *stands*, not what was decided:

| Badge | Means |
|---|---|
| probably not real | A checker flagged it; the review looked and thinks it does not hold. Your call, but it is not asking for a fix. |
| worth a look | A checker flagged it and the review kept it deliberately: it wants a person to look before the merge. |
| nobody has ruled | A checker raised it and the review took no position. Yours to weigh. |

Each one leads with the claim, carries one sentence of the review's reasoning and the diff lines it is about, and folds the review's full note behind **the review's full note**.

## Yours versus everyone's

A chip with a dotted border and a small **·cfg** mark is on the row because of *your* `~/.pr-review.yml`, not because of the PR. Every other chip is a fact about the PR and reads the same for every approver.

Three settings put chips on a row:

| Setting | Chip | What it does |
|---|---|---|
| `link_fixes: mine` (the default) | **link-only sweep: yours** | Pulls a link-only diff into your lane whatever lane it belongs to, because a lane owner's review buys nothing on a link swap. With `link_fixes: route` the row goes to its lane owner instead. |
| `stamp_max_lines` | `size:<n>>=<cap>` | A diff at or over the cap is read rather than stamped. |
| `stale_date_days` | `blog:stale-date:<date>` | A blog post dated further back than the window looks stale to publish now. |

`shape:link-only` is *not* one of them. It is a fact about the diff — every changed line is the same sentence with only a link rewritten — and it is true for everyone.

A link sweep still needs a human: the Sentinel's mechanical bar counts any modified link as substantive, so somebody has to approve it. What it does not need is a *particular* lane's human. `link_only: { approval: any-team }` in `.github/review-routing.yml` says any team in the matrix satisfies the approver gate for one, because the question a link sweep raises — does the new target resolve, and does it still say what the sentence claims — is careful reading rather than lane knowledge. Those rows carry `gate:any-team` and are everyone's, with the merge gate agreeing. Set `approval: lane` and the ordinary per-subject rule returns, at which point `link_fixes: mine` is what pulls a sweep into your lane.

## Filter chips

Filters are literal: **a row shows only while its value is lit in every group.** Turning a whole group off empties the board and the board says so, rather than silently meaning "no filter". `since` is the one threshold rather than a set of values. "Reset chips" restores the defaults.

Every verdict starts lit, including **stampable** and **blocked**. That is deliberate: the stampable rows arrive with their approve-and-merge button already selected, so the command at the bottom acts on them whether or not you scroll past them — hiding them by default would mean the default command merges PRs the page never showed you. Turn either group off when you want a shorter board; the counts on the chips say what you just put away.

The lever at the end of the bar is not a filter. It opens or closes every folded panel on the board at once (the manual keeps its own state), and each row carries the same lever for itself alone beside its PR links.

## The progress line

"3 of 21 decisions made", under the tally. A decision is a lit decision button on any row on the page — approve (either way), send back, close it out, route, unblock, refresh, re-run the review, re-run the failed checks, start the chain, ask for a consolidated PR — or a lit chain covering the row from its lead. Side actions (apply fixes, screenshot, deploy) never count. The denominator is every row that has a decision to make, blocked rows included; rows parked in the waiting lists are not on the page and are not counted.

## A review that didn't arrive whole

A long review is split across several comments. Its findings sections are the tail of the document, so when the collector could only read part of it, what is missing is exactly where the 🚨 rows live — and a row that looks findings-free for that reason is the most dangerous row on the board, because "no findings" is the shape of an approvable PR.

Two things say a review is incomplete, and either one blocks the row with `review:unreadable`:

- **A missing page.** The `k/N` markers promise N comments and GitHub returned fewer.
- **A tally that outruns the sections.** The card's own count table says three 🚨 and its sections parsed into none. The table and the sections are written by the same pass, so a disagreement means the body is truncated, whatever truncated it.

The unblock is **re-run the review** — a fresh one, not a refresh. `act.py` refuses the merge on its own account too: the preflight re-reads the review and will not merge over one it cannot see whole, whatever the board said.

Softer and not a blocker: **`review:parse-confidence:low`** on a row whose review parsed into no findings with nothing corroborating that (a v2 card with no tally table, a v3 card with no head sentinel or a broken `REVIEW_STATE`). Nothing says there *are* findings, so the row stays judgeable — but it is never stampable, and the honest move is to read the comment itself.

## Fixing one yourself

pulumi-bot's content-review and glow-up lanes open their PRs from a workflow run. Nobody reads a changes-requested review there, and closing one only makes the lane re-queue the same page on its next run — so a bot PR stuck on open findings used to offer exactly one button, "close it out", which fixes nothing.

Those rows carry **fix it yourself**. It is not a write and not part of the batch: it composes `/address-review N` onto a second, amber line above the `--act` command — one run per PR, because each is its own interactive session that walks the open findings with you and pushes the fixes to the branch. Light several and you get several lines; the `--act` command below is untouched either way, and the page still writes nothing.

It appears wherever the fix would survive: a `pulumi-bot` content-review or glow-up branch, or any other workflow-authored PR `act.py` is allowed to push to. It does **not** appear on dependabot PRs or the generated-docs regens (`automation/merge`), which are rebuilt from source — fix the generator — nor on a fork head, where there is no push access.

## The command bar

The bottom of the page composes your decisions into one command:

```
$ /pr-review --act --stamp 21550,21577:no-merge --force --request-changes 21664 --reason "21664=…" --route 21651:@pulumi/docs-blog-review
```

It is read off the lit buttons every time one changes, so it can never lag a click. Every approve button folds into the one `--stamp` list — `N`, `N:merge` or `N:no-merge` per PR, `--force` said once for the batch if any of them needs it — because `act.py` reads a flag once, and a second `--stamp` would be a second flag. A `--reason` that a card or button carries is scoped to its PR before it reaches the bar, as `--reason "N=text"`, so a batch can carry several. The same fragment is never repeated.

Copy it and run it, or hand it to Claude. Invoking it *is* the yes: `act.py` plans it, prints a preview of every write with its exact body, and executes — the reading you did on this page is what the command carries, so nothing asks you to confirm it a second time. (`--dry-run` runs the preflights and lists every write it would make without sending one, if you want to look first; it never runs git.) Every write is preceded by a re-read of the PR (still open, head unchanged since the plan); an approval also checks mergeable, CI green, and no changes-requested review from anyone but you — your own is superseded by the approval it posts. A PR that fails preflight is skipped and the rest of the batch continues.

## Waiting on others

A PR whose requested reviewer is a human who isn't you is waiting on them, not on you. Those rows collapse into a compact list at the bottom. `--include-handed-off` brings them back as full rows. Routing a PR is also how you say "don't show me this again": the review request lives on GitHub, so every future run sees it, and GitHub clears it when the reviewer acts.

## Waiting on the author

A PR you already sent back — your changes-requested review is the latest word, and nothing has been pushed since — is waiting on its author, not on you. Those rows wear `sent-back:<date>` and collapse into a second compact list under the first: the PR, its title, the author and the date you asked, the age, and a ✗ for red CI or a ⚠ for a conflict. Your own changes-requested review is never a blocker: the approval you would post supersedes it. The row returns to the groups when a commit lands; `--include-handed-off` brings it back now if you need to act on it.

## What is not on the board

- Anything that talks to GitHub. The page is inert.
- Anyone else's decisions. Judgments are written fresh each run and are not shared between approvers.
- Draft PRs, unless you asked for one by number.
