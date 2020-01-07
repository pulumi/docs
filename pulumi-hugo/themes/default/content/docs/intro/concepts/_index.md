---
title: Architecture & Concepts
meta_desc: This page provides an overview of Architecture and Concepts when using the Pulumi Cloud Development Platform.
menu:
  intro:
    identifier: concepts
    weight: 2

aliases: ["/docs/reference/concepts/"]
---

The Pulumi Cloud Development Platform is a combination of tools, libraries, runtime, and service that delivers a consistent development and operational control plane for cloud-native infrastructure.  Not only does Pulumi enable you to manage your infrastructure as code, it also lets you define and manage your infrastructure using real programming languages (and all of their supporting tools) instead of YAML.

At the center of Pulumi is an open-source cloud object model, coupled with an evaluation runtime that knows how to take programs written in any language, understand the cloud resources necessary to execute them, and then plan and manage those resources in a robust way. This cloud runtime and object model is inherently language- and cloud-neutral, enabling Pulumi to support many languages and clouds rapidly.

Each Pulumi [project]({{< relref "project" >}}) contains a [program]({{< relref "programming-model" >}})---executable code in a familiar language such as JavaScript, TypeScript, Python, or Go. You will manage this program as you would any other source code. For example, by using Git.

Each project also has associated [stacks]({{< relref "stack" >}}). When you select a stack and run the program, the Pulumi engine creates a model of the desired state of that stack. The objects and dependencies created by your program form the model. The model describes the [resources]({{< relref "programming-model" >}}) needed in the stack and their settings. For example, `new aws.ec2.Instance(...)`.  Pulumi updates the stack to match the desired state.

The following topics describe the core concepts behind Pulumi in more detail:

* [Programming Model]({{< relref "programming-model" >}}): _The most important concepts you'll use in Pulumi programs._
* [Projects]({{< relref "project" >}}): _Pulumi's way of organizing your infrastructure as code._
* [Stacks]({{< relref "stack" >}}): _Pulumi's fundamental unit of partitioning, configuring, and scaling environments._
* [Configuration and Secrets]({{< relref "config" >}}): _How to configure stacks, including storing secret encrypted settings._
* [Organizing Stacks and Projects]({{< relref "organizing-stacks-projects" >}}): _Best practices for organizing your Pulumi programs._
* [How Pulumi Works]({{< relref "how-pulumi-works" >}}): _A peek under the hood to learn more about how Pulumi performs deployments._
* [State and Backends]({{< relref "state" >}}): _An overview of how Pulumi stores state and manages concurrency._

After learning these core concepts, you'll want to learn [more about the CLI]({{< relref "/docs/reference/cli" >}}).
