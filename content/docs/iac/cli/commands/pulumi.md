---
title: "pulumi | CLI commands"
aliases:
  - /docs/reference/cli/pulumi/
meta_desc: "Modern Infrastructure as Code. Create, deploy, and manage cloud resources using familiar programming languages."
---



Pulumi command line

## Synopsis

Pulumi - Modern Infrastructure as Code

To begin working with Pulumi, run the `pulumi new` command:

    $ pulumi new

This will prompt you to create a new project for your cloud and language of choice.

The most common commands from there are:

    - pulumi up       : Deploy code and/or resource changes
    - pulumi stack    : Manage instances of your project
    - pulumi config   : Alter your stack's configuration or secrets
    - pulumi destroy  : Tear down your stack's resources entirely

For more information, please visit the project page: https://www.pulumi.com/docs/

## Options

```
      --color string                 Colorize output. Choices are: always, never, raw, auto (default "auto")
  -C, --cwd string                   Run pulumi as if it had been started in another directory
      --disable-integrity-checking   Disable integrity checking of checkpoint files
  -e, --emoji                        Enable emojis in the output
  -Q, --fully-qualify-stack-names    Show fully-qualified stack names
  -h, --help                         help for pulumi
      --logflow                      Flow log settings to child processes (like plugins)
      --logtostderr                  Log to stderr instead of to files
      --memprofilerate int           Enable more precise (and expensive) memory allocation profiles by setting runtime.MemProfileRate
      --non-interactive              Disable interactive mode for all commands
      --profiling string             Emit CPU and memory profiles and an execution trace to '[filename].[pid].{cpu,mem,trace}', respectively
      --tracing file:                Emit tracing to the specified endpoint. Use the file: scheme to write tracing data to a local file
  -v, --verbose int                  Enable verbose logging (e.g., v=3); anything >3 is very verbose
```

## SEE ALSO

* [pulumi about](/docs/iac/cli/commands/pulumi_about/)	 - Print information about the Pulumi environment.
* [pulumi ai](/docs/iac/cli/commands/pulumi_ai/)	 - Basic Pulumi AI CLI commands.
* [pulumi cancel](/docs/iac/cli/commands/pulumi_cancel/)	 - Cancel a stack's currently running update, if any
* [pulumi config](/docs/iac/cli/commands/pulumi_config/)	 - Manage configuration
* [pulumi console](/docs/iac/cli/commands/pulumi_console/)	 - Opens the current stack in the Pulumi Console
* [pulumi convert](/docs/iac/cli/commands/pulumi_convert/)	 - Convert Pulumi programs from a supported source program into other supported languages
* [pulumi destroy](/docs/iac/cli/commands/pulumi_destroy/)	 - Destroy all existing resources in the stack
* [pulumi env](/docs/iac/cli/commands/pulumi_env/)	 - Manage environments
* [pulumi gen-completion](/docs/iac/cli/commands/pulumi_gen-completion/)	 - Generate completion scripts for the Pulumi CLI
* [pulumi import](/docs/iac/cli/commands/pulumi_import/)	 - Import resources into an existing stack
* [pulumi install](/docs/iac/cli/commands/pulumi_install/)	 - Install packages and plugins for the current program or policy pack.
* [pulumi login](/docs/iac/cli/commands/pulumi_login/)	 - Log in to the Pulumi Cloud
* [pulumi logout](/docs/iac/cli/commands/pulumi_logout/)	 - Log out of the Pulumi Cloud
* [pulumi logs](/docs/iac/cli/commands/pulumi_logs/)	 - Show aggregated resource logs for a stack
* [pulumi new](/docs/iac/cli/commands/pulumi_new/)	 - Create a new Pulumi project
* [pulumi org](/docs/iac/cli/commands/pulumi_org/)	 - Manage Organization configuration
* [pulumi package](/docs/iac/cli/commands/pulumi_package/)	 - Work with Pulumi packages
* [pulumi plugin](/docs/iac/cli/commands/pulumi_plugin/)	 - Manage language and resource provider plugins
* [pulumi policy](/docs/iac/cli/commands/pulumi_policy/)	 - Manage resource policies
* [pulumi preview](/docs/iac/cli/commands/pulumi_preview/)	 - Show a preview of updates to a stack's resources
* [pulumi project](/docs/iac/cli/commands/pulumi_project/)	 - Manage Pulumi projects
* [pulumi refresh](/docs/iac/cli/commands/pulumi_refresh/)	 - Refresh the resources in a stack
* [pulumi schema](/docs/iac/cli/commands/pulumi_schema/)	 - Analyze package schemas
* [pulumi stack](/docs/iac/cli/commands/pulumi_stack/)	 - Manage stacks and view stack state
* [pulumi state](/docs/iac/cli/commands/pulumi_state/)	 - Edit the current stack's state
* [pulumi template](/docs/iac/cli/commands/pulumi_template/)	 - Work with Pulumi templates
* [pulumi up](/docs/iac/cli/commands/pulumi_up/)	 - Create or update the resources in a stack
* [pulumi version](/docs/iac/cli/commands/pulumi_version/)	 - Print Pulumi's version number
* [pulumi watch](/docs/iac/cli/commands/pulumi_watch/)	 - Continuously update the resources in a stack
* [pulumi whoami](/docs/iac/cli/commands/pulumi_whoami/)	 - Display the current logged-in user

###### Auto generated by spf13/cobra on 10-Feb-2026
