---
title_tag: "Azure DevOps Integration | Integrations"
meta_desc: Connect Azure DevOps repositories to Pulumi Cloud Deployments to deploy on push, preview pull requests, and post PR summaries.
title: "Azure DevOps Integration"
h1: "Azure DevOps Integration"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    integrations:
        name: Azure DevOps Integration
        parent: integrations-home
        weight: 4
aliases:
- /docs/deployments/deployments/azure-devops/
- /docs/iac/guides/continuous-delivery/azure-devops-integration/
---

Pulumi Cloud supports Azure DevOps as a VCS provider for Deployments. Connect your ADO repositories to deploy on push, preview pull requests, and post PR summaries.

## Prerequisites

- A Pulumi Cloud organization
- An Azure DevOps organization and project
- Org admin access in Pulumi Cloud (for initial setup)
- An Azure AD tenant

## Configure the Azure DevOps integration

An org admin must set up the integration before users can connect ADO repos.

### Step 1: Navigate to integrations

Navigate to **Settings** > **Version control** in your Pulumi Cloud organization.

### Step 2: Authorize with Azure

Select **Authorize Azure DevOps**. This opens an OAuth popup that authenticates against Microsoft Entra ID (Azure AD). You'll authorize two scopes:

1. **Microsoft Graph**: lets Pulumi discover your Azure AD tenant and manage app registrations.
1. **Azure DevOps**: grants access to repos, projects, and service hooks.

### Step 3: Select ADO organization and project

After authorization, select the Azure DevOps organization and project to connect.

- Each integration maps one Pulumi org to one ADO org + project pair.
- You can create multiple integrations if you use multiple ADO projects.

### Step 4: Save the integration

Select **Save**. Pulumi registers service hooks in your ADO project for `git.push`, `git.pullrequest.created`, and `git.pullrequest.updated` events.

{{% notes type="info" %}}
To disconnect, remove all ADO integrations first, then select **Disconnect** from the identity dropdown.
{{% /notes %}}

## Integration settings

After creating an integration, you can configure PR behavior. Toggle these settings per integration:

| Setting | Default | Description |
|---|---|---|
| PR Comments | Enabled | Post deployment status and resource changes as comments on ADO pull requests |
| Neo Summaries | Enabled | Include AI-generated summaries of infrastructure changes in PR comments |
| Detailed Diff | Disabled | Show property-level before/after diffs for changed resources in PR comments |

To update, toggle the setting directly. Changes save automatically.

### Deleting an integration

Select **Delete Integration** on the integration card. This removes the service hooks from ADO and disconnects all stacks using that integration.

## Create a project with the new project wizard

Once an admin has configured an ADO integration and you've authorized your account, you can use the [New Project Wizard](/docs/idp/concepts/new-project-wizard/) to create projects backed by ADO repos. Select **Azure DevOps** as the VCS provider during project setup. If only one provider is configured, it's selected automatically.

## Deployment settings

ADO-backed stacks support the same deployment settings as GitHub. Configure these under **Stack** > **Settings** > **Deploy**.

| Setting | Description |
|---|---|
| Push to Deploy | Automatically deploy when commits are pushed to the configured branch |
| Preview Pull Requests | Run `pulumi preview` on pull request creation/update and post results as a PR comment |
| PR Templates | Create a PR with the preview results when running a preview |
| Path Filters | Only trigger deployments when files matching specified glob patterns change (e.g., `infra/**`) |

### Selecting a repository and branch

1. Choose the ADO integration (if multiple are configured).
1. Select a repository from the autocomplete dropdown.
1. Select the target branch.

## Per-project app authentication (OIDC)

For production workloads, configure OIDC-based authentication so Pulumi doesn't rely on individual user OAuth tokens. This uses Microsoft Entra ID federated credentials, so no long-lived access tokens are stored.

## Neo AI integration

Neo, Pulumi's AI assistant, works with Azure DevOps pull requests. When enabled (the default), Neo posts:

- **Change summaries**: plain-language explanation of what infrastructure changes a PR introduces.
- **Resource diff details**: property-level before/after comparisons for modified resources.

These appear as comments on your ADO pull requests alongside standard deployment status updates.

To disable Neo summaries, toggle **Neo Summaries** off in your [integration settings](#integration-settings).

## Troubleshooting

| Issue | Resolution |
|---|---|
| "Azure DevOps not enabled for tenant" (AADSTS650052) | An Azure AD admin must enable Azure DevOps access for your tenant |
| Integration shows as invalid | Delete the integration and re-create it. Ensure service hooks were registered successfully in ADO |
| Deployments not triggering on push | Verify the service hooks exist in **ADO Project Settings > Service hooks**. Check that the branch matches your deployment settings |
| OIDC token exchange fails | Verify the federated credential issuer, subject, and audience match exactly. Check the service principal has ADO access |
| "Remove all integrations before disconnecting" | You must delete all ADO integrations before you can disconnect your Azure DevOps identity |
