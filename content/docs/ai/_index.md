---
title_tag: "Infrastructure AI"
meta_desc: Use AI agents with Pulumi. Bring Claude Code, Codex, or Cursor via Agent Skills and the MCP server, or use Neo, the purpose-built infrastructure agent.
title: Infrastructure AI
linktitle: Infrastructure AI
docs_home: true
notitle: true
norightnav: true
h1: Infrastructure AI
description: <p>Pulumi works with the AI agents you already use and provides Neo, a purpose-built infrastructure agent, for the deepest integration.</p>
menu:
    ai:
        identifier: ai-home
        weight: 1

link_buttons:
  primary:
    label: Get Started
    link: /docs/ai/get-started/

sections:
- type: flat
  heading: Overview
  description_md: |
    Pulumi is built to be driven by AI agents, including the coding agents your team already uses. Because Pulumi infrastructure is real code with a verifiable plan for every change, agents like Claude Code, Codex, Cursor, and GitHub Copilot can write, preview, and deploy it directly. The [Pulumi CLI](/docs/ai/concepts/cli-for-agents/) is designed for them: run any command with `npx pulumi`, perform one-shot resource operations with [`pulumi do`](/docs/iac/cli/direct-resource-operations/), and parse structured `--json` output. [Pulumi Agent Skills](/docs/ai/concepts/agent-skills/) teach agents proven Pulumi workflows, the [Pulumi MCP server](/docs/ai/guides/set-up-mcp-server/) offers the same reach over [MCP](/what-is/mcp-for-infrastructure-as-code/), and [agent accounts](/docs/administration/concepts/agent-accounts/) remove signup friction entirely.

    [Pulumi Neo](/docs/ai/concepts/neo/) is Pulumi's own infrastructure agent, built on the same foundations and adding organizational context, policy guardrails, human-in-the-loop approvals, and scheduled autonomous work. Use your favorite agent, use Neo, or use both together: Neo for long-running, governed infrastructure tasks, and your coding agent for interactive development.

- type: button-cards
  heading: Explore Infrastructure AI
  cards:
  - icon: rocket-launch
    heading: Get started
    link: /docs/ai/get-started/
    description: Connect the coding agent you already use to Pulumi, or enable Pulumi Neo for your organization and run your first task.
  - icon: lightbulb
    heading: Concepts
    link: /docs/ai/concepts/
    description: How Agent Skills and the agent-friendly Pulumi CLI work, and how Neo handles tasks, permissions, pull requests, and automations.
  - icon: pulumi-neo
    heading: Pulumi Neo
    link: /docs/ai/concepts/neo/
    description: Pulumi's purpose-built infrastructure agent. Investigates your live infrastructure, reviews and proposes changes to your IaC code, and takes on recurring maintenance.
  - icon: wrench
    heading: Guides
    link: /docs/ai/guides/
    description: Step-by-step tasks, such as connecting Claude Code, Cursor, and other agents to the Pulumi MCP server.
  - icon: plug
    heading: Integrations
    link: /docs/ai/integrations/
    description: Connect Neo to external MCP servers, cloud CLIs, and Slack.
  - icon: books
    heading: Reference
    link: /docs/ai/reference/
    description: The tools and prompts the Pulumi MCP server exposes, and the pulumi neo CLI command.

- type: flat
  heading: Have questions?
  description: <p>For questions or feedback, reach out on <a href="https://slack.pulumi.com" target="_blank">community Slack</a>, <a href="https://github.com/pulumi" target="_blank">GitHub</a>, or <a href="/support/">contact support</a>.</p>
---
