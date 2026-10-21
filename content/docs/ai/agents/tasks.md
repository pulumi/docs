---
title: Tasks and collaboration
title_tag: Tasks and collaboration | Pulumi Agents
h1: Tasks and collaboration
meta_desc: Start Pulumi Agent tasks from Pulumi Cloud or Slack, and collaborate with your team.
menu:
    ai:
        name: Tasks and collaboration
        parent: ai-agents-create-manage
        identifier: ai-agents-tasks
        weight: 40
---

Start a task by giving an agent an assignment in [Pulumi Cloud](#start-a-task-in-pulumi-cloud) or [Slack](#work-from-slack), or configure an [event or schedule](/docs/ai/agents/triggers/) to start tasks automatically. Each task contains the agent's work and results. You and your teammates can reply to answer questions, add context, or ask for changes.

These instructions apply to agents created for your organization. For personal tasks with Neo, see [Neo tasks](/docs/ai/neo/tasks/).

## Start a task in Pulumi Cloud

Open the agent's page and enter your request in **Describe the task for this agent**. Specify the result you want and enough context to begin:

- For an incident, include the affected service, symptoms, time window, and recent changes.
- For a dependency upgrade, name the repository, dependency, target version, and compatibility requirements.
- For a cost review, identify the resources or environment, review period, and workloads that must stay running.

The task uses the agent's saved configuration. [Edit the agent](/docs/ai/agents/configure/#change-an-existing-agent) to change instructions or access across tasks.

## Work from Slack

Follow the [Slack installation and account-linking steps](/docs/ai/neo/integrations/slack/#setting-up-the-integration). Mention `@pulumi` in a channel with your request, such as “Investigate errors in the checkout service.” If prompted to choose an agent, select its name to start the task.

Continue the assignment in its Slack thread. Each participant must link their own Pulumi account and have [permission to contribute](/docs/ai/agents/permissions/#give-teammates-access); channel membership alone does not grant that permission.

## Work with teammates

Teammates with [permission to contribute](/docs/ai/agents/permissions/#give-teammates-access) can reply in the task to add evidence, answer questions, or request changes.

## Next steps

- [Send work through events or schedules](/docs/ai/agents/triggers/).
- [Review access and approval controls](/docs/ai/agents/permissions/).
- [Stop or troubleshoot work](/docs/ai/agents/manage/).
