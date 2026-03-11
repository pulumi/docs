---
title_tag: "Pulumi Cloud: Roles"
meta_desc: Learn about roles in Pulumi Cloud and how they control access to resources
title: "Roles"
h1: "Roles"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  administration:
    name: Roles
    parent: administration-access-identity-rbac
    weight: 2
    identifier: pulumi-cloud-access-management-rbac-roles
aliases:
- /docs/administration/access-identity/rbac/roles/
- /docs/pulumi-cloud/access-management/rbac/roles/
- /docs/deployments/access-management/rbac/roles/
---

A role in Pulumi Cloud is the primary way to define what resources a principal (user, team, or machine token) can access and what they can do with them. Roles allow you to apply [permission sets](../permission-sets) to a set of [entities](../permission-sets#entities) and assign this access to a principal.

## Default roles

Pulumi Cloud provides several default roles that you can use to quickly get started:

### Organization roles

| <div style="width: 200px;">Role</div>| Description |
|------|-------------|
| `Admin` | Full access to all organization resources and settings. Can manage members, roles, and organization-wide configurations. |
| `Member` | Basic access to view organization resources and participate in stack operations. Cannot modify organization settings. When your organization has custom roles, you can set an **organization default role** — a custom role that applies to all members who have the Member organization role and have not been given an explicit custom role. To set the default role, navigate to **Settings** > **Roles**, open a custom role, and choose **Set as default role**. |
| `Billing Manager` | Access to view and manage billing information. Cannot modify other organization settings or resources. |

## Custom roles

{{% notes "info" %}}
Custom roles are only available to organizations using Pulumi Enterprise Edition and Pulumi Business Critical Edition. To learn more about editions, visit the [pricing page](/pricing/).

To assign custom roles to **individual users**, the **Assign custom roles to users** setting must be enabled for your organization (**Settings** > **Access Management**). When your organization has custom roles, you can also set an **organization default role** — a custom role that serves as the baseline for all members who have the Member organization role and have not been given an explicit custom role. The default role is set from **Settings** > **Roles** (not from the Access Management page).
{{% /notes %}}

You can create and manage custom roles to define more granular access controls for your organization. Custom roles can include:

1. **Global permission sets** — Organization-wide permissions (e.g. membership, billing, audit logs).
1. **Entity-specific permission sets** — Permission sets applied to specific stacks, environments, or insights accounts (you select the entities when defining the role).
1. **Tag-based (ABAC) rules** — When resource tags match the rule's conditions, the role grants a chosen permission set on that resource. Entity types for tag rules are stacks, environments, and insights accounts. See [Tag-based (ABAC) rules](#tag-based-abac-rules) below.

### Creating custom roles

To create a custom role, you must be an organization admin.

Visit the **Roles** page under **Settings** to see your organization roles

![View all organization roles](/docs/administration/access-identity/rbac/1-create-role.png).

To create a new role, click **Create custom role**. Provide a unique name and, optionally, a description to contextualize the role's purpose.

When creating or editing a custom role, you can configure entity access rules and organization access:

1. **Entity access rules** — Add rules to grant a permission set on specific entities or on all entities of a given type. For each rule, choose the entity type (stack, environment, or insights account) and whether the rule applies to specific entities, all entities, or entities matching tag conditions (ABAC). Select a permission set to grant when the rule matches.

To add a rule for specific stacks, select **Stacks** as the entity type, choose **Select specific stacks**, then click **Choose stacks**.

![Configuring an entity access rule for stacks](/docs/administration/access-identity/rbac/2-create-role.png).

A dialog lists the stacks in your organization. Search and select the stacks to include in the rule.

![Browsing available stacks in the rule criteria dialog](/docs/administration/access-identity/rbac/3-create-role.png).

![Selecting stacks to include in the rule](/docs/administration/access-identity/rbac/4-create-role.png).

After saving rules, the **Entity Access** section displays a table of all configured rules. You can add additional rules with **Add rule**.

1. **Organization access** — Set the permission level for organization-level operations (e.g. creating stacks, managing billing, audit logs). This applies to the organization as a whole and is separate from the entity-based rules above.

![Entity access rules and organization access configured, ready to create the role](/docs/administration/access-identity/rbac/5-create-role.png).

When done, click **Create role**.

You can now assign this role to principals in your organization.

### Managing custom roles

To update or delete a custom role, simply click on the ellipsis icon next to the role on the Roles page.

## Tag-based (ABAC) rules

Tag-based rules (also called tag-based access control or ABAC — attribute-based access control) are part of a **custom role**. Each rule has:

- **Entity type** — Stack, environment, or insights account.
- **Tag conditions** — One or more conditions on resource tags (e.g. tag `env` equals `production`, or tag `team` exists).
- **Permission set** — When the conditions match a resource, the role grants that permission set on that resource.

**Why use them:** Grant access to many resources at once by tag (e.g. all stacks with `team=platform`) without listing each resource. Useful for large organizations.

**How it works:** When evaluating access, Pulumi Cloud checks the user's roles (and the roles of the teams they belong to). For each tag rule in those roles, it evaluates the resource's tags against the rule's conditions. If they match, the rule's permission set is applied to that resource.

To configure a tag-based rule, select **Set conditions** as the scope when adding an entity access rule, then enter one or more tag key/value conditions and choose a permission set.

![Configuring a tag-based (ABAC) rule with entity type Stacks, tag condition sensitivity=critical, and Stack Admin permission](/docs/administration/access-identity/rbac/1-abac-rule.png).

In the Pulumi Cloud UI and API, these rules may be labeled "tag rules" or "tag-based access control rules"; ABAC (attribute-based access control) is the general industry term.

## Role assignment

Roles can be assigned to organization access tokens, users, and teams. Effective permissions are the **union** of the user's organization role and all roles assigned to the teams they belong to (composability).

### Organization access tokens

[Organization access tokens](/docs/administration/access-identity/access-tokens/#organization-access-tokens) can be assigned one role (default or custom) that defines the token's permissions across the organization.

Follow the process to [create an organization token](/docs/administration/access-identity/access-tokens/#creating-an-organization-access-token).

![Create an organization access token, a role field is available](/docs/administration/access-identity/rbac/1-create-token-role.png).

Choose a default or custom role to assign to the token.

![Assign a role to your organization token](/docs/administration/access-identity/rbac/2-create-token-role.png).

The token's access is limited to the permissions of that role within your organization.

### Users

Each organization member has one **organization role** (Admin, Member, Billing Manager, or a custom role). When your organization has custom roles and **Assign custom roles to users** is enabled (in **Settings** > **Access Management**), admins can assign any custom role to individual members. Members who have the Member organization role and have not been given an explicit custom role use the **organization default role** if one is set; otherwise they use the built-in Member role.

### Teams

When your organization has custom roles enabled, [teams can have role assignments](/docs/administration/access-identity/rbac/teams#team-role-assignments): one or more roles (default or custom). Team members receive the **union** of their own user role and all roles assigned to the teams they belong to. So team role assignments add on top of each member's baseline role.

## Best practices

When working with roles in Pulumi Cloud, consider these best practices:

1. **Principle of least privilege**: Assign only the scopes necessary for users to perform their tasks.
1. **Role reusability**: Design custom roles and permission sets in a way that maps to real-world concepts within your org, allowing for easy reuse.
1. **Tag-based rules**: Use tag-based rules to grant access to many resources by tag (e.g. `team=platform`) without listing each resource.
1. **Regular review**: Periodically schedule reviews of role assignments and scopes.
1. **Documentation**: Document the purpose and scopes of custom roles both internally and within the role's metadata.

## Related resources

- [Teams](/docs/administration/access-identity/rbac/teams)
- [Permission sets](/docs/administration/access-identity/rbac/permission-sets)
- [Scopes](/docs/administration/access-identity/rbac/scopes)
