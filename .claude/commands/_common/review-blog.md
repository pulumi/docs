---
user-invocable: false
description: Review criteria for blog posts and customer stories. Fact-check-first; heightened scrutiny by default.
---

# Review — Blog

Applied to blog posts (`content/blog/`) and customer stories (`content/customers/`). These are usually drafted whole-file (often with AI assistance) rather than edited incrementally, so scrutiny is heightened by default and the whole file is in scope.

> **v1 status — skeleton.** Until Session 2 fills this in, fall back to [`review-criteria.md`](review-criteria.md) (the Blogs/Marketing role-specific section) for the actual checks. The headings below define the v1 contract.

> **Fact-check-first treatment.** For blog content, fact-check is the headline finding bucket — get it right before commenting on AI-writing patterns or structure.

---

## Scope

- **Whole-file read** is mandatory. Diff-only is not enough — AI-drafted blogs hallucinate in the surrounding prose, not just the changed lines.
- Pre-existing extraction is **always on** for blog files (see below).

## Criteria

Pending — inherits from [`review-criteria.md`](review-criteria.md) (Blogs/Marketing role-specific section) until Session 2 fills this in.

## Pre-existing issues (always on)

Blog files are usually new in their entirety, so the diff/pre-existing distinction blurs. Render every finding under 🚨 Outstanding when the post is new; for incremental edits to existing posts, separate diff-introduced from pre-existing per the standard rules. Cap at 15 per file.

Pre-existing scope per the blog-domain plan: everything from `review-docs.md`, plus unsourced claims, temporally-rotted feature claims ("a new feature in v3.X" where v3.X is years old), broken `{{< github-card >}}` references, missing author avatars.

## Fact-check

Invoke [`pr-review/references/fact-check.md`](../pr-review/references/fact-check.md) with:

- Files: the changed `content/blog/**` / `content/customers/**` files
- Scrutiny: `heightened` (always)

CI fact-check is public-sources-only — see `docs-review-ci.md`. Notion and Slack are explicitly excluded for blog content in CI because blog claims are the most likely to surface internal context that shouldn't be in a public PR comment.
