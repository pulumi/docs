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
| 3 | `docs-review:references:docs` | `content/docs/**`, `content/tutorials/**`, `content/what-is/**` |
| 4 | `docs-review:references:website` | Any other `content/**.md` (pricing, legal, `vs/`, `why-pulumi/`, `about/`, `careers/`, etc.) |
| 5 | `docs-review:references:infra` | Two groups, same criteria. **Tooling and CI:** `.github/workflows/**`, `scripts/**` except `scripts/programs/**`, `infrastructure/**`, `Makefile` (repo root), `package.json` (repo root only), `webpack.config.js`, `webpack.*.js`. **Site build pipeline:** `layouts/**`, `assets/**`, `theme/**` (SCSS and TypeScript sources compiled into the site bundles), `static/**` except `static/programs/**` |
| 6 | `docs-review:references:shared-criteria` only | Anything else (`data/`, `styles/`, `archetypes/`, repo-root dotfiles, etc.). Triage labels such a PR `domain:other` |

`docs-review:references:shared-criteria` applies to every file regardless of domain.

**Every changed file routes somewhere.** Rules 1–5 name a criteria file; rule 6 is the catch-all, and files landing there get `docs-review:references:shared-criteria` and nothing more. When *no* file in a PR matches rules 1–5, `triage-classify.py` labels the PR `domain:other` so that an unlabeled PR always means triage didn't run, never that it ran and found nothing to say. `domain:other` is not itself a review lane — it is the label form of rule 6.

**Ordering matters.** A per-program `package.json` under `static/programs/<name>/package.json` is programs, not infra. `scripts/programs/**` (e.g., `scripts/programs/ignore.txt`) is programs tooling, not site infra. Only the repo-root `package.json` and `Makefile` count as infra. Rule 5's two groups are one domain, not two: `theme/src/scss/` and `.github/workflows/` both review under `docs-review:references:infra`.
