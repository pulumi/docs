---
layout: default_collection
title: "How to create an AWS Simple Queue Service (SQS) with Pulumi"

cloud: "AWS"
description: "is a fully managed message queuing service that makes it easy to decouple and scale microservices, distributed systems, and serverless applications"
library: "@pulumi/aws"
service: "SQS"

brand: "aws"
og:
    description: "Use Pulumi to code, deploy, and manage cloud, serverless, and container apps and infrastructure"
    image: "/images/service/aws-sqs.png"
---

[AWS here]: https://aws.amazon.com/sqs/
[Reference docs]: /reference/aws.html
[Github @pulumi/aws]: https://github.com/pulumi/pulumi-aws 
[Configure AWS]: /install/aws.html

This reference shows how to use Pulumi to define an {{ page.cloud }} {{ page.service }} resource using pure code which can then be deployed to {{ page.cloud }} and managed as infrastructure as code.

<div class="row">
<div class="col-md-9" markdown="1">

## What is {{ page.cloud }} {{ page.service }}?

<img class="how-to-logo" src="/images/brand/{{ page.brand }}.png" alt="{{ page.brand }}" width="100">

{{ page.cloud }} {{ page.service }} {{ page.description }}. Find out more at [AWS here].

</div>
<div class="col-md-3 find-out-more" markdown="1">

### Find out more

* [Reference docs]
* [GitHub @pulumi/aws]
* [Configure AWS]

</div>
</div>



## Create an {{ page.cloud }} {{ page.service }} resource using `{{ page.library }}`

The `{{ page.library }}` library enables fine-grained control over the {{ page.cloud }} {{ page.service }} resource meaning it can be coded, deployed, and managed entirely in code. 

```javascript
const aws = require("@pulumi/aws");

const queue = new aws.sqs.Queue("myqueue");
```