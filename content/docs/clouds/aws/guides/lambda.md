---
title_tag: "Using AWS Lambda & Serverless Events | Crosswalk"
title: Lambda
h1: AWS Lambda & Serverless Events
meta_desc: Pulumi Crosswalk for AWS brings a more natural, and easier to use, way of building serverless applications using AWS Lambda.
meta_image: /images/docs/meta-images/docs-clouds-aws-meta-image.png
menu:
  clouds:
    parent: aws-guides
    identifier: aws-guides-lambda
    weight: 9
search:
    keywords:
        - aws-apigateway.RestAPI
        - aws.cloudwatch.onSchedule
        - aws.cloudwatch.EventRule.onEvent
        - aws.cloudwatch.LogGroup.onEvent
        - aws.dynamodb.Table.onEvent
        - aws.kinesis.Stream.onEvent
        - aws.s3.Bucket.onObjectCreated
        - aws.s3.Bucket.onObjectRemoved
        - aws.s3.Bucket.onEvent
        - aws.sns.Topic.onEvent
        - aws.sqs.Queue.onEvent
        - APIGatewayProxyEvent
        - aws.s3.BucketEvent
        - aws.dynamodb.TableEvent
        - aws.kinesis.StreamEvent
        - aws.sns.TopicEvent
        - aws.sqs.QueueEvent
        - aws.cloudwatch.LogGroupEvent
        - aws.cloudwatch.EventRuleEvent
        - aws.lambda.CallbackFunction
        - aws.lambda.Function
        - aws.lambda.LayerVersion
        - codePathOptions
        - magic functions
        - lambda layers
        - tsconfig paths baseUrl
aliases:
- /docs/reference/crosswalk/aws/lambda/
- /docs/guides/crosswalk/aws/lambda/
---

{{< crosswalk-header >}}

