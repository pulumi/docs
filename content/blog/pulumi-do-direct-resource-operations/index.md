---
title: "Introducing pulumi do: Direct Resource Operations for Any Cloud"
date: 2026-05-22T06:00:00-07:00
draft: false
meta_desc: "pulumi do lets you create, read, update, delete, and query any cloud resource from the terminal with a single command. No IaC project required."
meta_image: meta.png
feature_image: feature.png
authors:
    - fraser-waters
    - pat-gavlin
    - arun-loganathan
tags:
    - features
    - pulumi-cli
    - ai-agents
    - product-launches
schema_type: auto

social:
    twitter:
    linkedin:
    bluesky:
---

Infrastructure as code is the right model for production systems. State tracking, drift detection, and repeatable deployments all matter when you're managing real workloads. But there are also times you need a quick, one-off interaction with the cloud: create a bucket, look up a VPC, delete a leftover resource.

Today we're introducing `pulumi do`, a new command for direct resource operations. Create, read, update, delete, and query any cloud resource from the terminal with a single command, across all 150+ Pulumi providers. No project, no stack, no state file required.

<!--more-->

## The problem: IaC is too heavy for every interaction

When you're managing production workloads, IaC earns its weight. State tracking catches drift before it causes outages. Dependency graphs sequence changes safely. Policy enforcement keeps teams in bounds. That full lifecycle is exactly what you want for systems that matter.

But when an LLM needs a Postgres database on AWS, the straightest-line path with IaC is eight steps: create a directory, initialize a project, pick a language, install packages, configure credentials, write infrastructure code, preview, deploy. That is a lot of surface area for errors, a lot of tokens consumed across those steps, and a lot of cost for what should be a simple operation. `pulumi do` collapses those eight steps into one, while using the same providers and type system that power a full Pulumi program.

As Joe described in [the agentic infrastructure era](/blog/the-agentic-infrastructure-era/), resource creation is only part of the problem. The real blocker for AI agents is everything around the code: creating cloud accounts, plumbing credentials, wiring configuration across services. [Agent accounts](/docs/administration/organizations-teams/agent-accounts/) tackle the first piece by letting agents provision a Pulumi Cloud account on the fly, no signup form, no browser. [Pulumi ESC](/docs/esc/) tackles the second by unifying credentials across every provider. Together with `pulumi do`, an agent goes from zero to deployed infrastructure without leaving the terminal. We also shipped a [redesigned CLI](/blog/better-cli-interactions-for-agents-and-humans/) so both humans and agents can find the right command on the first try. And when that one-off resource grows into a production system, `pulumi do` provides a graduation path back to full IaC.

## What it looks like

You need to spin up an S3 bucket. With the AWS CLI, you assemble `aws s3api create-bucket` with the right flags, region constraints, and JSON input. With `pulumi do`:

```bash
$ pulumi do aws:s3:Bucket create --input-file bucket.pcl
```

The bucket exists. The result is JSON on stdout. No project, no stack, no state file.

Need to look up a VPC instead?

```bash
$ pulumi do aws:ec2:getVpc --input-file query.pcl
```

Same CLI, same output contract, same provider ecosystem.

## One command, any provider

The command dynamically builds its CLI tree from any installed Pulumi provider's schema. Every resource type and every function becomes a subcommand at runtime. You get the same type checking and default handling that a full Pulumi program provides, applied at the CLI layer before anything touches the cloud.

### The command shape

```
# Provider functions (read-only queries)
pulumi do <package:module:function> [flags]

# Resource operations (create, read, patch, delete, list)
pulumi do <package:module:type> <operation> [<id>] [flags]
```

The package, module, and type/function segments come directly from the provider schema, so `--help` works at every level of the tree. Pass a package name, an optional module, and a function or resource type. The CLI resolves the rest.

### Provider functions

