---
title_tag: "HCL | Languages & SDKs"
meta_desc: An overview of how to use Pulumi HCL for infrastructure as code on any cloud (AWS, Azure, Google Cloud, Kubernetes, etc.).
title: HCL
h1: Pulumi & HCL
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: HCL
        parent: iac-languages
        weight: 7
        identifier: iac-languages-hcl
---

Pulumi supports writing your infrastructure as code using Pulumi HCL. Pulumi HCL is a
configuration language designed to provider a familiar experience for users transitioning from Terraform while embracing Pulumi's programming model. It supports managing infrastructure on any cloud, including Azure, AWS, and Google Cloud.

## Prerequisites

All you need to use Pulumi HCL is the [Pulumi CLI](/docs/install/).

## Example

```hcl
resource "myBucket" "aws:s3/bucket:Bucket" {
}

resource "myBucketWebsite" "aws:s3/bucketWebsiteConfigurationV2:BucketWebsiteConfigurationV2" {
  bucket        = myBucket.bucket
  indexDocument = {
    suffix = "index.html"
  }
}

resource "ownershipControls" "aws:s3/bucketOwnershipControls:BucketOwnershipControls" {
  bucket = myBucket.id
  rule   = {
    objectOwnership = "ObjectWriter"
  }
}

resource "publicAccessBlock" "aws:s3/bucketPublicAccessBlock:BucketPublicAccessBlock" {
  bucket          = myBucket.id
  blockPublicAcls = false
}

resource "indexHtml" "aws:s3/bucketObject:BucketObject" {
  bucket        = myBucket.id
  source        = "<h1>Hello, world!</h1>"
  acl           = "public-read"
  contentType   = "text/html"
  options {
    dependsOn = [ownershipControls, publicAccessBlock]
  }
}

output "bucketEndpoint" {
  value = "http://${myBucket.websiteEndpoint}"
}
```

Further examples are available in the [Pulumi examples repository](https://github.com/pulumi/examples). The specification for Pulumi HCL documents is in the [Pulumi HCL reference](/docs/iac/languages-sdks/hcl/hcl-language-reference/).

## Templates

The fastest way to start a new project is to use a template. The template will initialize a Pulumi
project and set up starter resources for the chosen cloud. The `hcl` template is cloud agnostic.

- `pulumi new aws-hcl`: creates a starter AWS Pulumi HCL project
- `pulumi new azure-hcl`: creates a starter Azure Pulumi HCL project
- `pulumi new gcp-hcl`: creates a starter Google Cloud Pulumi HCL project
- `pulumi new kubernetes-hcl`: creates a starter Kubernetes Pulumi HCL project

By default, `pulumi new` provides a number of templates provided by Pulumi, but it can also use your own custom templates.

To learn more about building and working with custom templates, see [Custom Templates](/docs/idp/developer-portals/templates) and the [`pulumi new`](/docs/cli/commands/pulumi_new/) docs.

You can also convert existing Terraform HCL projects to Pulumi HCL using the `pulumi convert` command:

```bash
pulumi convert --from terraform --language pcl
```

This will convert your Terraform files to HCL (`.hcl` files) that you can then use with Pulumi.

## Pulumi programming model

The Pulumi programming model defines the core concepts you will use when creating infrastructure as code programs using Pulumi. [Concepts](/docs/intro/concepts) describes these concepts with examples available in all supported languages, including Pulumi HCL.

To learn how the Pulumi programming model is implemented for Pulumi HCL, refer to the [Pulumi HCL reference guide](/docs/iac/languages-sdks/hcl/hcl-language-reference/).

## Converting from Terraform

Pulumi HCL provides an excellent migration path for Terraform users:

1. **Automated conversion**: Use `pulumi convert --from terraform --language pcl` to automatically convert Terraform HCL to Pulumi HCL
1. **Familiar syntax**: Pulumi HCL is inspired by Terraform's HCL, making it easy to read and understand
1. **Enhanced capabilities**: Access Pulumi's state management, secrets, and stack features while using familiar syntax

After conversion, you may need to make manual adjustments such as:

- Reviewing naming conventions (Pulumi uses camelCase)
- Verifying resource types are correctly mapped
- Updating function calls where needed
- Testing with `pulumi preview`

## HCL packages

The [Pulumi Registry](/registry/) houses 100+ HCL packages.
