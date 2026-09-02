<!-- CLAUDE_REVIEW 1/1 -->
## Pre-merge Review — Last updated 2026-07-07T16:27:09Z

> [!TIP]
> **Summary:** This PR rebalances Pulumi's AI documentation and marketing copy so it presents the full spectrum of AI agents — third-party coding agents (Claude Code, Codex, Cursor, GitHub Copilot) working through Agent Skills and the MCP server, alongside Pulumi Neo — rather than framing Neo as the only path. (Fixture note: captured from pulumi/docs#20079's pinned review for scrape-review-outcomes.py regression tests; the verification-trail evidence text is truncated to a representative subset — the bucket sections, count table, and history are verbatim.)
>
> **Review confidence:**
>
> | Dimension | Level | Notes |
> | :--- | :---: | :--- |
> | mechanics | HIGH | Content-only PR; full Hugo build runs in the deploy job. One pre-existing alias collision noted under 💡. |
> | facts | HIGH | Both prior facts findings (the `--json` overclaim and an unattributed "Many teams" claim) resolved by the two follow-up commits. |
> | cross-sibling consistency | HIGH | Read all four `organizations-teams` siblings; the added "See also" links introduce no inconsistency. |

<details>
<summary>Investigation log</summary>

- **Cross-sibling reads:** 4 of 4 siblings
- **External claim verification:** 69 of 74 claims verified (2 unverifiable, 1 contradicted) · 4 specialists (numerical, cross-reference, capability, framing); 0 cross-specialist corroborations · routed: 0 inline, 69 Pass 1, 0 Pass 2, 5 Pass 3 (verified 4, contradicted 0, unverifiable 1).
- **Cited-claim spot-checks:** not run (no cited claims)
- **Frontmatter sweep:** ran on body + meta_desc
- **Temporal-trigger sweep:** ran (recency words present in diff; spot-check in-review)
- **Code execution:** not run (no `static/programs/` change)
- **Code-examples checks:** not run (no fenced code blocks in content files)
- **Editorial-balance pass:** not run (not under content/blog/)

</details>

| 🚨 Outstanding | ⚠️ Low-confidence | 💡 Pre-existing | ✅ Resolved |
| :---: | :---: | :---: | :---: |
| **0** | **0** | **1** | **2** |

### 🔍 Verification trail

<details>
<summary><strong>75 claims extracted</strong> · <strong>69</strong> verified · <strong>2</strong> unverifiable · <strong>1</strong> contradicted</summary>

- L97 in `AGENTS.md` "Pulumi supports the full spectrum of AI agents…" → ➖ not-a-claim (evidence: internal editorial/positioning guidance, not a falsifiable factual assertion; source: AGENTS.md L97 (self-referential authoring guideline))
- L99 in `AGENTS.md` "- **Docs** (`content/docs/`, `content/what-is/`, `content/tutorials/`): community-centric and balanced…" → ✅ verified (evidence: Confirmed via GitHub API that content/docs/ai/skills/index.md exists; source: gh api repos/pulumi/docs/contents/content/docs/ai/skills)
- L30 in `content/docs/ai/_index.md` "`pulumi do` performs one-shot resource operations." → ✅ verified (evidence: the docs page for `pulumi do` documents direct resource operations; source: repo:content/docs/iac/cli/direct-resource-operations.md)
- L36 in `content/product/neo.md` "Neo is the industry's first AI agent built from the ground up…" → 🤷 unverifiable (evidence: Pulumi's own marketing superlative; no third-party authoritative source; source: gh search code --owner pulumi "industry's first AI agent")
- L205 in `content/docs/ai/skills/index.md` "A page titled 'What is agentic infrastructure?'… exists at /what-is/what-is-agentic-infrast…" → ❌ contradicted (evidence: file listing missed the page; source: gh api repos/pulumi/docs/contents/content/what-is)
- L61 in `content/what-is/what-is-agentic-infrastructure.md` "Many teams use Pulumi Neo for scheduled, longer-horizon infrastructure work…" → 🤷 unverifiable (evidence: unattributed "many teams" usage-pattern claim with no survey/data backing; source: content/docs/ai/skills/index.md)
- L171 in `content/what-is/what-is-agentic-infrastructure.md` "Pulumi Neo accepts natural-language tasks, reasons over your actual infrastructure state graph…" → 🤝 matches (evidence: the same file's workflow walkthrough describes this; source: repo:content/what-is/what-is-agentic-infrastructure.md)
- L55 in `content/what-is/what-is-agentic-infrastructure.md` "The Pulumi CLI can parse structured `--json` output." → ✅ verified (evidence: `46c4df5`/`d0c76f0` dropped the "from every command" quantifier; source: repo:content/docs/iac/cli/commands/pulumi_new.md; repo:content/docs/ai/_index.md L30)
- L1 in `content/docs/_index.md` "frontmatter alias `/docs/reference/` collides with `content/docs/reference/_index.md`" → 🚩 flagged (frontmatter: alias-collision)

</details>

### 🚨 Outstanding in this PR

_No outstanding findings in this PR._

### ⚠️ Low-confidence

_No low-confidence findings._

### 📋 Triaged verifier findings

<details>
<summary><em>I double-checked these and realized they weren't real findings — click to expand</em></summary>

- **[L205]** `content/docs/ai/skills/index.md` — link to `/what-is/what-is-agentic-infrastructure/` flagged as ❌ contradicted (target page reportedly not found). **Spurious:** the page exists — `content/what-is/what-is-agentic-infrastructure.md` is present in the repo (this PR edits it) and resolves to `/what-is/what-is-agentic-infrastructure/`, confirmed by the frontmatter sweep. The verification step's file listing simply missed it.

</details>

### 💡 Pre-existing issues in touched files (optional)

- **[L1]** `content/docs/_index.md` — **Pre-existing:** the frontmatter alias `/docs/reference/` collides with the live page at `content/docs/reference/_index.md` (the real page wins, so the alias is inert). This PR only reorders the section cards and doesn't touch the `aliases` list, so the collision predates it. Worth removing the dead alias in a follow-up, but not this PR's concern.

### ✅ Resolved since last review

- **[L30]** `content/docs/ai/_index.md` / **[L55]** `content/what-is/what-is-agentic-infrastructure.md` — *"…and parse structured `--json` output from every command."* — ✅ resolved: `46c4df5` first scoped the claim to "the commands that emit it," then `d0c76f0` dropped the quantifier entirely rather than hedge it, landing on "parse structured `--json` output" — no more unqualified "every command" for `pulumi new` and other scaffolding commands to contradict.

- **[L61]** `content/what-is/what-is-agentic-infrastructure.md` — *"Many teams use Pulumi Neo for scheduled, longer-horizon infrastructure work and their everyday coding agent for interactive development."* — ✅ resolved: `46c4df5` softened the unattributed "Many teams" adoption claim to "Teams often," removing the implication of measured usage data.

### 📜 Review history

- 2026-07-03T18:55:41Z — Balanced AI-positioning rebalance; flagged one `--json`-from-every-command overclaim, triaged a spurious "page not found" flag and a pre-existing alias collision (f87819a)
- 2026-07-07T16:27:09Z — Re-reviewed after fix push (2 new commits, d0c76f0); both facts findings resolved, 0 outstanding remain

---
Need a re-review? Want to dispute a finding? Mention `@claude` and include `#update-review`.  
(For ad-hoc questions or fixes, just `@claude` — no hashtag.)
