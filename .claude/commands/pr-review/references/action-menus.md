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
| `blocked` | the unblock: `--unblock N` (dirty or behind), `--refresh N` (stale review), `--rerun N` (errored **or unreadable** review — a page of a split review missing, or a tally that outruns the parsed sections), `--rerun-checks N` (red checks that look like flake), `--close N --superseded-by M` (duplicate) | for open 🚨 findings, `--request-changes N` (send back to author) or `--close N` on an `author:generated` row; `--route N:@owner` when the row is another lane's; **fix it yourself** and **ask @claude to fix them** on an `author:generated` row with open findings (below); `open PR`. A blocked row that ends up with no unblock at all shows "Blocked: … no action available" and is counted on its own tally tile |
| `author:self` (your own PR, any verdict) | `--route N:@owner` | `open PR`; never a stamp or a send-back — you answer its findings with `/address-review`, and someone else approves |

Approving a judged row answers its findings on the way past: one `/resolve F<n> <disposition>: <why>` comment per judged finding, posted before the approval, then the approval, then the merge. A `deferred` judgment is not resolved — it is what the send-back (or close) button is for.

Whether approving merges is on the button, never implied: bot PRs (dependabot, pulumi-bot, WorkPrentice) default to approve-and-merge, a person's PR defaults to approval alone because merging is the author's call. The second button is the other choice, and picking it puts the first one out. `act.py` reads the `:merge` / `:no-merge` suffix per PR, so a batch of both stays one command.

A blocked row is never stampable, with or without `--force`. An in-progress review and someone else's changes-requested review have no mechanical unblock; the row names the blocker and waits. Red checks offer `--rerun-checks N`, which re-runs the failed jobs of the head's workflow runs as the head is — for a flake, not for a diff that is actually red; a red commit status has no run to re-run, and the step says so. Your **own** changes-requested review is not a blocker at all: the row becomes `sent-back:<date>` and parks under "Waiting on the author" until a commit lands. An errored review's unblock is `--rerun N` (`@claude #new-review`), and a row where no review ran at all (`review:trivial`, a draft, a bot skip) offers the same command as a side action, "run a full review".

A conflict is a blocker the unblock can only sometimes clear, and the board now remembers which. `--unblock` merges or it aborts; when it aborts, `act.py` posts the conflicted files on the PR under `<!-- PR_REVIEW_UNBLOCK_CONFLICT -->`, keyed to the head it tried. `collect.unblock_conflict` reads that record back while it still describes the current head, and the row then carries `unblock:refused:conflict` and offers the send-back instead of the button. Without it the failure lived only in the run's stdout: the next render saw the same `mergeable:dirty`, offered the same **merge base & retry**, and re-ran the same conflict — a button that did nothing, every time. Any push to the branch moves the head, spends the record, and brings the button back.

## Cluster moves

A collision cluster's recommendation is a button on the row it belongs to (`analyze.attach_cluster_actions`), not a strip above the rows: the board has no batch controls at all, because a batch button sits where the evidence for the decision is not. `--stamp` for the stampable set needs none — those rows arrive with their approve button selected, so the default command already merges them — and every other batch is the row buttons it would have pressed.

- **chain** → `--chain C1`, on the lead's row, as its coloured button. It is offered only where the collision is the *only* thing holding the lead back: every overlapping cluster member is a `judge` row, because the overlap is itself a gate, so the verdict cannot answer this and `analyze.only_collisions_hold()` does — every recorded `gate_fails` entry is a `cluster:` / `directional:` / `duplicate:` code. A lead held up by anything else (an open ⚠️ row, a judged 🚨, a stale review, a new blog post, a diff over the size cap) gets no chain button, since `--chain` approves that lead with `--force`: it keeps its own approve-as-is button, next to the findings behind the call. The button `covers` the next link (`data-covers`): while it is lit that row reads "✓ covered by the chain from #N", counts as decided, and any decision picked there puts the chain out, so the command can never carry both. One link per run; the next waits on CI. A cluster with no next link that overlaps the lead gets no chain button, because the row's own approve is the same move.
- **consolidate** → `--request-changes <newest> --reason "<newest>=…"`, on the newest sweep's row, since that is the PR the request is posted on. A decision like any other: lighting it puts out the row's other decision.
- **ignore** and **theirs** carry no button; their detail stays in the folded "Collisions" section at the bottom.

`queue.do_next` still exists — the cluster moves plus the send-back / close / route / stamp / unblock batches, one sentence and one command each, most leverage first — but only `--terminal` prints it, because a terminal has no buttons to press and a batch command is the one thing it cannot compose by clicking.

## Terminal mode

`--terminal` prints the table — every row with its reasons wrapped rather than cut, its blockers (`blocked: …`, with `(no action available)` when nothing unblocks it), its open findings (`open: F<n> …`) or judgments (`judged: …`), and every action as `[label]  --fragment` — then the batch list (`do_next`: the row actions above, batched into one `$ /pr-review --act …` command each), the collision clusters (members listed with "(all waiting on others)" when analyze has stripped every member from the merge order), the directional conflicts, and both waiting lists. Then, for judge rows only, one AskUserQuestion per row:

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

**The two ways out of a stuck workflow PR.** A row whose author is a workflow (`author:generated`) with open findings carries both, because nobody will ever answer its review and closing it only re-queues the page:

- **fix it yourself** — the handoff. Composes `/address-review N` on its own amber line above the `--act` command, one interactive run per PR. You walk the findings and push the fixes.
- **ask @claude to fix them** — `--ask-fix N`. One comment, `@claude fix F1 and F3 #update-review`, naming the row's open findings by id with their summaries beneath, so the agent already watching the PR fixes them and refreshes the review. It is an ordinary write, so unlike the handoff it batches with everything else.

They do the same job, so they share one exclusive group (`data-exclusive="fix"`) and lighting either puts the other out — `clearRow` cannot pair them, since the handoff is deliberately not a decision. `--ask-fix` names only the review's *open* rows: a style or pre-existing finding is the review's own take-it-or-leave-it, and asking for it would turn an optional note into a push. A row with nothing open is refused at plan time rather than posting `@claude fix  #update-review`.

## "fix it yourself": the handoff

A PR a workflow opened (`author:generated` — pulumi-bot's content-review and glow-up lanes) that still carries open findings has nowhere to go: a send-back is never read, and closing it only makes the lane re-queue the same page next run. Those rows always carry **fix it yourself**, whatever else is on them.

It is a `handoffs` entry on the row, not an action: `{"id": "handfix", "label": "fix it yourself", "run": "/address-review N", "why": …}`, with no `cmd`. The board renders it as an amber dashed toggle that composes onto a **second line** above the `--act` command — one `/address-review N` per lit row, since each is a separate interactive session — and `--terminal` prints it as `[fix it yourself]  $ /address-review N  (an interactive run, not part of --act)`. It never reaches `act.py`, never counts toward the progress line, and never turns the page into something that writes.

`analyze.py` adds it when all three hold: the author cannot revise (`can_revise` is false), the row has at least one open 🚨 or ⚠️, and `act.push_allowed` permits the branch. That last one is why a dependabot PR, a generated-docs regen and a fork head get nothing: the fix would be rebuilt over or could not be pushed at all.

## Voice

The approval body and every posted comment follow `pr-review:references:message-templates`. Tone still adjusts to `etiquette_trust` (low → warm; standard → friendly; high → terse), and no comment ever discloses scrutiny level, AI-suspect signals or what was checked.
