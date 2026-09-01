# TAXONOMY.md — Content types for pulumi.com

This document defines the canonical vocabulary for the kinds of content published on pulumi.com, and states who **owns**, who **contributes to**, and who **consumes** each type. Use these terms in nav headings, page titles, planning docs, and cross-team conversation.

## Why this document exists

The word **"guides"** currently refers to five different things:

1. Docs uses **"Guides"** as a second-level nav heading inside several product sections (`content/docs/esc/guides/`, `content/docs/deployments/guides/`, `content/docs/idp/guides/` all carry `title: Guides`; `content/docs/iac/guides/` holds the same kind of content but has no landing page of its own).
2. Marketing publishes **pulumi.com/guides** — "End-to-end blueprints for real cloud patterns" plus a library of Neo prompts. That page is **not** served from this repository.
3. Marketing also publishes the tutorials at **pulumi.com/learn**, which are occasionally referred to as guides.
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
- **Contributes:** Eng/Product (feature knowledge), Community Eng
- **Consumes:** Practitioners building an understanding of how Pulumi works

### Guides

**Definition:** Walkthroughs that acquaint the reader with a product or feature. Sometimes that takes the form of a particular task ("build a component"), sometimes not ("organizing stacks," "composing environments"); best practices — advice on how to use the product well — also fall under this definition. What distinguishes a guide is how *core* it is to the product: if the thing being discussed is fundamental to Pulumi — something you need to know in order to use it — it's a guide; if it's about doing something *with* Pulumi that isn't core to the product (spinning up a specialized bit of infra, or integrating a third-party service the product has no direct integration with), it belongs elsewhere. Integrations the product supports directly — the VCS integrations, for example — are core, and their docs belong in guides. In short: guides in the docs are about *understanding* and *using* the product; tutorials are about *doing stuff* with the product. In the [Diátaxis](https://diataxis.fr/) sense, a guide here can take the form of either a "how-to guide" or an "explanation" — both fit the needs of these sections.

