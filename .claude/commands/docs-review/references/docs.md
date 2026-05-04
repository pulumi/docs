---
user-invocable: false
description: Review criteria for technical documentation under content/docs, content/learn, content/tutorials, content/what-is.
---

# Review — Docs

Applied to documentation pages: technical reference, conceptual docs, tutorials, learn modules, and what-is pages. Default scrutiny is `standard` (diff-only).

---

## Scope

- Diff-only by default. Surrounding prose is assumed sound.
- Whole-file read is opt-in (see §Pre-existing issues (opt-in) below).

## Criteria

The following reference files apply alongside the docs-specific checks below. Consult each as content in the diff triggers a relevant rule:

- `docs-review:references:shared-criteria` — every file (links, frontmatter, shortcodes)
- `docs-review:references:code-examples` — wherever code appears
- `docs-review:references:prose-patterns` — prose-bearing content
- `docs-review:references:image-review` — wherever images appear

The priorities below are ordered for **output rendering** — fact-check findings render before style findings — but investigate as content triggers each.

### Priority 1 — Fact-check first

Invoke `docs-review:references:fact-check` (`scrutiny=standard` by default). Bump scrutiny to `heightened` when the file is a new page (not previously in `content/`) or a whole-file rewrite (>70% of lines changed). In docs, pay particular attention to:

- **CLI flag existence.** `pulumi <subcommand> --<flag>` claims must match the current CLI source. Memorized flag lists are not authoritative.
- **Resource API surface.** Resource property claims (e.g., `aws.s3.Bucket` accepts `versioning`) must match the provider's registry schema source (`gh api repos/pulumi/pulumi-<provider>/contents/...`).
- **Version-availability claims.** "Available in v3.230+", "supported on Windows."
- **Output-format claims.** `pulumi up` / `preview` / `stack output` example output must reflect what the current CLI prints. Old-style output formats ("Performing changes:" when the CLI now prints "Updating (dev)") are deprecated-terminology findings.
- **Feature-existence claims.** "Pulumi ESC supports rotation for AWS." If the diff asserts a capability, verify it.

### Priority 2 — Code correctness

Snippet-level checks (syntax, imports, language idioms, language casing) live in `docs-review:references:code-examples`.

### Priority 3 — Cross-references and link integrity

- **Link target exists.** Every internal link added or modified in the diff must resolve to an existing page in the PR's snapshot (`gh api repos/<owner>/<repo>/contents/<path>`). Missing targets are 🚨.
- **Anchor resolves.** `/docs/foo/#bar` requires `#bar` to exist on `/docs/foo/`. Verify by fetching the target file and grep for `## Bar` / `### Bar` (or whatever heading level the slug matches).
- **Orphan cross-refs after moves.** If the PR moves a page, every inbound link elsewhere in `content/docs/` or `content/product/` must be updated (aliases handle outsider/historic links, but the repo's own internal links should use the new canonical path).
- **Missing cross-link to a canonical concept page.** When the diff text mentions a Pulumi concept that has a canonical doc page (stacks, providers, components, ESC environments, projects, programs, policy packs), and no occurrence of the term in the file is hyperlinked, flag it once per concept. Quote the most prominent unlinked occurrence; propose the link target (e.g., `[stacks](/docs/iac/concepts/stacks/)`). Do not flag the page whose subject *is* the concept (a stacks page doesn't need to link "stacks" in its own intro). Do not flag terms outside Pulumi's vocabulary.

### Priority 4 — Terminology and product accuracy

Vale catches product-name capitalization, the Pulumi Policies singular-verb rule, "public preview" vs "public beta", and preferred-terminology pairs from `STYLE-GUIDE.md` (surfaced under ⚠️ Low-confidence per `docs-review:references:output-format` §Style nits). The reviewer's job here is **first-mention acronym expansion** that Vale doesn't cover: when a product acronym (ESC, IDP, IaC) appears in the diff for the first time in the file, propose `Pulumi ESC (Environments, Secrets, and Configuration)` on first mention. Subsequent mentions use the short form.

`data/glossary.toml` is the authoritative term list for glossary cross-references.

### Priority 5 — Prose patterns and spelling/grammar

Apply `docs-review:references:prose-patterns` and `docs-review:references:spelling-grammar`.

### Priority 6 — SEO and discoverability

Quote-and-rewrite mandate. Apply most strictly to **what-is pages** (`content/what-is/`) and **concept docs**; less strictly to reference and tutorial content where the patterns naturally differ.

- **Title matches page subject.** Quote the `title:` frontmatter and the page's first paragraph; flag when the page's actual subject is materially different from what the title claims.
- **Quotable definition for what-is and concept pages.** The opening 1–2 sentences should answer "what is X" as a standalone definition that could be quoted by an AI tool without surrounding context. Quote the opening; flag fluff intros ("In this guide, we'll explore...") and propose a direct definition.
- **Answer-first H2 headings on concept content.** Question-style or how-style headings ("How does Pulumi ESC handle secrets?") rank better for AI answer extraction than label-style ("ESC overview"). Quote the heading; propose an answer-first rewrite. Don't flag label headings on reference docs (API listings, CLI flags) — labels are correct there.
- **Semantic chunking.** Each H2 section should cover one focused concept. Flag when a single section mixes definition, history, benefits, and a tutorial; quote the section's first heading and propose a split with new H2s.
- **Down-funnel specificity.** Concept docs that introduce a feature without showing a concrete integration or use case are too generic to be cited. Flag the most generic section; propose adding a specific scenario, integration, or edge case.
- **Numbered, executable steps for "get started" / "how to" sections.** Quickstart prose that doesn't break into numbered steps with copy-pasteable commands. Quote the section; propose a numbered list with explicit `pulumi …` commands.

### Priority 7 — Callouts and shortcodes

- **`{{% notes %}}`** uses one of `info` / `tip` / `warning`. A misspelled `type=` silently renders the default and looks wrong.
- **`{{< chooser >}}`** / **`{{< choosable >}}`** pairs must match: every language listed in the `chooser` needs a corresponding `choosable` block, and vice versa.
- **Percent vs angle-bracket syntax.** `{{% ... %}}` for shortcodes that process Markdown (notes, choosable, details). `{{< ... >}}` for shortcodes that emit pre-rendered content (cleanup, example). See `STYLE-GUIDE.md` §Shortcode syntax.

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

Scope of pre-existing findings for docs: broken links/anchors, orphan cross-refs, deprecated terminology, within-file terminology inconsistencies. These render in the 💡 bucket per `docs-review:references:output-format` (cap per output-format). Skip style nits (heading case, list numbering, product-name capitalization, banned-word substitutions) -- the linter (markdownlint, Prettier) and Vale own those.

## Do not flag

- **Vague editorial feedback without quote-and-rewrite.** "Could be clearer" / "consider reorganizing this paragraph" without a quoted construction and a specific proposed rewrite is editorial vagueness, not a review finding. Concrete prose, structural, and SEO/AEO suggestions (apply `docs-review:references:prose-patterns`; split a mixed-concept H2; rewrite a label-style heading as answer-first; convert prose-quickstart to numbered steps) ARE in scope -- but every finding must quote the offending text and propose the fix.
- **Superseded terminology in historical context.** When a doc describes old behavior intentionally (e.g., "before v3.0, this was called X"), don't flag the old name as deprecated terminology.
- **Anything Vale catches.** Product-name capitalization, Policies-singular, public-preview/public-beta, click→select, banned words, difficulty qualifiers — all surface via `.vale-findings.json` per `docs-review:references:output-format` §Style nits. Don't double-flag.
