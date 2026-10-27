---
title: MCP server tools
title_tag: Pulumi MCP server tools and prompts
h1: Pulumi MCP server tools and prompts
meta_desc: Reference for the tools and prompts the Pulumi MCP server exposes to AI agents, covering Pulumi Cloud, Neo, the Pulumi Registry, and code generation.
menu:
    ai:
        name: MCP server tools
        parent: ai-reference
        identifier: ai-reference-mcp-server-tools
        weight: 10
---

The [Pulumi MCP server](/docs/ai/guides/set-up-mcp-server/) exposes the following tools and prompts to your agent. For what each tool needs from your organization and what it can cost, see [Costs and edition requirements](/docs/ai/guides/set-up-mcp-server/#costs-and-edition-requirements).

## Tools

You don't call these tools directly: describe what you want and your agent picks the tool. The names matter when your agent asks you to approve a tool call and when you allow or deny tools in its settings.

### Pulumi Cloud

| Tool | Description |
|---|---|
| `get-stacks` | List the stacks in your organization. |
| `resource-search` | Search resources across all stacks using [resource search queries](/docs/discovery-governance/concepts/discovery/querying-resources/), such as `package:aws` or `-.tags:` (resources without tags). |
| `get-policy-violations` | List [policy as code](/docs/discovery-governance/concepts/policy-as-code/) violations for your stacks. |
| `get-users` | List the members of your organization and their roles. |

### Neo

| Tool | Description |
|---|---|
| `neo-bridge` | Start a Neo task, send it follow-up messages, and approve or reject its requests. Returns a link to the task in the Pulumi Cloud console. |
| `neo-get-tasks` | List your organization's Neo tasks and their status. |
| `neo-continue-task` | Check the status of an existing task and read its latest events. |
| `neo-reset-conversation` | Clear the server's tracked state for a task, or for all tasks. |

### Pulumi Registry

| Tool | Description |
|---|---|
| `list-resources` | List the resource types in a provider or module. |
| `list-functions` | List the functions in a provider or module. |
| `get-resource` | Get a resource's properties and documentation. |
| `get-function` | Get a function's inputs, outputs, and documentation. |
| `get-type` | Get the JSON schema for a type reference. |

### Code generation

| Tool | Description |
|---|---|
| `deploy-to-aws` | Return step-by-step instructions the agent follows to analyze your application and write Pulumi code that deploys it to AWS. |

## Prompts

Prompts are reusable instructions your agent can load, usually from a slash-command or prompt menu:

- `deploy-to-aws`: deploy application code to AWS by generating a Pulumi program.
- `convert-terraform-to-typescript`: convert Terraform HCL to a Pulumi TypeScript program.
- `cdk-migration-plan`: plan a migration from the AWS CDK to Pulumi.
- `cdk-migration-automated`: migrate a CDK app to Pulumi with automated conversion.
- `cdk-migration-manual`: migrate a CDK app to Pulumi by hand.
- `cdk-migration-troubleshoot`: troubleshoot a CDK-to-Pulumi migration.
