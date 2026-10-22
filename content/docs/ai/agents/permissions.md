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

Give each agent only the access it needs. For agents your team creates, assign a Pulumi Cloud role to control access to stacks and ESC environments. Neo uses your existing Pulumi Cloud permissions. Credentials for connected tools control access to those tools.

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

Set **Default mode** to control when the agent asks for approval. In **Auto** mode, actions do not require your approval. If no mode is set, the agent uses **Auto**. Approving an action does not grant permissions beyond the agent's role and connected credentials.

For Neo, see [permission and approval modes](/docs/ai/neo/permissions/#permission-mode-and-approval-mode).

## Give teammates access

To start a task, a teammate needs `agent_task:create` and access to the agent. For an agent with an assigned role, the teammate must hold that role directly or through a team, or have `organization:update`. The default **Agent Read Only** role does not need to be assigned to teammates. See [Roles](/docs/administration/concepts/rbac/roles/) for role assignments.

For tasks started directly, teammates with access to the agent can view and contribute to its tasks. For tasks started by an organization-owned automation, `agent_automations:read` grants viewing access, and `agent_automations:update` grants access to reply and approve actions. Holding the agent's role alone does not grant access to these automated tasks.

Task owners and teammates with task-specific permissions can also access tasks. For example, `agent_task:read` grants viewing access, while `agent_task:contribute` allows replies. Running a shared agent from a personal schedule does not give other teammates access to the resulting tasks.

## Review and remove access

When the job changes, remove unneeded access. Before revoking shared credentials, check which other tasks or agents use them.

To stop work already running, follow the [agent task controls](/docs/ai/agents/manage/#pause-future-work-and-stop-current-work) or [Neo task controls](/docs/ai/neo/tasks/#interruptions-and-resuming).
