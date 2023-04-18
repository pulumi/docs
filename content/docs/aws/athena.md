---
title: "Creating an AWS Athena Data Service with Pulumi"
layout: "aws-single"
meta_desc: "Learn how to use Pulumi to define an AWS Athena resource which can then be deployed to AWS and managed as infrastructure as code."
meta_image: "/images/docs/service/aws-athena.png"

service: "Athena"
aws_here: "https://aws.amazon.com/athena/"

menu:
  aws:
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
