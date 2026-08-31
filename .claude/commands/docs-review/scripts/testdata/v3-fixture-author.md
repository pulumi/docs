<!-- CLAUDE_REVIEW 1/1 -->
<!-- CLAUDE_REVIEW_AUTHOR -->
<!-- CLAUDE_REVIEW_HEAD aaaabbbbccccddddeeeeffff0000111122223333 -->
## Review — action needed (3 blocking) — Last updated 2026-08-31T18:00:00Z

_<TODO: one sentence — what this PR is and what the review checked>_

### 🚨 Must fix or refute (blocks merge)

- [ ] **F1** **[L80-82]** `content/docs/iac/x.md` — *"The esc CLI defaults to JSON output"* — verdict: contradicted <TODO: write the fix / suggestion block for the author (quote-and-rewrite mandate). If you judge the verdict spurious (verifier checked stale data / wrong site / SPA page / missed a PR-local alias / compared a paraphrased version of the claim), rewrite the bullet body as `**Spurious:** <1-2 sentence reason>` — build-evidence files it on the evidence page and drops it from this card (the `**Spurious:**` label IS the resolution). If pre-existing on a line this PR didn't touch, rewrite the bullet body as `**Pre-existing:** <reason>` — it is filed on the evidence page and dropped from this card.>

- [ ] **F2** **[L30]** `content/docs/iac/x.md` — [style-blocker] _terminology_ — Use 'Pulumi Cloud', not 'Pulumi Service'

### ❓ Only you can answer these (blocks merge)

- [ ] **F3** **[L61]** `content/docs/iac/x.md` — *"Many teams reduce costs by 40% using this pattern"* — verdict: unverifiable <TODO: if this is a factual blocker (a price/spec/capability with no citation a reader needs), promote to `### 🚨 Must fix or refute` on the author card; otherwise keep it here — this bullet IS the question the author must answer. REMOVE only if it's not actually a checkable claim (then it should already be `not-a-claim`). If the verifier was demonstrably mis-sourced (wrong URL followed, ran out of turns on a duplicate, the cited URL was unrelated to the claim subject, etc.), rewrite the bullet body as `**Mis-sourced:** <reason>` — it is filed on the evidence page and dropped from this card.>

#### Style suggestions

*Optional polish from pattern-based linting — never blocking, not counted above. Take the ones that read better and ignore the rest. ✏️ marks one you can apply from the [Files changed](https://github.com/pulumi/docs/pull/999/files) tab — use **Add suggestion to batch** on each, then **Commit suggestions** to take several in a single commit.*

##### content/docs/iac/x.md

- **line 33:** [style] _wordiness_ — Consider 'use' instead of 'utilize'

### ✅ Resolved since last review

_No items resolved since the last review._

📎 **Full evidence:** %%EVIDENCE_URL%% — verification trail, investigation log, review history.

<!-- REVIEW_STATE {"findings":{},"high_water":4,"schema":1} -->

<!-- CLAUDE_REVIEW_FOOTER -->

---

**How to answer a finding** — every 🚨 and ❓ item above needs one of these before merge:

1. **Fix it** — push the change; the review refreshes and marks it fixed.
1. **Refute or accept it** — reply on this PR with one line per finding:
   `/resolve F3 refuted: the flag does exist in 3.261`
   Dispositions: `fixed` · `refuted` · `deferred` · `accepted` · `not-applicable` (the last three need a reason after `:`).
1. **Accept everything at once** — `/resolve all accepted: <why>` — you own the PR; saying so is a valid answer.
1. **Argue it out** — comment `@claude #update-review` with your reasoning and the review will re-adjudicate (it may concede, or hold with a 🛡️ note for your reviewer).

Pushing new commits refreshes this review automatically when the changes line up with the findings above; otherwise mention `@claude #update-review`. `@claude #new-review` starts over from scratch. Please don't edit, hide, or delete this comment — it is the review's record. Full mechanics: CONTRIBUTING.md §AI-assisted contributions.
