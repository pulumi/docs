---
title: Configuring
---

Most of us will start out by setting configuration values for _other_ packages, using `pulumi config`,
rather than defining your own.

Each configuration setting inside of a stack has a key and a value.  We will interact with settings using the keys.

Remember that configuration variables are scoped to packages.  As a result, all keys are of the form
`<PACKAGE>:<NAME>`.  For instance, the `aws` package's `region` variable has `aws:region` as its key.

The [`pulumi config`](/reference/cli/pulumi_config.html) family of commands manage a stack's configuration.

To set a variable in the current stack, use the `set` subcommand:

```bash
$ pulumi config set aws:region us-west-2
```

To retrieve a variable's current value, use the `get` subcommand:

```bash
$ pulumi config get aws:config
us-west-2
```

To list all of a stack's current settings, just run `pulumi config`:

```bash
$ pulumi config
KEY                                        VALUE
aws:region                                 us-west-2
ahoy-pulumi:replicaCount                   8
```

Finally, to remove a variable's value altogether, use the `rm` subcommand:

```bash
$ pulumi config rm aws:config
```

We're almost done with this section.  Before wrapping up, let's see how templates can make everything just a little
easier.

<div class="tour-nav">
    <a class="tour-button enabled" href="basics-configuration.html" title="Configuration">◀</a>
    <span class="tour-index"><strong>8</strong>/9</span>
    <a class="tour-button enabled" href="basics-templates.html" title="Templates">▶</a>
</div>
