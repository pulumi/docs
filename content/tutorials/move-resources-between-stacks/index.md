---
title: "Move Resources Between Stacks"
title_tag: "Move Resources Between Stacks"
layout: single

# A succinct description of the tutorial. It appears on the Tutorials home and collection pages.
description: Learn how to move resources between stacks or projects.

# A similar description used for search results and social-media previews.
meta_desc: Learn how to move resources between stacks or projects.

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
    When refactoring a Pulumi project from a monolithic structure to micro stacks, you might need to move resources between different projects or stacks without recreating them. While it is possible to accomplish this by manually modifying Pulumi state files, doing so requires significant effort, can be error prone, and can be very time consuming.
    
    In this tutorial, you will learn how to move your resources using the `pulumi state move` command instead.

# A list of three to five things the reader will have learned by the end of the tutorial.
youll_learn:
    - How to identify a resource's URN
    - How to move a resource between stacks
    - Why and how to use aliases

# A list of tutorial prerequisites. Markdown is fine. Keep it simple; no need to be exhaustive here.
prereqs:
    - A [Pulumi Cloud account](https://app.pulumi.com/signup) and [access token](/docs/pulumi-cloud/accounts/#access-tokens)
    - The [Pulumi CLI](/docs/install/)
    - An [Amazon Web Services](https://aws.amazon.com/) account
    - The [AWS CLI](https://aws.amazon.com/cli/)
    - Your desired [language runtime installed](/docs/clouds/aws/get-started/begin/#install-language-runtime)

# The estimated time, in minutes, for new users to complete the topic.
estimated_time: 10

# # An optional list of collections this tutorial should be belong to. Collections are defined in data/tutorials/collections.yaml.
# collections:
#     - some-non-existent-collection
---

## Create a new project

To start, login to the [Pulumi CLI](/docs/cli/commands/pulumi_login/) and ensure it is [configured to use your AWS account](/docs/clouds/aws/get-started/begin/#configure-pulumi-to-access-your-aws-account). Next, [create a new project](/docs/clouds/aws/get-started/create-project/) and replace the default program code with the following:

{{< example-program path="aws-s3bucket-s3objects-random" >}}

This code example creates the following resources:

- A random object from the [Pulumi Random provider](/registry/packages/random/)
- An S3 bucket resource
- Two S3 bucket objects

It also includes one export that will output the name of the Pulumi random object.

Given that this example program makes use of the Pulumi Random provider, you will also need to make sure to [install this dependency into your project](https://github.com/pulumi/pulumi-random?tab=readme-ov-file#installing).

Now run the `pulumi up` command to deploy your resources before moving onto the next steps.

## Move a resource between stacks

The `pulumi state move` command works as follows:

```
$ pulumi state move --help
Move resources from one stack to another

This command can be used to move resources from one stack to another. This can be useful when
splitting a stack into multiple stacks or when merging multiple stacks into one.

Usage:
  pulumi state move [flags] <urn>...

Flags:
      --dest string       The name of the stack to move resources to
  -h, --help              help for move
      --include-parents   Include all the parents of the moved resources as well
      --source string     The name of the stack to move resources from
  -y, --yes               Automatically approve and perform the move
```

### Move within the same project

TBD

### Move to a different project

To demonstrate how to move a resource between two different projects, you will need to [create a second Pulumi project](/docs/clouds/aws/get-started/create-project/).

Then run the `pulumi stack ls --all` command to view your list of existing stacks:

## Add a resource alias

The `pulumi state move` only modifies the state file of the source and destination stacks. It does not modify the code of your program directly. With that being said, you will need to modify both programs to match the changes you have made. This can typically be accomplished by copy/pasting source code for the resources and/or components between the two codebases. Inputs and outputs of resources that were moved may need to be adjusted as part of this process. This can be done either by using stack references, or recreating the inputs in the program.

## Clean-up

## Next steps
