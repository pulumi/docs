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
    There are certain scenarios in which you might need to move resources between different project stacks without recreating them, such as when refactoring a Pulumi project from a monolithic structure to micro-stacks. While it is possible to accomplish this by manually modifying Pulumi state files, doing so requires significant effort, can be error prone, and can be very time consuming.
    
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

Given that this example program makes use of the Pulumi Random provider, you will also need to make sure to [install this dependency into your project](https://github.com/pulumi/pulumi-random?tab=readme-ov-file#installing). Once that is installed, run the `pulumi up` command to deploy your resources before moving onto the next steps.

## Review the `pulumi state move` command

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

Both the `--dest` and `--source` flags can be either stacks in the current project, or stacks in across different projects. The resources being moved have to be specified by their full [Uniform Resource Name (URN)](/docs/concepts/resources/names/#urns), and multiple URNs can be passed at once for scenarios in which you need to move multiple resources at once.

{{< notes type="info" >}}

This command will only work for stacks that exist within the same backend. It is currently not possible to move a resource between different backends, but you can move stacks between backends using other existing tools. Please refer to the [Migrating Between State Backends](/docs/concepts/state/#migrating-between-state-backends) documentation for more information.

{{< /notes >}}

## Move a resource between stacks

Let's say you have a situation where your program code has grown too large, and you want to group the AWS resources separately from the Random resource. This means you want to move the S3 bucket and its bucket objects to a separate stack. In this section, you will learn how to move these resource into the state file of a different stack.

### Create an additional stack

To start, [create a second Pulumi project](/docs/clouds/aws/get-started/create-project/) to where you will move your AWS resources.

From within the original project folder, run the `pulumi stack ls --all` command to verify the existence of your stacks:

```bash
$ pulumi stack ls

NAME                                                                LAST UPDATE     RESOURCE COUNT  URL
source*                                                             37 minutes ago  7               https://app.pulumi.com/v-torian-pulumi-corp/pulumi-state-move-tutorial/source
v-torian-pulumi-corp/pulumi-state-move-dest/dest-project            n/a             n/a             https://app.pulumi.com/v-torian-pulumi-corp/pulumi-state-move-dest/dest-project
```

### Retrieve fully qualified stack names

Next, you will need to collect the fully qualified stack names of the source and destination stacks. The format of a stack's fully qualified name is `<organization>/<project>/<stack>`. In the `URL` column of the output in the above section, you can see the value of each stack's fully qualified name after the `https://app.pulumi.com/` part of the URL. An example of a fully qualified stack name is shown below:

```bash
v-torian-pulumi-corp/pulumi-state-move-dest/dest-project
```

### Retrieve resource URN

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

In this scenario, you only need the URN of the S3 bucket resource and not the URNs for the bucket objects. This is because the bucket objects are children of the S3 bucket resource, and when running the `pulumi state move` command against resources that have children, all of the children of that resource will also be moved.

### Move the resource

Now run the following command, making sure to replace `<SOURCE_STACK>` with the fully qualified stack name of the source stack, `<DEST_STACK>` with the fully qualified stack name of the destination stack, and `<URN>` with the value of the S3 bucket URN.

```bash
pulumi state move \
--source <SOURCE_STACK> \
--dest <DEST_STACK> \
<URN>
```

Since URNs can contain characters that get interpreted by the shell, it is always a good idea to wrap them in single quotes (') when passing them as arguments as shown in the example below:

```bash
$ pulumi state move \
--source v-torian-pulumi-corp/pulumi-state-move-tutorial/source \
--dest v-torian-pulumi-corp/pulumi-state-move-dest/dest-project \
'urn:pulumi:source::pulumi-state-move-tutorial::aws:s3/bucket:Bucket::b'

Planning to move the following resources from v-torian-pulumi-corp/pulumi-state-move-tutorial/source to v-torian-pulumi-corp/pulumi-state-move-dest/dest-project:

  - urn:pulumi:source::pulumi-state-move-tutorial::aws:s3/bucket:Bucket::b
  - urn:pulumi:source::pulumi-state-move-tutorial::aws:s3/bucket:Bucket$aws:s3/bucketObject:BucketObject::index.html
  - urn:pulumi:source::pulumi-state-move-tutorial::aws:s3/bucket:Bucket$aws:s3/bucketObject:BucketObject::random.html

The following resources being moved to v-torian-pulumi-corp/pulumi-state-move-dest/dest-project have dependencies on resources in v-torian-pulumi-corp/pulumi-state-move-tutorial/source:

  - urn:pulumi:source::pulumi-state-move-tutorial::aws:s3/bucket:Bucket$aws:s3/bucketObject:BucketObject::random.html has a dependency on urn:pulumi:source::pulumi-state-move-tutorial::random:index/randomPet:RandomPet::my-pet-name
  - urn:pulumi:source::pulumi-state-move-tutorial::aws:s3/bucket:Bucket$aws:s3/bucketObject:BucketObject::random.html (content) has a property dependency on urn:pulumi:source::pulumi-state-move-tutorial::random:index/randomPet:RandomPet::my-pet-name

If you go ahead with moving these dependencies, it will be necessary to create the appropriate inputs and outputs in the program for the stack the resources are moved to.

Do you want to perform this move? yes
Successfully moved resources from v-torian-pulumi-corp/pulumi-state-move-tutorial/source to v-torian-pulumi-corp/pulumi-state-move-dest/dest-project
```

There are a few things to note about the example above:

- When moving resources from the currently selected stack, you can omit the `--source` argument and use only `--dest` argument.
- When moving resources between stacks across different projects, you will need to use the fully qualified stack name. When moving resources between stacks within the same project, you can pass just the name of the stack.
- Before the resources are moved, the command gives a list of resources that will be moved. You will notice that even though you have only provided the URN for the S3 bucket as an argument, the command indicates that both the S3 bucket resource as well as the two child bucket objects will be moved.
- The output also warns you about any dependencies that will not be transferred to the destination stack. When dealing with cross-project stacks, you will need to create the appropriate inputs and outputs in the program of the destination stack, and you will learn how to do this in the next section.

## Update program code

The `pulumi state move` only modifies the state file of the source and destination stacks. It does not modify the code of your program directly. In the case of moving resources between stacks across different programs, you will need to modify both programs to match the changes you have made. This can typically be accomplished by copy/pasting source code for the resources and/or components between the two program files.

Additionally, inputs and outputs of resources that were moved may need to be adjusted as part of this process. This can be done either by using stack references or by recreating the inputs in the program.

### Update source program code

First, start by removing the AWS resources from your source program code. You can copy and paste these resource definitions safely to the side as you will be adding them to the destination program code in a later step. Update your source program code so that it resembles the following:

{{< chooser language "javascript,typescript,python,go,csharp,yaml" / >}}

{{% choosable language javascript %}}

```javascript
{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="javascript" from="1" to="2" >}}

{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="javascript" from="5" to="5" >}}

{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="javascript" from="27" to="27" >}}
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="typescript" from="1" to="2" >}}

{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="typescript" from="5" to="5" >}}

{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="typescript" from="27" to="27" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="python" from="1" to="2" >}}

{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="python" from="5" to="5" >}}

{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="python" from="21" to="21" >}}
```

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="go" from="1" to="3" >}}
{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="go" from="5" to="15" >}}

{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="go" from="38" to="41" >}}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="csharp" from="1" to="1" >}}
{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="csharp" from="3" to="8" >}}

