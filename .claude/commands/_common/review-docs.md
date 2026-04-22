---
user-invocable: false
description: Review criteria for technical documentation under content/docs, content/learn, content/tutorials, content/what-is.
---

# Review — Docs

Applied to documentation pages: technical reference, conceptual docs, tutorials, learn modules, and what-is pages.

> **v1 status — skeleton.** Until Session 2 fills this in, fall back to [`review-criteria.md`](review-criteria.md) (the Documentation role-specific section) for the actual checks. The headings below define the v1 contract.

---

## Scope

- Diff-only by default. Surrounding prose has been reviewed previously and is assumed sound.
- Whole-file read is *opt-in* per the pre-existing extraction rule below.

## Criteria

Pending — inherits from [`review-criteria.md`](review-criteria.md) (Documentation role-specific section) until Session 2 fills this in.

## Pre-existing issues (opt-in)

Extract pre-existing issues from a touched file when:

- The file is large (>500 lines), OR
- The PR substantively edits the file (>30 changed lines OR a top-level structural change), OR
- The file is a new page (every line is, by definition, "in the diff" — but rendering them as 🚨 Outstanding would drown the author).

Pre-existing scope per the docs-domain plan: broken links/anchors, orphan cross-refs, product name capitalization, deprecated terminology, missing code-block languages, within-file terminology inconsistencies. Cap at 15 per file.

## Fact-check

Invoke [`pr-review/references/fact-check.md`](../pr-review/references/fact-check.md) with:

- Files: the changed `content/docs/**`, `content/learn/**`, `content/tutorials/**`, `content/what-is/**` files
- Scrutiny: `standard`
- Bump to `heightened` when the file is a new page or a whole-file rewrite

CI fact-check is public-sources-only — see `docs-review-ci.md`.
