---
# This file is auto-generated from github.com/pulumi/pulumi/v3/pkg/cmd/pulumi/markdown
title: "pulumi delivery register | CLI commands"
aliases:
  - /docs/reference/cli/pulumi_delivery_register/
meta_desc: "Reference for the pulumi delivery register command: [PREVIEW] Register the Pulumi Delivery pipeline that a program declares."
---



[PREVIEW] Register the Pulumi Delivery pipeline that a program declares

## Synopsis

[PREVIEW] Register the Pulumi Delivery pipeline that the program on this stack declares.

This command registers the pipeline by running the Pulumi program and observing the pipeline
resources that it allocates. It stores them in Pulumi Cloud as the pipeline definition and
starts no run.

The pipeline needs to know where its program lives. When the stack configuration has no
`delivery:source` value, this command detects the repository URL and the project directory
from the git checkout, and writes them to the stack configuration file. Commit that file so
that runs can find the program. The pipeline tracks the default branch of the repository; set
`delivery:source.branch` to track another branch.

```
pulumi delivery register [flags]
```

## Options

```
      --attach-debugger stringArray[=program]   Enable the ability to attach a debugger to the program and source based plugins being executed. Can limit debug type to 'program', 'plugins', 'plugin:<name>' or 'all'.
  -c, --config stringArray                      Config to use during the update and save to the stack config file
      --config-file string                      Use the configuration values in the specified file rather than detecting the file name
      --config-path                             Config keys contain a path to a property in a map or list to set
      --continue-on-error                       Continue updating resources even if an error is encountered (can also be set with PULUMI_CONTINUE_ON_ERROR environment variable)
  -d, --debug                                   Print detailed debugging output during resource operations
      --diff                                    Display operation as a rich diff showing the overall change
      --exclude stringArray                     Specify a resource URN to ignore. These resources will not be updated. Multiple resources can be specified using --exclude urn1 --exclude urn2. Wildcards (*, **) are also supported
      --exclude-dependents                      Allows ignoring of dependent targets discovered but not specified in --exclude list
      --expect-no-changes                       Return an error if any changes occur during this update. This check happens after the update is applied
  -h, --help                                    help for register
      --ignore-protect                          Ignore the protect resource option for this operation, allowing protected resources to be deleted or replaced. Use with caution: deleted resources cannot be recovered
  -j, --json                                    Serialize the update diffs, operations, and overall output as JSON
  -m, --message string                          Optional message to associate with the update operation
      --neo                                     Enable Pulumi Neo's assistance for improved CLI experience and insights (can also be set with PULUMI_NEO environment variable)
      --neo-task-on-failure                     Start a Neo task to help debug errors that occur during the operation
      --override-env stringArray                [EXPERIMENTAL] Override an imported environment for this run only, as <env>=<replacement>; repeatable
  -p, --parallel int32                          Allow P resource operations to run in parallel at once (1 for no parallelism). (default 16)
      --policy-pack strings                     Run one or more policy packs as part of this update
      --policy-pack-config strings              Path to JSON file containing the config for the policy pack of the corresponding "--policy-pack" flag
  -r, --refresh string[="true"]                 Refresh the state of the stack's resources before this update
      --replace stringArray                     Specify a single resource URN to replace. Multiple resources can be specified using --replace urn1 --replace urn2. Wildcards (*, **) are also supported
      --run-program                             Run the program to determine up-to-date state for providers to refresh resources, this only applies if --refresh is set
      --secrets-provider string                 The type of the provider that should be used to encrypt and decrypt secrets (possible choices: default, passphrase, awskms, azurekeyvault, gcpkms, hashivault). Only used when creating a new stack from an existing template (default "default")
      --show-config                             Show configuration keys and variables
      --show-full-output                        Display full length of inputs & outputs
      --show-policy-exceptions                  Show each exempted policy violation instead of a summary
      --show-policy-remediations                Show per-resource policy remediation details instead of a summary
      --show-reads                              Show resources that are being read in, alongside those being managed directly in the stack
      --show-replacement-steps                  Show detailed resource replacement creates and deletes instead of a single step
      --show-sames                              Show resources that don't need be updated because they haven't changed, alongside those that do
      --show-secrets                            Show secret outputs in the CLI output
      --skip-config-validation                  Skip validation of stack config values against the project config schema
      --skip-plugin-pre-install                 Skip the up-front provider plugin install step; missing plugins are installed lazily by the engine. When deploying from a template, also skips installing the project's runtime dependencies.
  -f, --skip-preview                            Do not calculate a preview before performing the update
  -s, --stack string                            The name of the stack to operate on. Defaults to the current stack
      --suppress-outputs                        Suppress display of stack outputs (in case they contain sensitive values)
      --suppress-permalink string[="false"]     Suppress display of the state permalink
      --suppress-progress                       Suppress display of periodic progress dots
  -t, --target stringArray                      Specify a single resource URN to update. Other resources will not be updated. Multiple resources can be specified using --target urn1 --target urn2. Wildcards (*, **) are also supported
      --target-dependents                       Allows updating of dependent targets discovered but not specified in --target list
      --target-replace stringArray              Specify a single resource URN to replace. Other resources will not be updated. Shorthand for --target urn --replace urn.
      --urns                                    Display full URNs instead of short resource names
  -y, --yes                                     Automatically approve and perform the update after previewing it
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
      --otel-traces string           Export OpenTelemetry traces to the specified endpoint. Use file:// for local JSON files, grpc:// or https:// for remote collectors
      --profiling string             Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}', respectively
      --tracing file:                Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file
  -v, --verbose int                  Enable verbose logging (e.g., v=3); anything >3 is very verbose
```

## SEE ALSO

* [pulumi delivery](/docs/iac/cli/commands/pulumi_delivery/)	 - [PREVIEW] Manage Pulumi Delivery pipelines on Pulumi Cloud

###### Auto generated by spf13/cobra on 18-Nov-2026
