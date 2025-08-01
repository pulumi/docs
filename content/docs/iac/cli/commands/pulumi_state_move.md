---
title: "pulumi state move"
aliases:
  - /docs/reference/cli/pulumi_state_move/
---



Move resources from one stack to another

## Synopsis

Move resources from one stack to another

This command can be used to move resources from one stack to another. This can be useful when
splitting a stack into multiple stacks or when merging multiple stacks into one.


```
pulumi state move [flags] <urn>...
```

## Options

```
      --dest string       The name of the stack to move resources to
  -h, --help              help for move
      --include-parents   Include all the parents of the moved resources as well
      --source string     The name of the stack to move resources from
  -y, --yes               Automatically approve and perform the move
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
