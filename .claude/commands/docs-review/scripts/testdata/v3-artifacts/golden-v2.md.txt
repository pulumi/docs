## Pre-merge Review — Last updated 2026-08-31T18:00:00Z
<!-- CLAUDE_REVIEW_HEAD aaaabbbbccccddddeeeeffff0000111122223333 -->

> [!TIP]
> **Summary:** <TODO: one paragraph — (1) what this PR is (content type + subject; for a new page, which existing pages it parallels), (2) what specific kind of wrongness would block a reader's success, (3) which investigative passes ran>.
>
> **Review confidence:**
>
> | Dimension | Level | Notes |
> | :--- | :---: | :--- |
> | mechanics | <TODO: HIGH/MEDIUM/LOW> | <TODO: short note when not HIGH; leave empty when HIGH> |
> | facts | <TODO: HIGH/MEDIUM/LOW> | <TODO: short note when not HIGH; leave empty when HIGH> |

<details>
<summary>Investigation log</summary>

- **Cross-sibling reads:** not run (not in a templated section)
- **External claim verification:** 2 of 5 claims verified (1 unverifiable, 1 contradicted, 1 framing-drift) · 4 specialists (numerical, cross-reference, capability, framing); 0 cross-specialist corroborations · routed: 0 inline, 3 Pass 1, 1 Pass 2 (verified 1, contradicted 0, unverifiable 0), 1 Pass 3 (verified 0, contradicted 0, unverifiable 1).
- **Cited-claim spot-checks:** 1 of 1 cited claims fetched and compared
- **Frontmatter sweep:** ran on body + meta_desc
- **Temporal-trigger sweep:** not run (no trigger words)
- **Code execution:** not run (no `static/programs/` change)
- **Code-examples checks:** not run (no fenced code blocks in content files)
- **Editorial-balance pass:** not run (not under content/blog/)

</details>

| 🚨 Outstanding | ⚠️ Low-confidence | 💡 Pre-existing | ✅ Resolved |
| :---: | :---: | :---: | :---: |
| **2** | **2** | **0** | **0** |

### 🔍 Verification trail

<details>
<summary><strong>5 claims extracted</strong> · <strong>2</strong> verified · <strong>1</strong> unverifiable · <strong>1</strong> contradicted · <strong>1</strong> framing-drift</summary>

- L12-14 in `content/docs/iac/x.md` "Pulumi supports Python 3.9 and later" → ✅ verified (evidence: setup.py requires >=3.9; source: github.com/pulumi/pulumi setup.py)
- L61 in `content/docs/iac/x.md` "Many teams reduce costs by 40% using this pattern" → 🤷 unverifiable (evidence: WebSearch ran; no source found for the 40% figure)
- L80-82 in `content/docs/iac/x.md` "The esc CLI defaults to JSON output" → ❌ contradicted (evidence: esc env get renders a table by default; --format json is opt-in; source: esc CLI docs)
- L95 in `content/docs/iac/x.md` "Most users adopt ESC within a week" → 🌀 framing-drift (framing: widened denominator; evidence: source says trial users, not most users; source: internal adoption dashboard)
- L101 in `content/docs/iac/x.md` "State is stored encrypted at rest" → 🤝 matches (evidence: security whitepaper section 4; source: pulumi.com/security)

</details>

### 🚨 Outstanding in this PR

*These must be resolved or refuted before merging.*

- **[L80-82]** `content/docs/iac/x.md` — *"The esc CLI defaults to JSON output"* — verdict: contradicted <TODO: write the fix / suggestion block for the author (quote-and-rewrite mandate). If you judge the verdict spurious (verifier checked stale data / wrong site / SPA page / missed a PR-local alias / compared a paraphrased version of the claim), replace the body with `**Spurious:** <1-2 sentence reason>` AND move the bullet to `### 📋 Triaged verifier findings` (do NOT leave it in 🚨; do NOT add `no author action required` / `nothing to fix` codas — the `**Spurious:**` label IS the resolution). If pre-existing on a line this PR didn't touch, replace with `**Pre-existing:** <reason>` AND move to `### 💡 Pre-existing`. `trail-verdict-bucket-promotion` accepts the bullet under 🚨, 📋, or 💡.>

- **[L30]** `content/docs/iac/x.md` — [style-blocker] _terminology_ — Use 'Pulumi Cloud', not 'Pulumi Service'

### ⚠️ Low-confidence

*Review each and resolve as appropriate — these don't block the PR.*

- **[L61]** `content/docs/iac/x.md` — *"Many teams reduce costs by 40% using this pattern"* — verdict: unverifiable <TODO: if this is a factual blocker (a price/spec/capability with no citation a reader needs), promote to 🚨 Outstanding; either way file the author-question buffer line. REMOVE only if it's not actually a checkable claim (then it should already be `not-a-claim`). If the verifier was demonstrably mis-sourced (wrong URL followed, ran out of turns on a duplicate, the cited URL was unrelated to the claim subject, etc.), replace the body with `**Mis-sourced:** <reason>` AND move the bullet to `### 📋 Triaged verifier findings`.>

- **[L95]** `content/docs/iac/x.md` — *"Most users adopt ESC within a week"* — verdict: framing-drift; framing: widened denominator <TODO: this is a `framing-drift` finding — the anchor value is accurate but the claim's published meaning differs from what the source supports (see the framing note). Write the fix as a quote-and-rewrite that restores the source's framing (scope, denominator, tense, qualifiers). PROMOTE to 🚨 Outstanding if the drifted phrasing also appears in `social.*` frontmatter (it auto-posts on merge) or would materially mislead a reader; move to 📋 Triaged with `**Spurious:**` only if the framing comparison itself is wrong.>

#### Style suggestions

*Optional polish from pattern-based linting — never blocking, not counted above. Take the ones that read better and ignore the rest. ✏️ marks one you can apply from the [Files changed](https://github.com/pulumi/docs/pull/999/files) tab — use **Add suggestion to batch** on each, then **Commit suggestions** to take several in a single commit.*

##### content/docs/iac/x.md

- **line 33:** [style] _wordiness_ — Consider 'use' instead of 'utilize'

### 📋 Triaged verifier findings

<details>
<summary><em>I double-checked these and realized they weren't real findings — click to expand</em></summary>

_No triaged findings._

</details>

### 💡 Pre-existing issues in touched files (optional)

_No pre-existing issues in touched files._

### ✅ Resolved since last review

_No items resolved since the last review._

### 📜 Review history

- 2026-08-31T18:00:00Z — <TODO: one-line summary of what this review found> (aaaabbbb)

<!-- CLAUDE_REVIEW_FOOTER -->

---

- **Refresh this review** — comment `@claude #update-review`. Say what you fixed, or which finding you dispute and why; both work in the same mention.
- **Ask for anything else** — comment `@claude` with no hashtag (questions, one-off fixes). Leaves this review untouched.

> [!IMPORTANT]
> Please don't hide, resolve, or delete this comment! It breaks things!

📖 [How pre-merge review works](https://github.com/pulumi/docs/blob/master/CONTRIBUTING.md#after-review--three-paths-to-refresh) — the full lifecycle, short-circuits, and escape hatches.
