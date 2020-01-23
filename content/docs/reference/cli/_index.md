---
title: "Pulumi CLI"
meta_desc: An overview of the Pulumi CLI and common commands used to deploy cloud applications.
menu:
  reference:
    identifier: cli
    weight: 3

aliases: [/docs/reference/commands/]
---

Pulumi is controlled primarily using the command line interface (CLI). It works in conjunction with the Pulumi service
to deploy changes to your cloud apps and infrastructure.  It keeps a history of who updated what in your team and when.
This CLI has been designed for great inner loop productivity, in addition to
[continuous integration and delivery]({{< relref "/docs/guides/continuous-delivery" >}}) scenarios.

## Installation

The Pulumi CLI is free to download and install:

<a class="btn" href="{{< relref "/docs/get-started/install" >}}">INSTALL PULUMI</a>

## Common Commands

The most common commands in the CLI that you'll be using are as follows:

* [`pulumi new`]({{< relref "pulumi_new" >}}): creates a new project using a template
* [`pulumi stack`]({{< relref "pulumi_stack" >}}): manage your stacks (at least one is required to perform an update)
* [`pulumi config`]({{< relref "pulumi_config" >}}): configure variables such as keys, regions, and so on
* [`pulumi up`]({{< relref "pulumi_up" >}}): preview and deploy changes to your program and/or infrastructure
* [`pulumi preview`]({{< relref "pulumi_preview" >}}): preview your changes explicitly before deploying
* [`pulumi destroy`]({{< relref "pulumi_destroy" >}}): destroy your program and its infrastructure when you're done

## Environment Variables

For a list of environment variables that you can use to work with the Pulumi CLI, see [Environment Variables]({{< relref "/docs/reference/cli/environment-variables" >}}).

## Complete Reference

Below is the complete documentation for all available commands:

{{< pulumi-command >}}

## Command-line Completion

The Pulumi CLI also has a command to generate a [command-line completion script](
https://en.wikipedia.org/wiki/Command-line_completion) for Bash and Zsh.  This gives you tab completion for all commands,
sub-commands, and flags, which can make it easier to remember what to type and where.

### Bash

To use this, you'll first need to ensure bash completion is installed:

* On most current Linux distros, bash completion should be available.
* On a Mac, install with `brew install bash-completion`.

The `pulumi gen-completion bash` command self-generates its own CLI script. You can save the output to a file.

* On Linux, save to `pulumi gen-completion bash > /etc/bash_completion.d/pulumi`.
* On macOS, save to `pulumi gen-completion bash > /usr/local/etc/bash_completion.d/pulumi`.

Ensure that bash completion is run when you launch a new terminal by adding it to `~/.bash_profile`.

On Linux:

```
if [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
fi
```

On macOS:

```
if [ -f /usr/local/etc/bash_completion ]; then
    . /usr/local/etc/bash_completion
fi
```

Finally, after saving the `pulumi` bash completion script, either reopen your terminal or source your profile
in order to reload the bash completion scripts in your current terminal session (`. ~/.bash_profile`).

### Zsh

The `pulumi gen-completion zsh` command self-generates its own CLI script. You can save the output to a file inside a directory listed in the `$fpath` variable.

You can list your `$fpath` directories and pick one of them:

```shell
echo $fpath
```

You can also use an arbitrary directory like `~/.zsh/completion/` and then add it to your `fpath` in `~/.zshrc` :

```shell
fpath=(~/.zsh/completion $fpath)
```

Make sure `compinit` is loaded or do it by adding in `~/.zshrc`:

```shell
autoload -Uz compinit && compinit -i
```

Then reload your shell:

```shell
exec $SHELL -l
```
