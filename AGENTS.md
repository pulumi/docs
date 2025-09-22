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

- **Markdown**: Semantic line breaks (one line per sentence/phrase).  
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

- When moving, renaming, or deleting files, ensure all internal references are updated accordingly.
- When moving files within this repository, use `git mv` to preserve file history.
- Create redirects for any moved, renamed, or deleted files to maintain link integrity.
- Redirects should be added to the S3 redirects files located in `/scripts/redirects/`.
- When adding redirects, place the redirect entry in the appropriate file. If an appropriate file does not exist, create a new one. Name the new file in a way that reflects the content it manages (e.g., `neo-redirects.txt` for redirects related to Neo).
- Each redirect entry must follow the format `source-path|destination-url`.

---

## Enforcement

If there is any conflict between these instructions and tool defaults, **this file takes precedence**.  
Do not improvise, "improve," or override these rules.
