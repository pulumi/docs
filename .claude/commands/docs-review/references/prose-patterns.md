---
user-invocable: false
description: Concrete prose patterns to flag in user-facing content. Quote-and-rewrite mandate; no abstract editorial advice.
---

# Prose Patterns

Applied to prose-bearing content (docs and blogs). Concrete patterns only — every finding must quote the offending text and propose a rewrite. If you can't quote the construction or propose a fix, drop the finding. Abstract "this could be clearer" / "consider reorganizing" feedback isn't a review concern.

**Cap findings at 5 per file.** If a file has more, surface only the most impactful (the ones whose fix most improves clarity). Force triage; don't render every instance.

---

## Patterns

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

---

## Do not flag

- **Sentence rhythm in isolation.** "This sentence could be tighter" without a quoted construction and a proposed rewrite is editorial feedback, not a review finding.
- **Stylistic preference between equivalents.** "You could say X instead of Y" where both are correct and idiomatic is not a finding. Only flag when a pattern above matches.
- **Quoted material.** Don't apply these patterns to text inside `>` blockquotes, error messages, fixture data, or API responses being illustrated.
- **Code identifiers and CLI output.** Variable names, function names, command output, and log lines aren't prose.
