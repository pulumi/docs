---
title: "Commands (CLI)"
---

Pulumi is controlled primarily using the command line interface (CLI).  The Pulumi service works in conjunction with
the CLI to carry out tasks such as deploying updates to your cloud program and infrastructure, and keeping a history
of who updated what in your team and when.  This CLI has been designed to work well in unattended scenarios, such as
in [continuous integration and deployment](./cd.html), and communicates all errors properly using non-zero exit codes.

The most common commands in the CLI that you'll be using are as follows:

* [`pulumi new`](./cli/pulumi_new.html): creates a new project using a template
* [`pulumi stack`](./cli/pulumi_stack.html): manage your stacks (at least one is required to perform an update)
* [`pulumi config`](./cli/pulumi_config.html): configure variables such as keys, regions, and so on
* [`pulumi update`](./cli/pulumi_update.html): preview and deploy changes to your program and/or infrastructure
* [`pulumi destroy`](./cli/pulumi_destroy.html): destroy your program and its infrastructure when you're done

Below is the complete documentation for all available commands:

{% include_relative cli/pulumi.md %}
