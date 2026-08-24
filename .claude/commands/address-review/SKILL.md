---
name: address-review
description: "Work a PR's pre-merge review to zero. Watches for the pinned review to land after you ship, then walks every finding — blockers, low-confidence, and style suggestions — with you until each one is fixed, refuted, deferred, or explicitly accepted. Use when the user types /address-review, ships a PR to pulumi/docs, asks to watch or monitor a PR for review results, says the review came back / what did the review say / address the review feedback, or is about to merge a PR that still has open findings."
argument-hint: "[<PR number or URL>] [--watch] [--no-watch] [--resume]"
user-invocable: true
---

# `/address-review` — work a pre-merge review to zero

**The rule this skill exists to enforce:** a PR is not finished when it is pushed. It is finished when **every** item the pre-merge review raised has been *fixed*, *refuted*, *deferred to a filed issue*, or *explicitly accepted with a stated reason* — 🚨 blockers, ⚠️ low-confidence findings, and ✏️ style suggestions alike.

The review pipeline is good at finding things and has no way to make anyone look at them. The measured failure mode is real: `scrape-review-outcomes.py` tracks an `ignored_low_confidence` outcome precisely because authors clear 🚨 and stop reading. This skill is the counterweight.

**Related skills:** `/docs-review` runs the same criteria locally *before* you push (cheaper). `/shipit` creates the PR and hands off here. `/pr-review` is the *maintainer* adjudication layer — it decides approve/merge; this one is the *author* side and runs first.

---

## Usage

`/address-review [<PR number or URL>] [--watch|--no-watch] [--resume]`

- **PR** — optional; inferred from the current branch when omitted.
- `--watch` — skip the offer and start watching for the review immediately.
- `--no-watch` — the review is already posted; go straight to the worklist.
- `--resume` — reload the saved worklist state and continue where the last session stopped.

Worklist state lives in `.review-worklist-<PR>.json` at the repo root (gitignored). It survives context loss: a fresh session with `--resume` picks up every disposition already recorded.

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

### Step 1 — Resolve the PR and classify the review state

```bash
PR=$(gh pr view --json number --jq .number)          # when no argument was given
gh pr view "$PR" --json isDraft,mergeStateStatus,labels,headRefOid,url,title
```

Classify from the labels — the five state labels are mutually exclusive (`set-review-label.sh` owns them):

| Label / signal | Meaning | What to do |
|---|---|---|
| PR is a draft | Review doesn't run on drafts | Offer to mark ready-for-review; that is what fires the review |
| `review:in-progress` | Workflow running now | Step 2 (watch) |
| `review:outstanding-issues` | Review posted, 🚨 > 0 | Step 3 |
| `review:no-blockers` | Review posted, 🚨 == 0 | Step 3 — ⚠️ and ✏️ items still need dispositions |
| `review:stale` | Pushed since the review ran | Refresh first (see Step 6), then Step 3 |
| `review:error` | Workflow failed before publishing | Check the Actions run; `@claude #update-review` to retry |
| `review:trivial` / `review:frontmatter-only` / `review:oversized` | Full review short-circuited | No pinned comment. If `review:prose-flagged` is also set, triage's advisory comment **is** the worklist — walk it the same way |

Verify freshness even on a `CURRENT`-looking label: pushes made with `GITHUB_TOKEN` or by a coding agent don't fire `synchronize`, so `review:stale` can be missing on a review that predates the head commit.

```bash
HEAD_SHA=$(gh pr view "$PR" --json headRefOid --jq .headRefOid)
REVIEWED_SHA=$(bash .claude/commands/docs-review/scripts/pinned-comment.sh fetch --pr "$PR" \
  | grep -oE '<!-- CLAUDE_REVIEW_HEAD [0-9a-f]+ -->' | tail -1 | grep -oE '[0-9a-f]{7,40}')
```

A `REVIEWED_SHA` that isn't a prefix of `HEAD_SHA` means stale regardless of labels — say so, and refresh before working the list. Working a stale review wastes the user's time on findings that may already be fixed.

### Step 2 — Watch for the review (only when it hasn't landed)

Follow `address-review:references:watching`. It covers both environments (event subscription where available, bounded polling otherwise), what to do while waiting, and when to give up and hand back.

### Step 3 — Build the worklist

```bash
python3 .claude/commands/docs-review/scripts/review-worklist.py --pr "$PR" --format json \
  --state ".review-worklist-$PR.json"
```

The script enumerates every item needing a disposition and assigns each a stable id (`outstanding:L40-50`, `low:L12`, `style:content/docs/a.md:L88`, `pre-existing:L7`), merges in the inline one-click suggestions posted on the Files-changed tab, and reports what is still undecided. On `--resume`, the same command reloads prior dispositions.

**If `parse_confidence` comes back `low`, do not proceed as if the list were complete** — read the pinned comment yourself and work from it, saying that the enumerator couldn't parse it.

Present the counts before working: `4 items: 1 blocker, 1 low-confidence, 2 style (1 one-click). Pre-existing: 1 (optional).` Then start.

### Step 4 — Walk the worklist with the user

