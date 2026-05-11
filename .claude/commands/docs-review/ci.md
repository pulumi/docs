---
user-invocable: false
description: Docs-review entry point for CI. Diff-only, posts to a pinned PR comment.
---

# Docs Review (CI)

This is the **CI entry point** for the docs review pipeline.

---

## Hard rules for CI

1. **Never read working-tree state.** No `git status`, `git diff` against the local checkout, no `ls`, no Read against arbitrary repo files. The CI runner's working tree is a shallow checkout that may not reflect what's in the PR. Use `gh pr view` and `gh pr diff` for **everything** about the PR.
2. **Post only via `pinned-comment.sh upsert-validated`** for the initial post (see §4 below). Never call plain `upsert` directly except as the soft-floor fallback after a second validation failure. The validator catches structural drift the model occasionally introduces (style-count, render-mode, dispatch-metadata, trail-vs-rendered consistency); the wrapper enforces it atomically.
3. **Diffs do not show trailing-newline status.** Do not flag missing trailing newlines from CI; the lint job catches this.
4. **Don't run `make` targets.** No `make build`, `make lint`, `make serve`. Lint and build run in their own jobs.
5. **No file paths from the working tree in findings.** Every `file:line` reference must come from the PR's diff or `gh pr view --json files` output.
6. **No internal-source MCP servers.** Notion and Slack MCP tools are not whitelisted in CI; review output is public. Live code execution beyond `gh` and file reads is unavailable.
7. **Bash patterns the runner sandbox rejects.** Three friction patterns the harness blocks regardless of the allow-list — write commands that avoid them:
   - **Reading or writing under `/tmp/`.** The filesystem-path policy restricts `cat`, `grep`, and output redirection to the runner's working directory. Use the `Read` tool (not Bash `cat`) for any `/tmp/...` path; never redirect output to `/tmp/...`. Workflow-managed pre-step artifacts (`.fetched-urls.json`, `.editorial-balance.json`, `.vale-findings.json`, `.cross-sibling-discovery.json`, `.frontmatter-validation.json`, `.hugo-build.json`, `.candidate-claims.json` — see `docs-review:references:pre-computation`) live in the workspace root and are Bash-accessible.
   - **Shell control flow in Bash (`for`, `while`, `case`, `if`).** The multi-op decomposer rejects loops and conditionals even when each constituent command is allow-listed. For iteration over a list, use `python3 -c "..."` (allow-listed) or sequential single-op `gh` invocations.
   - **Brace expansion (`{a,b,c}`) and subshell grouping (`(cmd1; cmd2)`).** Both decompose unfavorably; expand the list manually or move the logic to a `python3 -c "..."` script.

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

If `.vale-findings.json` exists in the workspace, append each entry to ⚠️ Low-confidence per the Style-findings render contract in `docs-review:references:output-format` (bullet form, `#### Style findings` H4, the inline-vs-collapse render-mode rule, and the per-file roll-up summary for files with >5 style findings). Use the `category` field; never surface the `rule` field. The workflow has already filtered to PR-introduced lines and capped the count.

### 3. Build the output

Render using `docs-review:references:output-format` and apply its DO-NOT list before emitting.

### 4. Post via the pinned-comment script

Write the rendered output to a temp file and call the validating wrapper:

```bash
bash .claude/commands/docs-review/scripts/pinned-comment.sh upsert-validated \
  --pr "$PR_NUMBER" \
  --body-file "$REVIEW_OUTPUT_FILE"
```

The wrapper runs `validate-pinned.py` against the body, then calls `upsert` if validation passes. On a non-zero exit, read the fix-me marker with the `Read` tool (not Bash `cat` — see Hard rule 7):

```
Read /tmp/validate-pinned.fix-me.md
```

Each violation lists the rule, expected vs actual, and a hint. Re-render the body addressing every violation, then call `upsert-validated` once more. **Cap the retry at one attempt** — if the second validation also fails, fall back to plain `upsert` with the unfixed body and accept the soft-floor:

```bash
VALIDATE_SOFT_FLOOR=1 bash .claude/commands/docs-review/scripts/pinned-comment.sh upsert \
  --pr "$PR_NUMBER" \
  --body-file "$REVIEW_OUTPUT_FILE"
```

The validator will have already emitted a `::warning::validate-pinned soft-floor` CI annotation surfacing the residual violations to the maintainer.

The wrapper handles marker convention, splitting, in-place edits, and overflow. Do not delete the 1/M summary comment.
