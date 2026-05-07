---
user-invocable: false
description: Concrete prose patterns to flag in user-facing content. Quote-and-rewrite mandate; no abstract editorial advice.
---

# Prose Patterns

Applied to prose-bearing content (docs and blogs). Concrete patterns only — every finding must quote the offending text and propose a rewrite. If you can't quote the construction or propose a fix, drop the finding. Abstract "this could be clearer" / "consider reorganizing" feedback isn't a review concern.

**Cap structural-pattern findings at 10 per file.** Spelling and grammar render uncapped (see below). If a file has more than 10 structural findings, surface only the most impactful; don't render every instance.

---

## Patterns

> **Section unit.** Patterns with thresholds (hedging, repetitive openers, contrastive frames) evaluate over the block of prose between consecutive H2 (`## ...`) headings. In blog posts, the content from `<!--more-->` to the first H2 is also a section.

### Spelling and grammar

Apply `docs-review:references:spelling-grammar`. Render every finding — no cap.

### Undefined acronyms

A 2–5 letter capitalized acronym appears in the diff without a preceding `(parenthetical expansion)` and without prior expansion earlier in the file. Common offenders: IAM, ESC, IDP, IaC, DSL, RBAC, OIDC, SCIM. Quote the first occurrence; propose adding the expansion.

Don't flag well-established terms readers know unaided: HTTP, JSON, SQL, AWS, GCP, API, CLI, URL, IDE, OS.

### Nested clause stacks

Sentences with three or more subordinate clauses chained together (`which X, that Y, while Z, with the result that ...`). Quote the sentence; propose splitting into 2–3 sentences.

Example:

> "The resource, which inherits its provider from the parent stack, that defines the region as us-east-1, while also setting the bucket policy, is created during preview."

Propose:

> "The resource is created during preview. It inherits its provider from the parent stack and uses the parent's region (us-east-1). The bucket policy is set in the same step."

### Contrastive frames

`It's not X, it's Y` / `Not only X but also Y` / `This isn't about X; it's about Y`. One in a file is fine. Three or more across the file is a pattern finding.

### Uniform sentence rhythm

Three or more consecutive sentences of similar length (within ±3 words) in a single paragraph. Quote the paragraph; propose varying length by combining or splitting one sentence.

### Dense paragraphs

Paragraphs longer than 6 sentences or 8 visual lines. Often a sign the content should be a list, sub-section, or split. Quote the opening; propose a split or list conversion.

### AI-drafting tells

A handful of specific AI-drafting tells are caught by Vale rules under `styles/Pulumi/`: `SetPieceTransitions` (stock opener phrases), `EmDashDensity` (paragraph-level em-dash overuse), `ListicleH2Headings` (numbered listicle structure at H2), `HedgeThenPivot` (`While X, Y is also worth ...` constructions). Findings render as `⚠️ Low-confidence` style nits per `docs-review:references:output-format` §Style nits — the model does not aggregate or render a separate "AI-drafting" section.

These are heuristics, not classifiers. A single hit is hedged copy ("often appears in AI-drafted prose; consider rewriting"), surfaced for the maintainer to weigh. False positives are expected and easily ignored.

Complementary to `claude-triage.yml`'s author-allowlist + AI-trailer detection — that filters by author signals; this filters by surface phrasing.

---

Every finding names the *phrase* and the *pattern*: "nested clauses: 3 subordinates in one sentence; split into 2-3" beats "this prose is hard to follow."

## Do not flag

- **Sentence rhythm in isolation.** "This sentence could be tighter" without a quoted construction and a proposed rewrite is editorial feedback, not a review finding.
- **Stylistic preference between equivalents.** "You could say X instead of Y" where both are correct and idiomatic is not a finding. Only flag when a pattern above matches.
- **Quoted material.** Don't apply these patterns to text inside `>` blockquotes, error messages, fixture data, or API responses being illustrated.
- **Code identifiers and CLI output.** Variable names, function names, command output, and log lines aren't prose.
- **Anything Vale catches.** Passive voice, filler phrases, empty intensifiers, difficulty qualifiers, hedging, buzzwords, empty transitions, em-dash density, repetitive openers — all surface via `.vale-findings.json` per `docs-review:references:output-format` §Style nits. Don't double-flag.
