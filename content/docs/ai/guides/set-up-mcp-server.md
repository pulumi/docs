---
title_tag: "Pulumi MCP Server | AI-Assisted Infrastructure as Code"
meta_desc: "Connect Claude Code, Cursor, Windsurf, and other AI agents to Pulumi Cloud and the Pulumi Registry with Pulumi's hosted Model Context Protocol (MCP) server."
title: MCP server
h1: Pulumi Model Context Protocol server
menu:
    ai:
        name: Connect the MCP server
        parent: ai-coding-agents
        weight: 20
aliases:
- /docs/iac/using-pulumi/mcp-server/
- /docs/iac/guides/mcp-server.md
- /docs/iac/using-pulumi/mcp-server/index/
- /docs/iac/guides/ai-integration/mcp-server/
- /docs/ai/mcp-server/
---

<script>
// Redirect anchors whose content moved to the MCP server tools reference.
(function() {
  var refAnchors = ['tools', 'pulumi-cloud', 'neo', 'pulumi-registry', 'code-generation', 'prompts'];
  var anchor = window.location.hash.replace(/^#/, '');
  if (anchor && refAnchors.indexOf(anchor) !== -1) {
    window.location.replace('/docs/ai/reference/mcp-server-tools/#' + anchor);
  }
})();
</script>

Connect your coding agent to the Pulumi [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server to query stacks, search resources, read policy results, and look up provider schemas in the Pulumi Registry. For task tools, access controls, and billing, see [Costs and edition requirements](#costs-and-edition-requirements).

Pulumi hosts the server at `https://mcp.ai.pulumi.com/mcp`. Your coding agent must support remote MCP connections or use a local adapter.

> [!INFO]
> This page is about connecting your own AI agent to Pulumi. To connect Pulumi Agents to other services' MCP servers, such as Jira or Datadog, see [External MCP servers](/docs/ai/integrations/external-mcp-servers/).

## Configuration

Follow the instructions for your coding agent, then complete [Authentication](#authentication).

### Claude Code

```bash
claude mcp add --transport http pulumi https://mcp.ai.pulumi.com/mcp
```

Then run `/mcp` in Claude Code, select **pulumi**, and authenticate in the browser window that opens.

### Codex

Register the Pulumi server from your terminal:

```bash
codex mcp add pulumi --url https://mcp.ai.pulumi.com/mcp
```

If Codex prompts you to sign in, complete the browser flow. To start sign-in manually, run `codex mcp login pulumi`.

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

The MCP server authenticates Pulumi Cloud API requests with the [access token](/docs/administration/concepts/access-tokens/) you provide. Pulumi Cloud checks access to the requested resources. Choose a token that can read the stacks and resources you want to query. Your coding agent's tool settings separately control which MCP tools it can call.

### Authenticate in the browser

The first time your agent connects, it opens a browser window:

1. Paste a Pulumi access token.
1. Select the organization the server should use by default.
1. Confirm the redirect URL and select **Authorize Connection**.
1. Return to your agent.

The server stores the token encrypted and uses it for tool calls during the session. Sessions last 30 days. If the session or token expires, authenticate again; use a new token if the old one has expired or been deleted.

To switch the default organization, disconnect and reconnect the server in your agent and choose a different organization. You can also name an organization in a request, such as "list the stacks in the acme org".

### Choose a token

Create a separate token for the MCP server so you can revoke or rotate it without affecting the Pulumi CLI's token. The server accepts any Pulumi access token, but two kinds are most useful:

- **An [organization token](/docs/administration/concepts/access-tokens/#creating-an-organization-access-token)** acts as the organization with whatever [role](/docs/administration/concepts/rbac/roles/) you assign it, and works in a single organization. Assign a role that can read the stacks and resources you need. Organization tokens are available in {{< pulumi-cloud-editions "org-team-access-tokens" >}}.
- **A [user access token](/docs/administration/concepts/access-tokens/#personal-access-tokens)** acts as you, with your permissions in every organization you belong to. Create one at [app.pulumi.com/account/tokens](https://app.pulumi.com/account/tokens).

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
> If `X-Pulumi-Org` names an organization the token can't access, or you omit the header, the server uses the first organization the token can access, without returning an error. Check the organization name carefully when using a user token that belongs to more than one organization.

## Verify the connection

Ask your coding agent to list the stacks in your organization, naming the organization in the request. Check that the response lists stacks you recognize in that organization. If the tool fails or returns the wrong organization, see [Troubleshooting](#troubleshooting).

## Costs and edition requirements

Most MCP tools return data or instructions for your coding agent to use. The `neo-bridge` tool delegates work to Pulumi Agents: it can create a task, send follow-up messages, and approve or reject the task's requests.

| Tools | What they need | Cost |
|---|---|---|
| Registry tools, `deploy-to-aws`, and all prompts | Any Pulumi account | None. They return schemas and instructions that your agent's own model works with. |
| `get-stacks`, `get-users`, `get-policy-violations` | Any Pulumi Cloud organization | None |
| `resource-search` | [Resource search](/docs/discovery-governance/concepts/discovery/querying-resources/), available in {{< pulumi-cloud-editions "resource-search" >}} | Included in your edition |
| `neo-bridge` | Neo tasks with [Pulumi Agents](/docs/ai/agents/), available in {{< pulumi-cloud-editions "neo-integrations" >}} | Task usage is billed to your organization |

Follow-up messages and approvals sent through `neo-bridge` can continue a task's work and incur further usage. Review the requested action before approving it. Admins can configure [usage limits](/docs/ai/concepts/neo/usage-limits/); see that guide for the charges those limits cover.

To use the server for queries without task creation, messages, or approvals, disable `neo-bridge` in your coding agent's tool permissions. In Claude Code, add `mcp__pulumi__neo-bridge` to `permissions.deny` in `settings.json`; in Cursor, turn the tool off under **Tools & MCP**.

<span id="tools-and-prompts"></span>
<span id="example-requests"></span>

See [MCP server tools and prompts](/docs/ai/reference/mcp-server-tools/) for the full list of tools and prompts.

## Troubleshooting

**The token is rejected.** Check that the token hasn't expired or been deleted at [app.pulumi.com/account/tokens](https://app.pulumi.com/account/tokens), and that it complies with your organization's token expiry policy.

**The agent sees the wrong organization.** Reconnect the server and pick the right organization, or name the organization in your request. With header authentication, check the spelling of `X-Pulumi-Org`.

**The agent asks you to authenticate again.** Browser sessions last 30 days. Authenticate again to start a new session.

**New or renamed tools don't appear.** Some agents, including Cursor, cache tool definitions. Restart the agent or reconnect the server.

**A tool reports "Quota limit exceeded" or "Forbidden".** A quota error usually means the feature isn't available in your organization's edition; see [Costs and edition requirements](#costs-and-edition-requirements). "Forbidden" can mean the token's role lacks permission or the requested feature is disabled. See [Choose a token](#choose-a-token) and the task checks below.

**A request to `neo-bridge` does not create a task.** Ask an administrator to check that **Enable AI features for this organization** and **Enable Pulumi Agents** are both on in [organization AI settings](/docs/ai/concepts/neo/settings/#enable-neo-for-organization). Also check that the organization has not reached its [usage limit](/docs/ai/concepts/neo/usage-limits/).

<span id="next-steps"></span>
