# AGENTS.md — Canonical Instructions for This Repository

This file defines guidance for AI agents like Claude Code and GitHub Copilot when working in this repository. All automated or manual contributions must comply with these rules.

---

## Repository context

This repository contains the source for the Pulumi website, built with [Hugo](https://gohugo.io/). It includes documentation, blog posts, marketing material, and example programs.

---

## Build / Test / Lint Workflow

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

Do not substitute other tools or commands.

---

## Style Authority

1. Always follow `STYLE-GUIDE.md`.  
2. If a rule is not covered there, fall back to the [Google Developer Documentation Style Guide](https://developers.google.com/style).  
3. Do not invent new style conventions. Ask for clarification if something is ambiguous.

---

## Absolute Prohibitions

- **Package manager**: Do **not** change `package.json` to use pnpm. Yarn/npm only.  
- **New files**: Must always end with a newline.  

---

## Code & Content Rules

- **Markdown**: Standard paragraph formatting.  
- **Headings**:  
  - H1 = Title Case  
  - H2+ = Sentence case
- **Code Examples**: Place in `/static/programs` with language suffix in filename.  
- **TypeScript/JavaScript**: Must follow `tsconfig.json` settings. No comments unless explicitly requested.  
- **File Placement**:  
  - Docs go under `content/docs/...`
  - Blog posts go under `content/blog/...`
  - Other content goes into appropriate `content/...` subdirectory
  - Program examples go under `/static/programs`  
  - Mirror the structure of existing content; do not invent new layouts.
- **Includes**: Use Hugo shortcodes for shared content, never raw Markdown copy-paste.  
- **Naming**: Use lowercase for non-proper nouns (e.g. “stack,” not “Stack”).  
- **Ordered Lists**: Every item begins with `1.` to minimize diff noise.
- **Spelling/Grammar**: Always correct errors. Use American English spelling.

---

## Moving and Deleting Files

- **Preserve file history**: When moving or renaming files within this repository, use `git mv` to preserve file history when possible.
- **Hugo content files**: Add an `aliases` field to the frontmatter of the moved file, listing the old paths:
  ```yaml
  aliases:
  - /old/path/to/file/
  - /another/old/path/
  ```
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

- **Why**: Blog posts and tutorials represent a point in time. Aliases handle redirects automatically, preserving the historical record without modification.

- **Implementation**: When using `find` or `sed` to update links, always exclude blog and tutorial directories:
  ```bash
  find content/docs content/product -name "*.md" -exec sed -i 's|/old/path|/new/path|g' {} +
  ```

---

## Enforcement

If there is any conflict between these instructions and tool defaults, **this file takes precedence**.  
Do not improvise, "improve," or override these rules.
