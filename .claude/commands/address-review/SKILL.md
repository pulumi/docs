---
name: address-review
description: "Work a PR's pre-merge review to zero. Watches for the review to land after you ship, then walks every finding — blocking 🚨/❓ items, advisory ⚠️ reviewer checks, and ✏️ style suggestions — with you until each one is fixed, refuted, deferred, or explicitly accepted. Use when the user types /address-review, ships a PR to pulumi/docs, asks to watch or monitor a PR for review results, says the review came back / what did the review say / address the review feedback, or is about to merge a PR that still has open findings."
argument-hint: "[<PR number or URL>] [--watch] [--no-watch] [--resume]"
user-invocable: true
---

# `/address-review` — work a pre-merge review to zero

**The rule this skill exists to enforce:** a PR is not finished when it is pushed. It is finished when **every** item the pre-merge review raised has been *fixed*, *refuted*, *deferred to a filed issue*, or *explicitly accepted with a stated reason* — 🚨 blockers, ❓ author questions, ⚠️ reviewer checks, and ✏️ style suggestions alike.

The review pipeline is good at finding things and has no way to make anyone look at them. The measured failure mode is real: `scrape-review-outcomes.py` tracks an `ignored_low_confidence` outcome precisely because authors clear 🚨 and stop reading. This skill is the counterweight.

**Related skills:** `/docs-review` runs the same criteria locally *before* you push (cheaper). `/shipit` creates the PR and hands off here. `/pr-review` is the *maintainer* adjudication layer — it decides approve/merge; this one is the *author* side and runs first.

---

## Two surfaces

The v3 surface is on repo-wide for pulumi/docs (`REVIEW_V3_COMMENTS`), so **every fresh review renders v3 cards**. Write for v3 by default.

| | **v3 (default)** | **legacy v2** |
|---|---|---|
| Where the findings live | Author card `<!-- CLAUDE_REVIEW_AUTHOR -->` + reviewer brief `<!-- CLAUDE_REVIEW_BRIEF -->` | One monolithic pinned comment, `<!-- CLAUDE_REVIEW N/M -->`, sometimes paginated |
| Finding ids | `F1`, `F2`, … — stable across re-reviews, never reused | Synthetic `outstanding:L40`, `low:L12`, invented per run |
| Dispositions recorded in | `<!-- REVIEW_STATE … -->` on the author card (**source of truth**) | Nowhere — the ✅ Resolved prose is the only trace |
| Buckets | 🚨 outstanding · ❓ author-answer (both block) · ⚠️ reviewer-check (brief, advisory) · ✏️ style · 💡 pre-existing | 🚨 outstanding · ⚠️ low-confidence · ✏️ style · 💡 pre-existing |
| Merge gate | the **Sentinel** check run | none — the labels are advisory |
| Answer lanes | push · `@claude … #update-review` · `/resolve F<n> …` | push · `@claude … #update-review` |

A PR reviewed before the flip **keeps its v2 monolith forever** — a `#update-review` on it refreshes v2 in place (`claude-update.yml` grandfathers it deliberately). Only `@claude #new-review` regenerates it as cards. Detect the surface, don't assume it from the PR's age.

Everything below is the v3 path unless a step says otherwise; **§Legacy v2 PRs** covers the differences.

---

## Usage

`/address-review [<PR number or URL>] [--watch|--no-watch] [--resume]`

- **PR** — optional; inferred from the current branch when omitted.
- `--watch` — skip the offer and start watching for the review immediately.
- `--no-watch` — the review is already posted; go straight to the worklist.
- `--resume` — reload the saved worklist state and continue where the last session stopped.

Local worklist notes live in `.review-worklist-<PR>.json` at the repo root (gitignored). On v3 this is a **cache, not the ledger** — `REVIEW_STATE` on the PR is the ledger, and the enumerator seeds from it, so a fresh session with `--resume` recovers dispositions even with the file deleted.

---

## Offer this without being asked

**Whenever you open or push to a PR in this repo, the review loop is part of the job.** Do not wait to be asked.

