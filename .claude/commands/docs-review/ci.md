---
user-invocable: false
description: Docs-review entry point for CI. Diff-only, posts to a pinned PR comment.
---

# Docs Review (CI)

This is the **CI entry point** for the docs review pipeline.

---

## Hard rules for CI

1. **Never read working-tree state.** No `git status`, `git diff` against the local checkout, no `ls`, no Read against arbitrary repo files. The CI runner's working tree is a shallow checkout that may not reflect what's in the PR. Use `gh pr view` and `gh pr diff` for **everything** about the PR.
2. **Post only via the pinned-comment script** (see §4 below).
3. **Diffs do not show trailing-newline status.** Do not flag missing trailing newlines from CI; the lint job catches this.
4. **Don't run `make` targets.** No `make build`, `make lint`, `make serve`. Lint and build run in their own jobs.
5. **No file paths from the working tree in findings.** Every `file:line` reference must come from the PR's diff or `gh pr view --json files` output.
6. **No internal-source MCP servers.** Notion and Slack MCP tools are not whitelisted in CI; review output is public. Live code execution beyond `gh` and file reads is unavailable.

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

### 2. Compose the review

Route each changed file using `docs-review:references:domain-routing`. Run each file under its domain and merge findings into a single output object.

If `.vale-findings.json` exists in the workspace, append each entry to ⚠️ Low-confidence as `[style] <category> — <message>`, citing the line. Use the `category` field; never surface the `rule` field. Per-file roll-up summary (>5 nits) and the full render contract live in `docs-review:references:output-format`. The workflow has already filtered to PR-introduced lines and capped the count.

### 3. Build the output

Render using `docs-review:references:output-format` and apply its DO-NOT list before emitting.

### 4. Post via the pinned-comment script

Write the rendered output to a temp file and call:

```bash
bash .claude/commands/docs-review/scripts/pinned-comment.sh upsert \
  --pr "$PR_NUMBER" \
  --body-file "$REVIEW_OUTPUT_FILE"
```

The script handles marker convention, splitting, in-place edits, and overflow. Do not delete the 1/M summary comment.
