---
title: Architecture & Concepts
meta_desc: This page describes the primary concepts behind the Pulumi infrastructure as code platform.
menu:
  intro:
    identifier: concepts
    weight: 2

aliases: ["/docs/reference/concepts/"]
---

Pulumi is a modern infrastructure as code platform. It includes a CLI, runtime, libraries, and a hosted service that, working together, deliver a robust way of provisioning, updating, and managing cloud infrastructure. Instead of YAML or a domain-specific language (DSL), Pulumi leverages existing, familiar programming languages, including TypeScript, JavaScript, Python, Go, and .NET, and their native tools, libraries, and package managers.

This section will teach you the core concepts behind Pulumi, including how to author your Pulumi programs, the CLI you will use to deploy those programs, how projects (and their related concept, "stacks") help you to organize your environments, and how Pulumi works under the hood.

> If this is your first time using Pulumi, you likely want to begin with [the Getting Started guide]({{< relref "/docs/get-started" >}}) for your cloud of choice. It will walk you through an [AWS]({{< relref "/docs/get-started/aws" >}}), [Azure]({{< relref "/docs/get-started/azure" >}}), [GCP]({{< relref "/docs/get-started/gcp" >}}), or [Kubernetes]({{< relref "/docs/get-started/kubernetes" >}}) deployment from start to finish.

The following topics describe the core concepts behind Pulumi in more detail:

<div class="md:flex flex-row mt-6 mb-6">
    <div class="w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="{{< relref "programming-model" >}}"><i class="fas fa-book pr-2"></i>Programming Model</a></h3>
        <p>The core concepts you will use when authoring your Pulumi programs.</p>
    </div>
    <div class="w-1/2 border-solid ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="{{< relref "project" >}}"><i class="far fa-window-maximize pr-2"></i>Projects</a></h3>
        <p>Pulumi's way of organizing your infrastructure as code projects.</p>
    </div>
</div>
<div class="md:flex flex-row mt-6 mb-6">
    <div class="w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="{{< relref "stack" >}}"><i class="fas fa-cloud pr-2"></i>Stacks</a></h3>
        <p>Pulumi's fundamental unit of partitioning, configuring, and scaling environments.</p>
    </div>
    <div class="w-1/2 border-solid ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="{{< relref "config" >}}"><i class="fas fa-keyboard pr-2"></i>Configuration and Secrets</a></h3>
        <p>How to configure stacks, including storing secret encrypted settings.</p>
    </div>
</div>
<div class="md:flex flex-row mt-6 mb-6">
    <div class="w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="{{< relref "organizing-stacks-projects" >}}"><i class="fas fa-greater-than pr-2"></i>Organizing Projects</a></h3>
        <p>Best practices for organizing your Pulumi programs.</p>
    </div>
    <div class="w-1/2 border-solid ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="{{< relref "how-pulumi-works" >}}"><i class="fas fa-keyboard pr-2"></i>How Pulumi Works</a></h3>
        <p>A peek under the hood to learn more about how Pulumi performs deployments.</p>
    </div>
</div>
<div class="md:flex flex-row mt-6 mb-6">
    <div class="w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="{{< relref "state" >}}"><i class="fas fa-greater-than pr-2"></i>State and Backends</a></h3>
        <p>An overview of how Pulumi stores state and manages concurrency.</p>
    </div>
</div>

After learning these core concepts, you'll want to learn [more about the CLI]({{< relref "/docs/reference/cli" >}}).
