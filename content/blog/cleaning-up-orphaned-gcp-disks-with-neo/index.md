---
title: "Cleaning Up Orphaned GCP Persistent Disks with Neo"
date: 2026-04-20
draft: false
meta_desc: "Orphaned GCP disk cleanup with Neo: Read-Only Mode discovers, Plan Mode scopes, CrossGuard blocks any delete without a snapshot label."
meta_image: meta.png
feature_image: feature.png
authors:
    - neo-team
tags:
    - neo
    - gcp
    - ai
    - policy-as-code
schema_type: auto

social:
    twitter: |
        GCP persistent disks outlive the instances and clusters that created them. They bill quietly until someone decides they're safe to delete. Nobody does, because deleting prod disks is risky.

        We gave Neo the job. Here's how we made it safe to run.
    linkedin: |
        Unattached GCP persistent disks accumulate quietly. GKE cluster churn leaves PVC-backed disks behind. Teardowns remove instances without removing volumes. One-off experiments in a secondary zone outlive the engineers who ran them.

        Every one of these disks bills per GB per month, and nobody owns the cleanup.

        We cleared a production backlog with Neo. The part that surprised us was how short the safety layer turned out to be, and how much of the process was just a conversation.

        Here's the workflow and the policy code.
    bluesky: |
        Orphaned GCP persistent disks accumulate silently after GKE churn and teardowns. Every one bills per GB per month, and nobody owns the cleanup.

        We used Neo to clear the backlog on a production project. Here's how we kept it safe.
---

Unattached GCP persistent disks accumulate quietly. GKE cluster churn leaves PVC-backed disks behind. Teardowns remove instances without removing volumes. One-off experiments in a secondary zone outlive the engineers who ran them. Every one of these disks bills per GB per month, and nobody owns the cleanup.

<!--more-->

Today we use Neo to clear orphaned disk backlogs on a Pulumi-managed GCP project, gated by a CrossGuard policy that blocks any delete without a fresh snapshot label. This post shows the workflow, the prompts, and the policy.

## Overview

[Neo](/neo/) is Pulumi's infrastructure agent. It runs inside [Pulumi Cloud](/docs/pulumi-cloud/) and performs operations on stacks we already manage: `preview`, `up`, `refresh`, `destroy`, and `import`. Neo runs with the permissions of the user who creates the task, and every mutating operation waits for an approval in Pulumi Cloud. [CrossGuard](/crossguard/) evaluates resource changes at preview time and can block a destroy before it reaches the cloud.

Two recent Neo features matter for this workflow:

| Mode | What Neo can do | Why it fits |
|---|---|---|
| Read-Only | Reads, previews, and pull requests. No mutations. | Safe discovery of candidate disks. |
| Plan | Dedicated discovery and synthesis before any execution. | Agree on scope before a destroy runs. |

## Discovery in Read-Only Mode

We start in [Read-Only Mode](/blog/neo-read-only-mode/). Neo can enumerate and preview but cannot delete, so a bad prompt cannot cause a bad outcome.

> In the `platform-prod` stack, list every `gcp.compute.Disk` that is not attached to an instance and was created more than 90 days ago. Include size, zone, creation time, and labels. Do not propose any changes.

Neo returns a table of candidate disks drawn from stack state and the live GCP project. Disks created outside Pulumi are not in state and do not appear here. Those cases need `pulumi import` before Neo can act on them, which is a separate workflow.

## Planning the cleanup

We switch to [Plan Mode](/blog/neo-plan-mode/) to scope the destroy. Neo produces a plan that groups candidates by zone, excludes anything with a `keep=true` label, and calls out disks whose most recent snapshot is older than 30 days. We refine the plan through normal conversation, approve it, and Neo carries the context forward into execution.

The destroy preview arrives as a standard Pulumi diff:

```text
  gcp:compute:Disk (orphan-pvc-7f2a):
    - gcp:compute/disk:Disk
        name:         "gke-staging-pvc-7f2a"
        zone:         "us-central1-b"
        sizeGb:       200
        creationTime: "2025-08-14T09:11:23Z"
        labels:       { "snapshot-taken": "true" }

  Resources:
    - N to delete
```

Neo waits for an approval in Pulumi Cloud before any disk is removed.

## The safety layer

Destroying a persistent disk is irreversible. We require that every disk targeted for deletion carry a `snapshot-taken=true` label, applied by a preceding snapshot run. A CrossGuard policy enforces this at preview time:

```typescript
import * as gcp from "@pulumi/gcp";
import { PolicyPack, validateResourceOfType } from "@pulumi/policy";

new PolicyPack("gcp-disk-safety", {
  policies: [{
    name: "require-snapshot-label-before-delete",
    enforcementLevel: "mandatory",
    validateResource: validateResourceOfType(gcp.compute.Disk, (disk, args) => {
      const labels = disk.labels ?? {};
      if (labels["snapshot-taken"] !== "true") {
        args.reportViolation(
          "Disk must carry label snapshot-taken=true before it can be deleted.",
        );
      }
    }),
  }],
});
```

Cleanup becomes two phases. The first phase is its own prompt:

> Snapshot each disk on the approved destroy plan. Apply the label `snapshot-taken=true` after the snapshot completes successfully. Do not delete anything.

Neo produces a preview that creates one `gcp.compute.Snapshot` per target and updates each disk's labels. The policy passes, the update runs, and snapshots land in Cloud Storage. The second phase is the destroy. The policy passes because the label is present, and the approval gate is the only thing between preview and delete.

If someone prompts Neo to delete a disk that was never snapshotted, the preview fails policy evaluation and the destroy never reaches GCP.

## Governance by construction

Three controls make this workflow safe to run on a production project:

- Neo inherits the caller's permissions. A user who cannot delete disks cannot cause Neo to delete them.
- Every mutation waits for explicit approval in Pulumi Cloud. Read-Only Mode removes mutation from the option set entirely when that tighter boundary is wanted.
- CrossGuard enforces the snapshot requirement regardless of who or what initiated the destroy.

The Pulumi Cloud audit log records the prompt, the previews, the approvals, the resources changed, and the identity that approved each step. The same record applies whether the operator is a person at the CLI, a CI pipeline, or Neo.

## Getting started

- Open Neo in Pulumi Cloud and run a Read-Only task to inventory orphaned disks on a GCP stack.
- Add a CrossGuard policy pack that requires a snapshot label before deletion on any resource class where a destroy is expensive.
- Use Plan Mode when scoping the destroy so the plan is agreed before execution begins.

The same pattern applies to unattached static IPs, idle Cloud SQL read replicas, and Cloud Storage buckets with no lifecycle rule. The prompt changes. The governance does not.
