---
title_tag: "Pulumi Cloud: Scopes"
meta_desc: Learn about scopes in Pulumi Cloud and how they control access to resources
title: "Scopes"
h1: "Scopes"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: Scopes
    parent: pulumi-cloud-access-management-rbac
    weight: 4
    identifier: pulumi-cloud-access-management-rbac-scopes
aliases:
- /docs/intro/pulumi-service/scopes/
- /docs/intro/pulumi-cloud/scopes/
---

This document defines all the available scopes in Pulumi Cloud, organized by resource type and group.

## Type: Organization settings

### AI

#### AI Conversations Create

| Property | Value |
|----------|-------|
| Value | `ai_conversations:create` |
| Type | Organization settings |
| Granted by roles | `MemberRole`, `AdminRole` |
| Granted by permissions | N/A |

Create a new AI conversation session for interacting with Pulumi's AI assistant. This allows users to start new conversations and get help with their infrastructure code.

#### AI Conversations List All

| Property | Value |
|----------|-------|
| Value | `ai_conversations:list_all` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

View all AI conversations across the organization. This provides administrators with visibility into all AI assistant interactions.

#### AI Conversations Read

| Property | Value |
|----------|-------|
| Value | `ai_conversations:read` |
| Type | Organization settings |
| Granted by roles | `MemberRole`, `AdminRole` |
| Granted by permissions | N/A |

Access and view the content of AI conversations. This allows users to read their own conversations and continue previous interactions.

#### AI Conversations Update

| Property | Value |
|----------|-------|
| Value | `ai_conversations:update` |
| Type | Organization settings |
| Granted by roles | `MemberRole`, `AdminRole` |
| Granted by permissions | N/A |

Modify and continue existing AI conversations. This enables users to update their conversations with new questions or context.

### Agent Pools

#### Agent Pool Create

| Property | Value |
|----------|-------|
| Value | `agent_pool:create` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Create a new agent pool for running Pulumi operations. Agent pools provide isolated environments for executing infrastructure deployments.

#### Agent Pool Delete

| Property | Value |
|----------|-------|
| Value | `agent_pool:delete` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Remove an existing agent pool and its associated resources. This permanently deletes the pool and its configuration.

#### Agent Pool Read

| Property | Value |
|----------|-------|
| Value | `agent_pool:read` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

View agent pool configurations and status. This includes access to pool settings, agent status, and operational metrics.

#### Agent Pool Update

| Property | Value |
|----------|-------|
| Value | `agent_pool:update` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Modify agent pool settings and configurations. This allows updating pool parameters, scaling settings, and agent configurations.

### Audit Logs

#### Audit Logs Export

| Property | Value |
|----------|-------|
| Value | `audit_logs:export` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Export audit log data for compliance and analysis purposes. This enables downloading audit records in various formats.

#### Audit Logs Read

| Property | Value |
|----------|-------|
| Value | `audit_logs:read` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Access and view audit logs of organization activities. This provides visibility into system events and user actions.

### OIDC

#### Auth Policies Read

| Property | Value |
|----------|-------|
| Value | `auth_policies:read` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

View authentication policy configurations. This includes access to OIDC, SAML, and other identity provider settings.

#### Auth Policies Update

| Property | Value |
|----------|-------|
| Value | `auth_policies:update` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Modify authentication policies and identity provider settings. This allows updating security configurations and access rules.

### Org Deployments

#### Deployments Pause

| Property | Value |
|----------|-------|
| Value | `deployments:pause` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Temporarily halt all deployment operations across the organization. This is useful for maintenance or emergency situations.

#### Deployments Read

| Property | Value |
|----------|-------|
| Value | `deployments:read` |
| Type | Organization settings |
| Granted by roles | `MemberRole`, `AdminRole` |
| Granted by permissions | N/A |

View deployment configurations and status across the organization. This provides visibility into all deployment activities.

#### Deployments Read Usage

| Property | Value |
|----------|-------|
| Value | `deployments:read_usage` |
| Type | Organization settings |
| Granted by roles | `MemberRole`, `AdminRole`, BillingManagerRole |
| Granted by permissions | N/A |

