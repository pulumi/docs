---
user-invocable: false
description: Triage prose-check prompt. Loaded only when triage-classify.py classifies a PR as trivial or frontmatter-only. Classification itself is deterministic and lives in triage-classify.py.
---

# PR Triage — Prose Check

You are doing a focused spelling/grammar pass on a small pull request — either **trivial** (≤5 lines of prose-only body changes) or **frontmatter-only** (every change is inside a Hugo frontmatter block).

This is a fast, narrow pass. Output exactly one JSON object on a single line, no prose, no code fences:

```json
{"prose_concerns":["path/to/file.md:LINE — issue (suggested fix)", ...]}
```

If you find no issues, output `{"prose_concerns":[]}`. Be specific so the author can act without re-reading the diff. One concern per element. Cap at the 15 most important findings.

## Frontmatter-only PRs: scope

Inspect only prose-bearing fields:

- `title`, `linktitle`
- `meta_desc`, `description`
- `social_image_text`, `og_description`
- `excerpt`, `summary`

Skip data fields entirely:

- `aliases`, `slug`, `url`, `permalink`
- `tags`, `categories`, `keywords`, `topics`
- `draft`, `date`, `weight`, `expiryDate`, `publishDate`
- `author`, `authors`
- `cluster_*`, `block_*`, layout/template directives
- Any field whose value is a list of paths, URLs, identifiers, or dates.
