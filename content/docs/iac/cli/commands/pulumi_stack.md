---
title: "pulumi stack"
aliases:
  - /docs/reference/cli/pulumi_stack/
---



Manage stacks and view stack state

## Synopsis

Manage stacks and view stack state

A stack is a named update target, and a single project may have many of them.
Each stack has a configuration and update history associated with it, stored in
the workspace, in addition to a full checkpoint of the last known good update.


```
pulumi stack [flags]
```

## Options

```
  -h, --help           help for stack
  -i, --show-ids       Display each resource's provider-assigned unique ID
      --show-name      Display only the stack name
      --show-secrets   Display stack outputs which are marked as secret in plaintext
  -u, --show-urns      Display each resource's Pulumi-assigned globally unique URN
  -s, --stack string   The name of the stack to operate on. Defaults to the current stack
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
* [pulumi stack change-secrets-provider](/docs/iac/cli/commands/pulumi_stack_change-secrets-provider/)	 - Change the secrets provider for a stack
* [pulumi stack export](/docs/iac/cli/commands/pulumi_stack_export/)	 - Export a stack's deployment to standard out
* [pulumi stack graph](/docs/iac/cli/commands/pulumi_stack_graph/)	 - Export a stack's dependency graph to a file
* [pulumi stack history](/docs/iac/cli/commands/pulumi_stack_history/)	 - Display history for a stack
* [pulumi stack import](/docs/iac/cli/commands/pulumi_stack_import/)	 - Import a deployment from standard in into an existing stack
* [pulumi stack init](/docs/iac/cli/commands/pulumi_stack_init/)	 - Create an empty stack with the given name, ready for updates
* [pulumi stack ls](/docs/iac/cli/commands/pulumi_stack_ls/)	 - List stacks
* [pulumi stack output](/docs/iac/cli/commands/pulumi_stack_output/)	 - Show a stack's output properties
* [pulumi stack rename](/docs/iac/cli/commands/pulumi_stack_rename/)	 - Rename an existing stack
* [pulumi stack rm](/docs/iac/cli/commands/pulumi_stack_rm/)	 - Remove a stack and its configuration
* [pulumi stack select](/docs/iac/cli/commands/pulumi_stack_select/)	 - Switch the current workspace to the given stack
* [pulumi stack tag](/docs/iac/cli/commands/pulumi_stack_tag/)	 - Manage stack tags
* [pulumi stack unselect](/docs/iac/cli/commands/pulumi_stack_unselect/)	 - Resets stack selection from the current workspace

###### Auto generated by spf13/cobra on 31-Jul-2025
