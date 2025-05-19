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

| Value | Description |
|-------|-------------|
| `ai_conversations:create` | Create a new AI conversation session for interacting with Pulumi's AI assistant. This allows users to start new conversations and get help with their infrastructure code.<br><br>**Granted by default roles**: `MemberRole`, `AdminRole` |
| `ai_conversations:list_all` | View all AI conversations across the organization. This provides administrators with visibility into all AI assistant interactions.<br><br>**Granted by default roles**: `AdminRole` |
| `ai_conversations:read` | Access and view the content of AI conversations. This allows users to read their own conversations and continue previous interactions.<br><br>**Granted by default roles**: `MemberRole`, `AdminRole` |
| `ai_conversations:update` | Modify and continue existing AI conversations. This enables users to update their conversations with new questions or context.<br><br>**Granted by default roles**: `MemberRole`, `AdminRole` |

### Agent Pools

| Value | Description |
|-------|-------------|
| `agent_pool:create` | Create a new agent pool for running Pulumi operations. Agent pools provide isolated environments for executing infrastructure deployments.<br><br>**Granted by default roles**: `AdminRole` |
| `agent_pool:delete` | Remove an existing agent pool and its associated resources. This permanently deletes the pool and its configuration.<br><br>**Granted by default roles**: `AdminRole` |
| `agent_pool:read` | View agent pool configurations and status. This includes access to pool settings, agent status, and operational metrics.<br><br>**Granted by default roles**: `AdminRole` |
| `agent_pool:update` | Modify agent pool settings and configurations. This allows updating pool parameters, scaling settings, and agent configurations.<br><br>**Granted by default roles**: `AdminRole` |

### Audit Logs

| Value | Description |
|-------|-------------|
| `audit_logs:export` | Export audit log data for compliance and analysis purposes. This enables downloading audit records in various formats.<br><br>**Granted by default roles**: `AdminRole` |
| `audit_logs:read` | Access and view audit logs of organization activities. This provides visibility into system events and user actions.<br><br>**Granted by default roles**: `AdminRole` |

### OIDC

| Value | Description |
|-------|-------------|
| `auth_policies:read` | View authentication policy configurations. This includes access to OIDC, SAML, and other identity provider settings.<br><br>**Granted by default roles**: `AdminRole` |
| `auth_policies:update` | Modify authentication policies and identity provider settings. This allows updating security configurations and access rules.<br><br>**Granted by default roles**: `AdminRole` |

### Org Deployments

| Value | Description |
|-------|-------------|
| `deployments:pause` | Temporarily halt all deployment operations across the organization. This is useful for maintenance or emergency situations.<br><br>**Granted by default roles**: `AdminRole` |
| `deployments:read` | View deployment configurations and status across the organization. This provides visibility into all deployment activities.<br><br>**Granted by default roles**: `MemberRole`, `AdminRole` |
| `deployments:read_usage` | Access deployment usage metrics and statistics. This includes information about resource consumption and operational costs.<br><br>**Granted by default roles**: `MemberRole`, `AdminRole`, `BillingManagerRole` |
| `deployments:resume` | Resume deployment operations after a pause. This restores normal deployment functionality across the organization.<br><br>**Granted by default roles**: `AdminRole` |

### IaC Policy

| Value | Description |
|-------|-------------|
| `iac_policy_groups:create` | Create a new group of Infrastructure as Code policies. This allows organizing related policies for better management and enforcement.<br><br>**Granted by default roles**: `AdminRole` |
| `iac_policy_groups:delete` | Remove an existing group of Infrastructure as Code policies. This permanently deletes the policy group and its configurations.<br><br>**Granted by default roles**: `AdminRole` |
| `iac_policy_groups:read` | View Infrastructure as Code policy group configurations. This includes access to policy definitions and enforcement rules.<br><br>**Granted by default roles**: `MemberRole`, `AdminRole` |
| `iac_policy_groups:update` | Modify Infrastructure as Code policy group settings. This allows updating policy definitions and enforcement parameters.<br><br>**Granted by default roles**: `AdminRole` |
| `iac_policy_pack:create` | Create a new Infrastructure as Code policy pack. This allows bundling related policies for deployment and enforcement.<br><br>**Granted by default roles**: `AdminRole` |
| `iac_policy_pack:delete` | Remove an existing Infrastructure as Code policy pack. This permanently deletes the policy pack and its configurations.<br><br>**Granted by default roles**: `AdminRole` |
| `iac_policy_pack:read` | View Infrastructure as Code policy pack contents. This includes access to policy definitions and enforcement rules.<br><br>**Granted by default roles**: `AdminRole` |
| `iac_policy_pack:update` | Modify an existing Infrastructure as Code policy pack. This allows updating policy definitions and enforcement parameters.<br><br>**Granted by default roles**: `AdminRole` |
| `iac_policy_results:read` | View results of Infrastructure as Code policy evaluations. This provides insights into policy compliance and violations.<br><br>**Granted by default roles**: `AdminRole` |

