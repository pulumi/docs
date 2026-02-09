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
| `Admin` | Full access to all organization resources and settings. Can manage members, roles, and organization-wide configurations.</div> |
| `Member` | Basic access to view organization resources and participate in stack operations. Cannot modify organization settings. Default access for members to organization entities can be controlled via the **Access management** page under **Settings**.</div> |
| `Billing Manager` | Access to view and manage billing information. Cannot modify other organization settings or resources.</div> |

## Custom roles

{{% notes "info" %}}
Custom roles are only available to organizations using Pulumi Enterprise Edition and Pulumi Business Critical Edition.
To learn more about editions visit the [pricing page](/pricing/).
{{% /notes %}}

You can create and manage custom roles to define more granular access controls for your organization. Custom roles allow you to:

- Bundle specific permission sets for different resource types
- Control access to like resources or groups of resources

### Creating custom roles

To create a custom role, you must be an organization admin.

Visit the **Roles** page under **Settings** to see your organization roles

![View all organization roles](/docs/administration/access-identity/rbac/1-create-role.png).

To create a new role, click **Create custom role**

![Create a role page](/docs/administration/access-identity/rbac/2-create-role.png).

You will need to provide a unique name for the role. Optionally, but recommended, you can provide a description to contextualize the role and its purpose.

![Providing a name and description for the role](/docs/administration/access-identity/rbac/3-create-role.png).

You can assign permission sets to the role to be applied globally across all RBAC entities of a specific type, or to individual entities (specific stacks, environments, or insights accounts).

You'll first see the option to assign permission sets to entities globally within the org:

![Assigning a global permission set to the role](/docs/administration/access-identity/rbac/4-create-role.png).

You can also select **Add Pulumi entities** to assign permission sets to specific entities. You'll be able to search for stacks, environments, or insights accounts within your org and assign existing permission sets of their entity type to the entity.

![Assigning permission sets to two stacks](/docs/administration/access-identity/rbac/5-create-role.png).

When done, click **Create role**. You should be taken back to the Roles page, where you will see your new role:

![Your role has been created, visible here on the Roles page](/docs/administration/access-identity/rbac/6-create-role.png).

You can now assign this role to principals in your organization.

### Managing custom roles

To update or delete a custom role, simply click on the ellipsis icon next to the role on the Roles page.

## Role assignment

Currently, roles can be assigned to organization tokens. When early access has ended for this feature, you will be able to assign roles to teams or individual users in your organization.

### Assigning a role to an organization token

[Organization tokens](/docs/administration/access-identity/access-tokens/#organization-access-tokens) can be assigned both default and custom roles to narrow their scope within your organization.

Follow the process to [create an organization token](/docs/administration/access-identity/access-tokens/#creating-an-organization-access-token).

![Create an organization access token, a role field is available](/docs/administration/access-identity/rbac/1-create-token-role.png).

Note that you will have the ability to provide a role. Choose a default or custom role to assign to it.

![Assign a role to your organization token](/docs/administration/access-identity/rbac/2-create-token-role.png).

Proceed with creating the token. The access token you have created will be narrowed in scope according to the permissions of the role within your organization.

## Best practices

When working with roles in Pulumi Cloud, consider these best practices:

1. **Principle of Least Privilege**: Assign only the scopes necessary for users to perform their tasks.
2. **Role Reusability**: Design custom roles and permission sets in a way that maps to real-world concepts within your org, allowing for easy reuse.
3. **Regular Review**: Periodically schedule reviews of role assignments and scopes.
4. **Documentation**: Document the purpose and scopes of custom roles both internally and within the role's metadata.

## Related resources

- [Teams](/docs/administration/access-identity/rbac/teams)
- [Permission sets](/docs/administration/access-identity/rbac/permission-sets)
- [Scopes](/docs/administration/access-identity/rbac/scopes)
