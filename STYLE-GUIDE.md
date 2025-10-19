# Pulumi Documentation Style Guide

This guide defines Pulumi-specific style rules for our documentation.  
For topics not addressed here, refer to the [Google Developer Documentation Style Guide](https://developers.google.com/style).

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
- **Documentation should not link to marketing pages**. Pages within `/docs` should link to other documentation pages (`/docs/*`) or reference material (`/registry/*`), not to marketing pages (e.g., `/pricing`, `/contact`, `/product`, `/templates`, `/blog`, `/case-studies`, `/what-is`). If you need to reference a topic covered in a marketing page, create appropriate documentation content instead.

### External Link Indicator

Links that navigate users to a different UI/experience (different from the main docs site) should include the ↗ (U+2197 North East Arrow) symbol to indicate this transition.

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
- In prose text: append after the link text with a space
  - Example: `[Go SDK ↗](https://pkg.go.dev/...)`

**Rationale:** The ↗ symbol is the web-standard indicator for external links and helps users understand they're navigating to a different UI, preventing surprise when the page appearance changes.

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
- Expand product acronyms at first mention. Use just the product name after.  
- For non-Pulumi acronyms: spell out on first use, then use the acronym.  
  - Example: Virtual Private Cloud (VPC), then VPC.  
- Widely known acronyms (API, HTTP, REST) don’t need expansion.

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
