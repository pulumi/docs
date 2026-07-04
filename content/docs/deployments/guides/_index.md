---
title: Guides
title_tag: Pulumi Deployments Guides
meta_desc: Task-oriented guides for Pulumi Deployments — cloud credentials, custom images, customer-managed runners, private sources, OIDC, and dependent stack updates.
menu:
  deployments:
    name: Guides
    parent: deployments-home
    identifier: deployments-guides
    weight: 25
---

These guides walk through common Pulumi Deployments tasks. Each one is self-contained, so start with whichever matches what you are trying to do.

- [Cloud Credentials](/docs/deployments/guides/cloud-credentials/): Supply the cloud credentials a deployment needs to manage your infrastructure.
- [Requiring Approval Before a Deployment Runs](/docs/deployments/guides/gated-deployments/): Deployments has no native approval gate; this workaround requires reviewer sign-off using an ESC Open approval.
- [Customer-Managed Workflow Runners](/docs/deployments/guides/customer-managed-workflow-runners/): Set up and scale self-hosted runner pools.
- [Custom Images](/docs/deployments/guides/custom-images/): Customize the container image your deployments run in.
- [Private Sources](/docs/deployments/guides/private-sources/): Give deployments access to private Git repositories and package feeds.
- [Dependent Stack Updates](/docs/deployments/guides/dependent-stack-updates/): Trigger downstream stacks automatically when an upstream stack changes, without duplicate fires or loops.
- [OIDC Setup](/docs/deployments/guides/oidc/): Configure OpenID Connect to obtain short-lived cloud provider credentials.
