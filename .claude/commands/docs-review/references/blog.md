---
user-invocable: false
description: Review criteria for blog posts and customer stories. Fact-check-first; heightened scrutiny by default.
---

# Review — Blog

Applied to blog posts (`content/blog/`) and customer stories (`content/case-studies/`). These are usually drafted whole-file (often with AI assistance) rather than edited incrementally, so scrutiny is `heightened` by default and the whole file is in scope.

> **Fact-check-first treatment.** Fact-check is the headline finding bucket. Get it right before commenting on AI-writing patterns or structure.

---

## Scope

- **Whole-file read** is mandatory. Diff-only is not enough -- AI-drafted blogs hallucinate in the surrounding prose, not just the changed lines.
- Pre-existing extraction is **always on** for blog files (see below).

## Criteria

The following reference files apply alongside the blog-specific priorities below. Consult each as content in the diff triggers a relevant rule:

- `docs-review:references:shared-criteria` — every file (links, frontmatter, shortcodes)
- `docs-review:references:code-examples` — wherever code appears
- `docs-review:references:prose-patterns` — prose-bearing content
- `docs-review:references:image-review` — wherever images appear

Investigate as content triggers each priority below.

### Priority 1 — Fact-check first

Invoke `docs-review:references:fact-check` (`scrutiny=heightened`) **before** any style pass. The reference owns claim extraction; in blog copy, pay particular attention to **performance multipliers**, **competitor claims**, and **adoption / market-position statistics** — common in this domain and high-blast-radius when wrong.

### Priority 2 — Prose patterns and spelling/grammar

Apply `docs-review:references:prose-patterns` and `docs-review:references:spelling-grammar`.

**Blog-specific patterns** (apply alongside the shared references):

- **TL;DR / summary paragraphs that restate the post.** The reader just finished reading; they don't need a recap. Quote the recap; propose removal.
- **Self-criticism of prior Pulumi decisions.** "We used to handle this badly," "the old way was wrong," "before we got this right." Acceptable in case-studies discussing a *customer's* prior tooling; not acceptable when describing prior Pulumi product behavior. Quote the construction; reframe as forward-looking: "v3.0 introduced X" not "before v3.0, we got it wrong."
- **Weak conclusions.** A closing paragraph that doesn't name a specific next step. "Check out Pulumi to learn more" without a specific link or command. Quote the conclusion; propose a concrete CTA: "Try it: `pulumi up` against the example at `<link>`" or "See the X reference at /docs/foo/."
- **Listicle bloat.** Posts structured as `## item N:` patterns or numbered top-N lists. Cap at 12 items; cap total post length at ≈3,000 words for listicles. If a list goes longer, suggest which items to cut or merge.

### Priority 3 — Code correctness

Apply `docs-review:references:code-examples`.

### Priority 4 — Product accuracy

Vale catches Pulumi product-name capitalization, the Pulumi Policies singular-verb rule, and "public preview" vs "public beta" (surfaced under ⚠️ Low-confidence per `docs-review:references:output-format` §Style nits). The reviewer's job here is the things Vale can't:

