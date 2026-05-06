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

### AI-drafting signals

Run on `content/blog/**` and on `content/docs/**` files longer than ~300 lines. Six independent pattern checks; **≥3 triggers fires the section** (rendered per `docs-review:references:output-format` §AI-drafting signals).

1. **Uniform per-section template.** ≥5 H2 sections following the same internal structure: opening sentence + N bullets + closing transition + opening of next section. Detect by extracting per-section structure as a tuple `(opening, list_count, closing_transition)`; ≥5 identical tuples triggers.
1. **Set-piece transitions.** Phrases that pattern-match the AI-drafting list: "But here's the thing", "And that's the key insight", "Let's dive in", "Now here's where it gets interesting", "Here's what's wild", "The reality is", "But it gets better", "Here's the kicker". ≥3 hits triggers.
1. **Parallel four-bullet lists.** A bulleted list where each bullet has *exactly* the same structure (e.g., `**Term**: explanation` four times in a row, no irregularity). ≥2 such lists triggers.
1. **Em-dash density.** Em-dashes per 1000 words exceeds threshold (start at 8 per 1000 words; one em-dash per ~125 words is a strong AI-drafting signal). Tune in re-test if false-positive rate is high.
1. **Listicle-style numbered intros.** Multiple H2 sections starting with a number (`**1. Foo**` / `**2. Bar**`) AND each section ends with a one-sentence summary in parallel structure.
1. **Hedge-then-pivot construction.** Sentences of the form "While X is true, Y is also worth considering" or "Although X, what's really important is Y" — three or more occurrences in the same post.

**Dispatch.** Run the six detectors as two parallel subagents via the Agent tool (`general-purpose`). Each subagent receives only its three detector definitions (verbatim from the list above) plus the file content -- not the other subagent's detectors, not the rendering format, not this dispatch block.

- **`structural`** (Sonnet 4.6). Detectors 1, 3, 5 (uniform per-section template, parallel four-bullet lists, listicle-style numbered intros).
- **`lexical`** (Haiku 4.5). Detectors 2, 4, 6 (set-piece transitions, em-dash density, hedge-then-pivot construction).

Each subagent returns `{detector_index, triggered: bool, evidence: [<line-anchored quote>...]}` per detector. Main agent counts triggers across both; the existing **≥3 of 6** threshold and the rendering format (`docs-review:references:output-format` §AI-drafting signals) are unchanged.

The rendered section is a maintainer-signaling flag, not a finding bucket. Specific pattern instances that *also* constitute findings (set-piece transitions misleading the reader, an em-dash that creates ambiguity) surface separately in ⚠️ with the standard quote-and-rewrite mandate.

Complementary to `claude-triage.yml`'s author-allowlist + AI-trailer detection — that filters by author signals; this filters by content signals. Both can fire on the same PR.

---

Every finding names the *phrase* and the *pattern*: "nested clauses: 3 subordinates in one sentence; split into 2-3" beats "this prose is hard to follow."

## Do not flag

- **Sentence rhythm in isolation.** "This sentence could be tighter" without a quoted construction and a proposed rewrite is editorial feedback, not a review finding.
- **Stylistic preference between equivalents.** "You could say X instead of Y" where both are correct and idiomatic is not a finding. Only flag when a pattern above matches.
- **Quoted material.** Don't apply these patterns to text inside `>` blockquotes, error messages, fixture data, or API responses being illustrated.
- **Code identifiers and CLI output.** Variable names, function names, command output, and log lines aren't prose.
- **Anything Vale catches.** Passive voice, filler phrases, empty intensifiers, difficulty qualifiers, hedging, buzzwords, empty transitions, em-dash density, repetitive openers — all surface via `.vale-findings.json` per `docs-review:references:output-format` §Style nits. Don't double-flag.
