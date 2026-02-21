---
description: Review blog post quality for style, accuracy, SEO, and publishing readiness (checks AI writing patterns, technical claims, meta elements, and Pulumi conventions).
---

# Blog Review Command

**Use this when:** You're writing or editing a blog post and want to check quality before committing, or when you want blog-specific content feedback without the full PR approval workflow.

Reviews blog post changes for style, accuracy, SEO, publishing readiness, and common AI writing patterns. Works on currently open files (context-sensitive) or on a specific PR number.

---

## Usage

`/blog-review [PR_NUMBER]`

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
  1. Uncommitted changes (git status)
  1. Branch changes (git merge-base)

---

## Instructions for Blog Review

Follow the appropriate section below based on your execution context:

### Continuous Integration (CI) Context

When running in CI (e.g., GitHub Actions), follow these efficiency guidelines to minimize token usage:

1. Start by running `gh pr view <PR_NUMBER> --json title,body,files,additions,deletions` to get PR metadata
1. Get the full diff with `gh pr diff <PR_NUMBER>`
1. Work primarily from the diff output - this is much more efficient than reading full files
1. Only use the Read tool on specific files when the diff doesn't provide enough context
1. Do NOT attempt to run `make serve`, `make lint`, or `make build` - these commands are not available in CI and will fail
1. Focus your review on the changed lines shown in the diff, not entire files
1. Use Grep sparingly - only when absolutely necessary to understand context

After completing your review, post it to the PR by running:

```bash
gh pr comment <PR_NUMBER> --body "YOUR_REVIEW_CONTENT_HERE"
```

Your review should include:

- Issues found with specific line numbers from the affected files. Do not use line numbers from the diff.
- Constructive suggestions using suggestion code fence formatting blocks
- An instruction to mention you (@claude) if the author wants additional reviews or fixes

Use `_common:review-criteria` for universal checks, plus the blog-specific criteria below, except for the following adjustments:

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

Once scope is determined, review the changes according to ALL criteria below. Provide the review in the conversation formatted appropriately for display in the terminal. Include the scope of files reviewed in your summary and offer to review additional files if desired.

---

## Review Criteria

### Universal checks

For universal review criteria (spelling, grammar, links, frontmatter, code examples, images, SEO basics), see [review-criteria.md](_common/review-criteria.md).

### Blog-specific criteria

Apply ALL of the following blog-specific checks in addition to the universal criteria above.

#### 1. AI writing pattern detection

This is the most commonly flagged category in blog PR reviews. Check for:

- **Em-dash overuse**: Flag if more than 1-2 em-dashes per section. Suggest replacing with commas, parentheses, or separate sentences.
- **Contrastive pattern**: Flag "It's not X, it's Y" / "This isn't X. It's Y" formulations. These read as formulaic.
- **Choppy uniform sentences**: Flag sequences of short declarative sentences of similar length. Vary sentence length and structure; mix short and long sentences.
- **Unnecessary TL;DR / summary paragraphs**: Flag opening paragraphs that simply restate what the following sections cover. The intro should motivate, not summarize.
- **Repetitive sentence openers**: Flag sequences starting with "This X...", "The X...", or any repeated pattern. Vary openers.
- **Hedging language**: Flag "generally", "typically", "tends to", "something like", "in many cases". Blog posts are thought leadership — write recommendations with confidence.

#### 2. Links and sources

- Every tool, technology, pattern, or talk mentioned MUST have a hyperlink on first reference.
- Unsourced technical claims need citations (e.g., AWS docs, Kubernetes docs, RFCs).
- Internal Pulumi features must link to their docs page under `/docs/`.
- Previously mentioned repos/tools should be re-linked if referenced again after significant distance.
- Use the `{{< github-card >}}` shortcode for repository references where appropriate.

#### 3. Meta elements and publishing readiness

