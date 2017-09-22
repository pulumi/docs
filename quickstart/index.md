---
layout: default
nav_section: "quickstart"
---

# Getting Started

Welcome to Pulumi, a new way to program the cloud. In this guide, we'll
introduce the core concepts, tools and frameworks for building and deploying
your Pulumi cloud applications.

With Pulumi, you write __programs__ that describe your cloud infrastructure and
application behaviour.  These programs have access to __packages__ which provide
cloud primitives you can use to create your application.  You can also build
your own packages with new components built from these cloud primitives, and
reuse those components across your cloud programs.  With the `pulumi`
__command-line tool__, you can manage the deployment of these applications into your
cloud provider.

In the current release, Pulumi programs can be authored in JavaScript or
TypeScript (we recommend TypeScript to get the most benefits from the tools and
frameworks).  We expect to introduce additional languages in future releases.

The current release include three packages to use as building blocks for your
Pulumi programs.  We expect to introduce additional cloud providers and
additional higher-level cloud components in future releases:
* `pulumi` - Core primitives for interacting with the Pulumi runtime
* `@pulumi/aws` - A library of the full suite of AWS resources (265 resources)
* `@pulumi/cloud` - A highly-productive, cloud-neutral library for rapid cloud
  application development

## Setup and Installation

Download `pulumi.zip`, unpack to XXX.  Put YYY on your PATH.  To verify you have
the tools insteadll, run `pulumi version`.

## Your First Program - AWS EC2 Instance

For our first application, we'll create an AWS EC2 instance and associated
Security Group using Pulumi.

Create a folder `webserver`.  In that folder, save the following as `index.js`:

```javascript
let aws = require("@pulumi/aws");

let group = new aws.ec2.SecurityGroup("web-secgrp", {
    description: "Enable HTTP access",
    ingress: [
        { protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] },
    ],
});

let server = new aws.ec2.Instance("web-server-www", {
    instanceType: "t2.micro",
    securityGroups: [ group.name ],
    ami: aws.ec2.getLinuxAMI("t2.micro"),
});
```

This example uses the `@pulumi/aws` package to create and manage AWS resources.
It creates two resources - an `aws.ec2.SecurityGroup` which allows access for
incoming HTTP requests and an `aws.ec2.Instance` which will be created in that
security group using the appropriate Amazon Machine Image (AMI) for the region
where you deploy the program.

Note that each resource expects a name as the first parameter - this name is
used by Pulumi to track 

_TODO_
* create an environment 
* plan 
* deploy
* make an edit
* re-deploy
* manage environments

### Lifecycle of a Pulumi Application

Note that when we re-deployed the application, we did not need to recreate all
of the infrastructure.  Instead, Pulumi analyses the current state of the
infrastructure and the requested new state represented by interpreting your
Pulumi application.  From these, it computes the minimal delta needed to adjust
the state of the running environment to match the new request.  For some
resources, changes can be made directly in place with no interruption to your
infrastructure.  For others, a resource may need to be replaced, and Pulumi will
create the new resource first, then update any other resources dependent on
this, before finally removing the no longer needed original resource.

_TODO_:
* Example of this.

## Pulumi Cloud Application - URL shortener

_TODO:
* `@pulumi/cloud`
* `HttpEndpoint`
* `Table`
* Getting logs from Cloudwatch

## Using TypeScript

_TODO_:
* `typescript` devDependency
* `tsconfig.json`
* `tsc`
* VS Code

