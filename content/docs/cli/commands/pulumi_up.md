---
title: "pulumi up"
aliases:
  - /docs/reference/cli/pulumi_up/
---



Create or update the resources in a stack

## Synopsis

Create or update the resources in a stack.

This command creates or updates resources in a stack. The new desired goal state for the target stack
is computed by running the current Pulumi program and observing all resource allocations to produce a
resource graph. This goal state is then compared against the existing state to determine what create,
read, update, and/or delete operations must take place to achieve the desired goal state, in the most
minimally disruptive way. This command records a full transactional snapshot of the stack's new state
afterwards so that the stack may be updated incrementally again later on.

The program to run is loaded from the project in the current directory by default. Use the `-C` or
`--cwd` flag to use a different directory.

```
pulumi up [template|url] [flags]
```

## Options

```
  -c, --config stringArray                    Config to use during the update and save to the stack config file
      --config-file string                    Use the configuration values in the specified file rather than detecting the file name
      --config-path                           Config keys contain a path to a property in a map or list to set
      --continue-on-error                     Continue updating resources even if an error is encountered (can also be set with PULUMI_CONTINUE_ON_ERROR environment variable)
  -d, --debug                                 Print detailed debugging output during resource operations
      --diff                                  Display operation as a rich diff showing the overall change
      --expect-no-changes                     Return an error if any changes occur during this update
  -h, --help                                  help for up
  -j, --json                                  Serialize the update diffs, operations, and overall output as JSON
  -m, --message string                        Optional message to associate with the update operation
  -p, --parallel int                          Allow P resource operations to run in parallel at once (1 for no parallelism). (default 16)
      --policy-pack strings                   Run one or more policy packs as part of this update
      --policy-pack-config strings            Path to JSON file containing the config for the policy pack of the corresponding "--policy-pack" flag
  -r, --refresh string[="true"]               Refresh the state of the stack's resources before this update
      --replace stringArray                   Specify a single resource URN to replace. Multiple resources can be specified using --replace urn1 --replace urn2. Wildcards (*, **) are also supported
      --secrets-provider string               The type of the provider that should be used to encrypt and decrypt secrets (possible choices: default, passphrase, awskms, azurekeyvault, gcpkms, hashivault). Only used when creating a new stack from an existing template (default "default")
      --show-config                           Show configuration keys and variables
      --show-full-output                      Display full length of stack outputs (default true)
      --show-policy-remediations              Show per-resource policy remediation details instead of a summary
      --show-reads                            Show resources that are being read in, alongside those being managed directly in the stack
      --show-replacement-steps                Show detailed resource replacement creates and deletes instead of a single step
      --show-sames                            Show resources that don't need be updated because they haven't changed, alongside those that do
  -f, --skip-preview                          Do not calculate a preview before performing the update
  -s, --stack string                          The name of the stack to operate on. Defaults to the current stack
      --suppress-outputs                      Suppress display of stack outputs (in case they contain sensitive values)
      --suppress-permalink string[="false"]   Suppress display of the state permalink
      --suppress-progress                     Suppress display of periodic progress dots
  -t, --target stringArray                    Specify a single resource URN to update. Other resources will not be updated. Multiple resources can be specified using --target urn1 --target urn2. Wildcards (*, **) are also supported
      --target-dependents                     Allows updating of dependent targets discovered but not specified in --target list
      --target-replace stringArray            Specify a single resource URN to replace. Other resources will not be updated. Shorthand for --target urn --replace urn.
  -y, --yes                                   Automatically approve and perform the update after previewing it
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

* [pulumi](/docs/cli/commands/pulumi/)	 - Pulumi command line

###### Auto generated by spf13/cobra on 23-Aug-2024
