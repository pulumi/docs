---
title: "Automation API: Supercharged Cloud Tooling"
date: 2021-01-14
meta_desc: "Pulumi's Automation API enables you to build cloud tools to increase developer productivity."
meta_image: automation_api_v2.png
authors:
    - sophia-parafina
tags:
    - Automation API
    - cloud tools
---

"Why use a programming language to build and maintain infrastructure?" is a question we hear frequently. There are apparent advantages such as using a mature and well-known language across a team, enabling cloud engineers to use software development best practices, and an ecosystem of tools for building robust systems.

Infrastructure as code enables you to build tools and environments to automate routine tasks, letting cloud engineers concentrate on efficiency and resilience. In this article, we'll take a look at how Pulumi's Automation API lets you build custom ops tooling that improves your workflow.

<!--more-->

## What is the Automation API?

Automation API is a programming interface overlaid on the Pulumi engine for deploying infrastructure. Instead of using the Pulumi CLI to deploy infrastructure, you can directly call the engine to run code from your chosen language. With the Automation API, your Pulumi programs and stacks are strongly-typed and composable infrastructure building blocks. You can fully embed Pulumi inside your software projects, which means your code can power a wide range of cloud automation projects without the Pulumi CLI and a reduced human-in-the-loop footprint.

{{% notes type="info" %}}
This alpha release of Automation API currently supports Node.js and go. Python and .NET (C#) will be released soon.
{{% /notes %}}

## Cleaning Up

To demonstrate how Automation API enables you to build tools, let's tackle the common problem of unused virtual machines in the cloud. Companies spent an estimated $11 billion on idle resources in 2020, according to [ParkMyCloud](https://www.parkmycloud.com/blog/cloud-computing-growth/). Merely shutting down unused resources can significantly decrease costs for any organization.

We can use the Automation API to build a specialized CLI tool for creating and managing virtual machines. We wrote `vmgr` to demonstrate provisioning temporary virtual machines that expire after a user-specified amount of time. The [complete example](https://github.com/pulumi/automation-api-examples/tree/main/go/vm_manager_azure) is available on Github.  The `vmgr`CLI is a tool for provisioning temporary development virtual machines in Azure. Let's take a look at this project.

An advantage of using a programming language is that you can use common software packages in your code. In the `vmgr` example, we use [Cobra](https://github.com/spf13/cobra), a library for CLI applications used in Go projects Kubernetes, Hugo, and Github CLI. Instead of writing CLI boilerplate code with arguments, we can use Cobra with Automation API. VMs are provisioned as [Stacks]({{< relref "/docs/intro/concepts/stack" >}}) and their state is held by the [Pulumi service]({{< relref "/docs/intro/concepts/state" >}}). The cleanup job queries the Pulumi Service for stacks older than specified and removes them along with any child resources.

'vmgr' takes two commands:

- `vmgr add`: creates a new VM web server with a public IP. These web servers share a resource group and virtual network that is referenced from a shared stack.
- vmgr cron <expiration>: scans all VM stacks for stacks that are older than the specified expiration. This command will continue to retry deletion even if it sees failures and will typically succeed in deleting the VM and public IP on the second try.

To delete VMs older than 5 minutes:

```bash
$ vmgr cron 5m
```

To delete VMs older than five days.

```bash
$vmgr cron 5d
```

`vmgr` is a tool you can give to developers that they can use immediately with the added benefit of reducing costs by removing unused instances. Automation API enables building tools that speed up the inner dev loop for application developers and reduces the operation team's burden to clean up unused instances.

## Automate All the Things

Cloud engineering will automate many tasks that are currently performed by operators. Using infrastructure as code and SDKs such as Automation API, we can build self-service tools that improve the inner dev loop for application developers and let operators perform higher-level tasks such as maintenance and infrastructure monitoring. This simple example demonstrates the effective use of infrastructure as code by importing other software libraries to build a specialized tool that is not possible with DSLs or YAML.

Automation API is currently in preview and will be part of the Pulumi 3.0 GA release, including additional language support. To get started with Automation API, try out the [examples](https://github.com/pulumi/automation-api-examples) and documentation for [node.js]({{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi/x/automation" >}}) and [go](https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/x/auto). If you are looking for a more complex example, check out [ploy](https://github.com/jaxxstorm/ploy), a CLI tool that builds  Docker images and deploys them on Kubernetes.
