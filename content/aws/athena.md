---
title: "How to create an AWS Athena data service with Pulumi"
meta_desc: "Use Pulumi to code, deploy, and manage cloud, serverless, and container apps and infrastructure"
meta_image: "/images/service/aws-athena.png"

aliases: ["athena.html"]

service: "Athena"
description: "is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL"
aws_here: "https://aws.amazon.com/athena/"

menu:
  aws:
    parent: aws
    name: Athena
---

## Create an AWS Athena resource using `@pulumi/aws`

The `@pulumi/aws` library enables fine-grained control over the AWS Athena resource meaning it can be coded, deployed, and managed entirely in code.

```javascript
const aws = require("@pulumi/aws");

const databaseBucket = new aws.s3.Bucket("mydatabasebucket");

const database = new aws.athena.Database("mydatabase", {
    name: "mydatabase",
    bucket: databaseBucket.bucket
});

const namedQuery = new aws.athena.NamedQuery("mynamedquery", {
    database: database.id,
    query: database.id.apply(n => `SELECT * FROM ${n} limit 10;`)
});
```
