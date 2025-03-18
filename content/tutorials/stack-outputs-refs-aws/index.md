---
title: "Reference AWS Resources Across Stacks"
title_tag: "Reference AWS Resources Across Stacks"
layout: single

# A succinct description of the tutorial. It appears on the Tutorials home and collection pages.
description: Learn more about exporting and referencing stack outputs in Pulumi.

# A similar description used for search results and social-media previews.
meta_desc: Learn more about exporting and referencing stack outputs in Pulumi.

# # An image for the tutorial. It appears on tutorial page and in social-media previews.
# meta_image: meta.png

# An optional video for the tutorial. When present, it appears at the top of the page, replacing
# the meta image. YouTube and HTML5 video sources are supported.
video:
    youtube: Iqbo5Pa97JQ

# The order in which the tutorial appears in most lists. Order is ascending, so higher numbers
# mean the tutorial will appear further down the list. Positive integers only.
weight: 999

# A brief summary of the tutorial. It appears at the top of the tutorial page. Markdown is fine.
summary: |
    In this tutorial, you will learn how to work with stack outputs, specifically how to export values from a stack and how to reference those values from another stack. You will do this by creating a simple AWS Lambda Function that will write a file to an S3 bucket. You will also create an EventBridge Scheduler resource in a new stack that will run the Lambda function from the first stack on a scheduled basis.

# A list of three to five things the reader will have learned by the end of the tutorial.
youll_learn:
    - How to create a stack output
    - How to view the stack output
    - How to reference the output from a different stack

# A list of tutorial prerequisites. Markdown is fine. Keep it simple; no need to be exhaustive here.
prereqs:
    - A [Pulumi Cloud account](https://app.pulumi.com/signup) and [access token](/docs/pulumi-cloud/accounts/#access-tokens)
    - The [Pulumi CLI](/docs/install/)
    - An [Amazon Web Services](https://aws.amazon.com/) account
    - The [AWS CLI](https://aws.amazon.com/cli/)
    - "[Node.js](/docs/languages-sdks/javascript/) or [Python](/docs/languages-sdks/python/) installed"

# The estimated time, in minutes, for new users to complete the topic.
estimated_time: 15

# # An optional list of collections this tutorial should be belong to. Collections are defined in data/tutorials/collections.yaml.
collections:
    - aws

aliases:
  - /docs/using-pulumi/stack-outputs-and-references/
  - /tutorials/stack-outputs-and-references/
---

## Understanding stack outputs

Every Pulumi resource has outputs, which are properties of that resource whose values are generated during deployment. You can export these values as stack outputs, and they can be used for important values like resource IDs, computed IP addresses, and DNS names.

These outputs are shown during an update, can be easily retrieved with the Pulumi CLI, and are displayed in Pulumi Cloud. For the purposes of this tutorial, you will primarily be working from the CLI.

### Create a new project

{{< tutorials/create-new-proj >}}

{{< chooser language "typescript,python,yaml" / >}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="typescript" from="1" to="2" >}}

// [Step 1: Create an S3 bucket.]

// [Step 2: Create a Lambda function.]

// [Step 3: Create an export.]
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="python" from="1" to="2" >}}

# [Step 1: Create an S3 bucket.]

# [Step 2: Create a Lambda function.]

# [Step 3: Create an export.]
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: s3-writer
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="yaml" from="2" to="5" >}}
  # [Step 1: Create an S3 bucket.]

  # [Step 2: Create a Lambda function.]

  # [Step 3: Create an export.]
```

{{% /choosable %}}

### Create project resources

The first resource you will define in your project is a simple S3 bucket as shown below.

{{< chooser language "typescript,python,yaml" / >}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="typescript" from="1" to="2" >}}

// [Step 1: Create an S3 bucket.]
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="typescript" from="4" to="4" >}}

// [Step 2: Create a Lambda function.]

// [Step 3: Create an export.]
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="python" from="1" to="2" >}}

# [Step 1: Create an S3 bucket.]
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="python" from="4" to="4" >}}

# [Step 2: Create a Lambda function.]

# [Step 3: Create an export.]
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: s3-writer
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="yaml" from="2" to="5" >}}
  # [Step 1: Create an S3 bucket.]
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="yaml" from="6" to="7" >}}

  # [Step 2: Create a Lambda function.]

  # [Step 3: Create an export.]
```

{{% /choosable %}}

The next resource you will add is a Lambda function with function code that will write a simple `.txt` file to your S3 bucket. You will also add an IAM role that will [grant your Lambda function permission](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html) to access AWS services and resources.