Access deployment usage metrics and statistics. This includes information about resource consumption and operational costs.

#### Deployments Resume

| Property | Value |
|----------|-------|
| Value | `deployments:resume` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Resume deployment operations after a pause. This restores normal deployment functionality across the organization.

### Teams

#### Github Team Create

| Property | Value |
|----------|-------|
| Value | `github_team:create` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Create a new team that syncs with GitHub. This enables integration between Pulumi and GitHub team structures.

### IaC Policy

#### IaC Policy Groups Create

| Property | Value |
|----------|-------|
| Value | `iac_policy_groups:create` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Create a new group of Infrastructure as Code policies. This allows organizing related policies for better management and enforcement.

#### IaC Policy Groups Delete

| Property | Value |
|----------|-------|
| Value | `iac_policy_groups:delete` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Remove an existing group of Infrastructure as Code policies. This permanently deletes the policy group and its configurations.

#### IaC Policy Groups Read

| Property | Value |
|----------|-------|
| Value | `iac_policy_groups:read` |
| Type | Organization settings |
| Granted by roles | `MemberRole`, `AdminRole` |
| Granted by permissions | N/A |

View Infrastructure as Code policy group configurations. This includes access to policy definitions and enforcement rules.

#### IaC Policy Groups Update

| Property | Value |
|----------|-------|
| Value | `iac_policy_groups:update` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Modify Infrastructure as Code policy group settings. This allows updating policy definitions and enforcement parameters.

#### IaC Policy Pack Create

| Property | Value |
|----------|-------|
| Value | `iac_policy_pack:create` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Create a new Infrastructure as Code policy pack. This allows bundling related policies for deployment and enforcement.

#### IaC Policy Pack Delete

| Property | Value |
|----------|-------|
| Value | `iac_policy_pack:delete` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Remove an existing Infrastructure as Code policy pack. This permanently deletes the policy pack and its configurations.

#### IaC Policy Pack Read

| Property | Value |
|----------|-------|
| Value | `iac_policy_pack:read` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

View Infrastructure as Code policy pack contents. This includes access to policy definitions and enforcement rules.

#### IaC Policy Pack Update

| Property | Value |
|----------|-------|
| Value | `iac_policy_pack:update` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Modify an existing Infrastructure as Code policy pack. This allows updating policy definitions and enforcement parameters.

#### IaC Policy Results Read

| Property | Value |
|----------|-------|
| Value | `iac_policy_results:read` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

View results of Infrastructure as Code policy evaluations. This provides insights into policy compliance and violations.

### Organization

#### Integrations Read

| Property | Value |
|----------|-------|
| Value | `integrations:read` |
| Type | Organization settings |
| Granted by roles | `MemberRole`, `AdminRole` |
| Granted by permissions | N/A |

View integration configurations for the organization. This includes access to settings for third-party services and tools.

#### Integrations Update

| Property | Value |
|----------|-------|
| Value | `integrations:update` |
| Type | Organization settings |
| Granted by roles | `MemberRole`, `AdminRole` |
| Granted by permissions | N/A |

Modify integration settings for the organization. This allows updating or reconfiguring third-party service connections.

### Membership

#### Invites Create

| Property | Value |
|----------|-------|
| Value | `invites:create` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Send invitations to new users to join the organization. This enables onboarding of new team members.

#### Invites Read

| Property | Value |
|----------|-------|
| Value | `invites:read` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

View pending and sent invitations for organization membership. This provides visibility into user onboarding status.

### OIDC

#### OIDC Issuers Create

| Property | Value |
|----------|-------|
| Value | `oidc_issuers:create` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Register a new OIDC issuer for authentication. This allows adding new identity providers for user login.

#### OIDC Issuers Delete

| Property | Value |
|----------|-------|
| Value | `oidc_issuers:delete` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Remove an existing OIDC issuer. This permanently deletes the identity provider configuration.

#### OIDC Issuers Read

| Property | Value |
|----------|-------|
| Value | `oidc_issuers:read` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

View OIDC issuer configurations. This includes access to identity provider details and settings.

#### OIDC Issuers Regenerate Thumbprints

