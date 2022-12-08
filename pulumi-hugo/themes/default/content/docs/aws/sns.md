---
title: "Creating an AWS SNS with Pulumi"
meta_desc: "Learn how to use Pulumi to define an AWS SNS resource which can then be deployed to AWS and managed as infrastructure as code."
meta_image: "/images/docs/service/aws-sns.png"

service: "SNS"
description: "is a flexible, fully managed pub/sub messaging and mobile notifications service for coordinating the delivery of messages to subscribing endpoints and clients"
aws_here: "https://aws.amazon.com/sns/"

layout: aws-single
menu:
  aws:
    name: SNS
---

## Create an AWS SNS resource using `@pulumi/aws`

The `@pulumi/aws` library enables fine-grained control over the AWS SNS resource meaning it can be coded, deployed, and managed entirely in code.

```javascript
const aws = require("@pulumi/aws");

const topic = new aws.sns.Topic("mytopic");

const topicSubscription = new aws.sns.TopicSubscription("mytopicsubscription", {
    topic: topic,
    protocol: "sqs",
    endpoint: queue.arn
});
```
