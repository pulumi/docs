---
title: Pulumi Agents
title_tag: Pulumi Agents | Infrastructure AI
meta_desc: Delegate ongoing infrastructure responsibilities to managed AI agents running in Pulumi Cloud. Configure their instructions, tools, and access for your team.
linktitle: Pulumi Agents
h1: Pulumi Agents
aliases:
- /docs/pulumi-cloud/neo/
- /docs/iac/neo/
- /docs/neo/
- /docs/ai/neo/
menu:
    ai:
        name: Pulumi Agents
        parent: ai-home
        identifier: ai-agents
        weight: 20
---

With Pulumi Agents, you can delegate infrastructure work in Pulumi Cloud. Ask an agent to diagnose a failed deployment, respond to an incident, or prepare a dependency upgrade. The agent uses the repositories and tools you connect to carry out the request. For code changes, it can open a pull request for your team to review and deploy.

<span id="neo-and-agents-you-configure"></span>
<span id="use-neo"></span>
<span id="tasks-and-access"></span>

## Start with Neo

Neo is the built-in agent in Pulumi Agents. You can give it work without creating or configuring another agent. By default, Neo uses your Pulumi Cloud permissions to access your stacks and configuration.

[Start your first task with Neo in Pulumi Cloud](/docs/ai/get-started/neo/), or use Neo from your [terminal](/docs/ai/concepts/neo/neo-in-the-cli/) or [editor](/docs/ai/concepts/neo/neo-in-your-editor/).

## Create an agent for your team

{{< pulumi-cloud "pulumi-agents" />}}

Create an agent to delegate infrastructure work and collaborate with your team. Give the agent instructions, connect the tools it needs, and assign a Pulumi Cloud role to control its access. To review changes to the agent in a pull request, [define it in code](/docs/ai/agents/as-code/).

<span id="use-pre-built-agents"></span>

Pulumi provides agents for incident investigation, drift response, deployment troubleshooting, and other infrastructure work. [Choose an agent](/docs/ai/agents/configure/) and tailor its instructions and settings to your team's work.

<span id="build-custom-agents"></span>

To supply your own instructions, [start with a blank agent](/docs/ai/agents/configure/#build-your-own-agent).

<span id="connect-your-tools"></span>
<span id="control-access-and-approvals"></span>

See [Integrations](/docs/ai/agents/integrations/) to connect repositories and other systems, and [Permissions and approvals](/docs/ai/agents/permissions/) to choose what the agent can access and when it asks for approval.

## Assign work

<span id="assign-and-automate"></span>
<span id="collaborate"></span>
<span id="use-pulumi-agents"></span>

Start a task by asking the agent to do something specific, such as upgrading a dependency in a repository and opening a pull request. Follow its progress in the task and reply if it needs more information. For agents your team creates, teammates with access can contribute to the same task.

[Continue a task with your team](/docs/ai/agents/tasks/), or [configure an event or schedule](/docs/ai/agents/triggers/) to start tasks automatically.

## Review proposed changes

[Review the code and preview](/docs/ai/agents/review-changes/) before merging a pull request. Your team's deployment workflow applies the changes.

See [Manage and troubleshoot](/docs/ai/agents/manage/) to change an agent's configuration, stop its work, or resolve a failed task.