| Property | Value |
|----------|-------|
| Value | `oidc_issuers:regenerate_thumbprints` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Regenerate security thumbprints for an OIDC issuer. This is used to maintain secure authentication.

#### OIDC Issuers Update

| Property | Value |
|----------|-------|
| Value | `oidc_issuers:update` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Modify OIDC issuer settings. This allows updating identity provider details and authentication parameters.

### Organization

#### Org Integrations Read

| Property | Value |
|----------|-------|
| Value | `org_integrations:read` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

View organization-level integration settings. This includes access to all configured integrations.

#### Org Integrations Update

| Property | Value |
|----------|-------|
| Value | `org_integrations:update` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Update organization-level integration settings. This allows modifying or removing integrations.

### Membership

#### Org Member Access

| Property | Value |
|----------|-------|
| Value | `org_member:access` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Access organization member details and permissions. This is used for managing user roles and access.

#### Org Member Add

| Property | Value |
|----------|-------|
| Value | `org_member:add` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Add a new member to the organization. This enables expanding the team with new users.

#### Org Member Delete

| Property | Value |
|----------|-------|
| Value | `org_member:delete` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Remove a member from the organization. This revokes their access and permissions.

#### Org Member Read

| Property | Value |
|----------|-------|
| Value | `org_member:read` |
| Type | Organization settings |
| Granted by roles | `MemberRole`, `AdminRole`, BillingManagerRole |
| Granted by permissions | N/A |

View details about organization members. This includes access to user profiles and roles.

#### Org Member Set Admin

| Property | Value |
|----------|-------|
| Value | `org_member:set_admin` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Grant or revoke admin privileges for an organization member. This controls elevated access.

#### Org Member Update

| Property | Value |
|----------|-------|
| Value | `org_member:update` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Update organization member information and roles. This allows changing user details and permissions.

#### Org Requests Create

| Property | Value |
|----------|-------|
| Value | `org_requests:create` |
| Type | Organization settings |
| Granted by roles | N/A |
| Granted by permissions | N/A |

Submit a new request to join or interact with the organization. This is used for onboarding or special access.

#### Org Requests Read

| Property | Value |
|----------|-------|
| Value | `org_requests:read` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

View all organization requests. This provides visibility into pending and processed requests.

#### Org Requests Status

| Property | Value |
|----------|-------|
| Value | `org_requests:status` |
| Type | Organization settings |
| Granted by roles | N/A |
| Granted by permissions | N/A |

Check the status of an organization request. This helps track onboarding or access progress.

#### Org Requests Update

| Property | Value |
|----------|-------|
| Value | `org_requests:update` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Update or process organization requests. This allows approving or denying requests.

### Organization Tokens

#### Org Token Create

| Property | Value |
|----------|-------|
| Value | `org_token:create` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Create a new organization API token. This enables programmatic access to organization resources.

#### Org Token Delete

| Property | Value |
|----------|-------|
| Value | `org_token:delete` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Delete an existing organization API token. This revokes programmatic access.

#### Org Token Read

| Property | Value |
|----------|-------|
| Value | `org_token:read` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

View organization API tokens. This includes access to token details and usage.

### Annotations

#### Organization Annotations Read

| Property | Value |
|----------|-------|
| Value | `organization_annotations:read` |
| Type | Organization settings |
| Granted by roles | `MemberRole`, `AdminRole` |
| Granted by permissions | N/A |

View annotations attached to the organization. This provides context and metadata for organizational resources.

#### Organization Annotations Update

| Property | Value |
|----------|-------|
| Value | `organization_annotations:update` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Modify or add annotations to the organization. This allows updating organizational metadata.

### Organization

#### Organization Billing

| Property | Value |
|----------|-------|
| Value | `organization:billing` |
| Type | Organization settings |
| Granted by roles | `AdminRole`, BillingManagerRole |
| Granted by permissions | N/A |

Manage billing settings and payment methods for the organization. This includes access to invoices and payment history.

#### Organization Change Backend

| Property | Value |
|----------|-------|
| Value | `organization:change_backend` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Change the backend infrastructure for the organization. This is used for advanced configuration and migration.

