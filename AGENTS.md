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

- **Link Style**: To ensure links don't break when files are moved:
  - Links within `/docs/` must use the full canonical path, e.g. `/docs/iac/concepts/stacks/`.
  - Never use parent-directory references (`../stacks/`) in links — they break when files move.

---

## Navigation and llms.txt

The left nav is data-driven from `data/docs_menu_sections.yml`, which is consumed by `layouts/partials/docs/menu.html` (the rendered nav), `layouts/index.llms.txt` (the curated `/llms.txt` index), and `layouts/partials/llm-sitemap-walk.json` (the `/docs/llm-sitemap.json` machine-readable sitemap). When you add, remove, or reorder top-level nav sections, all three flow through automatically. Per-section descriptions in `/llms.txt` come from each landing page's `meta_desc` front-matter — edit the page if you need to change how it reads in the index.

---

## Workflow Skills

Before starting any documentation task, check `.claude/commands/` for a relevant skill — there are well-structured skills covering common tasks like creating docs, reviewing PRs (see `.claude/commands/docs-review.md`), moving files, and more. To see a full inventory, run `.claude/commands/docs-tools/scripts/scrape-metadata.py`.

**Non-Claude agents**: If the user runs a slash command or issues a short command that could be a skill name (e.g., `fix-issue`, `new-doc`), look for a matching file in `.claude/commands/` to guide your actions.

---

## PR Lifecycle for AI-Assisted Contributions

The repository runs a tiered review pipeline on every PR. AI-assisted contributors should know how it works so they can collaborate with it instead of fighting it.

### Open as draft

When opening a PR you intend to iterate on, **open it as a draft**. Drafts are triaged (labels applied) but do not trigger the full Claude review. Iterate freely; pushes to the branch will not produce review noise.

### Mark ready for review when finished

Transitioning to **Ready for review** triggers:

1. A re-triage to refresh labels (domain, fact-check signal, agent-authored signal, trivial check).
2. The full Claude review (currently `claude-opus-4-7`), composed per touched domain. Findings post to a single pinned comment at the top of the PR — overflow is appended as additional pinned comments tagged `<!-- CLAUDE_REVIEW N/M -->`.

Mark the PR ready when you're done iterating, not when you start. Each ready-transition produces one full review run; thrashing through draft → ready → draft burns review budget and produces stale pinned comments.

### Author a clean commit history

If the PR was AI-drafted, leave the AI authoring trailers in commit messages (`Co-Authored-By: Claude ...`, `Generated with Claude Code`, etc.). Triage uses these to apply the `agent-authored` label, which is a signal for human adjudication — it does not change which review runs. Removing the trailers does not exempt the PR from review and is bad form.

### After review — three paths to refresh

A pinned review goes **stale** when you push new commits after it ran. Stale reviews don't auto-rerun. Three ways to refresh:

1. **`@claude` mention**: Leave a comment on the PR mentioning `@claude` (with or without a specific request). The re-entrant pipeline picks up new commits, runs `claude-sonnet-4-6`, and updates the existing pinned comment(s) in place. Three patterns the re-entrant pipeline understands:
    - **Fix-response** ("I addressed your feedback"): re-verifies the previous outstanding findings against the new diff and moves the resolved ones into ✅ Resolved.
    - **Dispute** ("I disagree with the X finding because Y"): re-examines the disputed finding with your evidence; either concedes cleanly or explains why it's keeping the finding.
    - **Re-verify** ("@claude refresh" / no specific request): re-checks outstanding findings only.
2. **Transition through draft and back to ready**: this re-triggers the full initial review. Use this when the PR has changed substantially since the last review.
3. **Wait for the human reviewer**: Cam's local `pr-review` skill reads the pinned comment as source of truth and refreshes it during adjudication if needed.

### Don't fight the pinned comment

The `<!-- CLAUDE_REVIEW N/M -->` comments are managed by the pipeline. Don't delete them — the re-entrant skill expects to find and edit them in place. If you accidentally delete the 1/M summary, the next run posts fresh at the bottom of the timeline; recoverable but ugly.

### Trivial PRs short-circuit

If triage labels the PR `review:trivial` (≤5 lines, prose-only, single file, no frontmatter or link changes), the Claude review skips entirely. Linters still run. This is intentional — typos and one-liners don't need a model in the loop.
