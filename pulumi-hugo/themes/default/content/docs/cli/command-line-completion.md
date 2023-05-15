---
title_tag: "Command-line completion | Pulumi CLI"
meta_desc: Information about command-line completion while using the Pulumi CLI.
title: Command-line completion
h1: Pulumi CLI command-line completion
menu:
  cli:
    weight: 3
---

The Pulumi CLI also has a command to generate a command-line completion script for Bash, Zsh, and Fish. This gives you tab completion for all commands,
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

### Fish

The `pulumi gen-completion fish` command self-generates its own CLI script. You can save the output to a file or use it in the current session:

```shell
pulumi gen-completion fish | source
```

To load the completions for each session, you need to save the completion to a file:

```bash
pulumi gen-completion fish > ~/.config/fish/completions/pulumi.fish
```

Finally, after saving the `pulumi` fish completion script, you need to reopen your terminal for the scripts to take effect.
