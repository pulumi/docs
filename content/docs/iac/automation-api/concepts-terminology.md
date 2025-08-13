---
title_tag: "Automation API Concepts & Terminology"
meta_desc: This page contains an overview of core concepts when using Automation API.
title: Concepts
h1: Automation API concepts & terminology
weight: 2
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Concepts
        parent: iac-automation-api
        weight: 2
aliases:
- /docs/guides/automation-api/concepts-terminology/
- /docs/using-pulumi/automation-api/concepts-terminology/
- /docs/iac/packages-and-automation/automation-api/concepts-terminology/
- /docs/iac/using-pulumi/automation-api/concepts-terminology/
---

Automation API lets you use functionality available in the Pulumi CLI via an SDK, as opposed to a Pulumi program which contains resource declarations and is invoked externally by the `pulumi` CLI. Automation API enables you to define a Pulumi program, its resources, stacks, and configuration for those stacks entirely in code, and then distribute that code as an executable invoked like any other executable in your supported language of choice (e.g., `python3 main.py` as opposed to `pulumi up`). Automation API is distributed as a namespace within the Pulumi SDK, and is part of Pulumi IaC's open source offering.

Automation API can be used for a number of use cases:

- Driving Pulumi deployments within CI/CD workflows
- Integration testing
- Multi-stage deployments such as blue-green deployment patterns
- Deployments involving application code like database migrations
- Building higher level tools, custom CLIs over Pulumi, etc.
- Using Pulumi behind a REST or GRPC API
- Debugging Pulumi programs (by using a single main entrypoint with "inline" programs)

## Workspace

To enable a broad range of runtime customization the API defines a `Workspace` interface. A `Workspace` is the execution context containing a single Pulumi project, a program, and multiple stacks. Workspaces are used to manage the execution environment, providing various utilities such as plugin installation, environment configuration (`$PULUMI_HOME`), and creation, deletion, and listing of Stacks.

### LocalWorkspace

The `LocalWorkspace` class is the default implementation of `Workspace`. This implementation relies on `Pulumi.yaml` and `Pulumi.[stack].yaml` as the intermediate format for Project and Stack settings. Modifying `ProjectSettings` will alter the Workspace `Pulumi.yaml` file, and setting config on a Stack will modify the `Pulumi.[stack].yaml` file. This is identical to the behavior of Pulumi CLI driven workspaces.

### RemoteWorkspace

The `RemoteWorkspace` class represents a workspace for running Pulumi operations remotely via Pulumi Deployments where the program is located in a remote Git repository.

## Stack

The `Stack` class represents an isolated, independently configurable instance of a Pulumi program. `Stack` exposes methods for the full pulumi lifecycle (`up`/`preview`/`refresh`/`destroy`), as well as managing configuration. Multiple Stacks are commonly used to denote different phases of development (such as development, staging and production) or feature branches (such as feature-x-dev, jane-feature-x-dev). You can learn more about stacks in the [intro docs](/docs/concepts/stack/).

## RemoteStack

The `RemoteStack` class represents an isolated, independently configurable instance of a Pulumi program. `RemoteStack` exposes methods for the full pulumi lifecycle (`up`/`preview`/`refresh`/`destroy`) for running these remotely from a remote workspace.

## Local Program

A local program is a traditional Pulumi CLI-driven program with its own directory, a `Pulumi.yaml` file, along with a file that defines the Pulumi program. Automation API can be used to drive these programs, as well as the CLI.

## Inline Program

Unlike traditional Pulumi programs, inline programs don't require a separate package on disk, with its own file and a `Pulumi.yaml`. Inline programs are functions that can be authored in the same file as your Automation API program or be imported from another package.

The program's lifecycle must be fully contained within the function, callback, or closure passed as the inline program. It is unsafe to perform actions outside the scope of the inline program function. Doing so can lead to unpredictable behavior, so always ensure that all resource operations and side effects occur within the inline program's execution context.
