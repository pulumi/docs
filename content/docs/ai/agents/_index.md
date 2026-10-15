---
title: Pulumi Agents
title_tag: Pulumi Agents | Infrastructure AI
meta_desc: Delegate infrastructure work to Pulumi Agents. Use a pre-built agent or create your own, assign tasks, and review the results with your team.
linktitle: Pulumi Agents
h1: Pulumi Agents
menu:
    ai:
        name: Pulumi Agents
        parent: ai-concepts
        identifier: ai-agents
        weight: 10
---

Pulumi Agents are managed AI agents built for infrastructure work. Pulumi provides the runtime, infrastructure tools, and access controls; you define the work and the access each agent needs. Choose a pre-built agent or create your own, then assign tasks or automate recurring work.

## Use pre-built agents

Pulumi provides agents for incident investigation, drift response, deployment troubleshooting, and other infrastructure work. [Choose an agent](/docs/ai/agents/configure/#start-with-a-pre-built-agent), connect the tools it needs, and adapt its instructions to your team.

For work you want to do with your own Pulumi Cloud permissions, use [Neo, the pre-built personal agent](/docs/ai/neo/). Ask it to investigate infrastructure or make changes from Pulumi Cloud, the [terminal](/docs/ai/neo/pulumi-cli/), or your [editor](/docs/ai/neo/editors/).

## Build custom agents

[Build an agent](/docs/ai/agents/custom/) for a specific job, such as finding resources with missing cost-allocation tags and opening pull requests to add them. Define which tags your team requires, where to find their values, and which repositories to check. The agent follows those instructions each time you assign it work.

## Connect your tools

Connect the tools your team uses so agents can work with your cloud resources, code, logs, issues, and other context.

## Assign and automate

Assign tasks directly, schedule recurring work, or set up an agent to respond to alerts and Pulumi events.

## Collaborate

Work with teammates in shared agent tasks or Slack threads to add context, answer questions, and refine the agent's work.

## Control access and approvals

Control which stacks, cloud accounts, and repositories an agent can access, and when it needs your approval. See [Permissions and approvals](/docs/ai/agents/permissions/) for how Pulumi Cloud roles, external credentials, and approval settings work together.

## Use Pulumi Agents

[Create and manage agents](/docs/ai/agents/create-and-manage/) for your team, or [assign work to an existing agent](/docs/ai/agents/tasks/). For personal tasks, follow the [Neo guides](/docs/ai/neo/#use-neo).
