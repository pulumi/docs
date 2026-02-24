---
user-invocable: false
description: Shared review criteria for documentation quality checks
---

# Review Criteria

Use the repository's CLAUDE.md, AGENTS.md, and STYLE-GUIDE.md for guidance on style and conventions.

Provide your review as a single summary, highlighting any issues found and suggesting improvements.

Be constructive and helpful in your feedback, but don't overdo the praise. Be concise.

Always provide relevant line numbers for any issues you identify.

**Criteria:**

- Always enforce `STYLE-GUIDE.md`. If not covered there, fall back to the [Google Developer Documentation Style Guide](https://developers.google.com/style).
- Check **spelling and grammar** in all files.
- Confirm that **all links resolve** and point to the correct targets (no 404s, no mislinked paths).
- Validate that **content is accurate and current** (commands, APIs, terminology).
- Ensure **all new files end with a newline**.
- Double-check indented lines to ensure they are not incorrectly indented as code blocks.
- **Code examples** must run correctly and follow best practices:
  - Do not suggest untested code.
  - Examples should show realistic use cases, not contrived demos.
  - Examples should handle errors appropriately.
  - Examples should follow language-specific best practices.
- **Files moved, renamed, or deleted**:
  - Confirm that moved or renamed files have appropriate aliases added to the frontmatter to avoid broken links.
  - Confirm that deleted files have a redirect created, if applicable.
- **Build, test, and infrastructure changes**:
  - If changes are made to build scripts (scripts/), GitHub Actions workflows (.github/workflows/), the Makefile, or infrastructure code (infrastructure/), verify that BUILD-AND-DEPLOY.md has been updated to reflect these changes.
  - Examples of changes requiring documentation updates: new make targets, modified deployment workflows, infrastructure configuration changes, new environment variables, updated build processes.
  - **High-risk changes**: Flag infrastructure changes (infrastructure/, package.json, webpack config, Lambda@Edge, CloudFront) and Dependabot dependency updates that affect runtime/bundling. **Your role is to identify and flag risks for human review**—see [Infrastructure Change Review](../../../BUILD-AND-DEPLOY.md#infrastructure-change-review) and [Dependency Management](../../../BUILD-AND-DEPLOY.md#dependency-management) sections in BUILD-AND-DEPLOY.md for risk details. Key risks: Lambda@Edge bundling (ESM/CommonJS, webpack changes), large dependency batches, runtime dependencies (marked, algolia, stencil), CloudFront changes
- **Images and assets**:
  - Check images have alt text for accessibility.
  - Verify image file sizes are reasonable.
  - Ensure images are in appropriate formats.
- **Front matter**:
  - Verify required front matter fields (title, description, etc.).
  - Check meta descriptions are present and appropriate length.
- **Cross-references and consistency**:
  - Check that related pages are cross-linked appropriately.
  - Verify terminology is consistent with other docs.
- **SEO**:
  - Check that page titles and descriptions are SEO-friendly.
  - Check that the titles and descriptions match the content.
  - Verify URL structure follows conventions.
- **Role-Specific Review Guidelines**
  - Documentation and blog/marketing materials have additional role-specific criteria below.

## Role-Specific Review Guidelines

### Documentation

When reviewing **Documentation**, serve the role of a professional technical writer. Review for:

- Clarity and conciseness.
- Logical flow and structure.
- No jargon unless defined.
- Avoid passive voice.
- Avoid overly complex sentences. Shorter is usually better.
- Avoid superlatives and vague qualifiers.
- Avoid unnecessary filler words or sentences.
- Be specific and provide examples.
- Use consistent terminology.

### Blogs or Marketing Materials

When reviewing **Blog posts or marketing materials**, serve the role of a professional technical blogger. Blogs have specific review criteria that differ from general documentation.

Review for:

**AI writing patterns** (most commonly flagged — check these first):

- Em-dash overuse: flag more than 1–2 em-dashes per section
- Contrastive patterns: "It's not X, it's Y" constructions
- Choppy, uniform sentence lengths (vary sentence rhythm)
- Unnecessary TL;DR or summary paragraphs that restate what follows
- Repetitive sentence openers across consecutive paragraphs
- Hedging language: "generally", "typically", "tends to", "can often" — write with confidence

**Content and structure:**

- Clear, engaging title with primary search term; no clickbait
- Strong opening that hooks the reader
- Clear structure with headings and subheadings; use liberal subheadings for scannability
- Each section opens with 1–2 motivation sentences explaining why the reader should care
- Concise paragraphs (3–4 sentences max); convert dense paragraphs to lists
- Listicles and best-practices posts should target ≤3,000 words; flag if >12 items with no cuts suggested
- No "easy" or "simple" per STYLE-GUIDE.md

**Writing quality:**

- Write recommendations with confidence; remove hedging language
- No self-criticism of prior Pulumi product decisions
- Strong conclusions with specific next steps (not vague "check out Pulumi")
- Reject filler, vague generalities, or AI-generated slop

**Links and sources:**

- First mention of every tool, technology, or product must be hyperlinked
- Unsourced technical claims require citations
- Internal Pulumi features must link to `/docs/`
- Use `{{< github-card >}}` shortcode for GitHub repo references

**Product accuracy:**

- Use official Pulumi product names only
- Don't describe existing features as "new" — use "now supports" or "recently added"
- Verify every technical claim (language support, API names, UI paths) is correct

**Meta elements and publishing readiness:**

- `meta_image` must be set — not the default placeholder image
- `meta_image` must use current Pulumi logos (old logo variants hurt social sharing)
- `<!--more-->` break is present, positioned after the first 1–3 paragraphs
- Author exists in `data/team/team/` with an avatar image
- Publish date is correct

**SEO:**

- Title contains primary search terms and accurately describes content
- Title is ≤60 characters, or `allow_long_title: true` is set in frontmatter
- Meta description is ≤160 characters and includes key terms
- H2 headings use answer-first phrasing (lead with the answer, not the question)

**CTAs and closing:**

- CTA is specific to the post's topic domain, not generic
- Feature announcements link directly to relevant docs
- Use `{{< blog/cta-button >}}` shortcode where appropriate

**Code examples:**

- Use `chooser`/`choosable` shortcodes for multi-language code blocks
- Language specifier required on all fenced code blocks

**Images:**

- Comparison screenshots use side-by-side images of the same view (before/after)
- Screenshots have alt text and 1px gray borders
- Image file format matches its actual content (no WebP files saved as .png)
- Animated GIFs: max 1200px wide, 3 MB

**End-of-review publishing readiness checklist** — summarize as a checklist at the end of every blog review:

- [ ] `<!--more-->` break present after intro
- [ ] `meta_image` set and not the default placeholder
- [ ] `meta_image` uses current Pulumi logos
- [ ] Author profile exists with avatar
- [ ] All links resolve
- [ ] Code examples correct with language specifiers
- [ ] No animated GIFs used as the preview image
- [ ] Images have alt text; screenshots have 1px gray borders
- [ ] Title ≤60 chars or `allow_long_title: true` set

## Additional Instructions

When blog posts introduce or announce new Pulumi features, providers, or significant functionality changes:

1. Check if corresponding documentation exists in `content/docs/` for the feature being announced
2. Verify that documentation, tutorials, or guides adequately cover the new functionality
3. If documentation is missing or incomplete, note this in your review with:
    - Specific gaps identified (e.g., "No ESC integration guide found")
    - Suggested documentation locations (e.g., "Should add to `content/docs/esc/guides/`")
    - Recommended documentation type (tutorial, concept guide, reference, etc.)