#### Organization Delete

| Property | Value |
|----------|-------|
| Value | `organization:delete` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Delete the organization and all its resources. This is a permanent and irreversible action.

#### Organization Read

| Property | Value |
|----------|-------|
| Value | `organization:read` |
| Type | Organization settings |
| Granted by roles | `MemberRole`, `AdminRole`, BillingManagerRole |
| Granted by permissions | N/A |

View organization details and settings. This includes access to organizational metadata and configuration.

#### Organization Read Activity

| Property | Value |
|----------|-------|
| Value | `organization:read_activity` |
| Type | Organization settings |
| Granted by roles | `MemberRole`, `AdminRole`, BillingManagerRole |
| Granted by permissions | N/A |

View recent activity and audit logs for the organization. This provides insight into changes and events.

#### Organization Read Usage

| Property | Value |
|----------|-------|
| Value | `organization:read_usage` |
| Type | Organization settings |
| Granted by roles | `MemberRole`, `AdminRole`, BillingManagerRole |
| Granted by permissions | N/A |

View usage statistics and metrics for the organization. This includes resource consumption and cost data.

#### Organization Rename

| Property | Value |
|----------|-------|
| Value | `organization:rename` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Change the name of the organization. This updates the organization's display name across the platform.

#### Organization Transfer Stacks

| Property | Value |
|----------|-------|
| Value | `organization:transfer_stacks` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Transfer ownership of stacks between organizations. This is used for organizational restructuring or migration.

#### Organization Update

| Property | Value |
|----------|-------|
| Value | `organization:update` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Update organization settings and configurations. This allows changing metadata, policies, and preferences.

### Org Webhooks

#### Organization Webhook Create

| Property | Value |
|----------|-------|
| Value | `organization_webhook:create` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Create a new webhook for organization events. This enables integration with external systems for event notifications.

#### Organization Webhook Delete

| Property | Value |
|----------|-------|
| Value | `organization_webhook:delete` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Delete an existing organization webhook. This removes the integration and stops event delivery.

#### Organization Webhook Read

| Property | Value |
|----------|-------|
| Value | `organization_webhook:read` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

View organization webhook configurations. This includes access to webhook endpoints and event triggers.

#### Organization Webhook Update

| Property | Value |
|----------|-------|
| Value | `organization_webhook:update` |
| Type | Organization settings |
| Granted by roles | `AdminRole` |
| Granted by permissions | N/A |

Modify an existing organization webhook. This allows updating endpoint URLs and event subscriptions.

## Type: Environment

### Environments

#### Environment Clone

```
environment:clone
```

**Granted by default permission**: EnvironmentPermissionBackendOpen

Create a copy of an existing environment with all its configurations. This is useful for creating staging or testing environments.

#### Environment Create

```
environment:create
```

**Granted by default roles**: `AdminRole`

Create a new environment for managing infrastructure configurations. Environments provide isolated spaces for different deployment stages.

#### Environment Decrypt

```
environment:decrypt
```

**Granted by default roles**: `AdminRole`

Access and decrypt sensitive environment data. This allows viewing encrypted configuration values and secrets.

#### Environment Delete

```
environment:delete
```

**Granted by default roles**: `AdminRole`

Remove an environment and its associated resources. This permanently deletes the environment and its configurations.

#### Environment List

```
environment:list
```

**Granted by default roles**: `AdminRole`

View all environments in the organization. This provides a list of available environments and their basic information.

#### Environment List Deleted

```
environment:list_deleted
```

**Granted by default roles**: `MemberRole`, `AdminRole`

View a list of environments that have been deleted but are still recoverable. This helps in managing and potentially restoring deleted environments.

#### Environment Open

```
environment:open
```

**Granted by default roles**: `AdminRole`

Access and interact with an environment's resources. This includes the ability to view and modify environment configurations.

#### Environment Read

```
environment:read
```

**Granted by default roles**: `AdminRole`

View environment configurations and settings. This provides read-only access to environment details and parameters.

#### Environment Restore Deleted

```
environment:restore_deleted
```

**Granted by default roles**: `AdminRole`

Recover a previously deleted environment. This restores the environment and its configurations to their previous state.

