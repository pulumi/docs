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

var insightsAccountPermissionSetRead = []Permission{
	InsightsAccountRead, InsightsAccountScanRead, InsightsAccountAccessRead,
}

var insightsAccountPermissionSetWrite = append(insightsAccountPermissionSetRead,
	InsightsAccountUpdatePolicyResults, InsightsAccountUpdate, InsightsAccountScan, InsightsAccountScanUpdate,
	InsightsAccountScanCancel, InsightsAccountScanPause, InsightsAccountScanResume,
)

var insightsAccountPermissionSetAdmin = append(insightsAccountPermissionSetWrite,
	InsightsAccountDelete, InsightsAccountAccessUpdate,
)

### Stack Permissions

| Permission | Description | Included Scopes |
|------------|-------------|----------------|
| `Stack Read` | Basic read-only access to stacks. Allows for running previews. | `stack:read`, `stack:export`, `stack:encrypt`, `stack:decrypt`, `stack_deployment:read`, `stack_deployment_settings:read`, `stack_access:read`, `stack_annotations:read`, `stack_schedule:read` |
| `Stack Write` | Ability to update stack configurations and run stack updates. | Stack Read, + `stack:import`, `stack:cancel_update`, `stack:write`, `stack_deployment_settings:write`, `stack_deployment_settings:encrypt`, `stack_deployment_cache:read`, `stack_tags:update`, `stack_annotations:update`, `stack_schedule:update`, `stack_schedule:create`, `stack_schedule:pause`, `stack_schedule:resume`, `stack_schedule:delete`, `stack_deployment:create`, `stack_webhook:create`, `stack_webhook:update`, `stack_webhook:delete`, `stack_webhook:read` |
| `Stack Admin` | Grants full control over stack operations. | Stack Write, + `stack:delete`, `stack_access:update`, `stack:transfer`, `stack:rename` |

### Environment Permissions

| Permission | Description | Included Scopes |
|------------|-------------|----------------|
| `Environment Read` | Basic read-only access to environments | `environment:read`, `environment:rotate_history`, `environment_version:read`, `environment_schedule:read`, `environment_tag:read` |
| `Environment Open` | Ability to access environment resources | Environment Read, + `environment:open`, `environment:clone`, `environment:read_decrypt`, `environment_version:read_decrypt`, `environment_version:open` |
| `Environment Write` | Ability to modify environment settings | Environment Open, + `environment:write`, `environment:rotate`, `environment_version:create`, `environment_version:update`, `environment_version:delete`, `environment_version:retract`, `environment_tag:create`, `environment_tag:update`, `environment_tag:delete`, `environment_schedule:create`, `environment_schedule:update`, `environment_schedule:pause`, `environment_schedule:resume`, `environment_schedule:delete`, `environment_webhook:read`, `environment_webhook:create`, `environment_webhook:update`, `environment_webhook:delete` |
| `Environment Admin` | Full control over environment operations | Environment Write, + `environment:delete` |


### Insights Account Permissions

| Permission | Description | Included Scopes |
|------------|-------------|----------------|
| `Account Read` | Basic read-only access to insights accounts | `insights_account:read`, `insights_account_scan:read`, `insights_account_access:read` |
| `Account Write` | Ability to modify insights accounts | Account Read, + `insights_account:update_policy_results`, `insights_account:update`, `insights_account:scan`, `insights_account_scan:update`, `insights_account_scan:cancel`, `insights_account_scan:pause`, `insights_account_scan:resume` |
| `Account Admin` | Full control over insights accounts | Account Write, + `insights_account:delete`, `insights_account_access:update` |

## Custom Permissions

### Creating Custom Permissions

## Related Resources

- [Teams](/docs/pulumi-cloud/access-management/rbac/teams)
- [Roles](/docs/pulumi-cloud/access-management/rbac/roles)
- [Scopes](/docs/pulumi-cloud/access-management/rbac/scopes)
