---
title_tag: "Pulumi CLI commands"
meta_desc: The Pulumi CLI offers many commands to execute from your command-line.
title: Commands
h1: Pulumi CLI commands
menu:
  cli:
    weight: 1
    identifier: commands
---

## Common Commands

The most common commands in the CLI that you'll be using are as follows:

* [`pulumi new`](pulumi_new): creates a new project using a template
* [`pulumi stack`](pulumi_stack): manage your stacks (at least one is required to perform an update)
* [`pulumi config`](pulumi_config): configure variables such as keys, regions, and so on
* [`pulumi up`](pulumi_up): preview and deploy changes to your program and/or infrastructure
* [`pulumi preview`](pulumi_preview): preview your changes explicitly before deploying
* [`pulumi destroy`](pulumi_destroy): destroy your program and its infrastructure when you're done

## Complete Reference

Below is the complete documentation for all available commands:

{{< pulumi-command >}}
