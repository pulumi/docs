---
title_tag: "Using AWS Lambda & Serverless Events | Crosswalk"
title: Using AWS Lambda & Serverless Events
meta_desc: Pulumi Crosswalk for AWS brings a more natural, and easier to use, way of building serverless applications using
           AWS Lambda.
linktitle: Lambda
menu:
  userguides:
    parent: crosswalk-aws
    weight: 9

aliases: ["/docs/reference/crosswalk/aws/lambda/"]
---

<a href="./">
    <img src="/images/docs/reference/crosswalk/aws/logo.svg" align="right" width="280" style="margin: 0 0 32px 16px;">
</a>

[AWS Lambda](https://aws.amazon.com/lambda/) lets you run code without provisioning or managing servers. You pay only
for the compute time you consume and there is no charge when your code is not running. With Lambda, you can run code
for virtually any type of application or backend service with zero administration. Just upload your code and Lambda
takes care of everything required to run and scale your code with high availability. You can set up your code to
automatically trigger from other AWS services or call it directly from any web or mobile app.

{{% notes type="info" %}}
This functionality is available in TypeScript only and as part of the [AWS Classic provider](/registry/packages/aws/).
{{% /notes %}}

## Overview

Pulumi Crosswalk for AWS brings a more natural, and easier to use, way of building serverless applications using
AWS Lambda. Pulumi lets you express Lambda functions using real code, and handles packaging, versioning, and
configuration of the associated AWS resources. This lets you focus on your application logic without needing to
worry about boilerplate, and with confidence that the resulting infrastructure automatically uses AWS best practices.

With Pulumi Crosswalk for AWS, event sources are available on all native resource types, including AWS S3, SQS,
DynamoDB, CloudWatch, Kinesis, and more, in addition to full support for [API Gateway](/docs/guides/crosswalk/aws/api-gateway/).
This improves discoverability of event sources in addition to adding strong typing to the event handler
inputs and outputs that AWS Lambda will deliver to your code.

## Available AWS Services with Event Sources

Below is a list of AWS Services and their available Lambda event sources:

<style>
table {
    margin-bottom: 20px;
    font-size: 14px;
}

td, th {
    padding: 8px 8px;
    text-align: left;
    border: 1px solid rgba(0,0,0,0.13);
}

thead tr th {
    background-color: #e0e0e0;
    font-weight: 800;
}

thead tr th:first-child {
    text-align: left;
}

tbody tr td:first-child {
    text-align: left;
}
</style>

| AWS Service | Event | Description |
|-------------|-------|-------------|
| API Gateway | [awsx.apigateway.API](/docs/reference/pkg/nodejs/pulumi/awsx/apigateway#API) | create serverless APIs using a simple approach |
| CloudWatch  | aws.cloudwatch.onSchedule | fire a CloudWatch event on a particular schedule, e.g. a cron expression |
| CloudWatch  | aws.cloudwatch.EventRule.onEvent | fire an event when a particular CloudWatch event occurs |
| CloudWatch  | aws.cloudwatch.LogGroup.onEvent | fire an event when a CloudWatch logs event occurs |
| DynamoDB    | aws.dynamodb.Table.onEvent | fire events for DynamoDB insert, modify, or remove operations |
| Kinesis     | aws.kinesis.Stream.onEvent | fire Kinesis Stream events at particular times or batch sizes |
| S3          | aws.s3.Bucket.onObjectCreated | trigger a function anytime an object is created in an S3 Bucket |
| S3          | aws.s3.Bucket.onObjectRemoved | trigger a function anytime an object is removed from an S3 Bucket |
| S3          | aws.s3.Bucket.onEvent | trigger a function for a wide range of S3 Bucket events |
| SNS         | aws.sns.Topic.onEvent | fire SNS Topic events when new messages arrive |
| SQS         | aws.sqs.Queue.onEvent | fire SQS Queue events when new messages are enqueued (or on DLQ events, etc) |

There are multiple approaches to creating a Lambda function. For these examples, we will trigger the Lambda's
execution when an S3 Bucket receives a new Object, however the manner of registering a handler is the same across
all of the above event sources. Refer to the API documentation links in the table above for detailed specifications
of the registration properties and event payloads.

## Registering a Lambda-based Serverless Event Handler

Most serverless programming models today treat the event sources -- e.g., S3 bucket, SQS queue, etc. -- and event
handlers -- the Lambdas and associated code -- as very different things. That is, the "infrastructure" is entirely
separate from the "app code", and managed with distinct tools and workflows. Pulumi, in contrast, uses one
programming model and CLI to manage both consistently.

You can create event sources and handlers in the same program, but Pulumi's approach is flexible, so that you can
elect to wire up new Lambda-based functions to existing resources -- such as if you already have core infrastructure
defined -- or even use functions that already exist, and glue them together with resources.

Because Pulumi provisions and manages resources, updating your functions after creating them is easy. Just edit your
code, run `pulumi up`, and Pulumi will diff and compute the minimal set of changes it can make to upgrade your code,
without any downtime required. This is as easy to do by hand as it is in
[CI/CD](/docs/guides/continuous-delivery).

### Register an Event Handler Using a Magic Lambda Function

One way to author a Lambda Function is to write it inline, within your Pulumi program. The Pulumi compiler and runtime
work in tandem to extract your function, package it up and upload it, and configure the resulting AWS Lambda resources.

For example, this code creates an S3 Bucket and executes an AWS Lambda anytime an Object is created within it:

```typescript
import * as aws from "@pulumi/aws";

// Create our bucket using infrastructure as code.
const docsBucket = new aws.s3.Bucket("docs");

// Create an AWS Lambda event handler on our bucket using magic functions.
docsBucket.onObjectCreated("docsHandler", (e) => {
    // your lambda code goes here
});
```

The `onObjectCreated` function blurs the line between infrastructure and application logic, and lets us focus
on what we want our code to do, rather than how it does it. This code looks like a typical event-driven program,
but is fully serverless so that it scales dynamically and you only pay for what you use.

> If the idea of mixing application and infrastructure logic like this is not appealing, don't worry; there are
> other approaches, including
> [allocating AWS Lambda Function objects explicitly](#register-an-event-handler-by-creating-a-lambda-function-resource)
> and [reusing existing functions](#register-an-event-handler-by-reusing-an-existing-lambda-function).

Nearly any code can go inside the body of that function. The JavaScript lambda may capture references to other
variables in the surrounding code, including other resources and event imported modules. The Pulumi compiler figures
out how to serialize the resulting closure as it uploads and configures the AWS Lambda. This works even if you
are composing multiple functions together. Just write code like usual -- that's why these are called _magic functions_.

#### Specifying Attributes on Your Magic Lambda Function

The Lambdas created by magic functions use reasonable defaults for CPU, memory, IAM, logging, and other configuration.
Should you need to change these settings, the `aws.lambda.CallbackFunction` class offers all of the underlying
settings, while also letting you use the magic function style of expressing the callback itself.

For example, let's say we want to increase the RAM available for our function from 128MB to 256MB:

```typescript
import * as aws from "@pulumi/aws";

// Create our bucket using infrastructure as code.
const docsBucket = new aws.s3.Bucket("docs");

// Create an AWS Lambda event handler on our bucket using magic functions.
docsBucket.onObjectCreated("docsHandler", new aws.lambda.CallbackFunction("docsHandlerFunc", {
    memorySize: 256 /*MB*/,
    callback: (e) => {
        // your lambda code goes here
    },
});
```

For more information about the properties available on `CallbackFunction`, refer to the [API documentation](
/registry/packages/aws/api-docs/lambda).

### Register an Event Handler by Creating a Lambda Function Resource

It is possible to create and register serverless event handlers by allocating `aws.lambda.Function` objects
explicitly. This gives you full control over how the Lambda Function is configured, and allows you to provision
functions that run code in a language different from what your Pulumi program is authored in. Even if the languages
are the same, this lets you keep your application and infrastructure code distinct from one another.

For example, this runs an AWS Lambda anytime an S3 Object is added to the given Bucket:

```typescript
import * as aws from "@pulumi/aws";

// Create our bucket using infrastructure as code.
const docsBucket = new aws.s3.Bucket("docs");

// Configure IAM so that the AWS Lambda can be run.
const docsHandlerRole = new aws.iam.Role("docsHandlerRole", {
   assumeRolePolicy: {
      Version: "2012-10-17",
      Statement: [{
         Action: "sts:AssumeRole",
         Principal: {
            Service: "lambda.amazonaws.com",
         },
         Effect: "Allow",
         Sid: "",
      }],
   },
});
new aws.iam.RolePolicyAttachment("zipTpsReportsFuncRoleAttach", {
   role: docsHandlerRole,
   policyArn: aws.iam.ManagedPolicies.AWSLambdaExecute,
});

// Next, create the Lambda function itself:
const docsHandlerFunc = new aws.lambda.Function("docsHandlerFunc", {
   // Upload the code for our Lambda from the "./app" directory:
   code: new pulumi.asset.AssetArchive({
      ".": new pulumi.asset.FileArchive("./app"),
   }),
   runtime: "nodejs12.x",
   role: docsHandlerRole.arn,
});

// Finally, register the Lambda to fire when a new Object arrives:
docsBucket.onObjectCreated("docsHandler", docsHandlerFunc);
```

Any of [the supported Lambda runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html) can be used,
including Node.js (as shown here), Python, Ruby, Java, Go, and .NET.

This example highlights both the benefits and drawbacks to programming at this level: we need to know how to
configure all of these ancillary resources (like IAM), but as a result, the entire power of Lambda is at our fingertips.

Notice that we've pointed to our application logic inside of `./app`. Pulumi will create the zipfile for you. If we
instead wanted to use a zipfile we've already packaged, just change code as follows:

```typescript
// ...
   code: new pulumi.asset.FileArchive("./app.zip"),
// ...
```

Using [Pulumi's Asset and Archive classes](/docs/reference/pkg/nodejs/pulumi/pulumi/asset), we can
fetch code from anywhere -- in-memory, on disk, or even over the network. Pulumi will detect changes in the contents
of these assets and archives so that when you run `pulumi up`, diffs will be detected and updated.

### Register an Event Handler by Reusing an Existing Lambda Function

It is possible to provision some but not all of the resources involved in configuring AWS Lambda:

* Provision the Lambda, but not the infrastructure, using Pulumi
* Provision the infrastructure, but not the Lambda, using Pulumi
* Provision neither with Pulumi, but use it to wire up the event handler

Every resource type in Pulumi has a static `get` that looks up an existing resource. These resources aren't managed
by Pulumi, but you can still access their properties and use them. In this case, we'll just look up an existing
Lambda, `docsHandlerFunc`, and register it as an event handler on the S3 Bucket we've defined:

```typescript
import * as aws from "@pulumi/aws";

// Create our bucket using infrastructure as code.
const docsBucket = new aws.s3.Bucket("docs");

// Look up an existing AWS Lambda Function, provisioned outside of Pulumi.
const docsHandlerFunc = aws.lambda.Function.get("docsHandlerFunc", "docsHandlerFunc-19d51dc");

// Register a handler so that this function is invoked when a new Object arrives:
docsBucket.onObjectCreated("docsHandler", docsHandlerFunc);
```

We've given the function's ID, `docsHandlerFunc-19d51dc`, which allows Pulumi to locate it in your account and reuse it.
This can make it easy to incrementally adopt Pulumi one piece at a time, collaborate between teams, or stitch together
resources managed by different stacks.

### Updating Your Functions

### Registering Functions for Existing Resources

Sometimes different members of the team manage different parts of the infrastructure. For example, maybe your DevOps
engineers provision resources like buckets, topics, and so on, and your developers wire up the functions.

It is just as easy to look up an existing resource using `get` and use that for our event handler:

```typescript
import * as aws from "@pulumi/aws";

// Look up an S3 bucket that already exists in our account.
const docsBucket = aws.s3.Bucket.get("docs", "docs-4f64efc");

// Create an AWS Lambda event handler on our bucket using magic functions.
docsBucket.onObjectCreated("docsHandler", (e) => {
    // your lambda code goes here
});
```

When you run `pulumi up`, you'll still see this bucket resource but notice it says `read` instead of `create` or `update`.
This just means that the resource is read from your account. No matter what you do, the bucket itself will not be
modified by Pulumi, other than to subscribe an event.

This can be combined with the earlier similar functionality for functions, to glue together a bucket and a Lambda,
where neither was actually provisioned by Pulumi:

```typescript
import * as aws from "@pulumi/aws";

// Look up an S3 bucket that already exists in our account.
const docsBucket = aws.s3.Bucket.get("docs", "docs-4f64efc");

// Look up an existing AWS Lambda Function, provisioned outside of Pulumi.
const docsHandlerFunc = aws.lambda.Function.get("docsHandlerFunc", "docsHandlerFunc-19d51dc");

// Register a handler so that this function is invoked when a new Object arrives:
docsBucket.onObjectCreated("docsHandler", docsHandlerFunc);
```

In this case, Pulumi is only being used to register the event handler, not provision the underlying resources.

## Structuring Your Serverless Code Base

A nice middle ground between magic and manual functions is to use your language's module system to structure your
project. This is similar to how you might structure a typical application: route definitions over here, business logic
over there, markup over here, etc. Pulumi can figure out the diffs regardless of how you've structured your code,
so updates are always based only on what's changed.

For example, maybe we've defined our callback function in `./app`:

```typescript
import * as aws from "@pulumi/aws";
export async function handleDocument(e: aws.s3.BucketEvent): Promise<void> {
   // your lambda code goes here
}
```

And now we can go back to our infrastructure code, and eliminate the application logic entirely:

```typescript
import { handleDocument } from "./app";

// ...

docsBucket.onObjectCreated("docsHandler", handleDocument);
```

We can take this further and use dynamic package management to split up the code, possibly even spreading pieces of
infrastructure and application code across multiple repos and/or packages. This works well for larger teams with
independent components versioning at their own pace.

Lastly, it's possible to use Pulumi stacks to actually break apart your cloud resources and functions into
independently deployable pieces. This allows teams to leverage features like RBAC. For instance, it's common for the
DevOps team to manage the physical cloud resources like queues, topics, and buckets, while the development team
authors and manages the serverless functions attached to them. For more information on this idea, see
[Organizing Projects and Stacks](/docs/guides/organizing-projects-stacks/)

## Easy Lambda Log Consumption

[Pulumi Crosswalk for AWS CloudWatch](/docs/guides/crosswalk/aws/cloudwatch/) ensures that resources have built-in
logging, with easy ways to customize associated policies. Additionally, the `pulumi logs` CLI command allows
us to monitor logs in realtime from any CloudWatch resources in our program. For Lambda Functions, this means
we can run `pulumi logs -f` to tail all of the logs for all of our Lambdas in a program.

For example, let's modify the example from earlier to print the name of the object to the console:

```typescript
import * as aws from "@pulumi/aws";

// Create our bucket using infrastructure as code.
const docsBucket = new aws.s3.Bucket("docs");

// Create an AWS Lambda event handler on our bucket using magic functions.
docsBucket.onObjectCreated("docsHandler", (e) => {
   for (const rec of e.Records || []) {
      const [ buck, key ] = [ rec.s3.bucket.name, rec.s3.object.key ];
      console.log(`Hello from Lambda -- got an S3 Object: ${buck}/${key}`);
    }
});

// Export the bucket name so it's easy to access.
export docsBucketName = docsBucket.bucketName;
```

Now after deploying this code, let's run `pulumi logs -f` and watch the program run:

```bash
$ pulumi logs -f
Collecting logs for stack dev since 2019-03-10T10:09:56.000-07:00...
```

Now that we're tailing the logs, we can copy a file to our bucket, and watch the Lambda execute:

```bash
$ aws s3 cp ./doc1.txt s3://$(pulumi stack output docsBucketName)
upload: ../doc1.txt to s3://docsBucket-96458ef/doc1.txt
```

After the upload completes, we'll see that our function comes alive:

```bash
 2019-03-10T11:10:48.617-07:00[docsBucket] Hello from Lambda -- got an S3 Object: docsBucket-96458ef/doc1.txt
```