### Membership

| Value | Description |
|-------|-------------|
| `invites:create` | Send invitations to new users to join the organization. This enables onboarding of new team members.<br><br>**Granted by default roles**: `AdminRole` |
| `invites:read` | View pending and sent invitations for organization membership. This provides visibility into user onboarding status.<br><br>**Granted by default roles**: `AdminRole` |

### Organization

| Value | Description |
|-------|-------------|
| `integrations:read` | View integration configurations for the organization. This includes access to settings for third-party services and tools.<br><br>**Granted by default roles**: `MemberRole`, `AdminRole` |
| `integrations:update` | Modify integration settings for the organization. This allows updating or reconfiguring third-party service connections.<br><br>**Granted by default roles**: `MemberRole`, `AdminRole` |

### OIDC

| Value | Description |
|-------|-------------|
| `oidc_issuers:create` | Register a new OIDC issuer for authentication. This allows adding new identity providers for user login.<br><br>**Granted by default roles**: `AdminRole` |
| `oidc_issuers:delete` | Remove an existing OIDC issuer. This permanently deletes the identity provider configuration.<br><br>**Granted by default roles**: `AdminRole` |
| `oidc_issuers:read` | View OIDC issuer configurations. This includes access to identity provider details and settings.<br><br>**Granted by default roles**: `AdminRole` |
| `oidc_issuers:regenerate_thumbprints` | Regenerate security thumbprints for an OIDC issuer. This is used to maintain secure authentication.<br><br>**Granted by default roles**: `AdminRole` |
| `oidc_issuers:update` | Modify OIDC issuer settings. This allows updating identity provider details and authentication parameters.<br><br>**Granted by default roles**: `AdminRole` |

### Organization

| Value | Description |
|-------|-------------|
| `org_integrations:read` | View organization-level integration settings. This includes access to all configured integrations.<br><br>**Granted by default roles**: `AdminRole` |
| `org_integrations:update` | Update organization-level integration settings. This allows modifying or removing integrations.<br><br>**Granted by default roles**: `AdminRole` |

### Membership

| Value | Description |
|-------|-------------|
| `org_member:access` | Access organization member details and permissions. This is used for managing user roles and access.<br><br>**Granted by default roles**: `AdminRole` |
| `org_member:add` | Add a new member to the organization. This enables expanding the team with new users.<br><br>**Granted by default roles**: `AdminRole` |
| `org_member:delete` | Remove a member from the organization. This revokes their access and permissions.<br><br>**Granted by default roles**: `AdminRole` |
| `org_member:read` | View details about organization members. This includes access to user profiles and roles.<br><br>**Granted by default roles**: `MemberRole`, `AdminRole`, `BillingManagerRole` |
| `org_member:set_admin` | Grant or revoke admin privileges for an organization member. This controls elevated access.<br><br>**Granted by default roles**: `AdminRole` |
| `org_member:update` | Update organization member information and roles. This allows changing user details and permissions.<br><br>**Granted by default roles**: `AdminRole` |
| `org_requests:create` | Submit a new request to join or interact with the organization. This is used for onboarding or special access. |
| `org_requests:read` | View all organization requests. This provides visibility into pending and processed requests.<br><br>**Granted by default roles**: `AdminRole` |
| `org_requests:status` | Check the status of an organization request. This helps track onboarding or access progress. |
| `org_requests:update` | Update or process organization requests. This allows approving or denying requests.<br><br>**Granted by default roles**: `AdminRole` |

### Organization Tokens

