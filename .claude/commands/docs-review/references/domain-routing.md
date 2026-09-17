---
description: Canonical path-precedence rules that route each changed file to exactly one review domain.
user-invocable: false
---

# Domain Routing

Each changed file routes to **exactly one** domain by path. Apply the rules in order; a file is classified under the first rule that matches, and subsequent rules do not re-apply.

| Order | Domain | Applies when the file path matches |
|---|---|---|
| 1 | `docs-review:references:programs` | `static/programs/**` (includes every nested file in a program directory: `Pulumi.yaml`, `package.json`, `requirements.txt`, source files) and `scripts/programs/**` |
| 2 | `docs-review:references:blog` | `content/blog/**`, `content/case-studies/**` |
| 3 | `docs-review:references:docs` | `content/docs/**`, `content/what-is/**` |
| 4 | `docs-review:references:website` | Any other `content/**.md` (pricing, legal, `vs/`, `why-pulumi/`, `about/`, `careers/`, etc.) |
| 5 | `docs-review:references:infra` | Two groups, same criteria, **two different labels**. **Tooling and CI** (label `domain:infra`): `.github/workflows/**`, `scripts/**` except `scripts/programs/**`, `infrastructure/**`, `Makefile` (repo root), `package.json` (repo root only), `webpack.config.js`, `webpack.*.js`. **Site rendering layer** (label `domain:frontend`): `layouts/**`, `assets/**`, `theme/**` (SCSS and TypeScript sources compiled into the site bundles), `static/**` except `static/programs/**` |
| 6 | `docs-review:references:shared-criteria` only | Anything else (`styles/`, `archetypes/`, `.claude/`, non-workflow `.github/` files, repo-root dotfiles, generated `data/` files, etc.). Triage labels such a PR `domain:other` |

`docs-review:references:shared-criteria` applies to every file regardless of domain.

**Content data files route with the content they serve.** A short list of `data/` files is content, not plumbing, and classifies accordingly (the authoritative map is `CONTENT_DATA_EXACT` / `CONTENT_DATA_PREFIXES` in `triage-classify.py`): the docs nav and reference tables (`data/docs_menu_sections.yml`, `data/docs_nav.yaml`, `data/resource_options.yaml`, `data/what_is_sections.yml`, `data/glossary.toml`) are rule 3; the blog taxonomies, homepage curation, author bios, and case-study industries (`data/blog_*.yaml`, `data/blog_series.yml`, `data/team/**`, `data/case_study_industries.yaml`) are rule 2; the pricing matrix and site-chrome data (`data/pulumi_pricing.yaml`, `data/announcements.yml`, `data/header_nav.yaml`, `data/footer.yml`, `data/awards.toml`, `data/newsroom.toml`, `data/partners/**`) are rule 4; the hero-animation sources and color tokens (`data/hero_agent_loop*.yaml`, `data/colors/**`) are rule 5's frontend group. Every other `data/` file (generated JSON, package schemas, version tables) is rule 6.

**Every changed file routes somewhere.** Rules 1–5 name a criteria file; rule 6 is the catch-all, and files landing there get `docs-review:references:shared-criteria` and nothing more. When *no* file in a PR matches rules 1–5, `triage-classify.py` labels the PR `domain:other` so that an unlabeled PR always means triage didn't run, never that it ran and found nothing to say. `domain:other` is not itself a review lane — it is the label form of rule 6.

**Ordering matters.** A per-program `package.json` under `static/programs/<name>/package.json` is programs, not infra. `scripts/programs/**` (e.g., `scripts/programs/ignore.txt`) is programs tooling, not site infra. Only the repo-root `package.json` and `Makefile` count as infra.

**Rule 5 is one review lens and two labels.** `theme/src/scss/` and `.github/workflows/` both review under `docs-review:references:infra` — Hugo correctness, the dark-mode pass, fingerprinted images, and build-pipeline criteria are the same lens either way. The label split exists for the v3 approval matrix (`.github/review-routing.yml`), not for review criteria: `domain:infra` is the build and deploy pipeline, approved by the tools team with a required staging run; `domain:frontend` is how the site looks, approved by marketing with no staging run. Changing the lens for `domain:frontend` files would mean reviewing a Hugo partial for voice and tone while nobody checks the template, so the lens stays infra.
