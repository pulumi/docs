---
name: docs-review
description: Review docs and blog post quality before committing (style, accuracy, Pulumi best practices). Use when you've made content changes locally and want a quality pass on open files, the current branch, or a specific PR — outputs to the conversation, never posts to GitHub.
user-invocable: true
---

# Docs Review (interactive)

**Use this when:** You're writing or editing documentation/blogs in your IDE or terminal and want feedback before opening a PR — or when you want to spot-check a specific PR locally.

This is the **interactive entry point**. It runs in IDE/terminal context with full tool access and outputs the review directly into the conversation. It never posts to GitHub.

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

Once scope is determined, apply the criteria in `docs-review:references:output-format`, composing the appropriate domain files based on which paths are touched. See `docs-review:references:domain-routing` for the canonical path → domain table.

`docs-review:references:shared-criteria` applies to every file regardless of domain. A mixed PR runs each file under its appropriate domain and merges the findings.

For PR-number invocations, use:

```bash
gh pr view {{arg}} --json title,body,files,additions,deletions,labels
gh pr diff {{arg}}
```

Provide the review directly in the conversation, formatted for terminal display. **Never** call `gh pr review`, `gh pr comment`, or `gh pr edit` from this skill — output is for the user's eyes only. Include the scope in the summary, and offer to broaden the review (e.g., to additional files) if useful.
