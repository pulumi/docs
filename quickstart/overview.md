---
layout: default 
nav_section: "quickstart"
---

<p><a href="/quickstart">Getting Started</a> &gt; <b>Overview</b></p>

# Pulumi Overview

Now that you've learned [what Pulumi can do for you](./concepts.html), let's learn how to create awesome cloud programs.

## Languages

In the current release, Cloud Applications can be authored in [JavaScript](
https://developer.mozilla.org/en-US/docs/Web/JavaScript) or [TypeScript](https://www.typescriptlang.org/), run in
[Node.js](https://nodejs.org/en/), and use [npm](https://www.npmjs.com/) for package management. Though it's not a requirement, we recommend using TypeScript for the most productive development experience, paired with [Visual Studio Code](https://code.visualstudio.com/).

We will support additional languages in the future. [Let us know](/contact) what language you'd like to see next!

## Packages

Pulumi's current Cloud SDK includes three packages to use as building blocks for your Cloud Applications.

The following three packages are included in the Pulumi Cloud SDK by default. To use them, run `npm link <package>` or `yarn link <package>` in the consuming Cloud Application's root directory. The quickstart tutorials will walk through these. The use of `link` is temporary, and will not be required once these packages have been published to npm.

Except for the core runtime package, `pulumi`, packages are scoped underneath the `@pulumi` namespace.  Anytime you
see a `@pulumi/...` package, you can expect some reusable cloud goodness that only Pulumi can deliver!

### pulumi

[Documentation](/packages/pulumi)

The `pulumi` package contains the core primitives for interacting with the Pulumi Fabric and Cloud Runtime. Aside from the class `pulumi.Config`, which allows you to retrieve settings that are set by the Pulumi CLI, most Cloud Applications can ignore this package altogether. The packages below use the `pulumi` package.

<!-- I removed this line, since Config is in pulumi. -Donna>
<!-- although for some advanced scenarios it may be necessary. -->

### @pulumi/aws

[Documentation](/packages/pulumi-aws)

The `@pulumi/aws` package contains the full suite of over 250 AWS resources.  All AWS resources that are available in the AWS console or CloudFormation, along with their full set of configuration properties.  Using this library, you can provision and connect low level infrastructure, VMs, databases, containers, and more.

### @pulumi/cloud

[Documentation](/packages/pulumi-cloud)

The `@pulumi/cloud` package is the recommended way to program the cloud using Pulumi.  It is a highly productive,
cloud-neutral library for building Cloud Applications rapidly and productively.  Programs built using this library are
inherently capable of running on any cloud, or even on-premises! The APIs are designed to be easy to use. Using this library is the easiest way to program the cloud and leverage all it has to offer.

*Note:* We expect to introduce additional cloud providers and cloud components in future releases.

## How Pulumi Works

### Programming AWS

To see how Pulumi works, let's look a simple Pulumi Cloud Application that uses `@pulumi/aws`:

```typescript
import * as aws from "@pulumi/aws";

let group = new aws.ec2.SecurityGroup("web-secgrp", {
    description: "Enable HTTP access",
    ingress: [
        { protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] },
    ],
});

let server = new aws.ec2.Instance("web-server-www", {
    instanceType: "t2.micro",
    securityGroups: [ group.name ],
    ami: aws.ec2.getLinuxAMI(size),
});
```

This simple program does several important and powerful things:

* Imports the cloud package, `@pulumi/aws`, which gives us the ability to write real code, rather than markup, to define infrastructure.
* Defines a security group as a first-class JavaScript object. You can then use the object `group` anywhere in your code. Pulumi will automatically turn the object reference into a resource reference.
* Uses the Pulumi helper function `aws.ec2.getLinuxAMI` to get the correct AWS Linux image for the current region, since the AMI varies based on region. (You'll learn more about setting a region for a Pulumi application in [Programming AWS](./aws.html)).

Notice that there is absolutely no `XML`, `JSON`, or `YAML` configuration code that must be written.  *This is the
entire Cloud Application!*. This simple example demonstrates Pulumi's power and ease of use.

To understand how this works, however, we must return to a point made in the [Concepts](./concepts.html) article: Pulumi programs are not run like ordinary programs.  You don't simply run the program on your machine.  Instead, you give the program to Pulumi, and it analyzes it to determine how to activate the program in your target cloud environment. It then "makes it so."

<!-- TODO: flesh this out. It didn't really resonate with me, as is. -Donna -->
A Pulumi Cloud Application is essentially an eternal program runs continuously in your cloud environment, is updated
incrementally from time to time, but logically never exits. This is a subtle distinction, and a new and innovative
concept that is key to Pulumi's magic. Once you embrace this concept, you can truly leverage Pulumi to its fullest.

To explore this further, let's just look at a definition from that program:

```typescript
let server = new aws.ec2.Instance("web-server-www", { ... });
```

It wouldn't make sense to recreate the `server` EC2 instance over and over again. Instead, we want a single EC2 instance for each unique instantiation of our Cloud Application---such as dev, stage, and production---and, as we update our code, we don't want to tear down and create this VM.  This is precisely what Pulumi does.  It will create that VM once, when we first create an instance, and then incrementally update the pieces around it as needed.

In fact, Pulumi understands the minimal set of changes it needs to make by computing the difference between the current state and the new desired state.  When we update an application, Pulumi does not need to recreate all of the infrastructure.

For some resources, changes can be made directly in place with no interruption to your Cloud Application's availability.
For others, a resource may need to be replaced, and Pulumi will create the new resource first, then update any other
resources dependent on this, before finally removing the no longer needed original resource.  Although the behavior
depends on the kind of resource being updated, Pulumi handles this automatically to minimize application downtime.

Pulumi tracks the state of the infrastructure in a *checkpoint* file, stored inside the `.pulumi` folder.  This
checkpoint file file is needed to make updates to the infrastructure.  In future releases, Pulumi will support
additional methods for managing infrastructure state across updates, including a reliable deployment service.

### Pulumi vs. CloudFormation

Since this is a simple example, it might seem that using AWS CloudFormation would not be too onerous. Unfortunately, because CloudFormation lacks high-level programming language constructs, even a simple infrastructure definition is very verbose. And, because CloudFormation uses embedded formulas and strings to reference objects, it's quite error-prone. With Pulumi, you don't need special tools to analyze your infrastructure definition, you just use regular code.

In particular, it takes *90 lines* of CloudFormation JSON to define the infrastructure for this simple example. (YAML is more verbose but easier to read). Pulumi programs tend to be 10x smaller than the CloudFormation JSON they replace. 

The elided CloudFormation definition is below. Notice the use of strings to connect objects and the custom syntax of `Fn::` and `Ref`. Wouldn't you rather just use JavaScript?

```json
{
  "AWSTemplateFormatVersion" : "2010-09-09",
  "Parameters" : {
    "InstanceType" : {
        // 7 lines elided
    }
  },
  "Mappings" : {
    "AWSInstanceType2Arch" : {
      "t1.micro"    : { "Arch" : "PV64"   }
      // 35 additional lines elided
    },
    "AWSRegionArch2AMI" : {
      "us-east-1"      : { "PV64" : "ami-50842d38", "HVM64" : "ami-08842d60", "HVMG2" : "ami-3a329952"  }
      // 9 additional lines elided
    }
  },
  "Resources" : {
    "WebServerInstance": {
      "Type": "AWS::EC2::Instance",
      "Properties": {
        "ImageId" : { "Fn::FindInMap" : [ "AWSRegionArch2AMI", { "Ref": "AWS::Region" },
                    { "Fn::FindInMap" : [ "AWSInstanceType2Arch", { "Ref": "InstanceType" }, "Arch" ]}]},
        "InstanceType"   : { "Ref": "InstanceType" },
        "SecurityGroups" : [ {"Ref": "WebServerSecurityGroup"} ]
      }
    },
    "WebServerSecurityGroup" : {
      "Type" : "AWS::EC2::SecurityGroup",
      "Properties" : {
        "GroupDescription" : "Enable HTTP access",
        "SecurityGroupIngress" : [
          {"IpProtocol" : "tcp", "FromPort" : "80",
           "ToPort" : "80", "CidrIp" : "0.0.0.0/0"}
        ]
      }
    }
  }
}
```

### Programming the Cloud

Beyond verbosity, there's a deeper problem with using markup to define infrastructure: it's not automatically deployed with your code. Your application code has dependencies on a particular infrastructure setup, but you must manually manage the deployment of your infrastructure so that it matches the code you have deployed. It's not enough to version this definition along with your code; you need a system that will automatically ensure that the two are always deployed in sync. 

When you use the `@pulumi/cloud` package, Pulumi will handle this automatically! Note that you can also mix the two abstraction models; parts of your code can target AWS directly, while other parts can use higher-level abstractions.

Let's consider a concrete example. Suppose you'd like to run a Docker container in a managed container service. Even though it's a managed container service, you still have to set up ports, create and configure a load balancer, and provision and configure up network drives. You also have to build the container image, push it to registry, and pull from that registry in your managed service. This requires a lot of configuration beyond the container definition itself!

With Pulumi, you can run Docker containers in the cloud, without having to provision all these resources. You can define your Docker image in one of three ways: 1) use the `image` property to point to an image in a container registry (such as DockerHub), 2) use the `build` property to point to a folder that contains a `Dockerfile`, or 3) 
use the `function` property to define a function inline. The last of these options is unique to Pulumi. But, whichever option you choose, you'll have the most productive container deployment experience available today.