- **Feature names.** Capitalization and punctuation must match how the product refers to itself in docs. If a blog introduces a feature, the feature name should match the canonical doc page's title.
- **"Generally available," not "generally released."** Release terminology beyond what Vale's substitution list covers.
- **Canonical links to docs.** Every feature announcement should link to the relevant `/docs/` page. Missing doc links are a pre-existing-issue finding (the blog post is fine on its own; it's the site SEO that suffers).
- **"New" vs "now supports."** A feature that landed more than ~30 days ago should use "now supports" or "recently added," not "new." If the frontmatter `date` is old relative to the claim's subject, flag.
- **Title quality.** Title should describe the post's subject specifically and contain the topical hook a search/AI user would type. Flag:
  - **Clickbait constructions** ("You won't believe...", "10 things every X needs"), question-headlines without a clear payoff.
  - **Title/body mismatch.** Quote the title and the post's first paragraph; flag when the body's actual subject is materially different from what the title sells (e.g., title is "Improving Pulumi Performance," body is specifically about Bun-runtime startup time).
  - **Generic titles missing the topical hook.** "Improving Performance" or "A New Approach to X" without naming the product, feature, or specific outcome. Quote the title; propose a more specific rewrite that includes the primary subject.

### Priority 5 — Documentation coverage (feature-announcement posts only)

When a blog post announces a new feature, provider, or significant capability:

- **Check that `/content/docs/` covers it.** Search for the feature name across `content/docs/`, `content/learn/`, `content/tutorials/`. If the only mention of the feature is the blog post itself, that's a finding.
- **Note specific gaps.** Don't just say "docs are missing" — name the page that should exist (e.g., "no `content/docs/esc/integrations/<feature>/` page found").
- **Suggest a doc type.** Reference / tutorial / concept guide / how-to — pick the one that matches the feature's nature.

This is a project-completeness flag, not a blog quality issue.

### Priority 6 — SEO and discoverability

Concrete rules from `seo-analyze:references:aeo-checklist` applied at review time. Quote-and-rewrite mandate: every finding names a specific construction and proposes a fix.

- **Quotable opening paragraph.** The first 1–2 sentences should answer "what is this post about" as a standalone definition, with no fluff intro. Quote the opening; flag empty transitions ("In this post, we'll explore...", "Let's dive in", "In recent years...") and propose a direct first-sentence rewrite that names the subject.
- **Answer-first H2 headings.** For concept-heavy posts, prefer question-style or how-style headings ("How does Pulumi ESC handle secrets?") over label-style ("ESC overview"). Label headings rank lower for AI answer extraction. Quote the heading; propose an answer-first rewrite. Don't flag label headings on action posts ("Get started," "Install Pulumi") — those are correct.
- **Specific data over vague superlatives.** "Pulumi is much faster" / "many users adopted X" / "significantly improved" without numbers. Quote the claim; propose a specific number, percentage, or comparison. Where the post genuinely lacks data, flag for fact-check rather than rewrite.
- **Down-funnel specificity.** A feature post that introduces the feature but never shows a concrete integration, command, or code example is too generic to rank or be cited. Quote the most generic section; propose adding a specific use case (named integration, CI flow, edge case).
- **Numbered, executable steps for "how-to" content.** "Get started" / "Set up X" sections that read as prose instead of numbered steps with copy-pasteable commands. Quote the section; propose a numbered list with explicit commands.
- **Dated context where it matters.** Posts that describe behavior tied to a specific Pulumi version or external state should name it ("As of v3.150…", "On 2026-04-29…"), not assume the reader knows. Flag undated state claims.

### Priority 7 — Links

- **All links resolve.** Inherited from `docs-review:references:shared-criteria`.
- **Link text is descriptive.** Inherited.
- **First mention is hyperlinked.** Every tool, technology, or product's *first* mention in the post should be a link (to docs, to the project homepage, to a GitHub repo). Flag only first-mention misses; subsequent mentions don't need the link.
- **Missing cross-link to canonical Pulumi docs.** When the post mentions a Pulumi concept with a canonical doc page (stacks, providers, components, ESC environments, projects, programs, policy packs) and no occurrence of the term is hyperlinked, flag it once per concept. Quote the most prominent unlinked occurrence; propose the link target (e.g., `[stacks](/docs/iac/concepts/stacks/)`). Complements the rule above — that one covers external tools and projects; this one covers internal Pulumi concept docs.
- **`{{< github-card >}}` references.** Format `owner/repo`; verify the repo exists (`gh api repos/<owner>/<repo>`). A broken card renders as an ugly empty block.

## Pre-existing issues (always on)

Blog files are usually new in their entirety, so the diff/pre-existing distinction blurs. For incremental edits to existing posts, separate diff-introduced from pre-existing per the standard rules in `docs-review:references:output-format`.

Scope of pre-existing findings for blog: everything from `docs-review:references:docs`, plus unsourced numerical claims, temporally-rotted feature claims ("a new feature in v3.X" where v3.X is years old), broken `{{< github-card >}}` references, missing author avatars, `meta_image` that is still the placeholder, `meta_image` that uses outdated Pulumi logos (the brand refresh moved on; old logos hurt social sharing).

## Do not flag

- **Colloquialisms as inclusive-language violations.** "Overkill," "kill the process," "kick off," "blow away" are fine in technical context.
- **Drafting social copy, CTAs, or button text.** Marketing owns voice; do not propose replacement copy.
- **Meta image colors, composition, or layout.** Do not critique design choices. (See §Publishing blockers for retired-logo, placeholder, and animated-GIF cases.)
- **Vague editorial feedback without quote-and-rewrite.** "Consider rewording for engagement" / "this could be clearer" / "you should reorganize this section" without a quoted construction and a specific proposed rewrite is editorial vagueness, not a review finding. Concrete prose, structural, and SEO/AEO suggestions (apply `docs-review:references:prose-patterns`; split a mixed-concept H2; rewrite a label-style heading as answer-first) ARE in scope -- but every finding must quote the offending text and propose the fix.
- **Heading case.** markdownlint owns case-consistency; Vale owns product-name miscapitalization (e.g., "Pulumi esc"). Don't flag either here.
- **Anything Vale catches.** Product-name capitalization, Policies-singular, public-preview/public-beta, click→select, banned words, difficulty qualifiers — all surface via `.vale-findings.json` per `docs-review:references:output-format` §Style nits. Don't double-flag.

## Publishing blockers

Each item below renders as a single 🚨 Outstanding finding when violated. Quote-and-rewrite mandate: name the field or file, propose the specific fix.

- **`meta_image` uses retired Pulumi logos.** Inspect the rendered meta_image (or its filename / path) for retired brand variants. Quote the path; propose the current-brand replacement.
- **`meta_image` is the unmodified `/new-blog-post` placeholder.** Compute SHA256 of the resolved meta_image file and compare against `.claude/commands/_common/images/blog-post-meta-placeholder.png`. Match → flag with a pointer to `/blog-meta-image` for regeneration. Skip on `draft: true` or archival posts (`date` in the past).
- **`meta_image` animated-GIF / format constraints** — see `docs-review:references:image-review`.
- **`<!--more-->` break missing or buried.** The break must be present and land after the first 1–3 paragraphs, not buried mid-post. Without it, the entire post body renders on the blog index. Quote the surrounding paragraphs; propose the correct placement. Skip on `draft: true` or archival posts.
- **`social:` block missing or empty.** Active blog posts (not draft, not archival) must have a `social:` frontmatter block with at least one of `twitter`, `linkedin`, or `bluesky` populated; without it the post won't be promoted. Flag the missing/empty block; do not draft the copy (marketing owns voice).
- **Author profile avatar missing.** `data/team/team/{author}.yaml` must reference an avatar file. Quote the missing field or the path of the file that should exist.

Other publishing-readiness items (title ≤60 chars, meta_desc length, `meta_image` `.png` extension, code language specifiers, image alt text and borders, link resolution) are handled by `lint-markdown.js` or by other references (`docs-review:references:shared-criteria`, `docs-review:references:code-examples`, `docs-review:references:image-review`). Don't re-flag them here.
