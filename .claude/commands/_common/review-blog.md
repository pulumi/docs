---
user-invocable: false
description: Review criteria for blog posts and customer stories. Fact-check-first; heightened scrutiny by default.
---

# Review — Blog

Applied to blog posts (`content/blog/`) and customer stories (`content/customers/`). These are usually drafted whole-file (often with AI assistance) rather than edited incrementally, so scrutiny is `heightened` by default and the whole file is in scope.

> **Fact-check-first treatment.** Fact-check is the headline finding bucket. Get it right before commenting on AI-writing patterns or structure.

---

## Scope

- **Whole-file read** is mandatory. Diff-only is not enough -- AI-drafted blogs hallucinate in the surrounding prose, not just the changed lines.
- Pre-existing extraction is **always on** for blog files (see below).

## Criteria

Apply [`review-shared.md`](review-shared.md) first. Then work through the five priorities below *in order* -- fact-check findings render before style findings in the output.

### Priority 1 — Fact-check first

Invoke [`fact-check.md`](fact-check.md) (`scrutiny=heightened`) **before** any style pass. Claim extraction covers:

- **Every number.** Performance multipliers ("41x faster"), throughput numbers, user counts, customer counts, version numbers, percentages, pricing, benchmark figures.
- **Every tech claim about Pulumi products.** "Pulumi ESC supports X." "Pulumi Cloud now does Y." "New in v3.X." If the diff asserts a capability, verify it against the current registry schema, release notes, or source.
- **Every tech claim about competitors and third-party tools.** "Terraform requires X." "CloudFormation doesn't support Y." Wrong claims about competitors are embarrassing and quotable.
- **Every benchmark or comparison.** "X is faster than Y." "Z reduces latency by N%." Needs a source.
- **Every adoption or market-position statistic.** "Used by N% of Fortune 500." "The most popular IaC tool for K8s." Needs a source.

Findings render in 🚨 / ⚠️ **before** style findings. The reader sees "is this post factually sound?" before "does this post read like a human wrote it?".

### Priority 2 — AI-slop detection

Flag the following patterns, with examples from the post. Each bullet names the *pattern* and the threshold at which it becomes a finding.

**Unit of measurement -- "section":** in this file, *section* means the block of prose from one H2 (`## ...`) heading to the next, or from the `<!--more-->` break to the first H2 if one leads the post. Flags and thresholds below all evaluate over that unit unless noted otherwise.

- **Em-dash density.** Three or more em-dashes in a single section. AI models overuse em-dashes as a rhythm device. Style guide allows them; heavy clustering is a tell.
- **Contrastive frames.** "It's not X, it's Y" / "Not only X but also Y" / "This isn't about X; it's about Y." One in a post is fine. Three or more across the post (not per-section) is a pattern finding.
- **Uniform sentence rhythm.** Three or more consecutive sentences of similar length (within ±3 words) in a single paragraph. Humans vary rhythm; AI drifts toward a mean.
- **Repetitive paragraph openers.** Three or more consecutive paragraphs (in the same section or across a section boundary) opening with the same structure: "When you X...", "If you want to X...", "Consider X...".
- **Hedging.** "Typically," "generally," "tends to," "can often," "largely," "in many cases." Two or more in a single section is a finding. See also `STYLE-GUIDE.md`'s write-with-confidence rule in the legacy `review-criteria.md` §Blogs.
- **TL;DR / summary paragraphs that restate the post.** The reader just finished reading; they don't need a recap.
- **Empty transitions.** "Let's dive in," "In this post we'll explore," "In conclusion," "Without further ado." Cut them -- flag on first occurrence.
- **Buzzword tax.** "Landscape," "ecosystem," "leverage" (as a verb), "robust," "seamless," "world-class," "battle-tested." Flag on first occurrence, with a suggested rewrite when the sentence survives the deletion; otherwise flag as a rewrite candidate. If the same buzzword appears three or more times across the post, coalesce the flags into a single finding rather than repeating.

Every AI-slop finding names the *phrase* and the *pattern*. Don't just say "this is AI-written" -- say "em-dash density: 6 em-dashes across 3 paragraphs; consider breaking some into separate sentences."

### Priority 3 — Code correctness

