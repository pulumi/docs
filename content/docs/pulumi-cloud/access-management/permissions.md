---
title_tag: "Pulumi Cloud: Permissions"
meta_desc: Learn about permissions in Pulumi Cloud and how they control access to resources
title: "Permissions"
h1: "Permissions"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: Permissions
    parent: pulumi-cloud-access-management
    weight: 3
    identifier: pulumi-cloud-access-management-permissions
---

Permissions in Pulumi Cloud are predefined bundles of scopes that are commonly used together. They provide a convenient way to grant related access rights to principals through roles.

## Permission Structure

Permissions in Pulumi Cloud follow a consistent format:

```
resource:action
```

For example:

- `stack:read` - Permission to read stack information
- `environment:write` - Permission to modify environment settings
- `organization:admin` - Permission to manage organization settings

## Default Permissions

Pulumi Cloud provides several default permissions that you can use to quickly get started:

### Stack Permissions

| Permission | Description | Included Scopes |
|------------|-------------|----------------|
| `read` | Basic read-only access to stacks | `stack:read` |
| `write` | Ability to update stack configurations | `stack:read`, `stack:write` |
| `admin` | Full control over stack operations | `stack:read`, `stack:write`, `stack:delete` |

### Environment Permissions

| Permission | Description | Included Scopes |
|------------|-------------|----------------|
| `read` | Basic read-only access to environments | `environment:read` |
| `open` | Ability to access environment resources | `environment:read`, `environment:open` |
| `write` | Ability to modify environment settings | `environment:read`, `environment:open`, `environment:write` |
| `admin` | Full control over environment operations | All environment scopes |

## Resource Types

Permissions can be applied to different types of resources in Pulumi Cloud:

### Organization Resources

- Organization settings
- Member management
- Billing and usage
- Audit logs
- Integration configurations

### Stack Resources

- Stack configurations
- Deployment settings
- Stack tags and annotations
- Stack webhooks
- Stack schedules

### Environment Resources

- Environment configurations
- Environment secrets
- Environment schedules
- Environment webhooks
- Environment versions

### Insights Resources

- Insights accounts
- Policy evaluations
- Scan configurations
- Results and reports

## Permission Inheritance

Permissions in Pulumi Cloud follow these inheritance rules:

1. **Role-Based Inheritance**: When a role is assigned to a team, all team members inherit the role's permissions
2. **Permission Inheritance**: Higher-level permissions include all scopes from lower-level permissions
3. **Resource Inheritance**: Some permissions automatically grant access to related resources

## Best Practices

When working with permissions in Pulumi Cloud, consider these best practices:

1. **Start with Default Permissions**: Use the default permissions when possible
2. **Create Custom Permissions**: Create custom permissions for specific use cases
3. **Regular Audits**: Periodically review permission assignments
4. **Documentation**: Document custom permissions and their purposes
5. **Testing**: Test permission assignments to ensure they work as expected

## Related Resources

- [Roles](/docs/pulumi-cloud/access-management/roles)
- [Scopes](/docs/pulumi-cloud/access-management/scopes)
- [Teams](/docs/pulumi-cloud/access-management/teams)
