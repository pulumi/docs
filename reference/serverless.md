# Easily Hooking up to Serverless Event

One of Pulumi's goals from the very beginning was to be able to deliver a way to create cloud infrastructure with the real programming languages that you are already using today. We believe that the existing constructs already present in these langauges, like flow control, inheritance, composition, and so on, provide the right abstractions to effectively build up infrastructure in a simple and familiar way.

In a [previous post](https://blog.pulumi.com/lambdas-as-lambdas-the-magic-of-simple-serverless-functions) we focused on how Pulumi could allow you to simply create an AWS Lambda out of your own JavaScript function.  While this was much easier than having to manually create a [Lambda Deployment Package](https://docs.aws.amazon.com/lambda/latest/dg/nodejs-create-deployment-pkg.html) yourself, it could still be overly complex to integrate these Lambdas into complete serverless application.  To get a sense of that complexity, let's look at how one would normally have to work with AWS's resource system to create a simple Serverless application:

```ts
// simplified for brevity
import * as aws from "@pulumi/aws";
import * as slack from "@slack/client";
// Create a simple bucket.
const bucket = new aws.s3.Bucket("testbucket", {
    serverSideEncryptionConfiguration: ...,
    forceDestroy: true,
});
// Create a lambda that will post a message to slack when the bucket changes.
// Note that we can pass a simple JavaScript/TypeScript lambda here thanks to the magic of Lambdas as Lambdas:
// https://blog.pulumi.com/lambdas-as-lambdas-the-magic-of-simple-serverless-functions
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
    function: lambda, action: "lambda:InvokeFunction", principal: "s3.amazonaws.com",
    sourceArn: bucket.id.apply(bucketName => `arn:aws:s3:::${bucketName}`),
}));
// now hookup a notification that will trigger the lambda when any object is created in the bucket.
const notification = new aws.s3.BucketNotification("onAnyObjectCreated", {
    bucket: bucket.id,
    lambdaFunctions: [{
        events: ["s3:ObjectCreated:*],
        lambdaFunctionArn: lambda.arn,
    }],
})
```

Phew... that's a lot of code :-/   And it just doesn't feel very idiomatic or appropriate for how people would expect things to work in their programming language of choice.  While people often work at this sort of low-level with AWS resource, Pulumi makes it possible to simply compose and connect these resources in a more pleasant fashion.  By just adding our own components we can make it possible to instead write the above as:

```ts
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

This now feels far more like how one might expect to express this concept with a normal application.  A simple conceptual idea now maps to a simple code pattern.  An object (the bucket) was created, and a callback was registered for a relevant event.  The actual low level details of how that is done are of less interest; though a following post will explain how we did it (and how you can do it too!).  

We've tried to make it this simple to hook up many interesting AWS serverless events.  For example, you can register to hear about events on [S3 Buckets](https://docs.aws.amazon.com/lambda/latest/dg/with-s3.html), SNS-topics,SQ 

One general note/question. I like this as a “how did we do it” post, but we haven’t yet done the more directly user-facing “what did we do and what can you do with it” post. I was imagining doing a simple user facing post on the features and benefits we added here, including:

    How easy it is now to hook up serverless events
    Reminder about how we let you use functions as lambdas
    The benefits of being able to mix-n-March with raw infra (and use it in all sorts of infrastructure - not just pure “serverless” apps)
    The existence of aws.sdk
    Support for (nearly) all AWS Lambda event sources.
    Pointers to some more examples that highlight these features