**One item at a time, in bucket order:** 🚨 Outstanding → ⚠️ Low-confidence → ✏️ Style → 💡 Pre-existing (optional; ask once whether to include them at all, default no).

For each item, present a compact block — never a wall:

```text
[1/4] 🚨 outstanding:L40  content/docs/ai/skills/index.md
Finding:  "Pulumi supports 9 languages" — the docs say six.
Evidence: ❌ contradicted (source: content/docs/iac/languages-sdks/)
Proposal: change "nine" → "six" on line 40.
```

Then `AskUserQuestion` with the dispositions that plausibly apply to *this* item, drawn from the closed set in `address-review:references:dispositions`: **Fix it** / **Refute it** / **Defer to an issue** / **Accept as-is** / **Not applicable**. The tool takes at most four options, so offer the three or four that fit — your recommendation first, marked `(Recommended)` — and let the rest arrive through "Other". Whatever the user picks, map it back to one of the five before recording it.

Rules for the walk:

- **Have a proposal before you ask.** Read the file, work out the actual change, and show it. "What do you want to do about this?" with no proposal makes the user do the work twice.
- **Verify the finding before proposing a fix.** The review can be wrong; a fix applied to a false finding is worse than the finding. When you believe it's wrong, recommend *Refute* and bring the evidence — that's what the dispute path is for.
- **Batch only what is genuinely identical.** Style suggestions on the same rewrite across several files can be one question ("apply all 6 Vale suggestions?"). Substantive findings get their own question each.
- **Record every decision immediately** into `.review-worklist-<PR>.json` — `{"items": {"<id>": {"disposition": "fixed", "note": "..."}}}` — so a lost session resumes instead of restarting. `deferred`, `accepted`, and `not-applicable` require a note; the enumerator treats a missing one as still-open.
- **Apply fixes to the working tree as you go, but don't push mid-walk.** One push at the end keeps the auto-refresh gate's small-diff shape intact.
- **Never silently drop an item.** If the user doesn't answer one, it stays open and shows up in the Step 7 report.

### Step 5 — Execute the batch

1. Run the repo's own checks on what you changed: `make lint`, plus `ONLY_TEST="<program>" ./scripts/programs/test.sh` when a `static/programs/` example moved. Never push a review fix that breaks the build.
1. Commit with a message naming the review round (`Address pre-merge review: language count, 6 Vale suggestions`), keeping the `Co-Authored-By: Claude ...` trailer.
1. Push: `git push -u origin <branch>`.
1. **One-click style suggestions**: applying them in the GitHub UI and pushing a fix for the same line collide. Pick one lane per item and say which — either the user clicks **Add suggestion to batch** on the Files-changed tab (nothing for you to commit), or you edit the line locally and the button goes stale. Don't do both.

### Step 6 — Refresh the review and verify convergence

A push marks the review stale. Refreshing is not optional — an unrefreshed review is a permanent record that the findings were never addressed.

- **Small fix-push** (≤80 changed lines, every hunk on a flagged line): `auto-refresh-gate.py` fires the scoped refresh on its own. Wait for it rather than double-posting.
- **Anything else**: comment `@claude #update-review` and say what you did. Put fix-responses and disputes in the *same* mention — the update path handles both:

  ```text
  @claude #update-review

  Fixed: the language count on L40 (now "six"), and the 6 advisory Vale
  suggestions.

  Disputing L12: "teams often" is sourced from the 2026 state-of-IaC
  survey, cited two paragraphs down. Please re-check with that in view.
  ```

- Then re-run Step 3's command and confirm the fixed items moved into ✅ Resolved and the disputed ones were adjudicated (conceded, or held with a reason). **A finding the model holds after a dispute is still open** — take it back into Step 4 with the model's reasoning in hand.

Loop Steps 4-6 until `--require-clean` passes:

```bash
python3 .claude/commands/docs-review/scripts/review-worklist.py --pr "$PR" \
  --state ".review-worklist-$PR.json" --require-clean
```

### Step 7 — Report and hand off

Report in one block: what was fixed (with the commit), what was refuted (and how the model adjudicated), what was deferred (with issue links), what was accepted (with reasons), and anything still open. Then say what's next:

- **Clean** — the PR is ready for a maintainer. Mention `/pr-review <PR>` for the adjudication pass.
- **Not clean** — name exactly what's left and offer to keep going. Don't call a PR ready while the exit code says otherwise.

---

## Non-negotiables

- **Never** mark an item resolved because it looks minor. Style suggestions get a disposition like everything else — `accepted` with "house voice, leaving it" is a fine answer; silence is not.
- **Never** delete, hide, or resolve the pinned `<!-- CLAUDE_REVIEW N/M -->` comment. Hiding it makes later refreshes edit a comment nobody can see. Use the review's own ✅ Resolved section as the tracker.
- **Never** push a fix without re-running the review afterward.
- **Never** invent a finding's resolution in the PR thread that the diff doesn't support. The pinned comment is scraped after merge into the `#docs-ops` digest; a false "fixed" corrupts the tuning data the review's severity rules are built from.
- **Never** hold the user hostage. Pushy means asking once, clearly, with the cost stated. It does not mean refusing to proceed.
