---
title: Introduction
---

> **Note:** The documentation is still in progress, so there are a number of TODOs and partially-written articles.
> We are hard at work finishing these.  If there is any specific content you are looking, for please reach
> out at [support@pulumi.com](mailto:support@pulumi.com) so we can prioritize adding it.

Pulumi is a programming platform for the cloud.  Pulumi lets you write cloud programs in your favorite language, using your favorite developer tools and IDEs, and handles the task of keeping your application, services, and infrastructure in sync, without needing to resort to separate configuration DSLs or templating languages.  Instead of treating application code and infrastructure as completely separate things, managed by different people with different skills using different tools, Pulumi levels the playing field by focusing on building all aspects of distributed cloud applications using a consistent set of tools and techniques.

Because Pulumi uses general purpose programming languages, you get all the things you already know and love from your favorite programming language: ranging from simple expressiveness features like loops, conditionals, and async; to a rich ecosystems of libraries from your package manager; all the way to powerful abstractions and reuse by way of classes and functions.  Pulumi currently supports JavaScript, TypeScript, and Python, with support for additional languages on the way.

Pulumi supports all major clouds -- including AWS, Azure and Google Cloud, as well as Kubernetes clusters -- and offers a higher level Pulumi Cloud Framework for productively building modern cloud-neutral applications that use containers, serverless, and hosted managed infrastructure, and that may run on any of these clouds with a great degree of code sharing.

## Better Together: Containers + Serverless Functions + Infrastructure
Pulumi supports the full spectrum of cloud programs.  It works just as well for containers

```javascript
// Create a container with a stable, load balanced DNS name:
let cache = new cloud.Service("redis-cache", {
    image: "redis:alpine",
    memory: 128,
    ports: [6379],
});
```

as it does serverless functions and APIs

```javascript
// Run a lambda every hour to clear the cache:
let { port, host } = await cache.getURL();
let redisClient() = () => require("redis").createClient(port, host);
cloud.timer.cron("clear-daily", { hourUTC: 7, minuteUTC: 30 }, async () => {
    await redisClient().clear();
});

// Register an API endpoint that can get and put keys:
let api = new cloud.APIGateway("cache-api");
api.get("/{key}", async (req, res) => {
    let obj = await redisClient().get(req.params["key"]);
    res.json(obj);
});
api.put("/{key}", async (req, res) => {
    await redisClient().put(req.params["key"], req.body);
    res.json({ status: "ok" });
});
api.publish();
```

as it does low-level cloud infrastructure

```javascript
// Create a simple VM-based web server in AWS listening on port 80:
let group = new aws.ec2.SecurityGroup("web-secgrp", {
    description: "Enable HTTP access",
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

Pulumi enables you to mix and match these high- and low-level cloud resources inside of the same program or file.  In some cases, you will want to just use pure infrastructure, such as when replacing DevOps tools, CloudFormation or Azure Resource Manager templates, or Chef and Puppet scripts; in other cases, you will want to just use the higher level frameworks, such as when building web-, API-, or event-oriented serverless applications.  We find, however, that most real world use cases end up mixing a range of these kinds of resources, because each has its own unique strengths, and the built-in composability of Pulumi makes it easy and productive to combine the best of both.

## Application and Infrastructure Code as One

Notice that, with the serverless function example earlier, we have used both **deployment-time** code -- the creation of the cache, cron-job, security group, and server -- alongside **runtime** code -- the body of the lambda itself, which may close over and capture references to other cloud resources and services.  This is a powerful capability unique to Pulumi and, much like your choice of high- versus low-level resources being unique to the situation, so too is the extent to which you will use this capability.

The ability to combine these two leads to a unique benefit of Pulumi: versioning application and infrastructure code together.  By using a consistent set of tools and languages to express all aspects of your cloud program, managing both becomes easier in a few ways; you can

* Commit both alongside one another in source control;
* Collaborate in the usual ways on changes, such as code reviews and pull requests;
* Reuse functionality flexibly across the boundaries;
* Apply traditional software engineering techniques, like testing, linting, and static analysis.

This shows up in several ways: the serverless scenario above; the ability to automatically build, publish, and consume container images as you deploy your Pulumi programs; and, the capability to version file assets within your infrastructure code, as a few examples.

Pulumi can be plugged in to your favorite CI tools to automate all application and infrastructure changes via a single CI pipeline.  This removes the need to use separate tools and services for building, packaging and publishing application code, containers, and infrastructure, and trying to keep them in sync.

Of course, you may have an application architecture where you really do want to version two layers of your system separately, and that is also well support in Pulumi.

## Immutable Infrastructure {#immutable-infrastructure}

It is important to note that Pulumi is based on the concept of **immutable infrastructure**.  Pulumi programs are not like Boto scripts that mutate infrastructure each time you run them. Instead, Pulumi runs your program to generate the desired set of resources and their dependencies.

Pulumi can perform this task in **preview mode** where you will be shown the full set of changes, in the order in which they would be made, before actually performing them.  After previewing the changes to see what would be done, you can perform an **update** which will apply those changes to the target cloud resource provider, such as AWS or Azure.

Most developers don’t need to dig into how exactly this works.  The key take-away, however, is that you have full visibility and control into the cloud resource requirements of your program.  This is often important because ultimately you will be creating resources in your cloud account.

## What Pulumi is Not

Pulumi is not a PaaS.  For the most part, it gets entirely out of your way at runtime.

Although Pulumi eases the integration between application code and infrastructure, it generally does not influence your runtime behavior.  This means, for example, that when you provision a container or lambda with Pulumi, you are running directly against your chosen cloud provider.

There are, of course, some areas where Pulumi will help you generate runtime code, such as when creating a serverless function using your favorite language’s syntax.  In these cases, Pulumi does the minimal amount of scaffolding to ensure you have a seamless experience, like injecting variables into your function’s scope.  Even then, there is no runtime agent or heavy footprint implied: it is simply code.  In other words, Pulumi is unopinionated about what runtime environment you choose to run those functions within.  We think this is important architectural decision that ensures that you retain full control over your cloud computing environment, especially in areas like security, reliability, and performance.

Pulumi also stays unopinionated about whether you choose containers, serverless, virtual machines, public clouds, or private clouds.  Pulumi as a platform is as happy if you use 100% containers as it is if you use 100% serverless functions as it is if you use a hybrid.  Indeed, Pulumi’s unique perspective is in embracing all of these things, living together in harmony.

## Next Steps

Check out the [quickstart](../quickstart) or the [conceptual documentation](./concepts.html) for more details on how to get started using Pulumi.
