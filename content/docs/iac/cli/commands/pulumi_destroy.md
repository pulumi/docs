---
title: "pulumi destroy | CLI commands"
aliases:
  - /docs/reference/cli/pulumi_destroy/
meta_desc: "Delete all resources in a stack. Safely tear down your cloud infrastructure."
---



Destroy all existing resources in the stack

## Synopsis

Destroy all existing resources in the stack, but not the stack itself

Deletes all the resources in the selected stack.  The current state is
loaded from the associated state file in the workspace.  After running to completion,
all of this stack's resources and associated state are deleted.

The stack itself is not deleted. Use `pulumi stack rm` or the 
`--remove` flag to delete the stack and its config file.

Warning: this command is generally irreversible and should be used with great care.

```
pulumi destroy [url] [flags]
```

## Options

```
  -c, --config stringArray                            Config to use during the destroy and save to the stack config file
      --config-file string                            Use the configuration values in the specified file rather than detecting the file name
      --config-path                                   Config keys contain a path to a property in a map or list to set
      --continue-on-error                             Continue to perform the destroy operation despite the occurrence of errors (can also be set with PULUMI_CONTINUE_ON_ERROR env var)
  -d, --debug                                         Print detailed debugging output during resource operations
      --diff                                          Display operation as a rich diff showing the overall change
  -x, --exclude stringArray                           Specify a resource URN to ignore. These resources will not be updated. Multiple resources can be specified using --exclude urn1 --exclude urn2. Wildcards (*, **) are also supported
      --exclude-protected                             Do not destroy protected resources. Destroy all other resources.
  -h, --help                                          help for destroy
  -j, --json                                          Serialize the destroy diffs, operations, and overall output as JSON
  -m, --message string                                Optional message to associate with the destroy operation
      --neo                                           Enable Pulumi Neo's assistance for improved CLI experience and insights (can also be set with PULUMI_NEO environment variable)
  -p, --parallel int32                                Allow P resource operations to run in parallel at once (1 for no parallelism). (default 16)
      --preview-only                                  Only show a preview of the destroy, but don't perform the destroy itself
  -r, --refresh string[="true"]                       Refresh the state of the stack's resources before this update
      --remote                                        [EXPERIMENTAL] Run the operation remotely
      --remote-agent-pool-id string                   [EXPERIMENTAL] The agent pool to use to run the deployment job. When empty, the Pulumi Cloud shared queue will be used.
      --remote-env --remote-env FOO=bar               [EXPERIMENTAL] Environment variables to use in the remote operation of the form NAME=value (e.g. --remote-env FOO=bar)
      --remote-env-secret --remote-env FOO=secret     [EXPERIMENTAL] Environment variables with secret values to use in the remote operation of the form NAME=secretvalue (e.g. --remote-env FOO=secret)
      --remote-executor-image string                  [EXPERIMENTAL] The Docker image to use for the executor
      --remote-executor-image-password string         [EXPERIMENTAL] The password for the credentials with access to the Docker image to use for the executor
      --remote-executor-image-username string         [EXPERIMENTAL] The username for the credentials with access to the Docker image to use for the executor
      --remote-git-auth-access-token string           [EXPERIMENTAL] Git personal access token
      --remote-git-auth-password string               [EXPERIMENTAL] Git password; for use with username or with an SSH private key
      --remote-git-auth-ssh-private-key string        [EXPERIMENTAL] Git SSH private key; use --remote-git-auth-password for the password, if needed
      --remote-git-auth-ssh-private-key-path string   [EXPERIMENTAL] Git SSH private key path; use --remote-git-auth-password for the password, if needed
      --remote-git-auth-username string               [EXPERIMENTAL] Git username
      --remote-git-branch string                      [EXPERIMENTAL] Git branch to deploy; this is mutually exclusive with --remote-git-commit; either value needs to be specified
      --remote-git-commit string                      [EXPERIMENTAL] Git commit hash of the commit to deploy (if used, HEAD will be in detached mode); this is mutually exclusive with --remote-git-branch; either value needs to be specified
      --remote-git-repo-dir string                    [EXPERIMENTAL] The directory to work from in the project's source repository where Pulumi.yaml is located; used when Pulumi.yaml is not in the project source root
      --remote-inherit-settings                       [EXPERIMENTAL] Inherit deployment settings from the current stack
      --remote-pre-run-command stringArray            [EXPERIMENTAL] Commands to run before the remote operation
      --remote-skip-install-dependencies              [EXPERIMENTAL] Whether to skip the default dependency installation step
      --remove                                        Remove the stack and its config file after all resources in the stack have been deleted
      --run-program                                   Run the program to determine up-to-date state for providers to destroy resources
      --show-config                                   Show configuration keys and variables
      --show-full-output                              Display full length of inputs & outputs
      --show-replacement-steps                        Show detailed resource replacement creates and deletes instead of a single step
      --show-sames                                    Show resources that don't need to be updated because they haven't changed, alongside those that do
  -f, --skip-preview                                  Do not calculate a preview before performing the destroy
  -s, --stack string                                  The name of the stack to operate on. Defaults to the current stack
      --suppress-outputs                              Suppress display of stack outputs (in case they contain sensitive values)
      --suppress-permalink string[="false"]           Suppress display of the state permalink
      --suppress-progress                             Suppress display of periodic progress dots
      --suppress-stream-logs                          [EXPERIMENTAL] Suppress log streaming of the deployment job
  -t, --target stringArray                            Specify a single resource URN to destroy. All resources necessary to destroy this target will also be destroyed. Multiple resources can be specified using: --target urn1 --target urn2. Wildcards (*, **) are also supported
      --target-dependents                             Allows destroying of dependent targets discovered but not specified in --target list
  -y, --yes                                           Automatically approve and perform the destroy after previewing it
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

###### Auto generated by spf13/cobra on 10-Feb-2026
