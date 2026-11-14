---
title: Use your coding agent
title_tag: Use your coding agent with Pulumi
h1: Use your coding agent with Pulumi
meta_desc: Use Pulumi skills, the MCP server, and the CLI with Claude Code, Codex, Cursor, and other coding agents.
menu:
    ai:
        name: Use Pulumi with your coding agent
        parent: ai-start
        identifier: ai-coding-agents
        weight: 10
---

Use Pulumi with Claude Code, Codex, Cursor, and other coding agents. Pulumi provides skills for infrastructure workflows, an MCP server for cloud context, and a CLI for infrastructure operations.

## Pulumi Agent Skills

Skills teach your coding agent Pulumi workflows, including writing components, managing secrets, and migrating infrastructure. See [Pulumi Agent Skills](/docs/ai/concepts/agent-skills/) for the available skills and installation instructions.

## Pulumi MCP server

The MCP server lets your coding agent query stacks and resources in Pulumi Cloud and look up resource schemas in the Pulumi Registry. See [Pulumi MCP server](/docs/ai/guides/set-up-mcp-server/) for client configuration, authentication, and supported tools.

## Pulumi CLI

Coding agents that can run shell commands can use the Pulumi CLI to preview and deploy infrastructure. See [CLI for agents](/docs/ai/concepts/cli-for-agents/) for CLI features such as structured JSON output and direct resource operations.
