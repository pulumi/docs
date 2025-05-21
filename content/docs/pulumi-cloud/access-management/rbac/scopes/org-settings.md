---
title_tag: "Pulumi Cloud: RBAC Scopes - Organization settings"
meta_desc: Learn about the available RBAC scopes in Pulumi Cloud.
title: "RBAC Scopes: Organization settings"
h1: "RBAC Scopes: Organization settings"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: "Organization settings"
    parent: pulumi-cloud-access-management-rbac-scopes
    weight: 4
    identifier: pulumi-cloud-access-management-rbac-scopes-org-settings
aliases:
- /docs/intro/pulumi-service/scopes/org-settings
- /docs/intro/pulumi-cloud/scopes/org-settings
---

This document defines all the available scopes in Pulumi Cloud, organized by [entity type](../../permissions#entity-types) and group.

## AI

| Value | Description |
|-------|-------------|
| `ai_conversations:create` | Create a new AI conversation session for interacting with Pulumi's AI assistant. This allows users to start new conversations and get help with their infrastructure code.<br><br>**Granted by default roles**: `Member`, `Admin` |
| `ai_conversations:list_all` | View all AI conversations across the organization. This provides administrators with visibility into all AI assistant interactions.<br><br>**Granted by default roles**: `Admin` |
| `ai_conversations:read` | Access and view the content of AI conversations. This allows users to read their own conversations and continue previous interactions.<br><br>**Granted by default roles**: `Member`, `Admin` |
| `ai_conversations:update` | Modify and continue existing AI conversations. This enables users to update their conversations with new questions or context.<br><br>**Granted by default roles**: `Member`, `Admin` |

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

## OIDC

| Value | Description |
|-------|-------------|
| `auth_policies:read` | View authentication policy configurations. This includes access to OIDC, SAML, and other identity provider settings.<br><br>**Granted by default roles**: `Admin` |
| `auth_policies:update` | Modify authentication policies and identity provider settings. This allows updating security configurations and access rules.<br><br>**Granted by default roles**: `Admin` |

## Org Deployments

| Value | Description |
|-------|-------------|
| `deployments:pause` | Temporarily halt all deployment operations across the organization. This is useful for maintenance or emergency situations.<br><br>**Granted by default roles**: `Admin` |
| `deployments:read` | View deployment configurations and status across the organization. This provides visibility into all deployment activities.<br><br>**Granted by default roles**: `Member`, `Admin` |
| `deployments:read_usage` | Access deployment usage metrics and statistics. This includes information about resource consumption and operational costs.<br><br>**Granted by default roles**: `Member`, `Admin`, `Billing Manager` |
| `deployments:resume` | Resume deployment operations after a pause. This restores normal deployment functionality across the organization.<br><br>**Granted by default roles**: `Admin` |

## IaC Policy

| Value | Description |
|-------|-------------|
| `iac_policy_groups:create` | Create a new group of Infrastructure as Code policies. This allows organizing related policies for better management and enforcement.<br><br>**Granted by default roles**: `Admin` |
| `iac_policy_groups:delete` | Remove an existing group of Infrastructure as Code policies. This permanently deletes the policy group and its configurations.<br><br>**Granted by default roles**: `Admin` |
| `iac_policy_groups:read` | View Infrastructure as Code policy group configurations. This includes access to policy definitions and enforcement rules.<br><br>**Granted by default roles**: `Member`, `Admin` |
| `iac_policy_groups:update` | Modify Infrastructure as Code policy group settings. This allows updating policy definitions and enforcement parameters.<br><br>**Granted by default roles**: `Admin` |
| `iac_policy_pack:create` | Create a new Infrastructure as Code policy pack. This allows bundling related policies for deployment and enforcement.<br><br>**Granted by default roles**: `Admin` |
| `iac_policy_pack:delete` | Remove an existing Infrastructure as Code policy pack. This permanently deletes the policy pack and its configurations.<br><br>**Granted by default roles**: `Admin` |
| `iac_policy_pack:read` | View Infrastructure as Code policy pack contents. This includes access to policy definitions and enforcement rules.<br><br>**Granted by default roles**: `Admin` |
| `iac_policy_pack:update` | Modify an existing Infrastructure as Code policy pack. This allows updating policy definitions and enforcement parameters.<br><br>**Granted by default roles**: `Admin` |
| `iac_policy_results:read` | View results of Infrastructure as Code policy evaluations. This provides insights into policy compliance and violations.<br><br>**Granted by default roles**: `Admin` |

## Membership

| Value | Description |
|-------|-------------|
| `invites:create` | Send invitations to new users to join the organization. This enables onboarding of new team members.<br><br>**Granted by default roles**: `Admin` |
| `invites:read` | View pending and sent invitations for organization membership. This provides visibility into user onboarding status.<br><br>**Granted by default roles**: `Admin` |

## Organization

| Value | Description |
|-------|-------------|
| `integrations:read` | View integration configurations for the organization. This includes access to settings for third-party services and tools.<br><br>**Granted by default roles**: `Member`, `Admin` |
| `integrations:update` | Modify integration settings for the organization. This allows updating or reconfiguring third-party service connections.<br><br>**Granted by default roles**: `Member`, `Admin` |

## OIDC

| Value | Description |
|-------|-------------|
| `oidc_issuers:create` | Register a new OIDC issuer for authentication. This allows adding new identity providers for user login.<br><br>**Granted by default roles**: `Admin` |
| `oidc_issuers:delete` | Remove an existing OIDC issuer. This permanently deletes the identity provider configuration.<br><br>**Granted by default roles**: `Admin` |
| `oidc_issuers:read` | View OIDC issuer configurations. This includes access to identity provider details and settings.<br><br>**Granted by default roles**: `Admin` |
| `oidc_issuers:regenerate_thumbprints` | Regenerate security thumbprints for an OIDC issuer. This is used to maintain secure authentication.<br><br>**Granted by default roles**: `Admin` |
| `oidc_issuers:update` | Modify OIDC issuer settings. This allows updating identity provider details and authentication parameters.<br><br>**Granted by default roles**: `Admin` |

## Organization

| Value | Description |
|-------|-------------|
| `org_integrations:read` | View organization-level integration settings. This includes access to all configured integrations.<br><br>**Granted by default roles**: `Admin` |
| `org_integrations:update` | Update organization-level integration settings. This allows modifying or removing integrations.<br><br>**Granted by default roles**: `Admin` |

## Membership

| Value | Description |
|-------|-------------|
| `org_member:access` | Access organization member details and permissions. This is used for managing user roles and access.<br><br>**Granted by default roles**: `Admin` |
| `org_member:add` | Add a new member to the organization. This enables expanding the team with new users.<br><br>**Granted by default roles**: `Admin` |
| `org_member:delete` | Remove a member from the organization. This revokes their access and permissions.<br><br>**Granted by default roles**: `Admin` |
| `org_member:read` | View details about organization members. This includes access to user profiles and roles.<br><br>**Granted by default roles**: `Member`, `Admin`, `Billing Manager` |
| `org_member:set_admin` | Grant or revoke admin privileges for an organization member. This controls elevated access.<br><br>**Granted by default roles**: `Admin` |
| `org_member:update` | Update organization member information and roles. This allows changing user details and permissions.<br><br>**Granted by default roles**: `Admin` |
| `org_requests:create` | Submit a new request to join or interact with the organization. This is used for onboarding or special access. |
| `org_requests:read` | View all organization requests. This provides visibility into pending and processed requests.<br><br>**Granted by default roles**: `Admin` |
| `org_requests:status` | Check the status of an organization request. This helps track onboarding or access progress. |
| `org_requests:update` | Update or process organization requests. This allows approving or denying requests.<br><br>**Granted by default roles**: `Admin` |

## Organization Tokens

| Value | Description |
|-------|-------------|
| `org_token:create` | Create a new organization API token. This enables programmatic access to organization resources.<br><br>**Granted by default roles**: `Admin` |
| `org_token:delete` | Delete an existing organization API token. This revokes programmatic access.<br><br>**Granted by default roles**: `Admin` |
| `org_token:read` | View organization API tokens. This includes access to token details and usage.<br><br>**Granted by default roles**: `Admin` |

## Annotations

| Value | Description |
|-------|-------------|
| `organization_annotations:read` | View annotations attached to the organization. This provides context and metadata for organizational resources.<br><br>**Granted by default roles**: `Member`, `Admin` |
| `organization_annotations:update` | Modify or add annotations to the organization. This allows updating organizational metadata.<br><br>**Granted by default roles**: `Admin` |

## Organization

| Value | Description |
|-------|-------------|
| `organization:billing` | Manage billing settings and payment methods for the organization. This includes access to invoices and payment history.<br><br>**Granted by default roles**: `Admin`, `Billing Manager` |
| `organization:change_backend` | Change the backend infrastructure for the organization. This is used for advanced configuration and migration.<br><br>**Granted by default roles**: `Admin` |
| `organization:delete` | Delete the organization and all its resources. This is a permanent and irreversible action.<br><br>**Granted by default roles**: `Admin` |
| `organization:read` | View organization details and settings. This includes access to organizational metadata and configuration.<br><br>**Granted by default roles**: `Member`, `Admin`, `Billing Manager` |
| `organization:read_activity` | View recent activity and audit logs for the organization. This provides insight into changes and events.<br><br>**Granted by default roles**: `Member`, `Admin`, `Billing Manager` |
| `organization:read_usage` | View usage statistics and metrics for the organization. This includes resource consumption and cost data.<br><br>**Granted by default roles**: `Member`, `Admin`, `Billing Manager` |
| `organization:rename` | Change the name of the organization. This updates the organization's display name across the platform.<br><br>**Granted by default roles**: `Admin` |
| `organization:transfer_stacks` | Transfer ownership of stacks between organizations. This is used for organizational restructuring or migration.<br><br>**Granted by default roles**: `Admin` |
| `organization:update` | Update organization settings and configurations. This allows changing metadata, policies, and preferences.<br><br>**Granted by default roles**: `Admin` |

## Org Webhooks

| Value | Description |
|-------|-------------|
| `organization_webhook:create` | Create a new webhook for organization events. This enables integration with external systems for event notifications.<br><br>**Granted by default roles**: `Admin` |
| `organization_webhook:delete` | Delete an existing organization webhook. This removes the integration and stops event delivery.<br><br>**Granted by default roles**: `Admin` |
| `organization_webhook:read` | View organization webhook configurations. This includes access to webhook endpoints and event triggers.<br><br>**Granted by default roles**: `Admin` |
| `organization_webhook:update` | Modify an existing organization webhook. This allows updating endpoint URLs and event subscriptions.<br><br>**Granted by default roles**: `Admin` |

## Project Annotations

| Value | Description |
|-------|-------------|
| `project_annotations:read` | [placeholder]<br><br>**Granted by default roles**: `Member`, `Admin` |
| `project_annotations:update` | [placeholder]<br><br>**Granted by default roles**: `Member`, `Admin` |

## Project

| Value | Description |
|-------|-------------|
| `project:decrypt` | [placeholder]<br><br>**Granted by default roles**: `Member`, `Admin` |
| `project:encrypt` | [placeholder]<br><br>**Granted by default roles**: `Member`, `Admin` |

## Resources

| Value | Description |
|-------|-------------|
| `resources:dashboard` | [placeholder]<br><br>**Granted by default roles**: `Member`, `Admin`, `Billing Manager` |
| `resources:index` | [placeholder]<br><br>**Granted by default roles**: `Admin` |
| `resources:search` | [placeholder]<br><br>**Granted by default roles**: `Member`, `Admin` |

## Roles

| Value | Description |
|-------|-------------|
| `role:create` | [placeholder]<br><br>**Granted by default roles**: `Admin` |
| `role:delete` | [placeholder]<br><br>**Granted by default roles**: `Admin` |
| `role:read` | [placeholder]<br><br>**Granted by default roles**: `Admin` |
| `role:update` | [placeholder]<br><br>**Granted by default roles**: `Admin` |

## SAML

| Value | Description |
|-------|-------------|
| `saml:read` | [placeholder]<br><br>**Granted by default roles**: `Member`, `Admin`, `Billing Manager` |
| `saml:update` | [placeholder]<br><br>**Granted by default roles**: `Admin` |

## SCIM

| Value | Description |
|-------|-------------|
| `scim:delete` | [placeholder]<br><br>**Granted by default roles**: `Admin` |
| `scim:read` | [placeholder]<br><br>**Granted by default roles**: `Admin` |
| `scim:update` | [placeholder]<br><br>**Granted by default roles**: `Admin` |

## Services

| Value | Description |
|-------|-------------|
| `services:admin` | [placeholder]<br><br>**Granted by default roles**: `Member`, `Admin` |
| `services:create` | [placeholder]<br><br>**Granted by default roles**: `Member`, `Admin` |
| `services:read` | [placeholder]<br><br>**Granted by default roles**: `Member`, `Admin` |
| `services:write` | [placeholder]<br><br>**Granted by default roles**: `Member`, `Admin` |

## Tags

| Value | Description |
|-------|-------------|
| `tags:read` | [placeholder]<br><br>**Granted by default roles**: `Member`, `Admin` |

## Teams

| Value | Description |
|-------|-------------|
| `team:create` | [placeholder]<br><br>**Granted by default roles**: `Admin` |
| `team:create_token` | [placeholder]<br><br>**Granted by default roles**: `Admin` |
| `team:delete` | [placeholder]<br><br>**Granted by default roles**: `Admin` |
| `team:delete_token` | [placeholder]<br><br>**Granted by default roles**: `Admin` |
| `team:list` | [placeholder]<br><br>**Granted by default roles**: `Member`, `Admin`, `Billing Manager` |
| `team:list_tokens` | [placeholder]<br><br>**Granted by default roles**: `Admin` |
| `team:read` | [placeholder]<br><br>**Granted by default roles**: `Member`, `Admin` |
| `team:update` | [placeholder]<br><br>**Granted by default roles**: `Admin` |
| `github_team:create` | Create a new team that syncs with GitHub. This enables integration between Pulumi and GitHub team structures.<br><br>**Granted by default roles**: `Admin` |

## Templates

| Value | Description |
|-------|-------------|
| `templates:read` | [placeholder]<br><br>**Granted by default roles**: `Member`, `Admin` |

## Template Sources

| Value | Description |
|-------|-------------|
| `templates:source:create` | [placeholder]<br><br>**Granted by default roles**: `Admin` |
| `templates:source:delete` | [placeholder]<br><br>**Granted by default roles**: `Admin` |
| `templates:source:read` | [placeholder]<br><br>**Granted by default roles**: `Admin` |
| `templates:source:update` | [placeholder]<br><br>**Granted by default roles**: `Admin` |
