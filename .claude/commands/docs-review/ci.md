---
user-invocable: false
description: Docs-review entry point for CI. Diff-only, posts to a pinned PR comment.
---

# Docs Review (CI)

This is the **CI entry point** for the docs review pipeline.

---

## Hard rules for CI

1. **Never read working-tree *source* state.** No `git status`, `git diff` against the local checkout, no `ls`, no Read against arbitrary repo content files. The CI runner's working tree is a shallow checkout that may not reflect what's in the PR. Use `gh pr view` and `gh pr diff` for **everything** about the PR. *(The workflow-generated pre-step artifacts in the workspace root — `.review-draft.md`, `.verified-claims.json`, etc. per Hard rule 7 — are not "working-tree source state"; Read them freely.)*
2. **Post only via `pinned-comment.sh upsert-validated`** for the initial post (see §4 below). Never call plain `upsert` directly except as the soft-floor fallback after a second validation failure. The validator catches structural drift the model occasionally introduces (style-count, render-mode, dispatch-metadata, trail-vs-rendered consistency, and now any surviving `<TODO:` placeholder); the wrapper enforces it atomically.
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

**Empty-diff short-circuit.** If `gh pr diff` returns no content (mode-only changes, renames with no content change, or any PR with zero text diff), exit the review with a one-line stdout log (`review: pr=<N> empty-diff skip`) and do **not** call `pinned-comment.sh upsert`.

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

Edit the draft (the composer ASSEMBLES; you JUDGE):

1. **Triage the stub bucket bullets.** For each `- **[L…]**` bullet with a `<TODO>` marker under 🚨 Outstanding / ⚠️ Low-confidence: decide whether the finding is real. If spurious — remove the bullet entirely and decrement the matching count-table cell. If real — replace the `<TODO: …>` with the fix prose / suggestion block per `docs-review:references:shared-criteria` (quote-and-rewrite mandate); mirror any `framing:` note already in the bullet (anti-hedge mandate for `⚔️ mismatch`: state the verdict, name the corroborating siblings, no either-or softening). For an `unverifiable` ⚠️ stub: decide whether it's a factual blocker — if so, move it to 🚨 Outstanding; either way, file the author-question buffer line.
2. **Add the findings the composer couldn't pre-stub** — Hugo-build errors & link-integrity breaks (from `.hugo-build.json`), frontmatter alias/URL collisions (from `.frontmatter-validation.json` — triage PR-internal renames per `docs-review:references:fact-check`), internal-link / shortcode breaks in the content, cross-sibling mismatches (from your in-review sibling-read fan-out — `docs-review:references:fact-check` §Cross-sibling consistency), code-examples findings (the 3-specialist checks), editorial-balance threshold flags (Tier 2 + the Tier 1 outliers shown in §📊), intuition-flag promotions, and any two-question-test findings from the domain rules. **Every `**[L<line>]**` bucket bullet you ADD MUST be backed by a matching 🔍 Verification trail line — `bucket-bullet-trail-match` / `bucket-bullet-line-range-prefix` enforce this and a missing anchor soft-floors the review.** If the finding has no fact-check claim behind it (hugo-build, frontmatter, code-examples, editorial-balance threshold, intuition, two-question-test), add its trail line first (`- L<line> "<short description>" → <emoji> <verdict>` — e.g. `❌ contradicted (Hugo build: <error>)` for a build error, `⚔️ mismatch` for a cross-sibling divergence, `🤷 unverifiable` for an editorial-balance flag whose verdict needs reviewer judgment). If a finding genuinely has no line anchor at all, **fold it into prose elsewhere — not into a `**[L…]**` bullet**.
3. **Fill the cross-sibling investigation-log line** — replace `0 of N siblings (fan-out runs in-review — replace this count)` with the actual `X of N siblings` from your fan-out (or with a carried-forward count on a re-entrant run).
4. **Write the Summary paragraph and the Review-confidence table** — fill the `<TODO>` summary (one paragraph: what this PR is / what wrongness blocks a reader / what passes ran) and each confidence row's `<TODO: HIGH/MEDIUM/LOW>` + Notes. Add or remove confidence rows per the references you actually applied; don't say HIGH unless the work finished.
5. **Fill the Review-history `<TODO: one-line summary>`** with a one-line summary of what this review found.
6. **Fill the Tier-2 editorial-balance `<TODO>`s** (vendor / entity mention counts, FAQ steering ratios) if the §📊 section is in rich form; don't touch the Tier 1 stats (`editorial-balance-counts-faithful` enforces them against the JSON).
7. **Keep the body self-consistent** — count-table cells == bucket-bullet counts (style findings count in ⚠️); every 🔍 trail line corresponds to a verdict (you may add a claim the artifact missed, you may **not** drop a candidate-claims-floor entry — see `docs-review:references:fact-check`); every `**[L…]**` bucket bullet matches a trail record; `contradicted`/`mismatch` trail verdicts surface in 🚨 Outstanding. **Never re-render a composed 🔍 trail line except to fix a literal rendering bug — and never drop, paraphrase, or truncate the `<evidence>; source: …>` parenthetical. In particular, never drop a `WebSearch ran query "…"` pointer on a Pass-3 unverifiable verdict: `pass-3-unverifiable-evidence` needs that pointer, the composer rendered it verbatim from `.verified-claims.json` — leave it intact.**
8. Apply the `docs-review:references:output-format` DO-NOT list before emitting. **Do NOT WebFetch / re-verify claims** — `.verified-claims.json` (rendered into the trail) is the verdict source; editing a trail line to change a verdict word fails the `verified-claims-trail-faithful` rule (if you believe a verdict is wrong, render it as recorded and open a follow-up issue). The only fan-out you run is the cross-sibling sibling-read digest (fresh-review path only).
9. **On a re-entrant run** (`docs-review:references:update`): the draft's 📜 Review history has only the new line and ✅ Resolved is empty — merge in the prior pinned comment's history lines (append-only) and populate ✅ Resolved with prior findings now absent.

