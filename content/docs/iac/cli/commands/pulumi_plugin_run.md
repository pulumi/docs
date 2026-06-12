---
# This file is manually maintained. The pulumi plugin run command is hidden from
# the CLI help by default (Hidden: !env.Dev.Value() in pulumi/pulumi) and therefore
# excluded from auto-generation. See https://github.com/pulumi/docs/issues/16749.
title: "pulumi plugin run | CLI commands"
meta_desc: "Learn about the pulumi plugin run command."
---



Run a command on a plugin binary

## Synopsis

[EXPERIMENTAL] Run a command on a plugin binary.

Directly executes a plugin binary. If VERSION is not specified,
the latest installed plugin will be used. If the plugin is not installed,
Pulumi will attempt to install it automatically.

This command is useful for running tool plugins that extend Pulumi's
capabilities, such as migration tools. For example:

```
pulumi plugin run <name-or-path[@version]> [-- <args...>] [flags]
```

## Examples

Run the `cdk2pulumi` tool plugin:

```bash
pulumi plugin install tool cdk2pulumi
pulumi plugin run cdk2pulumi -- --assembly cdk.out --stacks MyStack
```

Run the `terraform-migrate` tool plugin:

```bash
pulumi plugin install tool terraform-migrate
pulumi plugin run terraform-migrate -- stack --from path/to/terraform --to path/to/pulumi
```

## Options

```
  -h, --help          help for run
      --kind string   The plugin kind (default "tool")
```

## Options inherited from parent commands

```
      --color string                 Colorize output. Choices are: always, never, raw, auto (default "auto")
  -C, --cwd string                   Run pulumi as if it had been started in another directory
      --disable-integrity-checking   Disable integrity checking of checkpoint files
  -e, --emoji                        Enable emojis in the output
  -Q, --fully-qualify-stack-names    Show fully-qualified stack names
      --logflow                      Flow log settings to child processes (like plugins)
      --logtostderr                  Log to stderr instead of to files
      --memprofilerate int           Enable more precise (and expensive) memory allocation profiles by setting runtime.MemProfileRate
      --non-interactive              Disable interactive mode for all commands
      --otel-traces string           Export OpenTelemetry traces to the specified endpoint. Use file:// for local JSON files, grpc:// for remote collectors
      --profiling string             Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}', respectively
      --tracing file:                Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file
  -v, --verbose int                  Enable verbose logging (e.g., v=3); anything >3 is very verbose
```

## SEE ALSO

* [pulumi plugin](/docs/iac/cli/commands/pulumi_plugin/)	 - Manage language and resource provider plugins
* [pulumi plugin install](/docs/iac/cli/commands/pulumi_plugin_install/)	 - Install one or more plugins
