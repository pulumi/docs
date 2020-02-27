---
title: "Serverless on AWS with Pulumi: Simple, Event-based Functions"
authors: ["cyrus-najmabadi"]
tags: ["JavaScript","Serverless","AWS"]
date: "2019-01-14"
meta_desc: "Pulumi's AWS package provides the simplest way possible to do serverless programming on AWS."

---

One of Pulumi's goals is to provide the simplest way possible to do
serverless programming on AWS by enabling you to create cloud
infrastructure with the real programming languages that you are already
using today. We believe that the existing constructs already present in
these languages, like flow control, inheritance, composition, and so on,
provide the right abstractions to effectively build up infrastructure in
a simple and familiar way.

In a [previous post]({{< relref "lambdas-as-lambdas-the-magic-of-simple-serverless-functions" >}})
we focused on how Pulumi could allow you to simply create an AWS Lambda
out of your own JavaScript function. While this was much easier than
having to manually create a [Lambda Deployment Package](https://docs.aws.amazon.com/lambda/latest/dg/nodejs-create-deployment-pkg.html)
yourself, it could still be overly complex to integrate these Lambdas
into complete serverless application. <!--more-->To get a sense of that complexity,
let's look at how one would normally have to work with AWS's resource
system to create a simple Serverless application:

```typescript
// Simplified for brevity
import * as aws from "@pulumi/aws";
import * as slack from "@slack/client";

// Create a simple bucket.
const bucket = new aws.s3.Bucket("testbucket", {
    serverSideEncryptionConfiguration: ...,
    forceDestroy: true,
});

// Create a lambda that will post a message to slack when the bucket changes.
// We can pass a simple JavaScript/TypeScript lambda here thanks to the magic of "Lambdas as Lambdas"
// See: www.pulumi.com{{< relref "/blog/lambdas-as-lambdas-the-magic-of-simple-serverless-functions" >}}
const lambda = new aws.lambda.CallbackFunction("postToSlack", {
    callback: async (e) => {
      const client = new slack.WebClient(...);
      for (const rec of e.Records) {
        await client.chat.postMessage({ ... });
      }
    },
    ...
});

// Give the bucket permission to invoke the lambda.
const permission = new aws.lambda.Permission("invokelambda", {
  function: lambda,
  action: "lambda:InvokeFunction",
  principal: "s3.amazonaws.com", sourceArn: bucket.id.apply(bucketName => `arn:aws:s3:::${bucketName}`), }));

// Now hookup a notification that will trigger the lambda when any object is created in the bucket.
const notification = new aws.s3.BucketNotification("onAnyObjectCreated", {
    bucket: bucket.id,
    lambdaFunctions: [{
        events: ["s3:ObjectCreated:*"],
        lambdaFunctionArn: lambda.arn,
    }],
})
```

Phew... that's a lot of code `:-/` So what happened above? Well, in the
AWS resource-oriented view of the world, most things are nouns (i.e
objects). Your bucket is an object. The lambda is an object. The
permission is an explicit object. And even the connection between the
bucket and lambda (the `BucketNotification`) is itself an object. That's
one way to decompose the world, and it makes sense in some domains where
everything is just 'data'. But that isn't a natural fit for a
programming language, and it just doesn't feel very idiomatic or
appropriate for how people would expect things to work in their
programming language of choice. Programming languages have lots of other
facilities at their disposal to work with data. You can have
methods/functions/messages you can send to an object. You can have
events and callbacks on objects. You can encapsulate objects behind
other objects. You can 'run code' to do things based on those objects,
etc. etc.

Now, while data should be the start of how you interact with system, it
shouldn't be the end. Toward that goal, Pulumi makes it possible to
simply compose and connect these resources in a more natural fashion. By
just adding our own components, and leveraging what programing languages
can already do, we can make it possible to simplify the above down to:

```typescript
import * as aws from "@pulumi/aws";
import * as slack from "@slack/client";

// Create a simple bucket.
const bucket = new aws.s3.Bucket("testbucket", {
    serverSideEncryptionConfiguration: ...,
    forceDestroy: true,
});

// Create a lambda that will post a message to slack when the bucket changes.
bucket.onObjectCreated("postToSlack", async (e) => {
    const client = new slack.WebClient(...);
    for (const rec of e.Records) {
        await client.chat.postMessage({ ... });
    }
});
```

This now feels far more like how one might expect to express this
concept with a normal application. A simple conceptual idea now maps to
a simple code pattern. Instead of manually creating objects to represent
the connection between the Bucket and the Lambda, we simply directly ask
the Bucket to call the Lambda when the `ObjectCreated` event fires.
Because this is all 'code', we can take care of all the boring cruft
(like creating permissions) on your behalf. Of course, if you need to
tweak this, that's still possible. We believe you should always be in
control of what's going on. The actual low level details of how that is
done are interesting as well, but a followup post will explain how we
did it (and how you can do it too!). If you want to create your own
composable modules for making cloud deployments easier then definitely
look for that post!

Now, while it's how the above examples worked, it's also worth noting
that the use of a JavaScript function for the AWS Lambda is not
required. You can hook up a serverless event to call an AWS Lambda you
create just by using [new aws.lambda.Function](https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L14).
Or, you can get a reference to an existing AWS Lambda created outside of
Pulumi and have that be the receiver of your serverless event. Here's
how that would look:

```typescript
import * as aws from "@pulumi/aws";
import * as slack from "@slack/client";

// Create a simple bucket.
const bucket = new aws.s3.Bucket("testbucket", {
    serverSideEncryptionConfiguration: ...,
    forceDestroy: true,
});

// Retrieve an existing Lambda Function already created in your AWS infrastructure.
const func = aws.lambda.Function.get("postToSlack", "... existing lambda arn ...");

// Call that Lambda Function when an object is created in the bucket.
bucket.onObjectCreated("postToSlack", func);
```

We've tried to make it this simple to hook up many interesting AWS
serverless events. For example, you can register to hear about events on
[S3 Buckets](https://docs.aws.amazon.com/lambda/latest/dg/with-s3.html),
[SNS Topics](https://docs.aws.amazon.com/sns/latest/dg/sns-lambda-as-subscriber.html),
[SQS Queues](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html),
[Kinesis Streams](https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html),
[DynamoDB Tables](https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html),
[Cloudwatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/RunLambdaSchedule.html),
and more. We've tried to provide these prebuilt components for the most
common and interesting cases. If there's some serverless event we
haven't added support for that you want to use, definitely let us know!

Finally, because we think it's great to be able to use a JavaScript or
TypeScript function as the code for your Lambda, we've introduced a
simple quality-of-life improvement for writing those functions.
Specifically, because it's so common that one will use the real [AWS SDK
for Node.js](https://aws.amazon.com/sdk-for-node-js/) within a Lambda,
we've provided a quick and simple way to get to a fully initialized
instance of that API without needing any additional `requires` or
`imports` in your code. Here's how that would look:

```typescript
// The only module you need to import.
import * as aws from "@pulumi/aws";

// ...

bucket.onObjectCreated("postToSlack", async (e) => {
    // direct access to the aws-sdk through `aws.sdk`.
    const sqs = new aws.sdk.SQS();
    sqs.sendMessage(/*...*/);
});
```

This allows you to use `@pulumi/aws` as both the deployment-time API to
define your AWS infrastructure, as well as being the run-time API that
you can use when your Lambda executes to access the full set of AWS
functionality.

To get a sense of a more complete example of how this all ties together
you can see many of our [examples](https://github.com/pulumi/examples).
One example that helps demonstrate many of the above concept is
[Twitter+Athena](https://github.com/pulumi/examples/blob/master/aws-ts-twitter-athena/index.ts).
In it, we use serverless events to define a schedule, a callback to
invoke when the even t fires, use of a third-party twitter API to
retrieve a set of relevant Tweets, use of the aws-sdk to store the Tweet
information into an S3 Bucket, and finally the creation of an Athena
Query to extract information from the information stored into the
bucket. You could augment this example with any number of resources and
events for all sorts of interesting use cases.

As we've seen, with a tiny amount of code, you can easily define the
cloud resources you want to create (or reference your existing cloud
resources). It's then simple to add code to respond to events and call
new or existing Lambdas. And, if you use a JavaScript function to create
your Lambda, you can reference those resources along with the AWS SDK
easily, all within the same application code!
