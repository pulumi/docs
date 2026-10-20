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

Connect Datadog so an agent can query monitoring data during an investigation. Neo and agents you configure share the organization's connection, which uses a Datadog API key and application key.

## Prepare Datadog access

Enable **MCP Access** in Datadog organization settings. Give the service account **MCP Read** (`mcp_read`) and the resource-level permissions for the data the agent needs. Limit its application key to the required scopes. For an investigation, omit permissions to change monitors unless that is part of the job. See [Design access around the job](/docs/ai/agents/permissions/#design-access-around-the-job) for shared access guidance.

## Create the credentials

1. In Datadog **Organization Settings**, open **Service Accounts** and create or select the account.
1. Create a scoped application key for that service account.
1. Open **Organization Settings** > **API Keys** and create an API key in the same organization.
1. Identify your Datadog site: `us1`, `us3`, `us5`, `eu1`, `ap1`, or `ap2`.

See [Datadog MCP authentication](https://docs.datadoghq.com/mcp_server/setup/#api-and-application-keys) for the key requirements.

## Connect Datadog

As a Pulumi Cloud organization administrator:

1. Open **Neo Settings** > **Integrations** > **MCP servers**.
1. Find **Datadog** under **Available** and select **Authorize**.
1. Enter **Datadog site**, **API Key**, and **App Key**, then select **Save**.

For an agent you configure, [select Datadog in its configuration](/docs/ai/agents/configure/#connect-the-tools-it-needs). For Neo, Datadog is available to new tasks by default. Turn it off in the task composer if a task doesn't need it.