1. **On PR creation (draft).** Say in one line that automated review fires when the PR goes ready-for-review, and that you'll work the findings when they land. Don't offer to watch yet — a draft gets no review.
1. **On ready-for-review.** Offer to watch, with `AskUserQuestion`: *Watch for the review* (recommended) / *Ping me when I ask* / *Skip — I'll merge without it*. If watching, follow `address-review:references:watching`.
1. **When the review lands.** Announce the bucket counts and start Step 3. Do not summarize the review and stop — a summary is not a disposition.
1. **Whenever the user moves to merge with items still open.** Say so plainly, once, with the count and the shortest path to clearing it: *"3 findings still open (1 blocker, 2 style). Want me to work them now — about 5 minutes — or record why we're merging over them?"* Recording a reason is a legitimate outcome; skipping the question is not.

**Be pushy, not obstructive.** Raise it once per decision point, concretely, then do what the user says. Never block a merge the user has decided on, never re-litigate a finding they already dispositioned, and never nag about items that are already dispositioned. If the user says "just merge it," record `accepted` with their reason on the open items so the ledger tells the truth, then get out of the way.

---

## Process

Steps 1-3 are mostly silent. Step 4 is the skill.

### Step 1 — Resolve the PR, identify the surface, check freshness

```bash
PR=$(gh pr view --json number --jq .number)          # when no argument was given
gh pr view "$PR" --json isDraft,mergeStateStatus,labels,headRefOid,url,title
```

Classify from the labels — the five state labels are mutually exclusive (`set-review-label.sh` owns them):