Create a new folder in your project named `s3_writer`. Inside of this folder, you'll create a file named `lambda_function.py` and populate it with code that will write a simple `.txt` file to your bucket.

```python
import json
import os
import boto3
import datetime

s3 = boto3.resource('s3')

BUCKET_NAME = os.environ['BUCKET_NAME']

def lambda_handler(event, context):

    current_time = str(datetime.datetime.utcnow()).replace(" ", "")
    data_string = "Hello Pulumi!"

    object = s3.Object(
        bucket_name=BUCKET_NAME,
        key=f'{current_time}_test_file.txt'
    )

    object.put(Body=data_string)
```

Now, you can add the [Lambda function resource definition](https://www.pulumi.com/registry/packages/aws/api-docs/lambda/function/) and its corresponding [IAM role](https://www.pulumi.com/registry/packages/aws/api-docs/iam/role/) to your main project file.

{{< chooser language "typescript,python,yaml" / >}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="typescript" from="1" to="2" >}}

// [Step 1: Create an S3 bucket.]
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="typescript" from="4" to="4" >}}

// [Step 2: Create a Lambda function.]
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="typescript" from="6" to="18" >}}
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="typescript" from="20" to="35" >}}

// [Step 3: Create an export.]
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="python" from="1" to="2" >}}

# [Step 1: Create an S3 bucket.]
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="python" from="4" to="4" >}}

# [Step 2: Create a Lambda function.]
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="python" from="6" to="21" >}}
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="python" from="23" to="41" >}}

# [Step 3: Create an export.]
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: s3-writer
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="yaml" from="2" to="5" >}}
  # [Step 1: Create an S3 bucket.]
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="yaml" from="6" to="7" >}}

  # [Step 2: Create a Lambda function.]
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="yaml" from="9" to="30" >}}

{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="yaml" from="38" to="50" >}}

  # [Step 3: Create an export.]
```

{{% /choosable %}}

### Export resource values

Now that you have your project resources defined, you can [export the values](/docs/concepts/stack/#outputs) of various resource properties from your program. The `export` syntax is as follows:

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

To demonstrate how this works, let's export the names of your Lambda function and S3 bucket. The [Pulumi documentation](https://www.pulumi.com/registry/packages/aws/api-docs/lambda/function/#outputs) provides more information about what properties are available to export for each resource.

You can reference both your Lambda function name and bucket name via their `id` property, and you'll update your code to reflect that as shown below:

{{< chooser language "typescript,python,yaml" / >}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="typescript" from="1" to="2" >}}

// [Step 1: Create an S3 bucket.]
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="typescript" from="4" to="4" >}}

// [Step 2: Create a Lambda function.]
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="typescript" from="6" to="18" >}}
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="typescript" from="20" to="35" >}}

// [Step 3: Create an export.]
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="typescript" from="44" to="45" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="python" from="1" to="2" >}}

# [Step 1: Create an S3 bucket.]
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="python" from="4" to="4" >}}

# [Step 2: Create a Lambda function.]
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="python" from="6" to="21" >}}
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="python" from="23" to="41" >}}

# [Step 3: Create an export.]
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="python" from="50" to="51" >}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: s3-writer
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="yaml" from="2" to="5" >}}
  # [Step 1: Create an S3 bucket.]
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="yaml" from="6" to="7" >}}

  # [Step 2: Create a Lambda function.]
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="yaml" from="9" to="30" >}}

{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="yaml" from="38" to="50" >}}

# [Step 3: Create an export.]
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="yaml" from="60" to="62" >}}
```

{{% /choosable %}}

### Deploy your project resources

Now let’s save your file and run the `pulumi up` command to preview and deploy the resources you've just defined in your project.

```bash
Previewing update (dev):

     Type                      Name                     Plan
 +   pulumi:pulumi:Stack     my-first-app-dev           create
 +   ├─ aws:iam:Role         s3-writer-role             create
 +   ├─ aws:s3:BucketV2      my-bucket                  create
 +   └─ aws:lambda:Function  s3-writer-lambda-function  create

Outputs:
    lambdaName: output<string>
    bucketName: output<string>

Resources:
    + 4 to create

Do you want to perform this update? yes
Updating (dev):

     Type                      Name                     Status
 +   pulumi:pulumi:Stack     my-first-app-dev           created (18s)
 +   ├─ aws:iam:Role         s3-writer-role             created (1s)
 +   ├─ aws:s3:BucketV2      my-bucket                  created (1s)
 +   └─ aws:lambda:Function  s3-writer-lambda-function  created (13s)

Outputs:
    lambdaName: "s3-writer-lambda-function-981d4fa"
    bucketName: "my-bucket-4fb1589"

Resources:
    + 4 created

Duration: 20s
```

