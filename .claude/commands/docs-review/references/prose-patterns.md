---
user-invocable: false
description: Concrete prose patterns to flag in user-facing content. Quote-and-rewrite mandate; no abstract editorial advice.
---

# Prose Patterns

Applied to prose-bearing content (docs and blogs). Concrete patterns only — every finding must quote the offending text and propose a rewrite. If you can't quote the construction or propose a fix, drop the finding. Abstract "this could be clearer" / "consider reorganizing" feedback isn't a review concern.

**Cap structural-pattern findings at 10 per file.** Spelling and grammar render uncapped (see below). If a file has more than 10 structural findings, surface only the most impactful; don't render every instance.

---

## Patterns

> **Section unit.** Patterns with thresholds (em-dash density, hedging, repetitive openers, contrastive frames) evaluate over the block of prose between consecutive H2 (`## ...`) headings. In blog posts, the content from `<!--more-->` to the first H2 is also a section.

### Spelling and grammar

Apply `docs-review:references:spelling-grammar`. Render every finding — no cap.

### Passive voice

Patterns: `was/were/been/being + past participle`, `is/are + past participle` where the actor is named or recoverable from context. Quote the construction; propose an active rewrite.

- "the bucket is created by Pulumi" → "Pulumi creates the bucket"
- "the secret was rotated by ESC" → "ESC rotates the secret"

Don't flag when the actor is genuinely unknown or irrelevant: "the request is sent to the API," "the function is called when the resource updates" stay.

### Filler and prepositional bloat

| Flag | Replace with |
|---|---|
| `in order to` | `to` |
| `due to the fact that` | `because` |
| `at this point in time` | `now` |
| `for the purpose of` | `for` |
| `with respect to`, `in regard to` | `about` |
| `a number of` | `several`, or a specific count |
| `prior to` | `before` |
| `subsequent to` | `after` |

Quote the phrase in context; propose the shorter form.

### Empty intensifiers

`very`, `really`, `quite`, `rather`, `actually`, `basically`, `essentially` used as filler before an adjective. Quote with surrounding context; propose removal or a specific number.

- "very fast" → "fast" (or "completes in <50ms")
- "really simple" → "simple" — and reconsider "simple" itself per Difficulty qualifiers below
- "basically a wrapper" → "a wrapper"

Don't flag when the word carries semantic weight: "very specific" meaning "narrowly scoped" can stay if the meaning is preserved.

### Difficulty qualifiers

`easy`, `simple`, `just`, `obviously`, `clearly`, `of course` when characterizing task difficulty. These tell the reader how they should feel rather than letting the steps speak. Per `STYLE-GUIDE.md`. Quote the sentence; propose removal.

- "Just run `pulumi up`" → "Run `pulumi up`"
- "This is an easy way to..." → "This..." or describe the approach without judging difficulty
- "Obviously, you'll need..." → "You'll need..."

### Undefined acronyms

A 2–5 letter capitalized acronym appears in the diff without a preceding `(parenthetical expansion)` and without prior expansion earlier in the file. Common offenders: IAM, ESC, IDP, IaC, DSL, RBAC, OIDC, SCIM. Quote the first occurrence; propose adding the expansion.

Don't flag well-established terms readers know unaided: HTTP, JSON, SQL, AWS, GCP, API, CLI, URL, IDE, OS.

### Nested clause stacks

Sentences with three or more subordinate clauses chained together (`which X, that Y, while Z, with the result that ...`). Quote the sentence; propose splitting into 2–3 sentences.

Example:

> "The resource, which inherits its provider from the parent stack, that defines the region as us-east-1, while also setting the bucket policy, is created during preview."

Propose:

> "The resource is created during preview. It inherits its provider from the parent stack and uses the parent's region (us-east-1). The bucket policy is set in the same step."

### Hedging

`Typically`, `generally`, `tends to`, `can often`, `largely`, `in many cases` — undermine confidence when the underlying claim is concrete. Two or more in a single section is a finding. See also `STYLE-GUIDE.md`'s write-with-confidence rule.

- "Pulumi typically resolves outputs eagerly" → "Pulumi resolves outputs eagerly"
- "ESC tends to rotate every 24 hours" → "ESC rotates every 24 hours"

### Buzzword tax

`landscape`, `ecosystem`, `leverage` (as a verb), `robust`, `seamless`, `world-class`, `battle-tested`. Flag on first occurrence with a suggested rewrite when the sentence survives the deletion; otherwise flag as a rewrite candidate. If the same buzzword appears three or more times across the file, coalesce the flags into a single finding.

### Empty transitions

`Let's dive in`, `In this post we'll explore`, `In conclusion`, `Without further ado`, `In recent years`. Cut them — flag on first occurrence.

### Contrastive frames

`It's not X, it's Y` / `Not only X but also Y` / `This isn't about X; it's about Y`. One in a file is fine. Three or more across the file is a pattern finding.

### Em-dash density

Three or more em-dashes (`---` or `—`) in a single section. Em-dashes are allowed style; heavy clustering is a tell. Quote the section's lead em-dash; propose breaking one or two into separate sentences.

### Uniform sentence rhythm

Three or more consecutive sentences of similar length (within ±3 words) in a single paragraph. Quote the paragraph; propose varying length by combining or splitting one sentence.

### Repetitive paragraph openers

Three or more consecutive paragraphs opening with the same structure: `When you X...`, `If you want to X...`, `Consider X...`. Quote one of the openers; propose rewording at least one.

### Dense paragraphs

Paragraphs longer than 6 sentences or 8 visual lines. Often a sign the content should be a list, sub-section, or split. Quote the opening; propose a split or list conversion.

---

Every finding names the *phrase* and the *pattern*: "em-dash density: 6 em-dashes across 3 paragraphs; break some into separate sentences" beats "this prose is AI-written."

## Do not flag

- **Sentence rhythm in isolation.** "This sentence could be tighter" without a quoted construction and a proposed rewrite is editorial feedback, not a review finding.
- **Stylistic preference between equivalents.** "You could say X instead of Y" where both are correct and idiomatic is not a finding. Only flag when a pattern above matches.
- **Quoted material.** Don't apply these patterns to text inside `>` blockquotes, error messages, fixture data, or API responses being illustrated.
- **Code identifiers and CLI output.** Variable names, function names, command output, and log lines aren't prose.