### 4. Post via the pinned-comment script

Edit `.review-draft.md` in place (or copy it to a temp file first), then call the validating wrapper:

```bash
bash .claude/commands/docs-review/scripts/pinned-comment.sh upsert-validated \
  --pr "$PR_NUMBER" \
  --body-file .review-draft.md
```

The wrapper runs `validate-pinned.py` against the body (which now also enforces `no-todo-tokens` — **every `<TODO:` placeholder must be replaced** before posting) plus a Haiku surgical-fix pass, then calls `upsert` if validation passes. On a non-zero exit, read the fix-me marker with the `Read` tool (not Bash `cat` — see Hard rule 7):

```
Read /tmp/validate-pinned.fix-me.md
```

Each violation lists the rule, expected vs actual, and a hint. Address every violation in the body, then call `upsert-validated` once more. **Cap the retry at one attempt** — if the second validation also fails, fall back to `upsert --soft-floor` with the unfixed body and accept the soft-floor:

```bash
bash .claude/commands/docs-review/scripts/pinned-comment.sh upsert --soft-floor \
  --pr "$PR_NUMBER" \
  --body-file .review-draft.md
```

Use the `--soft-floor` *flag* — NOT the `VALIDATE_SOFT_FLOOR=1 bash …` env-prefix form (an env prefix makes the command not start with `bash`, so the runner's allow-list rejects it). `upsert --soft-floor` re-runs `validate-pinned.py --soft-floor` (emitting a `::warning::validate-pinned soft-floor` CI annotation that surfaces the residual violations to the maintainer), then publishes regardless.

The wrapper handles marker convention, splitting, in-place edits, and overflow. Do not delete the 1/M summary comment.

### Fallback (composer crashed / draft absent)

If `.review-draft.md` is absent or its first lines are a `> [!CAUTION]` composer-failed banner, assemble the review manually — the pre-composer procedure:

1. Route each changed file using `docs-review:references:domain-routing`. Run each file under its domain and merge findings into a single output object.
2. Read the pre-step artifacts directly: `.verified-claims.json` for the trail/verdicts (render one trail line per verdict, verbatim — verdict word + per-verdict emoji + evidence + source; **do not re-verify**); `.candidate-claims.json` is the claim *floor* — every entry must surface a verdict line in the 🔍 Verification trail (the `candidate-claims-coverage` rule fails the review otherwise) and you add any claims the artifact missed; `.vale-findings.json` for the `#### Style findings` block; `.editorial-balance.json` for the §📊 Tier 1; `.hugo-build.json` / `.frontmatter-validation.json` / `.cross-sibling-discovery.json` for the build / frontmatter / sibling checks. If `.verified-claims.json` is absent or its `verdicts[]` is empty, fall back further to the in-review extraction + verification path per `docs-review:references:fact-check` §Routed verification fallback.
3. Render per `docs-review:references:output-format` and apply its DO-NOT list before emitting.
4. Post via §4 above.

This is the safety net, not the normal path.
