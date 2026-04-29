---
user-invocable: false
description: Docs-review entry point for CI. Diff-only, posts to a pinned PR comment.
---

# Docs Review (CI)

This is the **CI entry point** for the docs review pipeline. It is invoked by `.github/workflows/claude-code-review.yml` when a PR transitions to `ready_for_review`.

---

## Hard rules for CI

1. **Never read working-tree state.** No `git status`, `git diff` against the local checkout, no `ls`, no Read against arbitrary repo files. The CI runner's working tree is a shallow checkout that may not reflect what's in the PR. Use `gh pr view` and `gh pr diff` for **everything** about the PR.
2. **Post only via the pinned-comment script** (see §5 below). All review output goes through it so the review survives across re-runs as a single logical comment sequence.
3. **Diffs do not show trailing-newline status.** Do not flag missing trailing newlines from CI; the lint job catches this.
4. **Don't run `make` targets.** No `make build`, `make lint`, `make serve`. Lint and build run in their own jobs.
5. **No file paths from the working tree in findings.** Every `file:line` reference must come from the PR's diff or `gh pr view --json files` output.
6. **No internal-source MCP servers.** Fact-check uses public sources only: `gh`, `WebFetch`, `WebSearch`, and local repo read. Notion and Slack are excluded by design — review output is public.

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

Route each changed file using `docs-review:references:domain-routing`. Run each file under its domain and merge findings into a single output object.

### 3. Fact-check (gated)

If the PR has the `fact-check:needed` label, invoke `docs-review:references:fact-check`. The domain file sets the scrutiny level.

### 4. Build the output

Render using `docs-review:references:output-format` and apply its DO-NOT list before emitting.

### 5. Post via the pinned-comment script

Write the rendered output to a temp file and call:

```bash
bash .claude/commands/docs-review/scripts/pinned-comment.sh upsert \
  --pr "$PR_NUMBER" \
  --body-file "$REVIEW_OUTPUT_FILE"
```

The script handles the `<!-- CLAUDE_REVIEW N/M -->` marker convention, splits at the 65k boundary, edits existing comments in place, appends overflow, and prunes the tail. The 1/M summary is never deleted.

### 6. Post-run

After a successful post, the workflow applies the `review:claude-ran` label and removes `review:claude-stale` if present.
