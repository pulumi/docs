---
title_tag: "Pulumi Cloud: Scopes"
meta_desc: Learn about scopes in Pulumi Cloud and how they control access to resources
title: "Scopes"
h1: "Scopes"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  administration:
    parent: administration-access-identity-rbac
    weight: 4
    identifier: administration-access-identity-rbac-scopes
aliases:
- /docs/intro/pulumi-service/scopes/
- /docs/intro/pulumi-cloud/scopes/
- /docs/pulumi-cloud/access-management/rbac/scopes/
---

Scopes are the most granular level of access control in Pulumi Cloud's RBAC system. Each scope represents a specific action that can be performed on a resource, such as reading stack configurations or updating environment settings. Scopes are the building blocks of [permission sets](../permission-sets), which are then bundled into [roles](../roles) to create comprehensive access control configurations.

## How Scopes Work

Scopes follow a consistent naming pattern: `object:action`. For example:

- `stack:read` - Allows reading stack configurations
- `environment:write` - Allows modifying environment settings
- `team:create` - Allows creating new teams

Scopes are always associated with a specific [entity type](../permission-sets#entity-types) (like stacks, environments, insights accounts, etc.) and can only be used within permission sets that match that entity type. This ensures that permission sets remain logically grouped and can't mix actions across different types of resources.

You can use scopes to build [custom permission sets](../permission-sets#creating-custom-permission-sets), which allow you to combine commonly related scopes to create meaningful access patterns. For example, a "Stack Manager" permission set might include scopes like:

- `stack:read`
- `stack:write`
- `stack:delete`
- `stack_deployment:create`

## Default Role Assignments

Many scopes are automatically granted through [default roles](../roles#default-roles) in Pulumi Cloud. For example:

- Organization admins have access to all scopes.
- Regular members have access to basic read and write scopes for common operations.
- Billing managers have access to billing-related scopes only.

## Available scopes

You can view the list of available scopes, organized by entity type:

- [Stacks](stacks)
- [Environments](environments)
- [Insights accounts](insights-accounts)
- [Organization settings](org-settings)

## Related Resources

- [Teams](/docs/administration/access-identity/rbac/teams)
- [Roles](/docs/administration/access-identity/rbac/roles)
- [Permission sets](/docs/administration/access-identity/rbac/permission-sets)
