---
title_tag: "Skipping Intermediate Deployments | Pulumi Deployments"
meta_desc: Collapse a backlog of queued Pulumi Deployments into a single run for high-volume stacks
title: "Skipping Intermediate Deployments"
h1: "Skipping Intermediate Deployments"
menu:
  deployments:
    name: Skipping Intermediate Deployments
    parent: deployments-concepts-settings
    identifier: deployments-concepts-settings-skip-intermediate-deployments
    weight: 70
---

By default, when multiple deployments are queued for a stack, Pulumi runs them sequentially until the backlog is cleared. For a stack that receives many pushes in quick succession — for example, a busy shared stack where pull requests merge frequently — this means every intermediate commit gets its own deployment, even though only the final state matters.

{{% notes type="info" %}}
For high-volume stacks, Pulumi recommends enabling **Skip intermediate deployments** to batch the backlog into a single run. This is the supported best practice for collapsing a queue of rapid-fire deployments; you should not need ad-hoc workarounds such as manually cancelling in-progress deployments.
{{% /notes %}}

With **Skip intermediate deployments** enabled, whenever a deployment finishes Pulumi skips every queued deployment of the same type except the most recent one, so the stack jumps straight to the latest desired state instead of replaying every commit in between. Because the changes are cumulative, the end result is the same, and you save the deployment minutes and wall-clock time the skipped runs would have consumed.

Enable it from your stack's deployment settings in the Pulumi Cloud UI, or set [`operationContext.options.skipIntermediateDeployments`](/registry/packages/pulumiservice/api-docs/deploymentsettings/) to `true` on the `pulumiservice.DeploymentSettings` resource.

Keep these trade-offs in mind:

- **Only deployments of the same type are consolidated.** Skipping applies per operation type (`update`, `preview`, `destroy`, and so on), so a queued `destroy` is never skipped in favor of an `update`.
- **You lose the per-commit deployment record.** Skipped commits do not get their own deployment, so you won't have an individual update history or preview for each intermediate change.
- **The deployment in progress is not interrupted.** Skipping consolidates the *queued* backlog; it does not cancel a deployment that is already running. Stopping a running deployment requires explicitly [cancelling it](/docs/reference/cloud-rest-api/deployments/), which is a dangerous operation that can leave the stack in an inconsistent state.
