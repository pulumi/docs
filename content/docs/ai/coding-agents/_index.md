---
title: Use your coding agent
title_tag: Use your coding agent with Pulumi
h1: Use your coding agent with Pulumi
meta_desc: Use Pulumi skills, the MCP server, and the CLI with Claude Code, Codex, Cursor, and other coding agents.
menu:
    ai:
        name: Use your coding agent
        parent: ai-home
        identifier: ai-coding-agents
        weight: 30
---

Use Pulumi from Claude Code, Codex, Cursor, or another coding agent in your repository.

## Install Pulumi skills {#pulumi-agent-skills}

Skills give your coding agent instructions for work such as writing components, managing secrets, and migrating Terraform projects. [Install the skills for your coding agent](/docs/ai/concepts/agent-skills/), then ask it to use the relevant skill on your project.

## Run Pulumi commands {#pulumi-cli}

Your coding agent needs the CLI to run a preview or another Pulumi command. See [CLI for agents](/docs/ai/concepts/cli-for-agents/) for installation options and commands to preview changes to your stack.

## Look up cloud resources and schemas {#pulumi-mcp-server}

[Connect the MCP server](/docs/ai/guides/set-up-mcp-server/) when your coding agent needs to query stacks and resources in Pulumi Cloud or look up resource schemas in the Pulumi Registry. The setup guide includes configuration for each supported client.

The server also exposes a tool that can start tasks and send approvals. Review [tool access and costs](/docs/ai/guides/set-up-mcp-server/#costs-and-edition-requirements) when choosing which tools to enable.
