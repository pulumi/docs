---
title_tag: "Direct Resource Operations (pulumi do) | Pulumi CLI"
meta_desc: "pulumi do provides direct cloud resource operations through the Pulumi CLI. Create, read, update, delete, and query resources without a project or program."
title: Direct Resource Operations
h1: Direct resource operations
menu:
    iac:
        name: Direct Resource Operations
        parent: iac-cli
        identifier: iac-cli-do
        weight: 55
aliases:
    - /docs/iac/concepts/direct-resource-operations/
---

{{% notes type="info" %}}
`pulumi do` is in **research preview**. The command interface may change based on feedback.
{{% /notes %}}

The `pulumi do` command provides direct operations on cloud resources through the Pulumi CLI without requiring a project, program, or state file. It exposes the full Pulumi provider ecosystem as a CLI, with commands generated dynamically from each provider's schema.

## Overview

`pulumi do` supports two types of operations:

- **Provider functions**: Read-only queries against cloud APIs (e.g., looking up a VPC, fetching an AMI).
- **Resource operations**: Create, read, patch (update), and delete cloud resources.

### Modes

- **Stateful**: This is the default mode for `pulumi do`. Resources created or updated in this mode are recorded as snippets in the state file of your current project, and their lifetime is tracked. Because they live in ordinary Pulumi state, they get the same benefits as program-managed resources: policy enforcement, drift detection with `pulumi refresh`, and references between resources. If you are not currently in a project, they are recorded in a global project named `default-global-project` (stored in your Pulumi home directory, with a stack named `default`) that's created automatically on first use.

- **Stateless**: This mode can be enabled using the `--stateless` flag. In this mode resources are not recorded anywhere, so it's a good fit for one-off operations or testing.

### Command syntax

```
# Provider functions
pulumi do <package:module:function> [flags]

# Resource operations
pulumi do <package:module:type> <operation> [<name>|<id>] [flags]
```

The `create`, `delete` and `patch` operations take the resource's [logical name](/docs/iac/concepts/resources/names), while the `read` operation takes the provider-assigned [physical ID](/docs/iac/concepts/resources/names). With `--stateless`, `create` takes no argument and `delete` and `patch` take the provider-assigned ID instead of the name.

The package, module, and type/function segments come directly from the provider schema. Pass `--help` at any level of the command tree to discover available subcommands.

### When to use `pulumi do` vs `pulumi up`

| Scenario | `pulumi do` | `pulumi up` |
|----------|:-----------:|:-----------:|
| Querying cloud APIs | Yes | No |
| Creating or modifying individual resources | Yes | Yes |
| Exploring a provider's capabilities | Yes | No |
| Agent-driven ad-hoc operations | Yes | Better for repeatable workflows |
| Production infrastructure management | No | Yes |
| State tracking and drift detection | Yes (stateful mode) | Yes |
| Multi-resource dependency graphs | Yes (stateful mode) | Yes |
| Policy enforcement and compliance | Yes (stateful mode) | Yes |
| Repeatable, reviewable deployments | No | Yes |

## Provider functions

Provider functions are read-only operations that query cloud APIs through Pulumi's provider layer.

### Running a function

```bash
$ pulumi do <package:module:function> --input-file <path>
```

The input file contains the function's arguments. The output is JSON written to stdout.

### Example: look up a VPC

```bash
$ pulumi do aws:ec2:getVpc --input-file query.yaml
```

Where `query.yaml` contains:

```yaml
tags:
    Name: production
```

Output:

```json
{
  "arn": "arn:aws:ec2:us-west-2:123456789:vpc/vpc-abc123",
  "cidrBlock": "10.0.0.0/16",
  "id": "vpc-abc123",
  "tags": {
    "Name": "production"
  }
}
```

### Input file formats

Top-level keys map to function parameters:

```yaml
parameterName: value
nestedParameter:
    key: value
```

The input is bound against the function's schema for full type checking before execution.

## Resource operations

Resource operations let you create, read, update, and delete cloud resources directly. Each operation uses the same provider logic as a full Pulumi program.

### Create

Creates a new cloud resource. Pass inputs via an input file, or set scalar inputs directly with per-input command-line flags. The CLI prompts for confirmation before creating.

```bash
$ pulumi do <package:module:type> create <name> --input-file <path>
$ pulumi do <package:module:type> create <name> --<input-name> <value>
```

Output on success is a JSON object with the provider-assigned `id` and all resource properties.

### Read

Reads the current state of an existing resource by its cloud provider ID.

```bash
$ pulumi do <package:module:type> read <provider-resource-id>
```

### Patch (update)

Updates an existing resource. The CLI reads the current state, merges your changes, displays a diff, and prompts for confirmation.

```bash
$ pulumi do <package:module:type> patch <name> --input-file <path>
```

### Delete

Deletes a resource by the name it was created with. The CLI prompts for confirmation before destroying.

```bash
$ pulumi do <package:module:type> delete <name>
```

With `--stateless`, pass the provider-assigned resource ID instead of the name.

## Flags

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--input-file` | string | | Path to a file containing function or resource inputs |
| `--input` | string | `yaml` | Input file format |
| `--<input-name>` | | | Set a single scalar input directly (one flag per input in the schema) |
| `--provider-file` | string | | Path to a file containing provider configuration |
| `--dry-run` | bool | `false` | Run in preview mode (provider returns placeholder values) |
| `--output` | string | `default` | Output format for resource operation results (`default` or `json`) |
| `--show-secrets` | bool | `false` | Show secret values in output |
| `--stateless` | bool | `false` | Run resource operations directly against the provider without recording state |
| `--yes` | bool | `false` | Auto-approve confirmation prompts |

## Output format

All `pulumi do` operations write output to stdout. Progress messages and prompts are written to stderr.

For structured output suitable for piping and scripting, pass `--output json`:

```bash
# Pipe function output to jq
$ pulumi do aws:ec2:getVpc --input-file query.yaml | jq '.cidrBlock'

# Redirect resource output to a file while seeing progress
$ pulumi do aws:s3:Bucket read my-bucket > result.json
```

Secrets appear as `[secret]` in output by default. Use `--show-secrets` to reveal them.

Provider functions return the raw function result as JSON. Resource operations return the resource's properties as a flat JSON object that includes the provider-assigned `id`.

## Provider configuration

Providers need credentials and configuration to operate. `pulumi do` resolves provider configuration through:

1. **Ambient credentials**: Environment variables and credential files already present in the shell (e.g., `AWS_ACCESS_KEY_ID`, `~/.aws/credentials`).
1. **Provider configuration file**: Supply provider config via a YAML file using the `--provider-file` flag.

    ```bash
    $ pulumi do aws:ec2:getVpc --input-file query.yaml \
        --provider-file aws-config.yaml
    ```

## See also

- [Pulumi CLI reference](/docs/iac/cli/)
- [Pulumi ESC](/docs/esc/)
- [Resource management with Pulumi IaC](/docs/iac/concepts/resources/)
- [Introducing `pulumi do`](/blog/pulumi-do-direct-resource-operations/) (blog post)
