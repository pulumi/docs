---
title: "Pulumi Agent Skills: Best practices and more for AI coding assistants"
date: 2026-01-28
draft: false
meta_desc: "Introducing packaged Pulumi expertise that works across Claude Code, Cursor, GitHub Copilot, and other AI coding assistants."
meta_image: meta.png
authors:
    - neo-team
tags:
    - ai
    - platform-engineering
    - features
    - claude-code
    - codex
    - ai-agents
schema_type: auto

social:
    twitter: |
        Introducing Pulumi Agent Skills: 11 skills in 2 plugin groups

        - Migration (7): Terraform, CDK, ARM/Azure to Pulumi
        - Authoring (4): Best practices, components, Automation API, ESC

        Works with Claude Code, Cursor, Copilot, and more.

        Install: npx skills add pulumi/agent-skills
    linkedin: |
        **Pulumi Agent Skills: Teaching AI Assistants How Experts Write Infrastructure**

        AI coding assistants generate infrastructure code that works but often misses what matters. The gap is not intelligence, it is expertise.

        **The Problem**
        General-purpose agents lack the domain knowledge that experienced Pulumi developers accumulate. They do not know that creating resources inside apply() breaks preview. They have not internalized the workflow differences between converting Terraform state versus just translating HCL syntax.

        **The Solution**
        Pulumi Agent Skills packages this expertise into structured knowledge that works across Claude Code, Cursor, GitHub Copilot, VS Code, Codex, and Gemini. Now available in 11 skills organized into two plugin groups.

        **What You Get**
        - Migration Plugin (7 skills): Complete Terraform, CDK, and ARM/Azure migration workflows with automated conversion and import tools
        - Authoring Plugin (4 skills): Best practices, component authoring, Automation API patterns, and Pulumi ESC for OIDC setup and credential management

        **Install All Skills or Choose Specific Groups**
        Claude Code: /plugin install pulumi-migration
        Universal: npx skills add pulumi/agent-skills

        Read more: pulumi.com/blog/pulumi-agent-skills
---

AI coding assistants have transformed how developers write software, including infrastructure code. Tools like Claude Code, Cursor, and GitHub Copilot can generate code, explain complex systems, and automate tedious tasks. But when it comes to infrastructure, these tools often produce code that works but misses the mark on patterns that matter: proper secret handling, correct resource dependencies, idiomatic component structure, and the dozens of other details that separate working infrastructure from production-ready infrastructure.

<!--more-->

We built [Neo](https://www.pulumi.com/product/neo/) for teams that want deep Pulumi expertise combined with organizational context and deployment governance. But developers have preferred tools, and we want people to succeed with Pulumi wherever they work. Some teams live in Claude Code. Others use Cursor, Copilot, Codex, Gemini CLI, or other platforms. That is why we are releasing Pulumi Agent Skills, a collection of packaged expertise that teaches any AI coding assistant how to work with Pulumi the way an experienced practitioner would.

## What are agent skills?

Skills are structured knowledge packages that follow the open [Agent Skills](https://agentskills.io) specification. They work across multiple AI coding platforms including Claude Code, GitHub Copilot, Cursor, VS Code, Codex, and Gemini CLI. When you install Pulumi skills, your AI assistant gains access to detailed workflows, code patterns, and decision trees for common infrastructure tasks.

## Available Pulumi skills

We are launching a set of skills organized into two plugin groups: migration and authoring. You can install all skills at once or choose specific plugin groups based on your needs.

### Migration Skills

Convert and import infrastructure from other tools to Pulumi. This plugin includes seven skills covering complete migration workflows, not just syntax translation.

* **Terraform to Pulumi** walks through the full migration workflow. It handles state translation, provider version alignment, and the iterative process of achieving a clean `pulumi preview` with no unexpected changes.

* **CDK to Pulumi** covers the complete AWS CDK migration workflow end to end, from conversion and import to handling CDK-specific constructs like Lambda-backed custom resources and cross-stack references.

* **Azure to Pulumi** covers the complete Azure Resource Manager and Bicep migration workflow, handling template conversion and resource import with guidance on achieving zero-diff validation.

### Authoring Skills

This plugin includes four skills focused on code quality, reusability, and credential management.

**Pulumi best practices** encodes the patterns that prevent common mistakes. It covers output handling, component structure, secrets management, safe refactoring with aliases, and deployment workflows. The skill flags anti-patterns that can cause issues with preview, dependencies, and production deployments.

**Pulumi Component** provides a complete guide for authoring ComponentResource classes. The skill covers designing component interfaces, multi-language support, and distribution. It teaches assistants how to build reusable infrastructure abstractions that work across TypeScript, Python, Go, C#, Java, and YAML.

**Pulumi Automation API** covers programmatic orchestration of Pulumi operations. The skill explains when to use Automation API versus the CLI, the tradeoffs between local source and inline programs, and patterns for multi-stack deployments.

**Pulumi ESC** covers centralized secrets and configuration management. The skill guides assistants through setting up dynamic OIDC credentials, composing environments, and integrating secrets into Pulumi programs and other applications.

## How to install

### Claude Code Plugin Marketplace

For Claude Code users, the plugin system provides the simplest installation experience:

```bash
/plugin marketplace add pulumi/agent-skills
/plugin install pulumi-migration     # Install migration skills
/plugin install pulumi-authoring     # Install authoring skills
```

You can install both plugin groups or choose only the ones you need.

### Universal installation

For Cursor, GitHub Copilot, VS Code, Codex, Gemini and other platforms, use the universal [Agent Skills](https://agentskills.io) CLI:

```bash
npx skills add pulumi/agent-skills
```

This works across all platforms that support the Agent Skills specification.

## Using skills

Once installed, skills activate automatically based on context. When you ask your assistant to help migrate a Terraform project, it draws on the Terraform skill's workflow. When you are debugging why resources are being recreated unexpectedly, the best practices skill helps the assistant check for missing aliases.

In Claude Code and Codex, you can invoke skills directly via slash commands:

```text
/pulumi-terraform-to-pulumi
```

Or describe what you need in natural language:

> "Help me migrate this CDK application to Pulumi"

> "Review this Pulumi code for best practices issues"

> "Create a reusable component for a web service with load balancer"

The assistant will follow the skill's procedures, ask clarifying questions when needed, and produce output that reflects Pulumi best practices rather than generic code generation.

## Get started

We expect this collection to grow. If you have Pulumi expertise worth packaging, whether provider-specific patterns, debugging workflows, or operational practices, we welcome contributions. See the [contributing guide](https://github.com/pulumi/agent-skills/blob/main/CONTRIBUTING.md) for details.

The skills are available now at [github.com/pulumi/agent-skills](https://github.com/pulumi/agent-skills). Install them in your preferred AI coding environment and let us know what you build.
