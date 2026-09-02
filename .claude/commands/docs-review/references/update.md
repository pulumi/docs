---
user-invocable: false
description: Re-entrant docs review. Updates the existing pinned review in place using the previous comment(s) and new commits.
---

# Update Review (re-entrant)

Shared primitive for "previous review + new commits/mention = updated review." Edit the existing pinned-comment sequence in place; a fresh post happens only via the Fallback path.

---

## Inputs

- `PR_NUMBER`
- (Optional) `MENTION_BODY` -- the text of the `@claude` mention that triggered the run, when applicable
- (Optional) `MENTION_AUTHOR` -- the GitHub username who left the mention

The skill loads everything else for itself:

```bash
# Previous review (the pinned comment sequence)
bash .claude/commands/docs-review/scripts/pinned-comment.sh fetch --pr "$PR_NUMBER"
# Returns the full body of every CLAUDE_REVIEW N/M comment, in order, separated by markers.

# Diff since the last review.
#
# NOT `gh pr diff --range` — that flag does not exist, so the call failed with
# "unknown flag" on every invocation and this lane silently re-read the whole
# PR every time. The compare API also works under CI's shallow checkout, which
# a local `git diff "$LAST_SHA..HEAD"` would not.
#
# Branch on `.status`, NOT on the exit code. A force-pushed-away commit usually
# still exists in the repo network, so comparing against it returns HTTP 200
# with status "diverged" — only a SHA GitHub has never seen 404s. Keying the
# force-push fallback on a non-zero exit would therefore never fire it.
LAST_SHA=$(bash .claude/commands/docs-review/scripts/pinned-comment.sh last-reviewed-sha --pr "$PR_NUMBER")
HEAD_SHA=$(gh pr view "$PR_NUMBER" --json headRefOid --jq .headRefOid)
CMP=$(gh api "repos/{owner}/{repo}/compare/$LAST_SHA...$HEAD_SHA" 2>/dev/null || echo '')
STATUS=$(printf '%s' "$CMP" | jq -r '.status // empty')

case "$STATUS" in
  identical)  : ;;   # no new commits — Range-empty case below
  ahead)
    # Scope to files the PR itself touches. `compare` is three-dot, so when the
    # author rebased or merged master forward between reviews the range also
    # carries master's own commits — reviewing those would raise findings on
    # files the author never touched.
    KEEP=$(gh pr view "$PR_NUMBER" --json files --jq '[.files[].path]')
    printf '%s' "$CMP" | jq -r --argjson keep "$KEEP" '
      .files[] | select(.filename as $f | $keep | index($f))
      | "--- \(.filename)\n\(.patch // "(no patch: binary, or file too large)")"'
    ;;
  *)          : ;;   # diverged / behind / empty → history rewritten; see fallbacks
esac

# Current PR state (including draft status)
gh pr view "$PR_NUMBER" --json title,body,isDraft,labels,files,headRefOid,headRefName
```

`last-reviewed-sha` reads the most recent SHA from the 📜 Review history section in the 1/M comment.

### Automated invocation

When `MENTION_AUTHOR` is `auto-refresh`, there is no human mention: the run was dispatched by the auto-refresh gate in claude-code-review.yml because a push touched only lines carried by 🚨 Outstanding findings (deterministically checked by `auto-refresh-gate.py`). Treat the run strictly as **Case 1 (fix-response)** scoped to the outstanding findings and the pushed lines: re-verify each outstanding finding against the new diff, move resolved ones to ✅ Resolved, and flag regressions the push introduced on those lines. Case 2 (dispute) never applies — there is no mention text to adjudicate — and do not re-extract claims or raise findings on content the push did not touch. `auto-refresh` is not a GitHub user; never render it as an `@`-mention.

**Fallback rules when `last-reviewed-sha` is unusable:**

