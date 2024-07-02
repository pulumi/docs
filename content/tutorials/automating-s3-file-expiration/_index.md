---
title: Automating AWS S3 File Expiration with Pulumi
meta_desc: A comprehensive guide to automate file expiration in AWS S3 using Pulumi.
description: A comprehensive guide to automate file expiration in AWS S3 using Pulumi.
page_title: Automate AWS S3 File Expiration with Pulumi
layout: topic
estimated_time: 5
providers:
    - aws
collections:
    - serverless
---

In this guide, we'll walk through the process of automating AWS S3 file expiration using Pulumi. Lifecycle rules in AWS S3 allow you to specify actions on objects that meet certain criteria over time, such as transitioning objects to a different storage class or automatically deleting them after a specified period. By following these simple steps in this guide, you'll be able to efficiently manage the lifecycle policies for objects stored in S3 buckets, ensuring that outdated files are automatically expired and removed.

With Pulumi, we can automate S3 file expiration by creating a Pulumi program that sets up these lifecycle rules. We'll use the aws.s3.BucketLifecycleConfigurationV2 resource, which allows us to define these rules programmatically.

Here's a step-by-step explanation of what we'll do:

Define the S3 Bucket: We'll create a new S3 bucket or use an existing one where the files are stored.
Set Up Lifecycle Rules: We'll define lifecycle rules to specify how files should be managed as they age. For example, we can define a rule to delete files after 30 days.
Apply the Configuration: We'll apply the lifecycle configuration to the S3 bucket using Pulumi.
Now, let's write a Pulumi program in TypeScript that creates an S3 bucket with a lifecycle policy to transition objects to Glacier after 90 days.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

// Create an S3 bucket
const bucket = new aws.s3.Bucket("my-automated-bucket", {
    // Bucket settings can be added here
});

// Define a lifecycle rule to transition objects to Glacier after 90 days
const bucketLifecyclePolicy = new aws.s3.BucketLifecycleConfigurationV2("my-bucket-lifecycle", {
    bucket: bucket.id,
    rules: [
        {
            id: "archiveToGlacier",
            status: "Enabled",
            filter: {
                prefix: "documents/",
            },
            transitions: [
                {
                    days: 90,
                    storageClass: "GLACIER",
                },
            ],
        },
    ],
});

// Define a bucket policy to enforce server-side encryption with AWS managed keys (SSE-S3)
const bucketPolicy = new aws.s3.BucketPolicy("my-bucket-policy", {
    bucket: bucket.id,
    policy: bucket.id.apply(id => JSON.stringify({
        Version: "2012-10-17",
        Statement: [
            {
                Sid: "EnforceSSE",
                Effect: "Deny",
                Principal: "*",
                Action: "s3:PutObject",
                Resource: `arn:aws:s3:::${id}/*`,
                Condition: {
                    StringNotEquals: {
                        "s3:x-amz-server-side-encryption": "AES256",
                    },
                },
            },
        ],
    })),
});

// Export the name of the bucket
export const bucketName = bucket.id;
```

In this program, we start by importing the AWS module from Pulumi. We then create an S3 bucket named my-automated-bucket. After that, we define a lifecycle configuration for this bucket. The lifecycle configuration includes a rule named archiveToGlacier, which transitions objects under the documents/ prefix to the Glacier storage class after 90 days.

The filter property with the prefix sub-property ensures that this rule only applies to objects stored under the documents/ folder. The transitions property inside the rule controls the transition of the objects. The days sub-property specifies the number of days after object creation when the objects should be transitioned to Glacier.

Finally, we export the bucket name, which can be useful if you want to reference this bucket from other parts of your Pulumi program or from other Pulumi stacks.

## Verify the configuration of your S3 file expiration

After deployment, you can verify the lifecycle configuration in the AWS Management Console:

- Navigate to the S3 service.
- Find and select your newly created bucket.
- Go to the "Management" tab.
- Check the "Lifecycle rules" section to see the applied rules.

## Wrapping up

This simple Pulumi program will ensure that any files uploaded to the documents/ folder in your S3 bucket will be automatically transitioned to Glacier after 90 days, helping you manage storage costs and keep your bucket tidy without manual intervention.

## Additional use cases for S3 automation with Pulumi

Automating S3 with Pulumi can extend beyond file expiration to address various other needs. Here are some additional use cases:

- **Automated Data Archiving**: Set up lifecycle policies to automatically transition older data to Glacier for cost-effective long-term archiving.
- **Security Compliance**: Automatically apply and enforce bucket policies to meet security and compliance requirements across all S3 buckets.
- **Disaster Recovery**: Automatically replicate data across different regions to ensure high availability and disaster recovery.
- **Data Processing Workflows**: Trigger Lambda functions to process data as soon as it's uploaded to S3, for use cases like image resizing, data transformation, or machine learning inference.
- **Audit and Monitoring**: Continuously monitor access and changes to S3 objects and generate alerts or reports for audit purposes.

By leveraging Pulumi with AWS S3, you can automate and streamline various aspects of your AWS S3 management, leading to more efficient, cost-effective, and secure cloud storage operations.

For more advanced configurations, refer to the [Pulumi AWS documentation](/docs/reference/pkg/aws/s3/bucketlifecycleconfiguration/) and the [AWS S3 Lifecycle Management guide](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html).

## Want to learn more about Pulumi?

Pulumi is free, [open source](https://github.com/pulumi/pulumi), and optionally pairs with the [Pulumi Cloud](/docs/pulumi-cloud/) to make managing infrastructure secure, reliable, and hassle-free.

- Follow the [Getting Started](/docs/get-started/) guide to give Pulumi a try.

- [Join our community on Slack](https://slack.pulumi.com/) to discuss this guide, and let us know what you think.
