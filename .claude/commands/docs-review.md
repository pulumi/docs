---
description: Review `pulumi/docs` changes for style, accuracy, and best practices
---

# Usage
# Local: /docs-review [pr-number]
# CI: Automatically runs on PRs

You will review documentation changes and provide feedback on style, accuracy, and best practices.

## For Local Usage: Determine Review Scope

**If a PR number is provided** ({{arg}}):
- Use `gh pr view {{arg}}` to retrieve the PR title, description, and metadata
- Use `gh pr diff {{arg}}` to get the full diff of changes
- Review the PR changes according to the criteria below

**If no PR number is provided**:
- Use `git status` to check for uncommitted changes
- Use `git diff master` to compare current branch against master
- If on master with uncommitted changes, review those changes
- Review the changes according to the criteria below

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
- **Code examples** must run correctly and follow best practices:
  - Do not suggest untested code.
  - Examples should show realistic use cases, not contrived demos.
  - Examples should handle errors appropriately.
  - Examples should follow language-specific best practices.
- **Files moved, renamed, or deleted**:
  - Confirm that moved or renamed files have appropriate aliases added to the frontmatter to avoid broken links.
  - Confirm that deleted files have a redirect created, if applicable.
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
  - Verify URL structure follows conventions.
- When reviewing **Documentation**: Serve the role of a professional technical writer. Review for:
  - Clarity and conciseness.
  - Logical flow and structure.
  - No jargon unless defined.
  - Avoid passive voice.
  - Avoid overly complex sentences. Shorter is usually better.
  - Avoid superlatives and vague qualifiers.
  - Avoid unnecessary filler words or sentences.
  - Be specific and provide examples.
  - Use consistent terminology.
- When reviewing **Blog posts or marketing materials**: Serve the role of a professional technical blogger. Review for:
  - Clear, engaging titles.
  - Strong opening that hooks the reader.
  - Clear structure with headings and subheadings.
  - Concise paragraphs (3-4 sentences max).
  - Use of lists and bullet points for readability.
  - Reject filler, vague generalities, or AI-generated slop.
  - Avoid clickbait phrasing.
  - Clear call-to-action at the end.
