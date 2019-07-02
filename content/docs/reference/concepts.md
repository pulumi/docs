---
title: Architecture & Concepts
menu:
  reference:
    identifier: concepts
    weight: 2
---

The Pulumi Cloud Development Platform is a combination of tools, libraries, runtime, and service that delivers a consistent development and operational control plane for cloud-native infrastructure.  That is, Pulumi enables you to not only manage your infrastructure as code, it enables you to define and manage your infrastructure using real programming languages and all of their supporting tools, not YAML.

At the center of Pulumi is an open-source cloud object model, coupled with an evaluation runtime that understands how to take programs written in any language, understand the cloud resources necessary to execute them, and then plan and manage those resources in a robust way. This cloud runtime and object model is inherently language- and cloud-neutral, enabling Pulumi to support many languages and clouds rapidly.

Each Pulumi [project]({{< relref "project.md" >}}) contains a [program]({{< relref "programming-model.md" >}}) --  executable code in a familiar language such as JavaScript, TypeScript, Python, or Go.  You will manage this program as you would any other source code, for example, using Git.

Each project also has associated [stacks]({{< relref "stack.md" >}}).  A stack is an isolated, independently configurable instance of a Pulumi program. Stacks are commonly used to denote different phases of development (such as development, staging and production) or feature branches (such as feature-x-dev, jane-feature-x-dev). 

When you select a stack and run the program, the Pulumi engine creates a model of the desired state of that stack.  The objects and dependencies created by your program form the model.  The model describes the [resources]({{< relref "programming-model.md" >}}) needed in the stack and their settings (for example, new aws.ec2.Instance(...)).  Pulumi updates the stack to match the desired state.

This following topics describe the core concepts behind Pulumi in more detail:

* [Programming Model]({{< relref "programming-model.md" >}}): the most important concepts you'll use in Pulumi programs.
* [Projects]({{< relref "project.md" >}}): Pulumi's way of organizing your infrastructure as code.
* [Stacks]({{< relref "stack.md" >}}): Pulumi's fundamental unit of partitioning, configuring, and scaling environments.
* [Configuration and Secrets]({{< relref "config.md" >}}): how to configure stacks, including storing secret encrypted settings.
* [Organizing Stacks and Projects]({{< relref "organizing-stacks-projects.md" >}}): best practices for organizing your Pulumi programs.
* [How Pulumi Works]({{< relref "how.md" >}}): a peek under the hood to learn more about how Pulumi performs deployments.
* [State and Backends]({{< relref "state.md" >}}): an overview of how Pulumi stores state and manages concurrency.

After learning these core concepts, you'll want to learn [more about the CLI]({{< relref "commands.md" >}}).
