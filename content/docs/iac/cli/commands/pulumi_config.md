---
title: "pulumi config"
aliases:
  - /docs/reference/cli/pulumi_config/
---



Manage configuration

## Synopsis

Lists all configuration values for a specific stack. To add a new configuration value, run
`pulumi config set`. To remove an existing value run `pulumi config rm`. To get the value of
for a specific configuration key, use `pulumi config get <key-name>`.

```
pulumi config [flags]
```

## Options

```
      --config-file string   Use the configuration values in the specified file rather than detecting the file name
  -h, --help                 help for config
  -j, --json                 Emit output as JSON
      --open                 Open and resolve any environments listed in the stack configuration. Defaults to true if --show-secrets is set, false otherwise
      --show-secrets         Show secret values when listing config instead of displaying blinded values
  -s, --stack string         The name of the stack to operate on. Defaults to the current stack
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
* [pulumi config cp](/docs/iac/cli/commands/pulumi_config_cp/)	 - Copy config to another stack
* [pulumi config env](/docs/iac/cli/commands/pulumi_config_env/)	 - Manage ESC environments for a stack
* [pulumi config get](/docs/iac/cli/commands/pulumi_config_get/)	 - Get a single configuration value
* [pulumi config refresh](/docs/iac/cli/commands/pulumi_config_refresh/)	 - Update the local configuration based on the most recent deployment of the stack
* [pulumi config rm](/docs/iac/cli/commands/pulumi_config_rm/)	 - Remove configuration value
* [pulumi config rm-all](/docs/iac/cli/commands/pulumi_config_rm-all/)	 - Remove multiple configuration values
* [pulumi config set](/docs/iac/cli/commands/pulumi_config_set/)	 - Set configuration value
* [pulumi config set-all](/docs/iac/cli/commands/pulumi_config_set-all/)	 - Set multiple configuration values

###### Auto generated by spf13/cobra on 31-Jul-2025
