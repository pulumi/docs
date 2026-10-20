---
title: Pulumi Agents
title_tag: Pulumi Agents | Infrastructure AI
meta_desc: Delegate ongoing infrastructure responsibilities to managed AI agents running in Pulumi Cloud. Configure their instructions, tools, and access for your team.
linktitle: Pulumi Agents
h1: Pulumi Agents
menu:
    ai:
        name: Pulumi Agents
        parent: ai-concepts
        identifier: ai-agents
        weight: 10
---

Pulumi Agents are managed AI agents that run in Pulumi Cloud. Each agent has saved instructions, connected tools, and permissions for its work. Use a pre-built agent or build your own to take on ongoing infrastructure responsibilities, such as investigating incidents or maintaining dependencies.

## Use pre-built agents

Pulumi provides agents for incident investigation, drift response, deployment troubleshooting, and other infrastructure work. [Choose an agent](/docs/ai/agents/configure/#start-with-a-pre-built-agent), connect the tools it needs, and adapt its instructions to your team.

[Neo](/docs/ai/neo/) is your pre-built personal agent. It works on your behalf using your existing Pulumi Cloud access. You do not need to create it or assign it a separate role.

## Build custom agents

[Build an agent](/docs/ai/agents/custom/) around your team's infrastructure and operating procedures. For example, an agent investigating checkout failures can correlate application errors with recent deployments and cloud configuration, follow your incident runbook, and prepare a fix for review. Give it your service's runbooks and access to the relevant logs, resources, and repositories.

## Connect your tools

[Connect your tools](/docs/ai/agents/integrations/) so agents can work with your cloud resources, code, logs, and issues.

## Assign and automate

[Assign work directly](/docs/ai/agents/tasks/), or use [events and schedules](/docs/ai/agents/triggers/) to start work automatically.

## Collaborate

[Collaborate in tasks or Slack threads](/docs/ai/agents/tasks/#work-with-teammates) to add context, answer questions, and refine the agent's work.

## Control access and approvals

Control which stacks, cloud accounts, and repositories an agent can access, and when it needs your approval. See [Permissions and approvals](/docs/ai/agents/permissions/) for how Pulumi Cloud roles, external credentials, and approval settings work together.

## Use Pulumi Agents

[Create and manage agents](/docs/ai/agents/create-and-manage/) for your team, or [assign work to an existing agent](/docs/ai/agents/tasks/). For personal tasks, follow the [Neo guides](/docs/ai/neo/#use-neo).
