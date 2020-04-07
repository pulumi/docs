---
title: "Architecture as Code: Microservices"
date: 2020-04-07
meta_desc: "Build microservices with reusable components created with common programming languages and Pulumi"
meta_image: microservices.png
authors:
    - sophia-parafina
tags:
    - microservices
---

This article is the third in a series about Architecture as Code. The [first article]({{ relref "/blog/architecture-as-code-intro">}}) provided an overview of virtual machines, microservices, serverless, and Kubernetes. The [second]({{< relref "/blog/architecture-as-code-vm" >}}) one went in-depth on deploying virtual machines as reusable components. In this third installment, we'll look at microservices and how to implement them as reusable components with Pulumi.

<!--more-->

## Microservices

Microservice architecture is based on the idea that each service represents an individual capability or function in an application. Services are independent of each other and can be deployed without service interruption. They communicate with each other via requests over HTTP typically through REST interfaces.

Each service is an application unto itself that must be written, configured, and deployed in coordination with other services that comprise the application. Cloud-based resources have made standing up microservices easier; however, we still need to configure each service. The advantage of using standard programming languages to deploy services is that we can further abstract resources into reusable components and apply testing methodologies to improve quality.

In the following sections, we'll discuss how to organize an application as microservices using stacks in Pulumi and how to configure the stacks so they can talk to each other. Also, we'll look at an example application and show how to create reusable components to build microservices.

## Projects and Stacks

Pulumi is organized around [Projects]({{< relref "/docs/intro/concepts/project" >}}) and [Stacks]({{< relref "/docs/intro/concepts/stack" >}}).  A Project specifies the runtime to use, which determines where to find the program to execute during deployment. A Stack is an independent instance of a Pulumi program used to denote different phases of development (such as development, staging, and production) or feature branches (such as new-feature-dev).

Monolithic stacks are a common way to structure a project. A single project defines the infrastructure and resources for an entire service. However, Pulumi also supports deploying microservices as individual stacks within a project. Because microservices represent a specific business capability, having stacks for each service allows teams to work independently of each other. Separate stacks can enforce security policies through Role-Based Access Control, and each service can be built and deployed independently of other components.

Microservices deployed as stacks communicate with each other through the [StackReference](https://www.pulumi.com/docs/intro/concepts/organizing-stacks-projects/#inter-stack-dependencies) resource, which makes stack exports such as networking, environmental variables, and even Kubernetes configuration available to stacks in the project. The `StackReference` constructor takes as input a string of the form `<organization>/<project>/<stack>`, and lets services access the outputs of that stack. The following section walks through a microservices example that deploys a database on AWS RDS, a REST application in AWS Fargate, and an AWS Application Load Balancer.

## A Microservices Application Infrastructure

We'll use the [AWS Stack Reference example](https://github.com/pulumi/examples/tree/master/aws-stackreference-architecture) to illustrate how Pulumi uses Architecture as Code to create reusable components and deployment frameworks. We’ve previously [blogged]({{< relref "blog/architect-aws-application-infra-with-pulumi-stack-references" >}}) about this example and covered the code in some detail.

Let's examine how it creates reusable components for building out resources. First up is the [VPC class](https://github.com/pulumi/examples/blob/master/aws-stackreference-architecture/networking/src/vpc.ts) in the [networking stack](https://github.com/pulumi/examples/tree/master/aws-stackreference-architecture/networking).

In the networking service, [`vpc.ts](https://github.com/pulumi/examples/blob/master/aws-stackreference-architecture/networking/src/vpc.ts) creates a TypeScript class that extends Pulumi ComponentResource. A ComponentResource abstracts one or more children that do not require custom create, read, update, and delete operations for provisioning. We can add the related resources to the correct parent to build out the class.

```ts
export class Vpc extends ComponentResource {
    vpc: aws.ec2.Vpc;
    privateZone: aws.route53.Zone;
    dhcpOptionSet: aws.ec2.VpcDhcpOptions;
    internetGateway: aws.ec2.InternetGateway;
    publicSubnets: aws.ec2.Subnet[] = [];
    privateSubnets: aws.ec2.Subnet[] = [];
    publicRouteTable: aws.ec2.RouteTable;
    privateRouteTables: aws.ec2.RouteTable[] = [];
    natGateways: aws.ec2.NatGateway[] = [];
    natElasticIpAddresses: aws.ec2.Eip[] = [];

   // ...

`"

The resource needs an interface to set the name and parameters for our new VPC class.

```ts
export interface VpcArgs {
    description: string;
    baseTags: aws.Tags;

    baseCidr: string;
    availabilityZoneNames: string[];
    enableFlowLogs?: boolean;

    endpoints: {
        s3: boolean;
        dynamodb: boolean;
    };
}
```

Finally, we need to be able to peer VPCs so that the services can communicate with each other. We can take advantage of TypeScript's [member function](https://www.typescriptlang.org/docs/handbook/classes.html#public-private-and-protected-modifiers) to implement peering.

```ts
public configurePeering(args: PeerToArgs) {

  // …
}
```

We can reuse this pattern to build a reusable [database component](https://github.com/pulumi/examples/blob/master/aws-stackreference-architecture/database/src/database.ts) from RDS. Likewise, the [REST application](https://github.com/pulumi/examples/blob/master/aws-stackreference-architecture/application/src/application.ts) creates a service using a container deployed in Fargate and fronted by an ALB. You can replace the container with an updated application without interrupting the service.

## Jumping In

We encourage you to try out deploying microservices with stacks. To download just the stack example from the  [examples repository](https://github.com/pulumi/examples/) we'll use a git sparse checkout to only copy the [aws-stackreference-architecture](https://github.com/pulumi/examples/tree/master/aws-stackreference-architecture) directory.

```bash
$ mkdir microservices
$ cd microservices

$ git init
$ git remote add origin -f https://github.com/pulumi/examples/
$ git config core.sparseCheckout true
$ aws-stackreference-architecture >> .git/info/sparse-checkout
$ git pull origin master
```

Follow the instructions to deploy the application. One caveat, when deploying the network microservice, set the number of availability zones to a minimum of two, e.g., `pulumi config set azCount 2`. Experiment with the example by adding data to the database and adding your REST application as a container. Add a web client to submit requests and display them. Let us know if you have questions on [Community Slack](https://pulumi-community.slack.com/) or send a tweet to show off your application.

To learn more about stacks, watch [Mike Metral's](https://twitter.com/mikemetral) presentation on [PulumiTV](https://www.youtube.com/channel/UC2Dhyn4Ev52YSbcpfnfP0Mw).

{{< youtube "629luaYjwMQ" >}}
