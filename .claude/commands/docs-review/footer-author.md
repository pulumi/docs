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

Please don't edit, hide, or delete this comment — it is the review's record. Full mechanics: [CONTRIBUTING.md §AI-assisted contributions](%%CONTRIBUTING_URL%%).
