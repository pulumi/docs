# Contributing Pulumi Documentation

## Draft-first pull requests

Open new PRs as **drafts** while you iterate. Automated review (style, accuracy, fact-check) fires only when you mark a PR **ready for review**, so a draft-first flow:

- Keeps your branch out of the noisy "every push triggers a review" loop.
- Lets you push iteratively without spamming the PR with new comments each time.
- Means the eventual review reflects your finished thinking, not a half-finished commit.

When you're ready, use the **Ready for review** button on the PR page. Triage runs again to refresh labels, then the full review fires once and pins its findings to a single comment at the top of the PR. New commits afterward will mark the review **stale** but won't auto-rerun — mention `@claude` in a comment to refresh, or transition through draft and back to ready.

If your change is genuinely trivial (a typo, a one-line fix), opening directly as ready is fine — the pipeline will short-circuit on the `review:trivial` label.

## AI-assisted contributions

The repository runs a tiered review pipeline on every PR. AI-assisted contributors should know how it works so they can collaborate with it instead of fighting it.

### What ready-for-review triggers

Transitioning to **Ready for review** triggers:

1. A re-triage to refresh labels (domain, trivial / frontmatter-only short-circuits, prose-flagged signal if applicable).
1. The full Claude review (currently `claude-opus-4-7`), composed per touched domain. Findings post to a single pinned comment at the top of the PR — overflow is appended as additional pinned comments tagged `<!-- CLAUDE_REVIEW N/M -->`.

Mark the PR ready when you're done iterating, not when you start. Each ready-transition produces one full review run; thrashing through draft → ready → draft burns review budget and produces stale pinned comments.

### Author a clean commit history

If the PR was AI-drafted, leave the AI authoring trailers in commit messages (`Co-Authored-By: Claude ...`, `Generated with Claude Code`, etc.). Stripping them to disguise authorship is bad form and does not change which review runs.

### After review — three paths to refresh

A pinned review goes **stale** when you push new commits after it ran. Stale reviews don't auto-rerun. Three ways to refresh:

1. **`@claude` mention**: Leave a comment on the PR mentioning `@claude` (with or without a specific request). The re-entrant pipeline picks up new commits, runs `claude-sonnet-4-6`, and updates the existing pinned comment(s) in place. Three patterns the re-entrant pipeline understands:
    - **Fix-response** ("I addressed your feedback"): re-verifies the previous outstanding findings against the new diff and moves the resolved ones into ✅ Resolved.
    - **Dispute** ("I disagree with the X finding because Y"): re-examines the disputed finding with your evidence; either concedes cleanly or explains why it's keeping the finding.
    - **Re-verify** ("@claude refresh" / no specific request): re-checks outstanding findings only.
1. **Transition through draft and back to ready**: this re-triggers the full initial review. Use this when the PR has changed substantially since the last review.
1. **Wait for the human reviewer**: Cam's local `pr-review` skill reads the pinned comment as source of truth and refreshes it during adjudication if needed.

### Don't fight the pinned comment

The `<!-- CLAUDE_REVIEW N/M -->` comments are managed by the pipeline. Don't delete them — the re-entrant skill expects to find and edit them in place. If you accidentally delete the 1/M summary, the next run posts fresh at the bottom of the timeline; recoverable but ugly.

### Trivial and frontmatter-only short-circuits

Two label-driven short-circuits skip the full Claude review (linters still run):

- **`review:trivial`** — ≤10 added lines, prose-only body changes, ≤2 docs/blog `.md` files, no frontmatter changes, no link changes, no code blocks. Typo fixes, wording polish, small same-claim sweeps across siblings, and removal-dominant cleanup (no upper bound on deletions). Marketing/website pages (`domain:website`) get full review regardless of size.
- **`review:frontmatter-only`** — any number of docs/blog `.md` files where every change is inside the frontmatter block. Aliases sweeps, `draft: false` flips, `meta_desc` rewrites, social copy edits.

For both categories, triage runs a focused spelling/grammar pass on the relevant diff slice. If it finds anything, it posts a single advisory comment listing the concerns AND applies `review:prose-flagged` so reviewers don't miss it. The short-circuit label still applies and the full review still skips. This is a guard against rubber-stamping — a typo "fix" that introduces a typo, or a `meta_desc` rewrite with a wrong-word substitution, gets flagged before merge.

Classification is deterministic and lives in `.claude/commands/docs-review/scripts/triage-classify.py` — domain (path-precedence), triviality, and frontmatter-only detection are all path/grep rules. The model is invoked only for the prose check, only when the shell pre-classifies as trivial or frontmatter-only.

## Documentation structure

The mapping from documentation page to section and table-of-contents (TOC) is stored largely in each page's front matter, leveraging [Hugo Menus](https://gohugo.io/content-management/menus/). Menus for the CLI commands and API reference are specified in `./config.toml`.

## Hugo tips

### Short codes

To share common content across articles, use [Hugo Shortcodes](https://gohugo.io/content-management/shortcodes/). Place a .html file in the [layouts/shortcodes] folder. To include it in a page, use syntax `{{< my-shortcode >}}`

For example, our custom [`cleanup`](layouts/shortcodes/cleanup.html) shortcode can be included in .md files, to include common text about cleaning up stack resources:

```plain
{{< cleanup >}}
```

HTML layouts can include other layouts inside the [layouts/partials](layouts/partials) directory, e.g.:

```plain
{{ partial "head.html" . }}
```

### Front matter

Front matter is defined as a YAML block at the top of a Markdown document that defines metadata about the page. Pulumi docs pages often include the following front matter variables:

- `aliases`: A list of relative URLs that should point to the content in this page. When moving or renaming a page, you must add an `alias` entry for the old path of the page relative to the `content/` folder.
- `allow_long_title`: Set to `true` in order disable length validation on the `title` attribute.
- `block_external_search_index`: Set to `true` to prevent crawlers from indexing the page.
- `h1`: If specified, the `<h1>` at the top of the page will use this value instead of the value in the `title` attribute.
- `menu`: Specifies where a page appears in the document navigation tree.
- `meta_desc`: Required (unless `redirect_to` is set), at least 50 characters, no longer than 160 characters. This displays as the description of the page in web search results.
- `meta_image`: Blog posts only. Relative path to an OpenGraph image (1200×628) for social media previews and the blog home page. The image must be a PNG file for compatibility.
- `feature_image`: Blog posts only. Relative path to a high-resolution hero image (1884×1256) displayed at the top of the blog post page.
- `meta_title`: If specified, the meta title (for OpenGraph) will use this value instead of the value in the `title` attribute.
- `redirect_to`: The relative or absolute URL of a permanent redirect.
- `title`: Required (unless `redirect_to` is set), 60 characters or less. This controls the default value for the `<title>` tag as well at the top level `<h1>` in the document.
- `title_tag`: If specified, the `<title>` tag on the rendered call will use this value instead of the `title` attribute.

You can also define arbitrary front-matter variable in the YAML section at the top of a file and refer to that same value in the page content. For instance, the you could add the following front matter `foo: "bar"`, and then reference the variable in markdown with the syntax `{{< param foo >}}`.

For more information, see [Front Matter](https://gohugo.io/content-management/front-matter/) in the Hugo docs.
