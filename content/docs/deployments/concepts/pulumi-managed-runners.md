---
title: Pulumi-managed runners
title_tag: Pulumi-managed runners | Pulumi Deployments
meta_desc: The Pulumi-hosted compute that runs your deployments by default — its hardware allocation, operating system, and how to customize the executor image.
menu:
  deployments:
    name: Pulumi-managed runners
    parent: deployments-concepts
    identifier: deployments-concepts-pulumi-managed-runners
    weight: 80
---

Every Pulumi Deployment runs in a container image on a *workflow runner* — the compute that executes your Pulumi program. By default, deployments run on Pulumi-managed (Pulumi-hosted) runners, so there is nothing to provision. If you need to run on your own infrastructure instead, see [Customer-managed runners](/docs/deployments/concepts/customer-managed-runners/).

Two settings control how a run works:

- The [image](/docs/deployments/guides/custom-images/): a Pulumi-managed Linux image by default, or a custom image when your project needs extra tools.
- The runner: Pulumi-managed by default, or [customer-managed](/docs/deployments/concepts/customer-managed-runners/) when you need to run on your own infrastructure.

## Hardware and operating system

When a deployment runs on a Pulumi-managed workflow runner, it executes inside a Linux container with the following resources:

| Resource | Allocation |
|---|---|
| vCPU | 2 |
| Memory | 8 GB |
| Disk | A 32 GB volume, with roughly half available for your program's working files after the executor image and dependency caches |

With the default executor image, the container's operating system is Debian, regardless of the operating system of the host it runs on. If you supply a [custom executor image](/docs/deployments/guides/custom-images/), the operating system is whatever that image is built on. If a deployment depends on a specific OS, package manager, or system library, match it to the image you use.

These specifications apply to Pulumi-managed workflow runners. [Customer-managed workflow runners](/docs/deployments/concepts/customer-managed-runners/) run on infrastructure you provision, so their hardware and operating system are whatever you configure.

## Security and isolation

Deployments run on single-use virtual machines; compute and storage are never shared across runs. Security features like OIDC let you fine-tune credential scope, lifetime, and expiration at a per-deployment level. If you require more isolation — for example, running inside your own private network — use [customer-managed runners](/docs/deployments/concepts/customer-managed-runners/). The same isolation applies to every workflow type supported by workflow runners, including [Insights](/docs/insights/) discovery scans and [policy evaluations](/docs/insights/policy/).

## Dependency caching

When using Pulumi-managed runners, you can speed up deployments with [dependency caching](/docs/deployments/concepts/settings/#dependency-caching), which stores your downloaded dependencies between runs.
