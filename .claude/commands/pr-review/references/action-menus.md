---
user-invocable: false
description: The row action bar per verdict, the terminal-mode menus, and which bot branches may be pushed to
---

# Row actions

Every row on the board carries an action bar; every button only adds an `act.py` fragment to the command at the bottom of the page. The bar is derived from the row's verdict and reason codes by `analyze.py`, so the board and `--terminal` offer the same choices.

## Action bar by verdict

| Verdict | Primary | Also offered |
|---|---|---|
| `stamp` | `--stamp N` (the button starts selected; on a bot row it approves and squash-merges, on a human-authored row it approves only) | `--stamp N:no-merge` ("approve, don't merge") on a bot row, `--stamp N:merge` ("approve & merge") on a human-authored one; `open PR` |
| `judge` | `--stamp N --force` (approve as-is, merging by the same rule) | the other merge choice (`--stamp N:no-merge --force` or `--stamp N:merge --force`); `--request-changes N` (send back to author: a changes-requested review built from the judgments, plus `needs-author-response`) — or, on an `author:generated` row, `--close N` ("close it out"), because a workflow never reads a review; `--fix N` when the row has a drafted description or one-click suggestions; `--render N` when it has preview pages; `--deploy N` on `risk:infra`; `--route N:@owner`; `open PR` |
| `route` | `--route N:@owner` (request review + post the defects) | `open PR`, `--stamp N --force` ("approve anyway": the lane is a default, not a lock) and its merge counterpart |
| `blocked` | the unblock: `--unblock N` (dirty or behind), `--refresh N` (stale review), `--rerun N` (errored **or unreadable** review — a page of a split review missing, or a tally that outruns the parsed sections), `--rerun-checks N` (red checks that look like flake), `--close N --superseded-by M` (duplicate) | for open 🚨 findings, `--request-changes N` (send back to author) or `--close N` on an `author:generated` row; `--route N:@owner` when the row is another lane's; **fix it yourself** on an `author:generated` row with open findings (below); `open PR`. A blocked row that ends up with no unblock at all shows "Blocked: … no action available" and is counted on its own tally tile |
| `author:self` (your own PR, any verdict) | `--route N:@owner` | `open PR`; never a stamp or a send-back — you answer its findings with `/address-review`, and someone else approves |

Approving a judged row answers its findings on the way past: one `/resolve F<n> <disposition>: <why>` comment per judged finding, posted before the approval, then the approval, then the merge. A `deferred` judgment is not resolved — it is what the send-back (or close) button is for.

Whether approving merges is on the button, never implied: bot PRs (dependabot, pulumi-bot, WorkPrentice) default to approve-and-merge, a person's PR defaults to approval alone because merging is the author's call. The second button is the other choice, and picking it puts the first one out. `act.py` reads the `:merge` / `:no-merge` suffix per PR, so a batch of both stays one command.

A blocked row is never stampable, with or without `--force`. An in-progress review and someone else's changes-requested review have no mechanical unblock; the row names the blocker and waits. Red checks offer `--rerun-checks N`, which re-runs the failed jobs of the head's workflow runs as the head is — for a flake, not for a diff that is actually red; a red commit status has no run to re-run, and the step says so. Your **own** changes-requested review is not a blocker at all: the row becomes `sent-back:<date>` and parks under "Waiting on the author" until a commit lands. An errored review's unblock is `--rerun N` (`@claude #new-review`), and a row where no review ran at all (`review:trivial`, a draft, a bot skip) offers the same command as a side action, "run a full review".

## Do next

The board opens with at most a handful of cards, each one sentence and one button, most leverage first: a cluster's recommendation (**consolidate** → `--request-changes <newest> --reason "<newest>=…"`; **chain** → `--chain C1`, a card with no row button: it covers both links, and a decision on either puts it out), then the batches (`--request-changes` for every row the judge sent back, `--close` for the generated rows that have no author to send anything back to, `--route` per owner, `--stamp` for the stampable rows — the card says how many of the set actually merge), then one card per mechanical unblock over the blocked rows (`--unblock`, `--refresh`, `--rerun`, `--rerun-checks`), so the opening says what is stuck and how many without unhiding every blocked row. A same-file cluster or one that is mostly waiting on others gets no card; its detail stays in the folded "Collisions" section at the bottom.

Three rules hold over every card:

