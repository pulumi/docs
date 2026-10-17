---
title: Manage and troubleshoot agents
title_tag: Manage and troubleshoot | Pulumi Agents
h1: Manage and troubleshoot agents
meta_desc: Update agent configuration, stop future or current work, and diagnose missing context, failed integrations, and tasks that do not start.
menu:
    ai:
        name: Manage and troubleshoot
        parent: ai-agents-create-manage
        identifier: ai-agents-manage
        weight: 70
---

Edit, pause, or delete an agent, and troubleshoot tasks that fail to start or cannot access the resources they need.

## Change saved configuration

On the agent's page, select **Edit**, update its settings, and save. Changes apply to new tasks and to existing tasks when the agent next resumes work. Work already in progress continues with the previous settings.

Change the agent's instructions, role, approval settings, and MCP integrations here. These settings cannot be overridden in an individual task.

## Pause future work and stop current work

Select **Pause** on the agent's page to prevent new tasks and stop existing tasks from continuing after their current work finishes. To stop work already in progress immediately, cancel the task separately.

Select **Resume** to allow work again. Scheduled runs and events skipped while paused are not replayed.

## Delete an agent

First, delete or reassign automations that reference the agent. Pulumi blocks deletion while an automation still references it.

Select **Delete** on the agent's page. The agent can no longer start tasks or continue existing tasks after its current work finishes. Past tasks still show which agent performed the work. Cancel running work separately if it needs to stop immediately.

## A task does not start

Check that the agent is active, then check how the task should start:

- **Manual request:** Confirm that the requester has permission to use the agent.
- **Pulumi event:** In the automation form, confirm the selected **Agent** and **Runs** setting. Check that **Operations**, **Results**, and **Stacks** match the event you expected.
- **Webhook:** In the automation form, confirm the selected **Agent** and that **Runs** is set to **When a webhook event arrives**.
- **Schedule:** In the automation form, confirm the selected **Agent**, that **Runs** is set to **On a schedule**, and the **Frequency**.

See [Events and schedules](/docs/ai/agents/triggers/) for setup instructions.

## The agent cannot access a resource

Check that:

- The agent has the required integration selected.
- The integration's credentials are valid.
- Those credentials grant access to the resource the agent needs.
- Any document path or URL in the assignment is correct.

See [Integrations](/docs/ai/agents/integrations/) for credential setup.

## A teammate cannot view or reply

Check permission to view the task separately from permission to contribute. In Slack, confirm that the teammate has linked the correct Pulumi account and is replying in the task's thread.

## Next steps

- [Review the agent's configuration](/docs/ai/agents/configure/).
- [Check event and schedule setup](/docs/ai/agents/triggers/).
- [Review permissions](/docs/ai/agents/permissions/).
