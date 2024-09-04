---
title: "Importing Infrastructure"
title_tag: "Importing Infrastructure"
layout: single

# A succinct description of the tutorial. It appears on the Tutorials home and collection pages.
description: Learn how to import existing cloud resources into your Pulumi programs in this tutorial.

# A similar description used for search results and social-media previews.
meta_desc: Learn how to import existing cloud resources into your Pulumi programs in this tutorial.

# An image for the tutorial. It appears on tutorial page and in social-media previews.
meta_image: meta.png

# An optional video for the tutorial. When present, it appears at the top of the page, replacing
# the meta image. YouTube and HTML5 video sources are supported.
# video:
#     url: /blog/drift-detection/drift.mp4
#     youtube: Q8tw6YTD3ac

# The order in which the tutorial appears in most lists. Order is ascending, so higher numbers
# mean the tutorial will appear further down the list. Positive integers only.
weight: 999

# A brief summary of the tutorial. It appears at the top of the tutorial page. Markdown is fine.
summary: |
    Most infrastructure as code projects require working with existing cloud resources, whether those resources were originally created with another Infrastructure as Code (IaC) tool or manually provisioned with a cloud provider console or CLI.

    Interacting with a previously created cloud resource with Pulumi typically happens in one of two ways. The first way is by referencing the properties of the existing cloud resource in order to use those properties to configure a Pulumi-managed resource. This first scenario is sometimes called _coexistence_, and you can learn more about it in [Adopting Pulumi > Coexistence documentation](/docs/using-pulumi/adopting-pulumi/#coexistence).
    
    The second way is by adopting the existing resource to bring it under management by Pulumi. This second scenario is called _adoption_ or _import_, and it is this scenario that will be covered in this tutorial.

# A list of three to five things the reader will have learned by the end of the tutorial.
youll_learn:
    - How to import resources using the CLI
    - How to import resources in bulk
    - How to import resources in code

# A list of tutorial prerequisites. Markdown is fine. Keep it simple; no need to be exhaustive here.
prereqs:
    - The [Pulumi CLI](/docs/install/)
    - A [Pulumi Cloud account](https://app.pulumi.com/signup) and [access token](/docs/pulumi-cloud/accounts/#access-tokens)
    - An [Amazon Web Services](https://aws.amazon.com/) account
    - The [AWS CLI](https://aws.amazon.com/cli/)
    - Your desired [language runtime installed](/docs/clouds/aws/get-started/begin/#install-language-runtime)

# The estimated time, in minutes, for new users to complete the topic.
estimated_time: 10

# An optional list of collections this tutorial should be belong to. Collections are defined in data/tutorials/collections.yaml.
# collections:
#     - some-non-existent-collection
---

## Create initial resources

To start, login to the [AWS Console](https://console.aws.amazon.com/s3) and [create a new S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html). You can create the bucket using default settings, making sure to provide a globally unique name for the bucket.

{{< video title="Running the pulumi login command with access token" src="/tutorials/importing-infrastructure/aws-console-create-s3-bucket.mp4" autoplay="true" loop="true" >}}

Then create a new Pulumi project and stack for the resource to live in.

## Importing a resource

In Pulumi, there are three paths to take when importing resources. Pulumi allows you to import resources from any currently existing system with either (1) the `pulumi import` CLI command or (2) an import option in the code. Alternately, you can bulk import resources from anywhere with a special JSON file and the `pulumi import` CLI command. The CLI command also offers a resource definition that you can add to your Pulumi program to manage the resource going forward.

### Import using the CLI

The `pulumi import` command looks up the resource using the specified type token and resource identifier, adds the resource to the stack's current state, and emits the code required to manage the resource with Pulumi from that point forward. This option requires the least manual effort, so is generally recommended, and is best suited to projects consisting consisting of only one stack.

To import an existing cloud resource with the Pulumi CLI, use the following syntax:

```bash
$ pulumi import <type> <name> <id>
```

* The first argument, `type`, is the Pulumi type token to use for the imported resource.

    You can find the type token for a given resource by navigating to the Import section of the resource's API documentation in the [Pulumi Registry](/registry/). For example, the type token of an [Amazon S3 Bucket](/registry/packages/aws/api-docs/s3/bucket/#import) resource, for example, is `aws:s3/bucket:Bucket`.

* The second argument, `name`, is the [resource name](/docs/concepts/resources/names) to apply to the resource once it's imported. The generated code will use this name for the resource declaration (the first parameter in any resource), so like all Pulumi resource names, it must be unique among all resources for this type within the scope of the containing project. (That is, you may have an S3 bucket and a VPC named `foo`, but you cannot have two S3 buckets named `foo`.)

* The third argument, `id`, is the value to use for the resource lookup in the cloud provider. This value should correspond to the designated `lookup property` specified in the Import section of the resource's API documentation in the Registry. In the case of an AWS S3 bucket, this would be `bucket`.
