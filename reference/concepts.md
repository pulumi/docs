---
title: Architecture and Concepts
---

Each Pulumi [project](project.html) contains a [program](#programs) and configuration parameters  Each project has one or more related [stacks](stack.html).

A Pulumi [program](#programs) is executable code in a familiar language such as JavaScript, TypeScript, Python, or Go.  You will manage this program as you would any other source code, for example, using Git.

When you select a [stack](stack.html) and run the program, the Pulumi engine creates objects and dependencies that form a model of the desired state of that stack.  The model describes the [resources](#resources) needed in the stack and their settings (for example, `new aws.ec2.Instance(...)`) .  As it runs, the Pulumi engine updates the stack to match the model.

A [stack](stack.html) is an isolated, independently configurable instance of a Pulumi program. Each stack belongs to a single project.  Stacks are commonly used to denote different phases of development (such as development, staging and production) or feature branches (such as feature-x-dev, jane-feature-x-dev). Stacks contain their configuration values.

This section describes the core concepts behind Pulumi:

* [Programming Model](programming-model.html): the most important concepts you'll use in Pulumi programs.
* [Projects](project.html): Pulumi's way of organizing your infrastructure as code.
* [Stacks](stack.html): Pulumi's fundamental unit of partitioning, configuring, and scaling environments.
* [Configuration and Secrets](config.html): how to configure stacks, including storing secret encrypted settings.
* [Organizing Stacks and Projects](organizing-stacks-projects.html): best practices for organizing your Pulumi programs.
* [How Pulumi Works](how.html): a peek under the hood to learn more about how Pulumi performs deployments.
* [State and Backends](state.html): an overview of how Pulumi stores state and manages concurrency.

After learning these core concepts, you'll want to learn [more about the CLI](commands.html).
