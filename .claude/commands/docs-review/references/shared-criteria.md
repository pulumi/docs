---
user-invocable: false
description: Review criteria applied to every PR review, regardless of domain.
---

# Review — Shared

Applied to every changed file in every review, in addition to the file's domain criteria. Owns the cross-cutting concerns that don't belong to any one domain.

Everything here is domain-neutral. If a check only matters for docs, blogs, infra, or programs, it goes in the corresponding domain file, not here.

---

## Scope

- All link targets (internal and external) resolve and point where the prose says they do.
- Required frontmatter is present and correctly typed.
- Files moved or renamed have `aliases` covering every old path; deleted files have a redirect.
- Internal links in `content/docs/` and `content/product/` use full canonical paths, not parent-directory references.
- Shortcode pairing: when one of `{name}.html` / `{name}.markdown.md` is changed, verify the other matches where appropriate.

## Criteria

### Links

- **Internal links resolve.** For every added or changed internal link, confirm the target file exists in the PR snapshot (use `gh pr view --json files` + `gh api repos/<owner>/<repo>/contents/<path>` for files not in the diff). Anchor links (`#section`) must point at an existing heading on the target page.
- **Canonical-path style.** Internal links in `content/docs/` and `content/product/` use the full canonical path (e.g., `/docs/iac/concepts/stacks/`). Flag parent-relative references (`../stacks/`) — they break when pages move.
- **External links resolve** at HEAD time (200 OK or a 3xx that lands somewhere live). Don't chase deep link-health across the whole site; only verify the ones the PR adds or modifies.
- **Link text is descriptive.** Flag `[here]`, `[click here]`, `[this link]`, or bare URLs used as link text. This is a `STYLE-GUIDE.md` rule, not a heuristic.

### Frontmatter

- Required fields per layout (`title`, `description`/`meta_desc`, `date` for time-sensitive content). Validate as YAML; unmatched quotes and inconsistent indentation break the whole site build, not just the page.
- **`description` / `meta_desc` length.** Aim for 120–160 characters. Search engines truncate around 160; under 120 leaves the snippet sparse. (Caught at pre-commit by `lint-markdown.js` `checkPageMetaDescription` for staged files; this rule covers cases that bypass the hook.)
- **`aliases` on move/rename.** When `gh pr view --json files` shows a file under its new path and the diff shows no content change to the old path, the moved file MUST have every prior URL listed in `aliases:`. Missing aliases are a ranking-destroying SEO failure -- flag as 🚨 every time, with the exact frontmatter addition as a suggestion block.
- **S3 redirects for non-Hugo files.** Deleted files outside Hugo's content management need entries in `scripts/redirects/*.txt` (format `source-path|destination-url`). See `AGENTS.md` §Moving and Deleting Files.

### Shortcode pairing

Several shortcodes have both `.html` and `.markdown.md` variants in `layouts/shortcodes/`. When the PR changes one, check the other for equivalent parameter names, defaults, and conditional logic. The markdown variant must preserve semantic comment markers (e.g., `<!-- chooser:type -->`) that the markdown pipeline reads.

HTML styling changes that don't affect output semantics need not propagate to the markdown variant; the reverse is also true. The check is "do the two variants still render equivalent content?", not "are they byte-identical?".

### Suggestion format

When a finding has a concrete fix, render it as a GitHub suggestion block inside the finding's comment body:

````markdown
```suggestion
<exact replacement for the cited lines>
```
````

Use suggestion blocks for replacements of five lines or fewer. For larger rewrites, describe the change in prose -- a 40-line suggestion block is unreviewable.

### Linter boundary

The following are owned by the lint job (`scripts/lint/lint-markdown.js` and peers). Do not restate findings the linter already catches:

- trailing newlines / trailing whitespace
- ordered-list `1.` numbering convention
- heading case (linter catches inconsistency; this file catches accuracy of content, not stylistic consistency)
- title length / meta description length / `meta_image` placeholder (`lint-markdown.js`'s `checkPageTitle`, `checkPageMetaDescription`, `checkMetaImage`)

A diff can't reliably show a missing trailing newline, so even if a file "looks" like it's missing one, don't claim it in a finding. The linter will either pass or fail on this file; that's the answer.

**Note:** image alt text (`MD045`) and fenced-code-block language specifiers (`MD040`) are *not* currently enforced by the linter — both rules are disabled in `.markdownlint-base.json`. Until they're enabled, those checks belong to the review skill: alt text is covered by `image-review.md`, code-block language by `code-examples.md`. Don't claim "the linter catches this" for either.

### Indented prose

- **Indented prose isn't accidentally rendered as a code block.** Markdown treats 4-space-indented lines as code. Flag indented paragraph text that's not meant to be code (common in nested lists where a continuation line was over-indented and turned silently into a code block in rendered output).

## Fact-check

This file does not invoke fact-check on its own. Domain files are the fact-check entry points.

## Do not flag

These are DO-NOT items from [`output-format.md`](output-format.md) restated for cross-cutting cases:

- **"This link might 404 eventually."** Speculative link-rot is not a finding. Either the link is broken now or it isn't.
- **"You could also link to X."** Unsolicited "also consider linking to" suggestions belong in a separate improvement pass, not in this review.
- **"Consider using a different heading level."** Heading hierarchy linting belongs to the linter. Only flag content errors (wrong target, stale anchor, factually incorrect), not stylistic hierarchy preferences.
- **Informational-only observations.** "I noticed this file was last updated in 2022" is noise unless it's tied to a concrete fix.
- **Findings on files the PR doesn't touch.** Even when scanning a linked page to verify a cross-reference, the finding goes against the file in this PR, not the page you navigated to.
