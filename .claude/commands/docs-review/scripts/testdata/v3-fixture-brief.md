<!-- CLAUDE_REVIEW_BRIEF -->
## Reviewer's guide v1 — not for the author

> [!TIP]
> **This is the reviewer's guide.** Before you approve this PR, work through the ⚠️ checklist below. Everything else was machine-verified — the evidence page has the receipts.
>
> _PR author: your to-do list is the other review comment, "Author action guide" — nothing on this card is yours._

> [!NOTE]
> **Summary:** <TODO: one paragraph — (1) what this PR is (content type + subject; for a new page, which existing pages it parallels), (2) what specific kind of wrongness would block a reader's success, (3) which investigative passes ran>.
>
> **Review confidence:**
>
> | Dimension | Level | Notes |
> | :--- | :---: | :--- |
> | mechanics | <TODO: HIGH/MEDIUM/LOW> | <TODO: short note when not HIGH; leave empty when HIGH> |
> | facts | <TODO: HIGH/MEDIUM/LOW> | <TODO: short note when not HIGH; leave empty when HIGH> |

### ⚠️ Check these before approving

| | ID | Where | Finding |
|---|---|---|---|
| ⬜ | **F4** | [`content/docs/iac/x.md` L95](https://github.com/pulumi/docs/blob/aaaabbbbccccddddeeeeffff0000111122223333/content/docs/iac/x.md#L95) | *"Most users adopt ESC within a week"* — verdict: framing-drift; framing: widened denominator <TODO: this is a `framing-drift` finding — the anchor value is accurate but the claim's published meaning differs from what the source supports (see the framing note). Write the fix as a quote-and-rewrite that restores the source's framing (scope, denominator, tense, qualifiers). PROMOTE to 🚨 Outstanding if the drifted phrasing also appears in `social.*` frontmatter (it auto-posts on merge) or would materially mislead a reader; rewrite as `**Spurious:** <reason>` only if the framing comparison itself is wrong.> |

### ✅ What you can rubber-stamp

- **Facts:** 2 of 5 factual claims machine-verified (1 unverifiable and 1 contradicted are filed with the author above/on the author card) — [trail](%%EVIDENCE_URL%%#trail).
- **Mechanics:** frontmatter sweep ran — [investigation log](%%EVIDENCE_URL%%#investigation-log).
- **Style:** 1 advisory suggestion(s) left with the author; never blocking.

💡 **Pre-existing issues in touched files:** 0 — [evidence page](%%EVIDENCE_URL%%#preexisting).

📎 **Full evidence:** %%EVIDENCE_URL%%

<sub>v1 · updated 2026-08-31T18:00:00Z · head aaaabbbb</sub>

<!-- CLAUDE_REVIEW_FOOTER -->

---

**For the reviewer:** the ⚠️ items above are the minutes that matter — the rest of this PR's review is machine-verified and linked from the evidence page. The author's open action items live on their own card (the comment headed "Author action guide"); merge is blocked until they answer those, so you don't need to police them. Approving this PR asserts the ⚠️ items looked right to you. If something here seems off, comment on the PR — `@claude #update-review` re-adjudicates with your input.
