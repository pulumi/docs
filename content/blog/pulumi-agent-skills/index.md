---
title: "Pulumi Agent Skills"
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
schema_type: auto

social:
    twitter: |
        Introducing Pulumi Agent Skills:

        - Migration workflows: Terraform, CDK, ARM to Pulumi
        - Best practices: Catch common mistakes before deploy
        - Pulumi ESC: OIDC and secrets done right

        Works with Claude Code, Cursor, Copilot, and more.

        Install: npx add-skill pulumi/agent-skills
    linkedin: |
        **Pulumi Agent Skills: Teaching AI Assistants How Experts Write Infrastructure**

        AI coding assistants generate infrastructure code that works but often misses what matters. The gap is not intelligence, it is expertise.

        **The Problem**
        General-purpose agents lack the domain knowledge that experienced Pulumi developers accumulate. They do not know that creating resources inside apply() breaks preview. They have not internalized the workflow differences between converting Terraform state versus just translating HCL syntax.

        **The Solution**
        Pulumi Agent Skills packages this expertise into structured knowledge that works across Claude Code, Cursor, GitHub Copilot, VS Code, Codex, and Gemini.

        **What You Get**
        - Migration skills: Complete Terraform, CDK, and ARM migration workflows, not just syntax translation
        - Best practices: Automatic detection of common mistakes like resources in apply(), missing aliases, improper secret handling
        - Pulumi ESC: OIDC setup, environment composition, and credential management patterns
        - Automation API: Multi-stack orchestration, self-service platforms, and embedded infrastructure patterns

        **One Command to Install**
        npx add-skill pulumi/agent-skills

        Read more: pulumi.com/blog/pulumi-agent-skills
---

AI coding assistants have transformed how developers write software, including infrastructure code. Tools like Claude Code, Cursor, and GitHub Copilot can generate code, explain complex systems, and automate tedious tasks. But when it comes to infrastructure, these tools often produce code that works but misses the mark on patterns that matter: proper secret handling, correct resource dependencies, idiomatic component structure, and the dozens of other details that separate working infrastructure from production-ready infrastructure.

<!--more-->

That's because general-purpose agents lack the domain knowledge that experienced IaC developers build up over time. Pulumi developers know, for example, that creating resources inside `apply()` means those resources will not appear in preview. They do not know the specific flags needed to import an existing Azure resource. They have not internalized the workflow differences between converting Terraform state versus just translating HCL syntax.

