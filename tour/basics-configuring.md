---
title: Configuring
---

Most of us will start out by setting configuration values for _other_ packages, using `pulumi config`,
rather than defining your own.

The [`pulumi config`](/reference/cli/pulumi_config.html) family of commands manage a stack's configuration.

Each configuration setting inside of a stack has a key and a value.  We will interact with settings using the keys.

To set a variable, use the `set` command with the key and value:

```bash
$ pulumi config set aws:region us-west-2
```

If the value is sensitive -- like a password or token -- pass `--secret` and it will be encrypted:

```bash
$ pulumi config set ahoy-pulumi:launchDarklyKey a76db238fg9321 --secret
```

To retrieve a variable's current value, use the `get` subcommand:

```bash
$ pulumi config get aws:config
us-west-2
```

Or to list all of a stack's current settings, run `pulumi config`:

```bash
$ pulumi config
KEY                                        VALUE
aws:region                                 us-west-2
ahoy-pulumi:launchDarklyKey                [secret]
```

Finally, to remove a variable's value altogether, use the `rm` subcommand:

```bash
$ pulumi config rm aws:config
```

We're almost done with the basics.  Before wrapping up, let's see how templates can make everything just a little
easier.

<div class="tour-nav">
    <a class="tour-button enabled" href="basics-configuration.html" title="Configuration">◀</a>
    <span class="tour-index"><strong>8</strong>/9</span>
    <a class="tour-button enabled" href="basics-templates.html" title="Templates">▶</a>
</div>
