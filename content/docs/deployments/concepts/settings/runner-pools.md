---
title_tag: "Deployment Runner Pools | Pulumi Deployments"
meta_desc: Choose where Pulumi Deployments run, on Pulumi-managed runners or your own customer-managed deployment runner pools
title: "Deployment Runner Pools"
h1: "Deployment Runner Pools"
menu:
  deployments:
    name: Deployment Runner Pools
    parent: deployments-concepts-settings
    identifier: deployments-concepts-settings-runner-pools
    weight: 40
---

When using Pulumi Deployments, you have options for where your workflows run:

- **[Pulumi-managed runners](/docs/deployments/concepts/pulumi-managed-runners/)**: runners in the Pulumi hosted pool, managed by Pulumi.
- **[Customer-managed deployment runners](/docs/deployments/concepts/customer-managed-runners/)**: self-hosted runners that can access private networks and resources, supporting deployments, [Discovery](/docs/discovery-governance/concepts/discovery/) scans, and [policy evaluations](/docs/discovery-governance/concepts/policy-as-code/).

To choose where a stack's deployments run, open the stack's **Settings** → **Deploy** page and pick a pool from the **Deployment runner pool** dropdown. Choose **Pulumi hosted pool** to use Pulumi-managed runners.

If a stack does not have a pool explicitly configured, the deployment uses the organization's [default workflow runner pool](/docs/deployments/guides/customer-managed-workflow-runners/#setting-an-organization-default-pool) if one is set, and otherwise falls back to the Pulumi hosted pool.

## Customer-managed deployment runner pools

{{< pulumi-cloud "customer-managed-runners" "named" />}}

To run a stack's deployments on customer-managed deployment runners, select one of your organization's runner pools from the **Deployment runner pool** dropdown. To create and scale pools, see the [customer-managed deployment runners setup guide](/docs/deployments/guides/customer-managed-workflow-runners/).

Self-hosted Pulumi Cloud installations have no Pulumi hosted pool, so every stack must use a customer-managed deployment runner pool. If the organization has no pools yet, the settings page links to create one, or tells you to ask an organization admin if you can't manage pools yourself.
