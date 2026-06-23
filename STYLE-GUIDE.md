# Pulumi Documentation Style Guide

This guide defines Pulumi-specific style rules for our documentation.  
It's the repo-specific layer. For brand-level voice, writing style, and visual conventions, the [Pulumi brand guidelines](https://brand.pulumi.com/) are authoritative — query them directly through the [Pulumi Brand MCP server](https://brand.pulumi.com/mcp) (see [Brand guidelines and the Brand MCP server](#brand-guidelines-and-the-brand-mcp-server) below). For anything none of these covers, fall back to the [Google Developer Documentation Style Guide](https://developers.google.com/style).

---

## Scope

This style guide applies to all Hugo content files in this repository.

The following exceptions are specifically excluded from this style guide:

- Non-content files (scripts, configuration, etc.) should follow general best practices for that file type.
- Meta Markdown files (e.g., `README.md`, `AGENTS.md`) may use different conventions as appropriate.

---

## Brand guidelines and the Brand MCP server

Pulumi's brand-level conventions — voice and tone, writing style (grammar, punctuation, product names), typography, logo and visual usage, and color — live in the [Pulumi brand guidelines](https://brand.pulumi.com/), served programmatically by the [Pulumi Brand MCP server](https://brand.pulumi.com/mcp). That server is the source of truth for brand questions this guide doesn't answer.

Precedence, highest first:

