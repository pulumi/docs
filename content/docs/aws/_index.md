---
title: "How to use Pulumi with AWS"
meta_desc: "Learn how to use Pulumi and AWS to code, deploy, and manage cloud, serverless, and container apps and infrastructure faster than ever before."
layout: aws-list
---

## Multi-cloud development with `@pulumi\cloud`

For a higher-level abstraction, and greater portability, the [`@pulumi\cloud-aws`](/docs/tutorials/cloudfx) library provides a set of classes that enable productive development for any cloud. When instantiated for AWS, code is adapted to use the available services in AWS, and the supporting services necessary to deploy them (e.g. IAM roles).

```javascript
var cloud = require("@pulumi/cloud-aws");

// Create RestAPI and Lambda Functions
const myLambda = new cloud.API("nameLambda");

// Create an S3 Bucket
const myBucket = new cloud.Bucket("nameBucket");

// Create container infrastructure using AWS Fargate
const myContainer = new cloud.Task("nameContainer");

// Create container infrastructure using AWS ECS
const myService = new cloud.Service("nameService");

// Create DynamoDB table
const myDatabase = new cloud.Table("nameTable");

// Create AWS Cloudwatch event rule
const myTimer = new cloud.Timer("nameTimer";)
```
