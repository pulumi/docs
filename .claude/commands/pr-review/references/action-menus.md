---
user-invocable: false
description: The row action bar per verdict, the terminal-mode menus, and which bot branches may be pushed to
---

# Row actions

Every row on the board carries an action bar; every button only adds an `act.py` fragment to the command at the bottom of the page. The bar is derived from the row's verdict and reason codes by `analyze.py`, so the board and `--terminal` offer the same choices.

## Action bar by verdict

| Verdict | Primary | Also offered |
|---|---|---|
| `stamp` | `--stamp N` (approve + squash-merge; the button starts selected) | `open PR` |
| `judge` | `--stamp N --force` (approve as-is) | `--request-changes N` (send back to author: a changes-requested review built from the judgments, plus `needs-author-response`); `--fix N` when the row has a drafted description or one-click suggestions; `--render N` when it has preview pages; `--deploy N` on `risk:infra`; `--route N:@owner`; `open PR` |
| `route` | `--route N:@owner` (request review + post the defects) | `open PR` |
| `blocked` | the unblock: `--unblock N` (dirty), `--refresh N` (stale review), `--close N --superseded-by M` (duplicate) | `open PR` |

A blocked row is never stampable, with or without `--force`. Red checks, an in-progress or errored review, and a changes-requested review have no mechanical unblock; the row names the blocker and waits.

## Do next

The board opens with at most a handful of cards, each one sentence and one button, most leverage first: a cluster's recommendation (**consolidate** → `--request-changes <newest> --reason …`; **chain** → `--chain C1`), then the batches (`--request-changes` for every row the judge sent back, `--route` per owner, `--stamp` for the stamp set). A same-file cluster or one that is mostly waiting on others gets no card; its detail stays in the folded "Collisions" section at the bottom.

## Terminal mode

`--terminal` prints the table and then, for judge rows only, one AskUserQuestion per row:

1. **Approve as-is** (`--stamp N --force`) — recommended when the judgment box's disposition is `accepted` / `not-applicable` / `refuted` and nothing else is open.
2. **Send back to author** (`--request-changes N`) — when a finding is the author's to fix: the judgments become the review body, line-anchored, in the voice `message-templates.md` sets for that author type.
3. **Route to owner** (`--route N:@owner`) — when the call belongs to the lane's team.
4. **Skip** — leave the row for later (`--refresh N` when the finding reads as stale is offered from the row itself).

AskUserQuestion is not used anywhere else in this skill; the board composes the command itself.

## Bot PRs: what may be pushed

The old rule was "no changes on bot PRs". It applies only where a push would be thrown away:

- **Dependabot** — never push. The PR is regenerated on the next run; edits break the update.
- **Generated-docs regens** (`pulumi-bot` with the `automation/merge` label) — never push. Regenerated from source; fix the generator.
- **`workprentice[bot]`** and **`content-review/*`** branches (pulumi-bot's content-review and glow-up PRs) — pushes are allowed: `--fix`, `--unblock`, and a hand fix all land as ordinary commits or **merge commits**. Never rebase, never force-push: the pipelines and other checkouts track these branches.

`act.py::push_allowed` enforces this and refuses `--unblock` / `--fix` on a branch it must not touch. A fork head is never pushed to.

## Voice

The approval body and every posted comment follow `pr-review:references:message-templates`. Tone still adjusts to `etiquette_trust` (low → warm; standard → friendly; high → terse), and no comment ever discloses scrutiny level, AI-suspect signals or what was checked.
