---
title_tag: "Pulumi Deployments: Security and Operations"
meta_desc: Security and operational considerations for Pulumi Deployments including isolation, deployment queues, dependency caching, and operational details.
title: Security and operations
h1: Pulumi Deployments Security and Operations
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: Security and operations
    parent: pulumi-cloud-deployments
    weight: 100
    identifier: pulumi-cloud-deployments-security-operations
aliases:
  - /docs/intro/deployments/faq/
  - /docs/pulumi-cloud/deployments/faq/
---

## Security and Isolation

Deployments run on single-use virtual machines and compute and storage are never shared across runs. We designed our architecture to maximize isolation. In addition, security features like OIDC allow you to fine tune credential scope, lifetime, and expiration policies at a per-deployment level. It is also possible to use [self-hosted runners](/docs/pulumi-cloud/deployments/customer-managed-agents/) if you require additional isolation.

## Deployment queue

Deployments are queued on a first-come, first-served basis. If you have multiple deployments running at the same time, they will be queued and run in the order they were submitted.

On a stack level, only one deployment can run at a time. On an organization level, the concurrency limit is determined by [SKU](/pricing/).

Deployments will remain in the queue for a maximum of 7 days. If a deployment is not started within 7 days (if deployments are paused or the agent pool assigned to the stack is unavailable), it will be automatically removed from the queue and marked as `skipped`.

## Paused deployments

It is possible to pause deployments at the stack or organization level. Deployments that are already running are allowed to complete and are not paused. New deployments are queued, and will run when the stack or organization’s deployments are resumed.