Same standard as [`review-docs.md`](review-docs.md) §Code examples. Code in blog posts gets heavily copied because people Google into blogs as often as into docs. Wrong code is wrong regardless of which `content/` directory it lives in.

For Pulumi example code specifically: imports resolve, property names match the provider schema, language-specific casing is correct.

### Priority 4 — Product accuracy

- **Pulumi product names.** Per `STYLE-GUIDE.md`: "Pulumi IaC," "Pulumi ESC," "Pulumi IDP," "Pulumi Cloud," "Pulumi Insights," "Pulumi Policies" (singular).
- **Feature names.** Capitalization and punctuation must match how the product refers to itself in docs. If a blog introduces a feature, the feature name should match the canonical doc page's title.
- **Release terminology.** "Public preview," not "public beta" (per `STYLE-GUIDE.md`). "Generally available," not "generally released."
- **Canonical links to docs.** Every feature announcement should link to the relevant `/docs/` page. Missing doc links are a pre-existing-issue finding (the blog post is fine on its own; it's the site SEO that suffers).
- **"New" vs "now supports."** A feature that landed more than ~30 days ago should use "now supports" or "recently added," not "new." If the frontmatter `date` is old relative to the claim's subject, flag.

### Priority 5 — Links

- **All links resolve.** Inherited from [`review-shared.md`](review-shared.md).
- **Link text is descriptive.** Inherited.
- **First mention is hyperlinked.** Every tool, technology, or product's *first* mention in the post should be a link (to docs, to the project homepage, to a GitHub repo). Flag only first-mention misses; subsequent mentions don't need the link.
- **`{{< github-card >}}` references.** Format `owner/repo`; verify the repo exists (`gh api repos/<owner>/<repo>`). A broken card card renders as an ugly empty block.

## Pre-existing issues (always on)

Blog files are usually new in their entirety, so the diff/pre-existing distinction blurs. Render every finding under 🚨 Outstanding when the post is new. For incremental edits to existing posts, separate diff-introduced from pre-existing per the standard rules in [`docs-review-core.md`](docs-review-core.md). Cap at 15 per file.

Scope of pre-existing findings for blog: everything from `review-docs.md`, plus unsourced numerical claims, temporally-rotted feature claims ("a new feature in v3.X" where v3.X is years old), broken `{{< github-card >}}` references, missing author avatars, `meta_image` that is still the placeholder.

## Fact-check

Invoke [`fact-check.md`](fact-check.md) with:

- **Files:** the changed `content/blog/**` / `content/customers/**` files
- **Scrutiny:** `heightened` (always)

CI fact-check is public-sources-only -- see `docs-review-ci.md`. Notion and Slack are explicitly excluded for blog content in CI because blog claims are the most likely to surface internal context that shouldn't be in a public PR comment.

## Do not flag

- **Colloquialisms as inclusive-language violations.** "Overkill," "kill the process," "kick off," "blow away" are fine in technical context. (The audit's most frequent false-positive class; sample PR #18493.) Note: this intentionally relaxes `STYLE-GUIDE.md` §Inclusive Language -- the style guide rule stands for authors; the review skill stops nagging about it.
- **Drafting social copy, CTAs, or button text.** Flag when the `social:` block is missing or malformed; do not draft replacement copy. Marketing owns voice here, not the reviewer.
- **Meta image design critique.** Flag when `meta_image` is the placeholder or uses outdated logos. Do not critique colors, composition, or layout.
- **"Consider rewording for engagement."** If there's a factual issue with the wording, say so. Don't draft a more engaging version for its own sake.
- **Structural rewrites.** "You should reorganize this section" is editorial, not a review finding. Flag factual, link, or code errors -- don't propose TOC rearrangements.
- **Publishing-readiness checklist.** The legacy `review-criteria.md` has a checklist block (social, meta_image, avatar, `<!--more-->` break). That's a separate tool's job. Here, flag missing `social:` / `meta_image` / author profile as single-line findings; don't render the full checklist in every review.
- **Heading case already consistent within the file.** Style linters catch inconsistency. The only heading case that's a finding is one that names a product incorrectly (e.g., "Pulumi esc" instead of "Pulumi ESC").
