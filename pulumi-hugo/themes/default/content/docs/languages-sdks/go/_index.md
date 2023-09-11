---
title_tag: "Go | Languages & SDKs"
meta_desc: An overview of how to use the Go language with Pulumi for infrastructure as code on any cloud (AWS, Azure, Google Cloud, Kubernetes, etc.).
title: Go
h1: Pulumi & Go
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    languages:
        identifier: go
        weight: 4
aliases:
- /docs/intro/languages/go/
---

<img src="/logos/tech/logo-golang.png" align="right" width="150" style="padding:8px; margin-top: -64px">

Pulumi supports writing your infrastructure as code in the Go language built for any [supported version](https://go.dev/doc/devel/release#policy).

<a class="btn btn-secondary" href="https://golang.org/doc/install" target="_blank" title="Install Go">Install Go</a>

## Templates

The fastest way to get started is to use a template. The template will initialize a Pulumi project.

From an empty directory, create a new project:

```bash
$ mkdir myproject && cd myproject
$ pulumi new go
```

This will create a `Pulumi.yaml` [project file](/docs/concepts/projects/) containing some minimal metadata about your project (including a name and description which you may wish to change) and a `main.go` file containing your program. The name of the directory is used as the project name in `Pulumi.yaml`. Use your favorite Go dependency manager (such as Go's built-in modules system, by running `go mod init` in your project's directory).

To deploy your infrastructure, first build your Go program: `go build -o $(basename $(pwd))`. Then run `pulumi up` and Pulumi will perform the operations needed to deploy the infrastructure you have declared.

This `go` template is cloud agnostic, and you will need to install additional Go modules for the cloud provider of your choice. Additional templates are available that do this for you:

* `pulumi new aws-go`: creates a starter AWS Go project
* `pulumi new azure-go`: creates a starter Azure Go project
* `pulumi new gcp-go`: creates a starter Google Cloud Go project

## Pulumi Programming Model

The Pulumi programming model defines the core concepts you will use when creating infrastructure as code programs using
Pulumi. [Concepts](/docs/intro/concepts) describes these concepts
with examples available in Go. These concepts are made available to you in the Pulumi SDK.

The Pulumi SDK is available to Go developers in source form on GitHub. To learn more,
[refer to the Pulumi SDK Reference Guide](https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi).

The Pulumi programming model includes a core concept of `Input` and `Output` values, which are used to track how outputs of one resource flow in as inputs to another resource.  This concept is important to understand when getting started with Go and Pulumi, and the [Inputs and Outputs](/docs/concepts/inputs-outputs/) documentation is recommended to get a feel for how to work with this core part of Pulumi in common cases.

## Package Documentation

In addition to the standard packages the [Pulumi Registry](/registry/) houses 100+ Go packages.

### Standard Packages

<dl class="tabular">
    <dt>Pulumi SDK</dt>
    <dd><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi">pulumi</a></dd>
</dl>
