---
title: "pulumi env set"
aliases:
  - /docs/reference/cli/pulumi_env_set/
---



Set a value within an environment.

## Synopsis

Set a value within an environment

This command fetches the current definition for the named environment and modifies a
value within it. The path to the value to set is a Pulumi property path. The value
is interpreted as YAML.


```
pulumi env set [<org-name>/][<project-name>/]<environment-name> <path> <value> [flags]
```

## Options

```
  -h, --help        help for set
      --plaintext   true to leave the value in plaintext
      --secret      true to mark the value as secret
      --string      true to treat the value as a string rather than attempting to parse it as YAML
```

## Options inherited from parent commands

```
      --color string                 Colorize output. Choices are: always, never, raw, auto (default "auto")
  -C, --cwd string                   Run pulumi as if it had been started in another directory
      --disable-integrity-checking   Disable integrity checking of checkpoint files
  -e, --emoji                        Enable emojis in the output
      --env string                   The name of the environment to operate on.
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

* [pulumi env](/docs/iac/cli/commands/pulumi_env/)	 - Manage environments

###### Auto generated by spf13/cobra on 31-Jul-2025
