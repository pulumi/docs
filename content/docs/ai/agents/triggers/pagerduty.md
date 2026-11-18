---
title: PagerDuty webhook
title_tag: PagerDuty webhook | Pulumi Agents
h1: PagerDuty webhook
pulumi_cloud_feature: pulumi-agents
meta_desc: Start Pulumi Agents tasks from PagerDuty events with a webhook subscription and an optional provider signing secret.
menu:
    ai:
        name: PagerDuty
        parent: ai-agents-triggers
        identifier: ai-agents-triggers-pagerduty
        weight: 40
---

After [creating a webhook automation](/docs/ai/agents/triggers/#connect-an-external-webhook) with the **PagerDuty** preset, keep the Pulumi setup panel open.

## Configure PagerDuty

1. In PagerDuty, open **Services > Service Directory** and select the service whose incidents should invoke the agent.
1. On the service's **Integrations** tab, find **Webhooks** and select **Add or manage webhooks for this service**, or **Webhook** if none exist. Select **New Webhook**.
1. Paste the Pulumi webhook URL into **Webhook URL**. Under **Event Subscription**, select the events that should start tasks. For new incidents, select `incident.triggered`.
1. Under **Custom Headers**, select **Add custom header**. Enter `X-Pulumi-Trigger-Secret` as the name and the Pulumi secret as its value. Pulumi requires this header even though PagerDuty labels it optional.
1. Select **Add Webhook** in PagerDuty.
1. If signature verification is enabled, copy the signing secret from PagerDuty's confirmation dialog into **PagerDuty signing secret** in Pulumi. Select **Done** to save it. If verification is disabled, select **Done** to close the setup panel.

The PagerDuty signing secret and the Pulumi header value are separate credentials. When signature verification is enabled, Pulumi rejects events until you save the signing secret with **Done**. Pulumi encrypts the signing secret and does not display it again.

If signature verification is disabled, Pulumi still requires the custom header. You can enable verification from the automation's edit page.

## Test the connection

Send a test notification for the configured event subscription. Follow [Test a webhook](/docs/ai/agents/triggers/#test-a-webhook) to check delivery and task results. Test deliveries can run the agent.
