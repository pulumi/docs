---
user-invocable: false
description: Dependabot label taxonomy and handling
---

# Dependabot Labels

## Label Taxonomy

The `label-dependabot.yml` workflow applies these labels. There is no risk-tier
classification — dependency updates are grouped per ecosystem, so the policy is
to evaluate each PR and merge it once CI is green. The labels below flag the
cases that change handling.

- `dependencies` - Standard label (applied by Dependabot itself)
- `deps-security-patch` - Genuine security fix; prioritize
- `deps-lambda-edge-risk` - Affects Lambda@Edge bundling/runtime (bundlers, Pulumi SDK, AWS SDK; ESM/CommonJS and 1 MB bundle-size concerns)
- `deps-bulk-update` - 5 or more dependencies in a single PR

All three are computed from `dependabot/fetch-metadata` outputs, not from the PR
body, so they can be trusted rather than re-derived. That matters because body
parsing got two of them badly wrong until 2026-09:

- `deps-security-patch` fired on almost every PR. The test was a `security`
  substring match, and Dependabot's standard footer contains that word on every
  single-dependency PR. 207 PRs in this repo match the boilerplate; 52 reference
  a real advisory.
- `deps-bulk-update` and `deps-lambda-edge-risk` never fired on **grouped** PRs,
  because the extractor looked for `Bumps [name]` and grouped bodies use a
  markdown table plus ``Updates `name` from x to y``. Grouped PRs are the only
  ones that can be bulk. PR #21285 bumped 7 packages including `webpack` and got
  neither label.

If you are reading a Dependabot PR from before that fix, treat its labels as
unreliable in both directions.

## Handling

When the `DEPS_AUTO_MERGE` repository variable is `true`, the default path is
**nothing to do**: `label-dependabot.yml` approves the PR as `pulumi-bot` and
arms GitHub auto-merge, which waits for the required build check. A PR only
reaches a human if it carries `deps-lambda-edge-risk` or `deps-bulk-update`, and
its triage comment names the flag that held it. In that state those two labels
are merge gates, not notes.

With the variable unset, the default path for every Dependabot PR is:

1. **Evaluate** - build and spot-check (the testing checklist lives in `pr-review:references:action-menus`).
2. **Approve + merge** once CI is green.

Two flags adjust this:

- `deps-security-patch` - prioritize over the regular cadence; evaluate and merge promptly.
- `deps-lambda-edge-risk` - before merging, verify the Lambda@Edge function size against the 1 MB compressed limit and confirm the CloudFront deployment succeeds in the testing environment. See the Infrastructure Change Review section of `BUILD-AND-DEPLOY.md`.

`deps-bulk-update` blocks auto-merge when it is enabled. Either way, a PR of
that size warrants a more careful build/test pass and a check for hidden major
versions.
