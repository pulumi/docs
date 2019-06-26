---
title: "How to create AWS EC2 instances with Pulumi"
meta_desc: "Use Pulumi to code, deploy, and manage cloud, serverless, and container apps and infrastructure"
meta_image: "/images/docs/service/aws-ec2.png"

service: "EC2"
description: "is a web service that provides secure, resizable compute capacity in the cloud. It is designed to make web-scale cloud computing easier for developers"
aws_here: "https://aws.amazon.com/ec2/"

layout: aws-single
menu:
  aws:
    name: EC2
---

## Create an AWS EC2 resource using `@pulumi/aws`

The `@pulumi/aws` library enables fine-grained control over the AWS EC2 resource meaning it can be coded, deployed, and managed entirely in code.

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
