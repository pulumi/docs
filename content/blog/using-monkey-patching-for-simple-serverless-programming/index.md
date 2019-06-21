---
title: "Serverless on AWS with Pulumi: simple, event-based functions"
authors: ["cyrus-najmabadi"]
tags: ["AWS/Lambda/Fargate", "Infrastructure-as-Code"]
date: "2019-01-14"

summary: "How to make serverless programming on AWS simple with Pulumi using the regular programming languages."
---

One of [Pulumi's](/) goals from the very beginning was
to be able to deliver a way to create cloud infrastructure with the real
programming languages that you are already using today. We believe that
the existing constructs already present in these langauges, like flow
control, inheritance, composition, and so on, provide the right
abstractions to effectively build up infrastructure in a simple and
familiar way.

Our early TypeScript SDKs enabled this by projecting things like the AWS
api surface area into classes corresponding to resources you could
create. Using the earliest version of the "@pulumi/aws" api, you could
then create those resources using normal program flow logic like so:

```javascript
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

Phew... that's a lot of code `:-/` But it accurately conveys all the real
AWS resources that need to be created in order to get this all working.
While this was feasible for people to do (and is what you often have to
do when manually creating infrastructure yourself), we thought this was
too much for someone to have to do all the time. It just didn't feel
very idiomatic or appropriate for how people would expect things to work
in their programming language of choice. So, to help address this
problem, we turned to [Monkey Patching](https://en.wikipedia.org/wiki/Monkey_patch) to dynamically add
intuitive functionality to these Resource classes to make them easier to
use. Before discussing how that was done, let's first see what the
result of that patching now allows you to write instead:

```javascript
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

That's it! `:-)` No need to manually create Lamdbas or Permissions or
BucketNotification. No need to explicitly configure settings for common
types of operations (like explicitly specifying `events`, or having to
pass along `arns`). `bucket.onObjectCreated` now feels like a natural,
idiomatic, way to hook up a code to run in response to something
happening (in this case, an object being created). This looks and feels
like natural JavaScript/TypeScript, but now takes care of all that extra
work on your behalf. And, importantly, you are not locked out from
having control over what happens. For example, if you needed to
configure the AWS Lambda that is created for you in some way, that
capability is still available to you.

So, how does this work? Well, it turns out that both JavaScript and
TypeScript have great built-in support for [Monkey Patching](https://en.wikipedia.org/wiki/Monkey_patch). At the JavaScript
level, adding more functionality to a type is trivial, just by
augmenting the `prototype` chain. We do that simply just with code like
so:

```javascript
Bucket.prototype.onObjectCreated = function (this: Bucket, name, handler, args, opts) {
    args = args || {};
    args.event = args.event || "*";

    const argsCopy = {
        filterPrefix: args.filterPrefix,
        filterSuffix: args.filterSuffix,
        events: ["s3:ObjectCreated:" + args.event],
    };

    return this.onEvent(name, handler, argsCopy, opts);
}
```

Here you can see how we've added the `onObjectCreated` method to
`Bucket`'s `prototype` so that it will be available on all instances of
`aws.s3.Bucket`. We also allow optional arguments to be passed in to
help configure the event (like what filters/events to listen for) if you
want to override our defaults. However, this only adds the code to be
available at runtime. We also need to update the type-definition for
`Bucket` for TypeScript so that all TypeScript consumers will know this
function is now available. This fortunately also simple, and all we have
to do is the following:

```javascript
declare module "./bucket" {
    interface Bucket {
        /** * Creates a new subscription to events fired from this Bucket to the handler provided, * along with options to control the behavior of the subscription. The handler will be * called whenever a matching [s3.Object] is created. */
        onObjectCreated(
            name: string, handler: BucketEventHandler,
            args?: ObjectCreatedSubscriptionArgs,
            opts?: pulumi.ComponentResourceOptions): BucketEventSubscription;
        // ...
```

You can see the [full patching here](https://github.com/pulumi/pulumi-aws/blob/71f11fdea5c7224dd93b774c450d6fc7f0d44b88/sdk/nodejs/s3/s3Mixins.ts#L210-L253).

This is a way to tell TypeScript that you intend to add a function to a
type later on yourself. This information will be merged into the type
information TypeScript has already built for the `Bucket` type.
Downstream consumers will then see the type with all its normal members
along with these additional members we've added after the fact. You can
read more about this in the [Declaration Merging](https://www.typescriptlang.org/docs/handbook/declaration-merging.html)
documentation for TypeScript.

And there you have it. A simple way to take a complex set of steps and
more cleanly expose it in a programming language in a way that will feel
more natural and intuitive. Hopefully this gives a good taste of what's possible with Pulumi
and why we feel like this is
the best way for people to create and update their cloud infrastructure
using real programming languages!
