---
title: "Modern Cloud Infrastructure in Golang  - The Road to 2.0"
authors: ["evan-boyle"]
tags: ["go", "golang", "aws", "gcp", "azure"]
date: "2020-02-25"
meta_desc: "Pulumi + Go is a powerful combo for your cloud-native infrastructure."
meta_image: "pulumigo.png"
---

Here at Pulumi, everyone on our engineering team is a Gopher. We build our open-source [pulumi/pulumi engine](https://github.com/pulumi/pulumi) and our SaaS with Go. Pulumi has supported Go in preview for more than a year, but we've recently invested in making Go support for Pulumi great as part of [Pulumi 2.0]({{< relref "/blog/pulumi-2-0-roadmap#better-language-support" >}}).

## What is Pulumi?

Pulumi lets you use real languages to express your application’s infrastructure needs, using a powerful technique called “infrastructure as code.” Using infrastructure as code, you declare desired infrastructure, and an engine provisions it for you so that it’s automated, easy to replicate, and robust enough for demanding production requirements. Pulumi improves this process by leveraging real languages and making modern cloud infrastructure patterns, such as containers and serverless programs, first-class and easy.

Automatically create, update, or delete cloud resources using Pulumi’s infrastructure as code engine, removing manual point-and-clicking in the cloud provider consoles, UIs, and ad-hoc scripts.
Use your favorite IDEs and tools, including Visual Studio Code, taking advantage of features like auto-completion, refactoring, and interactive documentation.
Catch mistakes early on with standard compiler errors, and an infrastructure-specific policy engine for enforcing security, compliance, and best practices.
Reuse any existing go packages, or distribute your own, whether that’s for infrastructure best practices, productivity, or just general programming patterns.
Build scalable cloud applications using classic infrastructure cloud-native technologies. including serverless functions, and highly scalable databases such as AWS Aurora, into your core development experience, bringing them closer to your application code.

Pulumi’s free open source SDK, which includes a CLI and assortment of libraries, enables these capabilities.

Creating an AWS S3 Bucket is familiar and simple:

```go
package main

import (
    "github.com/pulumi/pulumi-aws/sdk/go/aws/s3"
    "github.com/pulumi/pulumi/sdk/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // Create an AWS resource (S3 Bucket)
        bucket, err := s3.NewBucket(ctx, "my-bucket", nil)
        if err != nil {
            return err
        }

        // Export the name of the bucket
        ctx.Export("bucketName", bucket.ID())
        return nil
    })
}
```

## An Expressive and Idiomatic Type System

Making Go a first-class citizen is a goal for the Pulumi 2.0 release. We especially wanted Go to have more idiomatic and stronger typing than `interface{}`.

Pulumi’s [programming model]({{< relref "/docs/intro/concepts/programming-model" >}}) is inherently asynchronous. Consider creating a new AWS SecurityGroup, and using it to provision an EC2 instance. The EC2 instance must wait for the Group to finish provisioning, and the Pulumi engine must track this dependency. While two resources, modern cloud deployments commonly manage hundreds of resources. Pulumi models these resources using promise-like wrappers referred to as Inputs and Outputs allowing us to build a dependency graph, and parallelize cloud resource provisioning where possible.

Inputs, Outputs, and functions that operate over them ([All]({{< relref "/docs/intro/concepts/programming-model#all" >}}), [Apply]({{< relref "/docs/intro/concepts/programming-model#apply" >}}), [Sprintf]({{< relref "/docs/intro/concepts/programming-model#outputs-and-strings" >}})) must be compatible with raw type primitives (string, integer, list, map, boolean), and user-defined structs. In other words, we must support polymorphism in a language that doesn’t have generics. We hide the gritty details behind a rich, strongly-typed API that we were able to iterate on easily thanks to the utilization of [code generation](https://github.com/pulumi/pulumi/blob/master/sdk/go/pulumi/types_builtins.go).

## Try Pulumi + Go Today

Although Pulumi for Go is in “preview” status, it supports all of the essential Pulumi programming model features (and the rest is on its way). Our goal is to gather feedback and over the next few weeks, and work hard to improve the Go experience across the board, including more examples and better documentation. To get started check out:

- Getting started with Go and [AWS]({{< relref "/docs/get-started/aws" >}}), [Azure]({{< relref "/docs/get-started/azure" >}}), or [Google Cloud]({{< relref "/docs/get-started/gcp" >}}).
- Author and deploy serverless functions in Go on [AWS Lambda](https://github.com/pulumi/examples/tree/master/aws-go-lambda) and [GCP Cloud Functions](https://github.com/pulumi/examples/tree/master/gcp-go-functions).
- Build a serverless container-based application on [AWS ECS Fargate](https://github.com/pulumi/examples/tree/master/aws-go-fargate).
- Deploy a web server on a virtual machine with [AWS](https://github.com/pulumi/examples/tree/master/aws-go-webserver) or [Azure](https://github.com/pulumi/examples/tree/master/azure-go-webserver-component).
- Deploy a Kubernetes cluster using [Azure Kubernetes Service](https://github.com/pulumi/examples/tree/master/azure-go-aks).

To keep up with our progress, follow our [Go project on Github](https://github.com/orgs/pulumi/projects/7), and feel free to [open a new issue](https://github.com/pulumi/pulumi/issues/new) with ideas, feedback, and bugs. [Join the community in Slack](https://slack.pulumi.com/) to discuss your scenarios, and to get any needed assistance from the team and other end users.
