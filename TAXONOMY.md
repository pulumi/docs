# TAXONOMY.md — Content types for pulumi.com

This document defines the canonical vocabulary for the kinds of content published on pulumi.com, and states who **owns**, who **contributes to**, and who **consumes** each type. Use these terms in nav headings, page titles, planning docs, and cross-team conversation.

## Why this document exists

The word **"guides"** currently refers to five different things:

1. Docs uses **"Guides"** as a second-level nav heading inside several product sections (`content/docs/esc/guides/`, `content/docs/deployments/guides/`, `content/docs/idp/guides/` all carry `title: Guides`; `content/docs/iac/guides/` holds the same kind of content but has no landing page of its own).
2. Marketing publishes **pulumi.com/guides** — "End-to-end blueprints for real cloud patterns" plus a library of Neo prompts. That page is **not** served from this repository.
3. Marketing also publishes **pulumi.com/tutorials**, which are occasionally referred to as guides.
4. The Registry currently republishes Pulumi examples and labels them "how-to guides".
5. Historic docs URLs like `/docs/guides/...` still circulate and are handled by redirects (`scripts/redirects/`).

This document disambiguates those terms, assigns an owner to every content type, and records the naming conflicts we still need to resolve. It complements, and does not replace:

- `AGENTS.md` — file placement and agent workflow rules
- `STYLE-GUIDE.md` — prose and formatting rules
- `BLOGGING.md` — blog-specific authoring rules
- `CONTRIBUTING.md` — review pipeline and domain labels

## Ownership vocabulary

Teams:

- **Docs** — the documentation team (`@pulumi/docs` in the intended CODEOWNERS mapping).
- **Community Eng** — developer relations and advocacy.
- **Marketing** — technical content marketing, product marketing, and growth.
- **Eng/Product** — product engineering and product management.

"Owns" means: sets the standards for the type, approves changes, and is accountable for accuracy and upkeep. "Contributes" means: routinely authors or supplies material, subject to the owner's review. "Consumes" describes the primary audience the type is written for.

## The taxonomy

### Conceptual documentation ("Concepts")

**Definition:** Explanation-oriented documentation that builds a mental model — what a thing is, how it works, and why it's designed that way. Not tied to a specific task.

