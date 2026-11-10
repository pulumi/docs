---
title_tag: Connect Pulumi Delivery pipelines
meta_desc: Pass artifacts from an upstream Pulumi Delivery pipeline to a downstream one, and run several pipelines from a single monorepo.
title: Connect pipelines
h1: Connect pipelines
menu:
  delivery:
    name: Connect pipelines
    parent: delivery-guides
    weight: 30
aliases: []
---

Larger estates rarely fit in one pipeline. A platform team might own the cluster and network, while application teams each own a service that deploys onto it. Delivery connects these pipelines through [artifacts](/docs/delivery/concepts/artifacts/) and [pipeline sources](/docs/delivery/concepts/sources-and-triggers/#pipeline-sources).

## Upstream and downstream pipelines

The upstream pipeline publishes an `Artifact` from a stage:

```typescript
new delivery.Artifact("clusterEndpoint", { stage: prod, value: cluster.endpoint });
```

The downstream pipeline reads it with a `PipelineSource`:

```typescript
const platform = new delivery.PipelineSource("platform", {
    pipeline: "platform-delivery/main",
    stage: "prod",
    trigger: true,
});

new delivery.Stacks("app", {
    stage: dev,
    stacks: {
        app: {
            stack: "shop-app/dev",
            source: repo,
            directory: "app",
            config: { clusterEndpoint: platform.artifacts["clusterEndpoint"] },
        },
    },
});
```

With `trigger: true`, every new release that reaches the upstream `prod` stage starts a run of the downstream pipeline.

Both pipelines must be in the same organization, and the downstream pipeline's service principal needs read access to the upstream pipeline stack. Your own access isn't enough.

If any artifact is secret, the whole `artifacts` map is secret. Since `config` rejects secrets, pass a secret artifact in `environment` instead.

## Several pipelines in one repository

A monorepo can hold several pipeline programs. Give each its own program directory, its own pipeline stack, and a source that triggers only on its own paths:

```typescript
// delivery/shop/index.ts
const repo = new delivery.GitHubSource("repo", {
    repository: "acme/monorepo",
    branch: "main",
    trigger: { paths: ["shop/**", "delivery/shop/**"] },
});
const pipeline = new delivery.Pipeline("shop", {
    program: { source: repo, directory: "delivery/shop" },
});
```

A `search` pipeline in `delivery/search/index.ts` looks the same with `search/**` and `delivery/search/**` as its paths. A push that changes only `search/` then starts only the `search` pipeline. Register each pipeline with `pulumi up` in its own directory, on its own pipeline stack, such as `acme/shop-delivery/main` and `acme/search-delivery/main`.
