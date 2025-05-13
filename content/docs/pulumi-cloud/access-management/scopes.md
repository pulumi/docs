---
title_tag: "Pulumi Cloud: Authorization Scopes"
meta_desc: All available authorization scopes for Pulumi Cloud
title: "Authorization scopes"
h1: "Authorization scopes"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: Authorization scopes
    parent: pulumi-cloud-access-management
    weight: 5
    identifier: pulumi-cloud-access-management-authorization-scopes
aliases:
- /docs/intro/pulumi-service/scopes/
- /docs/intro/pulumi-cloud/scopes/
---

This document defines all the available scopes in Pulumi Cloud, organized by resource type and group.

## Type: Organization settings

### AI

#### AI Conversations Create

```
ai_conversations:create
```

**Granted by default roles**: `MemberRole`, `AdminRole`

Create a new AI conversation session for interacting with Pulumi's AI assistant. This allows users to start new conversations and get help with their infrastructure code.

#### AI Conversations List All

```
ai_conversations:list_all
```

**Granted by default roles**: `AdminRole`

View all AI conversations across the organization. This provides administrators with visibility into all AI assistant interactions.

#### AI Conversations Read

```
ai_conversations:read
```

**Granted by default roles**: `MemberRole`, `AdminRole`

Access and view the content of AI conversations. This allows users to read their own conversations and continue previous interactions.

#### AI Conversations Update

```
ai_conversations:update
```

**Granted by default roles**: `MemberRole`, `AdminRole`

Modify and continue existing AI conversations. This enables users to update their conversations with new questions or context.

### Agent Pools

#### Agent Pool Create

```
agent_pool:create
```

**Granted by default roles**: `AdminRole`

Create a new agent pool for running Pulumi operations. Agent pools provide isolated environments for executing infrastructure deployments.

#### Agent Pool Delete

```
agent_pool:delete
```

**Granted by default roles**: `AdminRole`

Remove an existing agent pool and its associated resources. This permanently deletes the pool and its configuration.

#### Agent Pool Read

```
agent_pool:read
```

**Granted by default roles**: `AdminRole`

View agent pool configurations and status. This includes access to pool settings, agent status, and operational metrics.

#### Agent Pool Update

```
agent_pool:update
```

**Granted by default roles**: `AdminRole`

Modify agent pool settings and configurations. This allows updating pool parameters, scaling settings, and agent configurations.

### Audit Logs

#### Audit Logs Export

```
audit_logs:export
```

**Granted by default roles**: `AdminRole`

Export audit log data for compliance and analysis purposes. This enables downloading audit records in various formats.

#### Audit Logs Read

```
audit_logs:read
```

**Granted by default roles**: `AdminRole`

Access and view audit logs of organization activities. This provides visibility into system events and user actions.

### OIDC

#### Auth Policies Read

```
auth_policies:read
```

**Granted by default roles**: `AdminRole`

View authentication policy configurations. This includes access to OIDC, SAML, and other identity provider settings.

#### Auth Policies Update

```
auth_policies:update
```

**Granted by default roles**: `AdminRole`

Modify authentication policies and identity provider settings. This allows updating security configurations and access rules.

### Org Deployments

#### Deployments Pause

```
deployments:pause
```

**Granted by default roles**: `AdminRole`

Temporarily halt all deployment operations across the organization. This is useful for maintenance or emergency situations.

#### Deployments Read

```
deployments:read
```

**Granted by default roles**: `MemberRole`, `AdminRole`

View deployment configurations and status across the organization. This provides visibility into all deployment activities.

#### Deployments Read Usage

```
deployments:read_usage
```

**Granted by default roles**: `MemberRole`, `AdminRole`, BillingManagerRole

Access deployment usage metrics and statistics. This includes information about resource consumption and operational costs.

#### Deployments Resume

```
deployments:resume
```

**Granted by default roles**: `AdminRole`

Resume deployment operations after a pause. This restores normal deployment functionality across the organization.

### Teams

#### Github Team Create

```
github_team:create
```

**Granted by default roles**: `AdminRole`

Create a new team that syncs with GitHub. This enables integration between Pulumi and GitHub team structures.

### IaC Policy

#### IaC Policy Groups Create

```
iac_policy_groups:create
```

**Granted by default roles**: `AdminRole`

Create a new group of Infrastructure as Code policies. This allows organizing related policies for better management and enforcement.

#### IaC Policy Groups Delete

```
iac_policy_groups:delete
```

**Granted by default roles**: `AdminRole`

Remove an existing group of Infrastructure as Code policies. This permanently deletes the policy group and its configurations.

#### IaC Policy Groups Read

```
iac_policy_groups:read
```

**Granted by default roles**: `MemberRole`, `AdminRole`

