---
title: "Using Pulumi with AWS SQS and Lambdas"
authors: ["cyrus-najmabadi"]
tags: ["JavaScript","Serverless","AWS"]
date: "2018-07-10"
meta_desc: "Learn how to use Amazon's SQS with Pulumi in order to post a Slack notification upon receipt of a message via SQS."

---

[Two weeks ago](https://aws.amazon.com/blogs/aws/aws-lambda-adds-amazon-simple-queue-service-to-supported-event-sources/)
Amazon added [Simple Queue Service](https://aws.amazon.com/sqs/) (SQS)
as a supported event source for
[Lambda](https://aws.amazon.com/lambda/). SQS is one of AWS's oldest
services, providing access to a powerful message queue that can do
things like guarantee messages will be delivered at least once, or
messages that will be processed in the same order they were received in.
Adding SQS as a supported event source for Lambda means that now it's
possible to use SQS in a serverless computing infrastructure, where
Lambdas are triggered in response to messages added to your SQS queue.
Now, instead of needing some sort of Service dedicated to polling your
SQS queue, or creating [Simple Notification Service](https://aws.amazon.com/sns/) (SNS)
notifications from your
messages, you can instead just directly trigger whatever Lambda you
want.
<!--more-->

## Example: Using AWS SQS and Lambda to post messages to Slack

Here's a simple example of using SQS as an event source with Pulumi:
upon receipt of a message via SQS we post a new message into Slack. The
full project is available on Github in our
[examples repo](https://github.com/pulumi/examples/tree/master/aws-js-sqs-slack),
and includes the instructions to get this up and running.

```javascript
let aws = require("@pulumi/aws");
let serverless = require("@pulumi/aws-serverless");
let config = require("./config");

let queue = new aws.sqs.Queue("mySlackQueue", { visibilityTimeoutSeconds: 180 });

serverless.queue.subscribe("mySlackPoster", queue, async (e) => {
    let slack = require("@slack/client");
    let client = new slack.WebClient(config.slackToken);
    for (let rec of e.Records) {
        await client.chat.postMessage({
            channel: config.slackChannel,
            text: `*SQS message ${rec.messageId}*: ${rec.body}`+
                `(with :love_letter: from Pulumi)`,
            as_user: true,
        });
        console.log(`Posted SQS message ${rec.messageId} to Slack channel ${config.slackChannel}`);
    }
}, { batchSize: 1 });

module.exports = {
    queueURL: queue.id,
};
```

## Implementing SQS in Pulumi

When we heard about this new functionality, we immediately knew we
wanted to let people access this new power from their Pulumi
applications. Based on Amazon's documentation on this new capability we
felt it would likely be very easy to provide. Amazon introduced this
functionality by reusing existing systems and APIs. Specifically, to
create a Lambda trigger off an SQS message you only need to create a new
[Event Source Mapping](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateEventSourceMapping.html)
mapping between the two. This seemed like it would be very simple, and
we set off to expose the right Pulumi API to make this possible.

[@pulumi/aws-serverless](https://github.com/pulumi/pulumi-aws-serverless)
is Pulumi's convenience library for creating
[Serverless](https://aws.amazon.com/serverless/) computing components.
And we added the necessary code to expose the functionality in our
simple Pulumi programming model
[here](https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/aws-serverless/queue.ts).
With this new API you would now be able to write code in your Pulumi
application like so:

```javascript
import * as aws from "@pulumi/aws";
import * as serverless from "@pulumi/aws-serverless";

// Create the queue. Provide whatever specific configuration you need here.
const sqsQueue = new aws.sqs.Queue("queue", {
    visibilityTimeoutSeconds: 300,
});

// Set up a subscription that will fire whenever the queue receives a message. Here we ask
// for 'batchSize = 1' so we will only process a single message at a time.
serverless.queue.subscribe("subscription", sqsQueue, async (event) => {
    // Add whatever code you want here to run in the AWS lambda. 'event' will contain the
    // all the necessary data about the message added to the queue.
}, { batchSize: 1 });
```

This example also demonstrates several of the great capabilities of a
Pulumi application. First, the ability to define your infrastructure
directly in code (i.e. the AWS Queue, Lambda, and Event Subscriptions),
instead of needing to do that separately. Second, the ability to avoid
needing to specify every single AWS resource necessary to get up and
running. For example, I did not have to supply explicit Roles,
Role-Policy-Attachments, or Permissions here as Pulumi took care of that
for me by default. Third, the ability to create an AWS Lambda directly
from a JavaScript/TypeScript arrow-function. That `async (event) => ...`
is written in code as a normal async-arrow-function, but it will be
converted by Pulumi into all the machinery necessary to have a true AWS
Lambda running in your infrastructure.

After adding the API and writing up a simple app to test things, we then
ran a `pulumi update` to deploy our application to AWS. Unfortunately,
we immediately ran into a problem:

```
Plan apply failed:
    Error creating Lambda event source mapping: ValidationException: 1 validation error detected: Value '' at
    'startingPosition' failed to satisfy constraint: Member must satisfy enum value set:
        [LATEST, AT_TIMESTAMP, TRIM_HORIZON]
```

So what happened? Well, as it turns out, Pulumi leverages and integrates
with many other amazing Open Source projects under the covers. In this
case, it was our integration with [Terraform](https://www.terraform.io/)
that was causing this small snag. It turns out that while Amazon relaxed
their API to no longer have that constraint on 'startingPosition',
Terraform was still referencing an older awssdk API that still contained
that constraint.

At Pulumi we think that Terraform is fantastic, and we love using it. So
we thought the best thing we could do in this position was to help out
that project to support this new functionality as well. We did this
around two weeks ago by contributing [this PR](https://github.com/terraform-providers/terraform-provider-aws/pull/5024)
to their project. We worked with Terraform over a couple over a few days
to get the PR up to snuff, and eventually got it in. With this, now both
Terraform and Pulumi customers will be able to benefit from these
changes in the upcoming releases for both projects!

After getting the change in we went back and tested our example and saw
that now everything worked as expected. We also expanded things out
[in an example](https://github.com/pulumi/pulumi-aws/blob/master/examples/queue/index.ts)
to show how you might use this in practice. In this example, we receive
the event, and then just write the data of it into an [S3 Bucket](https://aws.amazon.com/s3/). Running this example we now
successfully see:

```
pulumi update
Updating stack 'cysqstest'
Performing changes:

Type                                                Name                                        Status
+ pulumi:pulumi:Stack                               queue-cysqstest                             created
+ ├─ aws:serverless:Function                        subscription-queue-subscription             created
+ │ ├─ aws:iam:Role                                 subscription-queue-subscription             created
+ │ ├─ aws:iam:RolePolicyAttachment                 subscription-queue-subscription-32be53a2    created
+ │ ├─ aws:iam:RolePolicyAttachment                 subscription-queue-subscription-7cd09230    created
+ │ └─ aws:lambda:Function                          subscription-queue-subscription             created
+ ├─ aws:sqs:Queue                                  queue                                       created
+ ├─ aws:s3:Bucket                                  testbucket                                  created
+ └─ aws-serverless:queue:QueueEventSubscription    subscription                                created
+   ├─ aws:lambda:Permission                        subscription                                created
+   └─ aws:lambda:EventSourceMapping                subscription                                created

info: 11 changes performed:
+ 11 resources created
Update duration: 28s
```

Once created, we could then see this Stack at <https://app.pulumi.com>,
and we could easily use the functionality there to even navigate to
those resources over at our [AWS Console](https://console.aws.amazon.com). Over there were were able to
use the console to both send a message to the Queue, verify our Lambda
got triggered, and even check our Bucket to see the data written into
it. In only around a dozen lines of code, we were able to provision 11
AWS resources, and create a real end-to-end Serverless message-receiving
and processing pipeline. Now, we can expand on this functionality with
more resources or more functionality, run `pulumi update` and just
simply and safely update our cloud infrastructure!

You'll see this functionality lighting up in our next release of
`@pulumi/pulumi` and `@pulumi/aws-serverless`. We hope it helps you out
and makes your cloud life that much easier. Happy coding!
