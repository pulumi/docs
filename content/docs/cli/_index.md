---
title_tag: "Pulumi CLI Overview"
meta_desc: An overview of the Pulumi CLI and common commands used to deploy cloud applications.
title: Pulumi CLI
h1: Pulumi CLI overview
no_on_this_page: true
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cli:
    name: Overview
    weight: 3
aliases:
- /docs/reference/commands/
- /docs/tour/basics-deploying/
- /docs/tour/basics-destroying/
- /docs/tour/basics-previewing/
- /docs/tour/basics-up/
- /docs/tour/basics-updating/
- /docs/reference/cli/
---

Pulumi is controlled primarily using the command line interface (CLI). It works in conjunction with the Pulumi Cloud
to deploy changes to your cloud apps and infrastructure. It keeps a history of who updated what in your team and when.
This CLI has been designed for great inner loop productivity, in addition to
[continuous integration and delivery](/docs/using-pulumi/continuous-delivery/) scenarios.

## Installation

The Pulumi CLI is open source and free to use:

<a class="btn btn-secondary" href="/docs/get-started/install">Install Pulumi</a>

## Common Commands

The most common commands in the CLI that you'll be using are as follows:

* [`pulumi new`](/docs/cli/commands/pulumi_new/): creates a new project using a template
* [`pulumi stack`](/docs/cli/commands/pulumi_stack/): manage your stacks (at least one is required to perform an update)
* [`pulumi config`](/docs/cli/commands/pulumi_config/): configure variables such as keys, regions, and so on
* [`pulumi up`](/docs/cli/commands/pulumi_up/): preview and deploy changes to your program and/or infrastructure
* [`pulumi preview`](/docs/cli/commands/pulumi_preview/): preview your changes explicitly before deploying
* [`pulumi destroy`](/docs/cli/commands/pulumi_destroy/): destroy your program and its infrastructure when you're done

## Complete Reference

Below is the complete documentation for all available commands:

{{< pulumi-command >}}

## Environment Variables

For a list of environment variables that you can use to work with the Pulumi CLI, see [Environment Variables](/docs/cli/environment-variables/).