#### Environment Write

```
environment:write
```

**Granted by default roles**: `AdminRole`

Modify environment configurations and settings. This allows updating environment parameters and resource definitions.

#### Environment Yaml Open

```
environment_yaml:open
```

**Granted by default roles**: `MemberRole`, `AdminRole`

Access and view environment configuration in YAML format. This provides a structured view of environment settings.

### Environment Secrets Rotation

#### Environment Rotate

```
environment:rotate
```

**Granted by default permission**: EnvironmentPermissionBackendOpen

Initiate a rotation of secrets and credentials in an environment. This is a security measure to regularly update sensitive information.

#### Environment Rotate History

```
environment:rotate_history
```

**Granted by default permission**: EnvironmentPermissionBackendRead

View the history of secret rotations for an environment. This provides an audit trail of when secrets were last changed.

### Environment Schedules

#### Environment Schedule Create

```
environment_schedule:create
```

**Granted by default permission**: EnvironmentPermissionBackendOpen

Create a new schedule for automated environment operations. This allows setting up recurring tasks and maintenance windows.

#### Environment Schedule Delete

```
environment_schedule:delete
```

**Granted by default permission**: EnvironmentPermissionBackendOpen

Remove an existing environment schedule. This permanently deletes the scheduled task and its configuration.

#### Environment Schedule Pause

```
environment_schedule:pause
```

**Granted by default permission**: EnvironmentPermissionBackendOpen

Temporarily suspend an environment schedule. This halts automated operations without deleting the schedule.

#### Environment Schedule Read

```
environment_schedule:read
```

**Granted by default permission**: EnvironmentPermissionBackendRead

View environment schedule configurations and status. This includes access to schedule details and execution history.

#### Environment Schedule Resume

```
environment_schedule:resume
```

**Granted by default permission**: EnvironmentPermissionBackendOpen

Resume a paused environment schedule. This restores automated operations according to the schedule.

#### Environment Schedule Update

```
environment_schedule:update
```

**Granted by default permission**: EnvironmentPermissionBackendOpen

Modify an existing environment schedule. This allows updating timing, frequency, and other schedule parameters.

### Environment Tags

#### Environment Tag Create

```
environment_tag:create
```

**Granted by default permission**: EnvironmentPermissionBackendOpen

Add a new tag to an environment. This helps in organizing and categorizing environments.

#### Environment Tag Delete

```
environment_tag:delete
```

**Granted by default permission**: EnvironmentPermissionBackendOpen

Remove a tag from an environment. This allows cleaning up or reorganizing environment categorization.

#### Environment Tag Read

```
environment_tag:read
```

**Granted by default permission**: EnvironmentPermissionBackendOpen

View tags associated with environments. This provides access to environment categorization and metadata.

#### Environment Tag Update

```
environment_tag:update
```

**Granted by default permission**: EnvironmentPermissionBackendOpen

Modify existing environment tags. This allows updating tag values and metadata.

#### Environment Tags List

```
environment_tags:list
```

**Granted by default permission**: EnvironmentPermissionBackendOpen

View all tags used across environments. This provides a comprehensive view of environment categorization.

### Environment Versions

#### Environment Version Create

```
environment_version:create
```

**Granted by default permission**: EnvironmentPermissionBackendOpen

Create a new version of an environment. This allows tracking changes and maintaining environment history.

#### Environment Version Decrypt

```
environment_version:decrypt
```

**Granted by default permission**: EnvironmentPermissionBackendOpen

Access and decrypt sensitive data in an environment version. This allows viewing encrypted configuration values.

#### Environment Version Delete

```
environment_version:delete
```

**Granted by default permission**: EnvironmentPermissionBackendOpen

Remove a specific version of an environment. This permanently deletes the version and its configurations.

#### Environment Version Open

```
environment_version:open
```

**Granted by default permission**: EnvironmentPermissionBackendOpen

Access and interact with a specific environment version. This includes viewing and using version-specific configurations.

#### Environment Version Read

```
environment_version:read
```

**Granted by default permission**: EnvironmentPermissionBackendOpen

