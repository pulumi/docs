---
title: "Manage Pulumi Teams in Bulk with the New CLI Teams Flag"
date: "2023-03-31"
meta_desc: "We've added a new CLI flag to the stack init subcommand allowing users to grant team access to newly created stacks."
meta_image: "meta.png"

authors:
    - "robbie-mckinstry"
        
tags:
    - "cli"
    - "stack-init"
    - "cli-flags"
---

We've been hearing feedback from our customers that they need ways to manage permissions for their stacks at scale. Today we are announcing a `--teams` flag for [`pulumi stack init`](/docs/cli/commands/pulumi_stack_init), which allows customers to assign Teams to stacks from the CLI. This flag offers a third programmatic method for assigning permissions, supplementing [Pulumi Service REST API](/docs/reference/service-rest-api) or the [Pulumi Service Provider](/registry/packages/pulumiservice). Developers can now initialize their stacks with the right permissions directly from the CLI.

<!--more-->

Here's some background for any Pulumi newcomers. Pulumi projects
consist of stacks, which are separate deployments of the same infrastructure. Stacks may
also be configured with separate inputs. Organization admins can leverage RBAC
to grant access permissions at the organization or Pulumi Teams levels. Pulumi Teams and RBAC are available for Enterprise and Business Critical customers.

Stacks are often created via the CLI with the [`pulumi stack init` command](https://www.pulumi.com/docs/cli/commands/pulumi_stack_init/#options).
This command initializes a new stack. If you're using the
[Pulumi Service](https://www.pulumi.com/docs/concepts/state/#pulumi-service-backend) as your backend, you can view your newly created stack in the Pulumi Service console. If your organization uses teams, you will want to give your teammates access to the stack.

With the release of Pulumi v3.59.0, developers can assign Pulumi Team access during stack creation. To do this, pass in the `--teams` flag followed by the team's name. For instance:

```bash
pulumi stack init --teams Red
```

This saves time by eliminating context switching, allowing users to stay on task. Previously, the Service console was the most direct way to assign team access to a stack, meaning a trip to the browser before your teammates could access the stack. The `--teams` flag improves upon the process of managing stack permissions by removing this step.

Use the flag multiple times to assign access to multiple Pulumi Teams, as in:

```bash
pulumi stack init --teams Red --teams Blue
```

Currently, the feature always grants `read` and `write` access, the most commonly assigned permissions.

We implemented this feature as a direct result of feedback from daily users.
Context switching can be expensive when you're creating enough stacks.
At Pulumi, we enable our users to squeak out as much productivity from our tooling
as possible. We're always happy to make ergonomic improvements. We look
forward to continuing to raise the bar for cloud productivity.
