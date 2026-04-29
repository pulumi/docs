---
user-invocable: false
description: Review criteria for technical documentation under content/docs, content/learn, content/tutorials, content/what-is.
---

# Review — Docs

Applied to documentation pages: technical reference, conceptual docs, tutorials, learn modules, and what-is pages. Default scrutiny is `standard` (diff-only).

---

## Scope

- Diff-only by default. Surrounding prose is assumed sound.
- Whole-file read is opt-in per the pre-existing extraction rule below.

## Criteria

The following reference files apply alongside the docs-specific checks below. Consult each as content in the diff triggers a relevant rule:

- `docs-review:references:shared-criteria` — every file (links, frontmatter, shortcodes)
- `docs-review:references:code-examples` — wherever code appears
- `docs-review:references:prose-patterns` — prose-bearing content
- `docs-review:references:image-review` — wherever images appear

### API and resource accuracy

Snippet-level checks live in `code-examples.md`. Docs-specific anchor: when the diff references a resource property, cross-reference the provider's registry schema source (`gh api repos/pulumi/pulumi-<provider>/contents/...`), not memory.

### Cross-references between docs pages

- **Link target exists.** Every internal link added or modified in the diff must resolve to an existing page in the PR's snapshot (`gh api repos/<owner>/<repo>/contents/<path>`). Missing targets are 🚨.
- **Anchor resolves.** `/docs/foo/#bar` requires `#bar` to exist on `/docs/foo/`. Verify by fetching the target file and grep for `## Bar` / `### Bar` (or whatever heading level the slug matches).
- **Orphan cross-refs after moves.** If the PR moves a page, every inbound link elsewhere in `content/docs/` or `content/product/` must be updated (aliases handle outsider/historic links, but the repo's own internal links should use the new canonical path).

### CLI commands

- **Flags exist.** `pulumi <subcommand> --<flag>` claims must match the current CLI -- verify via `gh api repos/pulumi/pulumi/contents/<cli-source-path>` or by reading release notes for the referenced version. Memorized flag lists are not authoritative.
- **Output matches reality.** `pulumi up` / `pulumi preview` / `pulumi stack output` example output should reflect what the current CLI actually prints. Old-style output formats ("Performing changes:" when the CLI now prints "Updating (dev)") are deprecated-terminology findings.

### Terminology and style

Reference `STYLE-GUIDE.md` and `data/glossary.toml` for the authoritative lists; do not duplicate them here. Watchlist:

- **Product names.** "Pulumi IaC" / "Pulumi ESC" / "Pulumi IDP" / "Pulumi Cloud" / "Pulumi Insights" / "Pulumi Policies". Expand acronyms on first mention; use the short form after.
- **Singular "Pulumi Policies."** `STYLE-GUIDE.md` says it's a singular proper noun. Verb agreement follows (e.g., "Pulumi Policies enforces," not "enforce").
- **"public preview" not "public beta."**
- **Preferred pairs.** "Pulumi package" vs "native language package" -- see `STYLE-GUIDE.md` §Preferred terminology.

### Callouts and shortcodes

- **`{{% notes %}}`** uses one of `info` / `tip` / `warning`. A misspelled `type=` silently renders the default and looks wrong.
- **`{{< chooser >}}`** / **`{{< choosable >}}`** pairs must match: every language listed in the `chooser` needs a corresponding `choosable` block, and vice versa.
- **Percent vs angle-bracket syntax.** `{{% ... %}}` for shortcodes that process Markdown (notes, choosable, details). `{{< ... >}}` for shortcodes that emit pre-rendered content (cleanup, example). See `STYLE-GUIDE.md` §Shortcode syntax.

### SEO and discoverability

These are the feasible, concrete rules from `seo-analyze:references:aeo-checklist` applied at review time. Quote-and-rewrite mandate. The full AEO scoring pass still belongs to `/seo-analyze` for deeper analysis; these are the items that catch on a normal review. Apply most strictly to **what-is pages** (`content/what-is/`) and **concept docs**; less strictly to reference and tutorial content where the patterns naturally differ.

- **Title matches page subject.** Quote the `title:` frontmatter and the page's first paragraph; flag when the page's actual subject is materially different from what the title claims.
- **Quotable definition for what-is and concept pages.** The opening 1–2 sentences should answer "what is X" as a standalone definition that could be quoted by an AI tool without surrounding context. Quote the opening; flag fluff intros ("In this guide, we'll explore...") and propose a direct definition.
- **Answer-first H2 headings on concept content.** Question-style or how-style headings ("How does Pulumi ESC handle secrets?") rank better for AI answer extraction than label-style ("ESC overview"). Quote the heading; propose an answer-first rewrite. Don't flag label headings on reference docs (API listings, CLI flags) — labels are correct there.
- **Semantic chunking.** Each H2 section should cover one focused concept. Flag when a single section mixes definition, history, benefits, and a tutorial; quote the section's first heading and propose a split with new H2s.
- **Down-funnel specificity.** Concept docs that introduce a feature without showing a concrete integration or use case are too generic to be cited. Flag the most generic section; propose adding a specific scenario, integration, or edge case.
- **Numbered, executable steps for "get started" / "how to" sections.** Quickstart prose that doesn't break into numbered steps with copy-pasteable commands. Quote the section; propose a numbered list with explicit `pulumi …` commands.

## Pre-existing issues (opt-in)

Extract pre-existing issues from a touched file when any of:

- The file is large (>500 lines), OR
- The PR substantively edits it (>30 changed lines OR a top-level structural change), OR
- The file is a new page (every line is, by definition, "in the diff" -- but rendering them all as 🚨 Outstanding would drown the author).

**What counts as a "top-level structural change":** a change that reshapes the file's outline, not one that edits content within a fixed outline. Concretely, any of:

- Adding, removing, or renaming an H2 heading.
- Reordering H2 sections (changing their relative positions in the file).
- Moving an existing H2's content to a new file, or pulling new content into the file under a new H2.
- Changing the H1 (`title:`) in frontmatter.

Not a top-level structural change: edits inside an existing H2, adding/removing H3s under an unchanged H2, code-block updates, wording tweaks.

Scope of pre-existing findings for docs: broken links/anchors, orphan cross-refs, product-name capitalization, deprecated terminology, within-file terminology inconsistencies. These render in the 💡 bucket per [`output-format.md`](output-format.md). Cap at 15 per file. Skip style nits (heading case, list numbering) -- the linter owns those.

## Fact-check

Invoke [`fact-check.md`](fact-check.md) with:

- **Files:** the changed `content/docs/**`, `content/learn/**`, `content/tutorials/**`, `content/what-is/**` files
- **Scrutiny:** `standard`
- **Bump to `heightened`** when the file is a new page (not previously in `content/`) or a whole-file rewrite (>70% of lines changed)

CI fact-check is public-sources-only -- see `ci.md`.

## Do not flag

- **Vague editorial feedback without quote-and-rewrite.** "Could be clearer" / "consider reorganizing this paragraph" without a quoted construction and a specific proposed rewrite is editorial vagueness, not a review finding. Concrete prose, structural, and SEO/AEO suggestions (apply `prose-patterns.md`; split a mixed-concept H2; rewrite a label-style heading as answer-first; convert prose-quickstart to numbered steps) ARE in scope -- but every finding must quote the offending text and propose the fix.
- **Superseded terminology in historical context.** When a doc describes old behavior intentionally (e.g., "before v3.0, this was called X"), don't flag the old name as deprecated terminology.
