---
title: Datadog webhook
title_tag: Datadog webhook | Pulumi Agents
h1: Datadog webhook
pulumi_cloud_feature: pulumi-agents
meta_desc: Start Pulumi Agents tasks from Datadog monitor notifications with a webhook, custom payload, and the required Pulumi header.
menu:
    ai:
        name: Datadog
        parent: ai-agents-triggers
        identifier: ai-agents-triggers-datadog
        weight: 30
---

After [creating a webhook automation](/docs/ai/agents/triggers/#connect-an-external-webhook) with the **Datadog** preset, keep the Pulumi setup panel open.

## Configure Datadog

1. In Datadog, open **Integrations** and select **Webhooks**. On the **Configuration** tab, select **New** under **Webhooks** and enter a name.
1. Paste the Pulumi webhook URL into **URL**.
1. Replace **Payload** with the template below, also available through **Copy payload** in the Pulumi setup panel. It extends Datadog's default payload with monitor fields that identify the alert.

    ```json
    {
        "body": "$EVENT_MSG",
        "last_updated": "$LAST_UPDATED",
        "event_type": "$EVENT_TYPE",
        "title": "$EVENT_TITLE",
        "date": "$DATE",
        "org": {"id": "$ORG_ID", "name": "$ORG_NAME"},
        "id": "$ID",
        "alert_id": "$ALERT_ID",
        "alert_transition": "$ALERT_TRANSITION",
        "alert_priority": "$ALERT_PRIORITY",
        "alert_query": "$ALERT_QUERY",
        "alert_scope": "$ALERT_SCOPE",
        "hostname": "$HOSTNAME",
        "tags": "$TAGS",
        "link": "$LINK"
    }
    ```

1. Under **Custom Headers**, paste the JSON from the setup panel: `{"X-Pulumi-Trigger-Secret":"<pulumi-secret>"}`. Replace `<pulumi-secret>` with the displayed Pulumi secret.
1. Select **Save** in Datadog.
1. Add `@webhook-<name>` to the notification message of each monitor that should invoke the agent, replacing `<name>` with the webhook's name.
1. Return to Pulumi and select **Done**.

## Test the connection

Test a Datadog monitor whose notification message includes `@webhook-<name>`, replacing `<name>` with the webhook's name.

Follow [Test a webhook](/docs/ai/agents/triggers/#test-a-webhook) to check delivery and task results. Test deliveries can run the agent.