View Infrastructure as Code policy group configurations. This includes access to policy definitions and enforcement rules.

#### IaC Policy Groups Update

```
iac_policy_groups:update
```

**Granted by default roles**: `AdminRole`

Modify Infrastructure as Code policy group settings. This allows updating policy definitions and enforcement parameters.

#### IaC Policy Pack Create

```
iac_policy_pack:create
```

**Granted by default roles**: `AdminRole`

Create a new Infrastructure as Code policy pack. This allows bundling related policies for deployment and enforcement.

#### IaC Policy Pack Delete

```
iac_policy_pack:delete
```

**Granted by default roles**: `AdminRole`

Remove an existing Infrastructure as Code policy pack. This permanently deletes the policy pack and its configurations.

#### IaC Policy Pack Read

```
iac_policy_pack:read
```

**Granted by default roles**: `AdminRole`

View Infrastructure as Code policy pack contents. This includes access to policy definitions and enforcement rules.

#### IaC Policy Pack Update

```
iac_policy_pack:update
```

**Granted by default roles**: `AdminRole`

Modify an existing Infrastructure as Code policy pack. This allows updating policy definitions and enforcement parameters.

#### IaC Policy Results Read

```
iac_policy_results:read
```

**Granted by default roles**: `AdminRole`

View results of Infrastructure as Code policy evaluations. This provides insights into policy compliance and violations.

### Organization

#### Integrations Read

```
integrations:read
```

**Granted by default roles**: `MemberRole`, `AdminRole`

View integration configurations for the organization. This includes access to settings for third-party services and tools.

#### Integrations Update

```
integrations:update
```

**Granted by default roles**: `MemberRole`, `AdminRole`

Modify integration settings for the organization. This allows updating or reconfiguring third-party service connections.

### Membership

#### Invites Create

```
invites:create
```

**Granted by default roles**: `AdminRole`

Send invitations to new users to join the organization. This enables onboarding of new team members.

#### Invites Read

```
invites:read
```

**Granted by default roles**: `AdminRole`

View pending and sent invitations for organization membership. This provides visibility into user onboarding status.

### OIDC

#### OIDC Issuers Create

```
oidc_issuers:create
```

**Granted by default roles**: `AdminRole`

Register a new OIDC issuer for authentication. This allows adding new identity providers for user login.

#### OIDC Issuers Delete

```
oidc_issuers:delete
```

**Granted by default roles**: `AdminRole`

Remove an existing OIDC issuer. This permanently deletes the identity provider configuration.

#### OIDC Issuers Read

```
oidc_issuers:read
```

**Granted by default roles**: `AdminRole`

View OIDC issuer configurations. This includes access to identity provider details and settings.

#### OIDC Issuers Regenerate Thumbprints

```
oidc_issuers:regenerate_thumbprints
```

**Granted by default roles**: `AdminRole`

Regenerate security thumbprints for an OIDC issuer. This is used to maintain secure authentication.

#### OIDC Issuers Update

```
oidc_issuers:update
```

**Granted by default roles**: `AdminRole`

Modify OIDC issuer settings. This allows updating identity provider details and authentication parameters.

### Organization

#### Org Integrations Read

```
org_integrations:read
```

**Granted by default roles**: `AdminRole`

View organization-level integration settings. This includes access to all configured integrations.

#### Org Integrations Update

```
org_integrations:update
```

**Granted by default roles**: `AdminRole`

Update organization-level integration settings. This allows modifying or removing integrations.

### Membership

#### Org Member Access

```
org_member:access
```

**Granted by default roles**: `AdminRole`

Access organization member details and permissions. This is used for managing user roles and access.

#### Org Member Add

```
org_member:add
```

**Granted by default roles**: `AdminRole`

Add a new member to the organization. This enables expanding the team with new users.

#### Org Member Delete

```
org_member:delete
```

**Granted by default roles**: `AdminRole`

Remove a member from the organization. This revokes their access and permissions.

#### Org Member Read

```
org_member:read
```

**Granted by default roles**: `MemberRole`, `AdminRole`, BillingManagerRole

View details about organization members. This includes access to user profiles and roles.

#### Org Member Set Admin

```
org_member:set_admin
```

**Granted by default roles**: `AdminRole`

Grant or revoke admin privileges for an organization member. This controls elevated access.

#### Org Member Update

```
org_member:update
```

**Granted by default roles**: `AdminRole`

Update organization member information and roles. This allows changing user details and permissions.

#### Org Requests Create

```
org_requests:create
```

Submit a new request to join or interact with the organization. This is used for onboarding or special access.

#### Org Requests Read

```
org_requests:read
```

**Granted by default roles**: `AdminRole`

View all organization requests. This provides visibility into pending and processed requests.

