---
title: "How to create AWS EC2 instances with Pulumi"
cloud: "AWS"
service: "EC2"
description: "is a web service that provides secure, resizable compute capacity in the cloud. It is designed to make web-scale cloud computing easier for developers"
library: "@pulumi/aws"
brand: "aws"
og:
    description: "Use Pulumi to code, deploy, and manage cloud, serverless, and container apps and infrastructure"
    image: "/images/service/aws-ec2.png"
---
<!-- Links -->
[AWS here]: https://aws.amazon.com/ec2/
[Reference docs]: ../reference/aws.html
[Example code]: https://github.com/pulumi/examples/tree/master/aws-js-webserver
[Github @pulumi/aws]: https://github.com/pulumi/pulumi-aws 
[Configure AWS]: ../install/aws.html

This reference shows how to use Pulumi to define an {{ page.cloud }} {{ page.service }} resource using pure code which can then be deployed to {{ page.cloud }} and managed as infrastructure as code.

<div class="row">
<div class="col-md-9" markdown="1">

## What is {{ page.cloud }} {{ page.service }}?

<img class="how-to-logo" src="../images/brand/{{ page.brand }}.png" alt="{{ page.brand }}" width="100">

{{ page.cloud }} {{ page.service }} {{ page.description }}. Find out more at [AWS here].

</div>
<div class="col-md-3 find-out-more" markdown="1">

### Find out more

* [Reference docs]
* [Example code]
* [GitHub @pulumi/aws]
* [Configure AWS]

</div>
</div>



## Create an {{ page.cloud }} {{ page.service }} resource using `{{ page.library }}`

The `{{ page.library }}` library enables fine-grained control over the {{ page.cloud }} {{ page.service }} resource meaning it can be coded, deployed, and managed entirely in code. 

```javascript
const aws = require("@pulumi/aws");

const eip = new aws.ec2.Eip("myeip");

const securityGroup = new aws.ec2.SecurityGroup("mysecuritygroup", {
    ingress: [
        { protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] },
    ],
});

const vpc = new aws.ec2.Vpc("myvpc", {
    cidrBlock: "10.0.0.0/16"
})

const internetGateway = new aws.ec2.InternetGateway("myinternetgateway", {
    vpcId: vpc.id,
});

const publicRouteTable = new aws.ec2.RouteTable("myroutetable", {
    routes: [
        {
            cidrBlock: "0.0.0.0/0",
            gatewayId: internetGateway.id,
        },
    ],
    vpcId: vpc.id,
});
```