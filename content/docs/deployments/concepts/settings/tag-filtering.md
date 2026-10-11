---
title_tag: "Tag Filtering | Pulumi Deployments"
meta_desc: Use tag filters to trigger a Pulumi Deployment when a matching git tag is pushed, for release-based workflows
title: "Tag Filtering"
h1: "Tag Filtering"
menu:
  deployments:
    name: Tag Filtering
    parent: deployments-concepts-settings
    identifier: deployments-concepts-settings-tag-filtering
    weight: 30
---

When using a [VCS integration](/docs/integrations/version-control/) and push-to-deploy, you can trigger a deployment when a git tag is pushed instead of (or in addition to) a branch push. This is useful for release-based workflows where you deploy only when you cut a release — for example, pushing a `v1.2.0` tag — rather than on every commit. Tag triggers are supported across all version control integrations (GitHub, GitLab, Bitbucket, Azure DevOps, and Custom VCS).

Tag triggers are controlled by two deployment settings on your VCS configuration:

- **`deployTags`** — a boolean that enables deploying when a matching tag is pushed.
- **`tagFilters`** — a list of glob patterns that determine which tag names qualify. This is analogous to [path filters](/docs/deployments/concepts/settings/path-filtering/), except the patterns are matched against the **tag name** rather than changed file paths.

## Writing filters

Each filter is a glob pattern matched against the full tag name. A pattern must match the *entire* tag name:

- `v1.0.0` matches only that exact tag.
- `v*` matches every tag beginning with `v`, such as `v1.0.0` and `v2.3.1`.

A filter is an **include filter** by default. Prefix it with `!` to make it an **exclude filter**:

- `v*` — include tags beginning with `v`.
- `!*-rc*` — exclude release candidates such as `v1.2.0-rc1`.

## How filters are evaluated

The same model as path filters applies, evaluated against the pushed tag name:

- **`deployTags` disabled:** tag pushes never trigger a deployment, regardless of filters.
- **No filters (`deployTags` enabled):** every tag push triggers a deployment.
- **Only exclude filters:** every tag triggers a deployment unless an exclude filter matches it.
- **Exclude always wins.** If a tag matches an exclude filter, it is excluded even when it also matches an include filter. The order in which you list filters does not matter.

{{% notes type="warning" %}}
Like path filters, tag filters do **not** behave like a `.gitignore` file: once a tag matches an exclude filter, no include filter can bring it back. To deploy on a subset of tags while ignoring others, prefer narrow include patterns over broad excludes.
{{% /notes %}}

Deleting a tag never triggers a deployment.

When a tag push triggers a deployment, Pulumi sets the `PULUMI_CI_TAG_NAME` environment variable to the tag name (for example, `v1.2.0`), which your pre-run commands or Pulumi program can read — for instance, to stamp the release version onto your resources.

{{% notes type="info" %}}
GitLab integrations created before this feature did not subscribe to tag push events. To use tag triggers with one, enable **Tag push events** on the existing GitLab group webhook — there's no need to re-create the integration. See the [GitLab integration docs](/docs/integrations/version-control/gitlab/#push-to-deploy) for details. This caveat applies only to GitLab; other providers require no action.
{{% /notes %}}
