---
title_tag: "Go | Languages & SDKs"
meta_desc: An overview of how to use the Go language with Pulumi for infrastructure as code on any cloud (AWS, Azure, Google Cloud, Kubernetes, etc.).
title: Go
h1: Pulumi & Go
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Go
        parent: iac-languages
        weight: 4
        identifier: iac-languages-go
    languages:
        identifier: go
        weight: 4
aliases:
    - /docs/intro/languages/go/
    - /go/
    - /golang/
    - /docs/languages-sdks/go/
---

Pulumi supports writing your infrastructure as code in Go. Using a general-purpose language for infrastructure as code provides several key advantages:

- **Familiar syntax**: Write infrastructure code using the same language and patterns you already know
- **Rich ecosystem**: Leverage the Go module ecosystem in your infrastructure code
- **Native tooling**: Use your existing IDE, linters, test frameworks, and other development tools without requiring plugins or extensions
- **Type safety**: Catch errors at compile time with Go's static type system

## Installation requirements

### Go runtime

Pulumi supports any [supported version](https://go.dev/doc/devel/release#policy) of Go. We recommend using a recent release for the best experience.

To use the Go runtime, set `runtime: go` in your `Pulumi.yaml`:

```yaml
runtime: go
```

Install [Go](https://go.dev/doc/install) for your platform.

### Dependency management

Pulumi Go programs use [Go modules](https://go.dev/ref/mod) for dependency management. A new project includes a `go.mod` file; if you are starting from an existing directory, run `go mod init` to create one. Add the Pulumi SDK and provider packages with `go get`:

```bash
$ go get github.com/pulumi/pulumi/sdk/v3
```

## Getting started

The fastest way to get started with Pulumi and Go is to use a template:

```bash
$ pulumi new go
```

You can discover additional templates by running `pulumi new` with no arguments, or you can initialize a Pulumi program by supplying a specific URL to the `pulumi new` command. For example:

```bash
$ pulumi new https://github.com/pulumi/templates/tree/master/aws-go
```

See the [`pulumi new` documentation](/docs/iac/cli/commands/pulumi_new/) for full details.

The `go` template is cloud agnostic, and you will need to install additional Go modules for the cloud provider of your choice. Additional templates are available that do this for you:

- `pulumi new aws-go`: creates a starter AWS Go project
- `pulumi new azure-go`: creates a starter Azure Go project
- `pulumi new gcp-go`: creates a starter Google Cloud Go project

### Program entrypoint

A Pulumi Go program is an ordinary Go `main` package whose `main` function calls `pulumi.Run`. By default, Pulumi compiles and runs the program in the project directory. You can point at a different program directory with the top-level `main` attribute in your `Pulumi.yaml`:

```yaml
name: my-project
runtime: go
main: ./infra
```

If you prefer to build the program yourself, set the `binary` runtime option to the path of a prebuilt executable, and Pulumi will run it directly instead of compiling on each invocation:

```yaml
runtime:
  name: go
  options:
    binary: ./bin/my-program
```

## Defining resources

Writing a Pulumi program in Go involves declaring infrastructure resources using resource constructors. Here are the key concepts:

- **Declare resources**: Create infrastructure resources by instantiating resource types from provider packages. For example, `s3.NewBucket(ctx, "my-bucket", nil)` creates an S3 bucket.
- **Inputs and outputs**: The Pulumi programming model uses `Input` and `Output` types to track dependencies between resources. Understanding how to work with inputs and outputs is essential for building infrastructure. See [Inputs and outputs](/docs/concepts/inputs-outputs/) for the language-neutral overview, and [Inputs & outputs in Go](/docs/iac/languages-sdks/go/go-inputs-outputs/) for the Go-specific type model — `Input`/`Output` types, `ApplyT`, `All`, and output lifting.
- **Immutable infrastructure**: Once declared, resource properties are immutable within your program. Changes to resource definitions result in updates during the next deployment.
- **Stack outputs**: Export values from your program with `ctx.Export(...)` to make them accessible from the CLI or to other Pulumi programs.

The Pulumi SDK provides constructs for working with key Pulumi concepts. For more information, see:

- [Pulumi Concepts](/docs/iac/concepts/)
- [How Pulumi Works](/docs/iac/guides/basics/how-pulumi-works/)

## Program execution

Pulumi programs are most commonly executed using the Pulumi CLI commands such as `pulumi up`, `pulumi preview`, and `pulumi destroy`. The CLI compiles your Go program and handles authentication, state management, and orchestrating resource operations.

Alternatively, you can use the [Automation API](/docs/iac/concepts/automation-api/) to programmatically control the Pulumi engine from within your Go code. The Automation API allows you to:

- Embed Pulumi operations in regular Go applications
- Build custom deployment tools and workflows
- Create self-service infrastructure platforms

With Automation API, your Go code controls Pulumi, rather than Pulumi controlling your code.

## Documentation and resources

### Pulumi SDK

The [Pulumi SDK (`pulumi`)](https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi) contains the core constructs for working with Pulumi, including resources, configuration, stack outputs, and more. You will need to reference it in most Pulumi programs.

### Provider SDKs

For managing resources in a Pulumi program, you can find the relevant SDK reference documentation for each provider in [the Pulumi Registry](/registry/), which houses 100+ Go packages.

### Dev versions

Pulumi SDKs also publish pre-release versions that include all the latest changes from the main development branch. You can install them using the regular `go get` tooling. For example:

```bash
$ go get github.com/pulumi/pulumi/sdk/v3@master
```

For more information on when and how to use dev builds, see [Using dev builds for unreleased fixes](/docs/iac/operations/debugging/using-dev-builds/).

### Testing

- [Unit testing](/docs/iac/concepts/testing/unit/): Test your infrastructure code in isolation
- [Integration testing](/docs/iac/concepts/testing/integration/): Test your infrastructure deployments end-to-end
