---
user-invocable: false
description: The deploy-to-pulumi-test.io row action for infra PRs
---

# Infrastructure deployment (`--deploy N`)

A row whose risk tier is `infra` (it touches `scripts/`, `.github/workflows/`, `Makefile`, `infrastructure/`, `package.json` or `webpack.config.js` — `collect.py::risk_tier`) carries a **deploy to pulumi-test.io** action. It is a row action, not a step everyone walks through: nothing prompts for it, and a Dependabot or Renovate dependency bump is the same `infra` tier by path.

`act.py --deploy N` dispatches `testing-build-and-deploy.yml` at the PR's head branch (`POST actions/workflows/testing-build-and-deploy.yml/dispatches`). The run appears under the workflow's runs; the site rebuilds at https://pulumi-test.io in about ten minutes.

What to check once it is up: open the console (F12) for Lambda@Edge errors, run a search, click through navigation, and for a `deps-lambda-edge-risk` PR confirm the bundle is under the 1 MB limit (see `pr-review:references:dependabot-labels`). **The next merge to master resets pulumi-test.io**, so deploy, check, then stamp.

The Sentinel's G4 gate (infra evidence) wants a successful staging deploy at the head SHA: either the `staging/pulumi-test-io` commit status from a trusted writer, or a successful "Build and deploy testing" run at that SHA. `staging-deploy-auto.yml` dispatches one automatically for any same-repo PR touching `staging_evidence.paths`. `--deploy` is the manual retry: it dispatches the same workflow, and once that run succeeds G4 reads it (`staging-status.yml`'s sweep re-scores the Sentinel within about ten minutes). Re-running a failed run from the Actions tab works the same way.
