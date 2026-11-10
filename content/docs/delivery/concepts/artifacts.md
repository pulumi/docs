---
title_tag: Pulumi Delivery artifacts
meta_desc: Publish values such as endpoints and IDs from a Pulumi Delivery stage as artifacts, and read them from other pipelines with a PipelineSource.
title: Artifacts
h1: Artifacts
menu:
  delivery:
    name: Artifacts
    parent: delivery-concepts
    weight: 40
aliases: []
---

An _artifact_ is part of a release: a named value that a stage publishes once the release reaches it, such as a cluster endpoint, a database ID, or a container image tag. Other pipelines in your organization read it with a [`PipelineSource`](/docs/delivery/concepts/sources-and-triggers/#pipeline-sources). Artifacts are how one pipeline hands values to another without either one reaching into the other's stacks.

## Publish an artifact

Declare an `Artifact` in the stage whose release the value belongs to. The artifact takes the name of the resource:

```typescript
new delivery.Artifact("clusterEndpoint", { stage: prod, value: cluster.endpoint });
```

The value can be anything, including a secret or a nested structure. It usually comes from a member's outputs, such as a `Stacks` entry's stack outputs or a job's outputs.

An artifact is published once its stage admits the release and its value is known. Because it belongs to a stage, a downstream pipeline that reads the `prod` stage only ever sees values from releases that made it to `prod`.

## Read artifacts from another pipeline

A downstream pipeline reads the artifacts of one stage of an upstream pipeline through a `PipelineSource`:

```typescript
const platform = new delivery.PipelineSource("platform", {
    pipeline: "platform-delivery/main",
    stage: "prod",
    trigger: true,
});

const clusterEndpoint = platform.artifacts["clusterEndpoint"];
```

The `artifacts` output is a map keyed by artifact name. It's unknown during registration and preview and known during a run. With `trigger: true`, every new release that reaches the upstream stage starts a run of the downstream pipeline, so the downstream pipeline always deploys against the latest values.

Both pipelines must be in the same organization, and the downstream pipeline's [service principal](/docs/delivery/operations/permissions/#the-identity-a-pipeline-runs-as) needs read access to the upstream pipeline stack.

## Secret artifacts

If any artifact is secret, the whole `artifacts` map is secret. A `Stacks` entry's `config` rejects secret values, so pass a secret artifact to a member in `environment` instead.

## Next steps

- Walk through a full upstream and downstream setup in [Connect pipelines](/docs/delivery/guides/multiple-pipelines/).
- Learn how [pipeline sources trigger runs](/docs/delivery/concepts/sources-and-triggers/#triggers).
