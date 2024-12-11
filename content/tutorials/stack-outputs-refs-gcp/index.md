---
title: "Reference Google Cloud Resources Across Stacks"
title_tag: "Reference Google Cloud Resources Across Stacks"
layout: single

# A succinct description of the tutorial. It appears on the Tutorials home and collection pages.
description: Learn more about exporting and referencing stack outputs in Pulumi.

# A similar description used for search results and social-media previews.
meta_desc: Learn more about exporting and referencing stack outputs in Pulumi.

# An image for the tutorial. It appears on tutorial page and in social-media previews.
meta_image: stack-ref-gcp-meta.png

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
    In this tutorial, you will learn how to work with stack outputs, specifically how to export values from a stack and how to reference those values from another stack. You will do this by creating simple Google Cloud Storage Bucket and custom IAM Role resources in one stack. You will then create a Bucket Object resource in a second project/stack that will upload a file to the bucket created in the first stack.

# A list of three to five things the reader will have learned by the end of the tutorial.
youll_learn:
    - How to create a stack output
    - How to view the stack output
    - How to reference the output from a different stack

# A list of tutorial prerequisites. Markdown is fine. Keep it simple; no need to be exhaustive here.
prereqs:
    - The [Pulumi CLI](/docs/install/)
    - A [Pulumi Cloud account](https://app.pulumi.com/signup) and [access token](/docs/pulumi-cloud/accounts/#access-tokens)
    - A [Google Cloud account](https://cloud.google.com/cloud-console)
    - The [Google Cloud CLI](https://cloud.google.com/sdk/docs/install)
    - Familiarity with one of [Pulumi's supported languages](/docs/iac/languages-sdks/)

# The estimated time, in minutes, for new users to complete the topic.
estimated_time: 15

# # An optional list of collections this tutorial should be belong to. Collections are defined in data/tutorials/collections.yaml.
collections:
    - gcp
---

## Understanding stack outputs

Every Pulumi resource has outputs, which are properties of that resource whose values are generated during deployment. You can export these values as stack outputs, and they can be used for important values like resource IDs, computed IP addresses, and DNS names.

These outputs are shown during an update, can be easily retrieved with the Pulumi CLI, and are displayed in Pulumi Cloud. For the purposes of this tutorial, you will primarily be working from the CLI.

### Create a new project

```bash
# Example using Python
$ mkdir pulumi-tutorial-gcp
$ cd pulumi-tutorial-gcp
$ pulumi new gcp-python
```

Then replace the default code with the following code snippet to scaffold your project with the required imports and overall program structure:

{{< chooser language "javascript,typescript,python,go,csharp,yaml" / >}}

{{% choosable language javascript %}}

```javascript
{{< example-program-snippet path="gcp-storage-bucket-object" language="javascript" from="1" to="21" >}}
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="gcp-storage-bucket-object" language="typescript" from="1" to="20" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="gcp-storage-bucket-object" language="python" from="1" to="26" >}}
```

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="gcp-storage-bucket-object" language="go" from="1" to="41" >}}

{{< example-program-snippet path="gcp-storage-bucket-object" language="go" from="64" to="66" >}}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
{{< example-program-snippet path="gcp-storage-bucket-object" language="csharp" from="1" to="31" >}}

{{< example-program-snippet path="gcp-storage-bucket-object" language="csharp" from="48" to="48" >}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{< example-program-snippet path="gcp-storage-bucket-object" language="yaml" from="1" to="27" >}}
```

{{% /choosable %}}

This baseline code defines the following on your behalf:

- an [IAM Custom Role](/registry/packages/gcp/api-docs/projects/iamcustomrole/)
- a [Storage Bucket](/registry/packages/gcp/api-docs/storage/bucket/)
- an [IAM Role Assignment](/registry/packages/gcp/api-docs/projects/iammember/)

## Export resource values

As mentioned in the [Creating Resources on Google Cloud tutorial](/tutorials/creating-resources-gcp/), every resource has various properties. For any resources that you define in your Pulumi projects, you can [export the values](/docs/iac/concepts/stacks/#outputs) of its properties from your program as outputs. You can view a list of available properties that can be exported by referring to the resource properties section of a particular resource's API documentation (e.g. [Bucket properties](https://www.pulumi.com/registry/packages/gcp/api-docs/storage/bucket/#properties)). The `export` syntax is as follows:

{{< chooser language "javascript,typescript,python,go,csharp,yaml" / >}}

{{% choosable language javascript %}}

```javascript
exports.<output-name> = <output-value>;
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
export const <output-name> = <output-value>;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
pulumi.export("<output-name>", <output-value>)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
ctx.Export("<output-name>", <output-value>)
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
return await Pulumi.Deployment.RunAsync(() =>
{

    return new Dictionary<string, object?>
    {
        ["<output-name>"] = <output-value>
    };

});
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
outputs:
  <output-name>: ${<output-value>}
```

{{% /choosable %}}

When defining these exports, you'll need to provide two arguments:

| Argument | Description |
|--------------|-------------|
| Output name | This is the name you will use as the identifier of your output value |
| Output value | This is the actual value of your output |

To demonstrate how this works, let's export the name of your IAM Role. By referring to the documentation, you can see that the name of the IAM Role can be referenced via its `role ID` property, so update your code to reflect that as shown below:

{{< chooser language "javascript,typescript,python,go,csharp,yaml" / >}}

{{% choosable language javascript %}}

```javascript
{{< example-program-snippet path="gcp-storage-bucket-object" language="javascript" from="1" to="21" >}}

{{< example-program-snippet path="gcp-storage-bucket-object" language="javascript" from="32" to="32" >}}
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="gcp-storage-bucket-object" language="typescript" from="1" to="20" >}}

