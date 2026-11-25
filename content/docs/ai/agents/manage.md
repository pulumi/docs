---
title: Manage and troubleshoot agents
title_tag: Manage and troubleshoot | Pulumi Agents
h1: Manage and troubleshoot agents
pulumi_cloud_feature: pulumi-agents
meta_desc: Update agent configuration, stop future or current work, and diagnose missing context, failed integrations, and tasks that do not start.
menu:
    ai:
        name: Manage and troubleshoot
        parent: ai-agents
        identifier: ai-agents-manage
        weight: 90
---

Open **Agents** in Pulumi Cloud, select the **Agents** tab, then select the agent by name. From its page, you can edit its settings, pause work, or delete it.

## Change saved configuration

On the agent's page, select **Edit**, update its settings, and select **Save changes**.

Changes to **System prompt**, the role, approval mode, and selected MCP integrations apply to new tasks and to existing tasks when the agent next resumes work. These settings cannot be overridden in an individual task.

Changing the [model provider](/docs/ai/agents/configure/#choose-a-model) applies to new tasks. Existing tasks retain the provider they started with.

## Pause future work and stop current work

Select **Pause** on the agent's page to prevent new tasks and block further work in existing tasks. Pausing does not cancel work already executing. To cancel it, open the running task and select **Cancel**, the stop icon beside the message box.

Select **Resume** to allow work again. If you also paused an automation, resume it separately. Scheduled runs and events skipped while paused are not replayed.

## Delete an agent

First, select a different agent for each automation that uses this agent, or delete automations you no longer need. Pulumi prevents deletion while an automation still uses the agent.

If you delete an automation, teammates who viewed its tasks through their automation permissions lose that access. Task owners and teammates with permissions on the tasks themselves retain access.

Select **Delete** on the agent's page. The agent can no longer start tasks or continue existing tasks. Deleting an agent does not cancel work already executing; open each running task and select **Cancel** to cancel it. Past tasks still show which agent performed the work.

## A task does not start

Check that the agent is active. For events or schedules, also check that the automation is active. Resuming an agent does not resume its paused automations.

- **Manual request:** Confirm that the requester has [permission to use the agent](/docs/ai/agents/permissions/#give-teammates-access).
- **Pulumi event:** In the automation form, confirm the selected **Agent** and **Runs** setting. Check that **Operations**, **Results**, and **Stacks** match the event you expected.
- **Webhook:** In the automation form, confirm the selected **Agent** and that **Runs** is set to **When a webhook event arrives**.
- **Schedule:** In the automation form, confirm the selected **Agent**, that **Runs** is set to **On a schedule**, and the **Frequency**.

Check the task for an error message:

- **Usage limit reached:** Review the [organization usage limit](/docs/ai/concepts/neo/usage-limits/). Ask an administrator to raise it, or wait for the next billing period. Requests billed through your own model provider do not count toward this limit.
- **Model connection failed:** [Test the model provider](/docs/ai/agents/model-providers/#test-a-provider) used by this agent and correct its settings.
- **Agents disabled:** Ask an administrator to check that **Enable AI features for this organization** and **Enable Pulumi Agents** are both on in [organization AI settings](/docs/ai/concepts/neo/settings/#per-feature-controls).

See [Events and schedules](/docs/ai/agents/triggers/) for setup instructions.

## The agent cannot access a resource

Open the failed tool call in the task and use its error to check the right access setting:

- **Integration not available:** Confirm that it is connected. For an MCP integration, also select it in the agent's **Edit** form.
- **ESC environment access denied:** Grant the agent's role `environment:open` on the environment that supplies the connection's credentials.
- **Cloud resource access denied:** Check the connected cloud identity's permissions for the resource and action named in the error. Changing the agent's Pulumi Cloud role does not change those permissions.
- **Authentication failed:** Check whether the integration's credentials have expired or been revoked, then replace them if needed.
- **File or repository not found:** Check the path or URL in the assignment and the connected identity's access to it.

See [Integrations](/docs/ai/agents/integrations/) for credential setup.

## A teammate cannot view or reply

Check [teammate access](/docs/ai/agents/permissions/#give-teammates-access) for the way the task was started. Tasks started by an organization-owned automation use automation permissions; the agent's role alone does not grant access. In Slack, confirm that the teammate has linked the correct Pulumi account and is replying in the task's thread.

<span id="next-steps"></span>
