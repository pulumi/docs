<!-- CLAUDE_REVIEW_BRIEF -->
## Reviewer's guide v1 — not for the author

> [!TIP]
> **This is the reviewer's guide.** Work through the ⚠️ checklist below, then approve — **approving asserts only that the ⚠️ items looked right to you.** Machine-verified this run: links, shortcodes, page metadata, and every claim marked verified (receipts on the evidence page). Code samples are read, not compiled.
>
> _PR author: your to-do list is the other review comment, "Author action guide" — nothing on this card is yours._

**Approval needed from:** @pulumi/docs-guild — any member's approval satisfies the merge gate.

<!-- AUTHOR_STATE_BEGIN -->
**Waiting on the author** — 3 items block merge from the author's own card; you don't need to police them, but check the final diff shows them answered before you approve:

| ID | State | Claim |
|---|---|---|
| **F1** | 🚨 open | The esc CLI defaults to JSON output |
| **F2** | 🚨 open | [style-blocker] terminology: Use 'Pulumi Cloud', not 'Pulumi Service' |
| **F3** | ❓ open | Many teams reduce costs by 40% using this pattern |
<!-- AUTHOR_STATE_END -->

> [!NOTE]
> **What this PR changes:**
>
> - <TODO: one bullet per meaningful change — subject + what changed, one line each; a reviewer scans this list, so no compound bullets>
>
> <TODO: one sentence — what specific kind of wrongness would block a reader's success — then one sentence naming which investigative passes ran>.
>
> **Review confidence:**
>
> | Dimension | Level | Notes |
> | :--- | :---: | :--- |
> | mechanics | <TODO: HIGH/MEDIUM/LOW> | <TODO: short note when not HIGH; leave empty when HIGH> |
> | facts | <TODO: HIGH/MEDIUM/LOW> | <TODO: short note when not HIGH; leave empty when HIGH> |

### ⚠️ Check these before approving

| ID | Where | Finding |
|---|---|---|
| **F4** | [`content/docs/iac/x.md` L95](https://github.com/pulumi/docs/pull/999/files#diff-cadd3dace25e9e98ed0e94a7abf3fcd307fa70d888eef7825198f038022a4dc8R95) | *"Most users adopt ESC within a week"* — verdict: framing-drift; framing: widened denominator <TODO: this is a `framing-drift` finding — the anchor value is accurate but the claim's published meaning differs from what the source supports (see the framing note). Write the fix as a quote-and-rewrite that restores the source's framing (scope, denominator, tense, qualifiers). PROMOTE to 🚨 Outstanding if the drifted phrasing also appears in `social.*` frontmatter (it auto-posts on merge) or would materially mislead a reader; rewrite as `**Spurious:** <reason>` only if the framing comparison itself is wrong.> |

_Not your area? Any member of @pulumi/docs-guild can approve — hand it off rather than approving on faith._

### ✅ What you can rubber-stamp

- **Facts:** 5 factual claims checked — 2 verified clean, 2 open on the author's card ("Waiting on the author" above), 1 flagged in the ⚠️ list.
- **Mechanics:** frontmatter sweep ran.
- **Style:** 1 advisory suggestion(s) left with the author; never blocking.

💡 **Pre-existing issues in touched files:** 0 — details on the evidence page.

📎 **Full evidence:** [verification trail, investigation log, review history](%%EVIDENCE_URL%%).

<sub>Review v1 · updated 2026-08-31T18:00:00Z · head commit aaaabbbb</sub>

<!-- CLAUDE_REVIEW_FOOTER -->

---

**For the reviewer:** the ⚠️ items above are the minutes that matter — the receipts for everything machine-verified are on the evidence page. The author's open items live on their own card (the comment headed "Author action guide"); while any are open, a **Waiting on the author** list above tracks them, and merge stays blocked until they're answered. If something here seems off, comment on the PR — `@claude <your point> #update-review` re-adjudicates with your input.
