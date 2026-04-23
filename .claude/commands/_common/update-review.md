---
user-invocable: false
description: Re-entrant docs review. Updates the existing pinned review in place using the previous comment(s) and new commits.
---

# Update Review (re-entrant)

Shared primitive for "previous review + new commits/mention = updated review." Used by:

- `.github/workflows/claude.yml` when a `@claude` mention lands on a PR with an existing pinned review.
- The user-facing `pr-review` skill, when its adjudication step detects that the pinned review is stale.

The output of this skill replaces the contents of the existing pinned-comment sequence; it does **not** post a new comment unless the previous summary is gone (see "Fallback").

> **Re-entrant runs use Sonnet** (`claude-sonnet-4-6`). The cheaper model is doing the most-frequent task, so the constraints below -- especially "do not restate prior findings" -- must be foregrounded in the prompt with concrete examples. The Sonnet-specific examples further down this file are not decorative; they are how the rule sticks under a cheaper model.

---

## Inputs

- `PR_NUMBER`
- (Optional) `MENTION_BODY` -- the text of the `@claude` mention that triggered the run, when applicable
- (Optional) `MENTION_AUTHOR` -- the GitHub username who left the mention

The skill loads everything else for itself:

```bash
# Previous review (the pinned comment sequence)
bash .claude/commands/_common/scripts/pinned-comment.sh fetch --pr "$PR_NUMBER"
# Returns the full body of every CLAUDE_REVIEW N/M comment, in order, separated by markers.

# Diff since the last review
LAST_SHA=$(bash .claude/commands/_common/scripts/pinned-comment.sh last-reviewed-sha --pr "$PR_NUMBER")
gh pr diff "$PR_NUMBER" --range "$LAST_SHA..HEAD"

# Current PR state (including draft status)
gh pr view "$PR_NUMBER" --json title,body,isDraft,labels,files,headRefOid,headRefName
```

`last-reviewed-sha` reads the most recent SHA from the 📜 Review history section in the 1/M comment.

**Fallback rules when `last-reviewed-sha` is unusable:**

- **Empty output** (history line missing, comment corrupted): fall back to a full `gh pr diff "$PR_NUMBER"` (no range). Treat the whole PR as new content; this is equivalent to starting over.
- **SHA unreachable** (author force-pushed and rewrote history): `gh pr diff --range "$LAST_SHA..HEAD"` will fail with "unknown revision" or similar. Detect the non-zero exit and fall back to full `gh pr diff "$PR_NUMBER"`. Append a 📜 Review history line noting the force-push detection: `<timestamp> — history rewritten since last review; re-reviewed against HEAD (<SHA>)`.
- **Range empty** (`LAST_SHA` points at `HEAD`): no new commits since last review. Treat as Case 3 re-verify with no new content; do not re-extract claims.

Detection pattern:

```bash
LAST_SHA=$(bash .claude/commands/_common/scripts/pinned-comment.sh last-reviewed-sha --pr "$PR_NUMBER")
if [[ -z "$LAST_SHA" ]] || ! git rev-parse --verify "$LAST_SHA^{commit}" >/dev/null 2>&1; then
    DIFF=$(gh pr diff "$PR_NUMBER")
    FALLBACK_REASON="no valid last-reviewed-sha"
else
    DIFF=$(gh pr diff "$PR_NUMBER" --range "$LAST_SHA..HEAD")
    FALLBACK_REASON=""
fi
```

The CI runner's checkout is shallow, so `git rev-parse --verify` may also fail on reachable but un-fetched SHAs. Treat any verification failure as "unreachable" and fall back to full diff; the cost is one extra full-file pass, not correctness.

---

## Draft-PR handling

When `gh pr view` reports `isDraft: true`, **prepend** the pinned-comment body with a one-line italic note:

> *Reviewing a draft; findings may change as you iterate.*

Explicit `@claude` mention on a draft is explicit consent to run, so the skill does not abort -- but the author should not be surprised that findings surface on still-evolving content. The note is removed automatically on the next re-entrant run once the PR is marked Ready for review.

---

## Three cases

Decide which case applies *before* re-running fact-check or extracting new claims. Misclassifying wastes a model run and produces noisy output.

### Case 1 — fix-response

The author pushed commits that look like fixes for the previous 🚨 Outstanding findings. Signals:

- New commits since the previous review.
- (Optional) A mention like "I fixed the X you flagged" or "addressed feedback."

**Action:**

1. Re-verify each previously-outstanding finding against the new diff. For each:
   - Resolved → move to ✅ Resolved since last review (with commit SHA reference)
   - Still present → keep in 🚨 Outstanding
   - Worse → keep in 🚨 Outstanding with a note ("recurs after the latest commit")
2. Extract any *new* findings introduced by the new commits. Apply the domain rules.
3. Append a 📜 Review history line: `<timestamp> — re-reviewed after fix push (<commit count> new commits, <SHA>)`.

**Sonnet failure-mode example to avoid:**

> Finding X was posted in the previous review; the author pushed commit abc123 that addresses it.
>
> ❌ *Do not:* repost X as an outstanding finding with a note saying "previously flagged; looks addressed but confirming."
> ✅ *Do:* strike X through in the previous render, move it to ✅ Resolved with `(resolved in abc123)`, and leave 🚨 Outstanding narrower than before.

The bucket update is the communication. The reader sees fewer 🚨 items and more ✅ items; they do not need a prose recap.

### Case 2 — dispute

The author or another reviewer pushed back on a previous finding *without* a fix push. Signals:

- A mention like "I disagree with X" / "this is intentional" / "the linter passes, why are you flagging this?"
- No new commits, or commits unrelated to the disputed finding.

**Action:**

