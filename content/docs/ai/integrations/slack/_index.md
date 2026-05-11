---
title: Slack
title_tag: Neo Slack Integration
h1: Slack Integration
meta_desc: Mention @Neo in Slack channels to bring Neo into your team conversations.
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    ai:
        name: Slack
        parent: ai-integrations
        weight: 3
        identifier: ai-integrations-slack
---

Mention `@Neo` in any channel where Neo has been added to start a Neo [task](/docs/ai/tasks/) without leaving Slack. The response lands in the same thread, and follow-up messages continue the conversation, so the full exchange stays where the discussion is already happening.

## What you can do with `@Neo`

Neo has the same capabilities it does anywhere else: it can check stack state, investigate failures, walk through what a change will do, and carry out actions the team has agreed on. The difference is that the conversation happens in a Slack thread instead of the Pulumi Cloud console, which means the rest of the channel has visibility into what was asked and what Neo found.

## Setting up the integration

### 1. Install the Pulumi Neo Slack app

A Slack workspace admin installs the **Pulumi Neo Slack app** to the workspace.

### 2. Connect your Pulumi user to Slack

In Pulumi Cloud, open your **User account** → **Neo Slack** and connect your Slack identity. This lets Neo recognize you when you mention it in Slack.

### 3. Add Neo to a channel

In the channel where you want to mention Neo, open the channel's settings, navigate to **Integrations**, then **Add apps**, and add the Pulumi Neo app. Once per channel.

### 4. Mention `@Neo`

Mention `@Neo` followed by what you want:

> @Neo summarize the production stack.

Neo replies in the same thread.

## How permissions work

Tasks started from Slack run with the [RBAC permissions](/docs/pulumi-cloud/access-management/rbac/) of the Pulumi Cloud user linked to your Slack identity.

## Limitations

- Starting a conversation with Neo in a direct message isn't supported.
- One task per thread.
- Approve and reject happen in the Pulumi console, not in Slack.
