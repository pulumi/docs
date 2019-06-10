---
title: "TODO Port frontmatter"
authors: ["chris-smith"]
tags: ["todo"]
date: "2017-01-01"
draft: true
description: "TODO: Put in a reasonable summary"
---


In this post, we'll look at 12 "pearls" -- bite-sized code snippets --
that demonstrate some fun ways you can program the cloud using Pulumi.
In my introductory post, I mentioned [a few of my "favorite
things"](http://joeduffyblog.com/2018/06/18/hello-pulumi/#my-favorite-things).
Now let's dive into a few specifics, from multi-cloud to cloud-specific,
spanning containers, serverless, and infrastructure, and generally
highlighting why using real languages is so empowering for cloud
scenarios. Since Pulumi lets you do infrastructure-as-code from the
lowest-level to the highest, we will cover a lot of interesting ground
in short order.

If you want to follow along and try some of this out, Pulumi is [open
source on GitHub](https://github.com/pulumi/pulumi), [free to download
and use from https://pulumi.io](https://pulumi.io), and [the
tour](https://pulumi.io/tour) will acquaint you with the CLI. Most of
the examples are directly runnable and available in [our examples
repo](https://github.com/pulumi/examples), and are just a
`pulumi up`{.highlighter-rouge} away, unlike other approaches that
require you to point-and-click around in your cloud's console, and/or
author reams of yucky YAML. And you get to use real languages!

Here is an index of the pearls in case you want to dive straight into
one in particular:

[**Infrastructure**](../../../com/pulumi/blog/index.html):

1.  [Declare cloud infra using a real language (with
    loops!)](../../../com/pulumi/blog/index.html)
2.  [Make a reusable component out of your cloud
    infra](../../../com/pulumi/blog/index.html)

[**Serverless**](../../../com/pulumi/blog/index.html):

1.  [Go serverless without the
    YAML](../../../com/pulumi/blog/index.html)
2.  [Capture state in your serverless funcs, like real
    lambdas](../../../com/pulumi/blog/index.html)
3.  [Simple serverless cron jobs](../../../com/pulumi/blog/index.html)
4.  [Run Express-like serverless SPAs and REST APIs at near zero
    cost](../../../com/pulumi/blog/index.html)

[**Containers**](../../../com/pulumi/blog/index.html):

1.  [Deploy production containers without the
    fuss](../../../com/pulumi/blog/index.html)
2.  [Use containers without
    Dockerfiles](../../../com/pulumi/blog/index.html)
3.  [Invoke a long-running container as a
    task](../../../com/pulumi/blog/index.html)

[**General Tips and Tricks**](../../../com/pulumi/blog/index.html):

1.  [Use code to avoid hard-coding
    config](../../../com/pulumi/blog/index.html)
2.  [Use config to enable multi-instantiation and code
    reuse](../../../com/pulumi/blog/index.html)
3.  [Give your components runtime
    APIs](../../../com/pulumi/blog/index.html)

Even if you're uninterested in low-level infrastructure, it can be fun
to work through these examples; it's "turtles all the way down" with
Pulumi and doing so can help understand how the system works. And
similarly, it can be fun to see the high-level scenarios these building
blocks facilitate, even if you just want to stand up containers and
functions.

And with that, let's dive in.

Infrastructure
-------------------------------

### 

[[Runnable
Example](https://github.com/pulumi/examples/tree/master/aws-js-webserver)]

Pulumi gives you a way to express infrastructure configuration using
your favorite programming language. In this article, we'll use
TypeScript on Node.js, as it delivers great productivity by blending
dynamic and static typing with the NPM ecosystem of reusable packages.

At the lowest layer, there are packages for all major cloud providers --
[AWS](https://github.com/pulumi/pulumi-aws),
[Azure](https://github.com/pulumi/pulumi-azure), [Google
Cloud](https://github.com/pulumi/pulumi-gcp) -- in addition to
[Kubernetes](https://github.com/pulumi/pulumi-kubernetes) and
[OpenStack](https://github.com/pulumi/pulumi-openstack). So, if you want
an EC2 instance, Azure CosmosDB, or Kubernetes Pod, you just
`new`{.highlighter-rouge} up an object. From there, Pulumi uses an
infrastructure-as-code approach similar to using AWS CloudFormation,
Azure Resource Manager, Google Resource Manager, Kubernetes or Helm
YAML, or Terraform -- just without the YAML DSLs.

The strength of using a language truly begins to shine when you go
beyond `new`{.highlighter-rouge}, however. Using a language gives you
control structures, like for loops and if branches. This is easy to take
for granted, but compared to existing YAML DSLs, it is very powerful.

For example, let's create three EC2 VMs and export their IP addresses.
Normally you'd need to copy-and-paste, however for loops to the rescue!

**index.ts**:

::: {.language-typescript .highlighter-rouge}
::: {.highlight}
``` {.highlight}
import * as aws from "@pulumi/aws";
let webSg = new aws.ec2.SecurityGroup("web-secgrp", { 
ingress: [
{ protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] },
],
});
let webServers = [];
for (let i = 0; i < 3; i++) {
webServers.push(new aws.ec2.Instance(`web-server-${i}`, {
instanceType: "t2.micro",
ami: "ami-6869aa05", // us-east-1-only
securityGroups: [ webSg.name ],
userData: `#!/bin/bash
` +
`echo 'Hello, World #${i}!' > index.html
` +
`nohup python -m SimpleHTTPServer 80 &
`,
}));
}
export let publicHostnames = webServers.map(s => s.publicDns);
```
