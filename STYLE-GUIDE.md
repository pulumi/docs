# Pulumi Documentation Style Guide

This guide defines Pulumi-specific style rules for our documentation.  
For topics not addressed here, refer to the [Google Developer Documentation Style Guide](https://developers.google.com/style).

---

## Scope

This style guide applies to all Hugo content files in this repository.

The following exceptions are specifically excluded from this style guide:

- Non-content files (scripts, configuration, etc.) should follow general best practices for that file type.
- Meta Markdown files (e.g., `README.md`, `AGENTS.md`) may use different conventions as appropriate.

---

## Inclusive Language

Pulumi strives to use language that is clear, inclusive, and respectful.  

- Avoid ableist terms.  
  - Instead of _crazy_, use _wild_.  
  - Instead of _dummy_, use _placeholder_.  
- Avoid unnecessarily gendered language (e.g., use _folks_, _everyone_).  
- Avoid violent or aggressive terms (e.g., avoid _kill_).  
- Avoid pop-culture references that may not be globally understood.  
- Instead of "click," use "select."  
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
- Do not end headings with punctuation.
- Headings should be surrounded by blank lines.

**Navigation menu items**: Use **Title Case** for frontmatter menu fields (`menu.name`, `menu.title`). Navigation items are UI labels, not prose headings, and follow Title Case conventions consistent with industry standards.

---

## Links

- **Internal and external links**: use normal Markdown syntax.
  - `[Link text](/path/to/file)`
  - `[Link text](https://example.com)`
- Link text must be descriptive. Avoid vague text like _here_ or _click here_.
- When changing the URL of an existing page, add a redirect with a [Hugo alias](https://gohugo.io/content-management/urls/#yaml-front-matter).

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

## Images and Media

- Use relative paths for images stored in the same directory or a subdirectory.  
- Provide descriptive alt text for all images.
- For partial screenshots where the image may be hard to distinguish from the page background, add a 1px gray #999999 border.

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

- **`{{% shortcode %}}`** (percent signs) - Use for shortcodes that process Markdown content. Hugo processes these before Markdown rendering.
  - Examples: `notes`, `choosable`, `details`

- **`{{< shortcode >}}`** (angle brackets) - Use for shortcodes that output pre-formatted content. Hugo processes these after Markdown rendering.
  - Examples: `cleanup`, `example`

**Rule of thumb:** If the shortcode uses `markdownify` internally (check `layouts/shortcodes/`), use percent signs. Otherwise, use angle brackets.

Both syntaxes work for simple content, but use percent signs for shortcodes with nested Markdown like lists or headings.

---

## Paragraphs and Line Breaks

- Separate paragraphs with a blank line.  
- Do not use line breaks within paragraphs. Let text wrap naturally.  
- Keep paragraphs short (ideally ≤3 sentences).

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
  - Pulumi Cloud
  - Pulumi Policies  
- Expand product acronyms at first mention. Use just the product name after.  
- For non-Pulumi acronyms: spell out on first use, then use the acronym.  
  - Example: Virtual Private Cloud (VPC), then VPC.  
- Widely known acronyms (API, HTTP, REST) don’t need expansion.
- *Pulumi Policies* is the product name, so it's a singular proper noun (like "United States" or "Brooks Brothers").
  - Always refer to it in the singular form (e.g., "Pulumi Policies enforces compliance").
  - Never refer to it in the plural (e.g., avoid "Pulumi Policies enforce compliance").

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