| Value | Description |
|-------|-------------|
| `org_token:create` | Create a new organization API token. This enables programmatic access to organization resources.<br><br>**Granted by default roles**: `AdminRole` |
| `org_token:delete` | Delete an existing organization API token. This revokes programmatic access.<br><br>**Granted by default roles**: `AdminRole` |
| `org_token:read` | View organization API tokens. This includes access to token details and usage.<br><br>**Granted by default roles**: `AdminRole` |

### Annotations

| Value | Description |
|-------|-------------|
| `organization_annotations:read` | View annotations attached to the organization. This provides context and metadata for organizational resources.<br><br>**Granted by default roles**: `MemberRole`, `AdminRole` |
| `organization_annotations:update` | Modify or add annotations to the organization. This allows updating organizational metadata.<br><br>**Granted by default roles**: `AdminRole` |

### Organization

| Value | Description |
|-------|-------------|
| `organization:billing` | Manage billing settings and payment methods for the organization. This includes access to invoices and payment history.<br><br>**Granted by default roles**: `AdminRole`, `BillingManagerRole` |
| `organization:change_backend` | Change the backend infrastructure for the organization. This is used for advanced configuration and migration.<br><br>**Granted by default roles**: `AdminRole` |
| `organization:delete` | Delete the organization and all its resources. This is a permanent and irreversible action.<br><br>**Granted by default roles**: `AdminRole` |
| `organization:read` | View organization details and settings. This includes access to organizational metadata and configuration.<br><br>**Granted by default roles**: `MemberRole`, `AdminRole`, `BillingManagerRole` |
| `organization:read_activity` | View recent activity and audit logs for the organization. This provides insight into changes and events.<br><br>**Granted by default roles**: `MemberRole`, `AdminRole`, `BillingManagerRole` |
| `organization:read_usage` | View usage statistics and metrics for the organization. This includes resource consumption and cost data.<br><br>**Granted by default roles**: `MemberRole`, `AdminRole`, `BillingManagerRole` |
| `organization:rename` | Change the name of the organization. This updates the organization's display name across the platform.<br><br>**Granted by default roles**: `AdminRole` |
| `organization:transfer_stacks` | Transfer ownership of stacks between organizations. This is used for organizational restructuring or migration.<br><br>**Granted by default roles**: `AdminRole` |
| `organization:update` | Update organization settings and configurations. This allows changing metadata, policies, and preferences.<br><br>**Granted by default roles**: `AdminRole` |

### Org Webhooks

| Value | Description |
|-------|-------------|
| `organization_webhook:create` | Create a new webhook for organization events. This enables integration with external systems for event notifications.<br><br>**Granted by default roles**: `AdminRole` |
| `organization_webhook:delete` | Delete an existing organization webhook. This removes the integration and stops event delivery.<br><br>**Granted by default roles**: `AdminRole` |
| `organization_webhook:read` | View organization webhook configurations. This includes access to webhook endpoints and event triggers.<br><br>**Granted by default roles**: `AdminRole` |
| `organization_webhook:update` | Modify an existing organization webhook. This allows updating endpoint URLs and event subscriptions.<br><br>**Granted by default roles**: `AdminRole` |

### Project Annotations

| Value | Description |
|-------|-------------|
| `project_annotations:read` | [placeholder]<br><br>**Granted by default roles**: `MemberRole`, `AdminRole` |
| `project_annotations:update` | [placeholder]<br><br>**Granted by default roles**: `MemberRole`, `AdminRole` |

### Project

| Value | Description |
|-------|-------------|
| `project:decrypt` | [placeholder]<br><br>**Granted by default roles**: `MemberRole`, `AdminRole` |
| `project:encrypt` | [placeholder]<br><br>**Granted by default roles**: `MemberRole`, `AdminRole` |

### Resources

| Value | Description |
|-------|-------------|
| `resources:dashboard` | [placeholder]<br><br>**Granted by default roles**: `MemberRole`, `AdminRole`, `BillingManagerRole` |
| `resources:index` | [placeholder]<br><br>**Granted by default roles**: `AdminRole` |
| `resources:search` | [placeholder]<br><br>**Granted by default roles**: `MemberRole`, `AdminRole` |

### Roles

