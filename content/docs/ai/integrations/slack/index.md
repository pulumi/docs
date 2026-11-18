---
title: Slack
title_tag: Slack integration | Pulumi Agents
h1: Slack integration
meta_desc: Start Pulumi Agents tasks in Slack, connect your account, and collaborate in task threads.
aliases:
- /docs/ai/neo/integrations/slack/
menu:
    ai:
        name: Slack
        parent: ai-agents-integrations
        weight: 40
        identifier: ai-integrations-slack
pulumi_cloud_feature: neo-slack
---

<span id="what-you-can-do-with-neo"></span>

Delegate work by mentioning the Pulumi app in a channel or sending it a direct message. The agent posts its results in the Slack thread. You can use Neo or choose an agent your team has configured.

## Setting up the integration

### 1. Install the Slack app {#1-install-the-pulumi-neo-slack-app}

A Slack workspace admin installs the [**Pulumi Slack app**](https://api.pulumi.com/api/slack/neo/install) to the workspace.

### 2. Connect your Pulumi user to Slack

In Pulumi Cloud, open **Account settings** > **Pulumi Agents** and connect your Slack account. This links requests from your Slack account to your Pulumi account.

### 3. Start a task {#3-mention-neo-in-a-channel}

Add the app to the channel, then mention `@pulumi` with your request. For example:

> @pulumi explain why the preview failed for the checkout production stack. Show the relevant error and prepare a pull request if a code change is needed.

You can also open the app's **Messages** tab and send your request directly. If prompted to choose an agent, select the agent you want to use.

## How permissions work

Your Neo tasks use the permissions of your linked Pulumi Cloud account. Tasks assigned to an agent your team has configured use that agent's role.

To reply to a task assigned to a team agent, each participant must link their Pulumi account and have permission to contribute to that task. Joining a Slack channel does not grant Pulumi Cloud access. See [Permissions](/docs/ai/agents/permissions/) for agent roles and access to connected tools.

Channel members can read messages posted in the thread. Choose a channel whose membership is appropriate for the task's findings.

## Continue a task {#limitations}

Reply in the existing thread to provide context or request revisions. Each thread corresponds to one task. Start a new conversation for a separate assignment.
