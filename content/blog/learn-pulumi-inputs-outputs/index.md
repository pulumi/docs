---
title: "Learn Pulumi: Inputs and Outputs"
date: 2020-09-11T08:29:28-05:00
meta_desc: "Learn how inputs and outputs are key to building infrastructure with code."
meta_image: learn_pulumi.png
authors:
    - sophia-parafina
tags:
    - infrastructure as code
    - Promises
---

This article is about resource inputs and outputs, what they are, why we have them, and how to use them.

<!--more-->

## Inputs

When you create a resource, you pass arguments to its constructor. They are called the inputs and they can be

- concrete values (like strings, numbers, and booleans), arrays, or other structures
- asynchronous values or
- outputs from other resources

## Outputs

Cloud resources take time to create, for example, creating one or more virtual machines can take several minutes. After a resource is created, you can access any of its properties, which are called outputs. If you've written a web application, you might be familiar with the concept of [Promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise). A Promise is a proxy object for a value that's not known when the Promise is created. It lets an asynchronous method return a value like a synchronous method so that the program can execute without having to wait for a value.

Outputs are similar to Promises but are not the same. Outputs resolve to values once they're known, just like Promises. Unlike Promises, outputs also represent the dependency on the source of the value, which is how Pulumi creates a dependency graph of resources.

Pulumi lets you see how resources change with [preview]({{< relref "docs/reference/cli/pulumi_preview" >}}). A preview shows the difference from the current state to the desired state. No resources are deployed in a preview, so some outputs might not be known at runtime.

## A Web Application Example

Let's look at some code. This example is built on AWS but the same principles apply to other cloud providers. The example deploys two web servers behind a load balancer.

The first thing to notice is that the code is wrapped in an [`async ()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function) function. The reason for this is that we create a [Virtual Private Cloud (VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) which defines a virtual network for our application.  The VPC's public subnets are outputs that connect to the load balancer.

We use an AWS provided [default VPC](https://docs.aws.amazon.com/vpc/latest/userguide/default-vpc.html#default-vpc-components). The default VPC includes a default security group that allows ingress. However, we must create a security group to control egress from the VPC so that the web servers can respond.

```typescript
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";
import * as pulumi from "@pulumi/pulumi";

export = async () => {
    const config = new pulumi.Config("aws");
    const providerOpts = { provider: new aws.Provider("prov", { region: <aws.Region>config.require("region") }) };

    // Create a vpc
    const vpc = awsx.ec2.Vpc.getDefault();

    // Create a security group to open ingress to our load balancer on port 80, and egress out of the VPC.
    const sg = new awsx.ec2.SecurityGroup("web-sg", {
        vpc,
        egress: [{ protocol: "-1", fromPort: 0, toPort: 0, cidrBlocks: [ "0.0.0.0/0" ] }],
    });
```

In this part of the code, the [application load balancer (ALB)](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) is created, and port 80 is assigned to the load balancer's [listener](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html). Note that we create `publicIps` as an Output typed as a string array, which will hold the virtual machines' public IP addresses.

```typescript
    // Creates an ALB associated with the default VPC for this region and listen on port 80.
    const alb = new awsx.lb.ApplicationLoadBalancer("web-traffic", { securityGroups: [ sg ] });
    const listener = alb.createListener("web-listener", { port: 80 });
    const publicIps: pulumi.Output<string>[] = [];
```

We also call `await` to return the public subnets as an output, because we need that information before creating the virtual machines. It's important to remember you can't access the values of outputs directly. Later, we'll review other functions to manage the value of an output.

```typescript
    const subnets = await vpc.publicSubnets;
```

The most common way to use an output is to pass it to another resource as an input. In this example, we've instantiated a virtual machine per subnet, and we're passing the public IP address as its target.

```typescript
    // For each subnet, and each subnet/zone, create a VM and a listener.
    for (let i = 0; i < subnets.length; i++) {
        // Create the instance in the same VPC
        const vm = new aws.ec2.Instance(`web-${i}`, {
            ami: aws.getAmi({
                filters: [
                    { name: "name", values: [ "ubuntu/images/hvm-ssd/ubuntu-trusty-14.04-amd64-server-*" ] },
                    { name: "virtualization-type", values: [ "hvm" ] },
                ],
                mostRecent: true,
                owners: [ "099720109477" ], // Canonical
            }).then(ami => ami.id),
            instanceType: "m5.large",
            subnetId: subnets[i].subnet.id,
            availabilityZone: subnets[i].subnet.availabilityZone,
            vpcSecurityGroupIds: alb.securityGroups.map(sg => sg.securityGroup.id),
            userData: `#!/bin/bash
            echo "Hello World, from Server ${i+1}!" > index.html
            nohup python -m SimpleHTTPServer 80 &`,
        }, providerOpts);
        publicIps.push(vm.publicIp);
        alb.attachTarget("target-" + i, vm);
    }

    // Export the resulting URL so that it's easy to access.
    return { endpoint: listener.endpoint.hostname, publicIPs: publicIps  };
};
```

The last lined exports the hostname and the public IP addresses of the virtual machines as outputs. Pulumi can capture values and make them available to the project stack. This includes the command line, in the [Pulumi console](https://app.pulumi.com/), and even among stacks in your project.

The following script uses the `endpoint` output to call our webserver application.

```bash
for i in {1..5}; do curl http://$(pulumi stack output endpoint); done
```

As we can see, even with this basic "Hello World" webserver example, cloud applications introduce the problem of asynchronous resources. Inputs and outputs allow us to build infrastructure when resources are not immediately available.

## More ways to use outputs

Let's look at other ways to use a concrete value of an output. Using the example, we want to parse out the subdomain of the load balancer's hostname. Usually, you would expect a string, and we can call functions like substring and indexOf directly, but in this case, we can't because it's an Output. This is where we can use the [`apply`]({{< relref "/docs/intro/concepts/programming-model#apply" >}}) function. Pulumi invokes a callback when it knows the concrete value and `apply` takes the callback and returns another output that we can export.

```typescript
export const subdomain = listener.endpoint.hostname.apply(hostname => hostname.substring(0, indexOf(".")));
```

In addition to `apply`,  Pulumi offers other convenient helper methods for managing outputs.

If you want to call a method on a string, a number, or the underlying value, Pulumi offers a convenient way of accessing the members directly, even though it's an output. For example, we ca call the function to uppercase a string.

```typescript
export const upperHostname = listener.endpoint.hostname.toString().toUpperCase();
```

In another case, we may want to use concrete values from multiple outputs. We could do this by nesting multiple `applys`, but Pulumi provides `all` as a convenience function that can take multiple outputs and return a single output.

```typescript
export const url = pulumi.all([listener.endpoint.hostname, listener.endpoint.port]).apply( ( [hostname, port]) =>  `http://${hostname}:${port}` );
```

In addition, Pulumi has a string concatenation helper function because concatenation is frequently used. The `interpolate` function can reference outputs without calling apply or all on any of them.

``` typescript
export const url = pulumi.interpolate`http://${listener.endpoint.hostname}:${listener.endpoint.port}`;
```

This article is a brief introduction to Pulumi inputs and outputs. Learn more about the Pulumi [programming model]({{< relref "/docs/intro/concepts/programming-model" >}}) by visiting Pulumi Docs.

You can also watch the *Pulumi Help: Resource Inputs and Outputs (Node.js* on [PulumiTV](https://www.youtube.com/c/PulumiTV/).

{{< youtube "lybOxul2otM" >}}
