---
user-invocable: false
description: How to read the /pr-review board — every element on the page, what it means, and what clicking it does
---

# Reading the board

The board is a **worksheet, not a control panel**. Nothing on the page talks to GitHub. Every button is a toggle that adds a fragment to the command at the bottom; when you are happy with that command you copy it, or ask Claude to run it. Until then you can click anything and change your mind. Claude does not wait at the page for that, though: it plans the command the board opened with — read-only, no GitHub calls — and comes back with the preview and one question, execute or not.

One run of `/pr-review` renders one board. Re-running re-renders it, and publishing updates the same page.

## The four verdicts

Every open PR you can act on gets exactly one verdict. They are a sort order, not a judgment of quality.

| Verdict | Means | The usual move |
|---|---|---|
| **stamp** | Passed every gate: current review, no open findings, green CI, no collisions, your lane, small enough. | Approve. Bot PRs merge; a person's PR is theirs to merge. |
| **judge** | One thing needs a person: an open finding, a stale-looking summary, a new blog post, a diff over your size cap. | Read the judgment boxes, then approve as-is or send it back. |
| **route** | Not your lane per `.github/review-routing.yml`. | Request review from the owning team, or approve anyway if you're confident. |
| **blocked** | Nothing you can do until something else moves: a conflict, red CI, a stale review, a review still running. | Use the unblock the row offers, or leave it. |

## The Do next strip

The top of the board is a short list of moves worth making, most leverage first. Each card is three things:

1. **A statement of fact**, naming the PRs. "#21664 and #21662 were opened by a workflow run, so no author will ever answer a review."
2. **What pressing the button does**, in one sentence. "Closes each with a comment carrying the judgments on those rows."
3. **The button**, which presses exactly those rows' buttons for you.

A card is a shortcut for clicking the same buttons down in the rows, not a separate instruction. Light a card and its rows light. Pick a different decision on one of those rows and the card goes out, because it no longer describes what you asked for. A card and a row can never disagree, so the command at the bottom can never contradict itself.

Two cards deserve a note:

- **Start the chain** is the two row buttons it presses: approve and squash-merge the first PR in a collision cluster, then merge master into the next one so it can follow. It is one link per run; the next link waits on CI, about ten minutes.
- **Consolidate** posts one changes-requested review asking a bot for a single PR instead of N overlapping sweeps, with a reason no row button carries. That one has no row equivalent, so it tags the rows it covers with "covered by Do next N" instead of lighting them; choosing anything else on a covered row puts the card out.

## A row

```
#21622  Fix stale fully-qualified /docs/ links in 6 blog posts        [judge]
diff ↗
edit ↗
        blog · +7 −7 · 6 files · CI ✓ · reviewed@50f87c3 ≠ head 95358f6 · @workprentice[bot]
        [link-only sweep: yours] [review:base-merged] [warnings:2:F6,F7]  ▸ why · 4
        One-line summary of what the PR does.
        <judgment boxes>
        [open PR] [send back to author] [screenshot the preview]   [approve as-is & merge]
```

- **The three links on the left** are the PR, its Files changed tab (the diff), and the PR in the VS Code web editor, which gives you a real editor over the branch.
- **The reviewer's guide fold** carries what the guide says beyond its findings: what the PR changes, what the review already verified so you needn't, and links to the guide, the author card and the evidence page.
- **The preview fold** lists every page this PR changes on its own deployed copy of the site, the same list pulumi-bot pins on the PR. One click to a rendered page, without a trip to GitHub. Because those links exist, the screenshot action only appears in the detail view (`/pr-review N`), where the images embed in the page.
- **The chips** are the reasons for the verdict. The ones that change what you would click stay visible; the rest fold behind **why · N**. Hover any chip for a sentence explaining it; the raw code is in the tooltip too, so the queue stays greppable.
- **The judgment boxes** are the open findings, each with the question that was decided, the reasoning, the diff lines, and a badge saying why it does not stop the merge. See below.
- **The buttons**: one decision per row (approve, send back, close it out, route, unblock, refresh, re-run). Picking a second decision puts the first out. Side actions (apply fixes, screenshot the preview, deploy to the test site) ride along with whichever decision is lit. The right-aligned coloured button is the recommended one.
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

## The command bar

The bottom of the page composes your decisions into one command:

```
$ /pr-review --act --stamp 21550,21577 --request-changes 21664 --route 21651:@pulumi/docs-blog-review
```

Copy it and run it, or hand it to Claude. `act.py` plans it, shows a preview of every write it will make, and waits for a yes before executing. Each approval runs its own preflight immediately before merging: head unchanged since the plan, mergeable, CI green, no changes-requested review. A PR that fails preflight is skipped and the rest of the batch continues.

## Waiting on others

A PR whose requested reviewer is a human who isn't you is waiting on them, not on you. Those rows collapse into a compact list at the bottom. `--include-handed-off` brings them back as full rows. Routing a PR is also how you say "don't show me this again": the review request lives on GitHub, so every future run sees it, and GitHub clears it when the reviewer acts.

## What is not on the board

- Anything that talks to GitHub. The page is inert.
- Anyone else's decisions. Judgments are written fresh each run and are not shared between approvers.
- Draft PRs, unless you asked for one by number.
