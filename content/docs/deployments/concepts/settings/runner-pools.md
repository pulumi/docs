---
title_tag: "Deployment Runner Pools | Pulumi Deployments"
meta_desc: Choose where Pulumi Deployments run and assign the organization role a deployment uses
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
- **[Customer-managed deployment runners](/docs/deployments/concepts/customer-managed-runners/)**: self-hosted runners that can access private networks and resources, supporting deployments, [Discovery](/docs/discovery-governance/discovery/) scans, and [policy evaluations](/docs/discovery-governance/policy/).

To choose where a stack's deployments run, open the stack's **Settings** → **Deploy** page and pick a pool from the **Deployment runner pool** select. Choose **Pulumi hosted pool** to use Pulumi-managed runners.

If a stack does not have a pool explicitly configured, the deployment uses the organization's [default workflow runner pool](/docs/deployments/guides/customer-managed-workflow-runners/#setting-an-organization-default-pool) if one is set, and otherwise falls back to the Pulumi hosted pool.

## Customer-managed deployment runner pools

{{< pulumi-cloud "customer-managed-runners" "named" />}}

To run a stack's deployments on customer-managed deployment runners, select one of your organization's runner pools from the **Deployment runner pool** select. To create and scale pools, see the [customer-managed deployment runners setup guide](/docs/deployments/guides/customer-managed-workflow-runners/).

Self-hosted Pulumi Cloud installations have no Pulumi hosted pool, so every stack must use a customer-managed deployment runner pool. If the organization has no pools yet, the settings page links to create one, or tells you to ask an organization admin if you can't manage pools yourself.

## Pulumi Cloud role

When configuring deployment settings, you can choose the organization role that a stack's deployments run as. On the stack's **Settings** → **Deploy** page, pick a role from the **Pulumi Cloud role** select. Custom roles are marked with a **Custom** badge.

If you leave the select on **Default access**, the deployment will only have access to the specific stack being deployed. However, this limited access can cause failures when the deployment needs to:

- Access stack references from other stacks
- Access environments
- Manage organization resources such as teams, members, or OIDC issuers

By selecting an appropriate role, you provide the deployment with the necessary permissions to access these additional resources. For fine-grained access control, you can create custom roles with specific permissions tailored to what the deployment needs to accomplish.

Organization roles are managed through the Roles section. For more information on creating and managing roles, see the [Roles documentation](/docs/administration/concepts/rbac/roles/).

For a full explanation of how a deployment's permissions are determined, the default permissions for each trigger, and how to grant additional access, see [Permissions](/docs/deployments/operations/permissions/).
