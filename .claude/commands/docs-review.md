---
description: Review `pulumi/docs` changes for style, accuracy, and best practices
---

# Usage
# Local: /docs-review
# CI: Automatically runs on PRs

Please review the code changes in this repository and provide feedback on style, accuracy, and best practices. Compare the current branch against the `master` branch (or review uncommitted changes if present).

Provide your review as a single summary, highlighting any issues found and suggesting improvements.

Use the repository's CLAUDE.md, AGENTS.md, and STYLE-GUIDE.md for guidance on style and conventions.

Be constructive and helpful in your feedback, but don't overdo the praise. Be concise.

Always provide relevant line numbers for any issues you identify.

**Pull Request Review Criteria**:

- Always enforce `STYLE-GUIDE.md`. If not covered there, fall back to the [Google Developer Documentation Style Guide](https://developers.google.com/style).
- Check **spelling and grammar** in all files.
- Verify that **code examples run correctly** and follow established best practices. Do not suggest untested code.
- Confirm that **all links resolve** and point to the correct targets (no 404s, no mislinked paths).
- Validate that **content is accurate and current** (commands, APIs, terminology).
- Ensure **all new files end with a newline**.
- **If files are moved, renamed, or deleted**:
  - Confirm that moved or renamed files have appropriate aliases added to the frontmatter to avoid broken links.
  - Confirm that deleted files have a redirect created, if applicable.
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
