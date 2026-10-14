---
title: External MCP Servers
title_tag: Neo External MCP Server Integrations
h1: External MCP Servers
meta_desc: Connect Neo to external services through Model Context Protocol servers, bringing issue tracker, observability, and runbook context into Neo tasks.
aliases:
- /docs/ai/integrations/mcp/
menu:
    ai:
        name: External MCP integrations
        parent: ai-agents-integrations
        weight: 30
        identifier: ai-integrations-mcp
---

MCP integrations connect Neo to external services that expose a [Model Context Protocol](https://modelcontextprotocol.io/) server — the same open standard covered in [MCP for infrastructure as code](/what-is/mcp-for-infrastructure-as-code/). Once connected, Neo can use those services as tools during a [task](/docs/ai/neo/tasks/), with credentials managed centrally in Pulumi Cloud.

> [!INFO]
> This page is about connecting Neo to other services' MCP servers. To connect your own AI agent (Claude Code, Cursor, and others) to Pulumi, see the [Pulumi MCP server](/docs/ai/mcp-server/).

MCP integrations are configured at the organization level by an administrator. Once enabled, they are available to all Neo tasks in the organization.

## What you can do with MCP integrations

MCP integrations give Neo direct access to the systems your team uses to define, observe, and operate infrastructure: issue trackers, observability platforms, runbook wikis, and on-call tooling. Neo can pick up a ticket from Linear or Jira and write the matching infrastructure changes; during an investigation it can query real traces and metrics rather than reasoning from documentation; and runbooks, incident records, and on-call schedules are first-class inputs rather than things someone has to paste in.

Supported integrations are Atlassian (Jira and Confluence), Dash0, Datadog, Honeycomb, Linear, New Relic, PagerDuty, and Supabase. Each one becomes a set of tools Neo can call during a task, with credentials managed centrally in Pulumi Cloud.

## Enabling an MCP integration

To enable an integration, navigate to **Neo Settings**, select **Integrations**, select the integration, and provide the required credentials.

Each MCP integration connects to the service's MCP server. Available tools depend on the credentials and authentication method the service supports.

## Credential storage

Integration credentials are encrypted at rest in Pulumi Cloud using a per-organization encryption key. When a task needs to connect to an integration, Pulumi Cloud decrypts the credentials at task time, constructs the appropriate authentication headers, and connects to the service on Neo's behalf. Credentials are never exposed to the language model and are never embedded in task state.

## Disabling an integration

To remove an integration from your organization, navigate to **Neo Settings**, select **Integrations**, find the integration, and select **Remove**.

Disabling an integration deletes its stored credentials and immediately prevents any new tasks from using it. Tasks that are already running will lose access to the integration the next time Neo tries to use it.

## Per-task control

For tasks started from an agent you configure, [select MCP integrations in the agent configuration](/docs/ai/agents/configure/#connect-the-tools-it-needs). The saved selection applies across that agent's tasks.

Neo tasks inherit all integrations enabled by the organization. Before starting a task, turn off any integrations it does not need in the task composer. This selection applies only to that task.

## If an integration fails

Integrations are resolved independently at the start of each message. If credentials for one integration can't be retrieved, or its MCP server is unreachable, Neo logs a warning, skips that integration, and continues the task with the remaining ones. A single broken integration won't stop a task from running.

If Neo tries to use an integration that isn't available (for example, because the credentials were removed or expired), it will surface the failure in the conversation and continue with its other tools.

## Configuration

### Atlassian (Jira and Confluence)

1. In **admin.atlassian.com**, open **Rovo MCP**
    - Enable **API token authentication**
    - Add `https://*.pulumi.com/**` as an allowed domain
1. Open **Directory**, then **Service Accounts**
1. Create a service account and give it user access to each product you want Neo to access
1. Create a credential for the service account with type **API** and assign the necessary roles
1. In Neo, enter the **Service Account API Token** and your **Site URL** (e.g., `https://yoursite.atlassian.net`)

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
1. Copy the **Key ID** and **Key Secret**. You will not be able to see them again.
1. In Neo, enter the **Key ID** and **Key Secret** in the corresponding fields

### Linear

{{% notes type="info" %}}
Linear API keys are personal tokens. All actions Neo takes through this integration are attributed to the user who created the token, regardless of who creates the Neo task. This tool connection is separate from installing an agent in a Linear workspace.
{{% /notes %}}

1. In Linear, open **Settings**, then **Security & Access**
1. Select **New API Key**, give it a name, and choose the permissions Neo needs:
    - **Read**: required for all integrations Neo performs through Linear
    - **Create issues** and **Create comments**: required if you want Neo to file or comment on issues
    - **Write** or **Admin**: required if you want Neo to update or delete existing issues
1. Optionally limit the key to specific teams using the team-access controls
1. In Neo, enter the **API Key**

### New Relic

1. Have an administrator enable **New Relic MCP Server > API Keys** in **Feature Control Manager** and grant MCP read access to a centrally managed automation account.
1. Create a **User API Key** for that account.
1. In the New Relic integration, enter your account's **Region** (`us`, `eu`, or `jp`) and the **User API Key**.

The key uses the automation account's permissions. Tools that require OAuth are unavailable through this API-key integration. See [New Relic MCP authentication](https://docs.newrelic.com/docs/agentic-ai/mcp/overview/#authentication-options).

### PagerDuty

{{% notes type="info" %}}
PagerDuty User API Tokens are tied to a single user account. All actions Neo takes through this integration are attributed to the user who created the token, regardless of who creates the Neo task. For shared use, consider creating a dedicated PagerDuty user (e.g. `pulumi-bot`) whose token Neo can use.
{{% /notes %}}

1. In PagerDuty, open your user profile and select **User Settings**
1. Select **Create API User Token** and give it a name (e.g., "Neo Integration"). The token inherits the user's existing PagerDuty permissions, so its access matches whatever the user can already see in the PagerDuty UI.
1. Check **Read-only API Key** if you don't want Neo to be able to create or modify incidents, schedules, or escalation policies
1. Copy the token
1. In Neo, enter the **User API Token**

### Supabase

{{% notes type="info" %}}
Supabase Access Tokens are tied to a single user account. Supabase does not offer service-account credentials for the MCP server. All actions Neo takes through this integration are attributed to the user who created the token, regardless of who creates the Neo task. For shared use, consider creating a dedicated Supabase user (e.g. `pulumi-bot`) whose token Neo can use.
{{% /notes %}}

1. On **supabase.com**, open **Account Preferences**, then **Access Tokens**
1. Select **Generate New Token**, give it a name, and copy the token
1. In Neo, enter the **Access Token**