Provider functions are read-only operations that query cloud APIs through Pulumi's provider layer. They shipped in [Pulumi CLI v3.242.0](https://github.com/pulumi/pulumi/releases/tag/v3.242.0).

```bash
# Look up a VPC by tags
$ pulumi do aws:ec2:getVpc --input-file query.pcl

{
  "arn": "arn:aws:ec2:us-west-2:123456789:vpc/vpc-abc123",
  "cidrBlock": "10.0.0.0/16",
  "id": "vpc-abc123",
  "tags": {
    "Name": "production"
  }
}
```

The input file is a PCL (Pulumi Configuration Language) snippet describing the function arguments:

```hcl
tags = {
    "Name" = "production"
}
```

Internally, the CLI parses the input and binds it against the function's schema using a new `BindFunction` method in the PCL codegen library. You get full type checking before the provider is ever called. The bound PCL then runs through the same evaluation logic the engine uses for resource registrations (defaults, type casting, secret marking). The provider's `Invoke` call executes, and the result lands as JSON on stdout.

YAML input files also work. Pass `--input yaml` alongside `--input-file` and the CLI converts the YAML through a converter plugin before evaluation:

```bash
$ pulumi do aws:ec2:getVpc --input-file query.yaml --input yaml
```

Secrets in function results appear as `[secret]` by default. Pass `--show-secrets` to reveal them. The `--dry-run` flag sets the operation to preview mode, signaling the provider to return placeholder values instead of live data.

### Resource operations

Resource operations let you create, read, update, delete, and list cloud resources directly from the CLI. Each operation maps to a provider CRUD method, using the same provider logic a full Pulumi program would use.

**Create** a resource by passing inputs via a file:

```bash
$ pulumi do aws:s3:Bucket create --input-file bucket.pcl
```

Where `bucket.pcl` contains:

```hcl
bucket = "my-data-bucket"
```

The CLI prompts for confirmation before creating. Pass `--yes` to auto-approve. On success, the output is JSON with the cloud provider ID and all resource properties:

```json
{
  "id": "my-data-bucket",
  "arn": "arn:aws:s3:::my-data-bucket",
  "bucket": "my-data-bucket",
  "region": "us-west-2"
}
```

**Read** a resource's current state by its cloud provider ID:

```bash
$ pulumi do aws:s3:Bucket read my-data-bucket
```

The output follows the same `{"id", [properties]}` shape.

**Patch** (update) a resource by providing new inputs. The CLI reads the current state, merges your changes, shows a diff, and prompts for confirmation:

```bash
$ pulumi do aws:s3:Bucket patch my-data-bucket --input-file updates.pcl
```

**Delete** a resource. The CLI prompts for confirmation before destroying:

```bash
$ pulumi do aws:s3:Bucket delete my-data-bucket
```

**List** resources of a given type (when the provider supports it):

```bash
$ pulumi do aws:s3:Bucket list
```

The `--all` flag retrieves every resource. `--count N` limits the result set. The output is a JSON array of `{"id", "name"}` objects.

All mutating operations (create, patch, delete) prompt for confirmation. Pass `--yes` to skip the prompt, which is useful for scripting and agent workflows.

### Provider configuration

Providers need credentials to operate. Today, `pulumi do` resolves provider configuration through ambient credentials (environment variables and credential files already present in your shell, like `AWS_ACCESS_KEY_ID` or `~/.aws/credentials`).

You can also supply provider configuration via a PCL file:

```bash
$ pulumi do aws:ec2:getVpc --input-file query.pcl \
    --provider-file aws-config.pcl
```

## Designed for agents and humans

`pulumi do` pairs with [agent accounts](/docs/administration/organizations-teams/agent-accounts/), free ephemeral Pulumi Cloud accounts that agents create on the fly without a manual signup step. An agent running Claude Code, Codex, or Cursor can go from zero (no Pulumi account, no CLI installed) to creating cloud resources in a single session. The human claims the account later to make it permanent.

Three design choices make `pulumi do` work well for AI agents, and they make it better for humans too.