| Value | Description |
|-------|-------------|
| `role:create` | [placeholder]<br><br>**Granted by default roles**: `AdminRole` |
| `role:delete` | [placeholder]<br><br>**Granted by default roles**: `AdminRole` |
| `role:read` | [placeholder]<br><br>**Granted by default roles**: `AdminRole` |
| `role:update` | [placeholder]<br><br>**Granted by default roles**: `AdminRole` |

### SAML

| Value | Description |
|-------|-------------|
| `saml:read` | [placeholder]<br><br>**Granted by default roles**: `MemberRole`, `AdminRole`, `BillingManagerRole` |
| `saml:update` | [placeholder]<br><br>**Granted by default roles**: `AdminRole` |

### SCIM

| Value | Description |
|-------|-------------|
| `scim:delete` | [placeholder]<br><br>**Granted by default roles**: `AdminRole` |
| `scim:read` | [placeholder]<br><br>**Granted by default roles**: `AdminRole` |
| `scim:update` | [placeholder]<br><br>**Granted by default roles**: `AdminRole` |

### Services

| Value | Description |
|-------|-------------|
| `services:admin` | [placeholder]<br><br>**Granted by default roles**: `MemberRole`, `AdminRole` |
| `services:create` | [placeholder]<br><br>**Granted by default roles**: `MemberRole`, `AdminRole` |
| `services:read` | [placeholder]<br><br>**Granted by default roles**: `MemberRole`, `AdminRole` |
| `services:write` | [placeholder]<br><br>**Granted by default roles**: `MemberRole`, `AdminRole` |

### Tags

| Value | Description |
|-------|-------------|
| `tags:read` | [placeholder]<br><br>**Granted by default roles**: `MemberRole`, `AdminRole` |

### Teams

| Value | Description |
|-------|-------------|
| `team:create` | [placeholder]<br><br>**Granted by default roles**: `AdminRole` |
| `team:create_token` | [placeholder]<br><br>**Granted by default roles**: `AdminRole` |
| `team:delete` | [placeholder]<br><br>**Granted by default roles**: `AdminRole` |
| `team:delete_token` | [placeholder]<br><br>**Granted by default roles**: `AdminRole` |
| `team:list` | [placeholder]<br><br>**Granted by default roles**: `MemberRole`, `AdminRole`, `BillingManagerRole` |
| `team:list_tokens` | [placeholder]<br><br>**Granted by default roles**: `AdminRole` |
| `team:read` | [placeholder]<br><br>**Granted by default roles**: `MemberRole`, `AdminRole` |
| `team:update` | [placeholder]<br><br>**Granted by default roles**: `AdminRole` |
| `github_team:create` | Create a new team that syncs with GitHub. This enables integration between Pulumi and GitHub team structures.<br><br>**Granted by default roles**: `AdminRole` |

### Templates

| Value | Description |
|-------|-------------|
| `templates:read` | [placeholder]<br><br>**Granted by default roles**: `MemberRole`, `AdminRole` |

### Template Sources

| Value | Description |
|-------|-------------|
| `templates:source:create` | [placeholder]<br><br>**Granted by default roles**: `AdminRole` |
| `templates:source:delete` | [placeholder]<br><br>**Granted by default roles**: `AdminRole` |
| `templates:source:read` | [placeholder]<br><br>**Granted by default roles**: `AdminRole` |
| `templates:source:update` | [placeholder]<br><br>**Granted by default roles**: `AdminRole` |

## Type: Environment

### Environments

