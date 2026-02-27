---
title_tag: "Azure DevOps Integration | Pulumi Deployments"
meta_desc: Connect Azure DevOps repositories to Pulumi Cloud Deployments to deploy on push, preview pull requests, and get AI-powered PR summaries.
title: "Azure DevOps Integration"
h1: "Azure DevOps Integration"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  deployments:
    parent: deployments-deployments
    weight: 25
    identifier: deployments-deployments-azure-devops
---

Pulumi Cloud supports Azure DevOps as a VCS provider for Deployments. Connect your ADO repositories to deploy infrastructure on push, preview pull requests, and get AI-powered PR summaries — the same workflow available for GitHub.

## Prerequisites

- A Pulumi Cloud organization (Team or Enterprise)
- An Azure DevOps organization and project
- Org admin access in Pulumi Cloud (for initial setup)
- An Azure AD tenant (required for OIDC; optional for basic OAuth setup)

## Admin: Configure the Azure DevOps integration

An org admin must set up the integration before users can connect ADO repos.

### Step 1: Navigate to integrations

Go to **Settings > Integrations** in your Pulumi Cloud organization.

<!-- [SCREENSHOT: Org settings page showing Integrations tab with Azure DevOps card] -->

### Step 2: Authorize with Azure

Click **Authorize Azure DevOps**. This opens an OAuth popup that authenticates against Microsoft Entra ID (Azure AD). You'll authorize two scopes:

1. **Microsoft Graph** — lets Pulumi discover your Azure AD tenant and manage app registrations.
1. **Azure DevOps** — grants access to repos, projects, and service hooks (`vso.code`, `vso.identity`, `vso.project_manage`).

<!-- [SCREENSHOT: OAuth consent popup showing requested permissions] -->

### Step 3: Select ADO organization and project

After authorization, select the Azure DevOps organization and project to connect.

- Each integration maps one Pulumi org to one ADO org + project pair.
- You can create multiple integrations if you use multiple ADO projects.

<!-- [SCREENSHOT: Org and project dropdown selectors in integration setup form] -->

### Step 4: Save the integration

Click **Save**. Pulumi registers service hooks in your ADO project for `git.push`, `git.pullrequest.created`, and `git.pullrequest.updated` events.

<!-- [SCREENSHOT: Saved integration showing org/project name and status] -->

## User: Connect your Azure DevOps account

Each user who wants to use ADO repos must authorize their own account.

### Step 1: Go to integrations

Navigate to **Settings > Integrations** in your org. Under the Azure DevOps section, click **Authorize Azure DevOps**.

### Step 2: Complete OAuth

The same two-stage OAuth flow runs (Graph + ADO). Once complete, the popup closes and your identity shows as **Connected**.

<!-- [SCREENSHOT: Azure DevOps identity showing "Connected" status] -->

{{% notes type="info" %}}
To disconnect, remove all ADO integrations first, then click **Disconnect** from the identity dropdown.
{{% /notes %}}

## Integration settings

After creating an integration, you can configure PR behavior. Toggle these settings per integration:

| Setting | Default | Description |
|---|---|---|
| PR Comments | Enabled | Post deployment status and resource changes as comments on ADO pull requests |
| Neo Summaries | Enabled | Include AI-generated summaries of infrastructure changes in PR comments |
| Detailed Diff | Enabled | Show property-level before/after diffs for changed resources in PR comments |

<!-- [SCREENSHOT: Integration settings showing the three toggles] -->

To update, toggle the setting directly — changes save automatically.

### Deleting an integration

Click **Delete Integration** on the integration card. This removes the service hooks from ADO and disconnects all stacks using that integration.

## Create a project with the New Project Wizard

Once an admin has configured an ADO integration and you've authorized your account, you can create projects backed by ADO repos.

### Step 1: Open the New Project Wizard

Click **New Project** from your org's dashboard.

### Step 2: Select a template

Choose a starter template or start from scratch.

<!-- [SCREENSHOT: Template selection step in NPW] -->

### Step 3: Select Azure DevOps as the VCS provider

In the project details step, select **Azure DevOps** from the VCS provider dropdown. If only one provider is configured, it's selected automatically.

<!-- [SCREENSHOT: VCS provider selector showing GitHub and Azure DevOps options] -->

### Step 4: Choose a repository

Select an existing repository from the dropdown, or create a new one by entering a name.

