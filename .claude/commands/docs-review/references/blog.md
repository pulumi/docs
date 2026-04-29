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

The priorities below are ordered for **output rendering** — fact-check findings render before style findings — but investigate as content triggers each.

### Priority 1 — Fact-check first

Invoke `docs-review:references:fact-check` (`scrutiny=heightened`) **before** any style pass. The reference owns claim extraction; in blog copy, pay particular attention to **performance multipliers**, **competitor claims**, and **adoption / market-position statistics** — common in this domain and high-blast-radius when wrong.

Findings render in 🚨 / ⚠️ **before** style findings.

### Priority 2 — AI-slop detection

Flag the following patterns, with examples from the post. Each bullet names the *pattern* and the threshold at which it becomes a finding.

**Unit of measurement -- "section":** in this file, *section* means the block of prose from one H2 (`## ...`) heading to the next, or from the `<!--more-->` break to the first H2 if one leads the post. Flags and thresholds below all evaluate over that unit unless noted otherwise.

- **Em-dash density.** Three or more em-dashes in a single section. AI models overuse em-dashes as a rhythm device. Style guide allows them; heavy clustering is a tell.
- **Contrastive frames.** "It's not X, it's Y" / "Not only X but also Y" / "This isn't about X; it's about Y." One in a post is fine. Three or more across the post (not per-section) is a pattern finding.
- **Uniform sentence rhythm.** Three or more consecutive sentences of similar length (within ±3 words) in a single paragraph. Humans vary rhythm; AI drifts toward a mean.
- **Repetitive paragraph openers.** Three or more consecutive paragraphs (in the same section or across a section boundary) opening with the same structure: "When you X...", "If you want to X...", "Consider X...".
- **Hedging.** "Typically," "generally," "tends to," "can often," "largely," "in many cases." Two or more in a single section is a finding. See also `STYLE-GUIDE.md`'s write-with-confidence rule.
- **TL;DR / summary paragraphs that restate the post.** The reader just finished reading; they don't need a recap.
- **Empty transitions.** "Let's dive in," "In this post we'll explore," "In conclusion," "Without further ado." Cut them -- flag on first occurrence.
- **Buzzword tax.** "Landscape," "ecosystem," "leverage" (as a verb), "robust," "seamless," "world-class," "battle-tested." Flag on first occurrence, with a suggested rewrite when the sentence survives the deletion; otherwise flag as a rewrite candidate. If the same buzzword appears three or more times across the post, coalesce the flags into a single finding rather than repeating.
- **Self-criticism of prior Pulumi decisions.** "We used to handle this badly," "the old way was wrong," "before we got this right." Acceptable in case-studies discussing a *customer's* prior tooling; not acceptable when describing prior Pulumi product behavior. Quote the construction; reframe as forward-looking: "v3.0 introduced X" not "before v3.0, we got it wrong."
- **Weak conclusions.** A closing paragraph that doesn't name a specific next step. "Check out Pulumi to learn more" without a specific link or command. Quote the conclusion; propose a concrete CTA: "Try it: `pulumi up` against the example at `<link>`" or "See the X reference at /docs/foo/."
- **Dense paragraphs.** Paragraphs longer than 6 sentences or filling more than 8 visual lines. Often a sign the content should be a list, a sub-section, or split. Quote the opening; propose either a split or a list conversion.
- **Listicle bloat.** Posts structured as `## item N:` patterns or numbered top-N lists. Cap at 12 items; cap total post length at ≈3,000 words for listicles. If a list goes longer, suggest which items to cut or merge.

Every AI-slop / editorial finding names the *phrase* and the *pattern*. Don't just say "this is AI-written" -- say "em-dash density: 6 em-dashes across 3 paragraphs; consider breaking some into separate sentences."

### Priority 3 — Code correctness

Apply `docs-review:references:code-examples`.

### Priority 4 — Product accuracy

- **Pulumi product names.** Per `STYLE-GUIDE.md`: "Pulumi IaC," "Pulumi ESC," "Pulumi IDP," "Pulumi Cloud," "Pulumi Insights," "Pulumi Policies" (singular).
- **Feature names.** Capitalization and punctuation must match how the product refers to itself in docs. If a blog introduces a feature, the feature name should match the canonical doc page's title.
- **Release terminology.** "Public preview," not "public beta" (per `STYLE-GUIDE.md`). "Generally available," not "generally released."
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

