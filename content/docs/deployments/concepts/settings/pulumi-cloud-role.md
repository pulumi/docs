---
title_tag: "Pulumi Cloud Role | Pulumi Deployments"
meta_desc: Choose the organization role a stack's deployments run as, so they can reach stack references, environments, and organization resources
title: "Pulumi Cloud Role"
h1: "Pulumi Cloud Role"
menu:
  deployments:
    name: Pulumi Cloud Role
    parent: deployments-concepts-settings
    identifier: deployments-concepts-settings-pulumi-cloud-role
    weight: 95
---

When configuring deployment settings, you can choose the organization role that a stack's deployments run as. On the stack's **Settings** → **Deploy** page, open **Advanced settings** and pick a role from the **Pulumi Cloud role** dropdown.

If you leave the dropdown on **Default access**, the deployment only has access to the specific stack being deployed. However, this limited access can cause failures when the deployment needs to:

- Access stack references from other stacks
- Access environments
- Manage organization resources such as teams, members, or OIDC issuers

By selecting an appropriate role, you provide the deployment with the necessary permissions to access these additional resources.

Organization roles are managed through the Roles section. For more information on creating and managing roles, see the [Roles documentation](/docs/administration/concepts/rbac/roles/).

For a full explanation of how a deployment's permissions are determined, the default permissions for each trigger, and how to grant additional access, see [Permissions](/docs/deployments/operations/permissions/).

## Custom roles

{{< pulumi-cloud "custom-roles" "named" />}}

For fine-grained access control, create custom roles with permissions tailored to what the deployment needs. Custom roles appear in the **Pulumi Cloud role** dropdown marked with a **Custom** badge.
