---
title: Trigger Pulumi Agents from Infrastructure Events
date: 2026-11-23
meta_desc: Define a Pulumi Agent and a failed stack update trigger in TypeScript to investigate deployment failures and report findings in Slack.
feature_image: feature.png
authors:
    - pulumi-ai-team
tags:
    - ai-agents
    - typescript
category: product
---

Pulumi Agents can start work automatically in response to a Pulumi event or a webhook. With a trigger, you can give an agent a recurring assignment and choose when it should start. For events in Pulumi Cloud, that choice can be as specific as a failed update on a single stack.

A failed deployment is one use for a trigger. The agent can read the failed update, identify the affected resource, and post a diagnosis in Slack. That puts the error and a suggested next step in the deployment channel for the team to review.

<!--more-->

## A trigger for failed deployments

The example below defines an agent and a trigger in TypeScript. The trigger selects failed updates on `checkout/prod` and starts an investigation. The agent has read access to the stack’s update history and instructions to report what failed and what to check next.

The agent’s instructions describe what you want to learn from each failure. Its `roleId` determines what it can read. Here, `agentRoleId` is a configuration key that holds the ID of an existing Pulumi Cloud role with `stack:read` on `checkout/prod`. The configuration steps below show how to look up that ID and supply it through Pulumi ESC.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as service from "@pulumi/pulumiservice";

const config = new pulumi.Config();
const orgName = pulumi.getOrganization();

const agent = new service.api.agents.Definition("troubleshooter", {
    orgName,
    name: "deployment-troubleshooter",
    displayName: "Deployment Troubleshooter",
    roleId: config.require("agentRoleId"),
    customInstructions: [
        "Read the failed update and quote the error that explains the failure.",
        "Identify the affected resource if the update names one.",
        "Suggest what to check next and explain why.",
    ].join(" "),
});
```

## Start a task when an update fails

Add the automation to the same program. Its trigger matches three details that Pulumi Cloud records for a stack operation: the stack, the operation, and the result. When an `update` to `checkout/prod` finishes with a `failed` result, Pulumi starts a task for the agent referenced by `agent.definitionID`.

```typescript
new service.api.AgentAutomationV2("failed-update", {
    orgName,
    name: "Investigate failed production updates",
    kind: "triggered",
    trigger: {
        type: "stack_operation",
        stacks: [{ routingProject: "checkout", name: "prod" }],
        operations: ["update"],
        results: ["failed"],
        quietPeriodSeconds: 30,
    },
    task: {
        agentDefinitionId: agent.definitionID,
        toolExecutionMode: "cloud",
        message: { type: "user_message", content: "Investigate this failed update." },
    },
    notificationTargets: [
        { type: "slack", channelID: config.require("slackChannelId") },
    ],
});
```

The first failure starts the task immediately. The 30-second window lets subsequent matching events join the investigation. The agent reads the update using its Pulumi Cloud role, and Pulumi delivers the findings to the Slack channel in `notificationTargets`.

## Configure and deploy

Create a TypeScript project named `deployment-agents` with `pulumi new typescript --name deployment-agents`, and put both code snippets above in its `index.ts`. Select a stack for that project in the same Pulumi Cloud organization as `checkout/prod`.

1. **Find the role ID.** With a Pulumi account that can list roles in your organization, run the command below. Replace `YOUR_ORG` with the organization name. The output lists each role’s name and ID. Copy the ID of the role you’ve granted read access to `checkout/prod`.

   ```bash
   pulumi api /api/orgs/YOUR_ORG/roles --method GET -F uxPurpose=role |
     jq -r '.roles[] | [.name, .id] | @tsv'
   ```

1. **Connect the Slack channel.** Have a workspace admin install the Pulumi Slack app. In Pulumi Cloud, link the account you’ll use to deploy the automation to your Slack identity under **Account settings > Pulumi Agents**. This lets Pulumi find channels in your workspace. Invite the app to your deployment channel and copy the channel ID from its details in Slack.

1. **Supply both IDs through ESC.** Add the following to an ESC environment named `deployment-agents/settings`. The `deployment-agents` prefix on each key matches the project name in `Pulumi.yaml`.

   ```yaml
   values:
     pulumiConfig:
       deployment-agents:agentRoleId: "<Pulumi Cloud role ID>"
       deployment-agents:slackChannelId: "<Slack channel ID>"
   ```

From the `deployment-agents` project, import the environment into the selected stack and deploy:

```bash
npm install @pulumi/pulumiservice@1.7.0
pulumi config env add deployment-agents/settings
pulumi up
```

`pulumi up` creates the **Deployment Troubleshooter** agent and the **Investigate failed production updates** automation. The automation begins watching `checkout/prod`.

## What the team sees in Slack

In a live test on a disposable stack, the `check-release-manifest` resource ran a local command to verify that `release-manifest.json` existed. The file was absent, so the update failed.

Pulumi posted the automation’s name in the deployment channel as soon as the investigation started. The agent then replied in the Slack thread with its diagnosis. `check-release-manifest` had failed with `Missing release-manifest.json`. The agent suggested checking whether the build had generated the file and whether the command was looking in the right directory. Selecting **Continue in Pulumi** opened the full investigation for that update.
