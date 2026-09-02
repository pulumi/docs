<!-- CLAUDE_REVIEW 1/1 -->
<!-- CLAUDE_REVIEW_AUTHOR -->
<!-- CLAUDE_REVIEW_HEAD aaaabbbbccccddddeeeeffff0000111122223333 -->
## Author action guide v1 — 3 items block merge

> [!IMPORTANT]
> **You = the PR author.** This review needs your answers before this PR can merge. Fix each item below, or tell the review why it's wrong — **How to answer** at the bottom shows exactly what to type. Answering unblocks the review; a human reviewer still approves the merge.

_<TODO: one sentence — what this PR is and what the review checked>_

### 🚨 Fix or disagree

| ID | Where | Finding |
|---|---|---|
| **F1** | [`content/docs/iac/x.md` L80-82](https://github.com/pulumi/docs/pull/999/files#diff-cadd3dace25e9e98ed0e94a7abf3fcd307fa70d888eef7825198f038022a4dc8R80) · [✏️ edit](https://github.com/example/docs-fork/edit/fix/component-doc/content/docs/iac/x.md) | *"The esc CLI defaults to JSON output"* — verdict: contradicted <TODO: write the fix / suggestion block for the author (quote-and-rewrite mandate). If you judge the verdict spurious (verifier checked stale data / wrong site / SPA page / missed a PR-local alias / compared a paraphrased version of the claim), rewrite the Finding cell as `**Spurious:** <1-2 sentence reason>` — build-evidence files it on the evidence page and drops it from this card (the `**Spurious:**` label IS the resolution). If pre-existing on a line this PR didn't touch, rewrite the Finding cell as `**Pre-existing:** <reason>` — it is filed on the evidence page and dropped from this card.> |
| **F2** | [`content/docs/iac/x.md` L30](https://github.com/pulumi/docs/pull/999/files#diff-cadd3dace25e9e98ed0e94a7abf3fcd307fa70d888eef7825198f038022a4dc8R30) · [✏️ edit](https://github.com/example/docs-fork/edit/fix/component-doc/content/docs/iac/x.md) | [style-blocker] _terminology_ — Use 'Pulumi Cloud', not 'Pulumi Service' |

#### F1 · Do this

**Line (verbatim):** <TODO: the flagged line, quoted exactly as it appears in the file — the only quote of it on this card; never a paraphrase>
**Why:** <TODO: 1-2 sentences — what is wrong (🚨) or what only the author can settle (❓)>
**Fix:** <TODO: exactly ONE required action, stated first; put any replacement text in a fenced block; label an alternative "**If you'd rather keep it:**" — never two competing imperatives>

#### F2 · Do this

**Line (verbatim):** <TODO: the flagged line, quoted exactly as it appears in the file — the only quote of it on this card; never a paraphrase>
**Why:** <TODO: 1-2 sentences — what is wrong (🚨) or what only the author can settle (❓)>
**Fix:** <TODO: exactly ONE required action, stated first; put any replacement text in a fenced block; label an alternative "**If you'd rather keep it:**" — never two competing imperatives>

### ❓ Questions for you

| ID | Where | Finding |
|---|---|---|
| **F3** | [`content/docs/iac/x.md` L61](https://github.com/pulumi/docs/pull/999/files#diff-cadd3dace25e9e98ed0e94a7abf3fcd307fa70d888eef7825198f038022a4dc8R61) · [✏️ edit](https://github.com/example/docs-fork/edit/fix/component-doc/content/docs/iac/x.md) | *"Many teams reduce costs by 40% using this pattern"* — verdict: unverifiable <TODO: if this is a factual blocker (a price/spec/capability with no citation a reader needs), promote to `### 🚨 Fix or disagree` on the author card; otherwise keep it here — this row IS the question the author must answer. REMOVE only if it's not actually a checkable claim (then it should already be `not-a-claim`). If the verifier was demonstrably mis-sourced (wrong URL followed, ran out of turns on a duplicate, the cited URL was unrelated to the claim subject, etc.), rewrite the Finding cell as `**Mis-sourced:** <reason>` — it is filed on the evidence page and dropped from this card.> |

#### F3 · Do this

**Line (verbatim):** <TODO: the flagged line, quoted exactly as it appears in the file — the only quote of it on this card; never a paraphrase>
**Why:** <TODO: 1-2 sentences — what is wrong (🚨) or what only the author can settle (❓)>
**Fix:** <TODO: exactly ONE required action, stated first; put any replacement text in a fenced block; label an alternative "**If you'd rather keep it:**" — never two competing imperatives>

_Editing in the browser? The ✏️ links open the file in GitHub's editor — Ctrl+F for the quoted line._

#### Style suggestions

*Optional polish from pattern-based linting — never blocking, not counted above. Take the ones that read better and ignore the rest. ✏️ marks one you can apply from the [Files changed](https://github.com/pulumi/docs/pull/999/files) tab — use **Add suggestion to batch** on each, then **Commit suggestions** to take several in a single commit.*

##### content/docs/iac/x.md

- **line 33:** [style] _wordiness_ — Consider 'use' instead of 'utilize'

📎 **Full evidence:** [verification trail, investigation log, review history](%%EVIDENCE_URL%%).

<!-- REVIEW_STATE {"findings":{},"high_water":4,"schema":1} -->
<!-- The block above stores dispositions only; a finding ID absent from it is OPEN. Machines parse the JSON block, not this note. -->

<sub>Review v1 · updated 2026-08-31T18:00:00Z · head commit aaaabbbb</sub>

<!-- CLAUDE_REVIEW_FOOTER -->

---

### How to answer

Every 🚨 and ❓ item above needs one of these before merge:

1. **Fix it** — push the change. If your push lines up with the flagged lines, this card shows a 🔄 banner within a minute and then refreshes itself. No banner? Comment:

   ```text
   @claude I pushed a fix for F1 #update-review
   ```

1. **Disagree with it** — say which item and why; the review re-checks with your input:

   ```text
   @claude F2: <your reasoning — e.g. where the figure comes from> #update-review
   ```

   Either way your answer counts: the review marks the item resolved, or keeps it with a 🛡️ note for your human reviewer to weigh — it stops blocking merge in both cases.

1. **Accept it as-is** — you own the PR; a one-line reason is a valid answer, and your reviewer sees it beside the finding:

   ```text
   @claude F2: accepting as-is — <your reason> #update-review
   ```

   To accept every open item at once: `@claude accepting all open items — <reason> #update-review`.

The `#update-review` hashtag matters — it routes your reply to this review, and (besides pushing a fix) **it is the only reply that unblocks merge**. A bare `@claude` gets you ad-hoc help and leaves this card — and the merge block — untouched.

Please don't edit, hide, or delete this comment — it is the review's record. Full mechanics: [CONTRIBUTING.md §AI-assisted contributions](https://github.com/pulumi/docs/blob/master/CONTRIBUTING.md#ai-assisted-contributions).
