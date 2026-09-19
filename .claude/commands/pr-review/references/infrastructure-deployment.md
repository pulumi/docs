---
user-invocable: false
description: The deploy-to-pulumi-test.io row action for infra PRs
---

# Infrastructure deployment (`--deploy N`)

A row whose risk tier is `infra` (it touches `scripts/`, `.github/workflows/`, `Makefile`, `infrastructure/`, `package.json` or `webpack.config.js` — `collect.py::risk_tier`) carries a **deploy to pulumi-test.io** action. It is a row action, not a step everyone walks through: nothing prompts for it, and a Dependabot or Renovate dependency bump is the same `infra` tier by path.

`act.py --deploy N` dispatches `testing-build-and-deploy.yml` at the PR's head branch (`POST actions/workflows/testing-build-and-deploy.yml/dispatches`). The run appears under the workflow's runs; the site rebuilds at https://pulumi-test.io in about ten minutes.

What to check once it is up: open the console (F12) for Lambda@Edge errors, run a search, click through navigation, and for a `deps-lambda-edge-risk` PR confirm the bundle is under the 1 MB limit (see `pr-review:references:dependabot-labels`). **The next merge to master resets pulumi-test.io**, so deploy, check, then stamp.

The Sentinel's G4 gate (infra evidence) is separate: it wants the `staging/pulumi-test-io` commit status green at the head SHA, posted by a trusted writer. Two lanes produce it — `staging-deploy-auto.yml` dispatches one automatically for any PR touching `staging_evidence.paths`, and `/deploy-staging` is the manual retry. `--deploy` writes no status at all, so it is the quicker look and never satisfies G4.
