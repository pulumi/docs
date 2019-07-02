---
title: "How to create an AWS Kinesis data service with Pulumi"
meta_desc: "Use Pulumi to code, deploy, and manage cloud, serverless, and container apps and infrastructure"
meta_image: "/images/docs/service/aws-kinesis.png"

service: "Kinesis"
description: "makes it easy to collect, process, and analyze real-time, streaming data so you can get timely insights and react quickly to new information"
aws_here: "https://aws.amazon.com/kinesis/"

layout: aws-single
menu:
  aws:
    name: Kinesis
---

## Create an AWS Kinesis resource using `@pulumi/aws`

The `@pulumi/aws` library enables fine-grained control over the AWS Kinesis resource meaning it can be coded, deployed, and managed entirely in code.

```javascript
const aws = require("@pulumi/aws");

const stream = new aws.kinesis.Stream("mystream", {
    shardCount: 1
});
```
