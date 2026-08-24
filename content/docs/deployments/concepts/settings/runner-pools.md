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

- **Pulumi Hosted Pool**: Managed by Pulumi and available to all Pulumi Cloud customers
- **Customer-Managed Workflow Runners**: Self-hosted runners that can access private networks and resources, supporting deployments, [Discovery](/docs/insights/discovery/) scans, and [policy evaluations](/docs/insights/policy/)

If a stack does not have a pool explicitly configured, the deployment uses the organization's [default workflow runner pool](/docs/deployments/guides/customer-managed-workflow-runners/#setting-an-organization-default-pool) if one is set, and otherwise falls back to the Pulumi Hosted Pool.

For more information on customer-managed workflow runners, see the [Customer-Managed Workflow Runners documentation](/docs/deployments/concepts/customer-managed-runners/).

## Role assignment

When configuring deployment settings, you can assign organization roles to the stack token used for deployments. This setting appears as a dropdown menu under "Role assignment" that displays available organization roles.

If no role is selected, the deployment will only have access to the specific stack being deployed. However, this limited access can cause failures when the deployment needs to:

- Access stack references from other stacks
- Access environments
- Manage organization resources such as teams, members, or OIDC issuers

By selecting an appropriate role, you provide the deployment with the necessary permissions to access these additional resources. For fine-grained access control, you can create custom roles with specific permissions tailored to what the deployment needs to accomplish.

Organization roles are managed through the Roles section. For more information on creating and managing roles, see the [Roles documentation](/docs/administration/concepts/rbac/roles/).

For a full explanation of how a deployment's permissions are determined, the default permissions for each trigger, and how to grant additional access, see [Permissions](/docs/deployments/operations/permissions/).
