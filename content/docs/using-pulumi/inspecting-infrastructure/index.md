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
    - fundamentals
    - tutorial
---

TBD

[pulumi stack graph](/docs/cli/commands/pulumi_stack_graph/) - This command can be used to view the dependency graph that a Pulumi program emitted when it was run. This graph is output in the DOT format. This command operates on your stack’s most recent deployment.

[pulumi stack]() - This command enables you to manage stacks and view stack state.

[pulumi stack output](/docs/cli/commands/pulumi_stack_output/) - By default, this command lists all output properties exported from a stack. If a specific property-name is supplied, just that property’s value is shown.

[pulumi console]() - This command opens the current stack in the Pulumi Console

[pulumi logs](/docs/cli/commands/pulumi_logs/) - This command aggregates log entries associated with the resources in a stack from the corresponding provider. For example, for AWS resources, the pulumi logs command will query CloudWatch Logs for log data relevant to resources in a stack.

pulumi preview - Show a preview of updates to a stack’s resources

