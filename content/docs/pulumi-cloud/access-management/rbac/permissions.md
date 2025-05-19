---
title_tag: "Pulumi Cloud: Permissions"
meta_desc: Learn about permissions in Pulumi Cloud and how they control access to resources
title: "Permissions"
h1: "Permissions"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: Permissions
    parent: pulumi-cloud-access-management-rbac
    weight: 3
    identifier: pulumi-cloud-access-management-rbac-permissions
---

Permissions in Pulumi Cloud are predefined bundles of [scopes](../scopes) that are commonly used together. They provide a convenient way to grant related access rights to an [entity](./#entities) (resource) or set of entities (resources).

## Entities

An entity is a Pulumi object that can have permissions granted on it.

In Pulumi Cloud's authorization model, we use the term "entity" instead of "resource" to refer to such objects. This is because "resource" already has a specific meaning within Pulumi (referring to cloud infrastructure resources). We use the term "entity" to avoid confusion when discussing authorization.

### Entity types

An entity type is a category of resources that can be protected by the RBAC system. In Pulumi Cloud, entity types include stacks, environments, insights accounts, teams, and organization settings. Each entity type has its own set of associated permissions and can be managed independently through the RBAC system.

When creating a permission, it must be of a specific entity type, and only include scopes that are also of that entity type.

There are four qualified entity types in Pulumi, these are:

* **Stacks**: For all operations that affect stacks. Includes:
  * Stack updates
  * Stack configurations
  * Deployment settings
  * Stack tags and annotations
  * Stack webhooks
  * Stack schedules
* **Environments**: For all operations that affect environments. Includes:
  * Environment configurations
  * Environment secrets
  * Environment schedules
  * Environment webhooks
  * Environment versions
* **Insights accounts**: For all operations that affect insights accounts. Includes:
  * Insights accounts
  * Policy evaluations
  * Scan configurations
  * Results and reports
* **Organization settings**: For scopes and permissions that operate at the org level, like billing settings or managing third-party integrations. Includes:
  * Organization settings
  * Member management
  * Billing and usage
  * Audit logs
  * Integration configurations

## Default Permissions

Pulumi Cloud provides several default permissions that you can use to quickly get started:

### Stack Permissions

| Permission | Description | Included Scopes |
|------------|-------------|----------------|
| `read` | Basic read-only access to stacks. Allows for running previews. | `stack:read` |
| `write` | Ability to update stack configurations and run stack updates. | `stack:read`, `stack:write` |
| `admin` | Grants full control over stack operations. | `stack:read`, `stack:write`, `stack:delete` |

### Environment Permissions

| Permission | Description | Included Scopes |
|------------|-------------|----------------|
| `read` | Basic read-only access to environments | `environment:read` |
| `open` | Ability to access environment resources | `environment:read`, `environment:open` |
| `write` | Ability to modify environment settings | `environment:read`, `environment:open`, `environment:write` |
| `admin` | Full control over environment operations | All environment scopes |


### Insights Account Permissions

| Permission | Description | Included Scopes |
|------------|-------------|----------------|
| `read` | Basic read-only access to insights accounts | `environment:read` |
| `write` | Ability to modify insights accounts | `environment:read`, `environment:open`, `environment:write` |
| `admin` | Full control over insights accounts | All environment scopes |

## Custom Permissions

### Creating Custom Permissions

## Related Resources

- [Teams](/docs/pulumi-cloud/access-management/rbac/teams)
- [Roles](/docs/pulumi-cloud/access-management/rbac/roles)
- [Scopes](/docs/pulumi-cloud/access-management/rbac/scopes)