1. Re-examine the disputed finding against the **current** diff and any cited evidence in the mention.
2. If the author is right -- concede cleanly. Move the finding from 🚨 Outstanding to ✅ Resolved since last review with a brief "concede: <reason>" annotation.
3. If the author is wrong -- keep the finding and add a short reply paragraph to the 📜 Review history explaining why, with the evidence (file:line, command output, gh URL).
4. **Do not** reword the same finding hoping it lands better. The original wording is in the comment; either change your mind or explain why you didn't.

**Sonnet failure-mode example to avoid:**

> Author mentioned Claude saying: "you flagged X but it's fine because Y."
>
> ❌ *Do not:* reword the finding ("Consider that X may cause issues in scenario Z"), leave it in 🚨 Outstanding, and hope the rewording lands better than the original.
> ✅ *Do* one of two things:
>
> - **Concede cleanly:** "concede: author is right about Y; moving to ✅ Resolved."
> - **Hold the finding:** "holding: Y does not address X because <one-sentence reason>; evidence at <file:line>."
>
> Reword is the forbidden path. A finding is either in the bucket or out; a "softer rephrasing" is neither and is the worst output under a cheaper model.

### Case 3 — re-verify

A `@claude` mention with no specific request, or a generic "please re-review." Signals:

- Mention body is short and non-specific ("/claude refresh" / "@claude take another look").
- New commits may or may not be present.

**Action:**

1. If new commits → run as Case 1 (fix-response).
2. If no new commits → re-verify the existing 🚨 Outstanding findings only (don't re-extract from scratch). For each finding still applicable, leave in place; for each no longer applicable, move to ✅ Resolved.
3. Append 📜 Review history: `<timestamp> — re-verified on request (<author>)`.

**Sonnet failure-mode example to avoid:**

> Previous review had 3 outstanding findings (A, B, C). Author pushed no commits, no new mention beyond "@claude refresh."
>
> ❌ *Do not:* list A, B, C again as a new narrative ("I re-reviewed the PR. The following findings remain: A, B, C."). They are already visible in the pinned comment. Repeating them is the noisiest possible output.
> ✅ *Do:* append one 📜 Review history line ("<timestamp> — re-verified; 3 outstanding unchanged") and update the timestamp at the top of the 1/M comment. That is the full output. The bucket contents do not change.

Alternative ✅ path: if the re-verify surfaces something the previous review missed, add the new finding to 🚨 Outstanding. Do not also repeat A, B, C.

---

## What this skill must NOT do

- **Do not restate previously-Outstanding findings in the new run's narrative.** They're already visible in the 1/M comment; repeating them is the noisiest possible output. The bucket update *is* the communication.
- **Do not re-introduce findings the author already responded to** unless the response was wrong AND you have new evidence.
- **Do not delete the 1/M comment.** Always edit in place via the pinned-comment script. The script enforces this; do not work around it.
- **Do not lower scrutiny on disputed findings just because the author disputed them.** Concede on evidence, not on tone.
- **Do not rerun fact-check from scratch when the diff hasn't changed.** Reuse the previous results; only re-verify claims affected by new commits.
- **Do not reword findings as a pseudo-rebuttal.** See Case 2 example.

---

## Output

Hand the updated review object to `_common/docs-review-core.md`'s output format. The 1/M comment's content reshapes accordingly:

- 🚨 Outstanding shrinks (or grows on regressions)
- ✅ Resolved fills in
- 📜 Review history gains one line
- Status counts at the top update
- Draft-PR note (if applicable) appears at the top

Then post via `pinned-comment.sh upsert`:

```bash
bash .claude/commands/_common/scripts/pinned-comment.sh upsert \
  --pr "$PR_NUMBER" \
  --body-file "$REVIEW_OUTPUT_FILE"
```

`upsert` is the only posting path for re-entrant runs. The script edits the existing 1/M comment in place, appends overflow N/M comments, and prunes any stale tail. **Never** call `gh pr comment` directly from this skill; the pinned-comment script is the single source of truth for the comment sequence.

---

## Fallback — pinned comment is missing

If `pinned-comment.sh fetch` returns nothing -- author deleted the comment, history was rewritten, or this is a freshly transitioned PR that somehow skipped the initial review -- fall back to a full initial review using [`docs-review-ci.md`](../docs-review-ci.md) and post fresh. The new comment lands at the bottom of the timeline; not ideal, but recoverable.

---

## Known quirks

Documented here so they aren't "fixed" into new bugs by a future session.

### `@claude` mentions on issues (not PRs)

When a `@claude` mention lands on a GitHub **issue** (not a PR), `claude.yml`'s prompt evaluates to an empty string. The `claude-code-action` interprets an empty prompt as "execute the comment body's instructions," which is the original behavior for issue Q&A use cases. Do **not** "fix" this by adding a non-empty default prompt; that would break the issue-mention path. The re-entrant pipeline is PR-only by construction (it looks for `pull_request.*` context); issue mentions never reach this skill.

### Author deletes the 1/M pinned comment

The pinned-comment script refuses to delete the 1/M comment (index 0 is sacrosanct inside the script). If the *author* deletes it via the GitHub UI, the next re-entrant run's `pinned-comment.sh fetch` returns empty, and the skill falls through to the Fallback path above -- a fresh post at the bottom of the timeline. Recoverable but ugly. Not worth a second-anchor architecture for v1; the incidence rate is low and the rebuild is self-serve.

### Stale labels on long-running drafts

Triage runs on `opened` / `reopened` / `ready_for_review`, not on `synchronize`. A draft PR that sits through many commits and shifts domain (e.g., a docs PR that later grows to touch `static/programs/`) will have stale labels until the next ready-transition, at which point re-triage fixes them. Acceptable for v1; the review skill is not run during this interval, so the stale labels don't produce wrong output, just wrong filters in the GitHub UI.
