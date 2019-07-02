---
title: "How to create an AWS Simple Queue Service (SQS) with Pulumi"
meta_desc: "Use Pulumi to code, deploy, and manage cloud, serverless, and container apps and infrastructure"
meta_image: "/images/docs/service/aws-sqs.png"

service: "SQS"
description: "is a fully managed message queuing service that makes it easy to decouple and scale microservices, distributed systems, and serverless applications"
aws_here: "https://aws.amazon.com/sqs/"

layout: aws-single
menu:
  aws:
    name: SQS
---

## Create an AWS SQS resource using `@pulumi/aws`

The `@pulumi/aws` library enables fine-grained control over the AWS SQS resource meaning it can be coded, deployed, and managed entirely in code.

```javascript
const aws = require("@pulumi/aws");

const queue = new aws.sqs.Queue("myqueue");
```