{{< example-program-snippet path="gcp-storage-bucket-object" language="typescript" from="31" to="31" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="gcp-storage-bucket-object" language="python" from="1" to="26" >}}

{{< example-program-snippet path="gcp-storage-bucket-object" language="python" from="40" to="40" >}}
```

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="gcp-storage-bucket-object" language="go" from="1" to="41" >}}

{{< example-program-snippet path="gcp-storage-bucket-object" language="go" from="62" to="62" >}}

{{< example-program-snippet path="gcp-storage-bucket-object" language="go" from="64" to="66" >}}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
{{< example-program-snippet path="gcp-storage-bucket-object" language="csharp" from="1" to="31" >}}

{{< example-program-snippet path="gcp-storage-bucket-object" language="csharp" from="43" to="45" >}}
{{< example-program-snippet path="gcp-storage-bucket-object" language="csharp" from="47" to="48" >}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{< example-program-snippet path="gcp-storage-bucket-object" language="yaml" from="1" to="27" >}}

{{< example-program-snippet path="gcp-storage-bucket-object" language="yaml" from="40" to="41" >}}
```

{{% /choosable %}}

## Deploy your resources

Now save your file and run the `pulumi up` command to preview and deploy the resources you've just defined in your project.

```bash
$ pulumi up -y
Previewing update (stack-outputs)

     Type                           Name               Plan
 +   pulumi:pulumi:Stack            gcp-stack-outputs  create
 +   ├─ gcp:projects:IAMCustomRole  bucketViewerRole   create
 +   └─ gcp:storage:Bucket          my-bucket          create

Outputs:
    roleName: output<string>

Resources:
    + 3 to create

Updating (stack-outputs)

     Type                           Name               Status
 +   pulumi:pulumi:Stack            gcp-stack-outputs  created (6s)
 +   ├─ gcp:storage:Bucket          my-bucket          created (1s)
 +   └─ gcp:projects:IAMCustomRole  bucketViewerRole   created (2s)

Outputs:
    roleName: "bucketViewerRole"

Resources:
    + 3 created

Duration: 8s
```

You can see that the output you've created has been provided as a part of the update details. You will learn the different ways you can access this output in the next steps of the tutorial.