<!-- [SCREENSHOT: Repository selector/creation field] -->

### Step 5: Choose a branch

Pick the branch to deploy from. Defaults to the repo's default branch.

<!-- [SCREENSHOT: Branch selector dropdown] -->

### Step 6: Configure and deploy

Set your project name, stack name, and any required configuration values. Click **Create Project** to push the template and trigger the initial deployment.

<!-- [SCREENSHOT: Final configuration step before project creation] -->

## Deployment settings

ADO-backed stacks support the same deployment settings as GitHub. Configure these under **Stack > Settings > Deploy**.

| Setting | Description |
|---|---|
| Push to Deploy | Automatically deploy when commits are pushed to the configured branch |
| Preview Pull Requests | Run `pulumi preview` on pull request creation/update and post results as a PR comment |
| PR Templates | Create a PR with the preview results when running a preview |
| Path Filters | Only trigger deployments when files matching specified glob patterns change (e.g., `infra/**`) |

<!-- [SCREENSHOT: Stack deployment settings page with ADO repo selected] -->

### Selecting a repository and branch

1. Choose the ADO integration (if multiple are configured).
1. Select a repository from the autocomplete dropdown.
1. Select the target branch.

<!-- [SCREENSHOT: Repository and branch selection in deployment settings] -->

## Per-project app authentication (OIDC)

For production workloads, configure OIDC-based authentication so Pulumi doesn't rely on individual user OAuth tokens. This uses Microsoft Entra ID federated credentials — no long-lived access tokens are stored.

### How it works

1. Pulumi issues a short-lived OIDC JWT with claims identifying your org and project.
1. The JWT is exchanged for an Azure AD access token using a federated credential on an app registration in your tenant.
1. The Azure AD token authenticates against the Azure DevOps API.

### Setup

#### Step 1: Create an app registration in Azure AD

In the Azure portal, create (or reuse) an app registration in your tenant. Note the:

- **Application (client) ID**
- **Directory (tenant) ID**
- **Object ID** of the associated service principal

#### Step 2: Add a federated credential

On the app registration, go to **Certificates & secrets > Federated credentials > Add credential**.

Configure:

- **Issuer:** Your Pulumi Cloud OIDC issuer URL (e.g., `https://api.pulumi.com/oidc`)
- **Subject:** `pulumi:ado:org:<your-pulumi-org>:project:<ado-project-id>`
- **Audience:** `azure:<ado-org-name>`

<!-- [SCREENSHOT: Azure portal federated credential configuration] -->

#### Step 3: Grant ADO permissions

Ensure the service principal has appropriate permissions in your Azure DevOps organization (typically at least Basic access level and contributor to the target project).

#### Step 4: Configure in Pulumi Cloud

The per-project app credential is associated with your ADO integration. Once configured, Pulumi uses OIDC token exchange for all deployment operations. If OIDC is not configured, Pulumi falls back to the authorizing user's OAuth token.

<!-- [SCREENSHOT: Per-project app credential status in integration settings] -->

## Neo AI integration

Neo, Pulumi's AI assistant, works with Azure DevOps pull requests. When enabled (the default), Neo posts:

- **Change summaries** — AI-generated plain-language explanation of what infrastructure changes a PR introduces.
- **Resource diff details** — property-level before/after comparisons for modified resources.

These appear as comments on your ADO pull requests alongside standard deployment status updates.

To disable Neo summaries, toggle **Neo Summaries** off in your [integration settings](#integration-settings).

<!-- [SCREENSHOT: Example Neo PR comment on an Azure DevOps pull request] -->

## Troubleshooting

| Issue | Resolution |
|---|---|
| "Azure DevOps not enabled for tenant" (AADSTS650052) | An Azure AD admin must enable Azure DevOps access for your tenant |
| Integration shows as invalid | Delete the integration and re-create it. Ensure service hooks were registered successfully in ADO |
| OAuth token expired | Re-authorize via **Settings > Integrations > Authorize Azure DevOps** |
| Deployments not triggering on push | Verify the service hooks exist in **ADO Project Settings > Service hooks**. Check that the branch matches your deployment settings |
| OIDC token exchange fails | Verify the federated credential issuer, subject, and audience match exactly. Check the service principal has ADO access |
| "Remove all integrations before disconnecting" | You must delete all ADO integrations before you can disconnect your Azure DevOps identity |
