---
user-invocable: false
description: Review criteria applied to every PR review, regardless of domain.
---

# Review — Shared

Applied to every changed file in every review, in addition to the file's domain criteria. Owns the cross-cutting concerns that don't belong to any one domain.

> **v1 status — skeleton.** Until Session 2 fills this in with concrete checks, fall back to [`review-criteria.md`](review-criteria.md) for the actual checks. The headings below name the scope so domain files and entry points can reference them stably.

---

## Scope

- All link targets (internal and external) resolve and point where the prose says they do.
- Required frontmatter is present and correctly typed.
- Files moved or renamed have `aliases` covering every old path; deleted files have a redirect.
- Internal links in `content/docs/` and `content/product/` use full canonical paths, not parent-directory references.
- New files end with a newline (suppress unless the linter has *already* failed on this file — diffs don't show this reliably).
- Shortcode pairing: when one of `{name}.html` / `{name}.markdown.md` is changed, verify the other matches where appropriate.

## Criteria

Pending — inherits from [`review-criteria.md`](review-criteria.md) until Session 2 fills this in.

## Fact-check

This file does not invoke fact-check on its own. Domain files are the fact-check entry points.
