---
title: "Go"
meta_desc: An overview of how to use the Go language for infrastructure as code
           on any cloud (AWS, Azure, GCP, Kubernetes, etc.).
menu:
  intro:
    parent: languages
    weight: 4
---

<img src="/logos/tech/logo-golang.png" align="right" width="150" style="padding:8px; margin-top: -64px">

Pulumi supports writing your infrastructure as code using the Go language. Go 1.16 or later is required.

<a class="btn" href="https://golang.org/doc/install" target="_blank" title="Install Go">Install Go</a>

## Getting Started

The fastest way to get up and running is to choose from one of the following Getting Started guides:

<div class="tiles mt-4">
    <div class="flex-1 pb-4 md:mr-4">
        <a class="tile p-4" href="{{< relref "/docs/get-started/aws" >}}?language=go">
            <img class="h-8 mx-auto" src="/logos/tech/aws.svg" alt="AWS">
        </a>
    </div>
    <div class="flex-1 pb-4 md:mr-4">
        <a class="tile p-4" href="{{< relref "/docs/get-started/azure" >}}?language=go">
            <img class="h-8 mx-auto" src="/logos/tech/azure.svg" alt="Azure">
        </a>
    </div>
    <div class="flex-1 pb-4 md:mr-4">
        <a class="tile p-4" href="{{< relref "/docs/get-started/gcp" >}}?language=go">
            <img class="h-8 mx-auto" src="/logos/tech/gcp.svg" alt="Google Cloud">
        </a>
    </div>
    <div class="flex-1 pb-4">
        <a class="tile p-4" href="{{< relref "/docs/get-started/kubernetes" >}}?language=go">
            <img class="h-8 mx-auto" src="/logos/tech/k8s.svg" alt="Kubernetes">
        </a>
    </div>
</div>

## Templates

The fastest way to get started is to use a template. The template will initialize a Pulumi project. The getting started guides shown above will help do this on your cloud of choice, but this section describes doing so independently.

From an empty directory, create a new project:

```bash
$ mkdir myproject && cd myproject
$ pulumi new go
```

This will create a `Pulumi.yaml` [project file]({{< relref "../concepts/project" >}}) containing some minimal metadata about your project (including a name and description which you may wish to change) and a `main.go` file containing your program. The name of the directory is used as the project name in `Pulumi.yaml`. Use your favorite Go dependency manager (such as Go's built-in modules system, by running `go mod init` in your project's directory).

To deploy your infrastructure, first build your Go program: `go build -o $(basename $(pwd))`. Then run `pulumi up` and Pulumi will perform the operations needed to deploy the infrastructure you have declared.

This `go` template is cloud agnostic, and you will need to install additional Go modules for the cloud provider of your choice. Additional templates are available that do this for you:

* `pulumi new aws-go`: creates a starter AWS Go project
* `pulumi new azure-go`: creates a starter Azure Go project
* `pulumi new gcp-go`: creates a starter Google Cloud Go project

## Pulumi Programming Model

The Pulumi programming model defines the core concepts you will use when creating infrastructure as code programs using
Pulumi. [Architecture & Concepts]({{< relref "/docs/intro/concepts" >}}) describes these concepts
with examples available in Go. These concepts are made available to you in the Pulumi SDK.

The Pulumi SDK is available to Go developers in source form on GitHub. To learn more,
[refer to the Pulumi SDK Reference Guide](https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi).

The Pulumi programming model includes a core concept of `Input` and `Output` values, which are used to track how outputs of one resource flow in as inputs to another resource.  This concept is important to understand when getting started with Go and Pulumi, and the [Inputs and Outputs]({{< relref "/docs/intro/concepts/inputs-outputs" >}}) documentation is recommended to get a feel for how to work with this core part of Pulumi in common cases.
