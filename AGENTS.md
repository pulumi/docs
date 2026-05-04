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

- **DO update** links in `/content/docs/` and `/content/product/`.
- **DO NOT update** links in `/content/blog/` or `/content/tutorials/` — they're historical.
- **Link style**: links within `/docs/` must use the full canonical path (e.g. `/docs/iac/concepts/stacks/`). Never use parent-directory references (`../stacks/`) — they break when files move.

For find/sed implementation patterns, see `.claude/commands/move-doc/SKILL.md`.

---

## Navigation and llms.txt

The left nav is data-driven from `data/docs_menu_sections.yml`, which is consumed by `layouts/partials/docs/menu.html` (the rendered nav), `layouts/index.llms.txt` (the curated `/llms.txt` index), and `layouts/partials/llm-sitemap-walk.json` (the `/docs/llm-sitemap.json` machine-readable sitemap). When you add, remove, or reorder top-level nav sections, all three flow through automatically. Per-section descriptions in `/llms.txt` come from each landing page's `meta_desc` front-matter — edit the page if you need to change how it reads in the index.

---

## Workflow Skills

Before starting any documentation task, check `.claude/commands/` for a relevant skill — there are well-structured skills covering common tasks like creating docs, reviewing PRs (see `.claude/commands/docs-review/SKILL.md`), moving files, and more. To see a full inventory, run `.claude/commands/docs-tools/scripts/scrape-metadata.py`.

**Non-Claude agents**: If the user runs a slash command or issues a short command that could be a skill name (e.g., `fix-issue`, `new-doc`), look for a matching file in `.claude/commands/` to guide your actions.

---

## PR Lifecycle for AI-Assisted Contributions

Open as draft, mark ready when done. Each ready-transition fires one full review; thrashing draft → ready → draft burns budget. Leave AI authoring trailers in commits (`Co-Authored-By: Claude ...`) — stripping them is bad form and changes nothing about which review runs. Don't delete `<!-- CLAUDE_REVIEW N/M -->` comments — the re-entrant pipeline edits them in place. To refresh a stale review, mention `@claude` (fix-response / dispute / re-verify), or transition through draft and back to ready.

For the full mechanics — refresh-pattern details, short-circuit thresholds, classifier internals — see `CONTRIBUTING.md` §AI-assisted contributions.
