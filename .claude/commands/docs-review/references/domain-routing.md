---
description: Canonical path-precedence rules that route each changed file to exactly one review domain.
user-invocable: false
---

# Domain Routing

Each changed file routes to **exactly one** domain by path. Apply the rules in order; a file is classified under the first rule that matches, and subsequent rules do not re-apply.

| Order | Domain | Applies when the file path matches |
|---|---|---|
| 1 | `programs.md` | `static/programs/**` (includes every nested file in a program directory: `Pulumi.yaml`, `package.json`, `requirements.txt`, source files) |
| 2 | `blog.md` | `content/blog/**`, `content/case-studies/**` |
| 3 | `docs.md` | `content/docs/**`, `content/learn/**`, `content/tutorials/**`, `content/what-is/**` |
| 4 | `infra.md` | `.github/workflows/**`, `scripts/**` except `scripts/programs/**`, `infrastructure/**`, `Makefile` (repo root), `package.json` (repo root only), `webpack.config.js`, `webpack.*.js` |
| 5 | `shared-criteria.md` only | Anything else (`layouts/`, `assets/`, `data/`, etc.) |

`shared-criteria.md` applies to every file regardless of domain. Mixed PRs run each file under its appropriate domain and merge findings into one output object.

**Ordering matters.** A per-program `package.json` under `static/programs/<name>/package.json` is programs, not infra. `scripts/programs/**` (e.g., `scripts/programs/ignore.txt`) is programs tooling, not site infra. Only the repo-root `package.json` and `Makefile` count as infra.