## Access outputs via the CLI

Now that your resources are deployed, you can access its value either via the CLI or via your Pulumi program code. To access it via the CLI, you can use the [`pulumi stack output` command](/docs/iac/cli/commands/pulumi_stack_output/). Running this command by itself will list the names and values of all of the exports in your program:

```bash
$ pulumi stack output

Current stack outputs (1):
    OUTPUT    VALUE
    roleName  bucketViewerRole
```

If you want to retrieve a specific output value, you will need to provide the name of your desired output as shown below:

```bash
$ pulumi stack output roleName

bucketViewerRole
```

This can be especially useful if you have any workflow scripts that depend on the outputs of your program. For example, if you wanted to view the details of your IAM Role using the Google Cloud CLI, you can do so by running the [`gcloud iam roles describe` command](https://cloud.google.com/sdk/gcloud/reference/iam/roles/describe) and passing the output of `roleName` to the command, making sure to replace the value of `<YOUR_PROJECT_NAME>` with the name of your Google Cloud project:

```bash
$ gcloud iam roles describe --project=<YOUR_PROJECT_NAME> $(pulumi stack output roleName)

etag: BwYm3xAUufQ=
includedPermissions:
- storage.objects.get
- storage.objects.list
name: projects/pulumi-devrel/roles/bucketViewerRole
stage: GA
title: Bucket Viewer Role
```

You have seen how you can reference your output values from the CLI. Now let’s take a look at how you can do the same from within another Pulumi program stack.

## Access outputs via stack reference

Stack references allow you to access the outputs of one stack from another stack. This enables developers to create resources even when there are inter-stack dependencies. For this section, you are going to create a new Pulumi program that will access stack output values from your existing program.

### Reference resource group name

Start by making a new Pulumi project in a new directory. In this new program, you will need to add the code that will reference an output value from your first program. This can be done using Pulumi's [Stack Reference functionality](/docs/concepts/stack/#stackreferences). When defining a stack reference in code, you will need to pass in the fully qualified name of the stack as an argument. This name is comprised of the [organization](/docs/pulumi-cloud/organizations/), [project](/docs/iac/concepts/projects/), and [stack](/docs/iac/concepts/stacks/) names in the format of `<organization>/<project>/<stack>`

For example, if the name of your organization is `acmecorp`, the name of your first program is `infra`, and the name of your stack is `dev`, then your fully qualified name will be `acmecorp/infra/dev`.

With that being said, a stack reference will look like the following in your code:

{{< chooser language "javascript,typescript,python,go,csharp,yaml" / >}}

{{% choosable language javascript %}}

```javascript
"use strict";
const pulumi = require("@pulumi/pulumi");

const stackRef = new pulumi.StackReference("acmecorp/infra/dev");
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";

const stackRef = new pulumi.StackReference("acmecorp/infra/dev");
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi

stack_ref = pulumi.StackReference("acmecorp/infra/dev")
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
        stackRef, err := pulumi.NewStackReference(ctx, "acmecorp/infra/dev", nil)
        if err != nil {
            return err
        }

		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;

return await Pulumi.Deployment.RunAsync(() =>
{

    var stackRef = new StackReference("acmecorp/infra/dev");

});
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: my-second-app-dev
runtime: yaml
description: A program to create a Stack Reference

resources:
  stack-ref:
    type: pulumi:pulumi:StackReference
    properties:
      name: acmecorp/infra/dev
```

{{% /choosable %}}

{{% notes type="info" %}}

Make sure that the fully qualified name in the example above is populated with the values that are specific to your Pulumi organization, project, and stack.

{{% /notes %}}

You will now create an export in your second program that will output the value of the role name from your first program. This is to demonstrate how to retrieve output values from another stack for use in your program.

For the value of your export, you can retrieve it by taking your stack reference variable and using a Stack Reference function called getOutput() against it.

Update your code with the following:

{{< chooser language "javascript,typescript,python,go,csharp,yaml" / >}}

{{% choosable language javascript %}}

```javascript
"use strict";
const pulumi = require("@pulumi/pulumi");

// Retrieve the output values from the first stack
const stackRef = new pulumi.StackReference("acmecorp/infra/dev");

// Retrieve the role name from the output values
const roleName = stackRef.getOutput("roleName");

exports.roleName = roleName;
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";

// Retrieve the output values from the first stack
const stackRef = new pulumi.StackReference("acmecorp/infra/dev");

// Retrieve the role name from the output values
const roleName = stackRef.getOutput("roleName");

export const roleName = roleName;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi

# Retrieve the output values from the first stack
stack_ref = pulumi.StackReference("acmecorp/infra/dev")

# Retrieve the role name from the output values
role_name = stack_ref.get_output("roleName")

pulumi.export("roleName", role_name)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
        // Retrieve the output values from the first stack
        stackRef, err := pulumi.NewStackReference(ctx, "acmecorp/infra/dev", nil)
        if err != nil {
            return err
        }

        // Retrieve the role name from the output values
        roleName := stackRef.GetOutput(pulumi.String("roleName"))

        ctx.Export("roleName", roleName)
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;

return await Pulumi.Deployment.RunAsync(() =>
{
    // Retrieve the output values from the first stack
    var stackRef = new StackReference("acmecorp/infra/dev");

    // Retrieve the role name from the output values
    var roleName = stackRef.GetOutput("roleName");

    return new Dictionary<string, object?>
    {
        ["roleName"] = roleName
    };

});
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: my-second-app-dev
runtime: yaml
description: A program to create a Stack Reference

resources:
  # Retrieve the output values from the first stack
  stack-ref:
    type: pulumi:pulumi:StackReference
    properties:
      name: acmecorp/infra/dev

variables:
  # Retrieve the role name from the output values
  roleName: ${stack-ref.outputs["roleName"]}

outputs:
  roleName: ${roleName}
```

{{% /choosable %}}

To verify that your stack reference is working, run `pulumi up`.

```bash
$ pulumi up -y

Previewing update (dev):

     Type                      Name                     Plan
 +   pulumi:pulumi:Stack  my-second-app-dev             create

Outputs:
    roleName: output<string>

Resources:
    + 4 to create

Do you want to perform this update? yes
Updating (dev):

     Type                      Name                     Status
 +   pulumi:pulumi:Stack  my-second-app-dev             created (2s)

Outputs:
    roleName: "bucketViewerRole"

Resources:
    + 4 created

Duration: 3s
```

You should see the name of your IAM role from your first program successfully outputted in the update details of your second program.

## Use stack reference in resource definition

In this section, you will use everything you have learned in this tutorial to define a resource that uses a stack reference in the resource definition. In your second program, you will be defining a bucket object resource that will upload a file to the Storage Bucket that was created in your first program. Use the following steps as a guide for adding the Blob resource:

- Navigate to the [Google Cloud Registry documentation page](/registry/packages/gcp/)
- Search for the `gcp.storage.BucketObject` resource
- Define the Bucket Object resource in your second program code
- Export required property values in your first program code
- Import required property values in your second program
- Save and deploy your first program code
- Then save and deploy your second program code

Once you have completed these steps, you can verify that the object was successfully created and uploaded to the conbuckettainer by navigating to `Cloud Storage -> Buckets -> <YOUR_PROJECT_NAME> -> <YOUR_BUCKET_NAME>` in the Google Cloud Portal.

## View complete solution

You can view the code for the complete solution below.

### First program code

{{< chooser language "javascript,typescript,python,go,csharp,yaml" / >}}

{{% choosable language javascript %}}

```javascript
{{< example-program-snippet path="gcp-storage-bucket-object" language="javascript" from="1" to="21" >}}

{{< example-program-snippet path="gcp-storage-bucket-object" language="javascript" from="32" to="33" >}}
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="gcp-storage-bucket-object" language="typescript" from="1" to="20" >}}

{{< example-program-snippet path="gcp-storage-bucket-object" language="typescript" from="31" to="32" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="gcp-storage-bucket-object" language="python" from="1" to="26" >}}

{{< example-program-snippet path="gcp-storage-bucket-object" language="python" from="40" to="41" >}}
```

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="gcp-storage-bucket-object" language="go" from="1" to="41" >}}

