---
title: Agent Skills
title_tag: Pulumi Agent Skills
h1: Pulumi Agent Skills
meta_desc: Learn how to use Pulumi Agent Skills to teach AI coding assistants like Claude Code, Cursor, GitHub Copilot, and JetBrains Junie how to work with Pulumi.
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
- [JetBrains Junie](https://www.jetbrains.com/junie/)

## Available Skills

Skills are organized into three plugin groups: Migration, Pulumi, and Delegation.

### Migration Plugin

Convert and import infrastructure from other tools to Pulumi:

| Skill | Description |
|-------|-------------|
| pulumi-terraform-to-pulumi | Migrate Terraform projects to Pulumi |
| pulumi-cdk-to-pulumi | Migrate AWS CDK applications to Pulumi |
| cloudformation-to-pulumi | Migrate AWS CloudFormation stacks/templates to Pulumi |
| pulumi-arm-to-pulumi | Migrate Azure ARM templates and Bicep to Pulumi |

### Pulumi Plugin

Entry-point and specialized skills for writing and operating Pulumi infrastructure:

| Skill | Description |
|-------|-------------|
| pulumi-overview | Entry-point across `pulumi do`, IaC projects, and Pulumi Cloud; routes to specialized skills |
| pulumi-best-practices | Best practices for writing reliable Pulumi programs |
| pulumi-component | Guide for authoring ComponentResource classes |
| pulumi-automation-api | Best practices for using Pulumi Automation API |
| pulumi-esc | Guidance for working with Pulumi ESC (Environments, Secrets, and Configuration) |
| package-usage | Audit which stacks across an organization use a package and at what versions |
| provider-upgrade | Safely upgrade a Pulumi provider and reconcile the resulting diff |
| pulumi-upgrade-provider | Automate Pulumi provider repo upgrades with the `upgrade-provider` tool |
| upstream-patches | Manage upstream Terraform patch stacks in provider repos |

### Delegation Plugin

Hand off in-progress work from coding agents to Pulumi Neo:

| Skill | Description |
|-------|-------------|
| pulumi-neo-handoff | Transfer the current work to a Pulumi Neo task with goal, repository pointers, and a compacted conversation summary |

## Installation

### Claude Code Plugin System

For Claude Code users, the plugin system provides the simplest installation experience:

```bash
/plugin marketplace add pulumi/agent-skills
/plugin install pulumi-migration      # Install migration skills
/plugin install pulumi                # Install Pulumi skills (overview + specialized)
/plugin install pulumi-delegation     # Install delegation skills (Neo handoff)
```

### OpenAI Codex

Register the marketplace, then install plugins from the Codex TUI:

```bash
codex plugin marketplace add pulumi/agent-skills
```

Once the marketplace is registered, run `codex`, open the plugin marketplace, and pick `pulumi-migration`, `pulumi`, or `pulumi-delegation`.

### Universal Installation

Install all skills for use with any AI coding assistant:

```bash
npx skills add pulumi/agent-skills --skill '*'
```

Or install individual plugin groups:

```bash
npx skills add pulumi/agent-skills/migration --skill '*'      # 4 migration skills
npx skills add pulumi/agent-skills/pulumi --skill '*'         # 9 pulumi skills (overview + specialized)
npx skills add pulumi/agent-skills/delegation --skill '*'     # 1 delegation skill
```

This works with Claude Code, Cursor, Copilot, Codex, Junie, and other agent tools. To install for a specific agent, use the `--agent` flag:

```bash
npx skills add pulumi/agent-skills --skill '*' --agent junie
```

## Usage Examples

### General Pulumi Infrastructure

Ask your AI assistant:

```text
Create an S3 bucket and a Cloudflare DNS record
```

The assistant will use the `pulumi-overview` skill and route to specialized skills when deeper expertise is needed.

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

### Upgrading Providers

Ask your AI assistant:

```text
Help me upgrade the Pulumi AWS provider safely without changing real infrastructure
```

The assistant will use the `provider-upgrade` skill to guide you through a low-risk upgrade workflow.

### Handing Off Work to Pulumi Neo

Ask your AI assistant:

```text
Hand this off to Neo to apply the staging migration in production
```

The assistant will use the `pulumi-neo-handoff` skill to package the goal, repository state, and conversation summary into a new Pulumi Neo task and return a task URL.

## Contributing

We welcome contributions to Pulumi Agent Skills. Visit the [agent-skills repository](https://github.com/pulumi/agent-skills) on GitHub to:

- Write new skills
- Improve existing skills
- Report issues

See the [CONTRIBUTING.md](https://github.com/pulumi/agent-skills/blob/main/CONTRIBUTING.md) file for guidelines.
