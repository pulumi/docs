# AGENTS.md — Pulumi website (Hugo): docs, blog, marketing, and example programs

---

## Build / Test / Lint Workflow

> **Note:** For comprehensive details on the build system, deployment infrastructure, and CI/CD workflows, see `BUILD-AND-DEPLOY.md`. This file is large, so read only specific sections as needed to conserve tokens.

Agents must use these exact commands:

- Install deps: `make ensure`
- Build site: `make build`
- Serve locally on port 1313 (accessible with curl):  
  - Normal: `make serve` 
  - With asset rebuilds: `make serve-all`
- Lint: `make lint` (must pass before commit/merge)
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
- **Spelling/Grammar**: Always correct errors. Use American English spelling.

---

## Moving and Deleting Files

**⚠️ SEO CRITICAL**: Missing aliases on moved files will break search engine rankings and external links. Always verify aliases after file moves.

**Use the `/move-doc` skill** when moving Hugo content files — it handles `git mv`, alias injection, link updates, and verification automatically. If moving manually:

- Use `git mv` to preserve file history.
- Add an `aliases` field to the frontmatter listing the old paths:

  ```yaml
  aliases:
  - /old/path/to/file/
  - /another/old/path/
  ```

- Verify aliases using the scripts in `/scripts/alias-verification/`.
- **Non-Hugo files**: For generated content or files outside Hugo's content management, add redirects to the S3 redirect files located in `/scripts/redirects/`.
  - When adding S3 redirects, place entries in topic-appropriate files (e.g., `neo-redirects.txt` for Neo-related content).
  - S3 redirect format: `source-path|destination-url` (e.g., `docs/old/path/index.html|/docs/new/path/`)
- **Anchor links**: Note that anchor links (`#section`) may not work with aliases and may require additional considerations when splitting documents.

---

## Updating Internal Links

When moving documentation files, aliases automatically handle redirects. Update internal links strategically:

- **DO update links in**:
  - `/content/docs/` - Active documentation
  - `/content/product/` - Product pages

- **DO NOT update links in**:
  - `/content/blog/` - Blog posts are historical documents
  - `/content/tutorials/` - Tutorials are historical content

- **Implementation**: When using `find` or `sed` to update links, always exclude blog and tutorial directories:

  ```bash
  find content/docs content/product -name "*.md" -exec sed -i 's|/old/path|/new/path|g' {} +
  ```

---

## Navigation and llms.txt

The left nav is defined in `layouts/partials/docs/menu.html`. Whenever you add, remove, or reorder top-level nav sections, also update `layouts/index.txtfull.txt` to match — it mirrors the nav structure for LLM consumption and its own comment says so.

---

## Workflow Skills

Before starting any documentation task, check `.claude/commands/` for a relevant skill — there are well-structured skills covering common tasks like creating docs, reviewing PRs (see `.claude/commands/docs-review.md`), moving files, and more. To see a full inventory, run `.claude/commands/docs-tools/scripts/scrape-metadata.py`.

**Non-Claude agents**: If the user runs a slash command or issues a short command that could be a skill name (e.g., `fix-issue`, `new-doc`), look for a matching file in `.claude/commands/` to guide your actions.
