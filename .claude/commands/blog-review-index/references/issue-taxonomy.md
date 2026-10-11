---
user-invocable: false
description: The closed issue taxonomy and severity rubric for the blog known-issues index. record-findings.py validates every finding against this set.
---

# Blog Review — Issue Taxonomy

The taxonomy is **closed**: every issue in `.blog-review-findings.json` must
use one of the categories below, verbatim. The deterministic gate
(`scripts/blog-review/validate-findings.py` — keep its `CATEGORIES` set in
sync with this file) rejects anything else and the run is recorded
`incomplete`. If a real defect genuinely fits no category, record the
nearest one and say so in the evidence; propose a taxonomy change in a PR to
this file, never by inventing a value inline.

## Categories

| Category | What it covers |
|----------|----------------|
| `factual-rot` | A claim that was true at publish time and is now false or materially misleading: stale version-specific behavior presented as current, superseded benchmarks or pricing, "coming soon" for things that shipped (or died), statistics that no longer hold. |
| `dead-link` | A link that 404s, redirects to an irrelevant target, or points at a product/page that no longer exists. Internal links that miss their alias chain count. |
| `broken-code` | Code samples that no longer work: removed/renamed APIs, syntax invalid against current SDKs, imports that don't resolve, CLI flags that were dropped. Evidence must name the current API surface, not just suspicion. |
| `deprecated-product` | The post is about — or materially depends on — a Pulumi or third-party product/feature that has been renamed, deprecated, or retired (e.g. a walkthrough of a UI that no longer exists). |
| `seo-thin` | The post has little durable value for a searcher: near-duplicate of another post that does the job better, contentless announcement of a long-past event, listicle bloat with no substance. Name the superseding URL when one exists. |
| `ai-positioning` | The post violates the AGENTS.md "AI and agent positioning" rules: presents Neo as the only way to use AI with Pulumi, frames Neo as either-or against other coding agents, or disparages other agents. |
| `frontmatter` | Taxonomy/frontmatter defects: missing or invalid `category`, tag near-duplicates against `data/blog_tags.yaml`, series slug misuse, missing `meta_desc`, broken author reference. |
| `rendering` | The published page renders broken content: shortcode errors visible in output, missing images, malformed tables/code fences, a broken or buried `<!--more-->` break. |

## Severity rubric

| Severity | Bar |
|----------|-----|
| `blocker` | The post actively misleads or embarrasses **today**: a wrong claim a reader would act on, code that fails against current SDKs in a post that ranks, a walkthrough of a retired product presented as current. These drive noindex decisions hardest. |
| `major` | Clearly degrades the post's usefulness but a reader can route around it: a dead link on the main path, factual rot with visible date context, a deprecated product mentioned but not central. |
| `minor` | Real but low-stakes: a dead link in a footnote, tag hygiene, a stale minor version number in prose that doesn't change the guidance. |

Severity is about **reader harm now**, not about how hard a fix would be.
When torn between two severities, pick the lower one and let the evidence
speak — the index is aggregated over time, and inflation is worse than
understatement.
