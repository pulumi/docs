---
title: "pulumi state upgrade"
aliases:
  - /docs/reference/cli/pulumi_state_upgrade/
---



Migrates the current backend to the latest supported version

## Synopsis

Migrates the current backend to the latest supported version

This only has an effect on DIY backends.


```
pulumi state upgrade [flags]
```

## Options

```
  -h, --help   help for upgrade
  -y, --yes    Automatically approve and perform the upgrade
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

* [pulumi state](/docs/iac/cli/commands/pulumi_state/)	 - Edit the current stack's state

###### Auto generated by spf13/cobra on 31-Jul-2025