Render under 💡 Pre-existing (this is a project-completeness flag, not a blog quality issue) so the blog can ship without blocking on docs work.

### Priority 6 — SEO and discoverability

These are the feasible, concrete rules from `seo-analyze:references:aeo-checklist` applied at review time. Quote-and-rewrite mandate: every finding names a specific construction and proposes a fix. The full AEO scoring pass still belongs to `/seo-analyze` for deeper analysis; these are the items that catch on a normal review.

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
- **`{{< github-card >}}` references.** Format `owner/repo`; verify the repo exists (`gh api repos/<owner>/<repo>`). A broken card card renders as an ugly empty block.

## Pre-existing issues (always on)

Blog files are usually new in their entirety, so the diff/pre-existing distinction blurs. Render every finding under 🚨 Outstanding when the post is new. For incremental edits to existing posts, separate diff-introduced from pre-existing per the standard rules in `docs-review:references:output-format`. Cap at 15 per file.

Scope of pre-existing findings for blog: everything from `docs-review:references:docs`, plus unsourced numerical claims, temporally-rotted feature claims ("a new feature in v3.X" where v3.X is years old), broken `{{< github-card >}}` references, missing author avatars, `meta_image` that is still the placeholder, `meta_image` that uses outdated Pulumi logos (the brand refresh moved on; old logos hurt social sharing).

## Fact-check

Invoke `docs-review:references:fact-check` with:

- **Files:** the changed `content/blog/**` / `content/case-studies/**` files
- **Scrutiny:** `heightened` (always)

CI fact-check is public-sources-only -- see `docs-review/ci.md`.

## Do not flag

- **Colloquialisms as inclusive-language violations.** "Overkill," "kill the process," "kick off," "blow away" are fine in technical context.
- **Drafting social copy, CTAs, or button text.** Flag when the `social:` block is missing or malformed; do not draft replacement copy. Marketing owns voice here, not the reviewer.
- **Meta image design critique.** Flag when `meta_image` is the placeholder or uses outdated logos. Do not critique colors, composition, or layout.
- **Vague editorial feedback without quote-and-rewrite.** "Consider rewording for engagement" / "this could be clearer" / "you should reorganize this section" without a quoted construction and a specific proposed rewrite is editorial vagueness, not a review finding. Concrete prose, structural, and SEO/AEO suggestions (apply `docs-review:references:prose-patterns`; split a mixed-concept H2; rewrite a label-style heading as answer-first) ARE in scope -- but every finding must quote the offending text and propose the fix.
- **Heading case already consistent within the file.** Style linters catch inconsistency. The only heading case that's a finding is one that names a product incorrectly (e.g., "Pulumi esc" instead of "Pulumi ESC").

## Publishing-readiness checklist

End every blog review with this checklist as a 💡 Pre-existing block. Each item is a single-line finding when violated; the full checklist exists as a roll-up so the author can scan readiness at a glance:

- [ ] `social:` block present with copy for `twitter`, `linkedin`, `bluesky` (without it, the post won't be promoted on social)
- [ ] `meta_image` set, not empty (0 bytes), and not the default placeholder (used by LinkedIn + social cards)
- [ ] `meta_image` uses current Pulumi logos, not retired brand variants
- [ ] `<!--more-->` break present, positioned after the first 1–3 paragraphs (not buried mid-post)
- [ ] Author profile exists in `data/team/team/` with an avatar
- [ ] All links resolve (inherited from `docs-review:references:shared-criteria`)
- [ ] Code examples correct with language specifiers (per `docs-review:references:code-examples`)
- [ ] No animated GIFs used as `meta_image` (first-frame fallback breaks the social preview)
- [ ] Images have alt text; screenshots have 1px gray borders (per `docs-review:references:image-review`)
- [ ] Title ≤60 characters or `allow_long_title: true` set in frontmatter

Several of these are caught at pre-commit by `lint-markdown.js` (title length, meta description length, `meta_image` placeholder). Items the linter catches don't need to be flagged again here — render the checklist with linter-caught items already checked.
