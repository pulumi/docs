---
title_tag: "Pulumi Cloud: Permission sets"
meta_desc: Learn about permission sets in Pulumi Cloud and how they control access to resources
title: "Permission Sets"
h1: "Permission Sets"
menu:
  administration:
    name: Permission sets
    parent: administration-access-identity-rbac
    weight: 2
    identifier: pulumi-cloud-access-management-rbac-permission-sets
aliases:
- /docs/administration/access-identity/rbac/permissions/
- /docs/pulumi-cloud/access-management/rbac/permissions/
---

Permission sets in Pulumi Cloud are predefined bundles of [scopes](/docs/administration/access-identity/rbac/scopes) that are commonly used together. They provide a convenient way to grant related access rights to an [entity](/docs/administration/access-identity/rbac/entities) (resource) or set of entities (resources).

Every permission set belongs to a specific [entity type](/docs/administration/access-identity/rbac/entities#entity-types) (stacks, environments, or insights accounts) and can only include scopes of that same type.

## Default permission sets

Pulumi Cloud provides several default permission sets that you can use to quickly get started:

### Stack permission sets

| Permission set | Description | Included Scopes |
|------------|-------------|----------------|
| `Stack Read` | Basic read-only access to stacks. Allows for running previews. | `stack:read`, `stack:export`, `stack:encrypt`, `stack:decrypt`, `stack_deployment:read`, `stack_deployment_settings:read`, `stack_access:read`, `stack_schedule:read` |
| `Stack Write` | Ability to update stack configurations and run stack updates. | Stack Read, + `stack:import`, `stack:cancel_update`, `stack:write`, `stack_deployment_settings:write`, `stack_deployment_settings:encrypt`, `stack_deployment_cache:read`, `stack_tags:update`, `stack_schedule:update`, `stack_schedule:create`, `stack_schedule:pause`, `stack_schedule:resume`, `stack_schedule:delete`, `stack_deployment:create`, `stack_webhook:create`, `stack_webhook:update`, `stack_webhook:delete`, `stack_webhook:read` |
| `Stack Admin` | Grants full control over stack operations. | Stack Write, + `stack:delete`, `stack_access:update`, `stack:transfer`, `stack:rename` |

### Environment permission sets

| Permission set | Description | Included Scopes |
|------------|-------------|----------------|
| `Environment Read` | Basic read-only access to environments. | `environment:read`, `environment:rotate_history`, `environment_version:read`, `environment_schedule:read`, `environment_tag:read` |
| `Environment Open` | Ability to read the environment and access environment secrets. | Environment Read, + `environment:open`, `environment:clone`, `environment_version:open`, `environment_version:read` |
| `Environment Write` | Ability to modify environment settings. | Environment Open, + `environment:write`, `environment:rotate`, `environment_version:create`, `environment_version:update`, `environment_version:delete`, `environment_version:retract`, `environment_tag:create`, `environment_tag:update`, `environment_tag:delete`, `environment_schedule:create`, `environment_schedule:update`, `environment_schedule:pause`, `environment_schedule:resume`, `environment_schedule:delete`, `environment_webhook:read`, `environment_webhook:create`, `environment_webhook:update`, `environment_webhook:delete` |
| `Environment Admin` | Full control over environment operations. | Environment Write, + `environment:delete` |

### Insights account permission sets

| Permission set | Description | Included Scopes |
|------------|-------------|----------------|
| `Account Read` | Basic read-only access to insights accounts. | `insights_account:read`, `insights_account_scan:read`, `insights_account_access:read` |
| `Account Write` | Ability to modify insights accounts. | Account Read, + `insights_account:update`, `insights_account:scan`, `insights_account_scan:update`, `insights_account_scan:cancel`, `insights_account_scan:pause`, `insights_account_scan:resume` |
| `Account Admin` | Full control over insights accounts. | Account Write, + `insights_account:delete`, `insights_account_access:update` |

### Organization settings permission sets

These permission sets bundle organization-level (global) scopes. Rather than granting access to a specific [entity](/docs/administration/access-identity/rbac/entities), they set a role's [organization access level](/docs/administration/access-identity/rbac/entities#organization-level-access) — the permissions for org-wide operations such as billing, member management, and creating resources.

| Permission set | Description | Included Scopes |
|------------|-------------|----------------|
| `Read Only` | View-only organization access: usage, members, stacks, environments, teams, and Insights accounts; read deployments, integrations, services, templates, and resources. No create, update, or delete. | `ai_conversations:read`, `deployments:read`, `deployments:read_usage`, `environment:list_deleted`, `environment_tags:list`, `policy_groups:read`, `policy_pack:read`, `policy_results:read`, `integrations:read`, `org_member:read`, `organization_annotations:read`, `organization:read_usage`, `project_annotations:read`, `resources:dashboard`, `resources:search`, `saml:read`, `tags:read`, `team:read`, `templates:read`, `services:read` |
| `Standard` | Member-level organization access: everything `Read Only` allows, plus creating environments and using deployments, integrations, services, and resources. Excludes billing and member or organization admin settings. (Creating stacks, teams, and Insights accounts is governed separately by the org-wide capability toggles, not this permission set.) | Read Only, + `ai_conversations:create`, `ai_conversations:update`, `environment:create`, `integrations:update`, `project_annotations:update`, `project:decrypt`, `project:encrypt`, `services:create`, `services:write`, `services:admin`, `insights_policy_evaluator:read`, `insights_policy_evaluator:delete`, `insights_policy_evaluator:ensure`, `insights_policy_evaluator:update`, `insights_policy_queue:read` |
| `Organization Settings Billing` | Billing access. | `deployments:read_usage`, `org_member:read`, `organization:billing`, `organization:read_usage`, `resources:dashboard`, `saml:read`, `team:read` |

## Custom permission sets

{{% notes "info" %}}
Custom permission sets are only available to organizations using Pulumi Enterprise Edition and Pulumi Business Critical Edition.
To learn more about editions visit the [pricing page](/pricing/).
{{% /notes %}}

To create a custom permission set, you must be an organization admin.

1. Visit **Settings** > **Access management** and select the **Permission sets** tab.
1. To create a new permission set, select **Create custom permission set** within the associated entity group.
1. Provide a unique name for the permission set. Optionally, but recommended, provide a description to contextualize the permission set and its purpose.
1. Select the scopes you would like to bundle within this permission set.
1. Select **Create permission set**. The panel closes and your new permission set appears on the permission sets page.

You can now assign this custom permission set to roles within your organization.

{{% notes "info" %}}
A custom permission set cannot be deleted while it is in use by one or more roles. Remove the permission set from those roles before deleting it.
{{% /notes %}}

## Related resources

* [Scopes](/docs/administration/access-identity/rbac/scopes): The most granular access rights in Pulumi Cloud, written as `object:action`. Each scope belongs to one entity type and is the building block of permission sets.
* [Entities and organization-level access](/docs/administration/access-identity/rbac/entities): The objects that permission sets are granted on (stacks, environments, and Insights accounts), plus the organization-level access that governs org-wide operations.
* [Roles](/docs/administration/access-identity/rbac/roles): Collections of permission sets applied to entities and combined with an organization access level. You assign a role to users, teams, and machine tokens.
* [Teams](/docs/administration/access-identity/rbac/teams): Groups of users that can be assigned roles and entity access. Each member inherits the union of the team's roles on top of their own role.
