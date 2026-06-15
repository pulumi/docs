# AGENTS.md — Pulumi website (Hugo): docs, blog, marketing, and example programs

---

## Build / Test / Lint Workflow

> **Note:** For comprehensive details on the build system, deployment infrastructure, and CI/CD workflows, see `BUILD-AND-DEPLOY.md`. This file is large, so read only specific sections as needed to conserve tokens.

> **Never push directly to `master`.** Always create a branch and open a PR. Direct pushes to `master` bypass review and CI checks. (Server-side branch protection is planned but not yet in place.)

Agents must use these exact commands:

- Install deps: `make ensure`
- Build site: `make build`
- Serve locally on port 1313 (accessible with curl):  
  - Normal: `make serve` 
  - With asset rebuilds: `make serve-all`
- Lint: `make lint` (must pass before commit/merge)
- Lint prose: `make lint-prose` (Vale; nags, never blocks. Also surfaces in pinned PR reviews.)
- Format: `make format`
- Run all tests: `make test`
- Run specific program test:  
  `ONLY_TEST="program-name" ./scripts/programs/test.sh`
- Fix trailing spaces:  
  `sed -i '' 's/[[:space:]]*$//' file1.md file2.md ...`

Do not substitute other tools or commands, or change `package.json` to use pnpm (Yarn/npm only).

---

## Code & Content Rules

