---
title: ESC CLI
title_tag: Pulumi ESC CLI Overview
meta_desc: An overview of the Pulumi ESC (Environments, Secrets, and Configuration) CLI.
h1: Pulumi ESC CLI overview
no_on_this_page: true
menu:
  esc:
    parent: esc-home
    identifier: esc-cli-overview
    weight: 7
aliases:
    - /docs/esc-cli/
---

Pulumi ESC is controlled primarily using the command line interface (CLI). It works in conjunction with the Pulumi Cloud
to help your team manage environment complexity.

## Installation

The Pulumi ESC CLI is open source and free to use:

<a class="btn btn-secondary" href="/docs/esc/download-install/">Install Pulumi ESC</a>

## Common Commands

The most common commands in the CLI that you'll be using are as follows:

* [esc env](/docs/esc/cli/commands/esc_env/) - Manage environments
* [esc env diff](/docs/esc/cli/commands/esc_env_diff/) - Show the difference between versions of an environment
* [esc env edit](/docs/esc/cli/commands/esc_env_edit/) - Edit an environment definition
* [esc env get](/docs/esc/cli/commands/esc_env_get/) - Get a value within an environment
* [esc env init](/docs/esc/cli/commands/esc_env_init/) - Create an empty environment with the given name
* [esc env ls](/docs/esc/cli/commands/esc_env_ls/) - List environments
* [esc env version rollback](/docs/esc/cli/commands/esc_env_rollback/) - Rollback environment definition to a specific version
* [esc env rm](/docs/esc/cli/commands/esc_env_rm/) - Remove an environment or a value from an environment
* [esc env set](/docs/esc/cli/commands/esc_env_set/) - Set a value within an environment
* [esc env version](/docs/esc/cli/commands/esc_env_version/) - Manage the versions of an environment
* [esc env version rollback](/docs/esc/cli/commands/esc_env_rollback/) - Rollback environment definition to a specific version
* [esc env version tag](/docs/esc/cli/commands/esc_env_version_tag/) - Manage tagged versions
* [esc login](/docs/esc/cli/commands/esc_login/) - Log in to the Pulumi Cloud
* [esc open](/docs/esc/cli/commands/esc_open/) - Open the environment with the given name
* [esc run](/docs/esc/cli/commands/esc_run/) - Open the environment with the given name and run a command
* [esc version](/docs/esc/cli/commands/esc_version/) - Print esc's version number

To see a full list of Pulumi ESC CLI commands, you can run the following command:

```bash
esc --help
```

For more detailed help on a specific command, you can append `--help` to any command.
