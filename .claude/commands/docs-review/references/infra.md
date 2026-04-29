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

Infra files aren't prose; the job is flagging risks for human review, not catching style nits. Findings render in ⚠️ Low-confidence by default; see `output-format.md` §Bucket rules for the two 🚨 exceptions (secrets, clearly-broken state).

---

## Scope

- Diff-only. Whole-file reads happen only when the diff context isn't enough to judge a risky change.
- Pre-existing issues are **off**.
- Fact-check is **not** invoked.

## Criteria

`shared-criteria.md` applies alongside the risk axes below (mostly relevant here for link checking in comments and docs). Pair findings with a pointer to the relevant `BUILD-AND-DEPLOY.md` section.

### Lambda@Edge bundling

- **ESM vs CommonJS.** ESM-only packages (e.g., `url-pattern` >= 7.0.0) break Lambda@Edge if webpack is misconfigured. Flag any dependency bump to a package that went ESM-only in a recent major version.
- **`output.module` / `experiments.outputModule`.** Changes to webpack's output mode can break Lambda@Edge bundling silently. Flag any change to these fields.
- **Dynamic imports.** `import()` expressions may not work in the Lambda@Edge runtime. Flag when added to `infrastructure/**` source.
- **Bundle size.** Lambda@Edge has strict limits (1 MB compressed, 50 MB uncompressed). Flag dependency additions to `infrastructure/package.json` that are likely to push the bundle past those limits.

### CloudFront behavior

- **Redirect logic.** Changes to redirect handling may break existing URLs. Flag any change to `infrastructure/` that affects the URL rewrite path.
- **Cache behavior.** Modified cache settings require an invalidation after deployment. Flag so the reviewer remembers to include one.
- **Lambda associations.** Changes to CloudFront-Lambda event types must be coordinated with the Lambda code. Flag when one changes without the other.

### Runtime dependencies

Dependencies that execute in the browser or Lambda@Edge runtime carry extra risk. Flag when any of these are bumped:

- **Content parsing:** `marked`, `markdown-it`, `js-yaml`, `cheerio`, `gray-matter`
- **Search:** `@algolia/*`, `algoliasearch`, `search-insights`
- **Web components:** `@stencil/*`, `swiper`
- **AWS SDK:** `@aws-sdk/*` (Lambda@Edge risk)
- **Browser APIs:** `clipboard-polyfill`

See `BUILD-AND-DEPLOY.md` §Dependency risk tiers for the canonical classification.

### Workflow trigger changes

Changes that alter *when* CI runs produce large blast radii. Flag any change to:

- A workflow's `on:` block (especially adding/removing events like `push`, `pull_request`, `workflow_run`)
- `paths:` / `paths-ignore:` filters that change which changes kick off CI
- `concurrency:` keys -- loss of `cancel-in-progress: true` can create runaway job accumulation
- Cron schedules -- a typo silently disables the scheduled job

### Secret handling

- **No secrets in diff.** Any hardcoded credential, API key, token, or private URL in the diff is 🚨 immediately. `gh pr view --json` output is public; leaked secrets must be rotated.
- **No secrets in example commands / logs.** Even illustrative strings (`"api-key-12345"`) can be confused for real values if they pattern-match.
- **`secrets.*` references in workflows.** Flag when a secret is newly referenced in a workflow output, comment step, or debug print -- GitHub masks secrets in logs by default but comments and artifacts are not protected.

### Documentation drift

If the PR changes any of the above without updating `BUILD-AND-DEPLOY.md`, flag the omission. Examples:

- New `make` target but §Makefile Targets not updated
- Changed deployment workflow but §Production Deployment not updated
- New environment variable required by a script but §Environment Setup silent on it

Reference (don't duplicate): `BUILD-AND-DEPLOY.md` §Infrastructure Change Review for the canonical risk catalog; §Dependency risk tiers for the runtime/build/dev split.

## Do not flag

- **Style nits in working YAML.** Indentation, blank-line spacing, ordering of top-level keys -- workflows follow GitHub Actions conventions, not a Pulumi style guide.
- **Refactors to working scripts.** "You could consolidate these three steps" is editorial. Flag when a script is broken; don't rewrite it for aesthetics.
- **"Missing tests" on infra-only PRs.** Infra changes are tested in staging, not in unit tests.
- **Dependency-version aesthetic choices.** Whether a pin reads `^1.2.3` or `~1.2.3` is a Dependabot/package-manager concern, not a review finding.
- **Hardcoded values that are meant to be constants.** `timeout-minutes: 15` is a choice, not an error. Only flag when the value is clearly wrong (e.g., `timeout-minutes: 5` on a job known to take longer).