| Value | Description |
|-------|-------------|
| `environment:clone` | Create a copy of an existing environment with all its configurations. This is useful for creating staging or testing environments.<br><br>**Granted by default permission**: `EnvironmentPermissionBackendOpen` |
| `environment:create` | Create a new environment for managing infrastructure configurations. Environments provide isolated spaces for different deployment stages.<br><br>**Granted by default roles**: `MemberRole`, `AdminRole` |
| `environment:read_decrypt` | Access and decrypt sensitive environment data. This allows viewing encrypted configuration values and secrets.<br><br>**Granted by default permission**: `EnvironmentPermissionBackendOpen` |
| `environment:delete` | Remove an environment and its associated resources. This permanently deletes the environment and its configurations.<br><br>**Granted by default permission**: `EnvironmentPermissionBackendOpen` |
| `environment:list` | View all environments in the organization. This provides a list of available environments and their basic information.<br><br>**Granted by default roles**: `MemberRole`, `AdminRole` |
| `environment:list_deleted` | View a list of environments that have been deleted but are still recoverable. This helps in managing and potentially restoring deleted environments.<br><br>**Granted by default roles**: `MemberRole`, `AdminRole` |
| `environment:open` | Access and interact with an environment's resources. This includes the ability to view and modify environment configurations.<br><br>**Granted by default permission**: `EnvironmentPermissionBackendOpen` |
| `environment:read` | View environment configurations and settings. This provides read-only access to environment details and parameters.<br><br>**Granted by default permission**: `EnvironmentPermissionBackendRead` |
| `environment:restore_deleted` | Recover a previously deleted environment. This restores the environment and its configurations to their previous state.<br><br>**Granted by default roles**: `AdminRole` |
| `environment:write` | Modify environment configurations and settings. This allows updating environment parameters and resource definitions.<br><br>**Granted by default permission**: `EnvironmentPermissionBackendOpen` |
| `environment_yaml:open` | Access and view environment configuration in YAML format. This provides a structured view of environment settings.<br><br>**Granted by default roles**: `MemberRole`, `AdminRole` |

### Environment Secrets Rotation

| Value | Description |
|-------|-------------|
| `environment:rotate` | Initiate a rotation of secrets and credentials in an environment. This is a security measure to regularly update sensitive information.<br><br>**Granted by default permission**: `EnvironmentPermissionBackendOpen` |
| `environment:rotate_history` | View the history of secret rotations for an environment. This provides an audit trail of when secrets were last changed.<br><br>**Granted by default permission**: `EnvironmentPermissionBackendRead` |

### Environment Schedules

| Value | Description |
|-------|-------------|
| `environment_schedule:create` | Create a new schedule for automated environment operations. This allows setting up recurring tasks and maintenance windows.<br><br>**Granted by default permission**: `EnvironmentPermissionBackendOpen` |
| `environment_schedule:delete` | Remove an existing environment schedule. This permanently deletes the scheduled task and its configuration.<br><br>**Granted by default permission**: `EnvironmentPermissionBackendOpen` |
| `environment_schedule:pause` | Temporarily suspend an environment schedule. This halts automated operations without deleting the schedule.<br><br>**Granted by default permission**: `EnvironmentPermissionBackendOpen` |
| `environment_schedule:read` | View environment schedule configurations and status. This includes access to schedule details and execution history.<br><br>**Granted by default permission**: `EnvironmentPermissionBackendRead` |
| `environment_schedule:resume` | Resume a paused environment schedule. This restores automated operations according to the schedule.<br><br>**Granted by default permission**: `EnvironmentPermissionBackendOpen` |
| `environment_schedule:update` | Modify an existing environment schedule. This allows updating timing, frequency, and other schedule parameters.<br><br>**Granted by default permission**: `EnvironmentPermissionBackendOpen` |

### Environment Tags

| Value | Description |
|-------|-------------|
| `environment_tag:create` | Add a new tag to an environment. This helps in organizing and categorizing environments.<br><br>**Granted by default permission**: `EnvironmentPermissionBackendOpen` |
| `environment_tag:delete` | Remove a tag from an environment. This allows cleaning up or reorganizing environment categorization.<br><br>**Granted by default permission**: `EnvironmentPermissionBackendOpen` |
| `environment_tag:read` | View tags associated with environments. This provides access to environment categorization and metadata.<br><br>**Granted by default permission**: `EnvironmentPermissionBackendOpen` |
| `environment_tag:update` | Modify existing environment tags. This allows updating tag values and metadata.<br><br>**Granted by default permission**: `EnvironmentPermissionBackendOpen` |
| `environment_tags:list` | View all tags used across environments. This provides a comprehensive view of environment categorization.<br><br>**Granted by default permission**: `EnvironmentPermissionBackendOpen` |

### Environment Versions

