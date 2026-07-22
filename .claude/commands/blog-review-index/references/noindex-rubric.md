---
user-invocable: false
description: Advisory rubric for the noindex_signal assessment in blog-review findings. The model recommends; the future noindex process decides.
---

# Blog Review — Noindex Rubric

`noindex_signal.assessment` is **advisory evidence, not a decision**. The
eventual noindex process combines your content assessment with traffic and
Search Console thresholds you cannot see, and a human reviews the resulting
PRs. Your job is the content half: given what this post *says*, would a
search engine sending readers here serve them well?

## Assessments

- **`keep`** — the default. The post still answers its question truthfully,
  or has historical/announcement value that reads as such. Dated but honest
  content is `keep`: a 2020 tutorial that says it's about 2020 tooling and
  works within that frame harms nobody.
- **`candidate`** — the post's value to a searcher is questionable on
  content grounds: substantial unfixable `factual-rot`, a
  `deprecated-product` core, or `seo-thin` duplication where a better post
  exists. Reasonable people could disagree; the traffic data should settle it.
- **`strong-candidate`** — the post actively harms a reader who lands on it
  today: `blocker`-severity issues at its core, guidance that would break
  things if followed, or content whose subject no longer exists in any
  recognizable form. The gate requires at least one recorded issue before it
  accepts this assessment.

## Rules

1. **Ground the assessment in the issue list.** Every `candidate` /
   `strong-candidate` rationale must reference the recorded issues; an
   assessment with no supporting issues is invalid (the gate enforces this
   for `strong-candidate`).
2. **Never assess on age or traffic alone.** Old ≠ noindex; low-traffic ≠
   noindex. You don't have reliable traffic data, and the selection signals
   in the queue are for provenance, not judgment.
3. **Superseded ≠ worthless.** If a newer post covers the topic better,
   that's `seo-thin` evidence toward `candidate` — but only when the old
   post adds nothing (no unique migration path, no historical context worth
   ranking).
4. **The rationale is one or two sentences** a human skimming
   `_summary.json` can act on: what class of harm, anchored to which issues.