You can see that the outputs you've created have been provided as a part of the update details. You'll access these outputs via the CLI in the next steps of the tutorial.

### Access outputs via the CLI

Now that your resources are deployed, let's kick off your Lambda to S3 file writing process.

The first thing you will do is validate that your S3 bucket is empty. You can use the following [AWS CLI command](https://docs.aws.amazon.com/cli/latest/reference/s3api/list-objects-v2.html) to list all of the objects in your bucket:

```bash
aws s3api list-objects-v2 --bucket <bucket_name>
```

{{% notes type="info" %}}

The AWS CLI will run AWS commands with the `default` profile by default. If you would like to run commands with a different profile, take a look at the [relevant AWS documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) to learn how.

{{% /notes %}}

You will want to replace `<bucket_name>` with the actual name of your S3 bucket. While you can manually provide the name of your bucket, you can also programmatically reference your bucket name via the stack outputs.

You'll do this by using the [`pulumi stack output`](/docs/concepts/stack/#outputs) command and provide the name of your desired output as shown below:

```bash
aws s3api list-objects-v2 --bucket $(pulumi stack output bucketName)
```

Right now, your bucket is empty, so the response of this command should look like the following:

```bash
{
    "RequestCharged": null
}
```

Now, let's trigger your Lambda function so that it will write a new file to the bucket. You will use the [`aws lambda invoke`](https://docs.aws.amazon.com/cli/latest/reference/lambda/invoke.html) command and pass your Lambda function name to the `--function-name` option as shown below:

```bash
aws lambda invoke \
    --function-name $(pulumi stack output lambdaName) \
    --invocation-type Event \
    --cli-binary-format raw-in-base64-out \
    --payload '{ "test": "test" }' \
    response.json
```

You can verify the outcome of this function execution by running the same `list-objects-v2` command from before to check the contents of your S3 bucket. This time, you should see output similar to the following:

```bash
{
    "Contents": [
        {
            "Key": "2023-08-3107:53:28.137776_test_file.txt",
            "LastModified": "2023-08-31T07:53:29+00:00",
            "ETag": "\"f794802bfd4a70851294ba192d382c11\"",
            "Size": 13,
            "StorageClass": "STANDARD"
        }
    ],
    "RequestCharged": null
}
```

The `.txt` file in the `Key` field of the response object indicates that your Lambda function ran successfully.

You have seen how you can reference your output values from the CLI. Now let's take a look at how you can do the same from within another stack.

## Using stack references

Stack references allow you to access the outputs of one stack from another stack. This enables developers to create resources even when there are inter-stack dependencies.

For this section, you are going to create a new Pulumi program that will access the stack output values from your existing program.

### Reference the name of the Lambda function

Let's start by making a new Pulumi project in a new directory. In this new program, you need to add the code that will reference the values from your first program.

This can be done using Pulumi's [Stack Reference functionality](/docs/concepts/stack/#stackreferences). You'll need to pass in the fully qualified name of the stack as an argument. This name is comprised of the [organization](/docs/pulumi-cloud/admin/organizations/), project, and stack names in the format of `<organization>/<project>/<stack>`

For example, if the name of your organization is `my-org`, the name of your first program is `my-first-program`, and the name of your stack is `dev`, then your fully qualified name will be `my-org/my-first-program/dev`.

With that being said, a stack reference will look like the following in your code:

{{< chooser language "typescript,python,yaml" / >}}

{{% choosable language typescript %}}

```typescript
{{% loadcode "code/typescript/add-stack-reference.txt" %}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{% loadcode "code/python/add-stack-reference.py" %}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{% loadcode "code/yaml/add-stack-reference.yaml" %}}
```

{{% /choosable %}}

{{% notes type="info" %}}

Make sure that the fully qualified name in the example above is populated with the values that are specific to your Pulumi organization, project, and stack.

{{% /notes %}}

You will now create an export that will output the value of the Lambda function name from your first program. This is to demonstrate how to retrieve output values from another stack for use in your program.

For the value of your export, you can retrieve it by taking your stack reference variable and using a Stack Reference function called `getOutput()` against it.

Update your code with the following:

{{< chooser language "typescript,python,yaml" / >}}

{{% choosable language typescript %}}

```typescript
{{% loadcode "code/typescript/add-stack-ref-export.txt" %}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{% loadcode "code/python/add-stack-ref-export.py" %}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{% loadcode "code/yaml/add-stack-ref-export.yaml" %}}
```

{{% /choosable %}}

To check that your stack reference is working, let's run `pulumi up`.

```bash
Previewing update (dev):

     Type                      Name                     Plan
 +   pulumi:pulumi:Stack  my-second-app-dev             create

Outputs:
    firstProgramLambdaName: output<string>

Resources:
    + 4 to create

Do you want to perform this update? yes
Updating (dev):

     Type                      Name                     Status
 +   pulumi:pulumi:Stack  my-second-app-dev             created (2s)

Outputs:
    firstProgramLambdaName: "s3-writer-lambda-function-981d4fa"

Resources:
    + 1 created

Duration: 3s
```

You can see the name of your Lambda function from your first program successfully outputted in the update details of your second program.

### Run the Lambda function on a schedule

In this section, you will use Pulumi documentation to create an Eventbridge Scheduler resource in one stack that will trigger the Lambda function in another stack on a scheduled basis.

The scheduler should trigger the Lambda function to run once every minute.

An updated version of the Lambda Function project code has been provided below as a starting point.

{{< chooser language "typescript,python,yaml" / >}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="typescript" from="1" to="42" >}}