| Value | Description |
|-------|-------------|
| `environment_version:create` | Create a new version of an environment. This allows tracking changes and maintaining environment history.<br><br>**Granted by default permission**: `EnvironmentPermissionBackendOpen` |
| `environment_version:read_decrypt` | Access and decrypt sensitive data in an environment version. This allows viewing encrypted configuration values.<br><br>**Granted by default permission**: `EnvironmentPermissionBackendOpen` |
| `environment_version:delete` | Remove a specific version of an environment. This permanently deletes the version and its configurations.<br><br>**Granted by default permission**: `EnvironmentPermissionBackendOpen` |
| `environment_version:open` | Access and interact with a specific environment version. This includes viewing and using version-specific configurations.<br><br>**Granted by default permission**: `EnvironmentPermissionBackendOpen` |
| `environment_version:read` | View details of a specific environment version. This provides access to version-specific configurations and metadata.<br><br>**Granted by default permission**: `EnvironmentPermissionBackendOpen` |
| `environment_version:retract` | Mark a specific environment version as invalid or deprecated. This prevents its use while maintaining history.<br><br>**Granted by default permission**: `EnvironmentPermissionBackendOpen` |
| `environment_version:update` | Modify an existing environment version. This allows updating version-specific configurations and metadata.<br><br>**Granted by default permission**: `EnvironmentPermissionBackendOpen` |

### Environment Webhooks

| Value | Description |
|-------|-------------|
| `environment_webhook:create` | Create a new webhook for environment events. This enables integration with external systems and automation.<br><br>**Granted by default permission**: `EnvironmentPermissionBackendOpen` |
| `environment_webhook:delete` | Remove an existing environment webhook. This permanently deletes the webhook configuration.<br><br>**Granted by default permission**: `EnvironmentPermissionBackendOpen` |
| `environment_webhook:read` | View environment webhook configurations. This includes access to webhook settings and event triggers.<br><br>**Granted by default permission**: `EnvironmentPermissionBackendOpen` |
| `environment_webhook:update` | Modify an existing environment webhook. This allows updating webhook settings and event triggers.<br><br>**Granted by default permission**: `EnvironmentPermissionBackendOpen` |

## Type: Insights Account

### Insights Accounts

| Value | Description |
|-------|-------------|
| `insights_account_access:read` | View what users and roles can access an insights account.<br><br>**Granted by default permission**: `InsightsAccountPermissionRead` |
| `insights_account_access:update` | Manage what users and roles can access an insights account.<br><br>**Granted by default permission**: `InsightsAccountPermissionRead` |
| `insights_account:create` | Create a new insights account. This allows setting up monitoring and analysis capabilities for infrastructure.<br><br>**Granted by default roles**: `AdminRole` |
| `insights_account:delete` | Remove an existing insights account. This permanently deletes the account and its associated data.<br><br>**Granted by default permission**: `InsightsAccountPermissionWrite` |
| `insights_account:list` | View all insights accounts in the organization. This provides a list of available accounts and their basic information.<br><br>**Granted by default roles**: `MemberRole`, `AdminRole` |
| `insights_account:read` | View insights account configurations and data. This includes access to monitoring settings and analysis results.<br><br>**Granted by default permission**: `InsightsAccountPermissionRead` |
| `insights_account:update` | Modify insights account settings and configurations. This allows updating monitoring parameters and analysis rules.<br><br>**Granted by default permission**: `InsightsAccountPermissionWrite` |
| `insights_account:update_policy_results` | Update policy evaluation results for an insights account. This allows refreshing compliance data and analysis.<br><br>**Granted by default permission**: `InsightsAccountPermissionWrite` |

### Insights Scan

| Value | Description |
|-------|-------------|
| `insights_account:scan` | Initiate a new scan of an insights account. This triggers analysis of infrastructure configurations and compliance.<br><br>**Granted by default permission**: `InsightsAccountPermissionWrite` |
| `insights_account_scan:cancel` | Stop an ongoing insights account scan. This halts the current analysis process.<br><br>**Granted by default permission**: `InsightsAccountPermissionWrite` |
| `insights_account_scan:pause` | Temporarily suspend an insights account scan. This pauses the analysis process without losing progress.<br><br>**Granted by default permission**: `InsightsAccountPermissionWrite` |
| `insights_account_scan:read` | View insights account scan results and status. This includes access to analysis findings and progress.<br><br>**Granted by default permission**: `InsightsAccountPermissionRead` |
| `insights_account_scan:resume` | Resume a paused insights account scan. This continues the analysis process from where it was paused.<br><br>**Granted by default permission**: `InsightsAccountPermissionWrite` |
| `insights_account_scan:update` | Modify insights account scan settings. This allows updating scan parameters and analysis configurations.<br><br>**Granted by default permission**: `InsightsAccountPermissionWrite` |

