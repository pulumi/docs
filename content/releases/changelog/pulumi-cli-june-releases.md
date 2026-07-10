---
title: "CLI and SDK rollup: New commands, richer output, and more"
date: 2026-06-24
meta_desc: Our slate of June releases adds new Pulumi commands, improvements to developer and agent UX, and richer, more structured CLI output.
---

We shipped many new features and fixes in the Pulumi CLI and SDK this month. A few highlights:

* New subcommands for [`pulumi logs`](/docs/iac/cli/commands/pulumi_logs/), including [`list`](/docs/iac/cli/commands/pulumi_logs_list/) and [`remove`](/docs/iac/cli/commands/pulumi_logs_remove/) ([v3.246](https://github.com/pulumi/pulumi/releases/tag/v3.246.0))
* More output formats (e.g., JSON) for [`pulumi about`](/docs/iac/cli/commands/pulumi_about/) and [`pulumi whoami`](/docs/iac/cli/commands/pulumi_whoami/) ([v3.248](https://github.com/pulumi/pulumi/releases/tag/v3.248.0))
* Additional resource details (URN, name, type, parent) in the JSON-formatted output of Pulumi operations ([v3.246](https://github.com/pulumi/pulumi/releases/tag/v3.246.0))
* Renamed `pulumi stack init` to [`pulumi stack new`](/docs/iac/cli/commands/pulumi_stack_new/), with `init` aliased for compatibility ([v3.245](https://github.com/pulumi/pulumi/releases/tag/v3.245.0))
* Richer [`pulumi do`](/blog/pulumi-do-direct-resource-operations/) and [`pulumi neo`](/blog/pulumi-neo-cli/) interactions and workflows ([v3.245](https://github.com/pulumi/pulumi/releases/tag/v3.245.0), [v3.246](https://github.com/pulumi/pulumi/releases/tag/v3.246.0), [v3.247](https://github.com/pulumi/pulumi/releases/tag/v3.247.0))

... and lots more. See the [Releases page on GitHub](https://github.com/pulumi/pulumi/releases) for details.
