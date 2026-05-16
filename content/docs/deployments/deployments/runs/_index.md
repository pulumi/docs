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