### Insights Policy Evaluator

| Value | Description |
|-------|-------------|
| `insights_policy_evaluator:delete` | Remove an existing policy evaluator. This permanently deletes the evaluator and its configurations.<br><br>**Granted by default roles**: `MemberRole`, `AdminRole` |
| `insights_policy_evaluator:ensure` | Create or update a policy evaluator. This ensures the evaluator exists with the correct configuration.<br><br>**Granted by default roles**: `MemberRole`, `AdminRole` |
| `insights_policy_evaluator:read` | View policy evaluator configurations and status. This includes access to evaluation rules and results.<br><br>**Granted by default roles**: `MemberRole`, `AdminRole` |
| `insights_policy_evaluator:update` | Modify an existing policy evaluator. This allows updating evaluation rules and parameters.<br><br>**Granted by default roles**: `MemberRole`, `AdminRole` |

### Insights Policy Queue

| Value | Description |
|-------|-------------|
| `insights_policy_queue:read` | View the policy evaluation queue status. This provides visibility into pending and completed evaluations.<br><br>**Granted by default roles**: `MemberRole`, `AdminRole` |

## Type: Stack

### Stacks

| Value | Description |
|-------|-------------|
| `stack:access` | Access stack resources and perform write operations. This includes updating stack configurations and deployments.<br><br>**Granted by default roles**: `AdminRole`<br><br>**Granted by default permission**: `StackPermissionWrite` |
| `stack:cancel_update` | Cancel an ongoing stack update operation. This halts the current deployment or update process.<br><br>**Granted by default permission**: `StackPermissionWrite` |
| `stack:create` | Create a new stack for managing infrastructure resources. Stacks represent isolated units of deployment.<br><br>**Granted by default roles**: `AdminRole` |
| `stack:decrypt` | Decrypt sensitive stack data. This allows viewing encrypted configuration values and secrets.<br><br>**Granted by default permission**: `StackPermissionRead` |
| `stack:delete` | Delete a stack and its associated resources. This permanently removes the stack from the organization.<br><br>**Granted by default permission**: `StackPermissionWrite` |
| `stack:encrypt` | Encrypt stack data. This secures sensitive information within the stack.<br><br>**Granted by default permission**: `StackPermissionRead` |
| `stack:export` | Export stack data and configurations. This allows creating backups or migrating stacks.<br><br>**Granted by default permission**: `StackPermissionRead` |
| `stack:import` | Import resources into a stack. This allows bringing external resources under management.<br><br>**Granted by default permission**: `StackPermissionWrite` |
| `stack:list` | [placeholder]<br><br>**Granted by default roles**: `MemberRole`, `AdminRole` |
| `stack:list_deleted` | [placeholder]<br><br>**Granted by default roles**: `AdminRole` |
| `stack:read` | View stack configurations and settings. This provides read-only access to stack details and parameters.<br><br>**Granted by default permission**: `StackPermissionRead` |
| `stack:rename` | Change the name of a stack. This updates the stack's display name across the platform.<br><br>**Granted by default permission**: `StackPermissionWrite` |
| `stack:restore_deleted` | [placeholder]<br><br>**Granted by default roles**: `AdminRole` |
| `stack:transfer` | Transfer ownership of a stack to another organization or user. This is used for organizational restructuring or migration.<br><br>**Granted by default permission**: `StackPermissionWrite` |
| `stack:write` | Modify stack configurations and settings. This allows updating stack parameters and resource definitions.<br><br>**Granted by default permission**: `StackPermissionWrite` |

### Annotations

| Value | Description |
|-------|-------------|
| `stack_annotations:read` | View annotations attached to a stack. This provides context and metadata for stack resources.<br><br>**Granted by default permission**: `StackPermissionRead` |
| `stack_annotations:update` | Modify or add annotations to a stack. This allows updating stack metadata and documentation.<br><br>**Granted by default permission**: `StackPermissionWrite` |

### Stack Deployments

