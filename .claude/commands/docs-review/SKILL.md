---
name: docs-review
description: Review docs and blog post quality before committing (style, accuracy, Pulumi best practices). Use when you've made content changes locally and want a quality pass on open files, the current branch, or a specific PR — outputs to the conversation, never posts to GitHub.
user-invocable: true
---

# Docs Review (interactive)

Output goes into the conversation. This skill never posts to GitHub.

## Usage

`/docs-review [PR_NUMBER]`

If `PR_NUMBER` is provided, review the PR via `gh pr view` / `gh pr diff`. If omitted, auto-detect scope from the current IDE/terminal context.

## Scope detection (when no PR number is provided)

Walk these steps in order; stop at the first that yields a scope.

1. **Open files in the IDE.** Check the conversation context for system reminders that list open files. If any are present, treat those files as the scope.
2. **Uncommitted changes.** Check the gitStatus block (or run `git status`) for modified (`M`) and untracked (`??`) files. Use `git diff` and read the affected files.
3. **Branch changes vs. master:**

    ```bash
    git diff $(git merge-base --fork-point master HEAD)...HEAD
    ```

    If `--fork-point` fails (no reflog), fall back to `git diff $(git merge-base master HEAD)...HEAD`. Review every changed file in the branch.

## Performing the review

Route each file to a domain via `docs-review:references:domain-routing`, then apply that domain's criteria plus `docs-review:references:shared-criteria`. Render the output per `docs-review:references:output-format`.

For PR-number invocations:

```bash
gh pr view {{arg}} --json title,body,files,additions,deletions,labels
gh pr diff {{arg}}
```

Format for terminal display. Include the scope in the summary, and offer to broaden if useful.
