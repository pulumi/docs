---
user-invocable: false
description: Review criteria for technical documentation under content/docs, content/learn, content/tutorials, content/what-is.
---

# Review — Docs

Applied to documentation pages: technical reference, conceptual docs, tutorials, learn modules, and what-is pages. Default scrutiny is `standard` because docs usually get edited incrementally -- surrounding prose has been reviewed previously and carries context from prior review.

---

## Scope

- Diff-only by default. Surrounding prose is assumed sound.
- Whole-file read is opt-in per the pre-existing extraction rule below.

## Criteria

Apply [`review-shared.md`](review-shared.md) first, then these docs-specific checks.

### API and resource accuracy

- **Property names match the provider's current schema.** When the diff references a resource property (e.g., `bucket.versioning`, `cluster.nodePools`), cross-reference against the provider's registry schema. The authoritative source is the registry tree for that provider (`gh api repos/pulumi/pulumi-<provider>/contents/...`), not a memory of past API shapes.
- **Language-specific casing.** Pulumi resource properties are camelCase in TypeScript/JavaScript, snake_case in Python, PascalCase in C# and Go. If the same property appears in multiple language tabs (or a `chooser` block), every tab must use the correct casing for that language.
- **Required vs optional arguments.** Examples that omit a required argument should be flagged -- the example won't run. Examples that include every optional argument verbatim should not be flagged; that's a style preference, not an error.
- **Enum values.** Enum-typed properties (e.g., `aws.ec2.InstanceType`) must use values the provider accepts. A typo here means the example fails at preview time.

### Cross-references between docs pages

- **Link target exists.** Every internal link added or modified in the diff must resolve to an existing page in the PR's snapshot (`gh api repos/<owner>/<repo>/contents/<path>`). Missing targets are 🚨.
- **Anchor resolves.** `/docs/foo/#bar` requires `#bar` to exist on `/docs/foo/`. Verify by fetching the target file and grep for `## Bar` / `### Bar` (or whatever heading level the slug matches).
- **Orphan cross-refs after moves.** If the PR moves a page, every inbound link elsewhere in `content/docs/` or `content/product/` must be updated (aliases handle outsider/historic links, but the repo's own internal links should use the new canonical path).

### Code examples

- **Syntax.** No unclosed brackets, broken indentation, or obvious typos. A code block that doesn't parse in its language is a 🚨 finding.
- **Imports.** Imported symbols exist in the referenced package; package names are correct (`@pulumi/aws`, not `@pulumi/pulumi-aws`); no unused imports cluttering a teaching example.
- **Idiomatic per language.** `async`/`await` for TypeScript promise-returning APIs. Context managers in Python where appropriate. `err != nil` handling in Go. Don't flag cosmetic style; flag actual anti-patterns that would lead readers to wrong habits.
- **Referenced `static/programs/` snippets.** When a doc page uses `{{< example-program >}}`, the referenced program must exist in `static/programs/` and compile under each language variant the page advertises. Cross-reference to `CODE-EXAMPLES.md` for the testing contract.
- **Proposed fixes compile.** If you suggest a code replacement, it must itself pass these checks. Don't suggest untested code.

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

Scope of pre-existing findings for docs: broken links/anchors, orphan cross-refs, product-name capitalization, deprecated terminology, within-file terminology inconsistencies. These render in the 💡 bucket per [`docs-review-core.md`](docs-review-core.md). Cap at 15 per file. Skip style nits (heading case, list numbering) -- the linter owns those.

## Fact-check

Invoke [`fact-check.md`](fact-check.md) with:

- **Files:** the changed `content/docs/**`, `content/learn/**`, `content/tutorials/**`, `content/what-is/**` files
- **Scrutiny:** `standard`
- **Bump to `heightened`** when the file is a new page (not previously in `content/`) or a whole-file rewrite (>70% of lines changed)

CI fact-check is public-sources-only -- see `docs-review-ci.md`.

## Do not flag

- **Prose style within a paragraph.** "Could be clearer" / "consider reorganizing this paragraph" is editorial feedback, not a review finding. Flag factual errors, broken links, and code bugs, not sentence rhythm.
- **Property-name casing that matches the language's convention.** `bucketName` in TypeScript is correct; `bucket_name` in Python is correct. Flag only when the casing is wrong *for that language*, not when you prefer a different convention.
- **Code examples that omit optional arguments.** "You could also pass `tags: {...}`" is unsolicited enrichment. Docs deliberately keep starter examples minimal. Flag if a required argument is missing; don't flag for completeness.
- **CLI examples without output.** Not every code block needs a paired ` ```output ` block. Flag when the prose *claims* specific output and the block is missing; don't flag as a general "you should show what this prints."
- **Superseded terminology in historical context.** When a doc describes old behavior intentionally (e.g., "before v3.0, this was called X"), don't flag the old name as deprecated terminology.
