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
- Use capitalization only for proper nouns. For example, use “stack” not “Stack.”

---

## Links

- **Internal and external links**: use normal Markdown syntax.  
  - `[Link text](/path/to/file)`  
  - `[Link text](https://example.com)`  
- Link text must be descriptive. Avoid vague text like _here_ or _click here_.  
- When changing the URL of an existing page, add a redirect with a [Hugo alias](https://gohugo.io/content-management/urls/#yaml-front-matter).

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

- Use **semantic line breaks**: start a new line for each sentence or phrase.  
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
