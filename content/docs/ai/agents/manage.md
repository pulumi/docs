---
title: Manage and troubleshoot agents
title_tag: Manage and troubleshoot | Pulumi Agents
h1: Manage and troubleshoot agents
pulumi_cloud_feature: pulumi-agents
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

On the agent's page, select **Edit**, update its settings, and select **Save changes**. Changes apply to new tasks and to existing tasks when the agent next resumes work.

Change the agent's instructions, role, approval settings, and MCP integrations here. These settings cannot be overridden in an individual task.

## Pause future work and stop current work

Select **Pause** on the agent's page to prevent new tasks and block further work in existing tasks. Pausing does not cancel work already executing. To cancel it, open the running task and select **Cancel**, the stop icon beside the message box.

Select **Resume** to allow work again. Scheduled runs and events skipped while paused are not replayed.

## Delete an agent

First, delete or reassign automations that reference the agent. Pulumi blocks deletion while an automation still references it.

Select **Delete** on the agent's page. The agent can no longer start tasks or continue existing tasks. Deleting an agent does not cancel work already executing; open each running task and select **Cancel** to cancel it. Past tasks still show which agent performed the work.

## A task does not start

Check that the agent is active. For events or schedules, also check that the automation is active. Resuming an agent does not resume its paused automations.

- **Manual request:** Confirm that the requester has [permission to use the agent](/docs/ai/agents/permissions/#give-teammates-access).
- **Pulumi event:** In the automation form, confirm the selected **Agent** and **Runs** setting. Check that **Operations**, **Results**, and **Stacks** match the event you expected.
- **Webhook:** In the automation form, confirm the selected **Agent** and that **Runs** is set to **When a webhook event arrives**.
- **Schedule:** In the automation form, confirm the selected **Agent**, that **Runs** is set to **On a schedule**, and the **Frequency**.

See [Events and schedules](/docs/ai/agents/triggers/) for setup instructions.

## The agent cannot access a resource

- Confirm that the required integration is connected. For an MCP integration, check that it is selected in the agent's configuration.
- Confirm that the agent's role grants access to the relevant Pulumi Cloud resources, including any ESC environment that supplies credentials.
- Check that the integration's credentials are valid.
- Confirm that the credentials grant access to the resource the agent needs.
- Check document paths and URLs in the assignment.

See [Integrations](/docs/ai/agents/integrations/) for credential setup.

## A teammate cannot view or reply

Check [teammate access](/docs/ai/agents/permissions/#give-teammates-access). For tasks started by an automation, access to that automation matters; holding the agent's role alone may not be enough. In Slack, confirm that the teammate has linked the correct Pulumi account and is replying in the task's thread.

## Next steps

- [Review the agent's configuration](/docs/ai/agents/configure/).
- [Check event and schedule setup](/docs/ai/agents/triggers/).
- [Review permissions](/docs/ai/agents/permissions/).
