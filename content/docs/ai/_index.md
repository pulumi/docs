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
aliases:
- /docs/pulumi-cloud/neo/
- /docs/iac/neo/
- /docs/neo/
- /docs/ai/neo/
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
    Pulumi is built to be driven by AI agents, including the coding agents your team already uses. Because Pulumi infrastructure is real code with a verifiable plan for every change, agents like Claude Code, Codex, Cursor, and GitHub Copilot can write, preview, and deploy it directly. The [Pulumi CLI](/docs/iac/cli/) is designed for them: run any command with `npx pulumi`, perform one-shot resource operations with [`pulumi do`](/docs/iac/cli/direct-resource-operations/), and parse structured `--json` output from the commands that emit it. [Pulumi Agent Skills](/docs/ai/skills/) teach agents proven Pulumi workflows, the [Pulumi MCP server](/docs/ai/mcp-server/) offers the same reach over MCP, and [agent accounts](/docs/administration/organizations-teams/agent-accounts/) remove signup friction entirely.

    Pulumi Neo is Pulumi's own infrastructure agent. It ships with these skills built in, and adds organizational context, policy guardrails, human-in-the-loop approvals, and scheduled autonomous work. Use your favorite agent, use Neo, or use both together: Neo for long-running, governed infrastructure tasks, and your coding agent for interactive development.

- type: button-cards
  heading: Bring your own agent
  cards:
  - icon: lightbulb
    heading: Agent Skills
    link: /docs/ai/skills/
    description: Teach Claude Code, Codex, Cursor, Copilot, and other agents Pulumi workflows.
  - icon: terminal
    heading: Pulumi CLI
    link: /docs/iac/cli/
    description: An agent-friendly CLI, from npx pulumi and pulumi do to structured JSON output.
  - icon: plug
    heading: MCP server
    link: /docs/ai/mcp-server/
    description: Give any MCP-capable agent access to your Pulumi Cloud resources and the Registry.
  - icon: rocket-launch
    heading: Agent Accounts
    link: /docs/administration/organizations-teams/agent-accounts/
    description: Ephemeral Pulumi Cloud accounts provisioned automatically for AI agents.

- type: button-cards
  heading: Pulumi Neo
  cards:
  - icon: rocket-launch
    heading: Get Started
    link: /docs/ai/get-started/
    description: Learn how to use Pulumi Neo for AI-powered infrastructure automation.
  - icon: clipboard
    heading: Tasks
    link: /docs/ai/tasks/
    description: Multi-step operations for maintenance, analysis, and infrastructure changes.
  - icon: shuffle
    heading: Pull Requests
    link: /docs/ai/pull-requests/
    description: AI-proposed changes submitted as pull requests for review.
  - icon: list-checks
    heading: Code Reviews
    link: /docs/ai/code-reviews/
    description: Neo reviews your pull requests against what Pulumi Cloud knows about your running infrastructure.
  - icon: eye
    heading: Previews
    link: /docs/ai/running-previews/
    description: Generate infrastructure previews with approval gates.
  - icon: plug
    heading: Integrations
    link: /docs/ai/integrations/
    description: Connect Neo to external services, cloud CLIs, GitHub, and Slack.
  - icon: terminal
    heading: Neo in the CLI
    link: /docs/ai/pulumi-cli/
    description: Run pulumi neo to start an interactive Neo session in your terminal.
  - icon: clock
    heading: Automations
    link: /docs/ai/automations/
    description: Turn any Neo task into recurring work that produces pull requests on a schedule.

- type: flat
  heading: Have questions?
  description: <p>For questions or feedback, reach out on <a href="https://slack.pulumi.com" target="_blank">community Slack</a>, <a href="https://github.com/pulumi" target="_blank">GitHub</a>, or <a href="/support/">contact support</a>.</p>
---
