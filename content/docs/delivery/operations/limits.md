---
title_tag: Pulumi Delivery limits and known limitations
meta_desc: Size and time limits for Pulumi Delivery pipelines, and the features that aren't available during public preview.
title: Limits and known limitations
h1: Limits and known limitations
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
| Steps in a pipeline | 200. Each `Stacks` entry counts as one. |
| Passes in a run | 10,000, then the run fails. |
| Time limit of a pass | 1 hour |
| Time limit of a step | 2 hours. Set `timeout`, in seconds, on a `Stacks` entry to change it. |
| Job outputs | 1 MiB |
| Run stack retention | Deleted 90 days after the run ends |

Each entry of a `Stacks` group uses one slot of your organization's concurrency limit. Registration warns you about a group with more entries than the limit, because it can block itself.

<!-- TODO(launch): Add concurrency limits by edition once pricing is final (DLV-453). Essentials is currently 5 concurrent stack updates. -->

## Known limitations

These are the gaps in the public preview, and how to work around them where there's a workaround.

<!-- TODO(launch): Re-verify every item against the GA build on 2026-11-18. Drop what shipped. -->

### Runners and platforms

- Delivery runs only on Pulumi-managed runners. Customer-managed runner pools and Windows aren't supported.
- The Delivery provider has no Windows build, so you register pipelines from Linux or macOS.
- Delivery doesn't work with a DIY backend or with self-hosted Pulumi Cloud.
- `timeout` on a `Job` has no effect yet. A job stops after 2 hours.

### Sources and triggers

- Custom VCS sources and providers without webhooks aren't supported.
- Delivery doesn't support time-based triggers, ESC triggers, or dispatch inputs.
- The Pulumi CLI has no `pulumi delivery` command. Use the console or the REST API.

### Gates

- The `http()` rule isn't available. Registration rejects a stage that uses it.
- Delivery doesn't detect a cycle between stages. A run in a cycle waits until you cancel it.

### Pipeline stacks and run stacks

- Passes don't run policy packs. Target stacks keep their own policy groups.
- The pipeline stack's config comes from its config file in the repository, so commit it. Only the default Pulumi Cloud secrets provider is tested.
- Delivery deletes a run stack without running a destroy. Any resource in the pipeline program that isn't a Delivery resource stays in your cloud without state. A waiting run keeps its stack.
- You can't delete a pipeline stack while runs are in progress. Deleting a pipeline stack stops the pipeline and deletes its run stacks. After restoring the stack, run `pulumi up` on it to register the pipeline again.
- You can't move a pipeline stack to another organization, or rename or move a run stack.
- If one artifact of a `PipelineSource` is secret, its whole `artifacts` map is secret.