- **Lives at:** `content/docs/*/concepts/` (e.g. `content/docs/iac/concepts/`, `content/docs/esc/concepts/`)
- **Examples:** [Stacks](https://www.pulumi.com/docs/iac/concepts/stacks/), [State and backends](https://www.pulumi.com/docs/iac/concepts/state-and-backends/)
- **Owns:** Docs
- **Contributes:** Eng/Product (feature knowledge), DevRel
- **Consumes:** Practitioners building an understanding of how Pulumi works

### Guides

**Definition:** Task-oriented documentation for a reader who already knows what they want to accomplish — a sequence of steps to a specific, practical goal, inside the product docs. Assumes working knowledge; doesn't teach fundamentals.

- **Lives at:** `content/docs/iac/guides/`, `content/docs/esc/guides/`, `content/docs/deployments/guides/`, `content/docs/idp/guides/`
- **Examples:** [Migrating from Terraform](https://www.pulumi.com/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/), ESC + GitHub Actions integration guides
- **Owns:** Docs
- **Contributes:** Eng/Product, DevRel, community
- **Consumes:** Practitioners new to Pulumi or seeking help with (or a better understanding of) a particular product or feature

### Tutorials

**Definition:** Task-oriented, sequenced, hands-on lessons. The reader follows along end to end and comes out having *built something* and *learned Pulumi*. Tutorials sometimes have time estimates and are occasionally grouped into collections and multi-part modules. 

- **Lives at:** `content/tutorials/` → [pulumi.com/tutorials](https://www.pulumi.com/tutorials/) (also aliased at `/learn`) and `content/docs/*/get-started`
- **Examples:** IaC Get Started, Deployments Get Started, ESC Get Started, Pulumi Fundamentals (3-part module), "Importing AWS Infrastructure"
- **Owns:** Marketing
- **Contributes:** Docs, Eng/Product
- **Consumes:** Newcomers and learners

**Getting Started** (`content/docs/get-started/`, `content/docs/install/`) is the onboarding end of this same family — first-run, learning-oriented content — and follows tutorial conventions, but lives inside `/docs/` because it's the docs' front door.

### Reference

**Definition:** Lookup material — exhaustive, structured, factual. Optimized for finding one precise answer, not for reading front to back.

- **Lives at:** `content/docs/reference/`, generated CLI docs (`content/docs/iac/cli/commands/`, `content/docs/esc/cli/commands/`), SDK/API reference, and the [Pulumi Registry](https://www.pulumi.com/registry/) (published from its own pipeline)
- **Examples:** `pulumi up` CLI reference, Pulumi Python SDK API Reference
- **Owns:** Docs (hand-written pages); Eng/Product (generated content — CLI command docs are auto-generated and merge without docs review per the CODEOWNERS carve-outs)
- **Contributes:** Eng/Product
- **Consumes:** Practitioners who know what they're looking for

### Marketing guides (pulumi.com/guides)

**Definition:** End-to-end, outcome-framed patterns for a complete real-world scenario ("Build a Cloud Landing Zone," "HIPAA-Compliant Infrastructure on AWS"), packaged to show what Pulumi can do — including Neo prompt libraries. Part sales asset, part architecture pattern; the page describes them as "end-to-end blueprints for real cloud patterns."

- **Lives at:** [pulumi.com/guides](https://www.pulumi.com/guides/) — **not in this repository**; published from a separate marketing pipeline
- **Owns:** Marketing
- **Contributes:** DevRel, Eng/Product (technical validation)
- **Consumes:** Evaluators and buyers scoping a solution

> This type shares the name "Guides" with the docs how-to sections above. Both keep the name for now — see [Open questions](#open-questions-and-naming-conflicts).

### Topics 

**Definition:** Educational pages or topic clusters answering a definitional search query ("What is GitOps?"). Product-light, concept-heavy.

- **Lives at:** `content/what-is/` (section title: "Cloud Engineering Concepts Explained")
- **Owns:** Marketing
- **Contributes:** Docs, DevRel
- **Consumes:** Evaluators early in research

### Blog posts

**Definition:** Point-in-time announcements, engineering stories, and opinion. Blog posts are **historical records**: per `AGENTS.md`, they are not kept current — broken links get routed around, and revisions are the exception (stamped with `updated:`).

- **Lives at:** `content/blog/`
- **Owns:** Marketing. Individual blog authors own the accuracy of their content at time of publishing. Marketing owns the rest, including design, editorial, and amplification.
- **Contributes:** Everyone — Eng/Product, DevRel, Docs, Marketing, guest authors
- **Consumes:** Community, customers, news readers

### Case studies

**Definition:** Customer success narratives — who they are, what problem they had, how Pulumi solved it, with quotes and metrics.

- **Lives at:** `content/case-studies/`
- **Owns:** Marketing
- **Contributes:** Sales/CS (customer relationships), DevRel
- **Consumes:** Buyers seeking social proof

### Product and campaign pages

**Definition:** Template-driven pages that sell — product pages, solution pages, pricing, comparison/topic landing pages, and ad-campaign landing pages.

- **Lives at:** `content/product/`, `content/solutions/`, `content/topics/`, `content/pricing/`, `content/why-pulumi/`, `content/gads/`, and ~20 similar campaign directories
- **Owns:** Marketing
- **Contributes:** Eng/Product (feature accuracy), Docs (technical review)
- **Consumes:** Evaluators and buyers

### Events and workshops

**Definition:** Registration and recap pages for webinars, workshops, and conference presence.

- **Lives at:** `content/events/`
- **Owns:** Marketing and DevRel, jointly (Marketing owns promotion and pages; DevRel owns technical content delivered)
- **Consumes:** Community members and prospects

### Releases and Changelog

**Definition:** Dated records of what shipped — one changelog entry per change, plus launch pages.

- **Lives at:** `content/releases/`, `content/releases/changelog/`
- **Owns:** Marketing
- **Contributes:** Eng/Product, Docs, DevRel
- **Consumes:** Existing and prospective users tracking product evolution

### Templates 

**Definition:** Starter kits for generating new Pulumi projects with `pulumi new`.

- **Lives at:** `content/templates/` (sourced from https://github.com/pulumi/templates); includes both starter and architecture templates.
- **Owns:** Marketing
- **Contributes:** Eng/Product, DevRel
- **Consumes:** Practitioners bootstrapping new projects

### Example programs

**Definition:** Testable programs designed for embedding into docs and tutorials.

- **Lives at:** `static/programs/`, tested via `scripts/programs/test.sh`
- **Owns:** Docs
- **Contributes:** Eng/Product, Marketing, DevRel
- **Consumes:** Practitioners engaging with the docs. Every docs page that embeds an example should ideally use one of these programs.

## Summary table

| Type | One-line definition | Lives at | Owns | Contributes | Consumes |
|---|---|---|---|---|---|
| Conceptual docs | Explains how Pulumi works and why | `content/docs/*/concepts/` | Docs | Eng/Product, DevRel | Practitioners |
| Guides | Walkthroughs designed for understanding and using Pulumi | `content/docs/*/guides/` | Docs | Eng/Product, DevRel, community | Practitioners |
| Tutorials | Sequenced hands-on learning | `content/tutorials/` | Marketing | Docs, Eng/Product | Newcomers, learners |
| Reference | Exhaustive lookup material | `content/docs/reference/`, generated CLI docs | Docs + Eng/Product | Eng/Product | Practitioners |
| Topics | Adjacent and industry-relevant content | `content/what-is/` | Marketing | Docs, DevRel | Learners, evaluators |
| Blog posts | Point-in-time posts; historical | `content/blog/` | Marketing | Everyone | Community |
| Case studies | Customer success stories | `content/case-studies/` | Marketing | Sales/CS, DevRel | Buyers |
| Product/campaign pages | Pages that sell | `content/product/`, `solutions/`, `gads/`, … | Marketing | Eng/Product, Docs | Evaluators, buyers |
| Events & workshops | Registration/recap pages | `content/events/` | Marketing + DevRel | — | Community, prospects |
| Releases & changelog | Dated record of what shipped | `content/releases/` | Marketing | Eng/Product, Docs | Existing and prospective users |
| Templates | Runnable starting points | `content/templates/` | Marketing | Eng/Product, DevRel | Practitioners |
| Example programs | Tested, embeddable code | `static/programs/` | Docs | Eng/Product, DevRel | Practitioners |

## Open questions and naming conflicts

This document records these as unresolved; it does not itself rename anything or move ownership.

1. **The "Guides" name collision.** Docs nav sections and the marketing hub at pulumi.com/guides both go by "Guides," and both keep the name for now. This is a real conflict we should resolve: two different content types — task-scoped how-to docs and end-to-end sellable blueprints — answer to the same word, which muddies nav, search, and cross-team conversation. Possible resolutions:
   - Marketing renames its hub (its content self-describes as "blueprints"), releasing "guides" to docs. This may not be palatable to the marketing side.
   - Docs renames its sections — to "How-tos," "How-to guides," "Tasks," or similar. A label-only change: URLs keep the `/guides/` slug, so no aliases or redirects would be needed.

   No decision is made here; until one is, use the qualified terms from this document ("how-to guides" for the docs type, "marketing guides" for the hub) when the bare word would be ambiguous.
1. **Tutorials ownership.** pulumi.com/tutorials is Marketing/DevRel-owned today, but it's learner-facing technical content served from this repo alongside the docs — and the (commented-out) CODEOWNERS mapping assigns it to `@pulumi/docs`. Should tutorials roll into Docs ownership? Open question.
1. **Docs: give `content/docs/iac/guides/` a landing page.** IaC holds the same how-to content as the other product sections but has no `_index.md`, so the type is invisible in the IaC nav. Add one — titled "Guides" to match its siblings for now; it inherits whatever name the collision resolution lands on.
1. **Reserve "tutorials" for `content/tutorials/`.** Don't introduce "tutorial" sections inside `/docs/` (none exist today — keep it that way). Note that `/learn` is an alias of `/tutorials`, and `content/learn` does not exist as a directory.

## Known gaps

- **CODEOWNERS is entirely commented out** (`.github/CODEOWNERS`), so no ownership is enforced — and the commented-out mapping doesn't fully match reality anyway (it assigns `content/tutorials/` to `@pulumi/docs`, while actual ownership sits with Marketing/DevRel).
- **Stale `content/learn` reference:** the docs-review criteria (`.claude/commands/docs-review/references/docs.md`) scope includes `content/learn`, which doesn't exist.
- **Untyped campaign directories:** ~20 one-off landing directories under `content/` (`gads/`, `cjs26/`, `kubecon/`, `reinvent/`, …) have no declared type or owner beyond falling into the "website" review domain. They are treated here as product/campaign pages.
