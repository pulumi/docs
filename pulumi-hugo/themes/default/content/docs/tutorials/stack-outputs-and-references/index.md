---
title_tag: "Stack Outputs and References | Tutorials"
meta_desc: Learn more about exporting and referencing stack outputs in Pulumi.
title: "Stack Outputs and References"
h1: "Stack Outputs and References"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  usingpulumi:
    identifier: stack-outputs-refs
    weight: 1
tags:
    - aws
    - fundamentals
    - resources
    - stack-outputs
    - stack-references
    - python
    - tutorial
---

{{< youtube S-KfMsh78H8 >}}

<br>

In this tutorial, you will learn how to work with stack outputs, specifically how to export values from a stack and how to reference those values from another stack. You will do this by creating a simple AWS Lambda Function that will write a file to an S3 bucket. You will also create an EventBridge Scheduler resource in a new stack that will run the Lambda function from the first stack on a scheduled basis.

## Pre-Requisites

This tutorial assumes that you are familiar with the basics of the Pulumi workflow. If you are new to Pulumi, complete the [Get Started series](/docs/get-started/) first.

Additionally, you will need the following tools to complete this tutorial:

- A [Pulumi account](https://app.pulumi.com)
  - [Optional] Create an [access token](/docs/pulumi-cloud/access-management/access-tokens/)
- The [Pulumi CLI](https://www.pulumi.com/docs/install/)
- An [Amazon Web Services](https://aws.amazon.com/) account
- The [AWS CLI](https://aws.amazon.com/cli/)
- One of the following languages installed:
  - Node.js version 14 or later (for Typescript/Javascript)
  - Python version 3.7 or later

Let's get started!

## Understanding Stack Outputs

Every Pulumi resource has outputs, which are properties of that resource whose values are generated during deployment. We can export these values as stack outputs, and they can be used for important values like resource IDs, computed IP addresses, and DNS names.

These outputs are shown during an update, can be easily retrieved with the Pulumi CLI, and are displayed in the Pulumi Cloud. For the purposes of this tutorial, we will primarily be working from the CLI.

### Create a New Project

{{< tutorials/create-new-proj >}}

{{< chooser language "typescript,python,yaml" / >}}

{{% choosable language typescript %}}

```typescript
{{% loadcode "code/typescript/baseline.txt" %}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{% loadcode "code/python/baseline.py" %}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{% loadcode "code/yaml/baseline.yaml" %}}
```

{{% /choosable %}}

### Create Project Resources

The first resource we will define in our project is a simple S3 bucket as shown below.

{{< chooser language "typescript,python,yaml" / >}}

{{% choosable language typescript %}}

```typescript
{{% loadcode "code/typescript/create-s3-bucket.txt" %}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{% loadcode "code/python/create-s3-bucket.py" %}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{% loadcode "code/yaml/create-s3-bucket.yaml" %}}
```

{{% /choosable %}}

The next resource we will add is a Lambda function with function code that will write a simple `.txt` file to our S3 bucket. We will also add an IAM role that will [grant our Lambda function permission](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html) to access AWS services and resources.

To start, let's create a new folder in our project named `s3_writer`. Inside of this folder, we'll create a file named `lambda_function.py` and populate it with code that will write a simple `.txt` file to our bucket.

```python
{{% loadcode "code/lambda-code.py" %}}
```

Now, we can add the [Lambda function resource definition](https://www.pulumi.com/registry/packages/aws/api-docs/lambda/function/) and its corresponding [IAM role](https://www.pulumi.com/registry/packages/aws/api-docs/iam/role/) to our main project file.

{{< chooser language "typescript,python,yaml" / >}}

{{% choosable language typescript %}}

```typescript
{{% loadcode "code/typescript/create-lambda-function.txt" %}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{% loadcode "code/python/create-lambda-function.py" %}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{% loadcode "code/yaml/create-lambda-function.yaml" %}}
```

{{% /choosable %}}

### Export Resource Values

Now that we have our project resources defined, we can [export the values](/docs/concepts/stack/#outputs) of various resource properties from our program. When defining these exports, we'll need to provide two arguments:

| Argument | Description |
|--------------|-------------|
| Output name | This is the name we will use as the identifier of our output value |
| Output value | This is the actual value of our output |

To demonstrate how this works, let's export the names of our Lambda function and S3 bucket. The [Pulumi documentation](https://www.pulumi.com/registry/packages/aws/api-docs/lambda/function/#outputs) provides more information about what properties are available to export for each resource.

We can reference both our Lambda function name and bucket name via their `id` property, and we'll update our code to reflect that as shown below:

{{< chooser language "typescript,python,yaml" / >}}

{{% choosable language typescript %}}

```typescript
{{% loadcode "code/typescript/add-lambda-s3-export.txt" %}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{% loadcode "code/python/add-lambda-s3-export.py" %}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{% loadcode "code/yaml/add-lambda-s3-export.yaml" %}}
```

{{% /choosable %}}

### Deploy your Project Resources

Now let’s save our file and run the `pulumi up` command to preview and deploy the resources we've just defined in our project.

```bash
Previewing update (dev):

     Type                      Name                     Plan
 +   pulumi:pulumi:Stack     my-first-app-dev           create
 +   ├─ aws:iam:Role         s3-writer-role             create
 +   ├─ aws:s3:Bucket        my-bucket                  create
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
 +   ├─ aws:s3:Bucket        my-bucket                  created (1s)
 +   └─ aws:lambda:Function  s3-writer-lambda-function  created (13s)

Outputs:
    lambdaName: "s3-writer-lambda-function-981d4fa"
    bucketName: "my-bucket-4fb1589"

Resources:
    + 4 created

Duration: 20s
```

We can see that the outputs we've created have been provided as a part of the update details. We'll access these outputs via the CLI in the next steps of the tutorial.

### Access Outputs via the CLI

Now that our resources are deployed, let's kick off our Lambda to S3 file writing process.

The first thing we will do is validate that our S3 bucket is empty. We can use the following [AWS CLI command](https://docs.aws.amazon.com/cli/latest/reference/s3api/list-objects-v2.html) to list all of the objects in our bucket:

```bash
aws s3api list-objects-v2 --bucket <bucket_name>
```

{{% notes type="info" %}}

The AWS CLI will run AWS commands with the `default` profile by default. If you would like to run commands with a different profile, take a look at the [relevant AWS documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) to learn how.

{{% /notes %}}

We will want to replace `<bucket_name>` with the actual name of our S3 bucket. While we can manually provide the name of our bucket, we can also programmatically reference our bucket name via the stack outputs.

We'll do this by using the [`pulumi stack output`](/docs/concepts/stack/#outputs) command and provide the name of our desired output as shown below:

```bash
aws s3api list-objects-v2 --bucket $(pulumi stack output bucketName)
```

Right now, our bucket is empty, so the response of this command should look like the following:

```bash
{
    "RequestCharged": null
}
```

Now, let's trigger our Lambda function so that it will write a new file to the bucket. We will use the [`aws lambda invoke`](https://docs.aws.amazon.com/cli/latest/reference/lambda/invoke.html) command and pass our Lambda function name to the `--function-name` option as shown below:

```bash
aws lambda invoke \
    --function-name $(pulumi stack output lambdaName) \
    --invocation-type Event \
    --cli-binary-format raw-in-base64-out \
    --payload '{ "test": "test" }' \
    response.json
```

We can verify the outcome of this function execution by running the same `list-objects-v2` command from before to check the contents of our S3 bucket. This time, we should see output similar to the following:

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

The `.txt` file in the `Key` field of the response object indicates that our Lambda function ran successfully.

We have seen how we can reference our output values from the CLI. Now let's take a look at how we can do the same from within another stack.

## Using Stack References

Stack references allow you to access the outputs of one stack from another stack. This enables developers to create resources even when there are inter-stack dependencies.

For this section, we are going to create a new Pulumi program that will access the stack output values from our existing program.

### Reference the Name of the Lambda Function

Let's start by making a new Pulumi project in a new directory. In this new program, we need to add the code that will reference the values from our first program.

This can be done using Pulumi's [Stack Reference functionality](/docs/concepts/stack/#stackreferences). We'll need to pass in the fully qualified name of the stack as an argument. This name is comprised of the [organization](/docs/pulumi-cloud/organizations/), project, and stack names in the format of `<organization>/<project>/<stack>`

For example, if the name of our organization is `my-org`, the name of our first program is `my-first-program`, and the name of our stack is `dev`, then our fully qualified name will be `my-org/my-first-program/dev`.

With that being said, a stack reference will look like the following in our code:

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

We will now create an export that will output the value of the Lambda function name from our first program. This is to demonstrate how to retrieve output values from another stack for use in your program.

For the value of our export, we can retrieve it by taking our `stack_ref` variable and using a Stack Reference function called `get_output()` against it.

Let's update our code with the following:

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

To check that our stack reference is working, let's run `pulumi up`.

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

We can see the name of our Lambda function from our first program successfully outputted in the update details of our second program.

### Run the Lambda Function on a Schedule

In this section, you will use Pulumi documentation to create an Eventbridge Scheduler resource in one stack that will trigger the Lambda function in another stack on a scheduled basis.

The scheduler should trigger the Lambda function to run once every minute.

An updated version of the Lambda Function project code has been provided below as a starting point.

{{< chooser language "typescript,python,yaml" / >}}

{{% choosable language typescript %}}

```typescript
{{% loadcode "code/typescript/updated-baseline-lambda.txt" %}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{% loadcode "code/python/updated-baseline-lambda.py" %}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{% loadcode "code/yaml/updated-baseline-lambda.yaml" %}}
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

{{< details "Click here to view the complete project code" >}}

{{< details "Here is the complete code for exporting the Lambda function ARN." >}}

{{< chooser language "typescript,python,yaml" / >}}

{{% choosable language typescript %}}

```typescript
{{% loadcode "code/typescript/create-lambda-arn-export.txt" %}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{% loadcode "code/python/create-lambda-arn-export.py" %}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{% loadcode "code/yaml/create-lambda-arn-export.yaml" %}}
```

{{% /choosable %}}

{{< /details >}}

{{< details "Here is the complete code for creating the EventBridge Scheduler." >}}

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

{{< /details >}}

{{< /details >}}

## Clean Up

{{< cleanup >}}

{{% notes type="warning" %}}

Make sure to empty the contents of your S3 bucket before deleting the resources or the deletion will fail.

{{% /notes %}}

## Next Steps

In this tutorial, you created a Lambda function that writes a file to an S3 bucket. You also referenced the documentation to create an EventBridge Scheduler that would run the Lambda function on a scheduled basis.

You exported Lambda properties into stack outputs, and referenced those outputs across stacks using stack references.

To learn more about creating and managing resources in Pulumi, take a look at the following resources:

- Learn more about [stacks ouputs and references](/docs/concepts/stack/#stackreferences) in the Pulumi documentation.
- Learn more about [Pulumi inputs and outputs](/docs/concepts/inputs-outputs/) in the Pulumi documentation.
