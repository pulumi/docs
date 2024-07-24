---
title_tag: "Inspecting Infrastructure | Tutorials"
meta_desc: Learn how to inspect your Pulumi resources in this tutorial.
title: "Inspecting Infrastructure"
h1: "Inspecting Infrastructure"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  usingpulumi:
    identifier: inspecting-infrastructure
    weight: 1
tags:
    - resources
    - infrastructure
    - fundamentals
    - tutorial
---

Pulumi configurations and state data include highly structured information about the resources they manage, such as dependency information, [outputs](/docs/concepts/inputs-outputs/#outputs), and more.

The Pulumi CLI includes some commands for inspecting this data. You can use these to integrate other tools with Pulumi's infrastructure data, or just to gain a deeper or more holistic understanding of your infrastructure.

- [pulumi stack](/docs/cli/commands/pulumi_stack/) - This command lists the management details, resources, and output names and values of the current stack.

- [pulumi stack graph](/docs/cli/commands/pulumi_stack_graph/) - This command can be used to export a stack’s dependency graph to a file.

- [pulumi stack output](/docs/cli/commands/pulumi_stack_output/) - This command lists all output names and values that are exported from a stack. If a specific property-name is supplied, just that property’s value is shown.

- [pulumi stack export](/docs/cli/commands/pulumi_stack_export/) - This command generates a human readable version of the state file to standard out.

- [pulumi preview](/docs/cli/commands/pulumi_preview/) - This command displays a preview of the updates to an existing stack whose state is represented by an existing state file.

- [pulumi console](/docs/cli/commands/pulumi_console/) - This command opens the current stack in the Pulumi Console. From there, you can view detailed information about the stack such as its resources, outputs, and configuration values.
