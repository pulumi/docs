---
title: External MCP integrations
title_tag: External MCP integrations | Pulumi Agents
h1: External MCP integrations
meta_desc: Connect Pulumi Agents to issue trackers, monitoring tools, and other providers through external Model Context Protocol servers.
aliases:
- /docs/ai/integrations/mcp/
- /docs/ai/neo/integrations/mcp/
menu:
    ai:
        name: External MCP integrations
        parent: ai-agents-integrations
        weight: 30
        identifier: ai-integrations-mcp
---

MCP integrations let Pulumi Agents use tools from external providers through [Model Context Protocol](https://modelcontextprotocol.io/) servers. A teammate with permission to manage organization integrations (`org_integrations:update`) connects each provider with credentials stored in Pulumi Cloud. Agents can use these tools to query monitoring data, read runbooks, and work with issues during a task.

> [!INFO]
> To give an external coding agent access to Pulumi context, see the [Pulumi MCP server](/docs/ai/guides/set-up-mcp-server/).

Supported integrations are Atlassian (Jira and Confluence), Cloudflare, Dash0, Datadog, Honeycomb, Linear, New Relic, PagerDuty, Sentry, and Supabase.

## Enabling an MCP integration

To enable an integration, navigate to **Agent Settings**, select **Integrations**, open **MCP servers**, find the provider under **Available**, and select **Authorize**. Enter the required credentials, then select **Save**.

Each MCP integration connects to the service's MCP server. Available tools depend on the credentials and authentication method the service supports.

## Credential storage

Integration credentials are encrypted at rest in Pulumi Cloud using a per-organization encryption key. When a task needs to connect to an integration, Pulumi Cloud decrypts the credentials at task time, constructs the appropriate authentication headers, and connects to the service on the agent's behalf. Credentials are never exposed to the language model and are never embedded in task state.

## Disabling an integration

To remove an integration from your organization, navigate to **Agent Settings**, select **Integrations**, open **MCP servers**, find the integration, and select **Manage integration**, then **Disconnect integration**.

Disabling an integration deletes its stored credentials and immediately prevents any new tasks from using it. Existing tasks reload the available integrations when the agent next resumes work. To revoke credentials already in use, revoke them at the provider.

## Per-task control

For tasks started from an agent you configure, [select MCP integrations in the agent configuration](/docs/ai/agents/configure/#connect-the-tools-it-needs). The saved selection applies across that agent's tasks.

Neo tasks inherit all integrations enabled by the organization. Before starting a task, turn off any integrations it does not need in the task composer. This selection applies only to that task.

## If an integration fails

If an integration fails, check that its credentials are valid, that they grant access to the requested data, and that the provider's MCP server is reachable. To replace expired credentials, disconnect the integration, then connect it again with new credentials.

Some connection failures leave other tools available. A failure to retrieve or decrypt stored credentials can prevent a task from starting or continuing.

## Configuration

### Atlassian (Jira and Confluence)

1. In Atlassian Administration, select your organization, then open **Connectors** > **Atlassian MCP server**. Under **Authentication**, turn on **API token**.
1. Open **Directory** > **Service accounts**, create or select a service account, and give it access to the products the agent needs.
1. Select **Create credentials** > **API token**. Choose an expiration date and the scopes the agent needs, then copy the token.
1. In the Pulumi integration form, enter the **Service Account API Token** and your **Site URL**, such as `https://yoursite.atlassian.net`.

See Atlassian's [MCP authentication settings](https://support.atlassian.com/security-and-access-policies/docs/control-atlassian-mcp-server-settings/#Configure-authentication) and [service account API tokens](https://support.atlassian.com/user-management/docs/manage-api-tokens-for-service-accounts/).

### Cloudflare

1. In Cloudflare, open **Manage Account** > **Account API Tokens** and create an account-owned token.
1. Include **Account Resources: Read** so the MCP server can identify the account. Grant the token access only to the accounts, zones, and actions the agent needs.
1. In the Cloudflare integration, enter the **Account API Token**.

### Dash0

1. In Dash0, open **Settings**, then **Endpoints**, and copy the **MCP** endpoint URL for your organization.
1. Under **Settings**, open **Auth Tokens** and create an organization auth token. Grant **Reading** permissions for the datasets the agent needs.
1. In the Dash0 integration, enter the **MCP Endpoint URL** and **Organization Auth Token**.

Use your organization's regional endpoint. See Dash0's [auth token documentation](https://www.dash0.com/docs/dash0/miscellaneous/glossary/auth-tokens) to scope the token's permissions.

### Datadog

Follow [Connect Datadog](/docs/ai/agents/integrations/datadog/) to create a service account, set its permissions, and connect it to Pulumi.

### Honeycomb

1. In Honeycomb, navigate to **Account**, then **Team Settings**, then **API Keys**
1. Select **Create Management API Key** and give it a name (e.g., "MCP Integration")
1. Choose the **Model Context Protocol** and **Environments** scopes, then grant permissions:
    - **Read**: Required for all Honeycomb MCP operations. Make sure to grant read for both MCP and Environments.
    - **Write**: Required for the `create_board` tool.
1. Copy the **Key ID** and **Key Secret**. You will not be able to see the Key Secret again.
1. In the integration form, enter the **Key ID** and **Key Secret** in the corresponding fields

### Linear

{{% notes type="info" %}}
Linear API keys are personal tokens. All actions an agent takes through this integration are attributed to the user who created the token, regardless of who creates the task.
{{% /notes %}}

1. In Linear, open **Settings**, then **Security & Access**
1. Select **New API Key**, give it a name, and choose the permissions the agent needs:
    - **Read**: required for all operations the agent performs through Linear
    - **Create issues** and **Create comments**: required if the agent needs to file or comment on issues
    - **Write** or **Admin**: required if the agent needs to update or delete existing issues
1. Optionally limit the key to specific teams using the team-access controls
1. In the integration form, enter the **API Key**

### New Relic

1. Have an administrator enable **New Relic MCP Server > API Keys** in **Feature Control Manager** and grant MCP read access to a centrally managed automation account.
1. Create a **User API Key** for that account.
1. In the New Relic integration, enter your account's **Region** (`us`, `eu`, or `jp`) and the **User API Key**.

The key uses the automation account's permissions. Tools that require OAuth are unavailable through this API-key integration. See [New Relic MCP authentication](https://docs.newrelic.com/docs/agentic-ai/mcp/overview/#authentication-options).

### PagerDuty

{{% notes type="info" %}}
PagerDuty User API Tokens are tied to a single user account. All actions an agent takes through this integration are attributed to the user who created the token, regardless of who creates the task. For shared use, consider creating a dedicated PagerDuty user (e.g. `pulumi-bot`) whose token agents can use.
{{% /notes %}}

1. In PagerDuty, open your user profile and select **User Settings**
1. Select **Create API User Token** and give it a name (e.g., "Pulumi Agents"). The token inherits the user's existing PagerDuty permissions, so its access matches whatever the user can already see in the PagerDuty UI.
1. Copy the token
1. In the integration form, enter the **User API Token**

### Sentry

1. In Sentry, open **Settings** > **Custom Integrations** and create an internal integration.
1. Grant **Read** access to **Organization**, **Project**, **Team**, and **Issue & Event**, then copy the token.
1. In the Sentry integration, enter the **Internal integration token** and **Organization Slug**, such as `my-organization` from `my-organization.sentry.io`.

This integration connects to Sentry SaaS using its [explicit-token authentication](https://github.com/getsentry/toolkit#remote-with-an-explicit-sentry-token).

### Supabase

{{% notes type="info" %}}
Supabase Access Tokens are tied to a single user account. Supabase does not offer service-account credentials for the MCP server. All actions an agent takes through this integration are attributed to the user who created the token, regardless of who creates the task. For shared use, consider creating a dedicated Supabase user (e.g. `pulumi-bot`) whose token agents can use.
{{% /notes %}}

1. On **supabase.com**, open **Account Preferences**, then **Access Tokens**
1. Select **Generate New Token**, give it a name, and copy the token
1. In the integration form, enter the **Access Token**
