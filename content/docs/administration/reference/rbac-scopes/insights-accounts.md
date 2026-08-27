---
title_tag: "Pulumi Cloud: RBAC Scopes - Cloud accounts"
meta_desc: Learn about the available RBAC scopes in Pulumi Cloud.
title: "RBAC Scopes: Cloud Accounts"
h1: "RBAC Scopes: Cloud Accounts"
menu:
  administration:
    name: "Cloud accounts"
    parent: administration-reference-rbac-scopes
    weight: 3
    identifier: pulumi-cloud-access-management-rbac-scopes-insights-accounts
aliases:
- /docs/intro/pulumi-service/scopes/insights-accounts
- /docs/intro/pulumi-cloud/scopes/insights-accounts
- /docs/pulumi-cloud/access-management/rbac/scopes/insights-accounts/
- /docs/administration/access-identity/rbac/scopes/insights-accounts/
pulumi_cloud_feature: rbac
---

This document defines all the available [scopes](/docs/administration/concepts/rbac/scopes/) in Pulumi Cloud assignable to specific cloud accounts or sets of cloud accounts.

Note that creating, listing, or restoring cloud accounts are organization-level operations, and these scopes can be found in the [organization settings scopes](/docs/administration/reference/rbac-scopes/org-settings).

## Cloud accounts

| Value | Description |
|-------|-------------|
| `insights_account_access:read` | View what users and roles can access a cloud account.<br><br>**Granted by default permission set**: `Account Read` |
| `insights_account_access:update` | Manage what users and roles can access a cloud account.<br><br>**Granted by default permission set**: `Account Admin` |
| `insights_account:delete` | Remove an existing cloud account. This permanently deletes the account and its associated data.<br><br>**Granted by default permission set**: `Account Admin` |
| `insights_account:read` | View cloud account configurations and data. This includes access to monitoring settings and analysis results.<br><br>**Granted by default permission set**: `Account Read` |
| `insights_account:update` | Modify cloud account settings and configurations. This allows updating monitoring parameters and analysis rules.<br><br>**Granted by default permission set**: `Account Write` |

## Cloud account scans

| Value | Description |
|-------|-------------|
| `insights_account:scan` | Initiate a new scan of a cloud account. This triggers analysis of infrastructure configurations and compliance.<br><br>**Granted by default permission set**: `Account Write` |
| `insights_account_scan:cancel` | Stop an ongoing cloud account scan. This halts the current analysis process.<br><br>**Granted by default permission set**: `Account Write` |
| `insights_account_scan:pause` | Temporarily suspend a cloud account scan. This pauses the analysis process without losing progress.<br><br>**Granted by default permission set**: `Account Write` |
| `insights_account_scan:read` | View cloud account scan results and status. This includes access to analysis findings and progress.<br><br>**Granted by default permission set**: `Account Read` |
| `insights_account_scan:resume` | Resume a paused cloud account scan. This continues the analysis process from where it paused.<br><br>**Granted by default permission set**: `Account Write` |
| `insights_account_scan:update` | Modify cloud account scan settings. This allows updating scan parameters and analysis configurations.<br><br>**Granted by default permission set**: `Account Write` |
