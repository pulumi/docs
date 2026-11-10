---
title_tag: Pulumi Delivery limits
meta_desc: Size and time limits for Pulumi Delivery pipelines, and behavior to plan around when you design and operate one.
title: Limits
h1: Limits
menu:
  delivery:
    name: Limits
    parent: delivery-operations
    weight: 40
aliases: []
---

## Limits

| Limit | Value |
| --- | --- |
| Stack entries and jobs in a pipeline | 200. Each `Stacks` entry and each `Job` counts as one. Artifacts don't count. |
| Passes in a run | 10,000, then the run fails. |
| Time limit of a pass | 1 hour |
| Time limit of a stack update or job | 2 hours. Set `timeout`, in seconds, on a `Stacks` entry to change it. |
| Job outputs | 1 MiB |
| Run stack retention | Deleted 90 days after the run ends |

Each entry of a `Stacks` group uses one slot of your organization's concurrency limit. Registration warns you about a group with more entries than the limit, because it can block itself.

<!-- TODO(launch): Add concurrency limits by edition once pricing is final (DLV-453). Essentials is currently 5 concurrent stack updates. -->

## Behavior to plan around

These behaviors affect how you design and operate a pipeline.

### Runs

- Delivery doesn't detect a cycle between stages. A run in a cycle waits until you cancel it.
- A pipeline runs as one service principal for all of its stages. See [Permissions](/docs/delivery/operations/permissions/#the-identity-a-pipeline-runs-as).

### Pipeline stacks and run stacks

- Passes don't run policy packs. Target stacks keep their own policy groups.
- The pipeline stack's config comes from its config file in the repository, so commit it.
- Delivery deletes a run stack without running a destroy. Any resource in the pipeline program that isn't a Delivery resource stays in your cloud without state. A waiting run keeps its stack.
- You can't delete a pipeline stack while runs are in progress. Deleting a pipeline stack stops the pipeline and deletes its run stacks. After restoring the stack, run `pulumi up` on it to register the pipeline again.
- You can't move a pipeline stack to another organization, or rename or move a run stack.
- If one artifact of a `PipelineSource` is secret, its whole `artifacts` map is secret.
