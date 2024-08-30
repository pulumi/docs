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
    There are certain scenarios in which you might need to move resources between different projects or stacks without recreating them, such as when refactoring a Pulumi project from a monolithic structure to micro-stacks. While it is possible to accomplish this by manually modifying Pulumi state files, doing so requires significant effort, can be error prone, and can be very time consuming.
    
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

{{< notes type="info" >}}

This command will only work for stacks that exist within the same backend. It is currently not possible to move a resource between different backends, but you can move stacks between backends using other existing tools. Please refer to the [Migrating Between State Backends](/docs/concepts/state/#migrating-between-state-backends) documentation for more information.

{{< /notes >}}

Both `dest` and `source` can be either stacks in the current project, or stacks in across different projects. The resources being moved have to be specified by their full [Uniform Resource Name (URN)](/docs/concepts/resources/names/#urns), and multiple URNs can be passed at once.

Let's say you have a situation where your program code has grown too large, and you want to group the AWS resources separately from the Random resource. This means you want to move the S3 bucket as well as its bucket objects to a separate stack. In the next sections, you will learn how to move these resource into a different stack, one that exists in the same project, and one that exists in a different project.

### Move within the same project

To start, you will need to create a new stack within your project by running the `pulumi stack init` command. For the purposes of this tutorial, we have named the new stack `destination`:

```bash
$ pulumi stack init
Please enter your desired stack name.
To create a stack in an organization, use the format <org-name>/<stack-name> (e.g. `acmecorp/dev`).
stack name (dev): destination
Created stack 'destination'
```

Now run the `pulumi stack ls` command to verify your stacks in the current project:

```bash
$ pulumi stack ls
NAME          LAST UPDATE    RESOURCE COUNT  URL
destination*  n/a            n/a             https://app.pulumi.com/v-torian-pulumi-corp/pulumi-state-move-tutorial/destination
source        2 minutes ago  7               https://app.pulumi.com/v-torian-pulumi-corp/pulumi-state-move-tutorial/source
```

At this point, you will need to collect the fully qualified stack names of the source and destination stacks. The format of a stack's fully qualified name is `<organization>/<project>/<stack>`. In the `URL` column in the above output, you can see the value of each stack's fully qualified name after the `https://app.pulumi.com/` part of the URL.

Next, you will need to obtain the full URN of the S3 bucket resource. To do so, run the `pulumi stack --show-urns` command, and copy the value next to the `URN` parameter under the `aws:s3/bucket:Bucket` resource:

```bash
$ pulumi stack --show-urns
Current stack is source:
    Owner: v-torian-pulumi-corp
    Last updated: 28 seconds ago (2024-08-30 08:07:56.461286624 +0000 UTC)
    Pulumi version used: v3.130.0
Current stack resources (7):
    TYPE                                    NAME
    pulumi:pulumi:Stack                     pulumi-state-move-tutorial-source
    │  URN: urn:pulumi:source::pulumi-state-move-tutorial::pulumi:pulumi:Stack::pulumi-state-move-tutorial-source
    ├─ random:index/randomPet:RandomPet     my-pet-name
    │     URN: urn:pulumi:source::pulumi-state-move-tutorial::random:index/randomPet:RandomPet::my-pet-name
    ├─ aws:s3/bucket:Bucket                 b
    │  │  URN: urn:pulumi:source::pulumi-state-move-tutorial::aws:s3/bucket:Bucket::b
    │  ├─ aws:s3/bucketObject:BucketObject  index.html
    │  │     URN: urn:pulumi:source::pulumi-state-move-tutorial::aws:s3/bucket:Bucket$aws:s3/bucketObject:BucketObject::index.html
    │  └─ aws:s3/bucketObject:BucketObject  random.html
    │        URN: urn:pulumi:source::pulumi-state-move-tutorial::aws:s3/bucket:Bucket$aws:s3/bucketObject:BucketObject::random.html
    ├─ pulumi:providers:random              default_4_16_3
    │     URN: urn:pulumi:source::pulumi-state-move-tutorial::pulumi:providers:random::default_4_16_3
    └─ pulumi:providers:aws                 default_6_50_1
          URN: urn:pulumi:source::pulumi-state-move-tutorial::pulumi:providers:aws::default_6_50_1

Current stack outputs (1):
    OUTPUT   VALUE
    PetName  main-longhorn
```

In this scenario, you only need the URN of the S3 bucket resource and not the URNs for the bucket objects. This is because the bucket objects are children of the S3 bucket resource, and when running the command against resources that have children, all of the children of that resource will also be moved. Additionally, the relationships between all resources being moved is preserved.

Now run the `pulumi state move --source <SOURCE_STACK> --dest <DEST_STACK> <URN>` command, making sure to replace the following:

- `<SOURCE_STACK>` with the fully qualified stack name of the source stack
- `<DEST_STACK>` with the fully qualified stack name of the destination stack
- `<URN>` with the value of the S3 bucket URN

URNs can contain characters that get interpreted by the shell, so it is always a good idea to wrap them in single quotes (') when passing them as arguments:

```bash
$ pulumi state move \
--source v-torian-pulumi-corp/pulumi-state-move-tutorial/source \
--dest v-torian-pulumi-corp/pulumi-state-move-tutorial/destination \
'urn:pulumi:source::pulumi-state-move-tutorial::aws:s3/bucket:Bucket::b'
Planning to move the following resources from v-torian-pulumi-corp/pulumi-state-move-tutorial/source to v-torian-pulumi-corp/pulumi-state-move-tutorial/destination:

  - urn:pulumi:source::pulumi-state-move-tutorial::aws:s3/bucket:Bucket::b
  - urn:pulumi:source::pulumi-state-move-tutorial::aws:s3/bucket:Bucket$aws:s3/bucketObject:BucketObject::index.html
  - urn:pulumi:source::pulumi-state-move-tutorial::aws:s3/bucket:Bucket$aws:s3/bucketObject:BucketObject::random.html

The following resources being moved to v-torian-pulumi-corp/pulumi-state-move-tutorial/destination have dependencies on resources in v-torian-pulumi-corp/pulumi-state-move-tutorial/source:

  - urn:pulumi:source::pulumi-state-move-tutorial::aws:s3/bucket:Bucket$aws:s3/bucketObject:BucketObject::random.html has a dependency on urn:pulumi:source::pulumi-state-move-tutorial::random:index/randomPet:RandomPet::my-pet-name
  - urn:pulumi:source::pulumi-state-move-tutorial::aws:s3/bucket:Bucket$aws:s3/bucketObject:BucketObject::random.html (content) has a property dependency on urn:pulumi:source::pulumi-state-move-tutorial::random:index/randomPet:RandomPet::my-pet-name

If you go ahead with moving these dependencies, it will be necessary to create the appropriate inputs and outputs in the program for the stack the resources are moved to.

Do you want to perform this move? yes
Successfully moved resources from v-torian-pulumi-corp/pulumi-state-move-tutorial/source to v-torian-pulumi-corp/pulumi-state-move-tutorial/destination
```

{{< notes type="info" >}}

Depending on which stack you have as your currently active stack, you can either omit the `--source` or the `--dest` flags. For example, if `source` is your currently active stack, then you can omit the `--source` flag when running this command.

{{< /notes >}}

You will notice that even though we have only provided the URN for the S3 bucket as an argument, both the S3 bucket resource as well as the two bucket object resources are moved.

### Move to a different project

To demonstrate how to move a resource between two different projects, you will need to [create a second Pulumi project](/docs/clouds/aws/get-started/create-project/).

Then run the `pulumi stack ls --all` command to view your list of existing stacks:

## Add a resource alias

The `pulumi state move` only modifies the state file of the source and destination stacks. It does not modify the code of your program directly. With that being said, you will need to modify both programs to match the changes you have made. This can typically be accomplished by copy/pasting source code for the resources and/or components between the two codebases. Inputs and outputs of resources that were moved may need to be adjusted as part of this process. This can be done either by using stack references, or recreating the inputs in the program.

## Clean-up

{{< cleanup >}}

## Next steps