- **Empty output** (history line missing, comment corrupted): fall back to a full `gh pr diff "$PR_NUMBER"` (no range). Treat the whole PR as new content; this is equivalent to starting over.
- **History rewritten** (author force-pushed, so the recorded SHA is no longer an ancestor of HEAD): `.status` comes back `diverged` or `behind` — **not** a 404 and **not** a non-zero exit. GitHub keeps force-pushed-away commits in the repo network, so the compare still succeeds with HTTP 200; only a SHA it has never seen 404s. Fall back to full `gh pr diff "$PR_NUMBER"` and append a 📜 Review history line: `<timestamp> — history rewritten since last review; re-reviewed against HEAD (<SHA>)`. Keying this on the exit code instead of `.status` would mean the fallback never fires and the lane silently reviews a merge-base diff while recording that it reviewed the delta.
- **Range empty** (`LAST_SHA` points at `HEAD`): no new commits since last review. Treat as Case 3 re-verify with no new content; do not re-extract claims.

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
2. **Sweep for unflagged duplicates of any phrase the previous finding quoted.** When a previous finding cited a specific quoted phrase or claim, search the current file for every occurrence of that phrase (or a near-paraphrase) — not just the locations the original finding called out. On Hugo posts, that means body + `meta_desc` + every `social:` sub-key. If an occurrence the original finding missed still matches the verified-false claim, raise it as a new 🚨 finding citing the missed location. Initial reviews can miss frontmatter duplicates; re-entrant is the safety net before merge.
3. Extract any *new* findings introduced by the new commits. Apply the domain rules.
4. Append a 📜 Review history line: `<timestamp> — re-reviewed after fix push (<commit count> new commits, <SHA>)`.
5. Refresh the freshness header of the 1/M comment: the `Last updated <timestamp>` line AND the `<!-- CLAUDE_REVIEW_HEAD <sha> -->` sentinel on the next line, setting the sentinel to the PR head SHA this update reviewed. Label-independent consumers (`/pr-review` Step 2, the review-label-reconcile workflow) compare that sentinel against the live PR head to detect a stale review when a push never fired a `synchronize` event (Copilot-agent and `GITHUB_TOKEN` pushes don't) — a stale sentinel makes a fresh review look outdated, and a missing one downgrades those consumers to timestamp heuristics.

**Failure-mode example:**

> Finding X was posted in the previous review; the author pushed commit abc123 that addresses it.
>
> ❌ *Do not:* repost X as an outstanding finding with a note saying "previously flagged; looks addressed but confirming."
> ✅ *Do:* strike X through in the previous render, move it to ✅ Resolved with `(resolved in abc123)`, and leave 🚨 Outstanding narrower than before.

The bucket update is the communication. The reader sees fewer 🚨 items and more ✅ items; they do not need a prose recap.

**When the "fix" is you implementing a suggested rewrite** (`@claude implement the suggested rewrite …`, or the author asking you to apply a finding's suggestion block): the rewrite was composed against the review's evidence, and that evidence includes the cross-sibling lane, which is a **mismatch detector, not ground truth**. Before pushing, re-check the result against the sibling pages the finding cited (the "per `<sibling>.md` L<a>–<b>" provenance in the suggestion) — read the cited lines, confirm each borrowed clause is true of *this* page's subject, and drop or reword any that isn't. PR #21293 applied a rewrite verbatim and inherited two clauses from `any-terraform-provider.md`, one of them wrong. A rewrite that cites no source for borrowed wording is not ready to implement; ask for the source first.

### Case 2 — dispute

The author or another reviewer pushed back on a previous finding *without* a fix push. Signals:

- A mention like "I disagree with X" / "this is intentional" / "the linter passes, why are you flagging this?"
- No new commits, or commits unrelated to the disputed finding.

**First, classify what kind of dispute this is** — author authority cuts differently depending on the claim:

- **Domain-knowledge assertion** ("I built this and it works because X", "the team decided on this pattern intentionally", "this codebase uses convention Y for reason Z"). The author is asserting context the model can't independently verify. **Default to concede** unless you can cite specific contrary evidence (file/line, command output, gh URL). When the author has write access on the repo and is asserting design intent or codebase context, "I'm the engineer / maintainer" is sufficient evidence on its own — they have access to context the model does not.
- **Verifiable claim** ("this is faster than X", "Y was added in v3.0", "the docs already say this elsewhere"). The dispute is about something measurable or checkable. Author authority does **not** establish the truth here — require actual evidence (link, benchmark, history, file:line) to concede.
- **Reframing of the model's reading** ("you misread the sentence", "the qualifier in the prose bounds the claim"). The model's interpretation is what's at issue, not the underlying fact. Re-evaluate the finding against the cited reading; concede or hold based on whether the new reading is plausible to a docs reader.

**Then act:**

1. Re-examine the disputed finding against the **current** diff and any cited evidence in the mention, using the classification above.
2. If conceding -- move the finding from 🚨 Outstanding to ✅ Resolved since last review with a brief "concede: <reason>" annotation.
3. If holding -- keep the finding **and** annotate it inline so a human reviewer scanning 🚨 Outstanding sees at a glance that it was contested:
   - Append a `🛡️ **Disputed by <author> on YYYY-MM-DD, model held.**` line directly under the finding text (a short one-line summary of why is OK; the full reasoning belongs in 📜 Review history).
   - Add a reply paragraph to 📜 Review history with the full evidence (file:line, command output, gh URL) explaining why the dispute didn't change the verdict. **You must cite contrary evidence to hold on a domain-knowledge dispute** — if the only basis for holding is your own reasoning vs. the author's assertion of authority, concede instead.
   - The Outstanding count does not change.
4. **Do not** reword the same finding hoping it lands better. The original wording is in the comment; either change your mind or explain why you didn't.

**The annotation shapes are machine-scraped.** `scrape-review-outcomes.py` derives the weekly outcome telemetry (fixed / conceded / disputed counts) from the exact `concede: <reason>` and `🛡️ **Disputed by <author> on YYYY-MM-DD, model held.**` forms above — a freelanced variant ("author disputed this", "conceding the point") silently drops the finding out of those counts, and the validator's `outcome-annotation-shape` rule flags it.

**Failure-mode examples:**

> Author (write access) mentions Claude saying: "I built this — the project intentionally uses pattern X because of Y."
>
> ❌ *Do not:* hold the finding because your training-data view of "best practice" disagrees with the author's stated intent. The author has codebase context you do not.
> ✅ *Do:* concede with `concede: author confirms intentional pattern; deferring to repo authority`.

> Author mentions Claude saying: "you flagged X but it's fine because Y."
>
> ❌ *Do not:* reword the finding ("Consider that X may cause issues in scenario Z"), leave it in 🚨 Outstanding, and hope the rewording lands better than the original.
> ❌ *Do not:* leave the finding text untouched and only add a Review history line. The reviewer scrolling Outstanding has no way to know it was contested.
> ✅ *Do* one of two things:
>
> - **Concede cleanly:** move to ✅ Resolved with `concede: author is right about Y`.
> - **Hold the finding** (only with citable contrary evidence): keep in 🚨 Outstanding, append `🛡️ **Disputed by <author> on YYYY-MM-DD, model held.** <one-line reason>` under the finding, and put the full reasoning in 📜 Review history.
>
> Reword is the forbidden path. A finding is either in the bucket or out; a "softer rephrasing" is neither.

### Case 3 — re-verify

A `@claude` mention with no specific request, or a generic "please re-review." Signals:

- Mention body is short and non-specific ("/claude refresh" / "@claude take another look").
- New commits may or may not be present.

**Action:**

1. If new commits → run as Case 1 (fix-response).
2. If no new commits → re-verify the existing 🚨 Outstanding findings only (don't re-extract from scratch). For each finding still applicable, leave in place; for each no longer applicable, move to ✅ Resolved.
3. Append 📜 Review history: `<timestamp> — re-verified on request (<author>)`.

**Failure-mode example:**

> Previous review had 3 outstanding findings (A, B, C). Author pushed no commits, no new mention beyond "@claude refresh."
>
> ❌ *Do not:* list A, B, C again as a new narrative ("I re-reviewed the PR. The following findings remain: A, B, C."). They are already visible in the pinned comment. Repeating them is the noisiest possible output.
> ✅ *Do:* append one 📜 Review history line ("<timestamp> — re-verified; 3 outstanding unchanged") and update the timestamp at the top of the 1/M comment (plus the `<!-- CLAUDE_REVIEW_HEAD -->` sentinel when the head moved). That is the full output. The bucket contents do not change.

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

Hand the updated review object to `docs-review:references:output-format`. The 1/M comment's content reshapes accordingly:

- 🚨 Outstanding shrinks (or grows on regressions)
- ✅ Resolved fills in
- 📜 Review history gains one line
- Status counts at the top update
- Draft-PR note (if applicable) appears at the top

Then post via `pinned-comment.sh upsert`:

```bash
bash .claude/commands/docs-review/scripts/pinned-comment.sh upsert \
  --pr "$PR_NUMBER" \
  --body-file "$REVIEW_OUTPUT_FILE"
```

`upsert` is the only posting path for re-entrant runs. The script edits the existing 1/M comment in place, appends overflow N/M comments, and prunes any stale tail. **Never** call `gh pr comment` directly from this skill; the pinned-comment script is the single source of truth for the comment sequence.

---

## Fallback — pinned comment is missing

If `pinned-comment.sh fetch` returns nothing -- author deleted the comment, history was rewritten, or this is a freshly transitioned PR that somehow skipped the initial review -- fall back to a full initial review using `docs-review/ci.md` and post fresh.

---

## Known quirks

### Author deletes the 1/M pinned comment

If the author deletes the 1/M comment via the GitHub UI, the next re-entrant run's `pinned-comment.sh fetch` returns empty and the skill falls through to the Fallback path above.

---

## The v3 surface — adjudicate, don't render

> Everything above this line is the **v2** contract (single pinned sequence,
> model renders and self-publishes). On a PR whose review is v3 (an author
> card marked `<!-- CLAUDE_REVIEW_AUTHOR -->` plus a reviewer brief), the
> update lane inverts: **the model adjudicates and writes one structured
> patch; deterministic tooling renders and publishes.** The model never
> upserts, never edits the cards, and never touches the evidence.

### The patch — `.review-update.json`

```json
{"schema": 1, "case": "fix-response|dispute|re-verify|mixed",
 "history_summary": "one line for the evidence history (≤120 chars)",
 "findings": [
   {"id": "F3", "action": "resolve", "annotation": "fixed in a1b2c3"},
   {"id": "F4", "action": "concede", "reason": "author is right about X"},
   {"id": "F5", "action": "hold",    "reason": "evidence: the docs say otherwise"},
   {"id": "F8", "action": "accept",  "reason": "author: internal figure, shipping as-is", "bulk": false},
   {"id": "F6", "action": "promote", "to": "outstanding", "reason": "also in social copy"},
   {"id": "F7", "action": "retext",  "text": "sharper wording, same finding",
    "detail": {"why": "1-2 sentences", "fix": "exactly ONE action", "keep": "optional fallback"}},
   {"action": "add", "bucket": "outstanding|author-answer|reviewer-check",
    "file": "content/docs/x.md", "lines": [10, 12], "text": "…", "origin": "model"}
 ]}
```

Closed action set — `apply-update.py` rejects anything else (exit 2):

| Action | Meaning | Rendered as | REVIEW_STATE |
|---|---|---|---|
| `resolve` | the push fixed it (verify against the diff) | row → ✅ Resolved with the annotation | `fixed` (actor `update-lane`, sha) |
| `concede` | the model concedes the finding was wrong | row → ✅ with `concede: <reason>` — the exact v2 machine-scraped shape | none — the annotation is the record |
| `hold` | the author answered; the model still disagrees | row **moves to the brief's ⚠️ list** with `🛡️ **Disputed by <actor> on YYYY-MM-DD, model held.** <reason>` — a judgment call for the human reviewer; its Do-this block drops | `refuted` (actor = the disputing author, note = your reason) — **it stops blocking merge**, as the author card promises |
| `accept` | the mention accepts the finding as-is (the author card's third verb; `bulk: true` when it accepted everything at once) | row **moves to the brief's ⚠️ list** with `✋ **Accepted as-is by <actor> on YYYY-MM-DD.** <reason>` — the reviewer weighs a knowingly-shipped finding | `accepted` (actor, note = the author's reason, `bulk`) — stops blocking |
| `promote` | bucket moves **up only** (⚠️ → ❓ → 🚨) | row moves section/card | none |
| `add` | new problem in the pushed lines only | new row, next F-id | none |
| `retext` | wording sharpened on a finding that stays open **on its own merits** | Finding cell replaced (ONE line: claim quote + verdict), id + anchor preserved; optional `detail` `{why, fix[, keep]}` rebuilds the `#### F<n> · Do this` block (verbatim line kept) | none |

The three v2 cases map directly: **Case 1 fix-response** → `resolve` actions
(and `add` for new problems in the pushed lines); **Case 2 dispute** →
`concede` or `hold` (same concession-default for write-access authors'
domain-knowledge disputes); **Case 3 re-verify** → `resolve` / `retext` /
`hold`. A finding the model has nothing to say about gets **no entry** and
carries forward unchanged — silence is not a disposition here, unlike the
author's answer loop.

**An answered item never stays where it was.** When the mention answers what
a ❓ asked (names the source, confirms the intent), disputes a 🚨, or accepts
an item as-is, the author has done their part and the card promised them it
counts: the only legal outcomes are `concede` (the answer settles it —
including "the source is internal, and that's the author's call"), `hold`
(you still disagree, and a human should weigh it), or `accept` (they took
ownership; you don't adjudicate an acceptance). Never `retext` a finding to restate the ask
with the author's reply folded in — that keeps them blocked on an item they
already answered, and it was the first live failure of this lane (fork PR
242, 2026-09-01). `retext` is for sharpening a finding that remains open on
its own merits; its cell stays one line, and any changed action goes in
`detail.fix`. Residual edits the author volunteered ("I'll attribute it
inline") are theirs to make, not grounds to hold.

### What the deterministic side does

`claude-update.yml`'s publish step re-fetches the LIVE author card (merging
any `/resolve` that landed while the model worked — newest `updated_at`
wins), runs `apply-update.py` (validate patch → apply actions → merge
REVIEW_STATE → refresh header count, `Last updated`, and the
`CLAUDE_REVIEW_HEAD` marker). The `#### F<n> · Do this` detail blocks
follow their rows automatically — apply-update strips them, re-inserts each
under its finding's current section, and drops the block when its row
resolves or concedes; the brief's "Waiting on the author" table is
regenerated from the post-application findings + dispositions (a row a
`/resolve` dispositioned stays put but leaves the blocking count on both
cards — `build-evidence.refresh_counts`, which the /resolve lane calls too);
the brief's **Facts** bullet is re-derived from the refreshed evidence
(`refresh_facts_line`: totals fixed at compose time, open/⚠️/settled
recounted); the ✅
Resolved section is inserted on the first resolve (the composer omits it
while empty); a 🔄 re-review banner stamped by the auto-refresh gate is
cleared by the card rewrite (or, on the error path, explicitly); the
brief's `#### Editorial stances` sub-list sits below the ⚠️ table's section
span and comes through verbatim. It then
validates both cards against schema v23,
records the evidence object (prior trail/investigation log/stances carried
forward from S3; `"degraded": "prior-evidence-unavailable"` when it can't be
fetched), re-renders the evidence page, and upserts brief-then-author. Any
failure lands on `review:error` — a half-published pair must never read as
current.

### Auto-refresh runs

`MENTION_AUTHOR == auto-refresh` is strictly Case 1: `apply-update.py`
**drops** `concede`, `hold`, and `add` actions from auto runs with a logged
warning. An unattended refresh may observe fixes; it may not adjudicate
disputes or raise findings.

### Known simplifications

- The v3 refresh does not regenerate advisory style suggestions (the author
  card keeps its style block from the last full compose, and existing
  one-click buttons stand). A full re-style pass is `@claude #new-review`.
- `history_summary` is the only history the lane writes; the card has no 📜
  section — history lives on the evidence page.
