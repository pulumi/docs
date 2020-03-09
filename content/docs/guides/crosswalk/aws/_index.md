---
title: "Pulumi Crosswalk for AWS"
meta_desc: Pulumi Crosswalk for AWS supports a simplified approach to defining and deploying cloud infrastructure.
linktitle: Crosswalk for AWS
menu:
  userguides:
    identifier: crosswalk-aws
    weight: 4

aliases: ["/docs/reference/crosswalk/aws/"]
---

<a href="{{< relref "./" >}}">
    <img src="/images/docs/reference/crosswalk/aws/logo.svg" align="right" width="280" style="margin: 0 0 32px 16px;">
</a>

Pulumi Crosswalk for AWS is a collection of libraries that use automatic well-architected best practices to make common infrastructure-as-code tasks in AWS easier and more secure.

<img src="/images/docs/reference/crosswalk/aws/arch.png">

## Overview

Pulumi Crosswalk for AWS supports "day one" tasks, such as creating your initial container-based workloads using
[Amazon Elastic Container Service (ECS)]({{< relref "ecs" >}})---including Fargate or [Kubernetes (EKS)](
{{< relref "eks" >}})---and creating serverless workloads using [Amazon API Gateway]({{< relref "api-gateway" >}}) and [AWS Lambda]({{< relref "lambda" >}}). Secure and cost-conscious defaults are chosen so that simple programs automatically use best practices for the underlying infrastructure, enabling better productivity with confidence.

Pulumi Crosswalk for AWS also supports "day two and beyond" tasks, such as scaling your workload, securing and
integrating it with your existing infrastructure, or going to production in multiple complex environments. This includes [Amazon Virtual Private Cloud (VPC)]({{< relref "vpc" >}}) for network isolation, [AWS Auto Scaling](
{{< relref "autoscaling" >}}) for dynamic scaling, [Amazon CloudWatch]({{< relref "cloudwatch" >}}) for
monitoring, alarms, and dashboards, and [AWS Identity and Access Management (IAM)]({{< relref "iam" >}}) for
securing your infrastructure.

For example, this program builds and publishes a Dockerized application to a private [Elastic Container Registry (ECR)](
{{< relref "ecr" >}}), spins up an ECS Fargate cluster, and runs a scalable, load balanced service, all in
response to a single `pulumi up` command line invocation:

```typescript
import * as awsx from "@pulumi/awsx";

// Create a load balancer on port 80 and spin up two instances of Nginx.
const lb = new awsx.lb.ApplicationListener("nginx", { port: 80 });
const nginx = new awsx.ecs.FargateService("nginx", {
    taskDefinitionArgs: {
        containers: {
            nginx: {
                image: "nginx",
                portMappings: [ lb ],
            },
        },
    },
    desiredCount: 2,
});

// Export the load balancer's address so that it's easy to access.
export const url = lb.endpoint.hostname;
```

This example uses the default VPC and reasonable security defaults, but supports easy customization of all aspects.

## Getting Started

To get started with Pulumi Crosswalk for AWS, [download and install Pulumi]({{< relref "/docs/get-started/install" >}}), and [configure it to work with your AWS account]({{< relref "/docs/intro/cloud-providers/aws/setup" >}}). Afterwards,
[try the Getting Started tutorial]({{< relref "/docs/tutorials/aws/ecs-fargate" >}}) or select one of the
relevant User Guides to get started:

### Containers

* [Elastic Container Service (ECS)]({{< relref "ecs" >}})
* [Elastic Kubernetes Service (EKS)]({{< relref "eks" >}})
* [Elastic Container Registry (ECR)]({{< relref "ecr" >}})

### Serverless

* [Lambda]({{< relref "lambda" >}})
* [API Gateway]({{< relref "api-gateway" >}})

### Monitoring

* [CloudWatch]({{< relref "cloudwatch" >}})

### Core Infrastructure

* [Auto Scaling]({{< relref "autoscaling" >}})
* [Elastic Load Balancing (ELB)]({{< relref "elb" >}})
* [Identity and Access Management (IAM)]({{< relref "iam" >}})
* [Virtual Private Cloud (VPC)]({{< relref "vpc" >}})

### Continuous Deployment

* [Using Pulumi from AWS Code Services]({{< relref "/docs/guides/continuous-delivery/aws-code-services" >}})

### Other AWS Services

Pulumi supports the entirety of the AWS platform. If your favorite service isn't listed above, check out:

* [Other AWS Services]({{< relref "other" >}})

## Frequently Asked Questions (FAQ)

### What Clouds Does Pulumi Crosswalk Support?

Pulumi Crosswalk supports AWS only at the moment. Support for additional clouds is on the roadmap
([Azure](https://github.com/pulumi/pulumi-azure/issues/277), [GCP](https://github.com/pulumi/pulumi-gcp/issues/165),
and [Kubernetes](https://github.com/pulumi/pulumi-kubernetes/issues/589)).

### What Languages are Supported?

Pulumi Crosswalk for AWS is currently supported only in
[Node.js (JavaScript or TypeScript) languages]({{< relref "/docs/intro/languages/javascript" >}}). Support for other languages,
[including Python](https://github.com/pulumi/pulumi-awsx/issues/308), is on the future roadmap.

### What Packages Define Pulumi Crosswalk for AWS?

Because Pulumi Crosswalk for AWS is a broader "brand" for our framework spanning multiple packages, there isn't
a single package that contains everything. The [`@pulumi/aws`]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws" >}}),
[`@pulumi/awsx`]({{< relref "/docs/reference/pkg/nodejs/pulumi/awsx" >}}), and
[`@pulumi/eks`]({{< relref "/docs/reference/pkg/nodejs/pulumi/eks" >}}) packages each has an important role to play.

### Is Pulumi Crosswalk for AWS Free to Use?

Yes, Pulumi Crosswalk for AWS is completely open source and free to use, along with the Community Edition of Pulumi.
[Pulumi's commercial offerings]({{< relref "/pricing" >}}) already fully support Pulumi Crosswalk for AWS.

If you would like to contribute to the packages, please see the relevant repo on GitHub: [`pulumi/pulumi-aws`](
https://github.com/pulumi/pulumi-aws), [`pulumi/pulumi-awsx`](https://github.com/pulumi/pulumi-awsx), or
[`pulumi/eks`](https://github.com/pulumi/pulumi-eks). Issues and Pull Requests are welcome!

### If I'm an Existing User, What Has Changed?

The primary change is new functionality added to the above packages, and the availability of these User Guides.
Pulumi Crosswalk for AWS continues to work with the standard Pulumi CLI and Pulumi Service. If you already use the free Community
Edition, or paid Team or Enterprise Edition, you can continue to do so now with Pulumi Crosswalk for AWS functionality.

### Is Support or Training Available for Pulumi Crosswalk for AWS?

Yes! Please fill out [this form]({{< relref "/contact" >}}) and a Pulumi team member will be in touch.
