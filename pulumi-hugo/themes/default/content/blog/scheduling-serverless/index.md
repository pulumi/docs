---
title: "Scheduling Serverless"
date: 2020-02-25
meta_desc: "Automate maintenance tasks by writing and scheduling serverless functions"
meta_image: meta.png
authors:
    - cyrus-najmabadi
tags:
    - serverless
    - lambda
---

Scheduling events has long been an essential part of automation; many tasks need to run at specific times or intervals. You could be checking StackOverflow for new questions every 20 minutes or compiling a report that is emailed every other Friday at 4:00 pm. Today, many of these tasks can be efficiently accomplished in the cloud. While each cloud has its flavor of scheduled functions, this post steps you through an example using [AWS CloudWatch](https://aws.amazon.com/cloudwatch/) with the help of Pulumi.

<!--more-->

## Scheduling Serverless Functions

Let's assume we have an S3 Bucket similar to the Recycle Bin on your desktop. It contains discarded items that we might not be ready to delete yet, but because we are paying for storage, we want to empty this bucket every Friday at 6:00 pm EST.

```typescript
import * as aws from "@pulumi/aws";
import { ObjectIdentifier } from "aws-sdk/clients/s3";

// Create an AWS resource (S3 Bucket)
const trashBucket = new aws.s3.Bucket("trash");
```

We’re now ready to create our Lambda function and schedule it. Pulumi simplifies creating Lambda functions by allowing us to provide a handler function to an event such as `cloudwatch.onSchedule`. To learn more, check out our [Lambdas as Lambdas](https://www.pulumi.com/blog/lambdas-as-lambdas-the-magic-of-simple-serverless-functions/) post. Let’s create a `cloudwatch.EventRuleEventHandler` async function that will get all the items from the trash bucket and delete them.

```typescript
// A handler function that will list objects in the bucket and bulk delete them
const emptyTrash: aws.cloudwatch.EventRuleEventHandler = async (
  event: aws.cloudwatch.EventRuleEvent
) => {
  const s3Client = new aws.sdk.S3(); //creates interface to service
  const bucket = trashBucket.id.get();

  const { Contents = [] } = await s3Client //get list of objects in bucket
    .listObjects({ Bucket: bucket })
    .promise();
  const objects: ObjectIdentifier[] = Contents.map(object => {
    return { Key: object.Key! };
  });

  await s3Client //delete objects
    .deleteObjects({
      Bucket: bucket,
      Delete: { Objects: objects, Quiet: false }
    })
    .promise()
    .catch(error => console.log(error));
  console.log(
    `Deleted ${Contents.length} item${
      Contents.length === 1 ? "" : "s"
    } from ${bucket}.`
  );
};
```

Now that we have our handler function, we can create a CloudWatch event that fires based on the specified schedule, which is every Friday at 6:00 pm EST. We’ll need to represent that as a Schedule Expression. CloudWatch events support cron and rate expressions. If we wanted our function to run on a set interval (i.e., every 20 minutes), we would choose a rate expression. Since we want fine-grained schedule control, we’ll be using a cron expression. You can learn more at the [Schedule Expressions documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html). Because time for cron jobs uses UTC, we’ll need to schedule our event to fire on Friday at 11:00 pm UTC.

// Schedule the function to run every Friday at 11:00pm UTC (6:00pm EST)
// More info on Schedule Expressions at
// https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html
```typescript
const emptyTrashSchedule: aws.cloudwatch.EventRuleEventSubscription = aws.cloudwatch.onSchedule(
  "emptyTrash",
  "cron(0 23 ? * FRI *)",
  emptyTrash

// Export the name of the bucket
export const bucketName = trashBucket.id;
);
```

Now, run `pulumi up` to deploy your new scheduled function.

```bash
$ pulumi up
Previewing update (dev):
…

Updating (dev):

     Type                                          Name                           Status
     pulumi:pulumi:Stack                           aws-ts-scheduled-function-dev
 +   └─ aws:cloudwatch:EventRuleEventSubscription  emptyTrash                     created
 +      ├─ aws:cloudwatch:EventRule                emptyTrash                     created
 +      ├─ aws:iam:Role                            emptyTrash                     created
 +      ├─ aws:iam:RolePolicyAttachment            emptyTrash-32be53a2            created
 +      ├─ aws:lambda:Function                     emptyTrash                     created
 +      ├─ aws:lambda:Permission                   emptyTrash                     created
 +      └─ aws:cloudwatch:EventTarget              emptyTrash                     created

Outputs:
    bucketName: "trash-1cde441"

Resources:
    + 7 created
    2 unchanged

Duration: 14s
```

Test it out by adding some items to your bucket and see if they’re deleted. You can use `pulumi logs` to view the `console.log` from the handler function. If you can’t wait until Friday, experiment with changing the cron expression and rerun `pulumi up`. You can find the [full code](https://github.com/pulumi/examples/tree/master/aws-ts-scheduled-function) in our GitHub repository.

## Want to know more?

This simple example demonstrates what you can do with serverless functions, such as AWS Lambda, without having to set up your infrastructure. Check out more serverless examples in the [Pulumi Examples](https://github.com/pulumi/examples) to see what you can build.

- [Serverless URL Shortener on Azure](https://github.com/pulumi/examples/tree/aws-ts-scheduled-function/azure-ts-serverless-url-shortener-global)
- [GCP function to SMS friends](https://github.com/pulumi/examples/tree/aws-ts-scheduled-function/gcp-py-functions)
- [Serverless App to Copy and Zip S3 Objects Between Buckets](https://github.com/pulumi/examples/tree/aws-ts-scheduled-function/aws-ts-s3-lambda-copyzip)
