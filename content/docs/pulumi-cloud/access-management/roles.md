---
title_tag: "Pulumi Cloud: Roles"
meta_desc: Learn about roles in Pulumi Cloud and how they control access to resources
title: "Roles"
h1: "Roles"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: Roles
    parent: pulumi-cloud-access-management
    weight: 4
    identifier: pulumi-cloud-access-management-roles
---

A role in Pulumi Cloud is the primary way to define what resources a principal (user, team, or service account) can access and what they can do with them. Roles combine sets of scopes that can be assigned to principals to control their access to resources.

## Default Roles

Pulumi Cloud provides several default roles that you can use to quickly get started:

### Organization Roles

| Role | Description |
|------|-------------|
| `AdminRole` | Full access to all organization resources and settings. Can manage members, roles, and organization-wide configurations. |
| `MemberRole` | Basic access to view organization resources and participate in stack operations. Cannot modify organization settings. |
| `BillingManagerRole` | Access to view and manage billing information. Cannot modify other organization settings. |

## Custom Roles

You can create custom roles to define more granular access controls for your organization. Custom roles allow you to:

- Bundle specific scopes for different resource types
- Control access to specific resources or groups of resources
- Create reusable permissions that can be assigned to multiple principals

### Creating Custom Roles

When creating a custom role, you can:

1. Define which resources the role applies to (e.g., all stacks, specific environments)
2. Specify what actions are allowed on those resources
3. Combine multiple permissions to create comprehensive access patterns

### Role Assignment

Roles can be assigned to:

- Individual users
- Teams
- Service accounts (organization tokens)

When a role is assigned to a team, all members of that team inherit the role's permissions.

## Role Types

Roles in Pulumi Cloud can be categorized into different types based on their purpose:

### Organization Management Roles

These roles control access to organization-wide settings and resources:

- Member management
- Organization settings
- Billing and usage
- Audit logs
- Integration configurations

### Resource-Specific Roles

These roles control access to specific types of resources:

- Stack management
- Environment access
- Insights account administration
- IaC policy management

### Service Roles

These roles are designed for automated systems and service accounts:

- Deployment automation
- CI/CD integration
- Monitoring and scanning
- API access

## Best Practices

When working with roles in Pulumi Cloud, consider these best practices:

1. **Principle of Least Privilege**: Assign only the scopes necessary for users to perform their tasks
2. **Role Reusability**: Create roles that can be reused across multiple principals
3. **Regular Review**: Periodically review role assignments and scopes
4. **Documentation**: Document the purpose and scopes of custom roles
5. **Testing**: Test role assignments to ensure they provide the intended access

## Related Resources

- [Permissions](/docs/pulumi-cloud/access-management/permissions)
- [Scopes](/docs/pulumi-cloud/access-management/scopes)
- [Teams](/docs/pulumi-cloud/access-management/teams)
