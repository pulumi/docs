---
title: "Creating an AWS DynamoDB Data Service with Pulumi"
meta_desc: "Learn how to use Pulumi to define an AWS DynamoDB resource which can then be deployed to AWS and managed as infrastructure as code."
meta_image: "/images/docs/service/aws-dynamodb.png"

service: "DynamoDB"
description: "is a fast and flexible nonrelational database service for all applications that need consistent, single-digit millisecond latency at any scale"
aws_here: "https://aws.amazon.com/dynamodb/"

layout: aws-single
menu:
  aws:
    name: DynamoDB
---

## Create an AWS DynamoDB resource using `@pulumi/aws`

The `@pulumi/aws` library enables fine-grained control over the AWS DynamoDB resource meaning it can be coded, deployed, and managed entirely in code.

```javascript
const aws = require("@pulumi/aws");

const db = new aws.dynamodb.Table("mytable", {
    attributes: [
        { name: "Id", type: "S" },
    ],
    hashKey: "Id",
    readCapacity: 1,
    writeCapacity: 1,
});
```
