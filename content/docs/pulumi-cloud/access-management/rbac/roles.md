---
title_tag: "Pulumi Cloud: Roles"
meta_desc: Learn about roles in Pulumi Cloud and how they control access to resources
title: "Roles"
h1: "Roles"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: Roles
    parent: pulumi-cloud-access-management-rbac
    weight: 2
    identifier: pulumi-cloud-access-management-rbac-roles
---

A role in Pulumi Cloud is the primary way to define what resources a principal (user, team, or machine token) can access and what they can do with them. Roles allow you to apply [permissions](../permissions) to a set of [entities](../permissions#entities) and assign this access to a principal.

## Default Roles

Pulumi Cloud provides several default roles that you can use to quickly get started:

### Organization Roles

| <div style="width: 200px;">Role</div>| Description |
|------|-------------|
| `Admin` | Full access to all organization resources and settings. Can manage members, roles, and organization-wide configurations.</div> |
| `Member` | Basic access to view organization resources and participate in stack operations. Cannot modify organization settings. Default access for members to organization entities can be controlled via the **Access management** page under **Settings**.</div> |
| `Billing Manager` | Access to view and manage billing information. Cannot modify other organization settings or resources.</div> |

## Custom Roles

{{% notes "info" %}}
Custom roles are only available to organizations using Pulumi Enterprise Edition and Pulumi Business Critical Edition.
To learn more about editions visit the [pricing page](/pricing/).
{{% /notes %}}

You can create and manage custom roles to define more granular access controls for your organization. Custom roles allow you to:

- Bundle specific permissions for different resource types
- Control access to like resources or groups of resources

### Creating Custom Roles

To create a custom role, you must be an organization admin.

Visit the **Roles** page under **Settings** to see your organization roles

![View all organization roles](/docs/pulumi-cloud/access-management/rbac/1-create-role.png).

To create a new role, click **Create custom role**

![Create a role page](/docs/pulumi-cloud/access-management/rbac/2-create-role.png).

You will need to provide a unique name for the role. Optionally, but recommended, you can provide a description to contextualize the role and its purpose.

![Providing a name and description for the role](/docs/pulumi-cloud/access-management/rbac/3-create-role.png).

You can assign permissions to the role to be applied globally across all RBAC entities of a specific type, or to individual entities (specific stacks, environments, or insights accounts).

You'll first see the option to assign permissions to entities globally within the org:

![Assigning a global permission to the role](/docs/pulumi-cloud/access-management/rbac/4-create-role.png).

You can also select **Add Pulumi entities** to assign permissions to specific entities. You'll be able to search for stacks, environments, or insights accounts within your org and assign existing permissions of their entity type to the entity.

![Assigning permissions to two stacks](/docs/pulumi-cloud/access-management/rbac/5-create-role.png).

When done, click **Create role**. You should be taken back to the Roles page, where you will see your new role:

![Your role has been created, visible here on the Roles page](/docs/pulumi-cloud/access-management/rbac/6-create-role.png).

You can now assign this role to principals in your organization.

### Managing Custom Roles

To update or delete a custom role, simply click on the ellipsis icon next to the role on the Roles page.

## Role Assignment

Currently, roles can be assigned to organization tokens. When early access has ended for this feature, you will be able to assign roles to teams or individual users in your organization.

### Assigning a role to an organization token

[Organization tokens](/docs/pulumi-cloud/access-management/access-tokens/#organization-access-tokens) can be assigned both default and custom roles to narrow their scope within your organization.

Follow the process to [create an organization token](/docs/pulumi-cloud/access-management/access-tokens/#creating-an-organization-access-token).

![Create an organization access token, a role field is available](/docs/pulumi-cloud/access-management/rbac/1-create-token-role.png).

Note that you will have the ability to provide a role. Choose a default or custom role to assign to it.

![Assign a role to your organization token](/docs/pulumi-cloud/access-management/rbac/2-create-token-role.png).

Proceed with creating the token. The access token you have created will be narrowed in scope according to the permissions of the role within your organization.

## Best Practices

When working with roles in Pulumi Cloud, consider these best practices:

1. **Principle of Least Privilege**: Assign only the scopes necessary for users to perform their tasks.
2. **Role Reusability**: Design custom roles and permissions in a way that maps to real-world concepts within your org, allowing for easy reuse.
3. **Regular Review**: Periodically schedule reviews of role assignments and scopes.
4. **Documentation**: Document the purpose and scopes of custom roles both internally and within the role's metadata.

## Related Resources

- [Teams](/docs/pulumi-cloud/access-management/rbac/teams)
- [Permissions](/docs/pulumi-cloud/access-management/rbac/permissions)
- [Scopes](/docs/pulumi-cloud/access-management/rbac/scopes)