- `meta_image` is present in frontmatter and is NOT the default placeholder `meta.png`.
- `meta_image` uses current Pulumi logos — outdated logos severely hurt social sharing due to caching.
- `<!--more-->` break is placed after the first 1-3 paragraphs.
- Publish `date` is set correctly (not in the far future unless intentionally scheduled).
- Author profile exists in `data/team/team/` with a corresponding avatar image in `static/images/team/`.
- Social sharing fields (`meta_desc` or equivalent) are present in frontmatter.

#### 4. SEO and titles

- Title contains the primary search term readers would use to find this content.
- Title accurately describes the content (no clickbait, no misleading counts like "Top 8" when the list has a different number of items).
- Title is under 60 characters, OR `allow_long_title: true` is set in frontmatter.
- Meta description is present, under 160 characters, and contains key search terms.
- H2 headings use answer-first phrasing matching likely search queries where appropriate.

#### 5. Content structure and motivation

- Every section opens with 1-2 sentences of motivation before diving into technical detail.
- Dense paragraphs (>4 sentences of prose) should be converted to bullet lists or broken up.
- Use subheadings liberally for scannability.
- Listicle or best-practices posts should target ~3,000 words max; if more than 12 items, suggest cutting or splitting.

#### 6. Writing quality

- Remove hedging language (covered above in AI patterns).
- Write recommendations with confidence — blog posts are thought leadership.
- Avoid self-criticism of prior Pulumi product decisions; frame improvements as user-driven progress.
- Conclusions must be strong with specific next steps, not soft or hedging.
- Avoid "easy" / "simple" per STYLE-GUIDE.md.
- Avoid filler, vague generalities, or generic platitudes.

#### 7. Product terminology and accuracy

- Use official Pulumi product names (verify against existing docs and marketing pages).
- Do not call existing features "new" — use "now supports" / "now accepts" for extensions of existing features.
- Every technical claim about a Pulumi feature must be verifiable against actual implementation.
- Flag claims about language support, API names, or UI paths that may be incorrect.

#### 8. CTAs and closing

- End-of-post CTAs must be specific to the topic domain, not generic "get started with Pulumi."
- Feature announcement posts should link to the relevant documentation.
- Include `{{< blog/cta-button >}}` or equivalent shortcode with topic-specific targets where appropriate.

#### 9. Code examples

- Code examples referenced in blog posts should be hosted in official Pulumi repos, not personal accounts.
- Examples must be correct for all claimed languages.
- Use `chooser` / `choosable` shortcodes for multi-language examples.
- Code blocks must have a language specifier for syntax highlighting.

#### 10. Images

- Comparison features need side-by-side images of the SAME view for fair comparison.
- Screenshots need alt text and 1px gray borders (mention `/add-borders` if borders are missing).
- Image file format must match actual content (e.g., a WebP file must not have a `.png` extension).
- Animated GIFs: max 1200px wide, 3 MB.

### Feature announcement posts (additional checks)

When a blog post introduces or announces a new Pulumi feature, provider, or significant functionality change, also check:

- Corresponding documentation exists in `content/docs/` for the feature being announced.
- Flag missing documentation gaps with specific suggested locations.
- `canonical_url` should point to the relevant docs page for feature announcements (NOT for non-syndicated content generally).

---

## Publishing Readiness Checklist

Summarize publishing readiness at the end of your review using this checklist (derived from BLOGGING.md):

- [ ] `<!--more-->` break present after intro paragraph
- [ ] `meta_image` is set and is not the default placeholder
- [ ] `meta_image` uses current logos for Pulumi and any third parties
- [ ] Post previews correctly on the blog home page (title, image, excerpt)
- [ ] Author profile exists in `data/team/team/` with avatar image
- [ ] All links resolve and point to correct targets
- [ ] Code examples are correct and have language specifiers
- [ ] No animated GIFs used as preview images
- [ ] Images have alt text; screenshots have borders
- [ ] Title is under 60 chars (or `allow_long_title: true` is set)
