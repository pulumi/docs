---
title_tag: The Pulumi CLI for AI Agents
meta_desc: "The Pulumi CLI is built for AI agents: run it with npx pulumi, do one-shot resource operations with pulumi do, and parse structured --json output."
title: CLI for agents
h1: The Pulumi CLI for agents
menu:
    ai:
        name: Pulumi CLI for agents
        parent: ai-concepts
        weight: 40
aliases:
- /docs/ai/cli-for-agents/
---

The [Pulumi CLI](/docs/iac/cli/) is built to be driven by AI agents. Because Pulumi infrastructure is real code with a verifiable plan for every change, agents like Claude Code, Codex, Cursor, and GitHub Copilot can write, preview, and deploy it directly, with no bespoke integration required. This page collects the CLI features that make that possible.

[Pulumi Agent Skills](/docs/ai/concepts/agent-skills/) teach agents Pulumi workflows. The [Pulumi MCP server](/docs/ai/guides/set-up-mcp-server/) lets them query Pulumi Cloud and the Registry. See [Use your coding agent with Pulumi](/docs/ai/coding-agents/) for an overview of these tools.

## No install step: `npx pulumi`

An agent working in a fresh sandbox rarely has the Pulumi CLI installed, and installing tools is exactly the kind of setup an agent shouldn't have to reason about. Running the CLI through `npx` removes that step entirely:

```bash
npx pulumi up
npx pulumi stack output --json
```

Any `pulumi` command works this way. For a persistent local environment, [install the CLI](/docs/install/) the usual way; for ephemeral agent runs, `npx pulumi` keeps the CLI reachable with nothing to set up first.

## One-shot resource operations: `pulumi do`

[`pulumi do`](/docs/iac/cli/direct-resource-operations/) performs direct operations on cloud resources without requiring a Pulumi program. It exposes the full Pulumi provider ecosystem as a CLI, with commands generated dynamically from each provider's schema, so an agent can create, read, update, or delete a single resource, or query a cloud API, without scaffolding a whole program first.

```bash
# Query a cloud API with a read-only provider function
pulumi do aws:ec2:getVpc --input-file query.yaml

# Read a single resource by its cloud provider ID
pulumi do aws:s3:Bucket read my-bucket
```

By default, resource changes are recorded in Pulumi state and support state tracking, drift detection, and policy enforcement. The `--stateless` flag opts out of that tracking. Use a Pulumi program and `pulumi up` for repeatable deployments defined in code. See [Direct resource operations](/docs/iac/cli/direct-resource-operations/) for the modes and their tradeoffs.

{{% notes type="info" %}}
`pulumi do` is in **research preview**. The command interface may change based on feedback.
{{% /notes %}}

## Structured `--json` output

Agents work best with machine-readable results rather than scraped human-readable text. Most Pulumi commands accept a `--json` flag that emits structured output an agent can parse directly, including `preview`, `up`, `destroy`, `refresh`, `stack output`, and `config`:

```bash
pulumi preview --json
pulumi stack output --json
```

`pulumi do` writes structured JSON to stdout as well, with progress and prompts going to stderr, so its output pipes cleanly into other tools. See the [Pulumi CLI command reference](/docs/iac/cli/commands/) for the flags each command supports.

## Verifiable by design: preview every change

Every Pulumi change has a [preview](/docs/iac/cli/commands/pulumi_preview/) that shows exactly what will be created, updated, or deleted before anything happens. That plan-then-apply model matters for agents: a change can be inspected (by the agent, by a human, or by a [policy](/docs/discovery-governance/concepts/policy-as-code/)) and confirmed before it lands, rather than discovered after the fact. An agent can run `pulumi preview --json`, reason about the diff, and only then run `pulumi up`.

## Zero-friction accounts

An agent that runs the CLI still needs somewhere to store state. [Agent accounts](/docs/administration/concepts/agent-accounts/) remove that friction: when the CLI detects it is running in an agent context with no Pulumi Cloud credentials, it provisions a free ephemeral account automatically and keeps working, printing a claim link the user can redeem later. No human has to sign up first for the agent to get started.

## Next steps

- [Agent Skills](/docs/ai/concepts/agent-skills/) — teach your agent proven Pulumi workflows it can apply on top of the CLI.
- [Pulumi MCP server](/docs/ai/guides/set-up-mcp-server/): query Pulumi Cloud and the Pulumi Registry through the [Model Context Protocol](/topics/agentic-infrastructure/mcp-for-infrastructure-as-code/).
- [Agent accounts](/docs/administration/concepts/agent-accounts/) — ephemeral Pulumi Cloud accounts provisioned automatically for agents.
- [Pulumi CLI reference](/docs/iac/cli/) — the full command set behind everything above.
