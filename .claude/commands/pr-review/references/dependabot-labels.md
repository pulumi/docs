---
user-invocable: false
description: Dependabot label taxonomy and handling
---

# Dependabot Labels

## Label Taxonomy

The `label-dependabot.yml` workflow applies these labels. There is no risk-tier
classification — dependency updates are grouped per ecosystem and arrive at low
volume, so the policy is to evaluate each PR and merge it once CI is green. The
labels below flag the only two cases that change handling.

- `dependencies` - Standard label (applied by Dependabot itself)
- `deps-security-patch` - Security vulnerability fix; prioritize
- `deps-lambda-edge-risk` - Affects Lambda@Edge bundling/runtime (webpack/bundler/AWS SDK; ESM/CommonJS and 1 MB bundle-size concerns)
- `deps-bulk-update` - 10+ dependencies in a single PR

## Handling

Default path for every Dependabot PR:

1. **Evaluate** - build and spot-check (the testing checklist lives in `pr-review:references:action-menus`).
2. **Approve + merge** once CI is green.

Two flags adjust this:

- `deps-security-patch` - prioritize over the regular cadence; evaluate and merge promptly.
- `deps-lambda-edge-risk` - before merging, verify the Lambda@Edge function size against the 1 MB compressed limit and confirm the CloudFront deployment succeeds in the testing environment. See the Infrastructure Change Review section of `BUILD-AND-DEPLOY.md`.

`deps-bulk-update` is informational: a 10+ dependency PR warrants a more careful
build/test pass and a check for hidden major versions, but is handled the same
way otherwise.
