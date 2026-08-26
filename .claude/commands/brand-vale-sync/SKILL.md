---
name: brand-vale-sync
description: Weekly drift check of the offline Vale mirror (styles/Pulumi/) against the Pulumi brand guide served by the brand MCP server, with deprecated/retired terms as the priority. Opens a draft PR when the mirror has fallen behind; updates only the sync manifest when it hasn't. Invoked by the brand-style-sync workflow; also user-invocable for an on-demand check.
---

# Brand → Vale sync review

The Vale rules under `styles/Pulumi/` are an **offline mirror** of the
mechanically enforceable subset of the Pulumi brand guide. The brand guide —
served by the **`pulumi-brand` MCP server** (`https://brand.pulumi.com/mcp`) —
is the source of truth; the mirror only follows. Your job: detect where the
mirror has drifted behind the guide, and open a PR that catches it up.

**If the brand MCP server is unreachable, stop and fail loudly.** Do not
guess at the guide's contents from memory or from cached prose in this repo —
a sync against a hallucinated source is worse than no sync.

## Scope

`styles/Pulumi/BRAND-SYNC.yaml` is the manifest: it maps each mirrored Vale
rule to the brand section and subsection it tracks, and records `last_synced`.
Rules **not** listed there (AI-drafting tells, Hugo mechanics, repo
conventions) are repo-owned — never "sync" them against the guide, and never
edit the brand guide side of anything (that's `pulumi/marketing-web`).

## Process

1. **Load the manifest** (`styles/Pulumi/BRAND-SYNC.yaml`).
1. **Pull each brand section it references** via the MCP server:
   `get_guidelines({section: "terminology"})`, `writing-style`, and `voice`.
1. **Compare, rule by rule.** For each manifest entry, read the Vale rule file
   and check the guide content it mirrors. You are looking for:
   - **Retired terms the mirror doesn't know** — a row in the terminology
     section's "Retired and disallowed names" table with no corresponding
     entry in `Substitutions.yml` (replacement right in every context),
     `RetiredNames.yml` (replacement usually right, message hedges), or
     `DeprecatedProductNames.yml` (no single fixed replacement) — nor an entry
     in the "Intentionally unmirrored" block at the top of `BRAND-SYNC.yaml`,
     which records the rows that deliberately have no rule and why. Check all
     four before reporting a gap. This is the highest-value check: renamed
     products rot fastest.
   - **Renamed or re-cased canonical names** — a "Product names" row that
     `Nomenclature.yml` mis-canonicalizes or misses.
   - **Mirror entries the guide no longer supports** — a swap or token whose
     brand rule was changed or dropped. Flag these for removal.
   - **Stale rule `message:`/`link:` text** that misquotes the guide.
1. **Judge before you write.** The mirror is deliberately narrower than the
   guide: only near-zero-false-positive, mechanically checkable rules belong
   in it (see the admission criteria in
   `.claude/commands/docs-review/scripts/vale-deterministic-fixes.yaml`).
   A guide rule with no safe regex (e.g. "runtime code" → "function
   serialization", where *runtime* has too many live meanings) is **correctly
   absent** — note it in the PR body as intentionally unmirrored rather than
   forcing a noisy rule. When adding a retired name, decide the tier:
   - single fixed replacement, right in every context → `Substitutions.yml`
     (auto-fixable, blocker)
   - replacement usually right, but the guide's carve-outs apply (historical
     prose, or a name mapping to more than one current term) →
     `RetiredNames.yml` (auto-fixable, blocker; the message asks the reader to
     confirm the swap fits the sentence)
   - no single fixed replacement → `DeprecatedProductNames.yml` (flag-only,
     blocker)
   - no safe regex at all → leave unmirrored and note it in the PR body

   All four tiers block. The tier decides how much the message hedges, not
   whether the finding may ship — `BRAND-SYNC.yaml` carries the same rule.
1. **Validate.** Run Vale (`make lint-prose ARGS=<a couple of touched content
   files>` or `vale` on a scratch fixture exercising each new/changed token,
   positive and negative cases) to prove the rules compile and match as
   intended. Run `make lint`.
1. **Report.**
   - **Drift found:** update the rule files and `BRAND-SYNC.yaml`
     (`last_synced` + any mapping changes), and open a **draft PR** titled
     `vale: sync brand-guide mirror (<date>)`. The body must list every
     change as *guide says X → mirror said Y → now Z*, plus the
     intentionally-unmirrored notes. Draft, not ready: tier placement
     (blocker vs. advisory) is a human call.
   - **No drift:** commit only the `last_synced` bump in `BRAND-SYNC.yaml`
     directly to a PR the same way (a one-line draft PR is fine and cheap to
     merge), or if invoked interactively, just report "in sync".
   - Never push to `master` directly.
