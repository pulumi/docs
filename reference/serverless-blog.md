Using monkey-patching in TypeScript for serverless programming

One of Pulumi's goals from the very beginning was to be able to deliver a way to create cloud infrastructure with the real programming
languages that you are already doing today. We believe that the existing constructs already present in these langauges, like flow control
inheritance, composition, and so on, provide the right abstractions to effectively build up infrastructure in a simple and familiar way.
Our early TypeScript SDKs enabled this by projecting things like the AWS api surface area into classes corresponding to resources you could 
create.  You could then create those resources using normal program flow logic like:

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
      let client = new slack.WebClient(...);
      for (let rec of e.Records) {
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

Phew... that's a lot of code.  But it accurately conveys all the real aws resources that need to be created to 
