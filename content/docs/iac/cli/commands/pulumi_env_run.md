---
title: "pulumi env run"
aliases:
  - /docs/reference/cli/pulumi_env_run/
---



Open the environment with the given name and run a command.

## Synopsis

Open the environment with the given name and run a command

This command opens the environment with the given name and runs the given command.
If the opened environment contains a top-level 'environmentVariables' object, each
key-value pair in the object is made available to the command as an environment
variable. Note that commands are not run in a subshell, so environment variable
references in the command are not expanded by default. You should invoke the command
inside a shell if you need environment variable expansion:

    run <environment-name> -- bash -c '"echo $MY_ENV_VAR"'

The command to run is assumed to be non-interactive by default and its output
streams are filtered to remove any secret values. Use the -i flag to run interactive
commands, which will disable filtering.

It is not strictly required that you pass `--`. The `--` indicates that any
arguments that follow it should be treated as positional arguments instead of flags.
It is only required if the arguments to the command you would like to run include
flags of the form `--flag` or `-f`.


```
pulumi env run [<org-name>/][<project-name>/]<environment-name> [flags] [--] [command]
```

## Options

```
  -h, --help                help for run
  -i, --interactive         true to treat the command as interactive and disable output filters
  -l, --lifetime duration   the lifetime of the opened environment (default 2h0m0s)
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