View details of a specific environment version. This provides access to version-specific configurations and metadata.

#### Environment Version Retract

```
environment_version:retract
```

**Granted by default permission**: EnvironmentPermissionBackendOpen

Mark a specific environment version as invalid or deprecated. This prevents its use while maintaining history.

#### Environment Version Update

```
environment_version:update
```

**Granted by default permission**: EnvironmentPermissionBackendOpen

Modify an existing environment version. This allows updating version-specific configurations and metadata.

### Environment Webhooks

#### Environment Webhook Create

```
environment_webhook:create
```

**Granted by default permission**: EnvironmentPermissionBackendOpen

Create a new webhook for environment events. This enables integration with external systems and automation.

#### Environment Webhook Delete

```
environment_webhook:delete
```

**Granted by default permission**: EnvironmentPermissionBackendOpen

Remove an existing environment webhook. This permanently deletes the webhook configuration.

#### Environment Webhook Read

```
environment_webhook:read
```

**Granted by default permission**: EnvironmentPermissionBackendOpen

View environment webhook configurations. This includes access to webhook settings and event triggers.

#### Environment Webhook Update

```
environment_webhook:update
```

**Granted by default permission**: EnvironmentPermissionBackendOpen

Modify an existing environment webhook. This allows updating webhook settings and event triggers.

## Type: Insights Account

### Insights Accounts

#### Insights Account Access

```
insights_account:access
```

**Granted by default permission**: InsightsAccountPermissionRead

Access and interact with an insights account. This includes basic operations and data viewing capabilities.

#### Insights Account Create

```
insights_account:create
```

**Granted by default permission**: InsightsAccountPermissionAdmin

Create a new insights account. This allows setting up monitoring and analysis capabilities for infrastructure.

#### Insights Account Delete

```
insights_account:delete
```

**Granted by default permission**: InsightsAccountPermissionAdmin

Remove an existing insights account. This permanently deletes the account and its associated data.

#### Insights Account List

```
insights_account:list
```

**Granted by default permission**: InsightsAccountPermissionRead

View all insights accounts in the organization. This provides a list of available accounts and their basic information.

#### Insights Account Read

```
insights_account:read
```

**Granted by default permission**: InsightsAccountPermissionRead

View insights account configurations and data. This includes access to monitoring settings and analysis results.

#### Insights Account Update

```
insights_account:update
```

**Granted by default permission**: InsightsAccountPermissionAdmin

Modify insights account settings and configurations. This allows updating monitoring parameters and analysis rules.

#### Insights Account Update Policy Results

```
insights_account:update_policy_results
```

**Granted by default permission**: InsightsAccountPermissionAdmin

Update policy evaluation results for an insights account. This allows refreshing compliance data and analysis.

### Insights Scan

#### Insights Account Scan

```
insights_account:scan
```

**Granted by default permission**: InsightsAccountPermissionAdmin

Initiate a new scan of an insights account. This triggers analysis of infrastructure configurations and compliance.

#### Insights Account Scan Cancel

```
insights_account:scan_cancel
```

**Granted by default permission**: InsightsAccountPermissionAdmin

Stop an ongoing insights account scan. This halts the current analysis process.

#### Insights Account Scan Pause

**Granted by default permission**: InsightsAccountPermissionAdmin

Temporarily suspend an insights account scan. This pauses the analysis process without losing progress.

#### Insights Account Scan Read

```
insights_account:scan_read
```

**Granted by default permission**: InsightsAccountPermissionRead

View insights account scan results and status. This includes access to analysis findings and progress.

#### Insights Account Scan Resume

```
insights_account:scan_resume
```

**Granted by default permission**: InsightsAccountPermissionAdmin

Resume a paused insights account scan. This continues the analysis process from where it was paused.

#### Insights Account Scan Update

```
insights_account:scan_update
```

**Granted by default permission**: InsightsAccountPermissionAdmin

Modify insights account scan settings. This allows updating scan parameters and analysis configurations.

### Insights Policy Evaluator

#### Insights Policy Evaluator Delete

```
insights_policy_evaluator:delete
```

**Granted by default permission**: InsightsAccountPermissionAdmin

