---
title: "Creating an AWS Kinesis Data Service with Pulumi"
meta_desc: "Learn how to use Pulumi to define an AWS Kinesis resource which can then be deployed to AWS and managed as infrastructure as code."
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
