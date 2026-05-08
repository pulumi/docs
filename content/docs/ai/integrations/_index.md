---
title: Integrations
title_tag: Neo Integrations
h1: Neo Integrations
meta_desc: Bring context from issue trackers, observability platforms, and wikis into Neo tasks, and give Neo scoped access to cloud CLIs through Pulumi ESC.
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    ai:
        name: Integrations
        parent: ai-home
        weight: 55
        identifier: ai-integrations
---

Neo integrations connect the agent to the rest of your stack. There are two kinds:

- **MCP integrations** bring **context** into a task — issues from Linear, traces from Honeycomb, runbooks from Confluence, incidents from PagerDuty. Each one is a [Model Context Protocol](https://modelcontextprotocol.io/) server that Neo connects to with credentials you store in the Pulumi Service.
- **[CLI integrations](/docs/ai/integrations/cli/)** let Neo **act** on cloud resources by running `aws`, `gcloud`, `az`, or `kubectl` against credentials managed by [Pulumi ESC](/docs/esc/). The Pulumi Service does not store these credentials — ESC does, and decrypts them only at task time.

The rest of this page covers MCP integrations. For CLI integrations, see the [CLI integrations](/docs/ai/integrations/cli/) page.

Integrations of either kind are configured at the organization level by an administrator. Once enabled, they are available to all tasks in the organization.

## What you can do with MCP integrations

- **Pick up work from your issue tracker.** Connect Linear or Jira and ask Neo to implement an issue. Neo reads the issue description, acceptance criteria, and comments, then writes the infrastructure changes to match.
- **Follow your runbooks.** Connect Atlassian and point Neo at a Confluence runbook. Neo follows the documented steps, adapting them to your current environment.
- **Investigate with real observability data.** Connect Honeycomb or Datadog and ask Neo to diagnose a performance problem. Neo queries actual traces and metrics from your environment to narrow down the cause.
- **Respond to incidents.** Connect PagerDuty and let Neo look up active incidents, on-call schedules, and escalation policies while it investigates.
- **Manage application infrastructure together.** Connect Supabase and let Neo coordinate database changes alongside your Pulumi infrastructure code.

## Enabling an MCP integration

To enable an integration, navigate to **Neo Settings**, select **Integrations**, select the integration, and provide the required credentials.

Each MCP integration connects Neo to the service's MCP server, which means Neo can use the full set of tools that service exposes through MCP.

## Credential storage

Integration credentials are encrypted at rest in the Pulumi Service using a per-organization encryption key. When a task needs to connect to an integration, the service decrypts the credentials at task time, constructs the appropriate authentication headers, and connects to the service on Neo's behalf. Credentials are never exposed to the language model and are never embedded in task state.

## Disabling an integration

To remove an integration from your organization, navigate to **Neo Settings**, select **Integrations**, find the integration, and select **Remove**.

Disabling an integration deletes its stored credentials and immediately prevents any new tasks from using it. Tasks that are already running will lose access to the integration the next time Neo tries to use it.

## How integrations work at task time

When Neo starts a task, it connects to each enabled integration's MCP server using the stored credentials. From there, Neo can use any tools the MCP server provides. For example, with the Honeycomb integration enabled, Neo can query traces to investigate a performance issue that came up during an infrastructure review. With Linear enabled, Neo can look up the details of an issue referenced in a task description.

The integration connection is transparent. Neo decides when to use an integration based on the context of your conversation, just as it decides when to use any other tool.

## Per-task control

By default, every task inherits all integrations the organization has enabled. If you want to narrow Neo's focus for a specific task (for example, running a deployment review without giving Neo access to your issue tracker), you can toggle individual integrations off from the task composer before starting the conversation. The toggles only affect the current task; the org-level configuration is unchanged.

## If an integration fails

Integrations are resolved independently at the start of each message. If credentials for one integration can't be retrieved, or its MCP server is unreachable, Neo logs a warning, skips that integration, and continues the task with the remaining ones. A single broken integration won't stop a task from running.

If Neo tries to use an integration that isn't available (for example, because the credentials were removed or expired), it will surface the failure in the conversation and continue with its other tools.

## Configuration

### Atlassian (Jira & Confluence)

1. In **admin.atlassian.com**, open **Rovo MCP**
    - Enable **API token authentication**
    - Add `https://*.pulumi.com/**` as an allowed domain
1. Open **Directory**, then **Service Accounts**
1. Create a service account and give it user access to each product you want Neo to access
1. Create a credential for the service account with type **API** and assign the necessary roles
1. In Neo, enter the **Service Account API Token** and your **Site URL** (e.g., `https://yoursite.atlassian.net`)

### Datadog

1. In **Organization Settings**, open **Service Accounts** and create a service account with read-only access
1. On the service account's details page, create an **App Key** and make sure to include the MCP read scope
1. In **Organization Settings**, open **API Keys** and create an **API Key**
1. Identify your Datadog site — it's the domain you use to access Datadog (for example, `datadoghq.com` is `us1`, `datadoghq.eu` is `eu1`). Supported codes: `us1`, `us3`, `us5`, `eu1`, `ap1`, `ap2`.
1. In Neo, enter the **Datadog site** code, **API Key**, and **App Key**

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
Linear API keys are personal tokens. All actions Neo takes through this integration are attributed to the user who created the token, regardless of who creates the Neo task. OAuth support is planned for a future release.
{{% /notes %}}

1. In Linear, open **Settings**, then **Security & Access**
1. Select **New API Key**, give it a name, and choose the permissions Neo needs:
    - **Read**: required for all integrations Neo performs through Linear
    - **Create issues** and **Create comments**: required if you want Neo to file or comment on issues
    - **Write** or **Admin**: required if you want Neo to update or delete existing issues
1. Optionally limit the key to specific teams using the team-access controls
1. In Neo, enter the **API Key**

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
Supabase Access Tokens are tied to a single user account — Supabase does not offer service-account credentials for the MCP server. All actions Neo takes through this integration are attributed to the user who created the token, regardless of who creates the Neo task. For shared use, consider creating a dedicated Supabase user (e.g. `pulumi-bot`) whose token Neo can use.
{{% /notes %}}

1. On **supabase.com**, open **Account Preferences**, then **Access Tokens**
1. Select **Generate New Token**, give it a name, and copy the token
1. In Neo, enter the **Access Token**
