---
title: "How to deploy an Express app to AWS"
allow_long_title: true
meta_desc: "Use Pulumi to deploy Express.js apps on AWS with our step-by-step guide. Ideal for developers managing daily Express.js tasks on AWS."
type: ai-answers
date: 2023-07-24
---

Let's create a simple Express.js app and deploy it to AWS Elastic Beanstalk using Pulumi in TypeScript.

Let's assume that your Express.js application is already built and bundled into a ZIP file named app.zip located in the same directory as your Pulumi program.

Here's a simple Pulumi program that does the job:


```typescript

import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as fs from "fs";

// Create an AWS resource (S3 Bucket)
const bucket = new aws.s3.Bucket("s3-bucket");

// Create an object in that bucket upload the local file 'app.zip' which is the Express.js app bundle
const object = new aws.s3.BucketObject("BucketObject", {
   bucket: bucket.bucket, // reference to the s3 bucket name
   source: new.asset.FileAsset("app.zip") // path to the file
});

// create an Elastic Beanstalk Application
const app = new aws.elasticbeanstalk.Application("my-app", {});

 //  create an Elastic Beanstalk Environment
const env = new aws.elasticbeanstalk.Environment("dev", {
   application: app.name,
   solutionStackName: "64bit Amazon Linux 2018.03 v2.11.4 running Node.js",
});

// Export the name of the bucket
exports.bucketName = bucket.bucket;

```

This Pulumi program first creates an S3 bucket, then uploads the app.zip file to that bucket. After that, it creates an AWS Elastic Beanstalk application and then a new environment within that application using the Node.js solution stack. This will have your Express.js server up and running on an AWS managed environment.

In your AWS Elastic Beanstalk environment, AWS handles all the tasks of provisioning, scaling, and managing the running of your application; all you have to do is provide it with the code and some configuration settings.

Important: Make sure you have your AWS credentials set up properly on your system, and you have the proper access rights to create and manage S3 buckets and Elastic Beanstalk applications and environments.

For detailed developer guide on each of the resources you can view them on the Pulumi Registry:

* [aws.s3.Bucket](https://www.pulumi.com/registry/packages/aws/api-docs/s3/bucket/)
* [aws.s3.BucketObject](https://www.pulumi.com/registry/packages/aws/api-docs/s3/bucketobject/)
* [aws.elasticbeanstalk.Application](https://www.pulumi.com/registry/packages/aws/api-docs/elasticbeanstalk/application/)
* [aws.elasticbeanstalk.Environment](https://www.pulumi.com/registry/packages/aws/api-docs/elasticbeanstalk/environment/)