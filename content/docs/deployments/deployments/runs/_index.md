---
title: Runs
title_tag: Deployment runs | Pulumi Deployments
meta_desc: How Pulumi Cloud executes your deployments. Choose the container image that runs your code and the workflow runner it runs on.
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  deployments:
    name: Runs
    parent: deployments-deployments
    identifier: deployments-deployments-runs
    weight: 40
---

Every Pulumi Deployment runs in a container image on a workflow runner. Two settings control how that run works:

- The [image](/docs/deployments/deployments/runs/images/): a Pulumi-managed Linux image by default, or a custom image when your project needs extra tools.
- The [runner](/docs/deployments/deployments/runs/customer-managed-agents/): Pulumi-hosted by default, or customer-managed when you need to run on your own infrastructure.

## Hardware and operating system

When a deployment runs on a Pulumi-hosted workflow runner, it executes inside a Linux container with the following resources:

| Resource | Allocation |
|---|---|
| vCPU | 2 |
| Memory | 8 GB |
| Disk | A 32 GB volume, with roughly half available for your program's working files after the executor image and dependency caches |

With the default executor image, the container's operating system is Debian, regardless of the operating system of the host it runs on. If you supply a [custom executor image](/docs/deployments/deployments/runs/images/), the operating system is whatever that image is built on. If a deployment depends on a specific OS, package manager, or system library, match it to the image you use.

These specifications apply to Pulumi-hosted workflow runners. [Customer-managed workflow runners](/docs/deployments/deployments/runs/customer-managed-agents/) run on infrastructure you provision, so their hardware and operating system are whatever you configure.
