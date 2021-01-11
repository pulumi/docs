---
title: "Go"
meta_desc: An overview of how to use the Go language for infrastructure as code
           on any cloud (AWS, Azure, GCP, Kubernetes, etc.).
menu:
  intro:
    parent: languages
    weight: 2

---

<img src="/logos/tech/logo-golang.png" align="right" width="150" style="padding:8px; margin-top: -64px">

Pulumi supports writing your infrastructure as code using the Go language. Go 1.14 or later is required.

<a class="btn" href="https://golang.org/doc/install" target="_blank" title="Install Go">INSTALL GO</a>

## Getting Started

The fastest way to get up and running is to choose from one of the following Getting Started guides:

<div class="tiles my-4">
    <a class="tile flex-1 p-4" href="{{< relref "/docs/get-started/aws" >}}">
        <img class="h-8 mx-auto" src="/logos/tech/aws.svg" alt="AWS">
    </a>
    <a class="tile md:mx-4 flex-1 p-4" href="{{< relref "/docs/get-started/azure" >}}">
        <img class="h-8 mx-auto" src="/logos/tech/azure.svg" alt="Azure">
    </a>
    <a class="tile flex-1 p-4" href="{{< relref "/docs/get-started/gcp" >}}">
        <img class="h-8 mx-auto" src="/logos/tech/gcp.svg" alt="Google Cloud">
    </a>
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

The Pulumi programming model includes a core concept of `Input` and `Output` values, which are used to track how outputs of one resource flow in as inputs to another resource.  This concept is important to understand when getting started with Go and Pulumi, and the [Inputs and Outputs]({{< relref "/docs/intro/concepts/inputs-outputs" >}}) documentation is recommended to get a feel for how to work with this core part of Pulumi in common cases.