{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="csharp" from="24" to="28" >}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="yaml" from="1" to="7" >}}

{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="yaml" from="25" to="26" >}}
```

{{% /choosable %}}

### Update destination program code

In your destination program code, you will need to add your AWS resource definitions. Additionally, you will need to add a stack reference to make use of the `PetName` export from the source program. Update your destination program code so that it resembles the following, making sure to replace the value of the fully qualified stack name with the name of your own source stack:

{{< chooser language "javascript,typescript,python,go,csharp,yaml" / >}}

{{% choosable language javascript %}}

```javascript
{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="javascript" from="1" to="1" >}}
{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="javascript" from="3" to="3" >}}

const stackRef = new pulumi.StackReference(`v-torian-pulumi-corp/pulumi-state-move-tutorial/source`)

{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="javascript" from="7" to="21" >}}
        content: stackRef.getOutput("PetName"),
{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="javascript" from="23" to="25" >}}
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="typescript" from="1" to="1" >}}
{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="typescript" from="3" to="3" >}}

const stackRef = new pulumi.StackReference(`v-torian-pulumi-corp/pulumi-state-move-tutorial/source`)

{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="typescript" from="7" to="21" >}}
        content: stackRef.getOutput("PetName"),
{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="typescript" from="23" to="25" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="python" from="1" to="1" >}}
{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="python" from="3" to="3" >}}

stack_ref = pulumi.StackReference("v-torian-pulumi-corp/pulumi-state-move-tutorial/source")

{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="python" from="7" to="16" >}}
    content=stack_ref.get_output("PetName")
{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="python" from="18" to="19" >}}
```

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="go" from="1" to="4" >}}
{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="go" from="6" to="10" >}}

        stackRef, err := pulumi.NewStackReference(ctx, "v-torian-pulumi-corp/pulumi-state-move-tutorial/source", nil)
        if err != nil {
            return err
        }

{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="go" from="17" to="31" >}}
            Content: stackRef.GetOutput("PetName"),
{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="go" from="33" to="36" >}}
{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="go" from="40" to="41" >}}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="csharp" from="1" to="2" >}}
{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="csharp" from="4" to="7" >}}
    var stackRef = new StackReference("v-torian-pulumi-corp/pulumi-state-move-tutorial/source");

{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="csharp" from="10" to="20" >}}
        Content = stackRef.GetOutput("PetName")
{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="csharp" from="22" to="22" >}}
{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="csharp" from="28" to="28" >}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="yaml" from="1" to="2" >}}

{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="yaml" from="5" to="5" >}}
  stack-ref:
    type: pulumi:pulumi:StackReference
    properties:
      name: v-torian-pulumi-corp/pulumi-state-move-tutorial/source
{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="yaml" from="8" to="20" >}}
      content: ${stack-ref.outputs["PetName"]}
{{< example-program-snippet path="aws-s3bucket-s3objects-random" language="yaml" from="22" to="23" >}}
```

{{% /choosable %}}

## Clean-up

{{< cleanup >}}

## Next steps

In this tutorial, you created a Pulumi Random resource and AWS S3 resources. You used the `pulumi state move` command to migrate the AWS resources from the state file of a source project to a destination project. You also updated both the source and destination project code to match the changes made.

To learn more about creating and managing resources in Pulumi, take a look a the following resources:

- Learn more about Pulumi state and backends in the [Managing Pulumi State and Backend Options documentation](/docs/concepts/state/).
- Learn more about the `pulumi state` command and its subcommands in the [Pulumi State CLI documentation](/docs/cli/commands/pulumi_state/).
- Learn more about Pulumi stacks in the [Stacks concept documentation](/docs/concepts/stack/).
- Learn more about the `pulumi stack` command and its subcommands in the [Pulumi Stack CLI documentation](https://www.pulumi.com/docs/cli/commands/pulumi_stack/).
