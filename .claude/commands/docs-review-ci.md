---
user-invocable: false
description: Docs-review entry point for CI. Diff-only, posts to a pinned PR comment.
---

# Docs Review (CI)

This is the **CI entry point** for the docs review pipeline. It is invoked by `.github/workflows/claude-code-review.yml` when a PR transitions to `ready_for_review`.

The interactive counterpart is [`docs-review.md`](docs-review.md). Shared review semantics live in [`_common/docs-review-core.md`](_common/docs-review-core.md).

---

## Hard rules for CI

These are non-negotiable. Past false-positive findings have come from violating them.

1. **Never read working-tree state.** No `git status`, `git diff` against the local checkout, no `ls`, no Read against arbitrary repo files to "verify the file actually has X." The CI runner's working tree is a shallow checkout that may not reflect what's in the PR; reasoning from it produces wrong findings. Use `gh pr view` and `gh pr diff` for **everything** about the PR.
2. **Never post via `gh pr comment` directly.** All review output goes through the pinned-comment script (see "Posting output" below) so the review survives across re-runs as a single logical comment sequence.
3. **Diffs do not show trailing-newline status.** Do not flag missing trailing newlines from CI. The lint job catches this; if you can't see it in the diff, don't claim it's missing.
4. **Don't run `make` targets.** No `make build`, `make lint`, `make serve`. Lint and build run in their own jobs.
5. **No file paths from the working tree in findings.** Every `file:line` reference must come from the PR's diff or `gh pr view --json files` output.
6. **No internal-source MCP servers.** This workflow has no Notion, Slack, or other internal-source access by design — review output is public, and internal sources create leakage and prompt-injection risk. Fact-check is public-sources-only here (`gh`, `WebFetch`, `WebSearch`, local repo read for cross-references).

---

## Inputs

The workflow passes these as environment variables (or substitutes them into the prompt):

- `PR_NUMBER` — the PR being reviewed
- `PR_LABELS` — comma-separated list of labels currently on the PR (set by triage)

Domain selection is driven by the labels (`review:docs`, `review:blog`, `review:infra`, `review:programs`, `review:mixed`, `review:trivial`). Fact-check is gated on `fact-check:needed`.

If `review:trivial` is present, exit early without producing a review (the workflow's job `if:` already handles the short-circuit; this is a defense-in-depth check).

---

## Procedure

### 1. Pull PR context

```bash
gh pr view "$PR_NUMBER" --json title,body,author,labels,files,additions,deletions,headRefName,baseRefName
gh pr diff "$PR_NUMBER"
```

Treat the diff as the source of truth for what changed. If `--json files` lists a file but the diff doesn't show it (rare — usually a mode-only change), note it but don't invent findings.

**Empty-diff short-circuit.** If `gh pr diff` returns no content (mode-only changes, renames with no content change, or any PR with zero text diff), exit the review with a one-line stdout log (`review: pr=<N> empty-diff skip`) and do **not** call `pinned-comment.sh upsert`. The script rejects empty bodies with "split produced no pages" by design; the short-circuit keeps the workflow green and avoids posting an empty comment. The workflow's post-run label step (`review:claude-ran`) should still apply so stale-marking works on subsequent pushes.

**Missing-label fallback.** The workflow passes the PR's current labels in the prompt. If triage failed for any reason (rate limit, transient `gh` error) and `review:docs` / `review:blog` / `review:infra` / `review:programs` are all missing, fall back to routing each file by path using the table in the next section — don't abort. Fact-check is gated on `fact-check:needed`; its absence degrades to "no fact-check" rather than aborting the review.

### 2. Compose the review

For each changed file, route to **exactly one** domain using path-precedence order. A file is classified under the first rule that matches; do not double-count.

| Order | Compose | Applies when the file path matches |
|---|---|---|
| 1 | `_common/review-shared.md` + `_common/review-programs.md` | `static/programs/**` (includes every nested file in a program directory) |
| 2 | `_common/review-shared.md` + `_common/review-blog.md` | `content/blog/**`, `content/customers/**` |
| 3 | `_common/review-shared.md` + `_common/review-docs.md` | `content/docs/**`, `content/learn/**`, `content/tutorials/**`, `content/what-is/**` |
| 4 | `_common/review-shared.md` + `_common/review-infra.md` | `.github/workflows/**`, `scripts/**` except `scripts/programs/**`, `infrastructure/**`, `Makefile` (repo root), `package.json` (repo root only), `webpack.config.js`, `webpack.*.js` |

A PR may touch files in more than one domain. Run each file under its appropriate domain; merge the findings into a single output object before posting.

Ordering note: a per-program `package.json` under `static/programs/<name>/package.json` is programs, not infra. `scripts/programs/**` is programs tooling, not site infra.

### 3. Fact-check (gated)

If the PR has the `fact-check:needed` label, invoke [`_common/fact-check.md`](_common/fact-check.md) with:

- The list of changed content files
- Scrutiny level set by the domain file (docs → `standard`, blog/programs → `heightened`)
- Public-sources-only constraints from this file (no Notion, no Slack)

### 4. Build the output

Render the findings using the shared format in [`_common/docs-review-core.md`](_common/docs-review-core.md):

- 🚨 Outstanding in this PR
- ⚠️ Low-confidence
- 💡 Pre-existing issues in touched files (optional, capped per file)
- ✅ Resolved since last review (only meaningful on re-runs; empty on initial)
- 📜 Review history

Apply the **DO-NOT list** in `docs-review-core.md` before emitting. Suppress findings the linter already catches (trailing newlines, fence languages, alt text, heading case, etc.).

### 5. Post via the pinned-comment script

Write the rendered output to a temp file and call:

```bash
bash .claude/commands/_common/scripts/pinned-comment.sh upsert \
  --pr "$PR_NUMBER" \
  --body-file "$REVIEW_OUTPUT_FILE"
```

The script handles the `<!-- CLAUDE_REVIEW N/M -->` marker convention, splits at the 65k boundary, edits existing comments in place, appends overflow, and prunes the tail.

**Never** delete and recreate the 1/M summary comment. The script handles this; do not work around it.

### 6. Post-run

After a successful post, the workflow applies the `review:claude-ran` label and removes `review:claude-stale` if present. Nothing for the prompt to do here.

---

## Re-entrant runs

This entry point is **initial review only**. Re-entrant updates (after `@claude` mentions or new commits) go through [`_common/update-review.md`](_common/update-review.md), invoked from `.github/workflows/claude.yml`.

If the workflow detects an existing pinned comment when it would otherwise post a fresh review, it should hand off to `update-review.md` instead. For v1, this hand-off is the workflow's responsibility.
