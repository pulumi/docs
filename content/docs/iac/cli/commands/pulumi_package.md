---
title: "pulumi package"
aliases:
  - /docs/reference/cli/pulumi_package/
---



Work with Pulumi packages

## Synopsis

Work with Pulumi packages

Install and configure Pulumi packages and their plugins and SDKs.

## Options

```
  -h, --help   help for package
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
      --profiling string             Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}', respectively
      --tracing file:                Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file
  -v, --verbose int                  Enable verbose logging (e.g., v=3); anything >3 is very verbose
```

## SEE ALSO

* [pulumi](/docs/iac/cli/commands/pulumi/)	 - Pulumi command line
* [pulumi package add](/docs/iac/cli/commands/pulumi_package_add/)	 - Add a package to your Pulumi project
* [pulumi package gen-sdk](/docs/iac/cli/commands/pulumi_package_gen-sdk/)	 - Generate SDK(s) from a package or schema
* [pulumi package get-mapping](/docs/iac/cli/commands/pulumi_package_get-mapping/)	 - Get the mapping information for a given key from a package
* [pulumi package get-schema](/docs/iac/cli/commands/pulumi_package_get-schema/)	 - Get the schema.json from a package
* [pulumi package info](/docs/iac/cli/commands/pulumi_package_info/)	 - Show information about a package
* [pulumi package publish](/docs/iac/cli/commands/pulumi_package_publish/)	 - Publish a package to the Pulumi Registry

###### Auto generated by spf13/cobra on 31-Jul-2025
