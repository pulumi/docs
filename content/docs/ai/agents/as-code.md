---
title: Define an agent in code
title_tag: Define an agent in code | Pulumi Agents
h1: Define an agent in code
pulumi_cloud_feature: pulumi-agents
meta_desc: Define a Pulumi Cloud agent and a failed stack update trigger in TypeScript.
menu:
    ai:
        name: Define an agent in code
        parent: ai-agents-create-manage
        identifier: ai-agents-as-code
        weight: 22
---

Define an agent and its trigger in the same Pulumi program so your team can review changes to both in a pull request. In this TypeScript example, a failed stack update starts a task for the deployment troubleshooting agent. The agent reads the update and records what failed and what to try next in the task.

<span id="define-the-agent"></span>
<span id="add-a-schedule-or-event"></span>

The program reads three values from the stack's [Pulumi ESC environment](/docs/esc/guides/pulumi-iac/). `watchedProject` and `watchedStack` identify the stack to monitor. `agentRoleId` identifies the Pulumi Cloud role that lets the agent read the stack's updates.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as pulumiservice from "@pulumi/pulumiservice";

const config = new pulumi.Config();
const orgName = pulumi.getOrganization();

const agent = new pulumiservice.api.agents.Definition("agent", {
    orgName,
    name: "deployment-troubleshooting",
    displayName: "Deployment Troubleshooting",
    purpose: "Explain why a stack update failed and suggest the next step.",
    customInstructions: [
        "Read the failed update that triggered this task and quote the error that explains the failure.",
        "Identify the affected resource if the update names one.",
        "Suggest a fix, or say what additional information you need to diagnose the failure.",
    ].join(" "),
    roleId: config.require("agentRoleId"),
});

new pulumiservice.api.AgentAutomationV2("failed-update", {
    orgName,
    name: "diagnose-failed-updates",
    kind: "triggered",
    trigger: {
        type: "stack_operation",
        quietPeriodSeconds: 30,
        stacks: [{
            routingProject: config.require("watchedProject"),
            name: config.require("watchedStack"),
        }],
        operations: ["update"],
        results: ["failed"],
    },
    task: {
        agentDefinitionId: agent.definitionID,
        toolExecutionMode: "cloud",
        message: {
            type: "user_message",
            content: "Diagnose the failed stack update.",
        },
    },
});
```

<span id="deploy-and-update-the-agent"></span>

Run `pulumi up` to create both resources. After the next failed update, open **diagnose-failed-updates** under **Agents** > **Automations** in Pulumi Cloud. Select the task under **All runs** to read the diagnosis.
