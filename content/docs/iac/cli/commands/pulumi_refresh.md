---
title: "pulumi refresh | CLI commands"
aliases:
  - /docs/reference/cli/pulumi_refresh/
meta_desc: "Learn about the pulumi refresh command."
---



Refresh the resources in a stack

## Synopsis

Refresh the resources in a stack.

This command compares the current stack's resource state with the state known to exist in
the actual cloud provider. Any such changes are adopted into the current stack. Note that if
the program text isn't updated accordingly, subsequent updates may still appear to be out of
sync with respect to the cloud provider's source of truth.

The program to run is loaded from the project in the current directory. Use the `-C` or
`--cwd` flag to use a different directory.

```
pulumi refresh [url] [flags]
```

## Options

```
      --clear-pending-creates                         Clear all pending creates, dropping them from the state
  -c, --config stringArray                            Config to use during the refresh and save to the stack config file
      --config-file string                            Use the configuration values in the specified file rather than detecting the file name
      --config-path                                   Config keys contain a path to a property in a map or list to set
  -d, --debug                                         Print detailed debugging output during resource operations
      --diff                                          Display operation as a rich diff showing the overall change
  -x, --exclude stringArray                           Specify a resource URN to ignore. These resources will not be refreshed. Multiple resources can be specified using --exclude urn1 --exclude urn2. Wildcards (*, **) are also supported
      --exclude-dependents                            Allows ignoring of dependent targets discovered but not specified in --exclude list
      --expect-no-changes                             Return an error if any changes occur during this refresh. This check happens after the refresh is applied
  -h, --help                                          help for refresh
      --import-pending-creates stringArray            A list of form [[URN ID]...] describing the provider IDs of pending creates
  -j, --json                                          Serialize the refresh diffs, operations, and overall output as JSON
  -m, --message string                                Optional message to associate with the update operation
      --neo                                           Enable Pulumi Neo's assistance for improved CLI experience and insights (can also be set with PULUMI_NEO environment variable)
  -p, --parallel int32                                Allow P resource operations to run in parallel at once (1 for no parallelism). (default 16)
      --preview-only                                  Only show a preview of the refresh, but don't perform the refresh itself
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
      --run-program                                   Run the program to determine up-to-date state for providers to refresh resources
      --show-replacement-steps                        Show detailed resource replacement creates and deletes instead of a single step
      --show-sames                                    Show resources that needn't be updated because they haven't changed, alongside those that do
      --skip-pending-creates                          Skip importing pending creates in interactive mode
  -f, --skip-preview                                  Do not calculate a preview before performing the refresh
  -s, --stack string                                  The name of the stack to operate on. Defaults to the current stack
      --suppress-outputs                              Suppress display of stack outputs (in case they contain sensitive values)
      --suppress-permalink string[="false"]           Suppress display of the state permalink
      --suppress-progress                             Suppress display of periodic progress dots
      --suppress-stream-logs                          [EXPERIMENTAL] Suppress log streaming of the deployment job
  -t, --target stringArray                            Specify a single resource URN to refresh. Multiple resource can be specified using: --target urn1 --target urn2
      --target-dependents                             Allows updating of dependent targets discovered but not specified in --target list
  -y, --yes                                           Automatically approve and perform the refresh after previewing it
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