// [Step 3: Create an export.]
// TO-DO
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="python" from="1" to="48" >}}

# [Step 3: Create an export.]
# TO-DO
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: s3-writer
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="yaml" from="2" to="60" >}}
# [Step 3: Create an export.]
# TO-DO
```

{{% /choosable %}}

Some baseline code for the Scheduler project has also been provided below:

{{< chooser language "typescript,python,yaml" / >}}

{{% choosable language typescript %}}

```typescript
{{% loadcode "code/typescript/updated-baseline-scheduler.txt" %}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{% loadcode "code/python/updated-baseline-scheduler.py" %}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{% loadcode "code/yaml/updated-baseline-scheduler.yaml" %}}
```

{{% /choosable %}}

Use the following steps as a guide for adding the scheduling functionality:

- Export the Lambda function ARN from the Lambda project
- Create a stack reference for the Lambda function ARN in your Scheduler project code
- Navigate to the [AWS Registry documentation page](https://www.pulumi.com/registry/packages/aws/)
- Search for the Scheduler Schedule resource
- Define the Schedule resource in your Scheduler project code
- [Configure the Schedule](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule-schedule.html#eb-create-scheduled-rule-schedule) to trigger the Lambda function once every minute
- Preview and deploy your updated project code

Once you have completed these steps, wait a few minutes and then run the following command again:

```bash
aws s3api list-objects-v2 --bucket $(pulumi stack output bucketName)
```

You should then see a number of `.txt` files in your S3 bucket.

## View complete solution

You can view the code for the complete solution below.

### First program code

{{< chooser language "typescript,python,yaml" / >}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="typescript" from="1" to="4" >}}

{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="typescript" from="7" to="7" >}}

{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="typescript" from="9" to="42" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="python" from="1" to="48" >}}

{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="python" from="52" to="52" >}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: s3-writer
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="yaml" from="2" to="58" >}}

{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="yaml" from="60" to="60" >}}
{{< example-program-snippet path="aws-s3bucket-lambda-eventbridge" language="yaml" from="63" to="63" >}}
```

{{% /choosable %}}

### Second program code

{{< chooser language "typescript,python,yaml" / >}}

{{% choosable language typescript %}}

```typescript
{{% loadcode "code/typescript/create-eb-scheduler.txt" %}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{% loadcode "code/python/create-eb-scheduler.py" %}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{% loadcode "code/yaml/create-eb-scheduler.yaml" %}}
```

{{% /choosable %}}

## Clean up

{{< cleanup >}}

{{% notes type="warning" %}}

Make sure to empty the contents of your S3 bucket before deleting the resources or the deletion will fail.

{{% /notes %}}

## Next steps

In this tutorial, you created a Lambda function that writes a file to an S3 bucket. You also referenced the documentation to create an EventBridge Scheduler that would run the Lambda function on a scheduled basis.

You exported Lambda properties into stack outputs, and referenced those outputs across stacks using stack references.

To learn more about creating and managing resources in Pulumi, take a look at the following resources:

- Learn more about creating resources in the [Creating Resources on AWS tutorial](/tutorials/creating-resources-aws/).
- Learn more about [stack outputs and references](/docs/concepts/stack/#stackreferences) in the Pulumi documentation.
- Learn more about [Pulumi inputs and outputs](/docs/concepts/inputs-outputs/) in the Pulumi documentation.
