---
description: Review changes for style, accuracy, and Pulumi best practices. Context-sensitive in IDEs, or provide a PR number to review a PR from this repo.
---

# Documentation Review Command

You will review documentation changes and provide feedback on style, accuracy, and best practices.

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

Use the repository's CLAUDE.md, AGENTS.md, and STYLE-GUIDE.md for guidance on style and conventions.

Provide your review as a single summary, highlighting any issues found and suggesting improvements.

Be constructive and helpful in your feedback, but don't overdo the praise. Be concise.

Always provide relevant line numbers for any issues you identify.

**Criteria:**

- Always enforce `STYLE-GUIDE.md`. If not covered there, fall back to the [Google Developer Documentation Style Guide](https://developers.google.com/style).
- Check **spelling and grammar** in all files.
- Confirm that **all links resolve** and point to the correct targets (no 404s, no mislinked paths).
- Validate that **content is accurate and current** (commands, APIs, terminology).
- Ensure **all new files end with a newline**.
- Double-check indented lines to ensure they are not incorrectly indented as code blocks.
- **Code examples** must run correctly and follow best practices:
  - Do not suggest untested code.
  - Examples should show realistic use cases, not contrived demos.
  - Examples should handle errors appropriately.
  - Examples should follow language-specific best practices.
- **Files moved, renamed, or deleted**:
  - Confirm that moved or renamed files have appropriate aliases added to the frontmatter to avoid broken links.
  - Confirm that deleted files have a redirect created, if applicable.
- **Build, test, and infrastructure changes**:
  - If changes are made to build scripts (scripts/), GitHub Actions workflows (.github/workflows/), the Makefile, or infrastructure code (infrastructure/), verify that BUILD-AND-DEPLOY.md has been updated to reflect these changes.
  - Examples of changes requiring documentation updates: new make targets, modified deployment workflows, infrastructure configuration changes, new environment variables, updated build processes.
- **Dependabot dependency updates**:
  - Dependabot PRs are automatically labeled with risk tiers and action guidance.
  - For detailed triage guidance and dependency categorizations, see the [Dependency Management](../../../BUILD-AND-DEPLOY.md#dependency-management) section in BUILD-AND-DEPLOY.md.
  - Check labels: `deps-risk-high/medium/low` and `deps-merge-after-test`/`deps-security-patch`/`deps-quarterly-review`.
  - For webpack/bundler updates, also check the [Infrastructure Change Review](../../../BUILD-AND-DEPLOY.md#infrastructure-change-review) section for Lambda@Edge risks.
- **Images and assets**:
  - Check images have alt text for accessibility.
  - Verify image file sizes are reasonable.
  - Ensure images are in appropriate formats.
- **Front matter**:
  - Verify required front matter fields (title, description, etc.).
  - Check meta descriptions are present and appropriate length.
- **Cross-references and consistency**:
  - Check that related pages are cross-linked appropriately.
  - Verify terminology is consistent with other docs.
- **SEO**:
  - Check that page titles and descriptions are SEO-friendly.
  - Check that the titles and descriptions match the content.
  - Verify URL structure follows conventions.
- **Role-Specific Review Guidelines**
  - Documentation and blog/marketing materials have additional role-specific criteria below.

### Role-Specific Review Guidelines

#### Documentation

When reviewing **Documentation**, serve the role of a professional technical writer. Review for:

- Clarity and conciseness.
- Logical flow and structure.
- No jargon unless defined.
- Avoid passive voice.
- Avoid overly complex sentences. Shorter is usually better.
- Avoid superlatives and vague qualifiers.
- Avoid unnecessary filler words or sentences.
- Be specific and provide examples.
- Use consistent terminology.

#### Blogs or Marketing Materials

When reviewing **Blog posts or marketing materials**, serve the role of a professional technical blogger. Review for:

- Clear, engaging titles.
- Strong opening that hooks the reader.
- Clear structure with headings and subheadings.
- Concise paragraphs (3-4 sentences max).
- Use of lists and bullet points for readability.
- Reject filler, vague generalities, or AI-generated slop.
- Avoid clickbait phrasing.
- Clear call-to-action at the end.

### Additional Instructions

When blog posts introduce or announce new Pulumi features, providers, or significant functionality changes:

1. Check if corresponding documentation exists in `content/docs/` for the feature being announced
2. Verify that documentation, tutorials, or guides adequately cover the new functionality
3. If documentation is missing or incomplete, note this in your review with:
    - Specific gaps identified (e.g., "No ESC integration guide found")
    - Suggested documentation locations (e.g., "Should add to `content/docs/esc/guides/`")
    - Recommended documentation type (tutorial, concept guide, reference, etc.)
