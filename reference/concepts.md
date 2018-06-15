---
title: Concepts
---

Pulumi is an open-source tool and service that allows you to easily connect and compose services for modern
cloud applications. Instead of using a configuration language, you use JavaScript or Python to define your desired cloud
resources. This reduces the learning curve and makes it easier to express your configuration requirements.

Pulumi enables developers to easily create repeatable infrastructure, and allows DevOps engineers to move logic out of
scripts and onto one toolchain. Instead of treating application code and infrastructure as separate things that are
managed by very different tools, Pulumi provides one tool for defining all aspects of a distributed cloud application.

Because Pulumi uses general purpose programming languages, you don't have to learn a custom configuration language. You can also bring software engineering to the task of defining cloud infrastructure, with reusable libraries, type checking, IDE tooling, and testing. Pulumi currently supports JavaScript, TypeScript, and Python, with more languages supported in the future.

Pulumi is based on the concept of _immutable infrastructure_.  Pulumi programs are not like Boto scripts that mutate infrastructure each time you run them. Instead, Pulumi runs your program to generate the desired set of resources and their dependencies, first showing a preview of changes before they are actually applied.

Pulumi supports all major clouds --- including AWS, Azure and Google Cloud, as well as Kubernetes clusters. There is also a higher level Pulumi Cloud Framework that makes it easy to configure resources in common patterns, such as a Docker container connected to a load balancer, a serverless API that has both static content and functions, or a standard network configuration for a VPC.

## Better together: containers + serverless functions + infrastructure

Pulumi supports the full spectrum of cloud programs.  

You can use serverless functions and APIs:

```javascript
// Create a public HTTP endpoint (using AWS APIGateway)
const endpoint = new cloud.HttpEndpoint("hello");

// Serve static files from the `www` folder (using AWS S3)
endpoint.static("/", "www");

// Serve a simple REST API on `GET /name` (using AWS Lambda)
endpoint.get("/source", (req, res) => res.json({name: "AWS"}))

// Export the public URL for the HTTP service
exports.url = endpoint.publish().url;
```

Or containers:

```javascript
// Create a container with a stable, load balanced DNS name:
let cache = new cloud.Service("my-web-app", {
    // point to a local folder that contains a Dockerfile
    build: "./app", 
    memory: 128,
    ports: [80],
});
```

Or low-level cloud infrastructure:

```javascript
// Create a simple VM-based web server in AWS listening on port 80:
let group = new aws.ec2.SecurityGroup("web-secgrp", {
    ingress: [
        { protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] },
    ],
});
let server = new aws.ec2.Instance("web-server", {
    instanceType: "t2.micro",
    securityGroups: [group.name],
    ami: "ami-7172b611",
});
```

Pulumi enables you to mix and match these high- and low-level cloud resources inside of the same program or file. If you are replacing infrastructure automation tools or CloudFormation and Azure Resource Manager templates, you'll likely use pure infrastructure. If you are building a traditional web workload or a serverless application, you can use the higher-level libraries. Because Pulumi makes it easy to compose resources, you can choose the exact kinds of resources that your application needs.

Pulumi covers a range of scenarios, whether you are using containers, serverless, virtual machines, public clouds, or private clouds.

## What Pulumi is not

Pulumi is not a PaaS.  For the most part, it gets entirely out of your way at runtime. Although Pulumi eases the integration between application code and infrastructure, it generally does not influence your runtime behavior.  For example, when you provision a container or Lambda function with Pulumi, you are running directly against your chosen cloud provider.

## Pulumi concepts

A Pulumi program is just an ordinary program authored in JavaScript or Python. A program has [project file](./project.html) named Pulumi.yaml in its root.

A program may require [configuration](./config.html), such as the region you are deploying to, specific resource options (such as storage configuration, instance size, or number of instances). You can also securely store [secrets](./config/html#secrets), such as passwords and tokens for external services. Configuration and secrets are all stored outside of your program text, which makes it easy to deploy multiple instances of your program with different values.

A program is deployed to a [stack](./stack.html), which is an isolated, independently configurable instance of your program's resources. Each stack represents one of the environments in which the program runs, such as `staging`, `production` or `dev-alice`. Since configuration can vary from one stack to another, it is easy to specify that a development stack should provision fewer resources than the production version.

Each Pulumi stack has a collection of associated resources.  A resource defines and tracks an externally managed cloud resource - such as an AWS Lambda Function, a Kubernetes Pod or an Azure Virtual Network.  Each resource is managed by a **resource provider** which defines how creation, update and delete of resources should be managed in the target cloud environment. You can create and use [components](./programming-model.html#components), which are themselves composed of many resources. Components make it possible to create and share new abstractions on top of raw cloud infrastructure resources.

### Lifecycle of a Pulumi Stack

A stack exists from the time it is created (`pulumi stack init`) until it is deleted (`pulumi stack rm`). During that time, it can have a number of deployments (`pulumi update` or `pulumi destroy`).  

Each deployment runs the program to determine what the desired state is, and then creates, updates or deletes various resources to achieve that desired state.  As a result, at any given point in time, the stack has a set of resources associated with it.

Some of those resources may have runtime code associated with them, which can run continuously throughout the lifetime of the resource (in the case of containers or VMs), or on-demand (in the case of serverless functions).