Remove an existing policy evaluator. This permanently deletes the evaluator and its configurations.

#### Insights Policy Evaluator Ensure

```
insights_policy_evaluator:ensure
```

**Granted by default permission**: InsightsAccountPermissionAdmin

Create or update a policy evaluator. This ensures the evaluator exists with the correct configuration.

#### Insights Policy Evaluator Read

```
insights_policy_evaluator:read
```

**Granted by default permission**: InsightsAccountPermissionRead

View policy evaluator configurations and status. This includes access to evaluation rules and results.

#### Insights Policy Evaluator Update

```
insights_policy_evaluator:update
```

**Granted by default permission**: InsightsAccountPermissionAdmin

Modify an existing policy evaluator. This allows updating evaluation rules and parameters.

### Insights Policy Queue

#### Insights Policy Queue Read

```
insights_policy_queue:read
```

**Granted by default permission**: InsightsAccountPermissionRead

View the policy evaluation queue status. This provides visibility into pending and completed evaluations.

## Type: Stack

### Stacks

#### Stack Access

```
stack:access
```

**Granted by default roles**: `AdminRole`

**Granted by default permission**: StackPermissionWrite

Access stack resources and perform write operations. This includes updating stack configurations and deployments.

#### Stack Cancel Update

```
stack:cancel_update
```

**Granted by default permission**: StackPermissionWrite

Cancel an ongoing stack update operation. This halts the current deployment or update process.

#### Stack Create

```
stack:create
```

**Granted by default roles**: `AdminRole`

Create a new stack for managing infrastructure resources. Stacks represent isolated units of deployment.

#### Stack Decrypt

```
stack:decrypt
```

**Granted by default permission**: StackPermissionRead

Decrypt sensitive stack data. This allows viewing encrypted configuration values and secrets.

#### Stack Delete

```
stack:delete
```

**Granted by default permission**: StackPermissionWrite

Delete a stack and its associated resources. This permanently removes the stack from the organization.

#### Stack Encrypt

```
stack:encrypt
```

**Granted by default permission**: StackPermissionRead

Encrypt stack data. This secures sensitive information within the stack.

#### Stack Export

```
stack:export
```

**Granted by default permission**: StackPermissionRead

Export stack data and configurations. This allows creating backups or migrating stacks.

#### Stack Import

```
stack:import
```

**Granted by default permission**: StackPermissionWrite

Import resources into a stack. This allows bringing external resources under management.

#### Stack Read

```
stack:read
```

**Granted by default permission**: StackPermissionRead

View stack configurations and settings. This provides read-only access to stack details and parameters.

#### Stack Rename

```
stack:rename
```

**Granted by default permission**: StackPermissionWrite

Change the name of a stack. This updates the stack's display name across the platform.

#### Stack Transfer

```
stack:transfer
```

**Granted by default permission**: StackPermissionWrite

Transfer ownership of a stack to another organization or user. This is used for organizational restructuring or migration.

#### Stack Write

```
stack:write
```

**Granted by default permission**: StackPermissionWrite

Modify stack configurations and settings. This allows updating stack parameters and resource definitions.

### Annotations

#### Stack Annotation Read

```
stack_annotations:read
```

**Granted by default permission**: StackPermissionRead

View annotations attached to a stack. This provides context and metadata for stack resources.

#### Stack Annotation Update

```
stack_annotations:update
```

**Granted by default permission**: StackPermissionWrite

Modify or add annotations to a stack. This allows updating stack metadata and documentation.

### Stack Deployments

#### Stack Deployment Cache Clean

```
stack_deployment_cache:clean
```

**Granted by default permission**: StackPermissionWrite

Clear the deployment cache for a stack. This removes cached deployment artifacts and data.

#### Stack Deployment Cache Read

```
stack_deployment_cache:read
```

**Granted by default permission**: StackPermissionWrite

View the deployment cache for a stack. This includes access to cached deployment artifacts and data.

#### Stack Deployment Cancel

```
stack_deployment:cancel
```

**Granted by default permission**: StackPermissionWrite

Cancel an ongoing stack deployment. This halts the current deployment process.

#### Stack Deployment Create

