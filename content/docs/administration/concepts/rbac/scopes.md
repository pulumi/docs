---
title_tag: "Pulumi Cloud: Scopes"
meta_desc: Learn about scopes in Pulumi Cloud and how they control access to resources
title: "Scopes"
h1: "Scopes"
menu:
  administration:
    parent: administration-concepts-rbac
    weight: 1
    identifier: administration-concepts-rbac-scopes
aliases:
- /docs/intro/pulumi-service/scopes/
- /docs/intro/pulumi-cloud/scopes/
- /docs/pulumi-cloud/access-management/rbac/scopes/
- /docs/administration/access-identity/rbac/scopes/
pulumi_cloud_feature: rbac
---

Scopes are the most granular level of access control in Pulumi Cloud's RBAC system. Each scope represents a specific action that can be performed on a resource, such as reading stack configurations or updating environment settings. Scopes are the building blocks of [permission sets](/docs/administration/concepts/rbac/permission-sets), which are then bundled into [roles](/docs/administration/concepts/rbac/roles) to create comprehensive access control configurations.

## How scopes work

Scopes follow a consistent naming pattern: `object:action`. For example:

- `stack:read` - Allows reading stack configurations
- `environment:write` - Allows modifying environment settings
- `team:create` - Allows creating new teams

Scopes are always associated with a specific [entity type](/docs/administration/concepts/rbac/entities#entity-types) (like stacks, environments, cloud accounts, etc.) and can only be used within permission sets that match that entity type. This ensures that permission sets remain logically grouped and can't mix actions across different types of resources.

You can use scopes to build [custom permission sets](/docs/administration/concepts/rbac/permission-sets#custom-permission-sets), which allow you to combine commonly related scopes to create meaningful access patterns. For example, a "Stack Manager" permission set might include scopes like:

- `stack:read`
- `stack:write`
- `stack:delete`
- `stack_deployment:create`

## Default role assignments

Many scopes are automatically granted through [Pulumi-defined roles](/docs/administration/concepts/rbac/roles#pulumi-defined-roles) in Pulumi Cloud. For example:

- Organization admins have access to all scopes.
- Regular members have access to basic read and write scopes for common operations.
- Billing managers have access to billing-related scopes only.

## Available scopes

You can view the [complete catalog of scopes](/docs/administration/reference/rbac-scopes/), organized by entity type:

- [Stacks](/docs/administration/reference/rbac-scopes/stacks/)
- [Environments](/docs/administration/reference/rbac-scopes/environments/)
- [Cloud accounts](/docs/administration/reference/rbac-scopes/insights-accounts/)
- [Organization settings](/docs/administration/reference/rbac-scopes/org-settings/)

## Related resources

- [Permission sets](/docs/administration/concepts/rbac/permission-sets): Reusable bundles of related scopes for a single entity type. You grant them on entities or use them to set a role's organization access level.
- [Entities and organization-level access](/docs/administration/concepts/rbac/entities): The objects that permission sets are granted on (stacks, environments, and cloud accounts), plus the organization-level access that governs org-wide operations.
- [Roles](/docs/administration/concepts/rbac/roles): Collections of permission sets applied to entities and combined with an organization access level. You assign a role to users, teams, and machine tokens.
- [Teams](/docs/administration/concepts/rbac/teams): Groups of users that can be assigned roles and entity access. Each member inherits the union of the team's roles on top of their own role.
