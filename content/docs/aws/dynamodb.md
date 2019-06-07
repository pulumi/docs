---
title: "How to create an AWS DynamoDB data service with Pulumi"
meta_desc: "Use Pulumi to code, deploy, and manage cloud, serverless, and container apps and infrastructure"
meta_image: "/images/service/aws-dynamodb.png"

aliases: ["dynamodb.html"]

service: "DynamoDB"
description: "is a fast and flexible nonrelational database service for all applications that need consistent, single-digit millisecond latency at any scale"
aws_here: "https://aws.amazon.com/dynamodb/"

menu:
  aws:
    parent: aws
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