For all content files, follow `STYLE-GUIDE.md`. If a rule is not covered there, fall back to the [Google Developer Documentation Style Guide](https://developers.google.com/style). Do not invent new style conventions; ask for clarification if something is ambiguous.

Meta files like this one, `BUILD-AND-DEPLOY.md`, and agent instruction/skill files (e.g., `.claude/commands/*.md`) are exempt from formatting rules (heading case, trailing newlines, etc.).

For all content files (docs, blogs, tutorials, etc.):

- **Markdown**: Must always end with a newline.
- **Headings**:  
  - H1 = Title Case  
  - H2+ = Sentence case
- **TypeScript/JavaScript**: Must follow `tsconfig.json` settings. No comments unless explicitly requested.
- **TypeScript program files** (`static/programs/`): Use hand-written constructor style — resource name and opening `{` on the same line, `}, {` inline when an opts argument follows:
  ```typescript
  const r = new SomeResource("name", {
      prop: value,
  }, { 
      provider: p,
  });
  ```
  Do NOT use Prettier's multi-arg style where name, props, and opts are each on separate indented lines.
- **File Placement**:  
  - Docs go under `content/docs/...`
  - Blog posts go under `content/blog/...`
  - Other content goes into appropriate `content/...` subdirectory
  - Code examples go under `/static/programs` with a language suffix in the filename.  
  - Mirror the structure of existing content; do not invent new layouts.
- **Includes**: Use Hugo shortcodes for shared content, never raw Markdown copy-paste.  
- **Naming**: Use lowercase for non-proper nouns (e.g. “stack,” not “Stack”).  
- **Ordered Lists**: Every item begins with `1.` to minimize diff noise.
- **Diagrams**: Prefer Mermaid diagrams over ASCII art. The site renders Mermaid natively via a Hugo code block hook (`layouts/_default/_markup/render-codeblock-mermaid.html`). Use ` ```mermaid ` fenced code blocks. See [Mermaid docs](https://mermaid.js.org/) for syntax.
- **Images on template-driven pages**: Place new images for template-driven pages (homepage, product pages, event pages, case studies — anything rendered through `layouts/partials/template-partials/*`) under `assets/fingerprinted/`, mirroring the path you'd use under `static/`. The template partials route every `<img>` through `layouts/partials/fingerprinted-img.html`, which content-hashes filenames, converts rasters to WebP, and generates responsive `srcset`s. Frontmatter paths still look like `/images/foo.svg`; the partial resolves them. Missing assets cause a build panic, so there is no silent fallback. `meta_image` and assets used by non-template layouts can stay in `static/`.
- **Spelling/Grammar**: Always correct errors. Use American English spelling.

---

## Moving and Deleting Files

**⚠️ SEO CRITICAL**: Missing aliases on moved files break search rankings and external links.

Use the `/move-doc` skill for Hugo content files — it handles `git mv`, alias injection, link updates, and verification. For non-Hugo files (generated content, static assets), add S3 redirects in `/scripts/redirects/` (format: `source-path|destination-url`, place entries in topic-appropriate files). Manual move procedure and anchor-link caveats: see `.claude/commands/move-doc/SKILL.md`.

---

## Updating Internal Links

When moving documentation, aliases handle redirects automatically. Update internal links strategically:

- **DO update** links in `/content/docs/`, `/content/product/`, and `/content/tutorials/`.
- **`/content/blog/`** is historical — swap a broken link only for an equivalent replacement (stamp `lastmod`); otherwise route around it with an alias/redirect.
- **Link style**: links within `/docs/` must use the full canonical path (e.g. `/docs/iac/concepts/stacks/`). Never use parent-directory references (`../stacks/`) — they break when files move.

For find/sed implementation patterns, see `.claude/commands/move-doc/SKILL.md`.

---

## Navigation and llms.txt

The left nav is data-driven from `data/docs_menu_sections.yml`, which is consumed by `layouts/partials/docs/menu.html` (the rendered nav), `layouts/index.llms.txt` (the curated `/llms.txt` index), and `layouts/partials/llm-sitemap-walk.json` (the `/docs/llm-sitemap.json` machine-readable sitemap). When you add, remove, or reorder top-level nav sections, all three flow through automatically. Per-section descriptions in `/llms.txt` come from each landing page's `meta_desc` front-matter — edit the page if you need to change how it reads in the index.

---

## Resource options

The reference pages under `content/docs/iac/concepts/resources/options/` show a classification callout (custom resource / component resource / both, plus per-SDK enforcement) rendered by the `resource-option-scope` shortcode. The classification data — and the summary table on that section's `_index.md` — is generated from `data/resource_options.yaml`, which is the single source of truth. **When you add a new resource option, you must add an entry to `data/resource_options.yaml` and place the `{{< resource-option-scope "<name>" >}}` shortcode on the new page.** That file's header comment is the authoritative step-by-step checklist; the build fails if a page references an option missing from the data file.

---

## Blog categories and tags

Blog posts carry two taxonomy axes (plus optional `series`):

- **`categories`** — the *kind* of post. This is a **closed, lint-enforced** set defined in `data/blog_categories.yaml` (the single source of truth read by `scripts/lint/lint-markdown.js`). Every `content/blog/*/index.md` must declare **exactly one** category (a second only in rare cross-kind cases); `make lint` fails on a missing, empty, invalid, or >2 value. **Do not invent categories** — pick an id from the data file. To add/rename one, edit `data/blog_categories.yaml` in a PR and raise it in #blogs.
- **`tags`** — the *topical* axis (clouds, languages, products, scenarios). Curated-but-open, **not** build-enforced. Reuse a tag from the canonical vocabulary in `data/blog_tags.yaml` and **avoid near-duplicates** (`kubernetes` not `k8s`, `infrastructure-as-code` not `iac`, `pulumi-cloud` not `pulumi-service`, `dotnet` not `c#`/`.net`). Tags are lowercase and hyphen-delimited.

See `BLOGGING.md` for the author-facing version of these rules.

---

## Workflow Skills

Before starting any documentation task, check `.claude/commands/` for a relevant skill — there are well-structured skills covering common tasks like creating docs, reviewing PRs (see `.claude/commands/docs-review/SKILL.md`), moving files, and more. To see a full inventory, run `.claude/commands/docs-tools/scripts/scrape-metadata.py`.

**Non-Claude agents**: If the user runs a slash command or issues a short command that could be a skill name (e.g., `fix-issue`, `new-doc`), look for a matching file in `.claude/commands/` to guide your actions.

---

## PR Lifecycle for AI-Assisted Contributions

Open as draft, mark ready when done. Each ready-transition fires one full review; thrashing draft → ready → draft burns budget. Leave AI authoring trailers in commits (`Co-Authored-By: Claude ...`) — stripping them is bad form and changes nothing about which review runs. Don't delete `<!-- CLAUDE_REVIEW N/M -->` comments — the re-entrant pipeline edits them in place. To refresh a stale review, mention `@claude #update-review` (fix-response / dispute / re-verify) or transition through draft and back to ready. Bare `@claude` (no hashtag) is for ad-hoc help,

For the full mechanics — refresh-pattern details, short-circuit thresholds, classifier internals — see `CONTRIBUTING.md` §AI-assisted contributions.
