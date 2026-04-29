---
description: Review docs and blog post quality before committing (checks style, accuracy, and Pulumi best practices on open files, branches, or PRs).
---

# Docs Review (interactive)

**Use this when:** You're writing or editing documentation/blogs in your IDE or terminal and want feedback before opening a PR — or when you want to spot-check a specific PR locally.

This is the **interactive entry point**. It runs in IDE/terminal context with full tool access and outputs the review directly into the conversation. It never posts to GitHub.

The CI counterpart is [`docs-review-ci.md`](docs-review-ci.md). Shared review semantics live in [`_common/docs-review-core.md`](_common/docs-review-core.md). **Do not** add CI-mode conditionals here — keep this file scope-detection-and-review only.

---

## Usage

`/docs-review [PR_NUMBER]`

If `PR_NUMBER` is provided, reviews the PR via `gh pr view` / `gh pr diff`. If omitted, auto-detects scope from the current IDE/terminal context.

---

## Scope detection

When no PR number is provided, walk these steps **in order** and stop at the first that yields a scope:

### Step 1: Open files in the IDE

Check the conversation context for system reminders that list open files. If any are present, treat those files as the review scope and read them directly. Skip to "Perform the review".

### Step 2: Uncommitted changes

If Step 1 didn't apply, check the gitStatus block at the start of the conversation (or run `git status`) for modified (`M`) and untracked (`??`) files. Use `git diff` and read the affected files. Skip to "Perform the review".

### Step 3: Branch changes vs. master

Only if Steps 1 and 2 didn't apply:

```bash
git diff $(git merge-base --fork-point master HEAD)...HEAD
```

If `--fork-point` fails (no reflog), fall back to:

```bash
git diff $(git merge-base master HEAD)...HEAD
```

Review every changed file in the branch.

### Perform the review

Once scope is determined, apply the criteria in [`_common/docs-review-core.md`](_common/docs-review-core.md), composing the appropriate domain files based on which paths are touched:

Path-precedence order — a file is classified under the first rule that matches:

- `static/programs/**` → `_common/review-shared.md` + `_common/review-programs.md` (includes every nested file in a program directory)
- `content/blog/**`, `content/customers/**` → `_common/review-shared.md` + `_common/review-blog.md`
- `content/docs/**`, `content/learn/**`, `content/tutorials/**`, `content/what-is/**` → `_common/review-shared.md` + `_common/review-docs.md`
- `.github/workflows/**`, `scripts/**` except `scripts/programs/**`, `infrastructure/**`, `Makefile` (repo root), `package.json` (repo root only), `webpack.config.js`, `webpack.*.js` → `_common/review-shared.md` + `_common/review-infra.md`
- Anything else → `_common/review-shared.md` only
- A mixed PR runs each file under its appropriate domain and merges the findings.

For PR-number invocations, use:

```bash
gh pr view {{arg}} --json title,body,files,additions,deletions,labels
gh pr diff {{arg}}
```

Provide the review directly in the conversation, formatted for terminal display. **Never** call `gh pr review`, `gh pr comment`, or `gh pr edit` from this skill — output is for the user's eyes only. Include the scope in the summary, and offer to broaden the review (e.g., to additional files) if useful.
