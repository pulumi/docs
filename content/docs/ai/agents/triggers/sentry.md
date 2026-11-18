---
title: Sentry webhook
title_tag: Sentry webhook | Pulumi Agents
h1: Sentry webhook
pulumi_cloud_feature: pulumi-agents
meta_desc: Start Pulumi Agents tasks from Sentry alerts or issue events with an internal integration and webhook signature verification.
menu:
    ai:
        name: Sentry
        parent: ai-agents-triggers
        identifier: ai-agents-triggers-sentry
        weight: 20
---

After [creating a webhook automation](/docs/ai/agents/triggers/#connect-an-external-webhook) with the **Sentry** preset, keep the Pulumi setup panel open. You need the **Manager** or **Owner** role in Sentry to create an internal integration.

## Configure Sentry

1. In Sentry, open **Settings > Custom Integrations**, select **Create New Integration**, choose **Internal Integration**, and select **Next**.
1. Enter a name and paste the Pulumi webhook URL into **Webhook URL**.
1. In **Webhook Headers**, paste the line from the Pulumi setup panel: `X-Pulumi-Trigger-Secret: <pulumi-secret>`. Replace `<pulumi-secret>` with the displayed Pulumi secret.
1. Turn on **Alert Action** to let alert rules notify the integration. To receive issue events instead, set **Issue & Event** to **Read** and select **issue** under **Webhooks**.
1. Select **Save Changes**.
1. Signature verification is enabled by default. Copy the integration's **Client Secret** from Sentry's **Credentials** section into **Sentry client secret** in Pulumi, then select **Done**. Sentry displays this secret only briefly after creating the integration.
1. For alert rules, add the action **Send a notification via an integration** to each alert that should invoke the agent and select this integration.

The Sentry client secret and the Pulumi header value are separate credentials. Pulumi uses the client secret to verify the `Sentry-Hook-Signature` header against the request body. When verification is enabled, requests are rejected until you save the client secret with **Done**. Pulumi encrypts the client secret and does not display it again.

If you disable signature verification, Pulumi still requires `X-Pulumi-Trigger-Secret` on every delivery. You can enable verification from the automation's edit page.

Sentry sends its integration webhook payload directly to Pulumi; no custom payload template is needed.

## Test the connection

Test the configured alert action or issue subscription. If signature verification is enabled and delivery fails, check that the integration's client secret is saved in Pulumi.

Follow [Test a webhook](/docs/ai/agents/triggers/#test-a-webhook) to check delivery and task results. Test deliveries can run the agent.
