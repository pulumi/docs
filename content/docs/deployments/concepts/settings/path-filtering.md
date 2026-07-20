---
title_tag: "Path Filtering | Pulumi Deployments"
meta_desc: Use path filters to trigger a Pulumi Deployment only when a push changes files you care about, especially in a monorepo
title: "Path Filtering"
h1: "Path Filtering"
menu:
  deployments:
    name: Path Filtering
    parent: deployments-concepts-settings
    identifier: deployments-concepts-settings-path-filtering
    weight: 20
---

When using a [VCS integration](/docs/integrations/version-control/) and push-to-deploy, you may want a deployment to trigger only when a push changes files you care about. You can do this with path filters. This is especially useful for monorepos, where a single repository holds multiple Pulumi programs and you want each stack to deploy only when its own files change.

## Writing filters

Each filter is a glob pattern matched against the full path of every file changed by a push, relative to the repository root. A pattern must match the *entire* path:

- `infrastructure/Pulumi.dev.yaml` matches only that one file.
- `infrastructure/**` matches every file anywhere under the `infrastructure/` directory.

A filter is an **include filter** by default. Prefix it with `!` to make it an **exclude filter**:

- `infrastructure/**` — include changes under `infrastructure/`.
- `!infrastructure/docs/**` — exclude changes under `infrastructure/docs/`.

## How filters are evaluated

A push triggers a deployment when **at least one changed file matches the filters**. An individual file matches when both of these are true:

1. It matches at least one include filter (or no include filters are configured), and
1. It does not match any exclude filter.

A few consequences worth knowing:

- **No filters:** every push triggers a deployment.
- **Only exclude filters:** every file is included unless an exclude filter matches it.
- **Exclude always wins.** If a file matches an exclude filter, it is excluded even when it also matches an include filter. The order in which you list filters does not matter.

{{% notes type="warning" %}}
Path filters do **not** behave like a `.gitignore` file. In `.gitignore`, a later negated pattern can re-include a path that an earlier pattern excluded. Pulumi path filters have no equivalent: once a file matches an exclude filter, no include filter can bring it back.

For example, given these filters:

```
!foo/**
foo/bar/**
```

a change to `foo/bar/main.ts` does **not** trigger a deployment — it matches the `!foo/**` exclude filter, and the `foo/bar/**` include filter cannot override that. To deploy on changes under `foo/bar/` while ignoring the rest of `foo/`, exclude only the specific subdirectories you want to skip (for example `!foo/baz/**`) rather than excluding all of `foo/`.
{{% /notes %}}
