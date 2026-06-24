---
title: Deployment queue
title_tag: "Deployment queue | Pulumi Deployments"
meta_desc: How Pulumi Deployments queues and runs deployments — first-come, first-served ordering, concurrency limits, queue expiry, and pausing deployments.
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  deployments:
    name: Deployment queue
    parent: deployments-operations
    identifier: deployments-operations-deployment-queue
    weight: 20
---

Deployments are queued on a first-come, first-served basis. If you have multiple deployments at the same time, they are queued and run in the order they were submitted.

On a stack level, only one deployment can run at a time. On an organization level, the concurrency limit is determined by [SKU](/pricing/).

Deployments remain in the queue for a maximum of 7 days. If a deployment is not started within 7 days — for example, because deployments are paused or the workflow runner pool assigned to the stack is unavailable — it is automatically removed from the queue and marked as `skipped`.

## Pausing deployments

You can pause deployments at the stack or organization level. Deployments that are already running are allowed to complete and are not paused. New deployments are queued and run when the stack's or organization's deployments are resumed.
