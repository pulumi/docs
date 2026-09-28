# Pulumi Documentation Style Guide

Pulumi's **voice, tone, prose, product naming, grammar, and punctuation** guidance lives in the **Pulumi brand guide** at [brand.pulumi.com](https://brand.pulumi.com/), and is consumable programmatically through the **brand MCP server**. That guide is the single source of truth for how Pulumi content reads. Do not restate or fork those rules here.

**Precedence:** wherever the brand guide overlaps with anything in this repo — these mechanics, the skills under `.claude/commands/`, or any social, SEO, or AEO guidance that still lives here — **the brand guide wins.** Some specialized guidance (e.g. social copy, SEO/AEO) currently lives only in this repo's skills; if and when the brand guide grows its own version, the brand guide's version takes priority.

This file covers only the **Hugo- and repo-specific mechanics** that the brand guide doesn't — how content is structured, linked, and rendered in *this* site.

For anything not covered in either place, fall back to the [Google Developer Documentation Style Guide](https://developers.google.com/style).

---

## Where the style rules live

Pulumi's voice and writing rules live in the brand guide, published at [brand.pulumi.com](https://brand.pulumi.com/) and exposed to agents through the public **brand MCP server** (see [brand.pulumi.com/mcp-server](https://brand.pulumi.com/mcp-server/)). Consult the relevant section before writing or reviewing:

| For… | See |
| ---- | --- |
| Voice and tone | [Voice & tone](https://brand.pulumi.com/voice/voice-and-tone/) |
| Grammar, punctuation, headings, links, lists, code-sample style | [Writing style](https://brand.pulumi.com/voice/writing-style/) |
| Product, feature, and category names — canonical casing, preferred terms, and retired names | [Names & terminology](https://brand.pulumi.com/voice/names-and-terminology/) |

An agent with the brand MCP server configured can pull any of these on its own — the server's instructions route it to the right section.

Key rules the brand guide owns (so you know what *not* to look for here): inclusive language; the Oxford comma; sentence case for headings; Pulumi product-name capitalization and the retired-names table; "public preview" over "public beta"; punctuation outside quotation marks; descriptive link text and alt text; and the prose patterns to avoid. The offline [Vale](https://vale.sh) rules in `styles/Pulumi/` mirror the mechanically enforceable subset of these (see [Automated checks](#automated-checks)).

---

## Scope

These mechanics apply to all Hugo content files in this repository.

- Non-content files (scripts, configuration, etc.) follow general best practices for their type.
- Meta Markdown files (`README.md`, `AGENTS.md`, `BUILD-AND-DEPLOY.md`, skill files) are exempt from these formatting rules.

---

## Headings

Heading **case is sentence case** for all levels — see the brand guide's [writing style](https://brand.pulumi.com/voice/writing-style/). The rest is Hugo mechanics:

- Exactly one H1 (`#`) per page, set in front matter `title`.
- Only increment one heading level at a time (no skipping levels).
- Do not end headings with punctuation, with one exception: headings in a "Frequently asked questions" section may end with `?` so the site's FAQPage JSON-LD auto-collector (`layouts/partials/schema/collectors/faq-entity.html`) detects them as questions.
- Surround headings with blank lines.

**Navigation menu items** (`menu.name`, `menu.title`): sentence case, consistent with headings.

---

## Links

The brand guide owns link *text* (descriptive, no "here"/"click here"). This site adds path mechanics:

- **Always use root-relative paths** (beginning with `/`) for internal links and image references — never page-relative paths like `./image.png`, `../other-page`, or bare `some-page`. Hugo content is sometimes a `.md` file and sometimes an `_index.md` in a folder, so `./` is ambiguous; root-relative paths are unambiguous and don't break when files move.
  - Correct: `[stacks](/docs/iac/concepts/stacks/)`, `![diagram](/blog/my-post/diagram.png)`
  - Incorrect: `[stacks](./stacks/)`, `![diagram](./diagram.png)`, `[stacks](../stacks/)`
- When changing the URL of an existing page, add a redirect with a [Hugo alias](https://gohugo.io/content-management/urls/#yaml-front-matter).

### External link indicator

Links that take users to a different UI/experience should include the ↗ (U+2197 North East Arrow) symbol when they appear in navigation menus or landing-page cards.

**When to use ↗:** links to generated API docs (`/docs/reference/pkg/*`), external sites (e.g. pkg.go.dev), Tutorials (different UI), or anything that leaves the main docs experience.

**Placement:**
- In menu configs (`config/_default/menus.yml`): append to the `name` field with a space — `name: SDK docs ↗`
- In landing-page cards: append to the `heading` field with a space — `heading: Python ↗`

Not needed for regular in-text links within documentation pages.

---

## Navigation patterns

Every section has an `_index.md` that the sidebar injects as the first item of the section's submenu. The label it receives — **"Overview"** or **"Introduction"** — depends on the page's role.

### Overview pages

Use **"Overview"** for section indexes whose primary purpose is routing readers to child pages, with little or no prose of their own. Add `docs_home: true` to enable the section home template.

Required frontmatter:

- `docs_home: true`
- `notitle: true` — suppresses the duplicate H1 (the template renders it from `h1:`)
- `norightnav: true` — hides the right-hand table of contents
- `h1:` — displayed in the page banner
- `description:` — short paragraph rendered in the banner (HTML string)
- `sections:` — list of section blocks using `type: cards-logo-label-link`, `type: button-cards`, or `type: flat`

See `content/docs/iac/_index.md` for the canonical example. Never use raw HTML to build navigation tiles or grid layouts.

### Introduction pages

Use **"Introduction"** for section indexes that contain substantive prose introducing a topic. No special frontmatter is required; any `_index.md` without `docs_home: true` receives this label automatically.

If the page also links to related child pages, use standard markdown (lists, tables) — not raw HTML grids or inline Tailwind classes.

---

## Images and media

The brand guide owns **alt text** (its [writing style](https://brand.pulumi.com/voice/writing-style/) section). This site adds:

- Use root-relative paths for all image references (see [Links](#links)).
- Name image files descriptively (helps accessibility and SEO); avoid generic names like `screenshot-1.png`.
- For partial screenshots where the image may be hard to distinguish from the page background, add a 1px gray #999999 border (the `/add-borders` skill does this).
- Images on template-driven pages go under `assets/fingerprinted/` (see `AGENTS.md`).

**Brand assets.** Use approved logos from the brand asset API (`https://brand.pulumi.com/api`); don't recolor, distort, or otherwise alter the logo, and never AI-generate Pulumi brand imagery or the Pulumipus mascot.

---

## Notes / callouts

Use the `{{ notes }}` shortcode sparingly. Supported levels:

- `info` — general information
- `tip` — helpful hints
- `warning` — important cautions

```go
{{% notes type="tip" %}}
This is a useful suggestion.
{{% /notes %}}
```

---

## Shortcode syntax

Hugo supports two shortcode notations:

- **`{{% shortcode %}}`** (percent signs) — for shortcodes that process Markdown content. Hugo processes these *before* Markdown rendering. Examples: `notes`, `choosable`, `details`.
- **`{{< shortcode >}}`** (angle brackets) — for shortcodes that output pre-formatted content. Hugo processes these *after* Markdown rendering. Examples: `cleanup`, `example`.

**Rule of thumb:** if the shortcode uses `markdownify` internally (check `layouts/shortcodes/`), use percent signs. Otherwise, use angle brackets. Use percent signs for shortcodes with nested Markdown like lists or headings.

---

## Code blocks and console output

The brand guide owns **code-sample style** — indentation, quoting, comments, line-splitting (its [writing style](https://brand.pulumi.com/voice/writing-style/) "Code samples" section). This site adds the Hugo rendering mechanics:

### Code fences

Use fenced code blocks (triple backticks) for all code and console output.

**Supported languages for syntax highlighting:** language-specific (`typescript`, `python`, `go`, `java`, `csharp`, `yaml`, etc.), shell commands (`bash`, `sh`), and console output (`output`).

### Console output

**Do not use indentation** (4 spaces) to denote console output. While valid Markdown, indented blocks are hard for humans and AI assistants to parse and maintain.

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

### Shell commands vs. output

- Use `bash` or `sh` for commands the user should type.
- Use `output` for the resulting console output.

```bash
pulumi up
```

```output
Updating (dev)
...
```

### Line highlighting

Use the `hl_lines` parameter on fenced code blocks to highlight specific lines with a purple background — useful for newly added or changed lines.

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

Combined with line numbers:

````markdown
```typescript {.line-numbers hl_lines=[5,"14-19"]}
// code here
```
````

Highlight only the few lines that are new or noteworthy. If the entire block matters equally, no highlighting is needed.

---

## Diagrams

Two formats are supported:

- **Mermaid** — flowcharts, sequence diagrams, class diagrams, etc. Rendered natively via the Hugo code block hook (`layouts/_default/_markup/render-codeblock-mermaid.html`). Use ` ```mermaid ` fenced blocks. Preferred.
- **GoAT (ASCII diagrams)** — good for simple flows.

See [Hugo diagrams docs](https://gohugo.io/content-management/diagrams/) and [Mermaid docs](https://mermaid.js.org/).

---

## Ordered lists

To minimize diff noise, every item in an ordered list begins with `1.` (Markdown auto-numbers):

```markdown
1. First step
1. Second step
1. Third step
```

(For list *grammar* — parallelism, when to use a list at all — see the brand guide.)

---

## Glossary

The [Pulumi glossary](/docs/reference/glossary/) defines common terms used throughout the documentation.

- When introducing a new concept or Pulumi-specific term, consider adding it to the glossary.
- The glossary helps both human and AI readers understand Pulumi terminology.
- To add or update terms, edit `data/glossary.toml`.
- Link to specific terms using anchor links: `/docs/reference/glossary/#term-name`.

For product, feature, and category names — canonical spellings, preferred terms like *Pulumi package* vs. *native language package*, and the retired names never to use again — see the brand guide's [Names & terminology](https://brand.pulumi.com/voice/names-and-terminology/) page (the `terminology` section via the MCP server). It is the single source of truth for naming; this repo's glossary defines *concepts*, not names.

---

## Cross-reference sections

Many pages end with a block of links to other pages. Use one of exactly two headings, chosen by the reader's intent — do not invent variants ("Related resources," "See also," "Additional resources," "What's next," "Further reading," and the like):

- **Next steps** — the reader should continue in a sequence: the next tutorial, the next step in a getting-started flow, or a recommended follow-on task. Use when there is a natural forward order.
- **Learn more** — links to related or reference material with no implied order: concept pages, other pages on the same topic, or external references. Use for lateral cross-references.

Rules:

- Use `##` (H2), sentence case: **Next steps** and **Learn more**, never "Next Steps" or "Learn More."
- Place the section at the end of the page.
- Choose by intent, not by page type. A concept page may have **Next steps**; a tutorial may have **Learn more**.
- If a page has both sequential and lateral links, use two sections named **Next steps** and **Learn more** — don't coin a third heading.

Exempt: the generated `SEE ALSO` blocks on CLI command pages (`content/docs/iac/cli/commands/`) and the auto-rendered "Related templates" aside on template pages, which are produced by tooling.

---

## FAQs

Dedicated FAQ pages have one canonical home: the FAQ hub at [`/docs/support/faq/`](https://www.pulumi.com/docs/support/faq/), under the **Support & Troubleshooting** nav section. This placement is intentional. Readers reach for an FAQ when they're in help-seeking mode, and Support & Troubleshooting is the site-wide help destination; keeping the pages together also avoids re-scattering Q&A across product sections. (The per-product FAQs that once lived at `/docs/esc/faq/`, `/docs/insights/policy/faq/`, `/docs/iac/faq/`, and similar paths were deliberately consolidated here — the aliases on the consolidated pages preserve those URLs.)

Rules:

- **Dedicated FAQ pages live only under `content/docs/support/faq/`**, one page per product area (`infrastructure.md`, `secrets-config.md`, `policies.md`, ...), each listed as a card on the hub's `_index.md` and placed in the `support` menu with `parent: support-faq`. Do not create an `faq.md` inside a product section.
- **Product sections link in.** Surface a product's FAQ from its landing page or a **Learn more** block (for example, "For common questions, see the [FAQ](/docs/support/faq/policies/)"), not by adding FAQ pages to the product's own nav.
- **FAQ is not troubleshooting.** "How do I fix this error?" content belongs with the rest of the day-2 material under [IaC Operations](https://www.pulumi.com/docs/iac/operations/) (Troubleshooting, Debugging) — or, for a Pulumi Cloud feature, on a `troubleshooting.md` page inside that feature's own section (the SAML and SCIM sections each have one) — not in an FAQ. FAQ pages answer conceptual and product questions ("Does Pulumi support rollbacks?", "How does Pulumi store state?").
- **Keep answers canonical.** If an answer needs more than a few paragraphs, the full explanation belongs in the topical docs and the FAQ entry gives the short answer plus a link. Don't let an FAQ become the only place something is documented.
- **In-page FAQ sections are different.** A "Frequently asked questions" H2 near the end of a what-is page, blog post, or product page is a page-level pattern, not part of the FAQ hub, and stays with its page. See [Headings](#headings) for the question-mark exception that lets the FAQPage JSON-LD collector pick those questions up.

---

## Neutral tone toward other products

Docs under `content/docs/` exist to inform readers, not to convince them. This matters most on comparison pages (`content/docs/iac/comparisons/`, `content/docs/esc/vs/`, `content/docs/deployments/versus.md`), but it applies anywhere docs mention another product. A reader who arrives on a comparison page is often still deciding, and a page that reads like a sales pitch loses their trust in the rest of the docs. Persuasive copy belongs on product and marketing pages (`content/product/`, the homepage), not in docs. The brand guide's [voice and tone](https://brand.pulumi.com/voice/voice-and-tone/) section asks for grounded copy without "overly promotional, salesy, or marketing-heavy language"; this section applies that to the Hugo docs tree.

This is about how docs treat *other products*, not a ban on opinions. Docs can and should recommend best practices for using Pulumi itself ("we recommend a general-purpose language for projects that need unit tests," "use one stack per environment") and patterns we've found effective for using Pulumi alongside other products ("provision the cluster with Pulumi and install charts with `helm.Release`"). State those as recommendations, with the reasoning, rather than as claims that the other product falls short.

Write docs so that a user of the other product would call them fair:

- **Describe, don't rank.** State what each product does and how. No superlatives or verdicts between products: "the best alternative," "Pulumi is the better choice," "more powerful than X." Let the reader draw the conclusion.
- **No persuasion framing.** Don't write sections whose purpose is to move the reader, such as "Why teams are leaving X," "What you get in return," "One platform, not a pile of point tools," or "X is no longer a reason to wait." Headings describe content ("Policy as code," "Pricing models"); they don't argue.
- **No fear, uncertainty, or doubt.** Leave out acquisitions, ownership changes, licensing controversies, pricing changes, or plan retirements unless the fact directly changes what the reader can do (for example, a free tier's resource limit, or a deprecated product like CDKTF). When one belongs, state it once, plainly, with a `<!-- verified: YYYY-MM -->` marker, and don't speculate about its consequences.
- **Represent the other product accurately and at its best.** Describe its equivalent features by name before saying what it lacks. "No equivalent" and "Limited" need to be true and specific; check the other product's current docs rather than working from memory. Don't frame a design difference as a defect (Vault storing only secrets isn't a missing "open ecosystem").
- **Keep table cells factual and parallel.** Each cell says what the product does, in the same register for both columns. No loaded qualifiers ("powerful," "requires significant management overhead," "a narrower training target") and no one-word judgments in place of a description.
- **Give the other product real "choose when" reasons.** A "When to choose" section lists genuine reasons to pick the other product, and doesn't follow them with a rebuttal. Put Pulumi's interoperability facts (HCL support, state backends, module reuse) in the adoption section instead.
- **No testimonials or sales proof.** Customer results, "proven at scale" sections, and vendor benchmarks don't belong in docs. Link to `/customers/` from a **Learn more** block if it's relevant.
- **Link to docs, not marketing pages.** Point to `/docs/...` pages for Pulumi features, not `/product/...` pages.
- **Compare Pulumi to other products, never other products to each other.** Every comparison is Pulumi vs. something else. Don't write pages, sections, table columns, or sentences that weigh two non-Pulumi products against each other (for example, "CDK vs. Terraform," or a table with Pulumi, AWS CDK, and Terraform columns side by side). Adjudicating between other vendors' products isn't our place, and we can't keep those claims accurate. A category page such as TACOS can describe what the category's products have in common, but compares the category to Pulumi, not its members to one another.
- **Front matter follows the same rules.** `title_tag`, `meta_desc`, and `h1` describe the comparison ("Pulumi vs. HCP Terraform") instead of selling it ("The best Terraform Cloud alternative").

Comparison pages share a structure; follow it for new ones: an intro stating what both products are and how they differ, **What is Pulumi?** (the `what-is-pulumi` shortcode), **What is _X_?**, **Detailed comparison** (a table), **Key differences**, **When to choose Pulumi vs. _X_**, **Adoption**, **Frequently asked questions**, and **Next steps**. `content/docs/iac/comparisons/crossplane.md` is a representative example.

---

## Tutorials

- End with a **Next steps** or **Learn more** section as appropriate — see [Cross-reference sections](#cross-reference-sections).

---

## Blog posts

See [BLOGGING.md](BLOGGING.md) for the repo mechanics of writing Pulumi blog posts. For blog voice, see the brand guide's voice and writing-style sections via the MCP server.

---

## Automated checks

The rules in this guide — and the mechanically enforceable subset of the brand guide's — are enforced by [Vale](https://vale.sh) via `.vale.ini` at the repo root. Custom rules live under `styles/Pulumi/` (product-name casing, retired/deprecated terms, inclusive language, substitutions, AI-drafting tells) and layer on top of the Google Developer Style Guide and write-good packages. **Vale runs offline in CI and can't call the MCP, so these rules are a local mirror of the brand guidance — the brand guide is the source of truth, and the mirror only follows it.** `styles/Pulumi/BRAND-SYNC.yaml` records which brand section each mirrored rule tracks, and the weekly `brand-style-sync` workflow re-checks the mirror against the live brand MCP server (retired names first, since renamed products rot fastest) and opens a draft PR when they drift. Run locally with `make lint-prose`, which also feeds front-matter `title:`/`h1:` fields (the site's H1s) through the same sentence-case rule via `scripts/lint/frontmatter-title-case.py` — Vale reads front matter, but the sentence-case rule is scoped to headings and front matter isn't parsed as one. Vale findings surface in the pinned PR review in two tiers: a small set of near-zero-false-positive correctness rules (wrong, retired, or miscased product names, non-American spellings, grammatical agreement — the `blocker:` list in `.claude/commands/docs-review/scripts/vale-deterministic-fixes.yaml`) renders under 🚨 Outstanding and must be resolved or refuted before merging; everything else renders under ⚠️ Low-confidence as advisory nags that never block.