- **No approval the person has not read.** `--stamp` names only rows whose verdict is `stamp` — every gate cleared mechanically, nothing judged. The chain card is the one that has to work for it: every overlapping cluster member is a `judge` row, because the overlap is itself a gate, so the card reads `analyze.only_collisions_hold()` — every recorded `gate_fails` entry is a `cluster:` / `directional:` / `duplicate:` code — and offers `--chain` only then. A lead held up by anything else gets a card that names the hold (`"#21622 leads the chain, but it needs a call of its own first (warnings:2:F6,F7)"`) and no button, since `--chain` approves that lead with `--force`.
- **No row the board does not render.** Cards are built from the same set `render_board` groups (not handed off, not waiting on its author), so `rowButton()` always finds the button a card would press. A card naming a parked row lights on click and goes straight back out.
- **A card is out, partly lit, or lit.** The button carries an `on/total` tally of the rows still holding its decision, and paints the middle state dashed and amber. Pressing a partial card takes every row back.

## Terminal mode

`--terminal` prints the table — every row with its reasons wrapped rather than cut, its blockers (`blocked: …`, with `(no action available)` when nothing unblocks it), its open findings (`open: F<n> …`) or judgments (`judged: …`), and every action as `[label]  --fragment` — then the Do-next moves with their `$ /pr-review --act …` commands, the collision clusters (members listed with "(all waiting on others)" when analyze has stripped every member from the merge order), the directional conflicts, and both waiting lists. Then, for judge rows only, one AskUserQuestion per row:

1. **Approve as-is** (`--stamp N --force`) — recommended when the judgment box's disposition is `accepted` / `not-applicable` / `refuted` and nothing else is open.
2. **Send back to author** (`--request-changes N`) — when a finding is the author's to fix: the judgments become the review body, line-anchored, in the voice `message-templates.md` sets for that author type.
3. **Route to owner** (`--route N:@owner`) — when the call belongs to the lane's team.
4. **Skip** — leave the row for later.

In board mode the page composes the command itself, so there is no per-row walk. In either mode these options set a row's disposition and compose a command; none of them runs it. There is no batch execute confirmation anywhere in this skill — a set of writes is authorized by the `--act` command the person invokes, never by a menu. A single row is the one place a question may carry its own action, and then only on the terms in the skill's "How a run ends": not the default option, labelled with the action and its reach ("Approve and squash-merge #21622", not "Proceed"), and only for a row the person has actually just read.

## Bot PRs: what may be pushed

The old rule was "no changes on bot PRs". It applies only where a push would be thrown away:

- **Dependabot** — never push. The PR is regenerated on the next run; edits break the update.
- **Generated-docs regens** (`pulumi-bot` with the `automation/merge` label) — never push. Regenerated from source; fix the generator.
- **`workprentice[bot]`** and **`content-review/*`** branches (pulumi-bot's content-review and glow-up PRs) — pushes are allowed: `--fix`, `--unblock`, and a hand fix all land as ordinary commits or **merge commits**. Never rebase, never force-push: the pipelines and other checkouts track these branches.

`act.py::push_allowed` enforces this and refuses `--unblock` / `--fix` on a branch it must not touch. A fork head is never pushed to.

## "fix it yourself": the handoff

A PR a workflow opened (`author:generated` — pulumi-bot's content-review and glow-up lanes) that still carries open findings has nowhere to go: a send-back is never read, and closing it only makes the lane re-queue the same page next run. Those rows always carry **fix it yourself**, whatever else is on them.

It is a `handoffs` entry on the row, not an action: `{"id": "handfix", "label": "fix it yourself", "run": "/address-review N", "why": …}`, with no `cmd`. The board renders it as an amber dashed toggle that composes onto a **second line** above the `--act` command — one `/address-review N` per lit row, since each is a separate interactive session — and `--terminal` prints it as `[fix it yourself]  $ /address-review N  (an interactive run, not part of --act)`. It never reaches `act.py`, never counts toward the progress line, and never turns the page into something that writes.

`analyze.py` adds it when all three hold: the author cannot revise (`can_revise` is false), the row has at least one open 🚨 or ⚠️, and `act.push_allowed` permits the branch. That last one is why a dependabot PR, a generated-docs regen and a fork head get nothing: the fix would be rebuilt over or could not be pushed at all.

## Voice

The approval body and every posted comment follow `pr-review:references:message-templates`. Tone still adjusts to `etiquette_trust` (low → warm; standard → friendly; high → terse), and no comment ever discloses scrutiny level, AI-suspect signals or what was checked.
