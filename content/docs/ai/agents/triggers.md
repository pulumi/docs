---
title: Events and schedules
title_tag: Events and schedules | Pulumi Agents
h1: Events and schedules
pulumi_cloud_feature: pulumi-agents
meta_desc: Start agent tasks from Pulumi events, external webhooks, or recurring schedules, and control future runs.
menu:
    ai:
        name: Events and schedules
        parent: ai-agents-create-manage
        identifier: ai-agents-triggers
        weight: 50
---

Configure an agent to start tasks automatically when a Pulumi operation completes, an external tool sends a webhook, or a schedule runs. Choose which events or schedule should start the task, and provide the assignment the agent should carry out.

Add automations to an existing agent from **Automations**. To configure its first trigger while creating it, follow [Choose how the agent starts](/docs/ai/agents/configure/#choose-how-the-agent-starts).

For Neo's scheduled tasks, see [Neo automations](/docs/ai/neo/automations/).

## Write the assignment

Describe what the agent should do each time the trigger fires or the schedule runs. Keep instructions that apply across all the agent's tasks in its [configuration](/docs/ai/agents/configure/). Create separate agents when different types of work need their own instructions, integrations, or permissions.

Use trigger settings to select which events start tasks. Instructions in the assignment do not filter incoming events.

## Connect a Pulumi operation

In Pulumi Cloud, open **Automations** and select **Set up trigger**:

1. Enter a **Name** for the automation.
1. Set **Runs** to **When a Pulumi operation completes**.
1. Choose the **Agent**.
1. In **Prompt**, write the assignment for each run.
1. Select the **Operations**, **Results**, and **Stacks** that should start tasks.
1. Select **Create automation**.

For example, select failed operations on production stacks to investigate deployment failures without creating tasks for development activity. Matching stacks are added to the task context automatically.

The first matching event starts a task. Later matching events join that task while its batch window is open. Events that arrive while the agent is working are combined and delivered when it can accept more input.

**Follow-up batch window (seconds)** sets how long the batch stays open after the most recent event, up to one hour after the first event. Once the batch closes, the next matching event starts a new task. The window does not delay delivery to an available task.

## Connect an external webhook

In Pulumi Cloud, open **Automations** and select **Set up trigger**:

1. Enter a **Name** for the automation.
1. Set **Runs** to **When a webhook event arrives**.
1. Choose the **Agent**.
1. In **Prompt**, write the assignment for each run.
1. Under **Webhook preset**, select **Generic webhook** or **PagerDuty**.
1. Select **Create automation**, then copy the **Webhook URL** and **Required header** from the setup panel.
1. Configure the sender to use that URL and include `X-Pulumi-Trigger-Secret` with the displayed secret value on every request.

The Pulumi secret is shown once. Save it before closing the panel. If you lose it, rotate it from the automation details page.

A webhook delivers the event payload. To retrieve more information, the agent also needs an [integration](/docs/ai/agents/integrations/) with the sending system. For example, a PagerDuty webhook delivers incident details, and the PagerDuty MCP integration lets the agent query the incident.

### PagerDuty setup

After completing the shared webhook steps with the **PagerDuty** preset, follow the setup panel to configure the event subscription.

If signature verification is enabled, paste the PagerDuty signing secret into **PagerDuty signing secret** and select **Done**. This secret is separate from the required Pulumi header.

## Schedule recurring work

In Pulumi Cloud, open **Automations** and select **New automation**, then **Start with a blank automation**:

1. Enter a **Name** for the automation.
1. Choose the **Agent**.
1. Set **Runs** to **On a schedule**.
1. Set **Frequency**.
1. In **Prompt**, write the assignment for each run, such as reviewing dependency upgrades in a specific repository.
1. Select **Create automation**.

Each task uses the agent's saved instructions and access settings.

## Stop future runs

Disable the automation to stop it from creating tasks. To stop new work across all an agent's triggers and schedules, [pause the agent](/docs/ai/agents/manage/#pause-future-work-and-stop-current-work).

To stop work already in progress, cancel the running task separately.