1. **This style guide** — repo-specific conventions for the Hugo content in this repository.
1. **Pulumi brand guidelines (Brand MCP server)** — brand-wide voice, writing style, and visual rules.
1. **[Google Developer Documentation Style Guide](https://developers.google.com/style)** — anything neither of the above covers.

Where this guide and the brand guidelines diverge, this guide wins for this repository — but any divergence should be deliberate and documented here. Don't invent a third convention; reconcile with the brand guidelines or note the exception.

Agents with the Brand MCP server configured can pull the full text of any section on demand (for example, `get_guidelines({ section: "writing-style" })`) and should prefer it to guessing. The same server provides approved logo assets (`get_logo`), the brand color palette and semantic tokens, and an APCA contrast checker. Use those when **creating** brand assets — blog meta images, diagrams, slide decks — not for second-guessing the colors in a product screenshot.

---

## Inclusive Language

Pulumi strives to use language that is clear, inclusive, and respectful.  

- Avoid ableist terms.  
  - Instead of _crazy_, use _wild_.  
  - Instead of _dummy_, use _placeholder_.  
- Avoid unnecessarily gendered language (e.g., use _folks_, _everyone_).  
- Avoid violent or aggressive terms (e.g., avoid _kill_).  
- Avoid pop-culture references that may not be globally understood.  
- Instead of "click," use "select" (or "choose").  
- Instead of "go to," use "navigate."  
- Avoid directional terms (e.g., "see above"); link directly.  
- Avoid words like "easy" or "simple." These judge difficulty and may alienate readers.

---

## Headings

- Exactly one H1 (`#`) per page, set in front matter `title`.
- H1: **Title Case**.
- H2 and deeper: **Sentence case**.
- Only increment one heading level at a time (no skipping levels).
- Use capitalization only for proper nouns. For example, use "stack" not "Stack."
- Do not end headings with punctuation, with one exception: headings in a "Frequently asked questions" section may end with `?` so the site's FAQPage JSON-LD auto-collector (`layouts/partials/schema/collectors/faq-entity.html`) detects them as questions.
- Headings should be surrounded by blank lines.

> **Title vs. headings.** The brand guide's sentence-case rule governs *headings*, and it treats the H1 as the page **title**, not a heading. Title Case for the H1 — rendered from front-matter `title`, consistent with the Title Case used for navigation menu items — is therefore in keeping with the [Pulumi brand writing-style guidelines](https://brand.pulumi.com/), not an exception to them. Sentence case applies to H2 and deeper. Don't "fix" existing H1s to sentence case.

**Navigation menu items**: Use **Title Case** for frontmatter menu fields (`menu.name`, `menu.title`). Navigation items are UI labels, not prose headings, and follow Title Case conventions consistent with industry standards.

---

## Links

- **Internal and external links**: use normal Markdown syntax.
  - `[Link text](/path/to/file)`
  - `[Link text](https://example.com)`
- Link text must be descriptive. Avoid vague text like _here_ or _click here_.
- When changing the URL of an existing page, add a redirect with a [Hugo alias](https://gohugo.io/content-management/urls/#yaml-front-matter).
- **Always use root-relative paths** (beginning with `/`) for all internal links and image references — never page-relative paths like `./image.png`, `../other-page`, or bare relative paths like `some-page`. Page-relative paths are ambiguous because Hugo content files are sometimes named `.md` files rather than `_index.md` files in a folder, making the meaning of `./` differ between the file's location on disk and the URL the page is served from. Root-relative paths are unambiguous, portable, and don't silently break when files move.
  - Correct: `[stacks](/docs/iac/concepts/stacks/)`, `![diagram](/blog/my-post/diagram.png)`
  - Incorrect: `[stacks](./stacks/)`, `![diagram](./diagram.png)`, `[stacks](../stacks/)`

### External Link Indicator

Links that navigate users to a different UI/experience (different from the main docs site) should include the ↗ (U+2197 North East Arrow) symbol to indicate this transition when linking from navigation menus or landing page cards.

**When to use ↗:**
- Links to generated API documentation (`/docs/reference/pkg/*`)
- Links to external sites (e.g., pkg.go.dev)
- Links to Tutorials (different UI)
- Any link that takes users away from the main docs experience

**Placement:**
- In menu configurations (`config/_default/menus.yml`): append to the `name` field with a space
  - Example: `name: SDK docs ↗`
- In landing page cards: append to the `heading` field with a space
  - Example: `heading: Python ↗`

The symbol is not needed in regular in-text links within documentation pages.

**Rationale:** The ↗ symbol is the web-standard indicator for external links and helps users understand they're navigating to a different UI, preventing surprise when the page appearance changes.

---

## Navigation patterns

Every section has an `_index.md` that the sidebar automatically injects as the first item of the section's submenu. The label it receives — **"Overview"** or **"Introduction"** — depends on the page's role.

### Overview pages

Use **"Overview"** for section indexes whose primary purpose is routing readers to child pages, with little or no prose of their own. Add `docs_home: true` to the frontmatter to mark the page as an overview and enable the section home template.

Required frontmatter:

- `docs_home: true`
- `notitle: true` — suppresses the duplicate H1 (the template renders it from `h1:`)
- `norightnav: true` — hides the right-hand table of contents (unused on overview pages)
- `h1:` — displayed in the page banner
- `description:` — short paragraph rendered in the banner (HTML string)
- `sections:` — list of section blocks using `type: cards-logo-label-link`, `type: button-cards`, or `type: flat`

See `content/docs/iac/_index.md` for the canonical example. Never use raw HTML to build navigation tiles or grid layouts.

### Introduction pages

Use **"Introduction"** for section indexes that contain substantive prose introducing a topic. No special frontmatter is required; any `_index.md` without `docs_home: true` receives this label automatically.

If the page also links to related child pages, use standard markdown (lists, tables) — not raw HTML grids or inline Tailwind classes.

---

## Images and Media

- Use root-relative paths for all image references (see [Links](#links) above).
- Provide descriptive alt text for all images. Describe the image's content or function in a few words, and omit lead-ins like "image of" or "screenshot of" — screen readers already announce those.
- Name image files descriptively (helps accessibility and SEO); avoid generic names like `screenshot-1.png`.
- For partial screenshots where the image may be hard to distinguish from the page background, add a 1px gray #999999 border.

**Brand assets.** For logos, illustrations, and other brand imagery, use the approved assets from the [Pulumi Brand MCP server](https://brand.pulumi.com/mcp) (`get_logo`, or the canonical URLs under `https://brand.pulumi.com/media/...`). Don't recolor, distort, add effects to, or otherwise alter the logo, and never use generative AI to create Pulumi brand imagery or the Pulumipus mascot. See the brand `logo`, `visuals`, and `guidelines` sections for the full rules.

---

## Notes / Callouts

Use the `{{ notes }}` shortcode sparingly. Supported levels:

- `info` — general information  
- `tip` — helpful hints  
- `warning` — important cautions  

**Example:**

```go
{{% notes type="tip" %}}
This is a useful suggestion.
{{% /notes %}}
```

---

## Shortcode syntax

Hugo supports two shortcode notations:

- **`{{% shortcode %}}`** (percent signs) - Use for shortcodes that process Markdown content. Hugo processes these before Markdown rendering
  - Examples: `notes`, `choosable`, `details`

- **`{{< shortcode >}}`** (angle brackets) - Use for shortcodes that output pre-formatted content. Hugo processes these after Markdown rendering
  - Examples: `cleanup`, `example`

**Rule of thumb:** If the shortcode uses `markdownify` internally (check `layouts/shortcodes/`), use percent signs. Otherwise, use angle brackets.

Both syntaxes work for plain text content, but use percent signs for shortcodes with nested Markdown like lists or headings.

---

## Paragraphs and Line Breaks

- Separate paragraphs with a blank line.  
- Do not use line breaks within paragraphs. Let text wrap naturally.  
- Keep paragraphs short (ideally ≤3 sentences).

---

## Grammar and punctuation

- Use the Oxford (serial) comma: "build, deploy, and manage," not "build, deploy and manage."
- Contractions are fine — preferred, even — in docs. They read more naturally.
- Put commas and periods outside closing quotation marks unless they belong to the quoted text — e.g., write `"us-west-2"`, with the comma outside.
- Em-dashes are fine when you write them yourself, but revise away the em-dashes, three-item series, and filler phrasings that LLMs tend to emit — they read as unedited machine output.

For dates, times, numbers, point of view (*you* vs. *we*), and other mechanics this guide doesn't specify, defer to the brand `writing-style` guidance via the [Brand MCP server](https://brand.pulumi.com/mcp).

---

## Lists

- Use ordered lists for steps.
- All items should begin with `1.` (Markdown will auto-number).

Example:

```markdown
1. First step
1. Second step
1. Third step
```

---

## Code Blocks and Console Output

### Code Fences

Use fenced code blocks (triple backticks) for all code and console output.

**Supported languages for syntax highlighting:**
- Language-specific: `typescript`, `python`, `go`, `java`, `csharp`, `yaml`, etc.
- Shell commands: `bash`, `sh`
- Console output: `output`

### Console Output

**Do not use indentation** (4 spaces) to denote console output. While technically valid Markdown, indented blocks are difficult for both humans and AI assistants to parse and maintain.

**Wrong:**

```markdown
    output line 1
    output line 2
```

**Correct:**

````markdown
```output
output line 1
output line 2
```
````

### Shell Commands vs Output

- Use `bash` or `sh` for commands the user should type
- Use `output` for the resulting console output

**Example:**

```bash
pulumi up
```

```output
Updating (dev)
...
```

**Rationale:** Fenced code blocks are explicit, easy to identify, and support syntax highlighting. Indented blocks can be confused with nested lists or quotes, especially when editing.

### Line highlighting

Use the `hl_lines` parameter on fenced code blocks to highlight specific lines with a purple background. This draws attention to the most important lines in a code sample, such as newly added or changed lines.

**Single lines and ranges:**

````markdown
```typescript {hl_lines=[3]}
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as vpc from "@pulumi/vpc"; // this line is highlighted
```
````

````markdown
```python {hl_lines=["3-5"]}
import pulumi
import pulumi_aws as aws
# lines 3 through 5
# are all
# highlighted
```
````

**Combined with line numbers:**

````markdown
```typescript {.line-numbers hl_lines=[5,"14-19"]}
// code here
```
````

Use line highlighting when a code block is long but only a few lines are new or noteworthy. Do not highlight every line — if the entire block matters equally, no highlighting is needed.

---

## Blockquotes

- Use blockquotes only for direct quotations.

Example:

> This is something a person said.

---

## Diagrams

We support two formats:

- **GoAT (ASCII diagrams)** — good for simple flows.  
- **Mermaid** — supports flowcharts, sequence diagrams, class diagrams, etc.  

See [Hugo diagrams docs](https://gohugo.io/content-management/diagrams/) and [Mermaid docs](https://mermaid.js.org/).

---

## Product Names and Acronyms

- Always capitalize Pulumi product names correctly.  
  - Pulumi IaC (Infrastructure as Code)  
  - Pulumi ESC (Environments, Secrets, and Configuration)  
  - Pulumi IDP (Internal Developer Platform)  
  - Pulumi Insights  
  - Pulumi Cloud (also Pulumi console / Pulumi Cloud console — but not "Pulumi UI")
  - Pulumi Deployments
  - Pulumi Neo
  - Pulumi Policies  
- Expand product acronyms at first mention. Use just the product name after.  
- For non-Pulumi acronyms: spell out on first use, then use the acronym.  
  - Example: Virtual Private Cloud (VPC), then VPC.  
- Widely known acronyms (API, HTTP, REST) don’t need expansion.
- *Pulumi Policies* is the product name, so it's a singular proper noun (like "United States" or "Brooks Brothers").
  - Always refer to it in the singular form (e.g., "Pulumi Policies enforces compliance").
  - Never refer to it in the plural (e.g., avoid "Pulumi Policies enforce compliance").
- Use **"public preview"** for pre-GA features, not "public beta." This aligns with Pulumi's release terminology.

---

## Glossary

The [Pulumi glossary](/docs/iac/concepts/glossary/) defines common terms and concepts used throughout the documentation.

- When introducing a new concept or Pulumi-specific term in documentation, consider adding it to the glossary.
- The glossary helps users (both human and AI agents) quickly understand Pulumi terminology.
- To add or update glossary terms, edit `data/glossary.toml`.
- Link to specific glossary terms using anchor links: `/docs/iac/concepts/glossary/#term-name`

### Preferred terminology

The following terms have precise meanings in Pulumi documentation. Use them consistently and prefer them over informal or ambiguous alternatives:

| Term | Definition |
| ---- | ---------- |
| **Native language package** | A component published to a language-specific registry (npm, PyPI, NuGet, Maven, etc.) without a Pulumi plugin. Consumable only in the language in which it was authored. |
| **Pulumi package** | A component or provider packaged with a Pulumi plugin so Pulumi can generate SDKs for any supported language. Consumable in all Pulumi languages. |

Use **"Pulumi package"** (not "cross-language package") when referring to components or providers distributed with a Pulumi plugin. Use **"native language package"** (not "single-language package" or "language-native package") when referring to components distributed as standard language packages without a Pulumi plugin.

---

## References to Commands or UI

- CLI commands: wrap in backticks (e.g., `pulumi up`).  
- UI elements: use **bold** (e.g., “Go to the **Account** page”).  
- Navigation: use arrows (e.g., **Settings** → **API Keys**).

---

## Tutorials

- If the tutorial is followed by another, end with a **Next steps** section.  
- If pointing to references or further reading, end with a **Learn more** section.

---

## Blog Posts

See [BLOGGING.md](BLOGGING.md) for guidance on writing Pulumi blog posts.

---

## Automated checks

The rules in this guide are enforced — where mechanically possible — by [Vale](https://vale.sh) via `.vale.ini` at the repo root. Custom rules live under `styles/Pulumi/` and layer on top of the Google Developer Style Guide and write-good packages. Run locally with `make lint-prose`. Vale findings also surface in the pinned PR review under ⚠️ Low-confidence and never block merges.