| Value | Description |
|-------|-------------|
| `stack_deployment_cache:clean` | Clear the deployment cache for a stack. This removes cached deployment artifacts and data.<br><br>**Granted by default permission**: `StackPermissionWrite` |
| `stack_deployment_cache:read` | View the deployment cache for a stack. This includes access to cached deployment artifacts and data.<br><br>**Granted by default permission**: `StackPermissionWrite` |
| `stack_deployment:cancel` | Cancel an ongoing stack deployment. This halts the current deployment process.<br><br>**Granted by default permission**: `StackPermissionWrite` |
| `stack_deployment:create` | Create a new deployment for a stack. This initiates the deployment process for infrastructure resources.<br><br>**Granted by default permission**: `StackPermissionWrite` |
| `stack_deployment:pause` | Pause an ongoing stack deployment. This temporarily halts the deployment process.<br><br>**Granted by default permission**: `StackPermissionWrite` |
| `stack_deployment:read` | View details of stack deployments. This includes access to deployment status and history.<br><br>**Granted by default permission**: `StackPermissionRead` |
| `stack_deployment:resume` | Resume a paused stack deployment. This continues the deployment process from where it was paused.<br><br>**Granted by default permission**: `StackPermissionWrite` |
| `stack_deployment_settings:encrypt` | Encrypt deployment settings for a stack. This secures sensitive configuration data.<br><br>**Granted by default permission**: `StackPermissionWrite` |
| `stack_deployment_settings:read` | View deployment settings for a stack. This includes access to configuration parameters and metadata.<br><br>**Granted by default permission**: `StackPermissionRead` |
| `stack_deployment_settings:write` | Modify deployment settings for a stack. This allows updating configuration parameters and metadata.<br><br>**Granted by default permission**: `StackPermissionWrite` |

### Stack Deploy Schedules

| Value | Description |
|-------|-------------|
| `stack_schedule:create` | Create a new schedule for automated stack deployments. This allows setting up recurring deployment tasks.<br><br>**Granted by default permission**: `StackPermissionWrite` |
| `stack_schedule:delete` | Delete an existing stack deployment schedule. This permanently removes the scheduled task.<br><br>**Granted by default permission**: `StackPermissionWrite` |
| `stack_schedule:pause` | Pause a scheduled stack deployment. This temporarily halts the scheduled deployment process.<br><br>**Granted by default permission**: `StackPermissionWrite` |
| `stack_schedule:read` | View stack deployment schedule configurations. This includes access to schedule details and execution history.<br><br>**Granted by default permission**: `StackPermissionRead` |
| `stack_schedule:resume` | Resume a paused stack deployment schedule. This restores automated deployment operations.<br><br>**Granted by default permission**: `StackPermissionWrite` |
| `stack_schedule:update` | Modify an existing stack deployment schedule. This allows updating timing, frequency, and other schedule parameters.<br><br>**Granted by default permission**: `StackPermissionWrite` |

### Stack Tags

| Value | Description |
|-------|-------------|
| `stack_tags:update` | Update tags associated with a stack. This helps in organizing and categorizing stack resources.<br><br>**Granted by default permission**: `StackPermissionWrite` |

### Stacks

| Value | Description |
|-------|-------------|
| `stack_teams:read` | View teams associated with a stack. This provides visibility into team access and collaboration.<br><br>**Granted by default permission**: `StackPermissionRead` |
| `stack_teams:update` | Modify teams associated with a stack. This allows updating team access and collaboration settings.<br><br>**Granted by default permission**: `StackPermissionWrite` |

### Stack Webhooks

| Value | Description |
|-------|-------------|
| `stack_webhook:create` | Create a new webhook for stack events. This enables integration with external systems for event notifications.<br><br>**Granted by default permission**: `StackPermissionWrite` |
| `stack_webhook:delete` | Delete an existing stack webhook. This removes the integration and stops event delivery.<br><br>**Granted by default permission**: `StackPermissionWrite` |
| `stack_webhook:read` | View stack webhook configurations. This includes access to webhook endpoints and event triggers.<br><br>**Granted by default permission**: `StackPermissionWrite` |
| `stack_webhook:update` | Modify an existing stack webhook. This allows updating endpoint URLs and event subscriptions.<br><br>**Granted by default permission**: `StackPermissionWrite` |

## Related Resources

- [Teams](/docs/pulumi-cloud/access-management/rbac/teams)
- [Roles](/docs/pulumi-cloud/access-management/rbac/roles)
- [Permissions](/docs/pulumi-cloud/access-management/rbac/permissions)
