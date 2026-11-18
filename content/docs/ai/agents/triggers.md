---
title: Events and schedules
title_tag: Events and schedules | Pulumi Agents
h1: Events and schedules
pulumi_cloud_feature: pulumi-agents
meta_desc: Start agent tasks from Pulumi events, external webhooks, or recurring schedules, and control future runs.
aliases:
- /docs/ai/concepts/neo/automations/
- /docs/ai/automations/
- /docs/ai/neo/automations/
menu:
    ai:
        name: Events and schedules
        parent: ai-agents
        identifier: ai-agents-triggers
        weight: 60
---

Use an automation to start agent tasks from Pulumi operations, webhooks, or a schedule.

In Pulumi Cloud, open **Agents**, then **Automations**. For a TypeScript example, see [Define the agent and its trigger](/docs/ai/agents/as-code/#define-the-agent). Creating an automation requires `agent_automations:create` and [access to the selected agent](/docs/ai/agents/permissions/#give-teammates-access). New automations belong to the organization; [automation permissions](/docs/ai/agents/permissions/#give-teammates-access) control access to their tasks.

<span id="write-the-assignment"></span>

Each automation has a **Name**, an **Agent** to run, and a **Prompt** describing what the agent should do. Each task also uses the agent's saved instructions and integrations. To configure a trigger while creating an agent, see [Choose how the agent starts](/docs/ai/agents/configure/#choose-how-the-agent-starts).

## Connect a Pulumi operation

In **Automations**, select **Set up trigger** and enter the name, agent, and prompt:

1. Set **Runs** to **When a Pulumi operation completes**.
1. Select the **Operations**, **Results**, and **Stacks** that should start tasks.
1. Select **Create automation**.

Supported operations include update, preview, refresh, destroy, import, rename, drift detection, and drift remediation. Results can be **Failed**, **Succeeded**, or **Canceled**. Only operations recorded in Pulumi Cloud can trigger tasks.

Select individual stacks in **Stacks**; prompts and stack tags do not filter events. Pulumi adds matching stacks to the task as context.

The first matching event starts a task. **Follow-up batch window (seconds)** controls how long later events can join that task instead of starting another. The default is 30 seconds after the most recent event, with a maximum of one hour after the first event. Once that window closes, the next matching event starts a new task. Events from different stacks can join the same task.

Events are delivered without waiting for the window to close. Events received while the agent is busy are combined for its next turn. This batching also applies to webhooks.

## Connect an external webhook

In **Automations**, select **Set up trigger** and enter the name, agent, and prompt:

1. Set **Runs** to **When a webhook event arrives**.
1. Under **Webhook preset**, select **Generic webhook**, **PagerDuty**, **Honeycomb**, **Sentry**, or **Datadog**.
1. Select **Create automation**. Keep the setup panel open for the webhook URL, secret, and connection instructions.
1. Configure the sender to use that URL and include `X-Pulumi-Trigger-Secret` with the displayed secret value on every request.

The Pulumi secret is shown once. Save it before closing the panel. If you lose it, rotate it from the automation details page.

Webhooks supply event data. To let the agent query the source for more information, also [connect its integration](/docs/ai/agents/integrations/).

<span id="pagerduty-setup"></span>
<span id="honeycomb-setup"></span>
<span id="sentry-setup"></span>
<span id="datadog-setup"></span>

For provider-specific setup, follow [PagerDuty](/docs/ai/agents/triggers/pagerduty/), [Honeycomb](/docs/ai/agents/triggers/honeycomb/), [Sentry](/docs/ai/agents/triggers/sentry/), or [Datadog](/docs/ai/agents/triggers/datadog/).

### Test a webhook

Send a test notification using the provider guide. Test deliveries can run the agent.

For a **Generic webhook**, replace the placeholders and send a JSON request:

```bash
curl --request POST '<webhook-url>' \
  --header 'Content-Type: application/json' \
  --header 'X-Pulumi-Trigger-Secret: <pulumi-secret>' \
  --header 'Idempotency-Key: checkout-alert-001' \
  --data '{"service":"checkout","summary":"Error rate above 5% for 10 minutes"}'
```

Use a unique `Idempotency-Key` for each event and reuse it when retrying that event. Without a key, identical payloads are treated as duplicate deliveries.

A successful webhook request returns HTTP `202`. Check **Last delivery** and **All runs** on the automation. Events can join an existing task through batching; duplicate deliveries are ignored.

For failed deliveries, check the URL, Pulumi header, and any provider signing credential. Rotating the Pulumi secret invalidates the old value immediately; update the sender's header before retrying.

<span id="schedules-owned-by-a-user"></span>
<span id="what-you-can-do-with-an-automation"></span>
<span id="creating-an-automation"></span>
<span id="defaults-that-fit-recurring-work"></span>
<span id="how-automations-interact-with-the-rest-of-neo"></span>
<span id="how-permissions-work"></span>
<span id="limitations"></span>

## Schedule recurring work

In **Automations**, select **New automation**, then **Start with a blank automation**. Enter the name, agent, and prompt:

1. Set **Runs** to **On a schedule**.
1. Set **Frequency** to hourly, daily, weekdays, weekly, or a custom cron expression. Preset times use your browser's local time zone; custom cron expressions use UTC.
1. Select **Create automation**.

## Stop future runs

Select **Pause** in the automation's actions menu to stop future runs, or **Resume** to restart them. Cancel running tasks separately. To stop all triggers and schedules for an agent, [pause the agent](/docs/ai/agents/manage/#pause-future-work-and-stop-current-work).
