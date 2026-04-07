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

A few examples:

- **Pick up work from your issue tracker.** Connect Linear or Jira and ask Neo to implement an issue. Neo reads the issue description, acceptance criteria, and comments, then writes the infrastructure changes to match.
- **Follow your runbooks.** Connect Confluence or Notion and point Neo at an operational runbook. Neo follows the documented steps, adapting them to your current environment.
- **Investigate with real observability data.** Connect Honeycomb or Datadog and ask Neo to diagnose a performance problem. Neo queries actual traces and metrics from your environment to narrow down the cause.
- **Debug with production error context.** Connect Sentry and ask Neo to fix a failing deployment. Neo pulls the error details, stack traces, and affected releases to inform its approach.
- **Manage application infrastructure together.** Connect Supabase and let Neo coordinate database changes alongside your Pulumi infrastructure code.

## Available integrations

The following integrations are available in the Neo integration catalog:

| Integration | Description |
|---|---|
| **Atlassian** | Jira issues, Confluence spaces, and project management |
| **Datadog** | Cloud-scale monitoring and analytics for infrastructure and applications |
| **Honeycomb** | Query traces, analyze performance, and investigate production issues |
| **Linear** | Issue tracking, project management, and team workflows |
| **Notion** | Connected workspace for notes, docs, and project management |
| **Sentry** | Application monitoring, error tracking, and performance insights |
| **Supabase** | Database management, authentication, and edge functions |

Each integration connects Neo to the service's [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server, which means Neo can use the full set of tools that service exposes through MCP.

## Enabling an integration

Organization administrators configure integrations in Neo Settings:

1. Navigate to **Neo Settings** in the Pulumi Cloud left navigation
1. Select the **Integrations** tab
1. Find the integration you want to enable and select **Configure**
1. Enter the required credentials for the integration
1. Select **Save**

The credentials you provide depend on the integration. Some require an API key, while others use OAuth to connect your organization's account. Each integration's configuration form includes guidance on where to find or generate the required credentials.

### Credential storage

Integration credentials are stored securely in [Pulumi ESC](/docs/esc/) (Environments, Secrets, and Configuration). When a task needs to connect to an integration, Neo resolves the credentials at task time from ESC, constructs the appropriate authentication headers, and connects to the service. Credentials are never embedded in task state.

## Disabling an integration

To remove an integration from your organization:

1. Navigate to **Neo Settings** → **Integrations**
1. Find the integration you want to disable and select **Remove**

Disabling an integration deletes its credentials from ESC and immediately prevents any new tasks from using it. Tasks that are already running will lose access to the integration on their next tool call.

## How integrations work at task time

When Neo starts a task, it connects to each enabled integration's MCP server using the stored credentials. From there, Neo can use any tools the MCP server provides. For example, with the Honeycomb integration enabled, Neo can query traces to investigate a performance issue that came up during an infrastructure review. With Linear enabled, Neo can look up the details of an issue referenced in a task description.

The integration connection is transparent. Neo decides when to use an integration based on the context of your conversation, just as it decides when to use any other tool.
