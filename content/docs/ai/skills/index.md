---
title: Agent Skills
title_tag: Pulumi Agent Skills
h1: Pulumi Agent Skills
meta_desc: Learn how to use Pulumi Agent Skills to teach AI coding assistants like Claude Code, Cursor, and GitHub Copilot how to work with Pulumi.
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    ai:
        name: Agent Skills
        parent: ai-home
        weight: 60
aliases:
- /docs/ai/agent-skills/
---

Pulumi Agent Skills are knowledge packages that teach AI coding assistants domain-specific Pulumi workflows. These skills help with infrastructure migrations, secret management, and code translation, teaching assistants how to work with Pulumi the way an experienced practitioner would.

## What are Agent Skills?

Agent Skills are reusable knowledge packages that teach AI coding assistants domain-specific workflows. They follow the [agentskills.io](https://agentskills.io) open standard and work with:

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code)
- [OpenAI Codex](https://openai.com/api/)
- [Cursor](https://cursor.sh)
- [GitHub Copilot](https://docs.github.com/en/copilot)
- [Google Gemini](https://geminicli.com/)

## Available Skills

Skills are organized into two plugin groups: Migration and Authoring.

### Migration Plugin

Convert and import infrastructure from other tools to Pulumi:

| Skill | Description |
|-------|-------------|
| pulumi-terraform-to-pulumi | Migrate Terraform projects to Pulumi |
| pulumi-cdk-to-pulumi | Convert AWS CDK applications to Pulumi |
| pulumi-arm-to-pulumi | Convert Azure ARM templates and Bicep to Pulumi |

### Authoring Plugin

Write quality Pulumi programs, components, automation, and secrets management:

| Skill | Description |
|-------|-------------|
| pulumi-best-practices | Best practices for writing reliable Pulumi programs |
| pulumi-component | Guide for authoring ComponentResource classes |
| pulumi-automation-api | Best practices for using Pulumi Automation API |
| pulumi-esc | Guidance for working with Pulumi ESC (Environments, Secrets, and Configuration) |

## Installation

### Claude Code Plugin System

For Claude Code users, the plugin system provides the simplest installation experience:

```bash
claude plugin marketplace add pulumi/agent-skills
claude plugin install pulumi-migration     # Install migration skills
claude plugin install pulumi-authoring     # Install authoring skills
```

### Universal Installation

Install all skills for use with any AI coding assistant:

```bash
npx skills add pulumi/agent-skills
```

Or install individual plugin groups:

```bash
npx skills add pulumi/agent-skills/migration      # 7 migration skills
npx skills add pulumi/agent-skills/authoring      # 4 authoring skills
```

This works with Claude Code, Cursor, Copilot, Codex, and other agent tools.

## Usage Examples

### Terraform to Pulumi Migration

Ask your AI assistant:

> "Convert this Terraform configuration to Pulumi TypeScript"

The assistant will use the `pulumi-terraform-to-pulumi` skill to produce idiomatic Pulumi code.

### CDK to Pulumi Migration

Ask your AI assistant:

```text
Help me migrate my CDK application to Pulumi
```

The assistant will use the `pulumi-cdk-to-pulumi` skill to guide you through the complete migration workflow.

### Managing Secrets with ESC

Ask your AI assistant:

```text
Set up AWS OIDC credentials using Pulumi ESC
```

The assistant will use the `pulumi-esc` skill to help configure dynamic credentials.

### Writing Components

Ask your AI assistant:

```text
Help me create a reusable Pulumi component for a web service
```

The assistant will use the `pulumi-component` skill to guide you through component authoring best practices.

## Contributing

We welcome contributions to Pulumi Agent Skills. Visit the [agent-skills repository](https://github.com/pulumi/agent-skills) on GitHub to:

- Write new skills
- Improve existing skills
- Report issues

See the [CONTRIBUTING.md](https://github.com/pulumi/agent-skills/blob/main/CONTRIBUTING.md) file for guidelines.
