---
title: "Announcing Pulumi Remote MCP Server"
date: 2025-10-07T20:00:00-05:00
draft: false
meta_desc: Announcing Pulumi Remote MCP Server with new tools and integration with Pulumi Neo
meta_image: meta.png
authors:
    - artur-laksberg
tags:
    - MCP
    - ai

---

We're excited to announce the Pulumi Remote MCP Server—a hosted service that brings AI-powered infrastructure management to any AI assistant that supports the [Model Context Protocol](https://modelcontextprotocol.io). Connect your favorite AI assistant to `https://mcp.ai.pulumi.com/mcp` and instantly access your Pulumi Cloud infrastructure, search resources across stacks, and delegate complex automation tasks to [Pulumi Neo](/docs/pulumi-cloud/neo/).

<!--more-->

## The Evolution of Pulumi MCP

Earlier this year, we [launched the Pulumi MCP server](https://www.pulumi.com/blog/mcp-server-ai-assistants/) as a local npm package that brought AI-assisted infrastructure management to developers' machines. The adoption and feedback from users and partners has been positive, validating the power of combining AI assistants with infrastructure-as-code.

As the MCP ecosystem has matured and more organizations have adopted the protocol, a clear pattern has emerged: remote MCP servers are becoming the industry standard. Remote servers provide a key advantage—**accessibility**. One endpoint works everywhere, with no per-machine setup.

Following industry trends and feedback from users and partners, we're introducing the Remote MCP Server to ease installation and version management. The remote server preserves everything developers love about the local version while adding powerful new capabilities like seamless Pulumi Neo integration.

> **Note:** The local MCP server continues to be available and fully supported for developers who prefer local tooling or need offline capabilities.

## Why Remote MCP?

The Pulumi Remote MCP Server runs as a hosted service. Instead of managing local installations, you configure it once and get automatic updates and consistent functionality across all your development environments.

### Zero local setup, universal access

Instead of installing npm packages, you simply configure your AI assistant with a single URL: `https://mcp.ai.pulumi.com/mcp`. That's it.

- **No per-machine installations** - Works the same on your laptop, desktop, or cloud workstation
- **No manual updates** - New features and improvements roll out automatically to all users
- **Works with any MCP-compatible AI assistant** - Cursor, Claude Code, Windsurf, Claude Desktop, and more

For instructions on how to configure different AI assistants, see [Pulumi MCP Server](/docs/iac/using-pulumi/mcp-server).

### Centralized authentication & secrets

Remote MCP also solves a critical security challenge: credential management. Instead of scattering Pulumi Access Tokens across laptops, containers, and scripts, the Remote MCP Server uses OAuth-based authentication with your Pulumi Cloud organization.

When you first connect, a browser window opens where you:

1. Enter your Pulumi Access Token (which is validated server-side)
2. Select which organization to access
3. Return to your AI assistant - now authenticated

Your credentials are stored securely in Pulumi Cloud, not on your individual machine.

## What Can You Do With It?

The Remote MCP Server is your AI assistant's gateway to your entire Pulumi infrastructure. It combines real-time access to your cloud resources with the power of autonomous infrastructure automation through Pulumi Neo.

### Discover and query infrastructure

Your AI assistant can instantly explore what you've deployed across your entire organization:

**Inventory your resources:**

- List all stacks in your organization with `get-stacks`
- Search for specific resources across all stacks using `resource-search`
- Find resources by type, name, tags, or any property: `type:aws:s3/bucket:Bucket AND acl:public-read`

**Audit and compliance:**

- Check for policy violations with `get-policy-violations`
- View organization members and their roles with `get-users`
- Identify security gaps, untagged resources, or misconfigured infrastructure

Ask questions like:

- "Show me all RDS databases without encryption enabled"
- "Which stacks have resources in us-east-1?"
- "Find all Lambda functions using deprecated runtimes"

### Generate infrastructure code

The MCP server connects directly to the [Pulumi Registry](https://www.pulumi.com/registry/), giving your AI assistant access to thousands of cloud resources with complete type information:

**Registry-powered code generation:**

- Browse available resources with `list-resources` and `list-functions`
- Get detailed schemas with `get-resource` and `get-type`
- Access property documentation, input/output types, and examples

Your AI assistant can:

- Look up the exact properties for any cloud resource
- Generate type-safe infrastructure code in TypeScript, Python, Go, or any Pulumi language
- Include proper configurations, security settings, and best practices
- Reference real documentation and examples

This means code generation is more accurate and up-to-date with the latest provider versions.

### Autonomous infrastructure with Pulumi Neo

This is where the Remote MCP Server truly shines. For complex infrastructure tasks that require multiple steps, code changes, testing, and pull requests, your AI assistant can delegate directly to [Pulumi Neo](https://www.pulumi.com/docs/pulumi-cloud/neo/)—Pulumi's autonomous infrastructure AI agent.

**What makes Neo special:**

Neo isn't just an AI that writes code—it's an AI that *ships* infrastructure changes autonomously:

- **Multi-step planning** - Neo breaks down complex requests into actionable plans
- **Code generation at scale** - Works across multiple stacks and repositories
- **Automated testing** - Validates changes before creating pull requests
- **Pull request workflows** - Creates PRs with detailed explanations and comments
- **Continuous execution** - Runs in Pulumi Cloud, not blocking your AI assistant
- **Human-in-the-loop** - Pauses for approval on critical changes

**Real-world Neo examples:**

Security remediation:
**"Ask Neo to find all security groups allowing SSH from 0.0.0.0/0 and create a PR restricting them to my office IP"**

Neo will:

1. Search your infrastructure for overly permissive security groups
2. Create a detailed plan for restricting access
3. Generate infrastructure code changes
4. Create a pull request with explanations
5. Wait for your approval to merge

Runtime migrations:
**"Ask Neo to migrate all Lambda functions from Python 3.8 to Python 3.12 and create PRs for each affected stack"**

Neo handles:

- Finding all Lambda functions with Python 3.8
- Checking for compatibility issues
- Updating runtime configurations
- Running tests to ensure functionality
- Creating separate PRs per stack for easy review

Policy compliance:
**"Ask Neo to scan for policy violations and fix them automatically"**

Neo will:

- Identify violations across all stacks
- Generate fixes following your policy rules
- Test changes to ensure compliance
- Create PRs with clear explanations of what was fixed and why

Cost optimization:
**"Ask Neo to find idle resources and create a plan to shut them down"**

Neo analyzes usage patterns, identifies waste, and proposes infrastructure changes to reduce costs—all autonomously.

The key difference: your AI assistant identifies *what* needs to be done, and Neo *does* it—writing code, running tests, creating PRs, and managing the entire workflow in Pulumi Cloud.

## Real-World Workflow

Here's what a typical session looks like:

**You:** "What stacks do I have with 'production' in the name?"

**AI Assistant:** Uses `get-stacks` to list: `api-production`, `web-production`, `data-production`

**You:** "Are there any policy violations in those stacks?"

**AI Assistant:** Uses `get-policy-violations` and reports: 3 S3 buckets without encryption, 2 security groups too permissive

**You:** "Ask Neo to fix those violations and create a PR"

**AI Assistant:** Uses `neo-bridge` to launch Neo task, provides link

**Neo:** Autonomously creates plan, generates fixes, tests changes, creates PR with detailed explanation

**You:** Review PR, approve, merge

## Getting Started

Ready to try it? Check out our [documentation](/docs/iac/using-pulumi/mcp-server/) for configuration instructions for your AI assistant of choice.

Key points:

1. **Configure once** - Add `https://mcp.ai.pulumi.com/mcp` to your AI assistant's MCP settings
2. **Authenticate** - Browser popup for token entry and org selection (one time)
3. **Start asking** - Query your infrastructure, generate code, delegate to Neo

The Remote MCP Server is available now for all Pulumi users. No installation required—just configure and connect.

## Learn More

- [Pulumi MCP Server Documentation](/docs/iac/using-pulumi/mcp-server/)
- [Pulumi Neo Documentation](/docs/pulumi-cloud/neo/)
- [Model Context Protocol](https://modelcontextprotocol.io)

We're excited to see what you build with AI-assisted infrastructure management. Let us know what you think in our [Community Slack](https://slack.pulumi.com)!