**Consistent command structure across every provider.** The `<package:module:type> <operation>` pattern is the same for AWS, Azure, Google Cloud, Kubernetes, Cloudflare, Datadog, and every other Pulumi provider. An agent that learns the pattern once can operate across any cloud. This is the guessability principle from [the CLI redesign](/blog/better-cli-interactions-for-agents-and-humans/) applied to resource operations: the right command should be the one you can guess.

**Predictable output contract.** JSON on stdout, progress on stderr, consistent exit codes. An agent can parse the result programmatically without scraping human-formatted tables.

**150+ providers under one syntax.** Many cloud and SaaS providers don't have a full CLI at all. Datadog's CLI focuses on CI/CD and serverless instrumentation rather than general resource management. Cloudflare's covers a subset of its API. `pulumi do` generates commands from the provider schema, so if a Pulumi provider exists for it, the CLI works. An agent doesn't need to learn (or even know about) each provider's native tooling.

## What's next

Resource operations and provider functions are the foundation. The `pulumi do` roadmap extends the same direct-operation model with credential management, state tracking, and a path to full IaC.

### Unified credentials with Pulumi ESC

One of the hardest parts of multi-cloud operations is credential management. Each provider has its own authentication scheme, environment variables, and session lifecycle. An agent working across AWS, Cloudflare, and Datadog today manages three separate credential mechanisms. That friction adds up fast.

We're building [Pulumi ESC](/docs/esc/) integration into `pulumi do` so you manage credentials once and resolve them everywhere. ESC handles credential resolution (including OIDC-based dynamic credential generation and short-lived tokens) across all your providers. No need to know how each provider's authentication works or manage environment variables manually. Name the credential set, and ESC does the rest, with rotation, RBAC, and audit built in.

### Cross-resource references

Real infrastructure has dependencies. A subnet needs a VPC ID. A security group rule needs a security group ID. When you're building resources one at a time, those references need to flow between commands.

A future version of `pulumi do` will let resource inputs reference outputs from previously created resources. The CLI will resolve those references automatically and preserve the dependency graph. When you later graduate to a full IaC program, the generated code contains proper resource references rather than hard-coded strings.

### Stateful mode and the graduation path

Today, `pulumi do` is stateless. Each command runs independently. A planned stateful mode will persist resource state across operations, enabling drift detection, lifecycle management, and a graduation path to full infrastructure as code.

The planned progression:

1. **Zero setup.** Your first `pulumi do` mutation automatically creates a default project and stack. No manual initialization.

1. **Accumulate resources.** Each operation stores resource state. After a few commands, you have a lightweight representation of your infrastructure.

1. **Eject to a full project.** When complexity demands it, generate a Pulumi project in your chosen language with all resources imported and dependency graphs intact.

1. **Connect to Pulumi Cloud.** Layer on governance, compliance, team collaboration, and deployment automation through [Pulumi Cloud](/product/). Resources created via `pulumi do` can be governed by [Pulumi Insights](/product/insights-governance/) from day one, even before you opt into a full IaC workflow.

The eject path works because `pulumi do` uses the same providers, resource types, and property schemas as `pulumi up`. The cloud resources stay exactly as they are. You're layering management capabilities on top of what already exists.

## Get started

`pulumi do` ships as a research preview in [Pulumi CLI v3.242.0](https://github.com/pulumi/pulumi/releases/tag/v3.242.0) and later. Install or update the CLI, install a provider plugin, and start running commands. The [documentation](/docs/iac/cli/direct-resource-operations/) has the full reference.

We'd like your feedback. Try `pulumi do`, tell us what works, and help shape the CLI that agents and humans both reach for first.

- [Documentation](/docs/iac/cli/direct-resource-operations/)
- [File a feature request](https://github.com/pulumi/pulumi/issues/new)
- [Pulumi Community Slack](https://slack.pulumi.com/) for discussion
