---
title_tag: "Direct Resource Operations (pulumi do) | Pulumi CLI"
meta_desc: "pulumi do provides direct cloud resource operations through the Pulumi CLI. Create, read, update, delete, and query resources without a project or program."
title: Direct Resource Operations
h1: Direct resource operations
meta_image: /images/docs/meta-images/docs-meta.png
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
- **Resource operations**: Create, read, patch (update), delete, and list cloud resources.

### Command syntax

```
# Provider functions
pulumi do <package> [<module>] <function> [flags]

# Resource operations
pulumi do <package> [<module>] <type> <operation> [<id>] [flags]
```

The package, module, and type/function segments come directly from the provider schema. Pass `--help` at any level of the command tree to discover available subcommands.

### When to use `pulumi do` vs `pulumi up`

| Scenario | `pulumi do` | `pulumi up` |
|----------|:-----------:|:-----------:|
| Querying cloud APIs | Yes | No |
| Creating or modifying individual resources | Yes | Yes |
| Exploring a provider's capabilities | Yes | No |
| Agent-driven ad-hoc operations | Yes | Better for repeatable workflows |
| Production infrastructure management | No | Yes |
| State tracking and drift detection | No (stateless) | Yes |
| Multi-resource dependency graphs | No | Yes |
| Policy enforcement and compliance | No | Yes |
| Repeatable, reviewable deployments | No | Yes |

## Provider functions

Provider functions are read-only operations that query cloud APIs through Pulumi's provider layer.

### Running a function

```bash
$ pulumi do <package> [<module>] <function> --input-file <path>
```

The input file contains the function's arguments. The output is JSON written to stdout.

### Example: look up a VPC

```bash
$ pulumi do aws ec2 getVpc --input-file query.pcl
```

Where `query.pcl` contains:

```hcl
tags = {
    "Name" = "production"
}
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

**PCL (default):** Top-level assignments map to function parameters:

```hcl
parameterName = "value"
nestedParameter = {
    key = "value"
}
```

The PCL input is bound against the function's schema for full type checking before execution.

**YAML:** Pass `--input yaml` alongside `--input-file`:

```bash
$ pulumi do aws ec2 getVpc --input-file query.yaml --input yaml
```

The CLI converts YAML to PCL through a converter plugin before evaluation.

## Resource operations

Resource operations let you create, read, update, delete, and list cloud resources directly. Each operation uses the same provider logic as a full Pulumi program.

### Create

Creates a new cloud resource. Pass inputs via an input file. The CLI prompts for confirmation before creating.

```bash
$ pulumi do <package> [<module>] <type> create --input-file <path>
```

Output on success:

```json
{
  "id": "<provider-assigned-id>",
  "properties": { ... }
}
```

### Read

Reads the current state of an existing resource by its cloud provider ID.

```bash
$ pulumi do <package> [<module>] <type> read <provider-resource-id>
```

### Patch (update)

Updates an existing resource. The CLI reads the current state, merges your changes, displays a diff, and prompts for confirmation.

```bash
$ pulumi do <package> [<module>] <type> patch <provider-resource-id> --input-file <path>
```

### Delete

Deletes a resource. The CLI prompts for confirmation before destroying.

```bash
$ pulumi do <package> [<module>] <type> delete <provider-resource-id>
```

### List

Lists resources of a given type (when the provider supports listing).

```bash
$ pulumi do <package> [<module>] <type> list
```

| Flag | Description |
|------|-------------|
| `--all` | Retrieve all resources (no pagination limit) |
| `--count N` | Limit the number of results returned |

## Flags

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--input-file` | string | | Path to a file containing function or resource inputs |
| `--input` | string | `pcl` | Input file format (`pcl` built-in; other formats like `yaml` require a converter plugin) |
| `--provider-file` | string | | Path to a file containing provider configuration |
| `--provider-format` | string | `pcl` | Format of the provider configuration file |
| `--dry-run` | bool | `false` | Run in preview mode (provider returns placeholder values) |
| `--show-secrets` | bool | `false` | Show secret values in output |
| `--yes` | bool | `false` | Auto-approve confirmation prompts |

## Output format

All `pulumi do` operations write structured JSON to stdout. Progress messages and prompts go to stderr. This separation allows clean piping and scripting:

```bash
# Pipe function output to jq
$ pulumi do aws ec2 getVpc --input-file query.pcl | jq '.cidrBlock'

# Redirect resource output to a file while seeing progress
$ pulumi do aws s3 Bucket read my-bucket > result.json
```

Secrets appear as `[secret]` in output by default. Use `--show-secrets` to reveal them.

Provider functions return the raw function result as JSON. Resource operations return a JSON object with `id` and `properties` fields.

## Provider configuration

Providers need credentials and configuration to operate. `pulumi do` resolves provider configuration through:

1. **Ambient credentials**: Environment variables and credential files already present in the shell (e.g., `AWS_ACCESS_KEY_ID`, `~/.aws/credentials`).
1. **Provider configuration file**: Supply provider config via a PCL file using the `--provider-file` flag.

    ```bash
    $ pulumi do aws ec2 getVpc --input-file query.pcl \
        --provider-file aws-config.pcl
    ```

<!-- TODO: Document ESC integration (--env flag) once available -->

## Stateful mode (planned)

<!-- TODO: Document stateful mode once available -->

Stateful mode will persist resource state across operations, enabling:

- Drift detection on resources created with `pulumi do`
- Lifecycle management (refresh, protect, retain-on-delete)
- Graduation to full IaC programs via `pulumi init --import-from-do`

In stateful mode, each mutation stores a PCL fragment in the stack's snapshot. The collection of fragments forms an embedded program that the engine can evaluate alongside a user's language program.

On first mutation, `pulumi do` automatically creates a default project at `$PULUMI_HOME/do/default/` with a `dev` stack.

## Graduation to infrastructure as code

`pulumi do` serves as an on-ramp to the full [Pulumi IaC workflow](/docs/iac/). The planned progression:

1. **Start with `pulumi do`**: Query cloud APIs and create resources with single commands.
1. **Accumulate state**: Stateful mode tracks resources and their relationships.
1. **Eject to a full project**: Run `pulumi init --import-from-do` to generate a Pulumi project with your resources imported and dependency-tracked.
1. **Manage with `pulumi up`**: Full IaC workflow with previews, diffs, policy checks, and CI/CD integration.

`pulumi do` uses the same providers and resource types as `pulumi up`, so there's nothing to migrate. The cloud resources stay exactly as they are. You're layering management capabilities on top.

## Limitations

Current limitations of `pulumi do`:

- **No ESC integration**: The `--env` flag for Pulumi ESC credential resolution is not yet available. Use ambient credentials or `--provider-file`.
- **No state tracking**: Stateless mode does not record what resources you create.
- **No inline flags for properties**: You must provide an input file. CLI flag-based property input is not yet supported.
- **Limited input formats**: PCL is built-in. Other formats (like YAML) require a converter plugin to be installed.
- **Hidden command**: `pulumi do` does not appear in `pulumi --help`. Access it directly by name.

## See also

- [Pulumi CLI reference](/docs/iac/cli/)
- [Pulumi ESC](/docs/esc/)
- [Resource management with Pulumi IaC](/docs/iac/concepts/resources/)
- [Introducing `pulumi do`](/blog/pulumi-do-direct-resource-operations/) (blog post)
