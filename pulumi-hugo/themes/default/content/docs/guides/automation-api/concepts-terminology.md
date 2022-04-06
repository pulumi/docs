---
title: Core Concepts and Terminology
meta_desc: This page contains an overview of core concepts when using Automation API.
linktitle: Automation API Concepts
weight: 1

menu:
  userguides:
    parent: automation-api
---

Automation API lets you define a Pulumi program as a function within your codebase rather than in a separate project and use methods to get and set configuration parameters programmatically.

The package can be used for a number of use cases:

- Driving pulumi deployments within CI/CD workflows
- Integration testing
- Multi-stage deployments such as blue-green deployment patterns
- Deployments involving application code like database migrations
- Building higher level tools, custom CLIs over Pulumi, etc.
- Using Pulumi behind a REST or GRPC API
- Debugging Pulumi programs (by using a single main entrypoint with "inline" programs)

## Workspace

To enable a broad range of runtime customization the API defines a `Workspace` interface. A `Workspace` is the execution context containing a single Pulumi project, a program, and multiple stacks. Workspaces are used to manage the execution environment, providing various utilities such as plugin installation, environment configuration (`$PULUMI_HOME`), and creation, deletion, and listing of Stacks.

### LocalWorkspace

The `LocalWorkspace` class is the default (and currently the only) implementation of `Workspace`. This implementation relies on `Pulumi.yaml` and `Pulumi.[stack].yaml` as the intermediate format for Project and Stack settings. Modifying `ProjectSettings` will alter the Workspace `Pulumi.yaml` file, and setting config on a Stack will modify the `Pulumi.[stack].yaml` file. This is identical to the behavior of Pulumi CLI driven workspaces.

## Stack

The `Stack` class represents an isolated, independently configurable instance of a Pulumi program. `Stack` exposes methods for the full pulumi lifecycle (`up`/`preview`/`refresh`/`destroy`), as well as managing configuration. Multiple Stacks are commonly used to denote different phases of development (such as development, staging and production) or feature branches (such as feature-x-dev, jane-feature-x-dev). You can learn more about stacks in the [intro docs]({{< relref "/docs/intro/concepts/stack" >}}).

## Local Program

A local program is a traditional Pulumi CLI-driven program with its own directory, a `Pulumi.yaml` file, along with a file that defines the Pulumi program. Automation API can be used to drive these programs, as well as the CLI.

## Inline Program

Unlike traditional Pulumi programs, inline programs don't require a separate package on disk, with its own file and a `Pulumi.yaml`. Inline programs are simply functions that can be authored in the same file as your Automation API program or be imported from another package.
