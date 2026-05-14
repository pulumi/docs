---
user-invocable: false
description: Docs-review entry point for CI. Diff-only, posts to a pinned PR comment.
---

# Docs Review (CI)

This is the **CI entry point** for the docs review pipeline.

---

## Hard rules for CI

1. **Never read working-tree *source* state.** No `git status`, `git diff` against the local checkout, no `ls`, no Read against arbitrary repo content files. The CI runner's working tree is a shallow checkout that may not reflect what's in the PR. Use `gh pr view` and `gh pr diff` for **everything** about the PR. *(The workflow-generated pre-step artifacts in the workspace root — `.review-draft.md`, `.verified-claims.json`, etc. per Hard rule 7 — are not "working-tree source state"; Read them freely.)*
2. **Do not post the pinned comment yourself.** Edit `.review-draft.md` in place and exit when the editorial pass is done. The workflow runs validate / splice / re-validate / upsert as separate steps after your session ends — you do not call `pinned-comment.sh`, `validate-pinned.py`, or any post-processing script from inside your turn. **Every `<TODO:` placeholder must be replaced** before you exit — the validator's `no-todo-tokens` rule fails the body otherwise.
3. **Diffs do not show trailing-newline status.** Do not flag missing trailing newlines from CI; the lint job catches this.
4. **Don't run `make` targets.** No `make build`, `make lint`, `make serve`. Lint and build run in their own jobs.
5. **No file paths from the working tree in findings.** Every `file:line` reference must come from the PR's diff or `gh pr view --json files` output.
6. **No internal-source MCP servers.** Notion and Slack MCP tools are not whitelisted in CI; review output is public. Live code execution beyond `gh` and file reads is unavailable.
7. **Bash patterns the runner sandbox rejects.** Friction patterns the harness blocks regardless of the allow-list — write commands that avoid them. (On the normal path you should not need any of these: the workflow's `compose-review.py` pre-step has already parsed every artifact into `.review-draft.md`; read that, not the JSON.)
   - **Reading or writing under `/tmp/`.** The filesystem-path policy restricts `cat`, `grep`, and output redirection to the runner's working directory. Use the `Read` tool (not Bash `cat`) for any `/tmp/...` path; never redirect output to `/tmp/...`. Workflow-managed pre-step artifacts (`.review-draft.md`, `.fetched-urls.json`, `.editorial-balance.json`, `.vale-findings.json`, `.cross-sibling-discovery.json`, `.frontmatter-validation.json`, `.hugo-build.json`, `.candidate-claims.json`, `.verified-claims.json` — see `docs-review:references:pre-computation`) live in the workspace root and are Bash-accessible.
   - **Shell control flow in Bash (`for`, `while`, `case`, `if`).** The multi-op decomposer rejects loops and conditionals even when each constituent command is allow-listed. For iteration over a list, use a single-line `python3 -c "..."` (allow-listed) or sequential single-op `gh` invocations.
   - **Brace expansion (`{a,b,c}`) and subshell grouping (`(cmd1; cmd2)`).** Both decompose unfavorably; expand the list manually or move the logic to a single-line `python3 -c "..."`.
   - **Multi-line `python3 -c "..."` strings and heredocs.** The `-c` argument must be a *single line* of `;`-separated statements — no embedded newlines, no `python3 <<'EOF' … EOF` heredocs (both are rejected by the multi-op decomposer even though `Bash(python3 -c:*)` is allow-listed). If the logic won't fit on one line, decompose it into separate single-op `python3 -c` / `jq` / `gh` invocations — do **not** write a helper script in the workspace root (`.dump-verdicts.py`, `.build-trail.py`, …): the allow-list only permits `python3 .claude/commands/docs-review/scripts/validate-pinned.py:*`, so an arbitrary `python3 .foo.py` is rejected. Everything you need to parse is already in `.review-draft.md`.

---

## Inputs

The workflow passes these as environment variables:

- `PR_NUMBER` — the PR being reviewed
- `PR_LABELS` — comma-separated list of labels currently on the PR (set by triage)

Route by path-precedence per `docs-review:references:domain-routing`. `PR_LABELS` is informational only.

---

## Procedure

### 1. Pull PR context

```bash
gh pr view "$PR_NUMBER" --json title,body,author,labels,files,additions,deletions,headRefName,baseRefName
gh pr diff "$PR_NUMBER"
```

Treat the diff as the source of truth for what changed. If `--json files` lists a file but the diff doesn't show it (rare — usually a mode-only change), note it but don't invent findings.

**Empty-diff short-circuit.** If `gh pr diff` returns no content (mode-only changes, renames with no content change, or any PR with zero text diff), exit the review with a one-line stdout log (`review: pr=<N> empty-diff skip`) without editing `.review-draft.md`.

### 2. Read the composed draft

The workflow ran `compose-review.py` and wrote **`.review-draft.md`** at the workspace root — an ~80%-assembled review body. **Read it with the `Read` tool.** It already contains, fully assembled and self-consistent:

- the `## Quality Review` header + timestamp;
- the Summary / Review-confidence-table *skeleton* (with `<TODO>` levels and an empty summary paragraph);
- the Investigation-log `<details>` block (all 8 bullets — every one deterministic except the **Cross-sibling reads** count, which is a `0 of N siblings (fan-out runs in-review — replace this count)` placeholder you overwrite);
- the bucket-count table (a *starting point* matching the stub-bullet counts);
- the 🔍 Verification trail — one line per `.verified-claims.json` verdict, verbatim: verdict word, per-verdict emoji (✅ `verified` · 🤝 `matches` · ➖ `not-a-claim` · 🤷 `unverifiable` · ❌ `contradicted` · ⚔️ `mismatch`), evidence pointer, source. **The composed trail is the hard contract — see §3 step 7; do not re-render its lines.**
- the 📊 Editorial-balance Tier 1 (blog only — empty form when `trigger=null`, rich form with section-depth stats + outliers otherwise; Tier 2 vendor/FAQ counts are `<TODO>`);
- the `#### Style findings` block (from `.vale-findings.json`, with the inline-vs-collapse render mode already chosen);
- the empty 💡 / ✅ forms;
- the 📜 Review-history line (timestamp + SHA + `<TODO: one-line summary>`);
- stub 🚨 / ⚠️ bucket bullets — one `**[L…]**`-prefixed bullet per *promoting* verdict (`contradicted`/`mismatch` → 🚨; `unverifiable` and low-confidence `verified` → ⚠️), each carrying the claim text + evidence pointer + a `<TODO>` marker. When a section has findings it opens with an italic guidance one-liner under the heading (`*These must be resolved or refuted before merging.*` for 🚨 Outstanding; `*Review each and resolve as appropriate — these don't block the PR.*` for ⚠️ Low-confidence) — same pattern as `*Found by pattern-based linting; Findings may be false positives.*` under `#### Style findings`.

**Do NOT rebuild any of these from scratch. Do NOT re-parse `.verified-claims.json` / `.candidate-claims.json` / `.vale-findings.json` / `.editorial-balance.json` — the draft is the parsed view.** Do NOT call `python3 -c` to slice artifacts. Do NOT re-dispatch the claim-finder subagents — extraction already happened.

**If `.review-draft.md` is absent, or its first lines are a `> [!CAUTION]` composer-failed banner**, ignore the draft entirely and assemble the review manually per **§Fallback** below.

### 3. Your editorial pass

Edit the draft (the composer ASSEMBLES; you JUDGE). Each numbered step below is wrapped in a `<step>` tag for structural anchoring — work through them in order.

**Bucket-transition vocabulary (used by steps 1 + 2).** Every `- **[L<line>]**` stub bullet has four possible outcomes; the `**Spurious:** / **Mis-sourced:** / **Pre-existing:**` label IS the resolution — never add a `No author action required` / `nothing to fix` / `the link is correct` coda after one.

- Keep in **🚨 Outstanding** — actionable; replace the `<TODO: …>` with the fix prose / suggestion block (quote-and-rewrite mandate; anti-hedge mandate for `⚔️ mismatch`). Default for `contradicted` / `mismatch` / Hugo preflight / frontmatter preflight.
- Move to **📋 Triaged verifier findings** with `**Spurious:** <reason>` — verifier got it wrong (stale data, wrong site, SPA page, paraphrased claim, ran out of turns on a duplicate). Applies to fact-check verdicts only; not preflight.
- Move to **📋 Triaged verifier findings** with `**Mis-sourced:** <reason>` — same shape as Spurious but applies to `unverifiable` ⚠️ entries (wrong URL followed, cited URL unrelated to claim subject, etc.).
- Move to **💡 Pre-existing issues in touched files** with `**Pre-existing:** <reason>` — already broken on a line this PR didn't touch (or, for frontmatter preflight, a PR-internal rename whose collision is intentional and announced).

`trail-verdict-bucket-promotion` accepts any of 🚨, 📋, or 💡 for `contradicted` / `mismatch` trail verdicts — you may NOT delete a stub bullet outright (only move it). REMOVE is allowed for ⚠️ `not-a-claim` cases and for preflight stubs that the reviewer confirms are CI-environment noise (then decrement the count cell).

<step number="1" name="Triage stub bucket bullets">
For each `- **[L…]**` `<TODO>`-marked bullet under 🚨 / ⚠️, apply the bucket-transition vocabulary above. 🚨 stubs come from `contradicted` / `mismatch` trail verdicts (or from preflight Hugo / frontmatter pre-stubs — see step 2). ⚠️ stubs come from `unverifiable` or low-confidence `verified`. The principle: 🚨 stays meaningful for a future merge-gate — only things the author must address before merging.
</step>

<step number="2" name="Add findings the composer couldn't pre-stub">
Hugo-build errors / link-integrity breaks and frontmatter alias/URL/menu-parent collisions are now pre-stubbed by the composer (route: `preflight`); their bullets carry a `<TODO: confirm or REMOVE …>` marker — confirm the fix or REMOVE per the bucket-transition vocabulary. **Add** the rest: internal-link / shortcode breaks in content, cross-sibling mismatches (from your in-review sibling-read fan-out — `docs-review:references:fact-check` §Cross-sibling consistency), code-examples findings (3-specialist checks), editorial-balance threshold flags (Tier 2 + Tier 1 outliers from §📊), intuition-flag promotions, two-question-test findings from the domain rules.

Every `**[L<line>]**` bucket bullet you ADD MUST be backed by a matching 🔍 trail line (`bucket-bullet-trail-match` / `bucket-bullet-line-range-prefix` enforce this — a missing anchor soft-floors the review). Render the file path as a backticked literal after the L-prefix: `- **[L45]** ` `content/docs/foo/_index.md` ` "claim text" — …`; the trail line uses `- L45 in ` `content/docs/foo/_index.md` ` "…"`. If the finding has no fact-check claim behind it, add its trail line first (`- L<line> in ` `path` ` "<short description>" → <emoji> <verdict>` — `⚔️ mismatch` for cross-sibling, `🤷 unverifiable` for an editorial-balance flag, etc.). Findings with no line anchor at all go in prose elsewhere — not in a `**[L…]**` bullet.
</step>

<step number="3" name="Fill cross-sibling investigation-log count">
Replace `0 of N siblings (fan-out runs in-review — replace this count)` with the actual `X of N siblings` from your fan-out (or carried-forward count on a re-entrant run).
</step>

<step number="4" name="Write Summary + Review-confidence table">
Fill the `<TODO>` summary paragraph (what this PR is / what wrongness blocks a reader / what passes ran) and each confidence row's `<TODO: HIGH/MEDIUM/LOW>` + Notes. Add or remove rows per the references you actually applied; don't say HIGH unless the work finished.
</step>

<step number="5" name="Fill Review-history one-line summary">
One line summarizing what this review found.
</step>

<step number="6" name="Fill Tier-2 editorial-balance TODOs">
Vendor / entity mention counts, FAQ steering ratios — if §📊 is in rich form. Don't touch the Tier 1 stats (`editorial-balance-counts-faithful` enforces them against the JSON).
</step>

<step number="7" name="Keep the body self-consistent">
Count-table cells == bucket-bullet counts (style findings count in ⚠️). Every 🔍 trail line corresponds to a verdict; you may add a claim the artifact missed but may NOT drop a candidate-claims-floor entry (`docs-review:references:fact-check`). Every `**[L…]**` bucket bullet matches a trail record. **Never re-render a composed 🔍 trail line except to fix a literal rendering bug — and never drop, paraphrase, or truncate the `<evidence>; source: …>` parenthetical.** In particular, the `WebSearch ran query "…"` pointer on a Pass-3 unverifiable verdict is load-bearing for `pass-3-unverifiable-evidence` — the composer rendered it verbatim from `.verified-claims.json`; leave it intact.
</step>

<step number="8" name="Apply output-format DO-NOT list">
See `docs-review:references:output-format`. Do NOT WebFetch / re-verify claims — `.verified-claims.json` (rendered into the trail) is the verdict source. Editing a trail line to change a verdict word fails `verified-claims-trail-faithful`; if you believe a verdict is wrong, render it as recorded and open a follow-up issue. The only fan-out you run is the cross-sibling sibling-read digest (fresh-review path only).
</step>

<step number="9" name="On a re-entrant run">
Per `docs-review:references:update`: the draft's 📜 Review history has only the new line and ✅ Resolved is empty — merge in the prior pinned comment's history lines (append-only) and populate ✅ Resolved with prior findings now absent.
</step>

<step number="10" name="Write for the author, not the pipeline">
Bullet bodies and Summary prose must read to a PR author who knows nothing about how this review was assembled. Refer to **outcomes** (`✅ verified`, `❌ contradicted`, source URL), not the **processes**. Avoid pipeline-internal terms like *"the extraction layer"*, *"the verifier / validator / splicer"*, *"Pass 1/2/3"*, *"framing comparison"*, *"soft floor"*, *"the composer"*, or script names. Say *"the verification step"* or describe the outcome directly.
- **Bad:** "Counted as ❌ contradicted because the extraction layer truncated the claim text..."
- **Good:** "Flagged as ❌ contradicted in error — the source actually supports the claim. The verification step compared a shortened version of the claim against the source."
</step>

### 4. When you're done

Save `.review-draft.md` and exit. The workflow runs the publish chain as separate steps after your session — validate, deterministic splice (and a model-lane fallback for rules that genuinely can't be spliced deterministically), re-validate, then upsert via `pinned-comment.sh upsert` (with `--soft-floor` if residual violations remain). You do **not** call any of these from inside your turn. Hard rule 2 carries the contract.

### Fallback (composer crashed / draft absent)

If `.review-draft.md` is absent or its first lines are a `> [!CAUTION]` composer-failed banner, assemble the review manually — the pre-composer procedure:

1. Route each changed file using `docs-review:references:domain-routing`. Run each file under its domain and merge findings into a single output object.
2. Read the pre-step artifacts directly: `.verified-claims.json` for the trail/verdicts (render one trail line per verdict, verbatim — verdict word + per-verdict emoji + evidence + source; **do not re-verify**); `.candidate-claims.json` is the claim *floor* — every entry must surface a verdict line in the 🔍 Verification trail (the `candidate-claims-coverage` rule fails the review otherwise) and you add any claims the artifact missed; `.vale-findings.json` for the `#### Style findings` block; `.editorial-balance.json` for the §📊 Tier 1; `.hugo-build.json` / `.frontmatter-validation.json` / `.cross-sibling-discovery.json` for the build / frontmatter / sibling checks. If `.verified-claims.json` is absent or its `verdicts[]` is empty, fall back further to the in-review extraction + verification path per `docs-review:references:fact-check` §Routed verification fallback.
3. Render per `docs-review:references:output-format` and apply its DO-NOT list before emitting.
4. Save the assembled body to `.review-draft.md` and exit — the workflow publishes it. (See §4 above.)

This is the safety net, not the normal path.
