---
title_tag: "Pulumi Cloud: RBAC Scopes - Environments"
meta_desc: Learn about the available RBAC scopes in Pulumi Cloud.
title: "RBAC Scopes: Environments"
h1: "RBAC Scopes: Environments"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  administration:
    name: "Environments"
    parent: administration-access-identity-rbac-scopes
    weight: 4
    identifier: pulumi-cloud-access-management-rbac-scopes-environments
aliases:
- /docs/intro/pulumi-service/scopes/environments
- /docs/intro/pulumi-cloud/scopes/environments
- /docs/pulumi-cloud/access-management/rbac/scopes/environments/
---

This document defines all the available [scopes](../) in Pulumi Cloud assignable to specific environments or sets of environments.

Note that creating, listing, or restoring environments are organization-level operations, and these scopes can be found in the [organization settings scopes](../org-settings).

## Environments

| Value | Description |
|-------|-------------|
| `environment:clone` | Create a copy of an existing environment with all its configurations. This is useful for creating staging or testing environments.<br><br>**Granted by default permission set**: `Environment Open` |
| `environment:delete` | Remove an environment and its associated resources. This permanently deletes the environment and its configurations.<br><br>**Granted by default permission set**: `Environment Admin` |
| `environment:open` | Access and interact with an environment's resources. This includes the ability to view and modify environment configurations.<br><br>**Granted by default permission set**: `Environment Open` |
| `environment:read` | View environment configurations and settings. This provides read-only access to environment details and parameters.<br><br>**Granted by default permission set**: `Environment Read` |
| `environment:write` | Modify environment configurations and settings. This allows updating environment parameters and resource definitions.<br><br>**Granted by default permission set**: `Environment Write` |

## Environment Secrets Rotation

| Value | Description |
|-------|-------------|
| `environment:rotate` | Initiate a rotation of secrets and credentials in an environment. This is a security measure to regularly update sensitive information.<br><br>**Granted by default permission set**: `Environment Write` |
| `environment:rotate_history` | View the history of secret rotations for an environment. This provides an audit trail of when secrets were last changed.<br><br>**Granted by default permission set**: `Environment Read` |

## Environment Schedules

| Value | Description |
|-------|-------------|
| `environment_schedule:create` | Create a new schedule for automated environment operations. This allows setting up recurring tasks and maintenance windows.<br><br>**Granted by default permission set**: `Environment Write` |
| `environment_schedule:delete` | Remove an existing environment schedule. This permanently deletes the scheduled task and its configuration.<br><br>**Granted by default permission set**: `Environment Write` |
| `environment_schedule:pause` | Temporarily suspend an environment schedule. This halts automated operations without deleting the schedule.<br><br>**Granted by default permission set**: `Environment Write` |
| `environment_schedule:read` | View environment schedule configurations and status. This includes access to schedule details and execution history.<br><br>**Granted by default permission set**: `Environment Read` |
| `environment_schedule:resume` | Resume a paused environment schedule. This restores automated operations according to the schedule.<br><br>**Granted by default permission set**: `Environment Write` |
| `environment_schedule:update` | Modify an existing environment schedule. This allows updating timing, frequency, and other schedule parameters.<br><br>**Granted by default permission set**: `Environment Write` |

## Environment Tags

| Value | Description |
|-------|-------------|
| `environment_tag:create` | Add a new tag to an environment. This helps in organizing and categorizing environments.<br><br>**Granted by default permission set**: `Environment Write` |
| `environment_tag:delete` | Remove a tag from an environment. This allows cleaning up or reorganizing environment categorization.<br><br>**Granted by default permission set**: `Environment Write` |
| `environment_tag:read` | View tags associated with environments. This provides access to environment categorization and metadata.<br><br>**Granted by default permission set**: `Environment Read` |
| `environment_tag:update` | Modify existing environment tags. This allows updating tag values and metadata.<br><br>**Granted by default permission set**: `Environment Write` |

## Environment Versions

| Value | Description |
|-------|-------------|
| `environment_version:create` | Create a new version of an environment. This allows tracking changes and maintaining environment history.<br><br>**Granted by default permission set**: `Environment Write` |
| `environment_version:delete` | Remove a specific version of an environment. This permanently deletes the version and its configurations.<br><br>**Granted by default permission set**: `Environment Write` |
| `environment_version:open` | Access and interact with a specific environment version. This includes viewing and using version-specific configurations.<br><br>**Granted by default permission set**: `Environment Open` |
| `environment_version:read` | View details of a specific environment version. This provides access to version-specific configurations and metadata.<br><br>**Granted by default permission set**: `Environment Open` |
| `environment_version:retract` | Mark a specific environment version as invalid or deprecated. This prevents its use while maintaining history.<br><br>**Granted by default permission set**: `Environment Write` |
| `environment_version:update` | Modify an existing environment version. This allows updating version-specific configurations and metadata.<br><br>**Granted by default permission set**: `Environment Write` |

## Environment Webhooks

| Value | Description |
|-------|-------------|
| `environment_webhook:create` | Create a new webhook for environment events. This enables integration with external systems and automation.<br><br>**Granted by default permission set**: `Environment Write` |
| `environment_webhook:delete` | Remove an existing environment webhook. This permanently deletes the webhook configuration.<br><br>**Granted by default permission set**: `Environment Write` |
| `environment_webhook:read` | View environment webhook configurations. This includes access to webhook settings and event triggers.<br><br>**Granted by default permission set**: `Environment Write` |
| `environment_webhook:update` | Modify an existing environment webhook. This allows updating webhook settings and event triggers.<br><br>**Granted by default permission set**: `Environment Write` |