#### Use an existing container image

To provision an NGINX service scaled out over two containers, you create a `cloud.Service` with the `image` property. Although the definition is simple, behind the scenes Pulumi will provision and configure an AWS EC2 Container Service cluster (EC2), set up a load balancer, set up AWS Elastic File Service (EFS), set up and provision IAM roles, and so forth. Pulumi does all the hard work: you just have to specify a Docker image and the number of instances:

```javascript
import * as cloud from "@pulumi/cloud";
import fetch from "node-fetch";

// A simple NGINX service, scaled out over two containers.
let nginx = new cloud.Service("base-nginx", {
    containers: {
        nginx: {
            image: "nginx",
            memory: 128,
            ports: [{ port: 80 }],
        },
    },
    replicas: 2,
});
```

#### Build a container

Often, you want to run a custom container defined in a `Dockerfile`. For instance, the base image of NGINX is probably not particularly useful. With Pulumi, building a custom container is just as easy as using a pre-built Docker image! Simply use the `build` property. Pulumi will automatically provision an AWS Container Registry (ECR) instance, build the Docker container, push to ECR, and create the container using the ECR image. You just supply your container definition.

Suppose we have an `index.html` file defined in `app/content/index.html` and a `Dockerfile` defined in `app` (relative to the Pulumi program root directory). The `Dockerfile` has the following contents:

