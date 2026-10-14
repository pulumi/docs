---
title: Pulumi Agents
title_tag: Pulumi Agents | Infrastructure AI
meta_desc: Delegate infrastructure work to Pulumi Agents. Use a pre-built agent or create your own, assign tasks, and review the results with your team.
linktitle: Pulumi Agents
docs_home: true
wide_banner: true
notitle: true
norightnav: true
h1: Pulumi Agents
description: <p>Pulumi Agents are managed AI agents built for infrastructure work. Pulumi provides the runtime, infrastructure tools, and access controls; you define the work and the access each agent needs. Choose a pre-built agent or create your own, then assign tasks or automate recurring work.</p>
menu:
    ai:
        name: Pulumi Agents
        parent: ai-concepts
        identifier: ai-agents
        weight: 10
sections:
    - type: flat
      heading: Use pre-built agents
      description: <p>Pulumi provides agents for incident investigation, drift response, deployment troubleshooting, and other infrastructure work. <a href="/docs/ai/agents/configure/#start-with-a-pre-built-agent">Choose an agent</a>, connect the tools it needs, and adapt its instructions to your team.</p><p>For work you want to do with your own Pulumi Cloud permissions, use <a href="/docs/ai/neo/">Neo, the pre-built personal agent</a>. Ask it to investigate infrastructure or make changes from Pulumi Cloud, the <a href="/docs/ai/neo/pulumi-cli/">terminal</a>, or your <a href="/docs/ai/neo/editors/">editor</a>.</p>
    - type: flat
      heading: Build custom agents
      description: <p><a href="/docs/ai/agents/custom/">Build an agent</a> for a specific job, such as finding resources with missing cost-allocation tags and opening pull requests to add them. Define which tags your team requires, where to find their values, and which repositories to check. The agent follows those instructions each time you assign it work.</p>
    - type: text-columns
      items:
          - heading: Connect your tools
            description: Connect the tools your team uses so agents can work with your cloud resources, code, logs, issues, and other context.
          - heading: Assign and automate
            description: Assign tasks directly, schedule recurring work, or set up an agent to respond to alerts and Pulumi events.
          - heading: Collaborate
            description: Work with teammates in shared agent tasks or Slack threads to add context, answer questions, and refine the agent's work.
    - type: flat
      heading: Control access and approvals
      description: <p>Control which stacks, cloud accounts, and repositories an agent can access, and when it needs your approval. See <a href="/docs/ai/agents/permissions/">Permissions and approvals</a> for how Pulumi Cloud roles, external credentials, and approval settings work together.</p>
    - type: flat
      heading: Use Pulumi Agents
      description: |
          <p><a href="/docs/ai/agents/create-and-manage/">Create and manage agents</a> for your team, or <a href="/docs/ai/agents/tasks/">assign work to an existing agent</a>. For personal tasks, follow the <a href="/docs/ai/neo/">Neo guides</a>.</p>
---
