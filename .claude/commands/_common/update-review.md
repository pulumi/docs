---
user-invocable: false
description: Re-entrant docs review. Updates the existing pinned review in place using the previous comment(s) and new commits.
---

# Update Review (re-entrant)

Shared primitive for "previous review + new commits/mention = updated review." Used by:

- `.github/workflows/claude.yml` when a `@claude` mention lands on a PR with an existing pinned review.
- The user-facing `pr-review` skill, when its adjudication step detects that the pinned review is stale.

The output of this skill replaces the contents of the existing pinned-comment sequence; it does **not** post a new comment unless the previous summary is gone (see "Fallback").

> **Re-entrant runs use Sonnet** (`claude-sonnet-4-6`). The cheaper model is doing the most-frequent task, so the constraints below — especially "do not restate prior findings" — must be foregrounded in the prompt.

---

## Inputs

- `PR_NUMBER`
- (Optional) `MENTION_BODY` — the text of the `@claude` mention that triggered the run, when applicable
- (Optional) `MENTION_AUTHOR` — the GitHub username who left the mention

The skill loads everything else for itself:

```bash
# Previous review (the pinned comment sequence)
bash .claude/commands/_common/scripts/pinned-comment.sh fetch --pr "$PR_NUMBER"
# Returns the full body of every CLAUDE_REVIEW N/M comment, in order, separated by markers.

# Diff since the last review
LAST_SHA=$(bash .claude/commands/_common/scripts/pinned-comment.sh last-reviewed-sha --pr "$PR_NUMBER")
gh pr diff "$PR_NUMBER" --range "$LAST_SHA..HEAD"

# Current PR state
gh pr view "$PR_NUMBER" --json title,body,labels,files,headRefOid,headRefName
```

`last-reviewed-sha` reads the most recent SHA from the 📜 Review history section in the 1/M comment. If unparseable, the skill falls back to a full `gh pr diff` (effectively starting over).

---

## Three cases

Decide which case applies *before* re-running fact-check or extracting new claims. Misclassifying wastes a model run and produces noisy output.

### Case 1 — fix-response

The author pushed commits that look like fixes for the previous 🚨 Outstanding findings. Signals:

- New commits since the previous review.
- (Optional) A mention like "I fixed the X you flagged" or "addressed feedback."

**Action:**

1. Re-verify each previously-outstanding finding against the new diff. For each:
   - Resolved → move to ✅ Resolved since last review
   - Still present → keep in 🚨 Outstanding
   - Worse → keep in 🚨 Outstanding with a note ("recurs after the latest commit")
2. Extract any *new* findings introduced by the new commits. Apply the domain rules.
3. Append a 📜 Review history line: `<timestamp> — re-reviewed after fix push (<commit count> new commits, <SHA>)`.

### Case 2 — dispute

The author or another reviewer pushed back on a previous finding *without* a fix push. Signals:

- A mention like "I disagree with X" / "this is intentional" / "the linter passes, why are you flagging this?"
- No new commits, or commits unrelated to the disputed finding.

**Action:**

1. Re-examine the disputed finding against the **current** diff and any cited evidence in the mention.
2. If the author is right — concede cleanly. Move the finding from 🚨 Outstanding to ✅ Resolved since last review with a brief "concede: <reason>" annotation.
3. If the author is wrong — keep the finding and add a short reply paragraph to the 📜 Review history explaining why, with the evidence (file:line, command output, gh URL).
4. **Do not** reword the same finding hoping it lands better. The original wording is in the comment; either change your mind or explain why you didn't.

### Case 3 — re-verify

A `@claude` mention with no specific request, or a generic "please re-review." Signals:

- Mention body is short and non-specific ("/claude refresh" / "@claude take another look").
- New commits may or may not be present.

**Action:**

1. If new commits → run as Case 1 (fix-response).
2. If no new commits → re-verify the existing 🚨 Outstanding findings only (don't re-extract from scratch). For each finding still applicable, leave in place; for each no longer applicable, move to ✅ Resolved.
3. Append 📜 Review history: `<timestamp> — re-verified on request (<author>)`.

---

## What this skill must NOT do

- **Do not restate previously-Outstanding findings in the new run's narrative.** They're already visible in the 1/M comment; repeating them is the noisiest possible output. The bucket update *is* the communication.
- **Do not re-introduce findings the author already responded to** unless the response was wrong AND you have new evidence.
- **Do not delete the 1/M comment.** Always edit in place via the pinned-comment script. The script enforces this; do not work around it.
- **Do not lower scrutiny on disputed findings just because the author disputed them.** Concede on evidence, not on tone.
- **Do not rerun fact-check from scratch when the diff hasn't changed.** Reuse the previous results; only re-verify claims affected by new commits.

---

## Output

Hand the updated review object to `_common/docs-review-core.md`'s output format. The 1/M comment's content reshapes accordingly:

- 🚨 Outstanding shrinks (or grows on regressions)
- ✅ Resolved fills in
- 📜 Review history gains one line
- Status counts at the top update

Then post via:

```bash
bash .claude/commands/_common/scripts/pinned-comment.sh upsert \
  --pr "$PR_NUMBER" \
  --body-file "$REVIEW_OUTPUT_FILE"
```

The pinned-comment script handles the in-place edit, overflow append, and tail prune.

---

## Fallback — pinned comment is missing

If `pinned-comment.sh fetch` returns nothing — author deleted the comment, history was rewritten, or this is a freshly transitioned PR that somehow skipped the initial review — fall back to a full initial review using [`docs-review-ci.md`](../docs-review-ci.md) and post fresh. The new comment lands at the bottom of the timeline; not ideal, but recoverable.
