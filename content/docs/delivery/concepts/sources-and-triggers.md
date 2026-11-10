---
title_tag: Pulumi Delivery sources and triggers
meta_desc: Declare the repositories and upstream pipelines that make up a Pulumi Delivery release, and control which changes start a run.
title: Sources and triggers
h1: Sources and triggers
menu:
  delivery:
    name: Sources and triggers
    parent: delivery-concepts
    weight: 10
aliases: []
---

A source tells Delivery where a release's code comes from. Every member checks out a source, and the commits of all the sources in a run make up its release. A trigger on a source decides whether a change to it starts a new run.

## Repository sources

Delivery has one source resource per version control provider. Each takes a `repository` and a `branch`:

| Resource | `repository` format |
| --- | --- |
| `GitHubSource` | `owner/repo` |
| `GitLabSource` | `group/subgroup/repo`, the full path |
| `BitbucketSource` | `workspace/repo` |
| `AzureDevOpsSource` | `org/project/repo` |

Pulumi Cloud uses your organization's [version control integration](/docs/integrations/version-control/) for whichever account, group, workspace, or Azure DevOps organization holds the repository. Give that integration access to every repository a source names, including the repository of the pipeline program itself.

A source locks its commit when the run first creates it. Every stage of the run then uses that commit, so `prod` deploys exactly what `dev` tested even if new commits land in between. The `commit` output holds the locked commit.

## Pipeline sources

A `PipelineSource` reads the release that a stage of another pipeline deployed. It's how a downstream pipeline picks up values, such as a cluster endpoint, that an upstream pipeline published as [artifacts](/docs/delivery/concepts/stages-and-gates/#artifacts). Both pipelines must be in the same organization, and a job can't check out a pipeline source.

```typescript
const platform = new delivery.PipelineSource("platform", {
    pipeline: "platform-delivery/main",
    stage: "prod",
    trigger: true,
});
```

See [Connect pipelines](/docs/delivery/guides/multiple-pipelines/) for the full pattern.

## Triggers

A source with no `trigger` is still part of the release, but changes to it never start a run. That's useful for a shared library repository that you want pinned in each release without redeploying on every commit.

To start a run on every push to the branch, set `trigger: true`. To start a run only when a push changes certain files, set `trigger` to a list of glob patterns:

```typescript
const app = new delivery.GitHubSource("app", {
    repository: "acme/shop",
    branch: "main",
    trigger: { paths: ["src/**", "delivery/**"] },
});
```

On a `PipelineSource`, `trigger: true` starts a run whenever the named upstream stage deploys a new release.

`trigger` must be `true` or, on a repository source, an object with a non-empty `paths` list. Setting `trigger: false` is an error; leave the property out instead.

## Other ways to start a run

You can also start a run from **Run pipeline** in the Pulumi Cloud console, or through the REST API. See [Get started](/docs/delivery/get-started/#watch-the-run).