#### Org Requests Status

```
org_requests:status
```

Check the status of an organization request. This helps track onboarding or access progress.

#### Org Requests Update

```
org_requests:update
```

**Granted by default roles**: `AdminRole`

Update or process organization requests. This allows approving or denying requests.

### Organization Tokens

#### Org Token Create

```
org_token:create
```

**Granted by default roles**: `AdminRole`

Create a new organization API token. This enables programmatic access to organization resources.

#### Org Token Delete

```
org_token:delete
```

**Granted by default roles**: `AdminRole`

Delete an existing organization API token. This revokes programmatic access.

#### Org Token Read

```
org_token:read
```

**Granted by default roles**: `AdminRole`

View organization API tokens. This includes access to token details and usage.

### Annotations

#### Organization Annotations Read

```
organization_annotations:read
```

**Granted by default roles**: `MemberRole`, `AdminRole`

View annotations attached to the organization. This provides context and metadata for organizational resources.

#### Organization Annotations Update

```
organization_annotations:update
```

**Granted by default roles**: `AdminRole`

Modify or add annotations to the organization. This allows updating organizational metadata.

### Organization

#### Organization Billing

```
organization:billing
```

**Granted by default roles**: `AdminRole`, BillingManagerRole

Manage billing settings and payment methods for the organization. This includes access to invoices and payment history.

#### Organization Change Backend

```
organization:change_backend
```

**Granted by default roles**: `AdminRole`

Change the backend infrastructure for the organization. This is used for advanced configuration and migration.

#### Organization Delete

```
organization:delete
```

**Granted by default roles**: `AdminRole`

Delete the organization and all its resources. This is a permanent and irreversible action.

#### Organization Read

```
organization:read
```

**Granted by default roles**: `MemberRole`, `AdminRole`, BillingManagerRole

View organization details and settings. This includes access to organizational metadata and configuration.

#### Organization Read Activity

```
organization:read_activity
```

**Granted by default roles**: `MemberRole`, `AdminRole`, BillingManagerRole

View recent activity and audit logs for the organization. This provides insight into changes and events.

#### Organization Read Usage

```
organization:read_usage
```

**Granted by default roles**: `MemberRole`, `AdminRole`, BillingManagerRole

View usage statistics and metrics for the organization. This includes resource consumption and cost data.

#### Organization Rename

```
organization:rename
```

**Granted by default roles**: `AdminRole`

Change the name of the organization. This updates the organization's display name across the platform.

#### Organization Transfer Stacks

```
organization:transfer_stacks
```

**Granted by default roles**: `AdminRole`

Transfer ownership of stacks between organizations. This is used for organizational restructuring or migration.

#### Organization Update

```
organization:update
```

**Granted by default roles**: `AdminRole`

Update organization settings and configurations. This allows changing metadata, policies, and preferences.

### Org Webhooks

#### Organization Webhook Create

```
organization_webhook:create
```

**Granted by default roles**: `AdminRole`

Create a new webhook for organization events. This enables integration with external systems for event notifications.

#### Organization Webhook Delete

```
organization_webhook:delete
```

**Granted by default roles**: `AdminRole`

Delete an existing organization webhook. This removes the integration and stops event delivery.

#### Organization Webhook Read

```
organization_webhook:read
```

**Granted by default roles**: `AdminRole`

View organization webhook configurations. This includes access to webhook endpoints and event triggers.

#### Organization Webhook Update

```
organization_webhook:update
```

**Granted by default roles**: `AdminRole`

Modify an existing organization webhook. This allows updating endpoint URLs and event subscriptions.

### Stacks

#### Project Annotation Read

```
project_annotations:read
```

**Granted by default roles**: `MemberRole`, `AdminRole`

View annotations attached to a project. This provides context and metadata for project resources.

#### Project Annotation Update

```
project_annotations:update
```

**Granted by default roles**: `MemberRole`, `AdminRole`

Modify or add annotations to a project. This allows updating project metadata and documentation.

#### Project Decrypt

```
project:decrypt
```

**Granted by default roles**: `MemberRole`, `AdminRole`

Decrypt sensitive project data. This allows viewing encrypted configuration values and secrets.

#### Project Encrypt

```
project:encrypt
```

**Granted by default roles**: `MemberRole`, `AdminRole`

Encrypt project data. This secures sensitive information within the project.

### Search

#### Resources Dashboard

```
resources:dashboard
```

**Granted by default roles**: `MemberRole`, `AdminRole`, BillingManagerRole

View a dashboard of all resources managed by the organization. This provides a centralized overview of infrastructure.

#### Resources Index

```
resources:index
```

**Granted by default roles**: `AdminRole`

Index resources for search and discovery. This enables efficient querying and organization of resources.