- **Lives at:** `content/docs/iac/guides/`, `content/docs/esc/guides/`, `content/docs/deployments/guides/`, `content/docs/idp/guides/`
- **Examples:** [Migrating from Terraform](https://www.pulumi.com/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/), ESC + GitHub Actions integration guides
- **Owns:** Docs
- **Contributes:** Eng/Product, Community Eng, community
- **Consumes:** Practitioners new to Pulumi or seeking help with (or a better understanding of) a particular product or feature

### Tutorials

**Definition:** Task-oriented, sequenced, hands-on lessons. The reader follows along end to end and comes out having *built something* and *learned Pulumi*. Tutorials sometimes have time estimates and are occasionally grouped into collections and multi-part modules. 

- **Lives at:** [pulumi.com/learn/tutorials](https://www.pulumi.com/learn/tutorials/) — **not in this repository**; published from pulumi/marketing-web (`apps/www/src/content/tutorials/`) — and `content/docs/*/get-started`
- **Examples:** IaC Get Started, Deployments Get Started, ESC Get Started, Pulumi Fundamentals (3-part module), "Importing AWS Infrastructure"
- **Owns:** Marketing
- **Contributes:** Docs, Eng/Product
- **Consumes:** Newcomers and learners

**Getting Started** (`content/docs/{iac,deployments,esc}/get-started/`) are the only tutorials that currently live within the docs. They're tutorials because they're end-to-end onboarding paths — hyperfocused on getting up and running with one aspect of Pulumi — and because they're owned, maintained, and measured by Marketing. We'll aim to call them the Getting Started *tutorials* (that's what they are in the Diátaxis sense), even though the word "guides" has stuck to them historically. Discovery and IDP don't currently have one, but probably should.

### Reference

**Definition:** Lookup material — exhaustive, structured, factual. Optimized for finding one precise answer, not for reading front to back.

- **Lives at:** `content/docs/reference/`, generated CLI docs (`content/docs/iac/cli/commands/`, `content/docs/esc/cli/commands/`), SDK/API reference, and the [Pulumi Registry](https://www.pulumi.com/registry/) (published from its own pipeline)
- **Examples:** `pulumi up` CLI reference, Pulumi Python SDK API Reference
- **Owns:** Docs (hand-written pages); Eng/Product (generated content — CLI command docs are auto-generated; the CODEOWNERS carve-out that would let them merge without docs review is currently commented out, like the rest of that file)
- **Contributes:** Eng/Product
- **Consumes:** Practitioners who know what they're looking for

### Marketing guides (pulumi.com/guides)

**Definition:** End-to-end, outcome-framed patterns for a complete real-world scenario ("Build a Cloud Landing Zone," "HIPAA-Compliant Infrastructure on AWS"), packaged to show what Pulumi can do — including Neo prompt libraries. Part sales asset, part architecture pattern; the page describes them as "end-to-end blueprints for real cloud patterns."

- **Lives at:** [pulumi.com/guides](https://www.pulumi.com/guides/) — **not in this repository**; published from a separate marketing pipeline
- **Owns:** Marketing
- **Contributes:** Community Eng, Eng/Product (technical validation)
- **Consumes:** Evaluators and buyers scoping a solution

> **Status: effectively end-of-life.** This content is being folded selectively into [Tutorials](#tutorials). The header and footer links were removed when Learn launched, so the pages are still served but unlinked. Going forward, "Guides" refers only to the docs guides above — see [Naming decisions](#naming-decisions-and-open-items).

### Topics 

**Definition:** Educational pages or topic clusters answering a definitional search query ("What is GitOps?"). Product-light, concept-heavy.

- **Lives at:** `content/what-is/` (section title: "Cloud Engineering Concepts Explained")
- **Owns:** Marketing
- **Contributes:** Docs, Community Eng
- **Consumes:** Evaluators early in research

### Blog posts

**Definition:** Point-in-time announcements, engineering stories, and opinion. Blog posts are **historical records**: per `AGENTS.md`, they are not kept current — broken links get routed around, and revisions are the exception (stamped with `updated:`).

- **Lives at:** `content/blog/`
- **Owns:** Marketing. Individual blog authors own the accuracy of their content at time of publishing. Marketing owns the rest, including design, editorial, and amplification.
- **Contributes:** Everyone — Eng/Product, Community Eng, Docs, Marketing, guest authors
- **Consumes:** Community, customers, news readers

### Case studies

**Definition:** Customer success narratives — who they are, what problem they had, how Pulumi solved it, with quotes and metrics.

- **Lives at:** `content/case-studies/`
- **Owns:** Marketing
- **Contributes:** Sales/CS (customer relationships), Community Eng
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
- **Owns:** Marketing and Community Eng, jointly (Marketing owns promotion and pages; Community Eng owns technical content delivered)
- **Consumes:** Community members and prospects

### Releases and Changelog

**Definition:** Dated records of what shipped — one changelog entry per change, plus launch pages.

- **Lives at:** `content/releases/`, `content/releases/changelog/`
- **Owns:** Marketing
- **Contributes:** Eng/Product, Docs, Community Eng
- **Consumes:** Existing and prospective users tracking product evolution

### Templates 

**Definition:** Starter kits for generating new Pulumi projects with `pulumi new`.

- **Lives at:** [pulumi.com/learn/templates](https://www.pulumi.com/learn/templates/) — **not in this repository**; published from pulumi/marketing-web, which syncs the starters from https://github.com/pulumi/templates and authors the architecture-template pages alongside them.
- **Owns:** Marketing
- **Contributes:** Eng/Product, Community Eng
- **Consumes:** Practitioners bootstrapping new projects

### Example programs

**Definition:** Testable programs designed for embedding into docs pages.

- **Lives at:** `static/programs/`, tested via `scripts/programs/test.sh`
- **Owns:** Docs
- **Contributes:** Eng/Product, Marketing, Community Eng
- **Consumes:** Practitioners engaging with the docs. Every docs page that embeds an example should ideally use one of these programs.

## Summary table

| Type | One-line definition | Lives at | Owns | Contributes | Consumes |
|---|---|---|---|---|---|
| Conceptual docs | Explains how Pulumi works and why | `content/docs/*/concepts/` | Docs | Eng/Product, Community Eng | Practitioners |
| Guides | Walkthroughs designed for understanding and using Pulumi | `content/docs/*/guides/` | Docs | Eng/Product, Community Eng, community | Practitioners |
| Tutorials | Sequenced hands-on learning | pulumi/marketing-web → `/learn/tutorials/` | Marketing | Docs, Eng/Product | Newcomers, learners |
| Reference | Exhaustive lookup material | `content/docs/reference/`, generated CLI docs | Docs + Eng/Product | Eng/Product | Practitioners |
| Topics | Adjacent, industry-relevant educational content ("what is X") | `content/what-is/` | Marketing | Docs, Community Eng | Learners, evaluators |
| Blog posts | Point-in-time posts; historical | `content/blog/` | Marketing | Everyone | Community |
| Case studies | Customer success stories | `content/case-studies/` | Marketing | Sales/CS, Community Eng | Buyers |
| Product/campaign pages | Pages that sell | `content/product/`, `solutions/`, `gads/`, … | Marketing | Eng/Product, Docs | Evaluators, buyers |
| Events & workshops | Registration/recap pages | `content/events/` | Marketing + Community Eng | — | Community, prospects |
| Releases & changelog | Dated record of what shipped | `content/releases/` | Marketing | Eng/Product, Docs | Existing and prospective users |
| Templates | Runnable starting points | pulumi/marketing-web → `/learn/templates/` | Marketing | Eng/Product, Community Eng | Practitioners |
| Example programs | Tested, embeddable code | `static/programs/` | Docs | Eng/Product, Community Eng | Practitioners |

## Naming decisions and open items

The "guides" collision described at the top of this document has been resolved as follows (agreed in [PR #20803](https://github.com/pulumi/docs/pull/20803)):

1. **"Guides" refers *only* to the docs guides** — the ones that live in the docs, generally underneath a given product or feature. These are owned by the Docs team, and each one, in the [Diátaxis](https://diataxis.fr/) sense, can take the form of either a "how-to guide" or an "explanation." These are the *only* things we'll refer to as Guides going forward.
1. **"Tutorials" refers to either:**
   - The things we currently call "the Getting Started guides" (`content/docs/*/get-started/`). We'll try to call these the Getting Started *tutorials* going forward — that's what they are in the Diátaxis sense.
   - The things that live at [pulumi.com/learn/tutorials](https://www.pulumi.com/learn/tutorials/). The content at pulumi.com/guides is being folded selectively into these.
1. **Tutorials are Marketing-owned** (specifically Technical Content Marketing), with contribution from everyone welcome.
1. **The hub at `/learn` has shipped.** It pulls together tutorials, templates, community examples, and a glossary, alongside blog posts categorized [as tutorials](https://www.pulumi.com/blog/category/tutorials/), series, workshops, and Academy programs. Like the Registry and pulumi.com/guides, it is served by a separate web app (pulumi/marketing-web) rather than this repo; `infrastructure/index.ts` proxies `/learn*` to it.

Open items:

1. **Give `content/docs/iac/guides/` a landing page.** IaC holds the same guide content as the other product sections but has no `_index.md`, so the type is invisible in the IaC nav. Add an introduction page, titled "Guides," to match its siblings.
1. **Reserve "tutorials" for the two things above.** Don't introduce other "tutorial" sections inside `/docs/`, and don't recreate `content/tutorials/` here — new tutorials go to pulumi/marketing-web.
1. **Bring team metadata current.** The team-management repo may need tweaks (at least on the Marketing side) to reflect the ownership described here.

## Known gaps

- **CODEOWNERS is entirely commented out** (`.github/CODEOWNERS`), so no ownership is enforced.
- **Untyped campaign directories:** ~20 one-off landing directories under `content/` (`gads/`, `cjs26/`, `kubecon/`, `reinvent/`, …) carry no declared type in repo metadata beyond falling into the "website" review domain. They are all Marketing-owned and treated here as product/campaign pages.
