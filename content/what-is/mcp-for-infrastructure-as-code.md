---
title: MCP for Infrastructure as Code: What It Means for Pulumi Users
meta_desc: MCP connects AI agents to your cloud infrastructure. Learn what the Model Context Protocol is and how Pulumi users connect IaC to MCP agents today.
type: what-is
page_title: "MCP for Infrastructure as Code: What It Means for Pulumi Users"
schema_type: howto
authors: ["alex-leventer"]
---

The Model Context Protocol (MCP) is an open standard that lets AI agents connect to external tools and data through one consistent interface instead of a custom integration per app. For Pulumi users, MCP means an agent can inspect your cloud state, generate infrastructure code in TypeScript or Python, run a preview, and delegate work to Neo, all from inside your editor.

## What is the Model Context Protocol (MCP)?

MCP is an open-source standard, originally created and open-sourced by Anthropic in November 2024, for connecting AI applications to external systems. As of December 2025, governance of the specification was donated to the [Agentic AI Foundation](https://www.linuxfoundation.org/), a directed fund under the Linux Foundation, so the protocol continues to evolve under neutral, vendor-independent stewardship rather than staying tied to any single company.

The [official MCP documentation](https://modelcontextprotocol.io/introduction) describes it this way:

> "MCP (Model Context Protocol) is an open-source standard for connecting AI applications to external systems... Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect electronic devices, MCP provides a standardized way to connect AI applications to external systems."

Before MCP, connecting *N* AI applications to *M* external tools required roughly *N × M* custom integrations, one per pairing. MCP collapses that to *N + M*: any MCP-compatible AI application can talk to any MCP server without bespoke glue code.

MCP defines three roles:

- **MCP Host** — the AI application a person interacts with, such as Claude Desktop, Claude Code, Cursor, or VS Code.
- **MCP Client** — a connector the host maintains, one per connected server.
- **MCP Server** — a program that exposes capabilities to the client, running either as a local subprocess (`stdio` transport) or as a remote service (Streamable HTTP transport).

Each server can expose three kinds of primitives:

| Primitive | Description |
|---|---|
| Tools | Executable actions the agent can call, such as running a Pulumi preview |
| Resources | Contextual data the agent can read, such as stack outputs or resource schemas |
| Prompts | Reusable templates that encode a common task, such as a deployment workflow |

Clients communicate with servers over JSON-RPC, discovering what a server offers through calls like `tools/list` and invoking capabilities through calls like `tools/call`. See the [MCP architecture docs](https://modelcontextprotocol.io/docs/learn/architecture) and [transport docs](https://modelcontextprotocol.io/docs/concepts/transports) for the full specification.

MCP has been adopted broadly across the agent ecosystem in the year since it launched, including by [Claude Desktop and Claude Code](https://modelcontextprotocol.io/introduction), [OpenAI's Agents SDK and Responses API](https://developers.openai.com/api/docs/mcp), [Gemini CLI and Vertex AI](https://modelcontextprotocol.io/introduction), [VS Code and GitHub Copilot](https://code.visualstudio.com/docs/copilot/chat/mcp-servers), [Cursor](https://cursor.com/docs/context/mcp), and [Windsurf](https://windsurf.com).

## Why MCP matters for infrastructure as code

Infrastructure work is a natural fit for MCP because the actions an agent needs — read the current state, look up what a resource type actually accepts, run a safe preview, open a pull request — are exactly the kind of discrete, well-defined tools MCP is designed to expose.

- **Agents can see live cloud state, not just static files.** A resource lookup tool lets an agent answer "what buckets do we have in production?" against the real deployment, not a guess based on source code.
- **Previews stay in the loop.** An MCP tool that runs `pulumi preview` lets the agent show you a diff before anything changes, keeping a human decision point in an otherwise autonomous workflow.
- **Prompts encode team conventions.** A server can ship reusable prompts, like a standard deployment or migration workflow, so every agent that connects follows the same playbook instead of improvising.
- **The protocol is host-agnostic.** Because MCP is an open standard rather than a single vendor's plugin format, a Pulumi MCP server works the same way whether you're driving it from Claude Code, Cursor, or any other MCP-compatible client, with no per-tool integration work on Pulumi's side.
- **Code-native infrastructure is easier to expose safely.** Because Pulumi programs are ordinary TypeScript, Python, Go, C#, or Java, the same language tooling an agent already reasons about well (types, functions, tests, package managers) extends naturally to infrastructure, which makes it easier to expose granular, well-typed tools an agent can call correctly on the first try.

## How Pulumi connects your IaC to MCP agents today

Pulumi ships an MCP server in two forms, aimed at slightly different setups. Both expose your Pulumi resource registry, stack state, and deployment actions as MCP tools; which one to use mostly comes down to whether you want a hosted connection or a local process tied to your own Pulumi CLI.

| | Hosted server | Local server |
|---|---|---|
| Transport | Streamable HTTP | stdio (local subprocess) |
| Auth | OAuth via browser popup | `PULUMI_ACCESS_TOKEN` environment variable |
| Requires Pulumi CLI installed | No | Yes |
| Package | N/A (managed endpoint) | `@pulumi/mcp-server` (npm) |
| Best for | Cursor, Claude Code, Claude Desktop, and other remote-capable clients | Environments where you already run the Pulumi CLI locally, or want the server bundled with your dev environment |

The **hosted server** lives at `https://mcp.ai.pulumi.com/mcp`, documented at [pulumi.com/docs/ai/mcp-server](https://www.pulumi.com/docs/ai/mcp-server/). It exposes tools such as `get-stacks`, `resource-search` (Lucene-style queries, for example `type:aws:s3/bucket:Bucket`), `get-policy-violations`, `get-users`, the registry lookups (`get-type`, `get-resource`, `get-function`, `list-resources`, `list-functions`), and the Neo delegation tools described below. It also ships prompts like `deploy-to-aws`, `convert-terraform-to-typescript`, and CDK migration helpers.

The **local server** is the `@pulumi/mcp-server` npm package (binary `pulumi-mcp-server`), run over stdio. It exposes the same registry lookups plus CLI-driven tools: `pulumi-cli-preview`, `pulumi-cli-up`, `pulumi-stack-output`, `pulumi-cli-refresh`, and `neo-task-launcher`. Because it shells out to the Pulumi CLI on your machine, it needs the CLI installed and a `PULUMI_ACCESS_TOKEN` set for any tool that deploys or reads Pulumi Cloud data.

## How to connect Pulumi to your AI agent

The fastest path is the hosted server, since it needs no local installation beyond your MCP-compatible client. These steps walk through connecting it to Cursor or Claude Code; a local alternative follows.

1. Create a Pulumi access token at [app.pulumi.com/account/tokens](https://app.pulumi.com/account/tokens). This token authenticates your agent to Pulumi Cloud and scopes it to your organization.
2. Add the hosted MCP server to your client's configuration. In Cursor, add this to `.cursor/mcp.json`:

   ```json
   {
     "mcpServers": {
       "pulumi": {
         "transport": "http",
         "url": "https://mcp.ai.pulumi.com/mcp"
       }
     }
   }
   ```

   In Claude Code, run:

   ```bash
   claude mcp add --transport http pulumi https://mcp.ai.pulumi.com/mcp
   ```
3. Authenticate when your client opens the OAuth browser popup. Paste the access token you created in step 1 and select the Pulumi organization you want the agent to operate against.
4. Confirm the connection by asking your agent a read-only question, such as "What stacks do I have in my Pulumi organization?" or "Show me all the S3 buckets across my stacks." A working connection returns real data pulled live from Pulumi Cloud.
5. Once the connection is confirmed, ask the agent to generate and preview infrastructure, for example: "I need to create an AWS Lambda that processes S3 events. Look up the Lambda and S3 properties and generate the TypeScript code." The agent uses the registry tools to look up accurate resource properties before writing code, then can run a preview through the same connection.

### Running the server locally instead

If you'd rather run the server yourself against a local Pulumi CLI, install `@pulumi/mcp-server` and connect over stdio. In Claude Code:

```bash
claude mcp add -s user pulumi -- npx @pulumi/mcp-server@latest stdio
```

Or in a raw MCP client configuration (Claude Desktop, VS Code, and similar):

```json
{
  "mcpServers": {
    "pulumi": {
      "command": "npx",
      "args": ["@pulumi/mcp-server@latest", "stdio"]
    }
  }
}
```

VS Code uses a `servers` key instead of `mcpServers` in its `settings.json`; otherwise the shape is the same. Set `PULUMI_ACCESS_TOKEN` in your environment for any tool that reads or writes to Pulumi Cloud.

## Generate infrastructure in your language: TypeScript and Python

Because the MCP registry tools return accurate, current resource and function signatures, an agent connected to Pulumi can generate idiomatic code in whichever language your team uses, without you writing a line of boilerplate yourself. Ask the same question in a TypeScript project and a Python project, and the agent looks up the same underlying resource schema through MCP but returns code fit to each language's conventions.

Asking "Create an S3 bucket with versioning enabled and block all public access" produces this in a TypeScript stack:

```typescript
import * as aws from "@pulumi/aws";

const bucket = new aws.s3.BucketV2("app-data", {
    forceDestroy: false,
});

const versioning = new aws.s3.BucketVersioningV2("app-data-versioning", {
    bucket: bucket.id,
    versioningConfiguration: {
        status: "Enabled",
    },
});

const publicAccessBlock = new aws.s3.BucketPublicAccessBlock("app-data-pab", {
    bucket: bucket.id,
    blockPublicAcls: true,
    blockPublicPolicy: true,
    ignorePublicAcls: true,
    restrictPublicBuckets: true,
});

export const bucketName = bucket.bucket;
```

And this in a Python stack:

```python
import pulumi_aws as aws

bucket = aws.s3.BucketV2(
    "app-data",
    force_destroy=False,
)

versioning = aws.s3.BucketVersioningV2(
    "app-data-versioning",
    bucket=bucket.id,
    versioning_configuration={
        "status": "Enabled",
    },
)

public_access_block = aws.s3.BucketPublicAccessBlock(
    "app-data-pab",
    bucket=bucket.id,
    block_public_acls=True,
    block_public_policy=True,
    ignore_public_acls=True,
    restrict_public_buckets=True,
)

pulumi.export("bucket_name", bucket.bucket)
```

Both programs declare the same three resources with the same configuration; only the syntax changes to match each language's idioms (camelCase versus snake_case arguments, `export` versus `pulumi.export`). Once the agent has written either version, the same MCP connection can run `pulumi preview` to show you the exact diff before anything is created, so you keep a review step even in an agent-driven workflow.

## Delegate to Neo through MCP

Pulumi's MCP server also exposes Neo, Pulumi's infrastructure engineering agent, as a delegation target. Tools like `neo-bridge` and `neo-task-launcher` let any MCP-connected client hand off a longer-running, autonomous task to Neo rather than working through it turn by turn.

For example, asking your agent "Ask Neo to analyze all my S3 buckets for security issues and create a pull request with fixes" triggers Neo to run the analysis and open a PR, returning a tracking link on [app.pulumi.com](https://app.pulumi.com) so you can follow the task to completion.

MCP works in the other direction for Neo as well: Neo is itself an MCP client that can connect out to a fixed set of third-party MCP servers as tools during a task, including Atlassian (Jira and Confluence), Datadog, Honeycomb, Linear, PagerDuty, and Supabase. An organization admin configures which of these are available under Neo's integration settings, and connections can be toggled per task. Credentials for these integrations are encrypted at rest per organization and decrypted only at task execution time; they are never exposed to the underlying language model. See the [Neo MCP integrations documentation](https://www.pulumi.com/docs/ai/integrations/mcp/) for the current list and setup details.

## Frequently asked questions

### What is the Model Context Protocol?

MCP is an open-source standard, created by Anthropic and now governed by the Agentic AI Foundation under the Linux Foundation, that lets AI applications connect to external tools and data through one consistent interface instead of a custom integration per pairing.

### Does Pulumi have an MCP server?

Yes. Pulumi offers a hosted MCP server at `mcp.ai.pulumi.com` for clients that support remote connections, and a local server distributed as the `@pulumi/mcp-server` npm package for clients that connect over stdio.

### Which AI tools work with the Pulumi MCP server?

Any MCP-compatible client can connect, including Claude Code, Claude Desktop, Cursor, VS Code with GitHub Copilot, and Windsurf. Because MCP is an open standard, new clients that implement the protocol work without any additional integration work on Pulumi's side.

### Do I need the Pulumi CLI installed to use MCP?

Only if you run the local server. The hosted server at `mcp.ai.pulumi.com` needs no local Pulumi CLI installation; you authenticate with an access token instead.

### Is MCP tied to one AI vendor?

No. MCP was created by Anthropic but was donated to the Agentic AI Foundation, a directed fund under the Linux Foundation, specifically so it could be governed independently of any single company. It's already implemented by clients from OpenAI, Google, Anthropic, and others.

### How does Neo relate to MCP?

Two ways. Pulumi's MCP server exposes Neo as a delegation target, so any MCP client can hand off autonomous infrastructure tasks to it. Separately, Neo itself acts as an MCP client, connecting to third-party MCP servers like Jira, Datadog, and PagerDuty to pull in context during its own tasks.

### Can an MCP-connected agent deploy real infrastructure?

Yes, through tools like `pulumi-cli-up` on the local server or the `deploy-to-aws` prompt on the hosted server. Because previews remain available through the same connection, teams typically keep a human review step before an agent-initiated deployment goes through, alongside policy as code guardrails for anything that shouldn't ship without a check.

## Learn more

- [Pulumi MCP server documentation](https://www.pulumi.com/docs/ai/mcp-server/)
- [Neo MCP integrations](https://www.pulumi.com/docs/ai/integrations/mcp/)
- [Model Context Protocol specification](https://modelcontextprotocol.io/specification/latest)
- [What is agentic infrastructure?](/what-is/what-is-agentic-infrastructure/)