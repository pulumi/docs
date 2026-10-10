---
title_tag: "Pulumi MCP Server | AI-Assisted Infrastructure as Code"
meta_desc: "Connect Claude Code, Cursor, Windsurf, and other AI agents to Pulumi Cloud and the Pulumi Registry with Pulumi's hosted Model Context Protocol (MCP) server."
title: MCP server
h1: Pulumi Model Context Protocol server
menu:
    ai:
        name: MCP server
        parent: ai-home
        weight: 8
aliases:
- /docs/iac/using-pulumi/mcp-server/
- /docs/iac/guides/mcp-server.md
- /docs/iac/using-pulumi/mcp-server/index/
- /docs/iac/guides/ai-integration/mcp-server/
---

The Pulumi [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server gives the AI agent you already use access to Pulumi. Through it, an agent can list your stacks, search your resources, check policy violations, look up resource schemas in the Pulumi Registry, and hand tasks to [Pulumi Neo](/docs/ai/neo/). For background on MCP in infrastructure work, see [MCP for infrastructure as code](/what-is/mcp-for-infrastructure-as-code/).

Pulumi hosts the server at `https://mcp.ai.pulumi.com/mcp`, so there is nothing to install or run locally.

> [!INFO]
> This page is about connecting your own AI agent to Pulumi. For the opposite direction, connecting Neo to other services' MCP servers (Jira, Datadog, and others), see [External MCP servers](/docs/ai/neo/integrations/mcp/).

## Configuration

Add the server to your agent, then authenticate with a Pulumi access token the first time the agent connects. See [Authentication](#authentication) for what the token is used for and how to choose an organization.

### Claude Code

```bash
claude mcp add --transport http pulumi https://mcp.ai.pulumi.com/mcp
```

Then run `/mcp` in Claude Code, select **pulumi**, and authenticate in the browser window that opens.

### Cursor

[![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](cursor://anysphere.cursor-deeplink/mcp/install?name=pulumi&config=eyJ0cmFuc3BvcnQiOiJodHRwIiwidXJsIjoiaHR0cHM6Ly9tY3AuYWkucHVsdW1pLmNvbS9tY3AifQ%3D%3D)

Or add the server to `.cursor/mcp.json` in your home directory or project root:

```json
{
  "mcpServers": {
    "pulumi": {
      "url": "https://mcp.ai.pulumi.com/mcp"
    }
  }
}
```

Then select **Connect** next to the server under **Cursor Settings > Tools & MCP** and authenticate in the browser.

### Claude Desktop

1. Open **Settings > Connectors** and select **Add custom connector**.
1. Set the name to `Pulumi` and the URL to `https://mcp.ai.pulumi.com/mcp`.
1. Restart Claude Desktop and authenticate in the browser when prompted.

### Windsurf

Add the server to Windsurf's MCP configuration (**Windsurf Settings > MCP Servers**), then authenticate in the browser when prompted:

```json
{
  "mcpServers": {
    "pulumi": {
      "serverUrl": "https://mcp.ai.pulumi.com/mcp"
    }
  }
}
```

### Kiro

Kiro connects to remote MCP servers through the [mcp-remote](https://www.npmjs.com/package/mcp-remote) package, which requires Node.js. Add the server to Kiro's [`mcp.json`](https://kiro.dev/docs/mcp/configuration/#configuration-locations), then authenticate in the browser when prompted:

```json
{
  "mcpServers": {
    "pulumi": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.ai.pulumi.com/mcp"]
    }
  }
}
```

### Other agents

Any agent that supports remote MCP servers over streamable HTTP with OAuth can connect to `https://mcp.ai.pulumi.com/mcp`. Agents that only support local (stdio) servers can use `mcp-remote` as shown for Kiro.

## Authentication

The MCP server calls Pulumi Cloud with a Pulumi [access token](/docs/administration/concepts/access-tokens/) that you provide. Every call runs as that token's identity, so the agent can see and do exactly what the token can, under your organization's [RBAC](/docs/administration/concepts/rbac/) settings, and nothing more. See [Choose a token](#choose-a-token) for which kind to use.

### Authenticate in the browser

The first time your agent connects, it opens a browser window:

1. Paste a Pulumi access token.
1. Select the organization the server should use by default.
1. Confirm the redirect URL and select **Authorize Connection**.
1. Return to your agent.

The server stores the token encrypted and uses it for every call until the session ends. Sessions last 30 days, after which the agent asks you to authenticate again. If you delete the token, or it expires, before then, tool calls fail until you authenticate again with a new token. To switch the default organization, disconnect and reconnect the server in your agent and choose a different organization. You can also name an organization in a request ("list the stacks in the acme org") and the agent passes it to the tool.

### Choose a token

The token you give the MCP server is separate from the one the Pulumi CLI uses (stored by `pulumi login` or set in `PULUMI_ACCESS_TOKEN`), so create a separate one for the MCP server. You can then revoke or rotate it without affecting the CLI. The server accepts any Pulumi access token, but two kinds are most useful:

- **An [organization token](/docs/administration/concepts/access-tokens/#creating-an-organization-access-token)** acts as the organization with whatever [role](/docs/administration/concepts/rbac/roles/) you assign it, and works in a single organization. This is the way to limit what the agent can see and do in Pulumi Cloud, for example by assigning a role that can only read stacks. Don't rely on the token's role to block [Neo tasks](#costs-and-edition-requirements), though: deny `neo-bridge` in your agent as well if you want the agent to be read-only. Organization tokens are available in {{< pulumi-cloud-editions "org-team-access-tokens" >}}.
- **A [personal access token](/docs/administration/concepts/access-tokens/#personal-access-tokens)** acts as you, with your permissions in every organization you belong to. Create one at [app.pulumi.com/account/tokens](https://app.pulumi.com/account/tokens).

If your organization enforces an [access token expiry policy](/docs/administration/concepts/access-tokens/#access-token-expiry-policy), the token must meet it, or calls against that organization fail.

### Authenticate without a browser

For CI pipelines and headless agents, skip the browser flow by sending the token in an `Authorization` header. The server validates the token on every request and stores nothing, so there is no session to expire. Add an `X-Pulumi-Org` header to choose the organization:

```json
{
  "mcpServers": {
    "pulumi": {
      "url": "https://mcp.ai.pulumi.com/mcp",
      "headers": {
        "Authorization": "Bearer ${PULUMI_MCP_TOKEN}",
        "X-Pulumi-Org": "acme"
      }
    }
  }
}
```

Read the token from an environment variable or secret store rather than committing it, and check how your agent expands variables in its MCP configuration.

> [!WARNING]
> If `X-Pulumi-Org` names an organization the token can't access, or you omit the header, the server uses the first organization the token can access, without returning an error. Check the organization name carefully when using a personal token that belongs to more than one organization.

## Costs and edition requirements

Most of the server's tools only read data, and the server itself never runs `pulumi up` or changes your infrastructure. What the tools need from your organization:

| Tools | What they need | Cost |
|---|---|---|
| Registry tools, `deploy-to-aws`, and all prompts | Any Pulumi account | None. They return schemas and instructions that your agent's own model works with. |
| `get-stacks`, `get-users`, `get-policy-violations` | Any Pulumi Cloud organization | None |
| `resource-search` | [Resource search](/docs/discovery-governance/concepts/discovery/querying-resources/), available in {{< pulumi-cloud-editions "resource-search" >}} | Included in your edition |
| `neo-bridge` | [Pulumi Neo](/docs/ai/neo/), available in {{< pulumi-cloud-editions "neo-integrations" >}} | Neo usage is billed to your organization |

`neo-bridge` is the tool that can cost money. Each task it starts, and each message or approval it sends, runs Neo in Pulumi Cloud, which counts against your organization's Neo usage as it would in the Pulumi Cloud console. Approving a Neo request can also let Neo change infrastructure or open pull requests. Admins can cap that spend with [Neo usage limits](/docs/ai/neo/usage-limits/); see [pricing](/pricing/) for rates.

To keep an agent from starting Neo work, deny `neo-bridge` in your agent's tool permissions. Restricting the token's role isn't enough on its own to prevent Neo tasks. In Claude Code, add `mcp__pulumi__neo-bridge` to `permissions.deny` in `settings.json`; in Cursor, turn the tool off under **Tools & MCP**.

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

## Example requests

- "What stacks do I have, and which ones haven't been updated in the last 90 days?"
- "Find every S3 bucket without tags and tell me which stacks they're in."
- "Look up the properties for an Azure Container Registry with geo-replication and write the TypeScript for it."
- "What policy violations do my production stacks have?"
- "Ask Neo to restrict every security group that allows SSH from 0.0.0.0/0 and open a pull request."

## Troubleshooting

**The token is rejected.** Check that the token hasn't expired or been deleted at [app.pulumi.com/account/tokens](https://app.pulumi.com/account/tokens), and that it complies with your organization's token expiry policy.

**The agent sees the wrong organization.** Reconnect the server and pick the right organization, or name the organization in your request. With header authentication, check the spelling of `X-Pulumi-Org`.

**The agent asks you to authenticate again.** Browser sessions last 30 days. Authenticate again to start a new session.

**New or renamed tools don't appear.** Some agents, including Cursor, cache tool definitions. Restart the agent or reconnect the server.

**A tool reports "Quota limit exceeded" or "Forbidden".** A quota error usually means the feature isn't available in your organization's edition; see [Costs and edition requirements](#costs-and-edition-requirements). "Forbidden" means the token's role lacks permission; see [Choose a token](#choose-a-token).

**Neo tasks don't start.** Check that Neo is enabled for your organization and that it hasn't reached its [usage limit](/docs/ai/neo/usage-limits/).

## Next steps

- [Pulumi Agent Skills](/docs/ai/skills/): teach your agent proven Pulumi workflows.
- [Pulumi Neo](/docs/ai/neo/): Pulumi's infrastructure agent.
- [Agent accounts](/docs/administration/concepts/agent-accounts/): Pulumi Cloud accounts that agents provision for themselves.
- [Access tokens](/docs/administration/concepts/access-tokens/): personal, organization, and team tokens.
- [What is agentic infrastructure?](/what-is/what-is-agentic-infrastructure/)
