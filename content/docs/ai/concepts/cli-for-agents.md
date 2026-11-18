---
title_tag: The Pulumi CLI for AI Agents
meta_desc: "Run the Pulumi CLI from a coding agent, inspect resources, preview code changes, and read JSON output."
title: CLI for agents
h1: The Pulumi CLI for agents
menu:
    ai:
        name: Use the Pulumi CLI
        parent: ai-coding-agents
        weight: 30
aliases:
- /docs/ai/cli-for-agents/
---

Run the [Pulumi CLI](/docs/iac/cli/) from your coding agent to inspect stacks, preview code changes, and apply updates you authorize. The agent uses the credentials and tools available in its local environment.

<span id="no-install-step-npx-pulumi"></span>

## Run the CLI with npx

If your environment has [Node.js and npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm), use `npx` to run the CLI without a separate global installation:

```bash
npx pulumi version
```

The command prints the CLI version. When the package is not installed locally, `npx` downloads it and may ask for confirmation. Your environment needs network access for that download.

Before running project commands, install the project's language dependencies, [log in to your backend](/docs/iac/cli/commands/pulumi_login/), and configure the stack and cloud credentials. Run commands from the directory containing `Pulumi.yaml`:

```bash
npx pulumi preview
```

For a persistent local environment, you can also [install the CLI](/docs/install/) and run `pulumi` directly.

<span id="one-shot-resource-operations-pulumi-do"></span>

## Inspect resources with pulumi do

[`pulumi do`](/docs/iac/cli/direct-resource-operations/) calls cloud providers without requiring a Pulumi program. For example, to read an existing S3 bucket, configure AWS credentials and replace `my-bucket` with the bucket's name:

```bash
npx pulumi do aws:s3:Bucket read my-bucket
```

The command returns the resource's properties. Use the resource type and inputs defined by the provider's schema. See [Direct resource operations](/docs/iac/cli/direct-resource-operations/) for provider functions, write operations, and state tracking. Use a Pulumi program for repeatable deployments defined in code.

{{% notes type="info" %}}
`pulumi do` is in **research preview**. The command interface may change based on feedback.
{{% /notes %}}

<span id="structured---json-output"></span>

## Read JSON output

Commands such as `preview`, `up`, `destroy`, `refresh`, `stack output`, and `config` support `--json` output:

```bash
npx pulumi preview --json
npx pulumi stack output --json
```

Ask the coding agent to read this JSON when it needs to inspect proposed changes or use stack outputs in another command. `pulumi do` also writes JSON to stdout, with progress and prompts on stderr. Check the [command reference](/docs/iac/cli/commands/) for the output and flags each command supports.

<span id="verifiable-by-design-preview-every-change"></span>

## Preview code changes

Run [`pulumi preview`](/docs/iac/cli/commands/pulumi_preview/) to inspect the resource operations proposed by a Pulumi program before an update. Review the diff and any policy results before authorizing a deployment.

A preview describes the proposed operations using the information available at that time. Some values are unknown until resources are created. Resources created inside an [`apply` callback](/docs/iac/concepts/inputs-outputs/apply/) may be absent from the preview when its input is unknown.

<span id="zero-friction-accounts"></span>

## Create an agent account

[Agent accounts](/docs/administration/concepts/agent-accounts/) let a coding agent start using Pulumi Cloud before a person creates an account. Set `PULUMI_ENABLE_AUTOMATIC_AGENT_SIGNUP=true` to opt in. When the CLI detects an agent environment without Pulumi Cloud credentials, it creates an ephemeral account and prints a claim link. Open that link to claim the account and keep its infrastructure.

<span id="next-steps"></span>
