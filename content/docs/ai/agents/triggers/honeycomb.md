---
title: Honeycomb webhook
title_tag: Honeycomb webhook | Pulumi Agents
h1: Honeycomb webhook
pulumi_cloud_feature: pulumi-agents
meta_desc: Start Pulumi Agents tasks from Honeycomb triggers with a webhook recipient and the required Pulumi authentication header.
menu:
    ai:
        name: Honeycomb
        parent: ai-agents-triggers
        identifier: ai-agents-triggers-honeycomb
        weight: 10
---

After [creating a webhook automation](/docs/ai/agents/triggers/#connect-an-external-webhook) with the **Honeycomb** preset, keep the Pulumi setup panel open.

## Configure Honeycomb

1. In Honeycomb, open **Team Settings > Integrations** and select **Add Integration**. Choose the **Webhook** provider and enter a name.
1. Paste the Pulumi webhook URL into **Webhook URL**. Leave **Shared Secret** empty.
1. On the **Headers** tab, add `X-Pulumi-Trigger-Secret` with the Pulumi secret as its value.
1. Leave the **Payload** tab unchanged. Pulumi reads Honeycomb's default payload.
1. Select **Add**. Open each Honeycomb trigger that should invoke the agent, select **Add Recipient**, choose the webhook, and save the trigger.
1. Return to Pulumi and select **Done**.

Honeycomb's **Shared Secret** field does not authenticate requests to Pulumi. The custom header is required. If a payload contains a top-level `shared_secret`, Pulumi removes that field before passing the event to the agent.

## Test the connection

Send a webhook test from Honeycomb and confirm the recipient is attached to the intended trigger. Honeycomb's standard test payload appears as **Honeycomb webhook test** with a **Test** badge.

Follow [Test a webhook](/docs/ai/agents/triggers/#test-a-webhook) to check delivery and task results. Test deliveries can run the agent.
