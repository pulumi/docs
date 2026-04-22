---
user-invocable: false
description: Review criteria for workflows, scripts, Makefile, infrastructure code, and build/bundling configuration.
---

# Review — Infra

Applied to changes touching:

- `.github/workflows/**`
- `scripts/**`
- `infrastructure/**`
- `Makefile`
- `package.json`, `webpack.config.js`, `webpack.*.js`

Infra files aren't prose. The review's job here is **flagging risks for human review**, not catching style nits.

> **v1 status — skeleton.** Until Session 2 fills this in, fall back to the Build/Test/Infrastructure section of [`review-criteria.md`](review-criteria.md) for the actual checks.

---

## Scope

- Diff-only. Whole-file reads happen only when the diff context isn't enough to judge a risky change.
- Pre-existing issues are **off** — infra files don't carry the same "improve while you're here" expectation as prose.

## Criteria

Pending — inherits from the Build/Test/Infrastructure section of [`review-criteria.md`](review-criteria.md) until Session 2 fills this in. Key risk axes to flag:

- Lambda@Edge bundling changes (ESM/CommonJS, webpack)
- CloudFront configuration changes
- Runtime dependency bumps (marked, algolia, stencil)
- New environment variables, secrets, or permissions
- Workflow trigger changes that alter when CI runs
- Missing `BUILD-AND-DEPLOY.md` updates for any of the above

See `BUILD-AND-DEPLOY.md` "Infrastructure Change Review" and "Dependency Management" sections for the canonical risk catalog.

## Fact-check

Not invoked. Infra files don't carry the kind of factual claims that fact-check is built for.