[AWS Lambda](https://aws.amazon.com/lambda/) lets you run code without provisioning or managing servers. You pay only
for the compute time you consume and there is no charge when your code is not running. With Lambda, you can run code
for virtually any type of application or backend service with zero administration. Just upload your code and Lambda
takes care of everything required to run and scale your code with high availability. You can set up your code to
automatically trigger from other AWS services or call it directly from any web or mobile app.

{{% notes type="info" %}}
The features described on this page are extensions of the [AWS Classic provider](/registry/packages/aws/) and are only available in JavaScript and TypeScript.
{{% /notes %}}

## Overview

Pulumi Crosswalk for AWS brings a more natural, and easier to use, way of building serverless applications using
AWS Lambda. Pulumi lets you express Lambda functions using real code, and handles packaging, versioning, and
configuration of the associated AWS resources for you. This lets you focus on your application logic without needing to
worry about boilerplate, and with confidence that the resulting infrastructure automatically uses AWS best practices.

With Pulumi Crosswalk for AWS, event sources are available on all native resource types, including AWS S3, SQS,
DynamoDB, CloudWatch, Kinesis, and more, in addition to full support for [API Gateway](/docs/clouds/aws/guides/api-gateway/).
This improves discoverability of event sources in addition to adding strong typing to the event handler
inputs and outputs that AWS Lambda will deliver to your code.

## Available AWS services and event sources

Below is a list of AWS Services and their available Lambda event sources.

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

| Service | Event | Description |
|-------------|-------|-------------|
| API Gateway | [aws-apigateway.RestAPI](/registry/packages/aws-apigateway/) request | trigger a Lambda function in response to an HTTP request |
| CloudWatch  | [aws.cloudwatch.onSchedule](https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/cloudwatchMixins.ts) | fire a CloudWatch event on a particular schedule, e.g. a cron expression |
| CloudWatch  | [aws.cloudwatch.EventRule.onEvent](https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRuleMixins.ts) | fire an event when a particular CloudWatch event occurs |
| CloudWatch  | [aws.cloudwatch.LogGroup.onEvent](https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/logGroupMixins.ts) | fire an event when a CloudWatch logs event occurs |
| DynamoDB    | [aws.dynamodb.Table.onEvent](https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/dynamodbMixins.ts) | fire events for DynamoDB insert, modify, or remove operations |
| Kinesis     | [aws.kinesis.Stream.onEvent](https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/kinesisMixins.ts) | fire Kinesis Stream events at particular times or batch sizes |
| S3          | [aws.s3.Bucket.onObjectCreated](https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/s3Mixins.ts) | trigger a function anytime an object is created in an S3 bucket |
| S3          | [aws.s3.Bucket.onObjectRemoved](https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/s3Mixins.ts) | trigger a function anytime an object is removed from an S3 bucket |
| S3          | [aws.s3.Bucket.onEvent](https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/s3Mixins.ts) | trigger a function for a wide range of S3 bucket events |
| SNS         | [aws.sns.Topic.onEvent](https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/snsMixins.ts) | fire SNS Topic events when new messages arrive |
| SQS         | [aws.sqs.Queue.onEvent](https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/sqsMixins.ts) | fire SQS Queue events when new messages are enqueued (or on DLQ events, etc) |

{{< notes >}}
The resources above belong to the [AWS Classic provider](/registry/packages/aws/), but they aren't yet included in the provider's API documentation. Issue [pulumi/pulumi#13231](https://github.com/pulumi/pulumi/issues/13231) tracks adding these resources to the Pulumi Registry. In the meantime, links to their source code are provided for reference.
{{< /notes >}}

There are multiple approaches to creating a Lambda function. The examples below trigger a Lambda
execution when an S3 bucket receives a new object, but the manner of registering a handler is the same across
all of the above event sources.

## Registering serverless event handlers

Most serverless programming models today treat event sources (S3 buckets, SQS queues, etc.) and event
handlers (the Lambdas and associated code) as very different things. That is, the "infrastructure" is entirely
separate from the "app code", and managed with distinct tools and workflows. Pulumi, however, allows you to use one
programming model and CLI to support managing both application and infrastructure consistently.

You can create event sources and handlers in the same program, but Pulumi's approach is flexible, so that you can
elect to wire up new Lambda-based functions to existing event sources (such as if you already have core infrastructure
defined) or even use functions that already exist, and glue them together with resources.

Because Pulumi provisions and manages resources, updating your functions after creating them is easy. Just edit your
code, run `pulumi up`, and Pulumi will diff and compute the minimal set of changes it can make to upgrade your code,
without any downtime required. This is as easy to do by hand as it is in
[CI/CD](/docs/using-pulumi/continuous-delivery/).

### Using magic Lambda functions

One way to author a Lambda Function is to write it inline, within your Pulumi program. The Pulumi compiler and runtime work in tandem to extract your function, package it up along with its dependencies, upload the package to AWS Lambda, and configure the resulting AWS Lambda resources automatically.

For example, this code creates an S3 bucket and executes an AWS Lambda anytime a new object is created within it:

```typescript
import * as aws from "@pulumi/aws";

// Create an S3 bucket.
const docsBucket = new aws.s3.Bucket("docs");

// Create an AWS Lambda event handler on the bucket using a magic function.
docsBucket.onObjectCreated("docsHandler", (event: aws.s3.BucketEvent) => {
    // Your Lambda code here.
});
```

The `onObjectCreated` function blurs the line between infrastructure and application logic, letting you focus
on what you want your code to do, rather than how it does it. This code looks like a typical event-driven program,
but is fully serverless so that it scales dynamically and you only pay for what you use.

{{< notes >}}
If the idea of mixing application and infrastructure logic like this is unappealing to you, don't worry --- there are
other approaches, including [provisioning AWS Lambda function resources explicitly](#register-an-event-handler-by-creating-a-lambda-function-resource)
and [reusing existing Lambda functions](#register-an-event-handler-by-reusing-an-existing-lambda-function).
{{< /notes >}}

Nearly any code can go inside the body of that function. The JavaScript arrow function may capture references to other
variables in the surrounding code, including other resources and even imported modules. The Pulumi compiler figures
out [how to serialize the resulting closure](/docs/concepts/function-serialization/) as it uploads and configures the AWS Lambda. This works even if you
are composing multiple functions together. Just write code like usual --- that's why these are called _magic functions_.

### Using Lambda function resources

In addition to declaring your serverless event handlers inline with magic functions, you can also create and register them by allocating [`aws.lambda.Function`](/registry/packages/aws/api-docs/lambda/function/) objects explicitly. This gives you full control over how the Lambda function is configured, and allows you to provision
functions that run code in a language different from the one your Pulumi program is authored in. Even if the languages
are the same, this lets you keep your application and infrastructure code distinct from one another.

For example, this program provisions an S3 bucket and runs an AWS Lambda anytime an S3 object is added to the bucket:

```typescript
import * as aws from "@pulumi/aws";
import * as pulumi from "@pulumi/pulumi";

// Create an S3 bucket.
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
        }],
    },
});

new aws.iam.RolePolicyAttachment("zipTpsReportsFuncRoleAttach", {
    role: docsHandlerRole,
    policyArn: aws.iam.ManagedPolicies.AWSLambdaExecute,
});

// Next, create the Lambda function itself.
const docsHandlerFunc = new aws.lambda.Function("docsHandlerFunc", {
    runtime: "nodejs18.x",
    role: docsHandlerRole.arn,
    handler: "index.handler",

    // Upload the code for the Lambda from the "./app" directory.
    code: new pulumi.asset.AssetArchive({
        ".": new pulumi.asset.FileArchive("./app"),
    }),
});

// Finally, register the Lambda to be invoked when a new bucket object arrives.
docsBucket.onObjectCreated("docsHandler", docsHandlerFunc);
```

Any of the [supported Lambda runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html) can be used,
including Node.js (as shown here), Python, Ruby, Java, Go, and .NET.

This example highlights both the benefits and drawbacks to programming at this level: you need to know how to
configure all of these ancillary resources (like IAM), but as a result, the entire power of Lambda is at your fingertips.

Notice the reference to the application logic at `./app`, which instructs Pulumi to create the zip file for you. If
instead you wanted to use a zip file you'd already packaged, you'd just change the code as follows:

```typescript
// ...
const docsHandlerFunc = new aws.lambda.Function("docsHandlerFunc", {
    // ...

    code: new pulumi.asset.FileArchive("./app.zip"),
});
// ...
```

Using [Pulumi's Asset and Archive classes](/docs/concepts/assets-archives/), you can
fetch code from anywhere --- in-memory, on disk, or even over the network. Pulumi automatically detects changes in the contents
of these assets and archives so that when you run `pulumi up`, diffs are detected and resources updated accordingly.

### Using existing Lambda functions

It is also possible to provision some but not all of the resources involved in configuring AWS Lambda. For example, you can:

* Provision the Lambda with Pulumi, but not the infrastructure
* Provision the infrastructure with Pulumi, but not the Lambda
* Provision neither with Pulumi, but use it to wire up an event handler

Every resource type in Pulumi has a static `get` method that looks up an existing resource. These resources aren't managed
by Pulumi, but you can still access and use their properties to configure other resources in your program.

This example looks up an existing Lambda named `docsHandlerFunc-19d51dc` and registers it as an event handler on a new S3 bucket:

```typescript
import * as aws from "@pulumi/aws";

// Create an S3 bucket.
const docsBucket = new aws.s3.Bucket("docs");

// Look up an existing AWS Lambda Function, provisioned outside of Pulumi.
const docsHandlerFunc = aws.lambda.Function.get("docsHandlerFunc", "docsHandlerFunc-19d51dc");

// Register a handler so that this function is invoked when a new Object arrives:
docsBucket.onObjectCreated("docsHandler", docsHandlerFunc);
```

Notice the function's ID, `docsHandlerFunc-19d51dc`, which allows Pulumi to locate it in your account and reuse it.
This can make it easy to incrementally adopt Pulumi one piece at a time, collaborate between teams, or stitch together
resources managed by different stacks.

### Using existing functions and event sources

Sometimes different members of the team manage different parts of the infrastructure. For example, maybe your DevOps
engineers provision resources like buckets, topics, and so on, and your developers wire up the event handlers for those resources.

It's just as easy to look up an existing resource using `get` and use that for an event handler:

```typescript
import * as aws from "@pulumi/aws";

// Look up an S3 bucket that already exists in your account.
const docsBucket = aws.s3.Bucket.get("docs", "docs-4f64efc");

// Create an AWS Lambda event handler on the bucket using a magic function.
docsBucket.onObjectCreated("docsHandler", (event: aws.s3.BucketEvent) => {
    // Your Lambda code here.
});
```

When you run `pulumi up`, you'll still see this bucket resource, but notice it says `read` instead of `create` or `update`.
This means the resource has been read from your account.

No matter what you do, the bucket itself will not be modified by Pulumi, other than to subscribe an event.

This can be combined with the earlier similar functionality for functions, to glue together a bucket and a Lambda,
where neither was actually provisioned by Pulumi:

```typescript
import * as aws from "@pulumi/aws";

// Look up an S3 bucket that already exists in your account.
const docsBucket = aws.s3.Bucket.get("docs", "docs-4f64efc");

// Look up an AWS Lambda Function that already exists in your account.
const docsHandlerFunc = aws.lambda.Function.get("docsHandlerFunc", "docsHandlerFunc-19d51dc");

// Register a handler so that this function is invoked when a new object arrives.
docsBucket.onObjectCreated("docsHandler", docsHandlerFunc);
```

In this case, Pulumi is only being used to register the event handler, not to provision the underlying bucket and function resources.

### Event types and contexts

Lambda functions invoked in response to serverless events are called with two arguments: an _event_ object and a _context_.

The event object contains information about the event --- e.g., for an S3 bucket event, the names of the bucket and filename that triggered it. The context object contains information about the Lambda invocation, such as the name of the function, its memory allocation, and its associated CloudWatch log group.

The properties of an event object vary based on the source of the event. To make inspecting and working with these objects more discoverable and type-safe, the TypeScript SDK includes a number of event types you can use to describe them:

| Event Source | Event Type | Package |
| --- | --- | --- |
| API Gateway | `APIGatewayProxyEvent` | [aws-lambda](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/types/aws-lambda/trigger/api-gateway-proxy.d.ts) |
| S3 bucket | `aws.s3.BucketEvent` | [@pulumi/aws](https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/s3/s3Mixins.ts) |
| DynamoDB Table | `aws.dynamodb.TableEvent` | [@pulumi/aws](https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/dynamodbMixins.ts) |
| Kinesis Stream | `aws.kinesis.StreamEvent` | [@pulumi/aws](https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/kinesis/kinesisMixins.ts) |
| SNS Topic | `aws.sns.TopicEvent` | [@pulumi/aws](https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/snsMixins.ts) |
| SQS Queue | `aws.sqs.QueueEvent` | [@pulumi/aws](https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sqs/sqsMixins.ts) |
| CloudWatch Log Group | `aws.cloudwatch.LogGroupEvent` | [@pulumi/aws](https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRuleMixins.ts) |
| CloudWatch Event | `aws.cloudwatch.EventRuleEvent` | [@pulumi/aws](https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/cloudwatch/eventRuleMixins.ts) |

Context objects are supplied to all Lambda functions and are typed as Lambda [`Context`](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/types/aws-lambda/handler.d.ts). You can learn more about Lambda context objects [in the AWS documentation](https://docs.aws.amazon.com/lambda/latest/dg/nodejs-context.html).

To use these types, you can apply them as type annotations to your callback arguments. Here, for example, the `APIGatewayProxyEvent` and `Context` types are applied to the arguments of an inline AWS API Gateway route handler:

```typescript
import * as apigateway from "@pulumi/aws-apigateway";
import { APIGatewayProxyEvent, Context } from "aws-lambda";

const api = new apigateway.RestAPI("api", {
    routes: [
        {
            path: "/api",
            eventHandler: async (event: APIGatewayProxyEvent, context: Context) => {
                return {
                    statusCode: 200,
                    body: JSON.stringify({
                        eventPath: event.path,
                        functionName: context.functionName,
                    })
                };
            },
        },
    ],
});
```

## Customizing Lambda function attributes

The Lambdas created by magic functions use reasonable defaults for CPU, memory, IAM, logging, and other configuration.
Should you need to customize these settings, the [`aws.lambda.CallbackFunction`](https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/lambdaMixins.ts) class offers all of the underlying settings, while also letting you use the magic function style of expressing the callback itself.

For example, to increase the RAM available to your function from 128MB to 256MB:

```typescript
import * as aws from "@pulumi/aws";

// Create an S3 bucket.
const docsBucket = new aws.s3.Bucket("docs");

// Create an AWS Lambda event handler on the bucket using a magic function.
docsBucket.onObjectCreated("docsHandler", new aws.lambda.CallbackFunction("docsHandlerFunc", {
    callback: (event: aws.s3.BucketEvent) => {
        // ...
    },

    memorySize: 256 /* MB */,
});
```

### Adding/removing files from a function bundle

Occasionally you may need to customize the contents of function bundle before uploading it to AWS Lambda --- for example, to remove unneeded Node.js modules or add certain files or folders to the bundle explicitly. The `codePathOptions` property of `CallbackFunction` allows you to do this.

In this example, a local directory `./config` is added to the function bundle, while an unneeded Node.js module `mime` is removed:

```typescript
import * as aws from "@pulumi/aws";
import * as fs from "fs";

const docsBucket = new aws.s3.Bucket("docs");

docsBucket.onObjectCreated("docsHandler", new aws.lambda.CallbackFunction("docsHandlerFunc", {
    callback: (event: aws.s3.BucketEvent) => {
        // ...
    },

    codePathOptions: {

        // Add local files or folders to the Lambda function bundle.
        extraIncludePaths: [
            "./config",
        ],

        // Remove unneeded Node.js packages from the bundle.
        extraExcludePackages: [
            "mime",
        ],
    },
}));
```

### Using Lambda layers {#lambda-layers}

[Lambda layers](https://docs.aws.amazon.com/lambda/latest/dg/chapter-layers.html) allow you to share code, configuration, and other assets across multiple Lambda functions. At runtime, AWS Lambda extracts these files into the function's filesystem, where you can access their contents as though they belonged to the function bundle itself.

Layers are managed with the [`aws.lambda.LayerVersion`](/registry/packages/aws/api-docs/lambda/layerversion/) resource, and you can attach them to as many `lambda.Function` or `lambda.CallbackFunction` resources as you need using the function's `layers` property. Here, the preceding program is updated to package the `./config` folder as a Lambda layer instead:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as fs from "fs";

const docsBucket = new aws.s3.Bucket("docs");

// Create a Lambda layer containing some shared configuration.
const configLayer = new aws.lambda.LayerVersion("config-layer", {
    layerName: "my-config-layer",

    // Use a Pulumi AssetArchive to zip up the contents of the folder.
    code: new pulumi.asset.AssetArchive({
        "config": new pulumi.asset.FileArchive("./config"),
    }),
});

docsBucket.onObjectCreated("docsHandler", new aws.lambda.CallbackFunction("docsHandlerFunc", {
    callback: (event: aws.s3.BucketEvent) => {
        // ...
    },

    // Attach the config layer to the function.
    layers: [
        configLayer.arn,
    ],
}));
```

Notice the path to the file is now `/opt/config/config.json` --- `/opt` being the path at which AWS Lambda extracts the contents of a layer. The configuration layer is now manageable and deployable independently of the Lambda itself, allowing changes to be applied immediately across all functions that use it.

#### Using layers for Node.js dependencies

This same approach can be used for sharing Node.js module dependencies. When you package your dependencies [at the proper path](https://docs.aws.amazon.com/lambda/latest/dg/packaging-layers.html) within the layer zip file, (e.g., `nodejs/node_modules`), AWS Lambda will unpack and expose them automatically to the functions that use them at runtime. This approach can be useful in monorepo scenarios such as the example below, which adds a locally built Node.js module as a layer, then references references the module from within the body of a `CallbackFunction`:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

// Create a layer containing a locally built Node.js module.
const utilsLayer = new aws.lambda.LayerVersion("utils-layer", {
    layerName: "utils",
    code: new pulumi.asset.AssetArchive({

        // Store the module under nodejs/node_modules to make it available
        // on the Node.js module path.
        "nodejs/node_modules/@my-alias/utils": new pulumi.asset.FileArchive("./layers/utils/dist"),
    }),
});

const docsBucket = new aws.s3.Bucket("docs");

docsBucket.onObjectCreated("docsHandler", new aws.lambda.CallbackFunction("docsHandlerFunc", {
    callback: async (event: aws.s3.BucketEvent) => {

        // Import the module from the layer at runtime.
        const { sayHello } = await import("@my-alias/utils");

        // Call a function from the utils module.
        console.log(sayHello());
    },

    // Attach the utils layer to the function.
    layers: [
        utilsLayer.arn,
    ],
}));
```

Notice the example uses the module name `@my-alias/utils`. To make this work, you'll need to add a few lines to your Pulumi project's `tsconfig.json` file to map your chosen module name to the path of the module's TypeScript source code:

```javascript
{
    "compilerOptions": {
        // ...
        "baseUrl": ".",
        "paths": {
            "@my-alias/utils": [
                "./layers/utils"
            ]
        }
    },
    // ...
}
```

Aliasing the module in this way allows you to take full advantage of TypeScript type checking and IntelliSense in development without having to compile the module into the function's source code when it's time to deploy.

## Structuring your serverless codebase

A nice middle ground between magic and manually defined functions is to use your language's module system to structure your
project. This is similar to how you might structure a typical application: route definitions over here, business logic
over there, markup over here, etc. Pulumi can figure out the diffs regardless of how you've structured your code,
so updates are always based only on the code that's changed.

For example, maybe you've defined your callback function in `./app`:

```typescript
import * as aws from "@pulumi/aws";
export async function handleDocument(e: aws.s3.BucketEvent): Promise<void> {
    // Your lambda code here.
}
```

In your infrastructure code, you can now eliminate the application logic entirely:

```typescript
import { handleDocument } from "./app";

// ...

docsBucket.onObjectCreated("docsHandler", handleDocument);
```

You can take this further and use dynamic package management to split up the code, possibly even spreading pieces of
infrastructure and application code across multiple repos and/or packages. This works well for larger teams with
independent components versioning at their own pace.

### Composing with multiple stacks

Lastly, it's possible to use Pulumi stacks to break out your cloud resources and functions into
independently deployable pieces. This allows teams to leverage features like RBAC. For instance, it's common for the
DevOps team to manage the physical cloud resources like queues, topics, and buckets, while the development team
authors and manages the serverless functions attached to them. For more information and guidance, see
[Organizing projects and stacks](/docs/using-pulumi/organizing-projects-stacks/).

## Easy Lambda log consumption

[Pulumi Crosswalk for AWS CloudWatch](/docs/clouds/aws/guides/cloudwatch/) ensures that resources have built-in
logging, with easy ways to customize associated policies. Additionally, the [`pulumi logs`](/docs/cli/commands/pulumi_logs/) CLI command allows
you to monitor your infrastructure's CloudWatch logs in real time. For Lambda functions, this means
you can run `pulumi logs -f` (`--force`) to stream all of the logs from all of the Lambdas that belong to the current stack.

For example, modifying the earlier example to print the name of the object to the console:

```typescript
import * as aws from "@pulumi/aws";

// Create an S3 bucket.
const docsBucket = new aws.s3.Bucket("docs");

// Create an AWS Lambda event handler on the bucket using a magic function.
docsBucket.onObjectCreated("docsHandler", (event: aws.s3.BucketEvent) => {
    for (const rec of event.Records || []) {
        const [ buck, key ] = [ rec.s3.bucket.name, rec.s3.object.key ];
        console.log(`Hello from Lambda -- got an S3 Object: ${buck}/${key}`);
    }
});

// Export the bucket name so it's easy to access.
export docsBucketName = docsBucket.bucketName;
```

After deploying this code, you can run `pulumi logs --follow` to tail the logs:

```bash
$ pulumi logs -f
Collecting logs for stack dev since 2019-03-10T10:09:56.000-07:00...
```

Now, when you copy a file to the bucket and watch the Lambda execute:

```bash
$ aws s3 cp ./doc1.txt s3://$(pulumi stack output docsBucketName)
upload: ../doc1.txt to s3://docsBucket-96458ef/doc1.txt
```

And when the upload completes, you'll see the function come to life:

```bash
 2019-03-10T11:10:48.617-07:00[docsBucket] Hello from Lambda -- got an S3 Object: docsBucket-96458ef/doc1.txt
```
