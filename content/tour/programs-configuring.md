---
title: Configuring your stack
aliases: ["programs-configuring.html"]
expanded_url: /tour/programs/
menu:
  tour:
    parent: programs
    weight: 3
---

Programs and packages use configuration variables for easy per-stack customization.

The [`pulumi config`]({{< relref "/reference/cli/pulumi_config.md" >}}) family of commands manage a stack's configuration.

Each configuration setting inside of a stack has a key and a value.  We will interact with settings using the keys.
These keys include the package name and the variable name, as in `aws:region` which is the `aws` package's `region`.

To set a variable, use the `pulumi config set` command with the key and value:

```bash
$ pulumi config set aws:region us-west-2
```

If the value is sensitive -- like a password or token -- pass `--secret` and it will be encrypted:

```bash
$ pulumi config set ahoy-pulumi:launchDarklyKey a76dFAKEg9321 --secret
```

To retrieve a variable's current value, use the `pulumi config get` subcommand:

```bash
$ pulumi config get aws:region
us-west-2
```

To list all of a stack's current settings, run `pulumi config`:

```bash
$ pulumi config
KEY                                        VALUE
aws:region                                 us-west-2
ahoy-pulumi:launchDarklyKey                [secret]
```

Finally, to remove a variable's value altogether, use the `pulumi config rm` subcommand:

```bash
$ pulumi config rm aws:region
```

***

We've now covered the project-level machinery, so let's dive further into core programming model concepts, beginning
with the most critical program concept of all -- resources.

<div class="tour-nav">
    <a class="tour-button enabled" href="{{< relref "programs-packages.md" >}}" title="Packages">◀</a>
    <span class="tour-index"><strong>4</strong>/8</span>
    <a class="tour-button enabled" href="{{< relref "programs-resources.md" >}}" title="Resources">▶</a>
</div>
