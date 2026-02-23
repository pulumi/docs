---
title_tag: "Pulumi Cloud: RBAC Scopes - Stacks"
meta_desc: Learn about the available RBAC scopes in Pulumi Cloud.
title: "RBAC Scopes"
h1: "RBAC Scopes"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  administration:
    name: "Stacks"
    parent: administration-access-identity-rbac-scopes
    weight: 4
    identifier: pulumi-cloud-access-management-rbac-scopes-stacks
aliases:
- /docs/intro/pulumi-service/scopes/stacks
- /docs/intro/pulumi-cloud/scopes/stacks
- /docs/pulumi-cloud/access-management/rbac/scopes/stacks/
---

This document defines all the available [scopes](../) in Pulumi Cloud assignable to specific stacks or sets of stacks.

Note that creating, listing, or restoring stacks are organization-level operations, and these scopes can be found in the [organization settings scopes](../org-settings).

## Stacks

| Value | Description |
|-------|-------------|
| `stack:cancel_update` | Cancel an ongoing stack update operation. This halts the current deployment or update process.<br><br>**Granted by default permission set**: `Stack Write` |
| `stack:decrypt` | Decrypt sensitive stack data. This allows viewing encrypted configuration values and secrets.<br><br>**Granted by default permission set**: `Stack Read` |
| `stack:delete` | Delete a stack and its associated resources. This permanently removes the stack from the organization.<br><br>**Granted by default permission set**: `Stack Admin` |
| `stack:encrypt` | Encrypt stack data. This secures sensitive information within the stack.<br><br>**Granted by default permission set**: `Stack Read` |
| `stack:export` | Export stack data and configurations. This allows creating backups or migrating stacks.<br><br>**Granted by default permission set**: `Stack Read` |
| `stack:import` | Import resources into a stack. This allows bringing external resources under management.<br><br>**Granted by default permission set**: `Stack Write` |
| `stack:read` | View stack configurations and settings. This provides read-only access to stack details and parameters.<br><br>**Granted by default permission set**: `Stack Read` |
| `stack:rename` | Change the name of a stack. This updates the stack's display name across the platform.<br><br>**Granted by default permission set**: `Stack Admin` |
| `stack:transfer` | Transfer ownership of a stack to another organization or user. This is used for organizational restructuring or migration.<br><br>**Granted by default permission set**: `Stack Admin` |
| `stack:write` | Modify stack configurations and settings. This allows updating stack parameters and resource definitions.<br><br>**Granted by default permission set**: `Stack Write` |

## Stack Deployments

| Value | Description |
|-------|-------------|
| `stack_deployment_cache:read` | View the deployment cache for a stack. This includes access to cached deployment artifacts and data.<br><br>**Granted by default permission set**: `Stack Write` |
| `stack_deployment:create` | Create a new deployment for a stack. This initiates the deployment process for infrastructure resources.<br><br>**Granted by default permission set**: `Stack Write` |
| `stack_deployment:read` | View details of stack deployments. This includes access to deployment status and history.<br><br>**Granted by default permission set**: `Stack Read` |
| `stack_deployment_settings:encrypt` | Encrypt deployment settings for a stack. This secures sensitive configuration data.<br><br>**Granted by default permission set**: `Stack Write` |
| `stack_deployment_settings:read` | View deployment settings for a stack. This includes access to configuration parameters and metadata.<br><br>**Granted by default permission set**: `Stack Read` |
| `stack_deployment_settings:write` | Modify deployment settings for a stack. This allows updating configuration parameters and metadata.<br><br>**Granted by default permission set**: `Stack Write` |

## Stack Deploy Schedules

| Value | Description |
|-------|-------------|
| `stack_schedule:create` | Create a new schedule for automated stack deployments. This allows setting up recurring deployment tasks.<br><br>**Granted by default permission set**: `Stack Write` |
| `stack_schedule:delete` | Delete an existing stack deployment schedule. This permanently removes the scheduled task.<br><br>**Granted by default permission set**: `Stack Write` |
| `stack_schedule:pause` | Pause a scheduled stack deployment. This temporarily halts the scheduled deployment process.<br><br>**Granted by default permission set**: `Stack Write` |
| `stack_schedule:read` | View stack deployment schedule configurations. This includes access to schedule details and execution history.<br><br>**Granted by default permission set**: `Stack Read` |
| `stack_schedule:resume` | Resume a paused stack deployment schedule. This restores automated deployment operations.<br><br>**Granted by default permission set**: `Stack Write` |
| `stack_schedule:update` | Modify an existing stack deployment schedule. This allows updating timing, frequency, and other schedule parameters.<br><br>**Granted by default permission set**: `Stack Write` |

## Stack Tags

| Value | Description |
|-------|-------------|
| `stack_tags:update` | Update tags associated with a stack. This helps in organizing and categorizing stack resources.<br><br>**Granted by default permission set**: `Stack Write` |

## Stack Webhooks

| Value | Description |
|-------|-------------|
| `stack_webhook:create` | Create a new webhook for stack events. This enables integration with external systems for event notifications.<br><br>**Granted by default permission set**: `Stack Write` |
| `stack_webhook:delete` | Delete an existing stack webhook. This removes the integration and stops event delivery.<br><br>**Granted by default permission set**: `Stack Write` |
| `stack_webhook:read` | View stack webhook configurations. This includes access to webhook endpoints and event triggers.<br><br>**Granted by default permission set**: `Stack Write` |
| `stack_webhook:update` | Modify an existing stack webhook. This allows updating endpoint URLs and event subscriptions.<br><br>**Granted by default permission set**: `Stack Write` |
