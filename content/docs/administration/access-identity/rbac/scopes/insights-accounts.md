---
title_tag: "Pulumi Cloud: RBAC Scopes - Insights accounts"
meta_desc: Learn about the available RBAC scopes in Pulumi Cloud.
title: "RBAC Scopes: Insights accounts"
h1: "RBAC Scopes: Insights accounts"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  administration:
    name: "Insights accounts"
    parent: administration-access-identity-rbac-scopes
    weight: 4
    identifier: pulumi-cloud-access-management-rbac-scopes-insights-accounts
aliases:
- /docs/intro/pulumi-service/scopes/insights-accounts
- /docs/intro/pulumi-cloud/scopes/insights-accounts
- /docs/pulumi-cloud/access-management/rbac/scopes/insights-accounts/
---

This document defines all the available [scopes](../) in Pulumi Cloud assignable to specific insights accounts or sets of insights accounts.

Note that creating, listing, or restoring insights accounts are organization-level operations, and these scopes can be found in the [organization settings scopes](../org-settings).

## Insights Accounts

| Value | Description |
|-------|-------------|
| `insights_account_access:read` | View what users and roles can access an insights account.<br><br>**Granted by default permission set**: `Account Read` |
| `insights_account_access:update` | Manage what users and roles can access an insights account.<br><br>**Granted by default permission set**: `Account Admin` |
| `insights_account:delete` | Remove an existing insights account. This permanently deletes the account and its associated data.<br><br>**Granted by default permission set**: `Account Admin` |
| `insights_account:read` | View insights account configurations and data. This includes access to monitoring settings and analysis results.<br><br>**Granted by default permission set**: `Account Read` |
| `insights_account:update` | Modify insights account settings and configurations. This allows updating monitoring parameters and analysis rules.<br><br>**Granted by default permission set**: `Account Write` |
| `insights_account:update_policy_results` | Update policy evaluation results for an insights account. This allows refreshing compliance data and analysis.<br><br>**Granted by default permission set**: `Account Write` |

## Insights Scan

| Value | Description |
|-------|-------------|
| `insights_account:scan` | Initiate a new scan of an insights account. This triggers analysis of infrastructure configurations and compliance.<br><br>**Granted by default permission set**: `Account Write` |
| `insights_account_scan:cancel` | Stop an ongoing insights account scan. This halts the current analysis process.<br><br>**Granted by default permission set**: `Account Write` |
| `insights_account_scan:pause` | Temporarily suspend an insights account scan. This pauses the analysis process without losing progress.<br><br>**Granted by default permission set**: `Account Write` |
| `insights_account_scan:read` | View insights account scan results and status. This includes access to analysis findings and progress.<br><br>**Granted by default permission set**: `Account Read` |
| `insights_account_scan:resume` | Resume a paused insights account scan. This continues the analysis process from where it was paused.<br><br>**Granted by default permission set**: `Account Write` |
| `insights_account_scan:update` | Modify insights account scan settings. This allows updating scan parameters and analysis configurations.<br><br>**Granted by default permission set**: `Account Write` |
