---
description: Review content quality while writing or before committing (checks style, accuracy, best practices on open files, branches, or PRs).
---

# Documentation Review Command

**Use this when:** You're writing or editing documentation and want to check quality before committing, or when you want content feedback without the full PR approval workflow.

Reviews documentation changes for style, accuracy, and Pulumi best practices. Works on currently open files (context-sensitive) or on a specific PR number.

---

## Usage

`/docs-review [PR_NUMBER]`

Reviews documentation changes for style, accuracy, and Pulumi best practices.

The `PR_NUMBER` argument is optional. If not provided in interactive mode, the command will auto-detect scope from IDE context (open files), uncommitted changes, or branch changes.

---

## Context Detection

This command operates in two modes based on execution context:

**CI Mode** - Detected when the prompt includes "You are running in a CI environment"

- Minimizes token usage by working primarily from diffs
- Posts review as a PR comment using `gh pr comment`
- Tool access is restricted (no `make` commands, limited to Read, Glob, Grep, and gh commands)
- Applies special handling for efficiency (e.g., trailing newline checks)

**Interactive Mode** - When running in IDE or terminal (outside CI)

- Provides review directly in the conversation (never uses `gh pr comment`)
- Full tool access available
- Auto-detects scope from:
  1. Open files in IDE (from system reminders)
  2. Uncommitted changes (git status)
  3. Branch changes (git merge-base)

---

## Instructions for Docs Review

Follow the appropriate section below based on your execution context:

### Continuous Integration (CI) Context

When running in CI (e.g., GitHub Actions), follow these efficiency guidelines to minimize token usage:

1. Start by running `gh pr view <PR_NUMBER> --json title,body,files,additions,deletions` to get PR metadata
2. Get the full diff with `gh pr diff <PR_NUMBER>`
3. Work primarily from the diff output - this is much more efficient than reading full files
4. Only use the Read tool on specific files when the diff doesn't provide enough context
5. Do NOT attempt to run `make serve`, `make lint`, or `make build` - these commands are not available in CI and will fail
6. Focus your review on the changed lines shown in the diff, not entire files
7. Use Grep sparingly - only when absolutely necessary to understand context

After completing your review, post it to the PR by running:

```bash
gh pr comment <PR_NUMBER> --body "YOUR_REVIEW_CONTENT_HERE"
```

Your review should include:

- Issues found with specific line numbers from the affected files. Do not use line numbers from the diff.
- Constructive suggestions using suggestion code fence formatting blocks
- An instruction to mention you (@claude) if the author wants additional reviews or fixes

Use the **Review Criteria** section below for your review, except for the following adjustments:

- Diffs do not display the trailing newline status of files. Do not flag missing trailing newlines unless you have confirmed the absence while reading the full file for another reason. Suspected missing newlines are not sufficient reason to read the full file.

### Interactive Context (IDE or Chat)

When running outside of CI, always provide your review directly in the conversation. Do NOT use `gh pr comment` to post to PRs.

Before beginning your review, you must determine the scope of changes to review:

**If a PR number is provided** ({{arg}}):

- Use `gh pr view {{arg}}` to retrieve the PR title, description, and metadata
- Use `gh pr diff {{arg}}` to get the full diff of changes
- Review the PR changes according to the criteria below.
- After completing your review, provide it in the conversation formatted appropriately for display in the terminal.

**If no PR number is provided**, follow these steps IN ORDER:

#### Step 1: Check for open files in IDE

DO NOT RUN ANY COMMANDS YET. First check the conversation context:

- Look for system reminders about files open in the IDE
- If you find an open file mentioned, read that file and review it
- Stop and offer to review additional files if desired
- Skip to Step 4 if this applies

#### Step 2: Check for uncommitted changes

If Step 1 didn't apply, check the gitStatus at the start of the conversation:

- Look for modified (M) or untracked (??) files in the git status
- If there are uncommitted changes, use `git diff` and `git status` to see what changed
- Review those specific files
- Skip to Step 4 if this applies

#### Step 3: Compare against branch point

ONLY if Steps 1 and 2 didn't apply:

- Use `git merge-base --fork-point master HEAD` to find the ancestor branch point
- Use `git diff $(git merge-base --fork-point master HEAD)...HEAD` to compare current branch against its immediate ancestor
- If `--fork-point` fails (no reflog), fall back to `git diff $(git merge-base master HEAD)...HEAD`
- Review all changed files in the branch

#### Step 4: Perform the review

Once scope is determined, review the changes according to the criteria below. Provide the review in the conversation formatted appropriately for display in the terminal. Include the scope of files reviewed in your summary and offer to review additional files if desired.

## Review Criteria

For complete review criteria, see [review-criteria.md](_common/review-criteria.md).

**Quick reference**: Check STYLE-GUIDE.md compliance, spelling/grammar, links, code examples, file moves with aliases, infrastructure changes, images with alt text, frontmatter, cross-references, SEO, and role-specific guidelines (documentation vs blog).
