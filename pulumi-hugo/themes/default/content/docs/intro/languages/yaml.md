---
title: "Pulumi YAML"
meta_desc: |
  An overview of how to use the Pulumi YAML config languages for infrastructure as code on any cloud (AWS, Azure, GCP, Kubernetes, etc.).
menu:
  intro:
    parent: languages
    weight: 5

aliases: ["/yaml/"]
---

<img src="/logos/tech/yaml.svg" align="right" width="150" style="padding:8px; margin-top: -64px">

Pulumi supports writing your infrastructure as code using Pulumi YAML. Pulumi YAML is a
configuration language designed to make describing infrastructure as simple as possible. It supports
managing infrastructure on any cloud, including Azure, AWS, and Google Cloud.

{{% notes "info" %}}
Pulumi YAML is currently in preview. Feedback is greatly appreciated!

Please post any Bug Reports or Feature Requests in [GitHub Issues](https://github.com/pulumi/pulumi-yaml/issues/new/choose).
{{% /notes %}}

## Getting Started

The fastest way to get up and running is to choose from one of the following Getting Started guides:

<div class="tiles mt-4">
    <div class="flex-1 pb-4 md:mr-4">
        <a class="tile p-4" href="{{< relref "/docs/get-started/aws" >}}?language=yaml">
            <img class="h-8 mx-auto" src="/logos/tech/aws.svg" alt="AWS">
        </a>
    </div>
    <div class="flex-1 pb-4 md:mr-4">
        <a class="tile p-4" href="{{< relref "/docs/get-started/azure" >}}?language=yaml">
            <img class="h-8 mx-auto" src="/logos/tech/azure.svg" alt="Azure">
        </a>
    </div>
    <div class="flex-1 pb-4 md:mr-4">
        <a class="tile p-4" href="{{< relref "/docs/get-started/gcp" >}}?language=yaml">
            <img class="h-8 mx-auto" src="/logos/tech/gcp.svg" alt="Google Cloud">
        </a>
    </div>
    <div class="flex-1 pb-4">
        <a class="tile p-4" href="{{< relref "/docs/get-started/kubernetes" >}}?language=yaml">
            <img class="h-8 mx-auto" src="/logos/tech/k8s.svg" alt="Kubernetes">
        </a>
    </div>
</div>

## Prerequisites

All you need to use Pulumi YAML is the [Pulumi CLI]({{< relref "/docs/get-started/install" >}}).

## Example

```yaml
name: simple-yaml
runtime: yaml
resources:
  my-bucket:
    type: aws:s3:Bucket
    properties:
      website:
        indexDocument: index.html
  index.html:
    type: aws:s3:BucketObject
    properties:
      bucket: ${my-bucket}
      source:
        Fn::StringAsset: <h1>Hello, world!</h1>
      acl: public-read
      contentType: text/html
outputs:
  bucketEndpoint: http://${my-bucket.websiteEndpoint}
```

{{% notes "info" %}}
The example is a fully valid and self-contained Pulumi project. You only need one file to create resources in Pulumi YAML.
{{% /notes %}}

## Templates

The fastest way to start a new project is to use a template. The template will initialize a Pulumi
project and set up starter resources for the chosen cloud. The `yaml` template is cloud agnostic.

- `pulumi new aws-yaml`: creates a starter AWS Pulumi YAML project
- `pulumi new azure-yaml`: creates a starter Azure Pulumi YAML project
- `pulumi new gcp-yaml`: creates a starter Google Cloud Pulumi YAML project
- `pulumi new kubernetes-yaml`: creates a starter Kubernetes Pulumi YAML project

## Pulumi Programming Model

The Pulumi programming model defines the core concepts you will use when creating infrastructure as
code programs using Pulumi. [Architecture & Concepts]({{< relref "/docs/intro/concepts" >}})
describes these concepts with examples available in all supported languages, including Pulumi YAML.

To learn how the Pulumi Programming Model is implemented for Pulumi YAML, refer
to the [Pulumi YAML Reference Guide](https://github.com/pulumi/pulumi-yaml#spec).

## Compiler support

Pulumi YAML includes native support for languages that compile to YAML/JSON via
the `compiler` runtime option.

```yaml
name: generated-from-cue
runtime:
  name: yaml
  options:
    compiler: cue export
```

Pulumi will run whatever program and arguments are specified in `compiler` and
interpret the output as a Pulumi YAML program.
