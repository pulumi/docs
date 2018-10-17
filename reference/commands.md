---
title: "Commands (CLI)"
---

Pulumi is controlled primarily using the command line interface (CLI).  The Pulumi service works in conjunction with
the CLI to carry out tasks such as deploying updates to your cloud program and infrastructure, and keeping a history
of who updated what in your team and when.  This CLI has been designed to work well in unattended scenarios, such as
in [continuous integration and deployment](cd.html), and communicates all errors properly using non-zero exit codes.

## Common Commands

The most common commands in the CLI that you'll be using are as follows:

* [`pulumi new`](./cli/pulumi_new.html): creates a new project using a template
* [`pulumi stack`](./cli/pulumi_stack.html): manage your stacks (at least one is required to perform an update)
* [`pulumi config`](./cli/pulumi_config.html): configure variables such as keys, regions, and so on
* [`pulumi up`](./cli/pulumi_up.html): preview and deploy changes to your program and/or infrastructure
* [`pulumi preview`](./cli/pulumi_preview.html): preview your changes explicitly before deploying
* [`pulumi destroy`](./cli/pulumi_destroy.html): destroy your program and its infrastructure when you're done

## Complete Reference

Below is the complete documentation for all available commands:

{% capture pulumi_cli %}{% include_relative cli/pulumi.md %}{% endcapture %}
{{ pulumi_cli | markdownify | replace_regex: 'pulumi_(.*)\.md', './cli/pulumi_\1.html' }}

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

Make sure compinit is loaded or do it by adding in ~/.zshrc:

```shell
autoload -Uz compinit && compinit -i
```

Then reload your shell:

```shell
exec $SHELL -l
```