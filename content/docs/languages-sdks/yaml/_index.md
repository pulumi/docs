---
title_tag: "YAML | Languages & SDKs"
meta_desc: An overview of how to use Pulumi YAML for infrastructure as code on any cloud (AWS, Azure, Google Cloud, Kubernetes, etc.).
title: YAML
h1: Pulumi & YAML
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  languages:
    identifier: yaml-language
    weight: 6

aliases:
- /yaml/
- /docs/intro/languages/yaml/
---

<img src="/logos/tech/yaml.svg" align="right" width="150" style="padding:8px; margin-top: -64px">

Pulumi supports writing your infrastructure as code using Pulumi YAML. Pulumi YAML is a
configuration language designed to make describing infrastructure as simple as possible. It supports
managing infrastructure on any cloud, including Azure, AWS, and Google Cloud.

## Prerequisites

All you need to use Pulumi YAML is the [Pulumi CLI](/docs/install/).

## Example

```yaml
name: simple-yaml
runtime: yaml
config:
  message:
    default: Hello, world!
    type: string
resources:
  my-bucket:
    type: aws:s3:Bucket
    properties:
      website:
        indexDocument: index.html
  ownership-controls:
    type: aws:s3:BucketOwnershipControls
    properties:
      bucket: ${my-bucket.id}
      rule:
        objectOwnership: ObjectWriter
  public-access-block:
    type: aws:s3:BucketPublicAccessBlock
    properties:
      bucket: ${my-bucket.id}
      blockPublicAcls: false
  index.html:
    type: aws:s3:BucketObject
    properties:
      bucket: ${my-bucket}
      source:
        fn::stringAsset: <h1>${message}</h1>
      acl: public-read
      contentType: text/html
    options:
      dependsOn:
        - ${ownership-controls}
        - ${public-access-block}
outputs:
  bucketEndpoint: http://${my-bucket.websiteEndpoint}
```

{{% notes "info" %}}
The example is a fully valid and self-contained Pulumi project. You only need one file to create resources in Pulumi YAML.
{{% /notes %}}

Further examples are given in the [Pulumi YAML GitHub
repository](https://github.com/pulumi/pulumi-yaml/tree/main/examples). The specification for Pulumi
YAML documents is in the [Pulumi YAML reference](/docs/languages-sdks/yaml/yaml-language-reference/).

## Templates

The fastest way to start a new project is to use a template. The template will initialize a Pulumi
project and set up starter resources for the chosen cloud. The `yaml` template is cloud agnostic.

- `pulumi new aws-yaml`: creates a starter AWS Pulumi YAML project
- `pulumi new azure-yaml`: creates a starter Azure Pulumi YAML project
- `pulumi new gcp-yaml`: creates a starter Google Cloud Pulumi YAML project
- `pulumi new kubernetes-yaml`: creates a starter Kubernetes Pulumi YAML project

By default, `pulumi new` provides a number of templates provided by Pulumi, but it can also use your own custom templates.

To learn more about building and working with custom templates, see [Custom Templates](/docs/pulumi-cloud/developer-portals/templates) and the [`pulumi new`](/docs/cli/commands/pulumi_new/) docs.

## Pulumi Programming Model

The Pulumi programming model defines the core concepts you will use when creating infrastructure as
code programs using Pulumi. [Concepts](/docs/intro/concepts)
describes these concepts with examples available in all supported languages, including Pulumi YAML.

To learn how the Pulumi Programming Model is implemented for Pulumi YAML, refer
to the [Pulumi YAML Reference Guide](/docs/languages-sdks/yaml/yaml-language-reference/).

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

## YAML Packages

The [Pulumi Registry](/registry/) houses 100+ YAML packages.