{{< example-program-snippet path="gcp-storage-bucket-object" language="go" from="62" to="66" >}}

```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
{{< example-program-snippet path="gcp-storage-bucket-object" language="csharp" from="1" to="31" >}}

{{< example-program-snippet path="gcp-storage-bucket-object" language="csharp" from="43" to="48" >}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{< example-program-snippet path="gcp-storage-bucket-object" language="yaml" from="1" to="27" >}}

{{< example-program-snippet path="gcp-storage-bucket-object" language="yaml" from="40" to="42" >}}
```

{{% /choosable %}}

### Second program code

{{< chooser language "javascript,typescript,python,go,csharp,yaml" / >}}

{{% choosable language javascript %}}

```javascript
"use strict";
const pulumi = require("@pulumi/pulumi");

const stackRef = new pulumi.StackReference("acmecorp/infra/dev");

const roleName = stackRef.getOutput("roleName");
const bucketName = stackRef.getOutput("bucketName");

{{< example-program-snippet path="gcp-storage-bucket-object" language="javascript" from="26" to="30" >}}
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";

const stackRef = new pulumi.StackReference("acmecorp/infra/dev");

const roleName2 = stackRef.getOutput("roleName");
const bucketName2 = stackRef.getOutput("bucketName");

{{< example-program-snippet path="gcp-storage-bucket-object" language="typescript" from="25" to="29" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi

stack_ref = pulumi.StackReference("acmecorp/infra/dev")

role_name = stack_ref.get_output("roleName")
bucket_name = stack_ref.get_output("bucketName")

{{< example-program-snippet path="gcp-storage-bucket-object" language="python" from="33" to="38" >}}
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
        stackRef, err := pulumi.NewStackReference(ctx, "acmecorp/infra/dev", nil)
        if err != nil {
            return err
        }

        roleName := stackRef.GetOutput(pulumi.String("roleName"))
        bucketName := stackRef.GetOutput(pulumi.String("bucketName"))


{{< example-program-snippet path="gcp-storage-bucket-object" language="go" from="51" to="60" >}}

		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;

return await Pulumi.Deployment.RunAsync(() =>
{

    var stackRef = new StackReference("acmecorp/infra/dev");

    var roleName = stackRef.GetOutput("roleName");
    var bucketName = stackRef.GetOutput("bucketName");

{{< example-program-snippet path="gcp-storage-bucket-object" language="csharp" from="36" to="41" >}}

});
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: infra
runtime: yaml
description: A program to create a Stack Reference

resources:
  stack-ref:
    type: pulumi:pulumi:StackReference
    properties:
      name: acmecorp/infra/dev

{{< example-program-snippet path="gcp-storage-bucket-object" language="yaml" from="29" to="34" >}}

variables:
  roleName: ${stack-ref.outputs["roleName"]}
  bucketName: ${stack-ref.outputs["bucketName"]}
```

{{% /choosable %}}

## Clean up

{{< cleanup >}}

## Next steps

In this tutorial, you created a Google Cloud Storage Bucket and custom IAM role. You also referenced the documentation to create a storage object that would upload a file to the bucket. You exported resource properties into stack outputs, and referenced those outputs across stacks using stack references.

To learn more about creating and managing resources in Pulumi, take a look at the following resources:

- Learn more about creating resources in the [Creating Resources on Google Cloud tutorial](/tutorials/creating-resources-gcp/).
- Learn more about [stack outputs and references](/docs/concepts/stack/#stackreferences) in the Pulumi documentation.
- Learn more about [Pulumi inputs and outputs](/docs/concepts/inputs-outputs/) in the Pulumi documentation.
