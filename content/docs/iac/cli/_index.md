---
title_tag: "Pulumi CLI Overview"
meta_desc: An overview of the Pulumi CLI and common commands used to deploy cloud applications.
title: Pulumi CLI
h1: Pulumi CLI overview
no_on_this_page: true
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  iac:
    name: Pulumi CLI
    weight: 45
    identifier: iac-cli
    parent: iac-home
  reference:
    name: Pulumi CLI
    parent: reference-cli
    weight: 1
aliases:
    - /docs/reference/commands/
    - /docs/tour/basics-deploying/
    - /docs/tour/basics-destroying/
    - /docs/tour/basics-previewing/
    - /docs/tour/basics-up/
    - /docs/tour/basics-updating/
    - /docs/reference/cli/
    - /docs/cli
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

* [`pulumi new`](/docs/iac/cli/commands/pulumi_new/): creates a new project using a template
* [`pulumi stack`](/docs/iac/cli/commands/pulumi_stack/): manage your stacks (at least one is required to perform an update)
* [`pulumi config`](/docs/iac/cli/commands/pulumi_config/): configure variables such as keys, regions, and so on
* [`pulumi up`](/docs/iac/cli/commands/pulumi_up/): preview and deploy changes to your program and/or infrastructure
* [`pulumi preview`](/docs/iac/cli/commands/pulumi_preview/): preview your changes explicitly before deploying
* [`pulumi destroy`](/docs/iac/cli/commands/pulumi_destroy/): destroy your program and its infrastructure when you're done
* [`pulumi api`](/docs/iac/cli/api/): call any [Pulumi Cloud REST API](/docs/reference/cloud-rest-api/) endpoint directly from the CLI, with stable exit codes and a JSON error envelope for scripts and agents

## Complete Reference

For the complete, versioned documentation of every Pulumi CLI command, see the
[CLI command reference](/docs/iac/cli/commands/).

## Environment Variables

For a list of environment variables that you can use to work with the Pulumi CLI, see [Environment variables](/docs/cli/environment-variables/).

## Error and exit codes

To learn how Pulumi maps internal errors to stable CLI exit codes you can use in automation, see [Pulumi CLI exit codes](/docs/iac/cli/exit-codes/).
