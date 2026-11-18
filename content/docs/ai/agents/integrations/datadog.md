---
title: Connect Datadog
title_tag: Connect Datadog | Pulumi Agents
h1: Connect Datadog
meta_desc: Connect Datadog to Pulumi Agents using an API key and a service account application key.
menu:
    ai:
        name: Datadog
        parent: ai-integrations-mcp
        weight: 40
---

Connect Datadog so an agent can query monitoring data during an investigation. The organization's connection uses a Datadog API key and application key.

## Prepare Datadog access

1. In Datadog **Organization Settings**, enable **MCP Access**.
1. Open **Service Accounts** and create or select the account that the integration will use.
1. Give the service account **MCP Read** (`mcp_read`) and the permissions for the data the agent needs. Reading monitors, for example, also requires **Monitors Read**. See [Datadog's required permissions](https://docs.datadoghq.com/mcp_server/setup/#required-permissions).

When you create the application key below, limit its permissions to the monitoring data the agent needs, such as monitors or logs. Omit write permissions unless the assignment requires them. See [Choose integration permissions](/docs/ai/agents/permissions/#design-access-around-the-job) to choose which permissions to grant.

## Create the credentials

1. Create a scoped application key for that service account.
1. Open **Organization Settings** > **API Keys** and create an API key in the same organization.
1. Identify your Datadog site: `us1`, `us3`, `us5`, `eu1`, `ap1`, or `ap2`.

See [Datadog MCP authentication](https://docs.datadoghq.com/mcp_server/setup/#api-and-application-keys) for the key requirements.

## Connect Datadog

With permission to manage organization integrations (`org_integrations:update`):

1. Open **Agent Settings** > **Integrations** > **MCP servers**.
1. Find **Datadog** under **Available** and select **Authorize**.
1. Enter **Datadog site**, **API Key**, and **App Key**, then select **Save**.

Before assigning work to an agent your team created, [select Datadog in the agent's tools](/docs/ai/agents/configure/#connect-the-tools-it-needs). Neo tasks have access to Datadog by default; turn it off in the message composer when a task does not need it.
