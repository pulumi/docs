---
title: Integrations
title_tag: Neo Integrations
h1: Neo Integrations
meta_desc: Bring context from issue trackers, observability platforms, and wikis into Neo tasks so it can act on what your team already knows.
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    ai:
        name: Integrations
        parent: ai-home
        weight: 55
        identifier: ai-integrations
---

Neo integrations bring context from your existing tools into infrastructure tasks. Neo can read directly from the services your team already uses, such as issue trackers, observability platforms, wikis, and databases, and apply that context to infrastructure tasks.

Integrations are configured at the organization level by an administrator. Once enabled, they are available to all tasks in the organization.

## What you can do with integrations

- **Pick up work from your issue tracker.** Connect Linear or Jira and ask Neo to implement an issue. Neo reads the issue description, acceptance criteria, and comments, then writes the infrastructure changes to match.
- **Follow your runbooks.** Connect Confluence or Notion and point Neo at an operational runbook. Neo follows the documented steps, adapting them to your current environment.
- **Investigate with real observability data.** Connect Honeycomb or Datadog and ask Neo to diagnose a performance problem. Neo queries actual traces and metrics from your environment to narrow down the cause.
- **Debug with production error context.** Connect Sentry and ask Neo to fix a failing deployment. Neo pulls the error details, stack traces, and affected releases to inform its approach.
- **Manage application infrastructure together.** Connect Supabase and let Neo coordinate database changes alongside your Pulumi infrastructure code.

## Enabling an integration

To enable an integration, navigate to **Neo Settings**, select **Integrations**, select the integration, and provide the required credentials.

Each integration connects Neo to the service's [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server, which means Neo can use the full set of tools that service exposes through MCP.

### Credential storage

Integration credentials are stored securely in [Pulumi ESC](/docs/esc/) (Environments, Secrets, and Configuration). When a task needs to connect to an integration, Neo resolves the credentials at task time from ESC, constructs the appropriate authentication headers, and connects to the service. Credentials are never embedded in task state.

## Disabling an integration

To remove an integration from your organization, navigate to **Neo Settings**, select **Integrations**, find the integration, and select **Remove**.

Disabling an integration deletes its credentials from ESC and immediately prevents any new tasks from using it. Tasks that are already running will lose access to the integration on their next tool call.

## How integrations work at task time

When Neo starts a task, it connects to each enabled integration's MCP server using the stored credentials. From there, Neo can use any tools the MCP server provides. For example, with the Honeycomb integration enabled, Neo can query traces to investigate a performance issue that came up during an infrastructure review. With Linear enabled, Neo can look up the details of an issue referenced in a task description.

The integration connection is transparent. Neo decides when to use an integration based on the context of your conversation, just as it decides when to use any other tool.

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
1. In Neo, enter the **API Key** and **App Key**

### Honeycomb

1. In Honeycomb, navigate to **Account**, then **Team Settings**, then **API Keys**
1. Select **Create Management API Key** and give it a name (e.g., "MCP Integration")
1. Choose the **Model Context Protocol** and **Environments** scopes, then grant permissions:
    - **Read**: Required for all Honeycomb MCP operations. Make sure to grant read for both MCP and Environments.
    - **Write**: Required for the `create_board` tool.
1. Copy the **Key ID** and **Key Secret**. You will not be able to see them again.
1. In Neo, enter the API key in the format `<key_id>:<secret_key>`

### Linear

{{% notes type="info" %}}
Linear API keys are personal tokens. All actions Neo takes through this integration are attributed to the user who created the token, regardless of who creates the Neo task. OAuth support is planned for a future release.
{{% /notes %}}

1. In Linear, open **Settings**, then **Security & Access**
1. Select **New API Key**, give it a name, and configure the permissions and team access for your use case
1. In Neo, enter the **API Key**

### Notion

Notion uses OAuth to connect your organization's account. Select **Connect** and follow the authorization flow.

### Sentry

Sentry uses OAuth to connect your organization's account. Select **Connect** and follow the authorization flow.

### Supabase

Requires:

- **Access Token**: On **supabase.com**, open **Account Preferences**, then **Access Tokens**
