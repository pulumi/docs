---
title: Permissions
title_tag: Permissions | Pulumi Agents
h1: Permissions
meta_desc: Scope Pulumi Agents access with Pulumi Cloud roles, external credentials, and approval settings.
menu:
    ai:
        name: Permissions and approvals
        parent: ai-concepts
        identifier: ai-agents-permissions
        weight: 20
---

Give each agent only the access it needs for its work. Its Pulumi Cloud role controls access to Pulumi resources, such as stacks and ESC environments. Credentials for connected tools control what it can access and change in those tools.

## Design access around the job

Grant the required actions on the relevant resources. Use a dedicated role or service account where supported, so you can revoke agent access independently of a teammate's access. If an integration requires a personal token, the agent uses its owner's permissions and identity.

Prefer short-lived credentials. For long-lived keys, assign someone to rotate and revoke them. Store credentials through the integration's setup flow or Pulumi ESC, never in task messages or instructions.

The [integration guides](/docs/ai/agents/integrations/) apply these choices to each provider.

## Scope Pulumi Cloud access

Select a role in the agent's **Role** field that grants only the access its work requires, including access to relevant stacks and ESC environments. This role applies across the agent's tasks. To change it, [edit the agent's access settings](/docs/ai/agents/configure/#set-its-access).

Neo uses the acting user's Pulumi Cloud access, subject to its task settings. See [Neo permissions](/docs/ai/neo/permissions/) for its execution identity and controls.

## Scope credentials for connected tools

Limit each integration's credentials to the resources and actions the agent needs. Selecting an integration or adding restrictions to the agent's instructions does not narrow those credentials. An agent declining a request doesn't prove that its credentials would deny it.

If an integration uses Pulumi ESC, the agent also needs permission to open the environment. Its Pulumi Cloud role controls that access; the credentials supplied by the environment control access to the connected tool.

## Separate approvals from access

Approval settings determine when an agent must ask before taking an action. Approving an action does not grant additional permissions.

**Read-only** restricts Pulumi Cloud writes, but doesn't make external credentials read-only.

For an agent you configure, set **Permissions** and **Default mode** on the agent. For Neo, see [permission and approval modes](/docs/ai/neo/permissions/#permission-mode-and-approval-mode).

## Review and remove access

When the job changes, remove unneeded access. Before revoking shared credentials, check which other tasks or agents use them.

To stop work already running, follow the [agent task controls](/docs/ai/agents/manage/#pause-future-work-and-stop-current-work) or [Neo task controls](/docs/ai/neo/tasks/#interruptions-and-resuming).