We built [Neo](https://www.pulumi.com/product/neo/) for teams that want deep Pulumi expertise combined with organizational context and deployment governance. But developers have preferred tools, and we want people to succeed with Pulumi wherever they work. Some teams live in Claude Code. Others use Cursor, Copilot, Codex, or Gemini. That is why we are releasing Pulumi Agent Skills, a collection of packaged expertise that teaches any AI coding assistant how to work with Pulumi the way an experienced practitioner would.

## What are agent skills?

Skills are structured knowledge packages that follow the open [Agent Skills](https://agentskills.io) specification. They work across multiple AI coding platforms including Claude Code, GitHub Copilot, Cursor, VS Code, Codex, and Gemini. When you install Pulumi skills, your AI assistant gains access to detailed workflows, code patterns, and decision trees for common infrastructure tasks.

## Available Pulumi skills

We are launching with skills covering two areas: migration workflows and Pulumi capabilities.

### Migration skills

These skills help AI assistants guide you through complete migrations, not just syntax translation.

* **Terraform to Pulumi** walks through the full migration workflow. It handles state translation, provider version alignment, and the iterative process of achieving a clean `pulumi preview` with no unexpected changes.

* **CDK to Pulumi** covers AWS CDK migrations in depth. The skill includes strategies for handling CDK's Lambda-backed custom resources, asset bundling, cross-stack references, and the decision framework for when to use `aws-native` versus `aws` providers.

* **CloudFormation to Pulumi** guides assistants through converting CloudFormation templates and importing existing stacks into Pulumi management.

* **ARM to Pulumi** handles Azure Resource Manager and Bicep template conversion, including the import workflow for bringing existing Azure resources under Pulumi management.

### Capability skills

These skills teach assistants how to use Pulumi features effectively.

**Pulumi ESC** covers Environments, Secrets, and Configuration. The skill explains when to use `esc env get` versus `esc env open`, how to set up OIDC credentials for AWS, Azure, and GCP, and the patterns for composing environments across teams and stacks.

**Pulumi best practices** encodes the patterns that prevent common mistakes. It covers output handling (never create resources inside `apply()`), component structure (always set `parent: this`), secrets management (encrypt from day one), safe refactoring with aliases, and deployment workflows. The skill flags anti-patterns like resources created inside `apply()` callbacks, missing parent relationships in components, and unencrypted secrets in stack configuration.

**Pulumi Automation API** covers programmatic orchestration of Pulumi operations. The skill explains when to use Automation API versus the CLI, the tradeoffs between local source and inline programs, and patterns for multi-stack deployments. It guides assistants through building self-service platforms, replacing fragile shell scripts, and embedding infrastructure provisioning in applications.

## Example: best practices in action

When you ask an assistant with the best practices skill to review code, it catches issues that generic agents miss. Consider this common mistake:

```typescript
const bucket = new aws.s3.Bucket("bucket");

bucket.id.apply(bucketId => {
    new aws.s3.BucketObject("object", {
        bucket: bucketId,
        content: "hello",
    });
});
```

A general-purpose agent might not flag this. An agent with the Pulumi best practices skill recognizes that creating resources inside `apply()` means they will not appear in `pulumi preview`, and suggests the correct pattern:

```typescript
const bucket = new aws.s3.Bucket("bucket");

const object = new aws.s3.BucketObject("object", {
    bucket: bucket.id,  // Pass the Output directly
    content: "hello",
});
```

The skill teaches the assistant why this matters: resources created inside `apply()` may not appear in preview, making deployments unpredictable and breaking the dependency graph that Pulumi uses to order operations correctly.

## How to install

The quickest way to install is with the [add-skill](https://add-skill.org/) CLI:

```bash
npx add-skill pulumi/agent-skills
```

This works across Claude Code, Cursor, GitHub Copilot, VS Code, Codex, Gemini, and other platforms that support the Agent Skills specification.

### Manual installation

You can also install manually for specific platforms:

**Claude Code**: Clone to your skills directory (`~/.claude/skills/` for global, or `.claude/skills/` for a project):

```bash
# Global (available across all projects)
git clone https://github.com/pulumi/agent-skills.git ~/.claude/skills/pulumi

# Project-specific
git clone https://github.com/pulumi/agent-skills.git .claude/skills/pulumi
```

**Cursor**: Add to your project's `.cursor/skills/` directory:

```bash
git clone https://github.com/pulumi/agent-skills.git .cursor/skills/pulumi
```

**GitHub Copilot / VS Code**: Clone to your skills directory:

```bash
git clone https://github.com/pulumi/agent-skills.git .github/skills/pulumi
```

**Codex**: Add to your project's `.codex/skills/` directory:

```bash
git clone https://github.com/pulumi/agent-skills.git .codex/skills/pulumi
```

**Gemini**: Add to your project's `.gemini/skills/` directory:

```bash
git clone https://github.com/pulumi/agent-skills.git .gemini/skills/pulumi
```

## Using skills

Once installed, skills activate automatically based on context. When you ask your assistant to help migrate a Terraform project, it draws on the Terraform skill's workflow. When you are debugging why resources are being recreated unexpectedly, the best practices skill helps the assistant check for missing aliases.

In Claude Code and Codex, you can invoke skills directly via slash commands:

```text
/pulumi-terraform-to-pulumi
```

Or describe what you need in natural language:

> "Help me migrate this CDK application to Pulumi"

> "Review this Pulumi code for best practices issues"

The assistant will follow the skill's procedures, ask clarifying questions when needed, and produce output that reflects accumulated Pulumi expertise rather than generic code generation.

We expect this collection to grow. If you have Pulumi expertise worth packaging, whether provider-specific patterns, debugging workflows, or operational practices, we welcome contributions. See the [contributing guide](https://github.com/pulumi/agent-skills/blob/main/CONTRIBUTING.md) for details.

## Get started

The skills are available now at [github.com/pulumi/agent-skills](https://github.com/pulumi/agent-skills). Install them in your preferred AI coding environment and let us know what you build.

{{< github-card repo="pulumi/agent-skills" >}}