| Label / signal | Meaning | What to do |
|---|---|---|
| PR is a draft | Review doesn't run on drafts | Offer to mark ready-for-review; that is what fires the review |
| `review:in-progress` | Workflow running now | Step 2 (watch) |
| `review:outstanding-issues` | Review posted, blocking findings > 0 | Step 3 |
| `review:no-blockers` | Review posted, no blocking findings | Step 3 — ⚠️ and ✏️ items still need dispositions |
| `review:stale` | Pushed since the review ran (or a run's head moved mid-review and its re-dispatch is pending or capped) | Refresh first (see Step 6), then Step 3 |
| `review:error` | Workflow failed before publishing | Check the Actions run; `@claude #new-review` to retry from scratch |
| `review:author-stalled` | The SLA sweep warned the author that items have sat unanswered | Work the list now; it's the clock, not a new finding |
| `review:waived` | Someone used the Sentinel break-glass | The gate is bypassed and logged. Findings still deserve dispositions — ask before treating the PR as done |
| `review:trivial` / `review:frontmatter-only` / `review:oversized` | Full review short-circuited | No review cards. If `review:prose-flagged` is also set, triage's advisory comment **is** the worklist — walk it the same way |

When two of those labels are set at once — a failed run can leave `review:error` beside the terminal label from the write that preceded it — the labels are the unreliable half. Believe the cards: their content and `CLAUDE_REVIEW_HEAD` say what was actually published, and a `review:error` alongside them means the run died after writing, so re-read before assuming the list is complete.

Then read the surface off the comments themselves rather than guessing:

```bash
BODY=$(bash .claude/commands/docs-review/scripts/pinned-comment.sh fetch --pr "$PR")
case "$BODY" in
  *'<!-- CLAUDE_REVIEW_AUTHOR -->'*) SURFACE=v3 ;;
  *'<!-- CLAUDE_REVIEW '*)           SURFACE=v2 ;;
  *)                                 SURFACE=none ;;
esac
```

`fetch` selects comments by the `<!-- CLAUDE_REVIEW N/M -->` first line, and the v3 author card keeps `<!-- CLAUDE_REVIEW 1/1 -->` as exactly that — so the author card comes back, and the reviewer brief, which carries no `N/M` marker, does not. **Test for the author marker first**, or every v3 PR reads as v2. You don't need the brief here; `review-worklist.py` fetches it itself in Step 3.

Freshness is the same check on both surfaces:

```bash
HEAD_SHA=$(gh pr view "$PR" --json headRefOid --jq .headRefOid)
REVIEWED_SHA=$(bash .claude/commands/docs-review/scripts/pinned-comment.sh last-reviewed-sha --pr "$PR")
```

Verify it even on a `CURRENT`-looking label: pushes made with `GITHUB_TOKEN` or by a coding agent don't fire `synchronize`, so `review:stale` can be missing on a review that predates the head commit. A `REVIEWED_SHA` that isn't a prefix of `HEAD_SHA` means stale regardless of labels — say so, and refresh before working the list. Working a stale review wastes the user's time on findings that may already be fixed.

### Step 2 — Watch for the review (only when it hasn't landed)

Follow `address-review:references:watching`. It covers both environments (event subscription where available, bounded polling otherwise), what to do while waiting, and when to give up and hand back.

### Step 3 — Build the worklist

```bash
python3 .claude/commands/docs-review/scripts/review-worklist.py --pr "$PR" --format json \
  --state ".review-worklist-$PR.json"
```

The script detects the surface itself. On v3 it reads both cards, enumerates every item needing a disposition under the card's own `F<n>` ids, merges in the inline one-click suggestions from the Files-changed tab, **seeds each finding's disposition from the `REVIEW_STATE` block**, and reports what is still undecided. Style items keep `style:<file>:L<n>` ids — they carry no `F<n>` and never appear in `REVIEW_STATE`, so those live in the local state file alone.

**If `parse_confidence` comes back `low`, do not proceed as if the list were complete** — read the cards yourself and work from them, saying that the enumerator couldn't parse them. On v3, `low` means the head sentinel is missing or `REVIEW_STATE` didn't parse; either gap means the seeded dispositions can't be trusted.

Present the counts before working: `5 items: 1 blocker, 1 author question, 2 style (1 one-click), 1 reviewer check (advisory).` Everything the enumerator returns goes in that total. **On v3 nothing is optional** — `extract_items_v3` emits 🚨, ❓, ⚠️ and ✏️ items, all with `optional: False`, so `remaining` is simply every undecided item and a count that leaves the advisory buckets out won't match what `--require-clean` measures. There is no 💡 item to leave out: pre-existing issues appear on the brief as a *count*, with the detail on the evidence page, and the enumerator never emits one. (On v2 it does, and there `optional: True` makes 💡 the one bucket `remaining` skips.) Then start.

### Step 4 — Walk the worklist with the user

**One item at a time, in bucket order:** 🚨 Outstanding → ❓ Questions for you → ✏️ Style → ⚠️ Reviewer checks. That's the whole v3 walk — 💡 pre-existing is a walk step on v2 only, since the v3 enumerator emits no such item. When the brief's pre-existing count is non-zero and the user wants them, read them off the evidence page and treat them as out-of-scope candidates (`deferred` with an issue), not as worklist rows.

The first two block merge. ⚠️ lives on the *reviewer's* brief and is addressed to the approver, not to you — it still gets a disposition, because an item the reviewer is told to check is an item someone has to answer, but it never blocks and it's the right bucket to batch.

For each item, present a compact block — never a wall:

```text
[1/5] 🚨 F1  content/docs/ai/skills/index.md L40
Finding:  "Pulumi supports 9 languages" — the docs say six.
Evidence: ❌ contradicted (source: content/docs/iac/languages-sdks/)
Proposal: change "nine" → "six" on line 40.
```

Then `AskUserQuestion` with the dispositions that plausibly apply to *this* item, drawn from the closed set in `address-review:references:dispositions`: **Fix it** / **Refute it** / **Defer to an issue** / **Accept as-is** / **Not applicable**. The tool takes at most four options, so offer the three or four that fit — your recommendation first, marked `(Recommended)` — and let the rest arrive through "Other". Whatever the user picks, map it back to one of the five before recording it.

Rules for the walk:

- **Have a proposal before you ask.** The v3 card usually hands you one: each blocking finding carries an `F<n> · Do this` block with the verbatim line, the reasoning, and a replacement. Read the file to confirm the line still matches, then show the change. "What do you want to do about this?" with no proposal makes the user do the work twice.
- **Verify the finding before proposing a fix.** The review can be wrong; a fix applied to a false finding is worse than the finding. When you believe it's wrong, recommend *Refute* and bring the evidence — that's what the dispute path is for.
- **Batch only what is genuinely identical.** Style suggestions on the same rewrite across several files can be one question ("apply all 6 Vale suggestions?"). Substantive findings get their own question each.
- **Record every decision immediately.** Write it into `.review-worklist-<PR>.json` — `{"items": {"F1": {"disposition": "fixed", "note": "..."}}}` — as you go, then push the non-`fixed` ones to `REVIEW_STATE` in Step 5. `deferred`, `accepted`, and `not-applicable` require a note; the enumerator treats a missing one as still-open.
- **Apply fixes to the working tree as you go, but don't push mid-walk.** One push at the end keeps the auto-refresh gate's small-diff shape intact.
- **Never silently drop an item.** If the user doesn't answer one, it stays open and shows up in the Step 7 report.

### Step 5 — Execute the batch

1. Run the repo's own checks on what you changed: `make lint`, plus `ONLY_TEST="<program>" ./scripts/programs/test.sh` when a `static/programs/` example moved. Never push a review fix that breaks the build.
1. Commit with a message naming the review round (`Address pre-merge review: language count, 6 Vale suggestions`), keeping the `Co-Authored-By: Claude ...` trailer.
1. Push: `git push -u origin <branch>`.
1. **Record the dispositions that a push doesn't evidence** — see Step 6 for which lane.
1. **One-click style suggestions**: applying them in the GitHub UI and pushing a fix for the same line collide. Pick one lane per item and say which — either the user clicks **Add suggestion to batch** on the Files-changed tab (nothing for you to commit), or you edit the line locally and the button goes stale. Don't do both.

### Step 6 — Answer the findings and verify convergence

A push alone answers only `fixed`. Everything else has to land in `REVIEW_STATE`, and an unanswered finding blocks the Sentinel however thoroughly you discussed it here.

**Pick the lane by what the finding needs:**

| Lane | Use it for | Cost |
|---|---|---|
| **Push a fix** | `fixed`. A small fix-push (≤80 changed lines, every hunk within ±3 lines of a finding's `[L…]` anchor) trips `auto-refresh-gate.py`: the card shows a 🔄 banner within a minute and refreshes itself. Wait for it rather than double-posting. **Only the author card's 🚨 and ❓ findings anchor a refresh** — a hunk fixing a ⚠️ brief item or a ✏️ suggestion falls outside every anchor and declines the whole push, so a mixed fix-push needs the mention below. | free |
| **`/resolve F<n> <disposition>[: reason]`** | Agent-facing bookkeeping — recording a disposition the user already decided, in bulk if needed (`/resolve all accepted: <why>`). Writes `REVIEW_STATE` directly, no model runs. | zero model cost |
| **`@claude <reasoning> #update-review`** | Anything needing adjudication: a dispute, a fix the gate didn't catch, a question answered in prose. The only lane that can *change the review's mind*. | a model run |

`/resolve` is deliberately not surfaced to human contributors — it's plumbing. Use it when you're recording, not arguing. It needs the PR author or a write/maintain/admin collaborator (it fails closed), it is ignored on comments from bot accounts, and `deferred` / `accepted` / `not-applicable` each need a reason after the colon.

**On your own PR, a non-`fixed` disposition is recorded as `author-accepted`**, with what you typed preserved as `original_disposition`. That's by design: self-adjudication shouldn't read as independent adjudication. The Sentinel counts it as answered, and the reviewer brief keeps the row visible for the human approver. Tell the user that's what will happen before they pick *Refute* on their own PR — a refutation they want the model to actually weigh belongs in `#update-review`, not `/resolve`.

Put fixes and disputes in the *same* mention — the update path handles both:

```text
@claude #update-review

Fixed: F1, the language count on L40 (now "six"), and the 6 advisory Vale
suggestions.

Disputing F3: "teams often" is sourced from the 2026 state-of-IaC survey,
cited two paragraphs down. Please re-check with that in view.
```

Then re-run Step 3's command and confirm the fixed items moved to answered and the disputed ones were adjudicated (conceded, or held with a reason). **A finding the model holds after a dispute is still open** — take it back into Step 4 with the model's reasoning in hand.

Loop Steps 4-6 until `--require-clean` passes:

```bash
python3 .claude/commands/docs-review/scripts/review-worklist.py --pr "$PR" \
  --state ".review-worklist-$PR.json" --require-clean
```

### Step 7 — Report and hand off

Report in one block: what was fixed (with the commit), what was refuted (and how the model adjudicated), what was deferred (with issue links), what was accepted (with reasons), and anything still open. Then say what's next.

**`--require-clean` is the author's bar, not the merge gate.** Where the Sentinel runs, a PR is done when its check passes: findings answered (G2), the team named in `.github/review-routing.yml` has approved (G3), CI green, no conflict. Read the check run rather than inferring:

```bash
gh pr checks "$PR" | grep -i sentinel
```

- **Clean and Sentinel green** — the PR is ready for a maintainer. Mention `/pr-review <PR>` for the adjudication pass.
- **Clean but Sentinel red on G3** — nothing is yours. It's waiting on a human approver; say so once and stop. A push cannot add an approval and can dismiss the ones already given.
- **Not clean** — name exactly what's left and offer to keep going. Don't call a PR ready while the exit code says otherwise.

The Sentinel is behind `REVIEW_V3_SENTINEL` (unset = dark, `report` = report-only, `1` = enforcing). That's a repo variable, so which mode is live can't be read from the repo — read the check run itself instead of trusting any sentence about the rollout, this one included. A `neutral` conclusion means the verdict rides inside the summary rather than gating: either report-only mode (`REPORT-ONLY — would be: …`) or a draft PR. `success` / `failure` means it's enforcing. Report-only mode maintains the gate-status *comment* only on `sentinel:preview` PRs, so no comment doesn't mean no check. When there's no Sentinel check on the PR at all, `--require-clean` is the whole bar — say that rather than implying a gate that isn't running.

---

## Legacy v2 PRs

A PR still carrying the monolith works the same way with four differences:

1. **Ids are synthetic** (`outstanding:L40-50`, `low:L12`, `pre-existing:L7`) and get re-invented on every refresh, so a stale local state file can mismatch. Re-run Step 3 after any refresh rather than trusting `--resume` across one.
1. **There is no `REVIEW_STATE` and no `/resolve`** — that lane is gated on the v3 surface. Every non-`fixed` disposition goes through `@claude … #update-review`, and the local state file is the only ledger.
1. **The bucket order is** 🚨 Outstanding → ⚠️ Low-confidence → ✏️ Style → 💡 Pre-existing. There is no ❓ bucket; ⚠️ here is low-confidence findings addressed to *you*, not reviewer checks.
1. **The Sentinel scores it by counting 🚨 bullets** on the current head. A v2 PR with open blockers can only clear G2 by having them disappear from the comment — there is no disposition lane to answer them with. If the user wants to answer rather than fix, the honest move is `@claude #new-review` to regenerate as cards; say so plainly, and note it costs a full review.

Offer the migration when it buys something (open blockers the user wants to dispute, or a long-lived PR that will see several more rounds). Don't offer it on a PR with nothing outstanding — a green v2 review is grandfathered by G1 and merges fine.

---

## Non-negotiables

- **Never** mark an item resolved because it looks minor. Style suggestions get a disposition like everything else — `accepted` with "house voice, leaving it" is a fine answer; silence is not.
- **Never** delete, hide, or resolve the review's own comments — the `<!-- CLAUDE_REVIEW_AUTHOR -->` card, the `<!-- CLAUDE_REVIEW_BRIEF -->` brief, or a legacy `<!-- CLAUDE_REVIEW N/M -->` monolith. Hiding one makes later refreshes edit a comment nobody can see, and the author card carries `REVIEW_STATE` — delete it and every disposition on the PR is gone.
- **Never** hand-edit `REVIEW_STATE`. Write it through `/resolve` or `#update-review`, both of which re-fetch the card immediately before writing; a hand-edit races the update lane's model step and loses.
- **Never** push a fix without confirming the review caught up afterward.
- **Never** invent a finding's resolution in the PR thread that the diff doesn't support. The cards are scraped after merge into the `#docs-ops` digest; a false "fixed" corrupts the tuning data the review's severity rules are built from.
- **Never** hold the user hostage. Pushy means asking once, clearly, with the cost stated. It does not mean refusing to proceed.
