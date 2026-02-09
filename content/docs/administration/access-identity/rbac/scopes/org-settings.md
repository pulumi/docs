---
title_tag: "Pulumi Cloud: RBAC Scopes - Organization settings"
meta_desc: Learn about the available RBAC scopes in Pulumi Cloud.
title: "RBAC Scopes: Organization settings"
h1: "RBAC Scopes: Organization settings"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  administration:
    name: "Organization settings"
    parent: administration-access-identity-rbac-scopes
    weight: 4
    identifier: pulumi-cloud-access-management-rbac-scopes-org-settings
aliases:
- /docs/intro/pulumi-service/scopes/org-settings
- /docs/intro/pulumi-cloud/scopes/org-settings
- /docs/pulumi-cloud/access-management/rbac/scopes/org-settings/
---

This document defines all the available scopes in Pulumi Cloud, organized by [entity type](../permission-sets#entity-types) and group.

## Agent Pools

| Value | Description |
|-------|-------------|
| `agent_pool:create` | Create a new agent pool for running Pulumi operations. Agent pools provide isolated environments for executing infrastructure deployments.<br><br>**Granted by default roles**: `Admin` |
| `agent_pool:delete` | Remove an existing agent pool and its associated resources. This permanently deletes the pool and its configuration.<br><br>**Granted by default roles**: `Admin` |
| `agent_pool:read` | View agent pool configurations and status. This includes access to pool settings, agent status, and operational metrics.<br><br>**Granted by default roles**: `Admin` |
| `agent_pool:update` | Modify agent pool settings and configurations. This allows updating pool parameters, scaling settings, and agent configurations.<br><br>**Granted by default roles**: `Admin` |

## Audit Logs

| Value | Description |
|-------|-------------|
| `audit_logs:export` | Export audit log data for compliance and analysis purposes. This enables downloading audit records in various formats.<br><br>**Granted by default roles**: `Admin` |
| `audit_logs:read` | Access and view audit logs of organization activities. This provides visibility into system events and user actions.<br><br>**Granted by default roles**: `Admin` |

## AI

{{% notes "info" %}}
These scopes control access to Pulumi's AI features, including [Pulumi Neo](/docs/ai/).
{{% /notes %}}

| Value | Description |
|-------|-------------|
| `ai_conversations:create` | Create a new Copilot conversation session for interacting with Copilot, Pulumi's AI assistant. This allows users to start new conversations and get help with their infrastructure code.<br><br>**Granted by default roles**: `Member`, `Admin` |
| `ai_conversations:list_all` | View all Copilot conversations across the organization. This provides administrators with visibility into all AI assistant interactions.<br><br>**Granted by default roles**: `Admin` |
| `ai_conversations:read` | Access and view the content of Copilot conversations. This allows users to read their own conversations and continue previous interactions.<br><br>**Granted by default roles**: `Member`, `Admin` |
| `ai_conversations:update` | Modify and continue existing Copilot conversations. This enables users to update their conversations with new questions or context.<br><br>**Granted by default roles**: `Member`, `Admin` |

## Deployments

| Value | Description |
|-------|-------------|
| `deployments:pause` | Temporarily halt all deployment operations across the organization. This is useful for maintenance or emergency situations.<br><br>**Granted by default roles**: `Admin` |
| `deployments:read` | View deployment configurations and status across the organization. This provides visibility into all deployment activities.<br><br>**Granted by default roles**: `Member`, `Admin` |
| `deployments:read_usage` | Access deployment usage metrics and statistics. This includes information about resource consumption and operational costs.<br><br>**Granted by default roles**: `Member`, `Admin`, `Billing Manager` |
| `deployments:resume` | Resume deployment operations after a pause. This restores normal deployment functionality across the organization.<br><br>**Granted by default roles**: `Admin` |

## Environments

| Value | Description |
|-------|-------------|
| `environment:create` | Create a new environment for managing infrastructure configurations. Environments provide isolated spaces for different deployment stages.<br><br>**Granted by default roles**: `Member`, `Admin` |
| `environment:list` | View all environments in the organization. This provides a list of available environments and their basic information.<br><br>**Granted by default roles**: `Member`, `Admin` |
| `environment:list_deleted` | View a list of environments that have been recently deleted but are still recoverable.<br><br>**Granted by default roles**: `Member`, `Admin` |
| `environment:restore_deleted` | Recover a previously deleted environment. This restores the environment and its configurations to their previous state.<br><br>**Granted by default roles**: `Admin` |
| `environment_tags:list` | View all tags used across environments. This provides a comprehensive view of environment categorization.<br><br>**Granted by default permission set**: `Environment Read` |
| `environment_yaml:open` | Access and view environment configuration in YAML format. This provides a structured view of environment settings.<br><br>**Granted by default roles**: `Member`, `Admin` |

## Insights Accounts

| Value | Description |
|-------|-------------|
| `insights_account:create` | Create a new insights account. This allows setting up monitoring and analysis capabilities for infrastructure.<br><br>**Granted by default roles**: `Admin` |
| `insights_account:list` | View all insights accounts in the organization, subject to having `account:read` permissions on specific accounts.<br><br>**Granted by default roles**: `Member`, `Admin` |

## Insights Policy

| Value | Description |
|-------|-------------|
| `policy_groups:create` | Create a new group of Infrastructure as Code policies. This allows organizing related policies for better management and enforcement.<br><br>**Granted by default roles**: `Admin` |
| `policy_groups:delete` | Remove an existing group of Infrastructure as Code policies. This permanently deletes the policy group and its configurations.<br><br>**Granted by default roles**: `Admin` |
| `policy_groups:read` | View Infrastructure as Code policy group configurations. This includes access to policy definitions and enforcement rules.<br><br>**Granted by default roles**: `Member`, `Admin` |
| `policy_groups:update` | Modify Infrastructure as Code policy group settings. This allows updating policy definitions and enforcement parameters.<br><br>**Granted by default roles**: `Admin` |
| `policy_pack:create` | Create a new Infrastructure as Code policy pack. This allows bundling related policies for deployment and enforcement.<br><br>**Granted by default roles**: `Admin` |
| `policy_pack:delete` | Remove an existing Infrastructure as Code policy pack. This permanently deletes the policy pack and its configurations.<br><br>**Granted by default roles**: `Admin` |
| `policy_pack:read` | View Infrastructure as Code policy pack contents. This includes access to policy definitions and enforcement rules.<br><br>**Granted by default roles**: `Admin` |
| `policy_pack:update` | Modify an existing Infrastructure as Code policy pack. This allows updating policy definitions and enforcement parameters.<br><br>**Granted by default roles**: `Admin` |
| `policy_results:read` | View results of Infrastructure as Code policy evaluations. This provides insights into policy compliance and violations.<br><br>**Granted by default roles**: `Admin` |

## Membership

| Value | Description |
|-------|-------------|
| `org_member:add` | Add a new member to the organization. This enables expanding the team with new users.<br><br>**Granted by default roles**: `Admin` |
| `org_member:delete` | Remove a member from the organization. This revokes their access and permissions.<br><br>**Granted by default roles**: `Admin` |
| `org_member:read` | View details about organization members. This includes access to user profiles and roles.<br><br>**Granted by default roles**: `Member`, `Admin`, `Billing Manager` |
| `org_member:set_admin` | Grant or revoke admin privileges for an organization member. This controls elevated access.<br><br>**Granted by default roles**: `Admin` |
| `org_member:update` | Update organization member information and roles. This allows changing user details and permissions.<br><br>**Granted by default roles**: `Admin` |
| `org_requests:read` | View all organization requests. This provides visibility into pending and processed requests.<br><br>**Granted by default roles**: `Admin` |
| `org_requests:update` | Update or process organization requests. This allows approving or denying requests.<br><br>**Granted by default roles**: `Admin` |
| `invites:create` | Send invitations to new users to join the organization. This enables onboarding of new team members.<br><br>**Granted by default roles**: `Admin` |
| `invites:read` | View pending and sent invitations for organization membership. This provides visibility into user onboarding status.<br><br>**Granted by default roles**: `Admin` |

## OIDC

| Value | Description |
|-------|-------------|
| `oidc_issuers:create` | Register a new OIDC issuer for authentication. This allows adding new identity providers for user login.<br><br>**Granted by default roles**: `Admin` |
| `oidc_issuers:delete` | Remove an existing OIDC issuer. This permanently deletes the identity provider configuration.<br><br>**Granted by default roles**: `Admin` |
| `oidc_issuers:read` | View OIDC issuer configurations. This includes access to identity provider details and settings.<br><br>**Granted by default roles**: `Admin` |
| `oidc_issuers:regenerate_thumbprints` | Regenerate security thumbprints for an OIDC issuer. This is used to maintain secure authentication.<br><br>**Granted by default roles**: `Admin` |
| `oidc_issuers:update` | Modify OIDC issuer settings. This allows updating identity provider details and authentication parameters.<br><br>**Granted by default roles**: `Admin` |
| `auth_policies:read` | View authentication policy configurations. This includes access to OIDC, SAML, and other identity provider settings.<br><br>**Granted by default roles**: `Admin` |
| `auth_policies:update` | Modify authentication policies and identity provider settings. This allows updating security configurations

## Organization

| Value | Description |
|-------|-------------|
| `organization:billing` | Manage billing settings and payment methods for the organization. This includes access to invoices and payment history.<br><br>**Granted by default roles**: `Admin`, `Billing Manager` |
| `organization:change_backend` | Change the backend infrastructure for the organization. This is used for advanced configuration and migration.<br><br>**Granted by default roles**: `Admin` |
| `organization:delete` | Delete the organization and all its resources. This is a permanent and irreversible action.<br><br>**Granted by default roles**: `Admin` |
| `organization:read_usage` | View usage statistics and metrics for the organization. This includes resource consumption and cost data.<br><br>**Granted by default roles**: `Member`, `Admin`, `Billing Manager` |
| `organization:rename` | Change the name of the organization. This updates the organization's display name across the platform.<br><br>**Granted by default roles**: `Admin` |
| `organization:transfer_stacks` | Transfer ownership of stacks between organizations. This is used for organizational restructuring or migration.<br><br>**Granted by default roles**: `Admin` |
| `organization:update` | Update organization settings and configurations. This allows changing metadata, policies, and preferences.<br><br>**Granted by default roles**: `Admin` |
| `org_integrations:read` | View organization-level integration settings. This includes access to all configured integrations.<br><br>**Granted by default roles**: `Admin` |
| `org_integrations:update` | Update organization-level integration settings. This allows modifying or removing integrations.<br><br>**Granted by default roles**: `Admin` |
| `integrations:read` | View configuration settings on a per-resource level. This includes access to settings for third-party services and tools.<br><br>**Granted by default roles**: `Member`, `Admin` |
| `integrations:update` | Manage integration settings on a per-resource level. This allows updating or reconfiguring third-party service connections.<br><br>**Granted by default roles**: `Member`, `Admin` |

## Organization Tokens

| Value | Description |
|-------|-------------|
| `org_token:create` | Create a new organization API token. This enables programmatic access to organization resources.<br><br>**Granted by default roles**: `Admin` |
| `org_token:delete` | Delete an existing organization API token. This revokes programmatic access.<br><br>**Granted by default roles**: `Admin` |
| `org_token:read` | View organization API tokens. This includes access to token details and usage.<br><br>**Granted by default roles**: `Admin` |

## Organization Webhooks

| Value | Description |
|-------|-------------|
| `organization_webhook:create` | Create a new webhook for organization events. This enables integration with external systems for event notifications.<br><br>**Granted by default roles**: `Admin` |
| `organization_webhook:delete` | Delete an existing organization webhook. This removes the integration and stops event delivery.<br><br>**Granted by default roles**: `Admin` |
| `organization_webhook:read` | View organization webhook configurations. This includes access to webhook endpoints and event triggers.<br><br>**Granted by default roles**: `Admin` |
| `organization_webhook:update` | Modify an existing organization webhook. This allows updating endpoint URLs and event subscriptions.<br><br>**Granted by default roles**: `Admin` |

## Project

| Value | Description |
|-------|-------------|
| `project:decrypt` | Allows decrypting sensitive project-level data and secrets.<br><br>**Granted by default roles**: `Member`, `Admin` |
| `project:encrypt` | Allows encrypting sensitive project-level data and secrets.<br><br>**Granted by default roles**: `Member`, `Admin` |

## Resources

| Value | Description |
|-------|-------------|
| `resources:dashboard` | Allows viewing the resources dashboard that provides an overview of all resources across the organization.<br><br>**Granted by default roles**: `Member`, `Admin`, `Billing Manager` |
| `resources:index` | Allows accessing the main resources index page and managing resource listings.<br><br>**Granted by default roles**: `Admin` |
| `resources:search` | Allows searching and filtering through organization resources.<br><br>**Granted by default roles**: `Member`, `Admin` |

## Roles

| Value | Description |
|-------|-------------|
| `role:create` | Allows creating new custom roles with specific permission sets.<br><br>**Granted by default roles**: `Admin` |
| `role:delete` | Allows deleting existing custom roles.<br><br>**Granted by default roles**: `Admin` |
| `role:read` | Allows viewing role definitions and their associated permission sets.<br><br>**Granted by default roles**: `Admin` |
| `role:update` | Allows modifying existing custom roles and their permission sets.<br><br>**Granted by default roles**: `Admin` |

## SAML

| Value | Description |
|-------|-------------|
| `saml:read` | Allows viewing SAML configuration and settings for the organization.<br><br>**Granted by default roles**: `Member`, `Admin`, `Billing Manager` |
| `saml:update` | Allows configuring and updating SAML settings for the organization.<br><br>**Granted by default roles**: `Admin` |

## SCIM

| Value | Description |
|-------|-------------|
| `scim:delete` | Allows removing SCIM configurations and terminating SCIM integration.<br><br>**Granted by default roles**: `Admin` |
| `scim:read` | Allows viewing SCIM configuration and integration settings.<br><br>**Granted by default roles**: `Admin` |
| `scim:update` | Allows modifying SCIM configuration and integration settings.<br><br>**Granted by default roles**: `Admin` |

## Services

| Value | Description |
|-------|-------------|
| `services:admin` | Allows full administrative control over service configurations and settings.<br><br>**Granted by default roles**: `Member`, `Admin` |
| `services:create` | Allows creating new service instances and configurations.<br><br>**Granted by default roles**: `Member`, `Admin` |
| `services:read` | Allows viewing service configurations and their current state.<br><br>**Granted by default roles**: `Member`, `Admin` |
| `services:write` | Allows modifying existing service configurations and settings.<br><br>**Granted by default roles**: `Member`, `Admin` |

## Stacks

| Value | Description |
|-------|-------------|
| `stack:create` | Create a new stack for managing infrastructure resources. Stacks represent isolated units of deployment.<br><br>**Granted by default roles**: `Admin` |
| `stack:list` | View all stacks in the organization, subject to having `stack:read` permissions on specific stacks.<br><br>**Granted by default roles**: `Member`, `Admin` |
| `stack:list_deleted` | View a list of stacks that have been recently deleted but are still recoverable.<br><br>**Granted by default roles**: `Admin` |
| `stack:restore_deleted` | Recover a previously deleted stack. This restores the stack and its configurations to their previous state.<br><br>**Granted by default roles**: `Admin` |
| `stack_access:read` | View information about the users and teams that have access to a stack.<br><br>**Granted by default roles**: `Member`, `Admin` |

## Tags

| Value | Description |
|-------|-------------|
| `tags:read` | Allows viewing tags and their associated resources across the organization.<br><br>**Granted by default roles**: `Member`, `Admin` |

## Teams

| Value | Description |
|-------|-------------|
| `team:create` | Allows creating new teams within the organization.<br><br>**Granted by default roles**: `Admin` |
| `team:create_token` | Allows generating new access tokens for team authentication.<br><br>**Granted by default roles**: `Admin` |
| `team:delete` | Allows removing teams from the organization.<br><br>**Granted by default roles**: `Admin` |
| `team:delete_token` | Allows revoking team access tokens.<br><br>**Granted by default roles**: `Admin` |
| `team:list` | Allows viewing all teams in the organization.<br><br>**Granted by default roles**: `Member`, `Admin`, `Billing Manager` |
| `team:list_tokens` | Allows viewing all active access tokens for teams.<br><br>**Granted by default roles**: `Admin` |
| `team:read` | Allows viewing team details and membership information.<br><br>**Granted by default roles**: `Member`, `Admin` |
| `team:update` | Allows modifying team settings and membership.<br><br>**Granted by default roles**: `Admin` |
| `github_team:create` | Create a new team that syncs with GitHub. This enables integration between Pulumi and GitHub team structures.<br><br>**Granted by default roles**: `Admin` |

## Templates

| Value | Description |
|-------|-------------|
| `templates:read` | Allows viewing and using available templates for creating new projects and stacks.<br><br>**Granted by default roles**: `Member`, `Admin` |

## Template Sources

| Value | Description |
|-------|-------------|
| `templates_source:create` | Allows adding new template sources to the organization.<br><br>**Granted by default roles**: `Admin` |
| `templates_source:delete` | Allows removing template sources from the organization.<br><br>**Granted by default roles**: `Admin` |
| `templates_source:read` | Allows viewing template source configurations and available templates.<br><br>**Granted by default roles**: `Admin` |
| `templates_source:update` | Allows modifying template source configurations and settings.<br><br>**Granted by default roles**: `Admin` |