#### Resources Search

```
resources:search
```

**Granted by default roles**: `MemberRole`, `AdminRole`

Search for resources within the organization. This allows users to find and access infrastructure components.

### Roles

#### Role Create

```
role:create
```

**Granted by default roles**: `AdminRole`

Create a new custom role for the organization. This allows defining specific sets of permissions.

#### Role Delete

```
role:delete
```

**Granted by default roles**: `AdminRole`

Delete a custom role from the organization. This removes the role and its associated permissions.

#### Role Read

```
role:read
```

**Granted by default roles**: `AdminRole`

View details of custom roles in the organization. This includes access to role definitions and assigned permissions.

#### Role Update

```
role:update
```

**Granted by default roles**: `AdminRole`

Modify an existing custom role. This allows updating the set of permissions assigned to the role.

### SSO

#### SAML Read

```
saml:read
```

**Granted by default roles**: `MemberRole`, `AdminRole`, BillingManagerRole

View SAML configuration and settings. This includes access to single sign-on provider details.

#### SAML Update

```
saml:update
```

**Granted by default roles**: `AdminRole`

Modify SAML configuration and settings. This allows updating single sign-on provider details.

#### SCIM Delete

```
scim:delete
```

**Granted by default roles**: `AdminRole`

Delete a SCIM integration. This removes automated user provisioning and management.

#### SCIM Read

```
scim:read
```

**Granted by default roles**: `AdminRole`

View SCIM integration settings. This includes access to automated user provisioning configurations.

#### SCIM Update

```
scim:update
```

**Granted by default roles**: `AdminRole`

Modify SCIM integration settings. This allows updating automated user provisioning configurations.

### Stacks

#### Stack List

```
stack:list
```

**Granted by default roles**: `MemberRole`, `AdminRole`

View a list of all stacks in the organization. This provides an overview of available stacks.

#### Stack List Deleted

```
stack:list_deleted
```

**Granted by default roles**: `AdminRole`

View a list of deleted stacks that are still recoverable. This helps in managing and potentially restoring stacks.

#### Tags Read

```
tags:read
```

**Granted by default roles**: `MemberRole`, `AdminRole`

View tags associated with projects. This provides access to project categorization and metadata.

### Teams

#### Team Create

```
team:create
```

**Granted by default roles**: `AdminRole`

**Granted by default permission**: TeamRoleAdmin

Create a new team within the organization. This enables grouping users for access control and collaboration.

#### Team Create Token

```
team:create_token
```

**Granted by default roles**: `AdminRole`

**Granted by default permission**: TeamRoleAdmin

Create a new token for team operations. This enables programmatic access for team-related actions.

#### Team Delete

```
team:delete
```

**Granted by default roles**: `AdminRole`

**Granted by default permission**: TeamRoleAdmin

Delete a team from the organization. This removes the team and its associated permissions.

#### Team Delete Token

```
team:delete_token
```

**Granted by default roles**: `AdminRole`

**Granted by default permission**: TeamRoleAdmin

Delete a team token. This revokes programmatic access for team-related actions.

#### Team List

```
team:list
```

**Granted by default roles**: `MemberRole`, `AdminRole`, BillingManagerRole

**Granted by default permission**: TeamRoleMember

View a list of all teams in the organization. This provides an overview of available teams.

#### Team List Tokens

```
team:list_tokens
```

**Granted by default roles**: `AdminRole`

**Granted by default permission**: TeamRoleAdmin

View all tokens associated with a team. This includes access to token details and usage.

#### Team Read

```
team:read
```

**Granted by default roles**: `MemberRole`, `AdminRole`

**Granted by default permission**: TeamRoleMember

View team details and settings. This includes access to team membership and configuration.

#### Team Update

```
team:update
```

**Granted by default roles**: `AdminRole`

**Granted by default permission**: TeamRoleAdmin

Modify team settings and membership. This allows updating team details and user assignments.

### Templates

#### Templates Read

```
templates:read
```

**Granted by default roles**: `MemberRole`, `AdminRole`

View available templates for infrastructure deployments. This includes access to template definitions and usage instructions.

#### Templates Source Create

```
templates:source:create
```

**Granted by default roles**: `AdminRole`

Create a new template source for infrastructure deployments. This allows adding new sources for reusable templates.

#### Templates Source Delete

```
templates:source:delete
```

**Granted by default roles**: `AdminRole`

Delete an existing template source. This removes the source and its associated templates.

#### Templates Source Read

```
templates:source:read
```

**Granted by default roles**: `AdminRole`

View template source configurations. This includes access to source details and available templates.

#### Templates Source Update

```
templates:source:update
```

**Granted by default roles**: `AdminRole`

Modify an existing template source. This allows updating source details and available templates.

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
