<!-- CLAUDE_REVIEW 1/1 -->
<!-- CLAUDE_REVIEW_AUTHOR -->
<!-- CLAUDE_REVIEW_HEAD aaaabbbbccccddddeeeeffff0000111122223333 -->
## Author action guide v1 — 3 items block merge

> [!IMPORTANT]
> **You = the PR author.** This review needs your answers before this PR can merge. Fix each item in the table below, or tell the review why it's wrong — **How to answer** at the bottom shows exactly what to type.

_<TODO: one sentence — what this PR is and what the review checked>_

### 🚨 Must fix or refute (blocks merge)

| | ID | Where | Finding |
|---|---|---|---|
| ⬜ | **F1** | [`content/docs/iac/x.md` L80-82](https://github.com/pulumi/docs/blob/aaaabbbbccccddddeeeeffff0000111122223333/content/docs/iac/x.md#L80-L82) | *"The esc CLI defaults to JSON output"* — verdict: contradicted <TODO: write the fix / suggestion block for the author (quote-and-rewrite mandate). If you judge the verdict spurious (verifier checked stale data / wrong site / SPA page / missed a PR-local alias / compared a paraphrased version of the claim), rewrite the Finding cell as `**Spurious:** <1-2 sentence reason>` — build-evidence files it on the evidence page and drops it from this card (the `**Spurious:**` label IS the resolution). If pre-existing on a line this PR didn't touch, rewrite the Finding cell as `**Pre-existing:** <reason>` — it is filed on the evidence page and dropped from this card.> |
| ⬜ | **F2** | [`content/docs/iac/x.md` L30](https://github.com/pulumi/docs/blob/aaaabbbbccccddddeeeeffff0000111122223333/content/docs/iac/x.md#L30) | [style-blocker] _terminology_ — Use 'Pulumi Cloud', not 'Pulumi Service' |

### ❓ Only you can answer these (blocks merge)

| | ID | Where | Finding |
|---|---|---|---|
| ⬜ | **F3** | [`content/docs/iac/x.md` L61](https://github.com/pulumi/docs/blob/aaaabbbbccccddddeeeeffff0000111122223333/content/docs/iac/x.md#L61) | *"Many teams reduce costs by 40% using this pattern"* — verdict: unverifiable <TODO: if this is a factual blocker (a price/spec/capability with no citation a reader needs), promote to `### 🚨 Must fix or refute` on the author card; otherwise keep it here — this row IS the question the author must answer. REMOVE only if it's not actually a checkable claim (then it should already be `not-a-claim`). If the verifier was demonstrably mis-sourced (wrong URL followed, ran out of turns on a duplicate, the cited URL was unrelated to the claim subject, etc.), rewrite the Finding cell as `**Mis-sourced:** <reason>` — it is filed on the evidence page and dropped from this card.> |

#### Style suggestions

*Optional polish from pattern-based linting — never blocking, not counted above. Take the ones that read better and ignore the rest. ✏️ marks one you can apply from the [Files changed](https://github.com/pulumi/docs/pull/999/files) tab — use **Add suggestion to batch** on each, then **Commit suggestions** to take several in a single commit.*

##### content/docs/iac/x.md

- **line 33:** [style] _wordiness_ — Consider 'use' instead of 'utilize'

### ✅ Resolved since last review

_No items resolved since the last review._

📎 **Full evidence:** %%EVIDENCE_URL%% — verification trail, investigation log, review history.

<!-- REVIEW_STATE {"findings":{},"high_water":4,"schema":1} -->

<sub>v1 · updated 2026-08-31T18:00:00Z · head aaaabbbb</sub>

<!-- CLAUDE_REVIEW_FOOTER -->

---

**How to answer** — every 🚨 and ❓ item above needs one of these before merge:

1. **Fix it** — push the change; the review refreshes and marks it fixed.
1. **Disagree with it** — reply with your reasoning, e.g.
   `@claude the 40% figure comes from the Q3 interview series #update-review`
   — the review re-adjudicates: it either concedes cleanly or holds with a 🛡️ note for your reviewer.
1. **Accept it and move on** — you own the PR; saying so is a valid answer:
   `@claude I know what I'm doing, mark everything resolved #update-review`
1. **Start over** — flip the PR to draft and back to ready; the review regenerates from scratch.

Pushing new commits refreshes this review automatically when the changes line up with the findings above; otherwise mention `@claude #update-review`. Please don't edit, hide, or delete this comment — it is the review's record. Full mechanics: [CONTRIBUTING.md §AI-assisted contributions](https://github.com/pulumi/docs/blob/master/CONTRIBUTING.md#ai-assisted-contributions).
