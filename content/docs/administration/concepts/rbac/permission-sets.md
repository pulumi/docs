---
title_tag: "Pulumi Cloud: Permission sets"
meta_desc: Learn about permission sets in Pulumi Cloud and how they control access to resources
title: "Permission Sets"
h1: "Permission Sets"
menu:
  administration:
    name: Permission sets
    parent: administration-concepts-rbac
    weight: 2
    identifier: pulumi-cloud-access-management-rbac-permission-sets
aliases:
- /docs/administration/access-identity/rbac/permissions/
- /docs/pulumi-cloud/access-management/rbac/permissions/
- /docs/administration/access-identity/rbac/permission-sets/
- /docs/administration/access-identity/stack-permissions/
- /docs/console/collaboration/stack-permissions/
- /docs/intro/console/stack-permissions/
- /docs/pulumi-cloud/access-management/stack-permissions/
- /docs/reference/service/roles-and-access-controls/
pulumi_cloud_feature: rbac
---

Permission sets in Pulumi Cloud are predefined bundles of [scopes](/docs/administration/concepts/rbac/scopes) that are commonly used together. They provide a convenient way to grant related access rights to an [entity](/docs/administration/concepts/rbac/entities) (resource) or set of entities (resources).

Every permission set belongs to a specific [entity type](/docs/administration/concepts/rbac/entities#entity-types) (stacks, environments, or cloud accounts) and can only include scopes of that same type.

## Default permission sets

Pulumi Cloud provides several default permission sets that you can use to quickly get started.

{{< rbac-scopes-updated >}}

### Stack permission sets

{{< rbac-permission-sets "stack" >}}

### Environment permission sets

{{< rbac-permission-sets "environment" >}}

### Cloud account permission sets

{{< rbac-permission-sets "insights-account" >}}

### Organization settings permission sets

These permission sets bundle organization-level (global) scopes. Rather than granting access to a specific [entity](/docs/administration/concepts/rbac/entities), they set a role's [organization access level](/docs/administration/concepts/rbac/entities#organization-level-access) — the permissions for org-wide operations such as billing, member management, and creating resources.

{{< rbac-permission-sets "global" >}}

## Custom permission sets

### Creating custom permission sets

To create a custom permission set, you must be an organization admin.

1. Visit **Settings** > **Access management** and select the **Permission sets** tab.
1. To create a new permission set, select **Create custom permission set** within the associated entity group.
1. Provide a unique name for the permission set. Optionally, but recommended, provide a description to contextualize the permission set and its purpose.
1. Select the scopes you would like to bundle within this permission set.
1. Select **Create permission set**. The panel closes and your new permission set appears on the permission sets page.

You can now assign this custom permission set to roles within your organization.

{{% notes type="info" %}}
A custom permission set cannot be deleted while it is in use by one or more roles. Remove the permission set from those roles before deleting it.
{{% /notes %}}

## Related resources

* [Scopes](/docs/administration/concepts/rbac/scopes): The most granular access rights in Pulumi Cloud, written as `object:action`. Each scope belongs to one entity type and is the building block of permission sets.
* [Entities and organization-level access](/docs/administration/concepts/rbac/entities): The objects that permission sets are granted on (stacks, environments, and cloud accounts), plus the organization-level access that governs org-wide operations.
* [Roles](/docs/administration/concepts/rbac/roles): Collections of permission sets applied to entities and combined with an organization access level. You assign a role to users, teams, and machine tokens.
* [Teams](/docs/administration/concepts/rbac/teams): Groups of users that can be assigned roles and entity access. Each member inherits the union of the team's roles on top of their own role.