```
stack_deployment:create
```

**Granted by default permission**: StackPermissionWrite

Create a new deployment for a stack. This initiates the deployment process for infrastructure resources.

#### Stack Deployment Pause

```
stack_deployment:pause
```

**Granted by default permission**: StackPermissionWrite

Pause an ongoing stack deployment. This temporarily halts the deployment process.

#### Stack Deployment Read

```
stack_deployment:read
```

**Granted by default permission**: StackPermissionRead

View details of stack deployments. This includes access to deployment status and history.

#### Stack Deployment Resume

```
stack_deployment:resume
```

**Granted by default permission**: StackPermissionWrite

Resume a paused stack deployment. This continues the deployment process from where it was paused.

#### Stack Deployment Settings Encrypt

```
stack_deployment_settings:encrypt
```

**Granted by default permission**: StackPermissionWrite

Encrypt deployment settings for a stack. This secures sensitive configuration data.

#### Stack Deployment Settings Read

```
stack_deployment_settings:read
```

**Granted by default permission**: StackPermissionRead

View deployment settings for a stack. This includes access to configuration parameters and metadata.

#### Stack Deployment Settings Write

```
stack_deployment_settings:write
```

**Granted by default permission**: StackPermissionWrite

Modify deployment settings for a stack. This allows updating configuration parameters and metadata.

### Stack Deploy Schedules

#### Stack Schedule Create

```
stack_schedule:create
```

**Granted by default permission**: StackPermissionWrite

Create a new schedule for automated stack deployments. This allows setting up recurring deployment tasks.

#### Stack Schedule Delete

```
stack_schedule:delete
```

**Granted by default permission**: StackPermissionWrite

Delete an existing stack deployment schedule. This permanently removes the scheduled task.

#### Stack Schedule Pause

```
stack_schedule:pause
```

**Granted by default permission**: StackPermissionWrite

Pause a scheduled stack deployment. This temporarily halts the scheduled deployment process.

#### Stack Schedule Read

```
stack_schedule:read
```

**Granted by default permission**: StackPermissionRead

View stack deployment schedule configurations. This includes access to schedule details and execution history.

#### Stack Schedule Resume

```
stack_schedule:resume
```

**Granted by default permission**: StackPermissionWrite

Resume a paused stack deployment schedule. This restores automated deployment operations.

#### Stack Schedule Update

```
stack_schedule:update
```

**Granted by default permission**: StackPermissionWrite

Modify an existing stack deployment schedule. This allows updating timing, frequency, and other schedule parameters.

### Stack Tags

#### Stack Tags Update

```
stack_tags:update
```

**Granted by default permission**: StackPermissionWrite

Update tags associated with a stack. This helps in organizing and categorizing stack resources.

### Stacks

#### Stack Teams Read

```
stack_teams:read
```

**Granted by default permission**: StackPermissionRead

View teams associated with a stack. This provides visibility into team access and collaboration.

#### Stack Teams Update

```
stack_teams:update
```

**Granted by default permission**: StackPermissionWrite

Modify teams associated with a stack. This allows updating team access and collaboration settings.

### Stack Webhooks

#### Stack Webhook Create

```
stack_webhook:create
```

**Granted by default permission**: StackPermissionWrite

Create a new webhook for stack events. This enables integration with external systems for event notifications.

#### Stack Webhook Delete

```
stack_webhook:delete
```

**Granted by default permission**: StackPermissionWrite

Delete an existing stack webhook. This removes the integration and stops event delivery.

#### Stack Webhook Read

```
stack_webhook:read
```

**Granted by default permission**: StackPermissionWrite

View stack webhook configurations. This includes access to webhook endpoints and event triggers.

#### Stack Webhook Update

```
stack_webhook:update
```

**Granted by default permission**: StackPermissionWrite

Modify an existing stack webhook. This allows updating endpoint URLs and event subscriptions.

## Related Resources

- [Teams](/docs/pulumi-cloud/access-management/rbac/teams)
- [Roles](/docs/pulumi-cloud/access-management/rbac/roles)
- [Permissions](/docs/pulumi-cloud/access-management/rbac/permissions)