```dockerfile
FROM nginx
COPY content /usr/share/nginx/html
```

It's easy to write a Pulumi program that builds the container and deploys it to the cloud:

```typescript
let builtService = new cloud.Service("custom-nginx", {
    containers: {
        nginx: {
            build: "./app",
            memory: 128,
            ports: [{ port: 80 }],
        },
    },
    replicas: 2,
});
```

#### Define code inline

Not all container definitions are complex. With Pulumi, you can even define your container code inline, with the `function` property. You can then use other resources by referencing them directly; there's no need to do complex configuration or use a discovery servicer to find the service to connect to:

```typescript
let customWebServer = new cloud.Service("inline-container-definition", {
    containers: {
        webserver: {
            memory: 128,
            ports: [{ port: 80 }],
            function: () => {
                let endpoint = await builtService.getEndpoint("nginx", 80);

                let http = require("http");
                http.createServer((req: any, res: any) => {
                    res.end(`Hello, world! Please also visit ${JSON.stringify(endpoint)}!`);
                }).listen(80);
            },
        },
    },
    replicas: 2,
});
```

This example uses `getEndpoint()` call to retrieve the internet-addressable URL of `nginx` container in the `builtService` container service. (In this example, since we only defined one container and exposed one port, we could also have used `getEndpoint()` without arguments.

## Next Up

This is just an overview of what you can do with Pulumi. To try it out yourself, check out one of the following tutorials: 

- To program AWS resources directly, see [Programming AWS](./aws.html).
- To program against Pulumi's Cloud Framework, see [Programming the Cloud](./cloud.html).

You can even mix both styles in the same application!

