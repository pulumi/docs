---
title: Tasks and collaboration
title_tag: Tasks and collaboration | Pulumi Agents
h1: Tasks and collaboration
meta_desc: Start Pulumi Agent tasks from Pulumi Cloud, Slack, or Linear, and collaborate with your team.
menu:
    ai:
        name: Tasks and collaboration
        parent: ai-agents-create-manage
        identifier: ai-agents-tasks
        weight: 40
---

Start a task by giving an agent an assignment in [Pulumi Cloud](#start-a-task-in-pulumi-cloud), [Slack](#work-from-slack), or [Linear](#assign-work-from-linear), or configure an [event or schedule](/docs/ai/agents/triggers/) to start tasks automatically. Each task contains the agent's work and results. You and your teammates can reply to answer questions, add context, or ask for changes.

These instructions apply to agents created for your organization. For personal tasks with Neo, see [Neo tasks](/docs/ai/neo/tasks/).

## Start a task in Pulumi Cloud

Open the agent's page and enter your request in **Describe the task for this agent**. Specify the result you want and enough context to begin:

- For an incident, include the affected service, symptoms, time window, and recent changes.
- For a dependency upgrade, name the repository, dependency, target version, and compatibility requirements.
- For a cost review, identify the resources or environment, review period, and workloads that must stay running.

The task uses the agent's saved configuration. [Edit the agent](/docs/ai/agents/configure/#change-an-existing-agent) to change instructions or access across tasks.

## Work from Slack

Follow the [Slack installation and account-linking steps](/docs/ai/neo/integrations/slack/#setting-up-the-integration). Mention the installed Pulumi app in a channel and ask it to list your agents. Address an agent by name, for example, `ask Incident investigator to investigate errors in the checkout service`.

Continue the assignment in its Slack thread. Each participant must link their own Pulumi account and have permission to contribute; channel membership alone does not grant that permission.

## Assign work from Linear

Delegate a Linear issue to the connected Pulumi agent to start a task. The agent uses the issue description and your message as context. Continue the conversation in Linear, and open the task in Pulumi Cloud when an action needs approval.

Your Linear account must be linked to your Pulumi account, with permission to use the agent.

## Work with teammates

Teammates with permission to contribute can reply in the task to add evidence, answer questions, or request changes.

## Next steps

- [Send work through events or schedules](/docs/ai/agents/triggers/).
- [Review access and approval controls](/docs/ai/agents/permissions/).
- [Stop or troubleshoot work](/docs/ai/agents/manage/).
