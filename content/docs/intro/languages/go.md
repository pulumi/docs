---
title: "Go"
meta_desc: An overview of how to use the Go language for infrastructure as code
           on any cloud (AWS, Azure, GCP, Kubernetes, etc.).
menu:
  intro:
    parent: languages
    weight: 2

aliases: ["/dotnet/"]
---

<img src="/logos/tech/logo-golang.png" align="right" width="150" style="padding:8px; margin-top: -64px">

Pulumi supports writing your infrastructure as code using the Go language.

<a class="btn" href="https://golang.org/doc/install" target="_blank" title="Install Go">INSTALL GO</a>

## Documentation

Pulumi Go documentation is available at [godoc](https://godoc.org/github.com/pulumi/pulumi).

## Getting Started

The fastest way to get up and running is to choose from one of the following Getting Started guides:

<div class="flex md:flex-row flex-col my-6">
    <a class="block flex-1 btn bg-transparent border border-solid border-gray-300 hover:bg-gray-200 p-4 mb-4 mr-0 md:mb-0 md:mr-4 flex justify-center" href="{{< relref "../../get-started/aws" >}}">
        <img class="h-5" src="/logos/tech/aws.svg" alt="AWS">
    </a>
    <a class="block flex-1 btn bg-transparent border border-solid border-gray-300 hover:bg-gray-200 p-4 mb-4 mr-0 md:mb-0 md:mr-4 flex justify-center" href="{{< relref "../../get-started/azure" >}}">
        <img class="h-5" src="/logos/tech/azure.svg" alt="Azure">
    </a>
    <a class="block flex-1 btn bg-transparent border border-solid border-gray-300 hover:bg-gray-200 p-4 flex justify-center" href="{{< relref "../../get-started/gcp" >}}">
        <img class="h-5" src="/logos/tech/gcp.svg" alt="Google Cloud">
    </a>
</div>

## Templates

The fastest way to get started is to use a template. The template will initialize a Pulumi project. The getting started guides shown above will help do this on your cloud of choice, but this section describes doing so independently.

From an empty directory, create a new project:

```bash
$ mkdir myproject && cd myproject
$ pulumi new go
```

This will create a `Pulumi.yaml` [project file]({{< relref "project" >}}) containing some minimal metadata about your project (including a name and description which you may wish to change) and a `main.go` file containing your program. The name of the directory is used as the project name in `Pulumi.yaml`. Use your favorite Go dependency manager (such as Go's built-in modules system, by running `go mod init` in your project's directory).

To deploy your infrastructure, first build your Go program: `go build -o $(basename $(pwd))`. Then run `pulumi up` and Pulumi will perform the operations needed to deploy the infrastructure you have declared.

This `go` template is cloud agnostic, and you will need to install additional Go modules for the cloud provider of your choice. Additional templates are available that do this for you:

* `pulumi new aws-go`: creates a starter AWS Go project
* `pulumi new azure-go`: creates a starter Azure Go project
* `pulumi new gcp-go`: creates a starter Google Cloud Go project
