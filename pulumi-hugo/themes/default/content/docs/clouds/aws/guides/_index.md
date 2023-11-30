---
title_tag: "Crosswalk for AWS Guides"
title: Guides
h1: AWS Guides
meta_desc: Pulumi Crosswalk for AWS supports a simplified approach to defining and deploying cloud infrastructure.
meta_image: /images/docs/meta-images/docs-clouds-aws-meta-image.png
menu:
  clouds:
    identifier: aws-guides
    parent: aws
    weight: 4

aliases:
- /docs/reference/crosswalk/aws/
- /docs/reference/crosswalk/
- /docs/guides/crosswalk/
- /docs/guides/crosswalk/aws/
---
<a href="./">
    <img src="/images/docs/reference/crosswalk/aws/logo.svg" align="right" width="280" style="margin: 0 0 32px 16px;">
</a>

Pulumi Crosswalk for AWS is a collection of libraries that use automatic well-architected best practices to make common infrastructure-as-code tasks in AWS easier and more secure.

<img src="/images/docs/reference/crosswalk/aws/arch.png">

## Overview

Pulumi Crosswalk for AWS supports "day one" tasks, such as creating your initial container-based workloads using
[Amazon Elastic Container Service (ECS)](/docs/clouds/aws/guides/ecs)---including Fargate or [Kubernetes (EKS)](
eks)---and creating serverless workloads using [Amazon API Gateway](/docs/clouds/aws/guides/api-gateway/) and [AWS Lambda](/docs/clouds/aws/guides/lambda/). Secure and cost-conscious defaults are chosen so that simple programs automatically use best practices for the underlying infrastructure, enabling better productivity with confidence.

Pulumi Crosswalk for AWS also supports "day two and beyond" tasks, such as scaling your workload, securing and
integrating it with your existing infrastructure, or going to production in multiple complex environments. This includes [Amazon Virtual Private Cloud (VPC)](/docs/clouds/aws/guides/vpc) for network isolation, [AWS Auto Scaling](
autoscaling) for dynamic scaling, and [AWS Identity and Access Management (IAM)](/docs/clouds/aws/guides/iam) for
securing your infrastructure.

For example, this program builds and publishes a Dockerized application to a private [Elastic Container Registry (ECR)](
ecr), spins up an ECS Fargate cluster, and runs a scalable, load balanced service, all in
response to a single `pulumi up` command line invocation:

{{< example-program path="awsx-load-balanced-fargate-ecr" >}}

This example uses the default VPC and reasonable security defaults, but supports easy customization of all aspects.

## Code Example Deep Dive

Watch this video to dive into an Amazon ECS and Fargate code example that conceptually illustrates the benefits of using Crosswalk libraries versus authoring code from scratch with the [AWS classic provider](/registry/packages/aws/).

{{< youtube "gi9ZoZwzHAM?rel=0" >}}

## Getting Started

To get started with Pulumi Crosswalk for AWS, [download and install Pulumi](/docs/install/), and [configure it to work with your AWS account](/registry/packages/aws/installation-configuration/). Afterwards,
[try the tutorial for Running Containers on ECS Fargate](/registry/packages/aws/how-to-guides/ecs-fargate/) or select one of the
relevant User Guides to get started:

### Containers

* [Elastic Container Service (ECS)](ecs)
* [Elastic Kubernetes Service (EKS)](eks)
* [Elastic Container Registry (ECR)](ecr)

### Serverless

* [Lambda](lambda/)
* [API Gateway](api-gateway/)

### Monitoring

* [CloudWatch](cloudwatch/)

### Core Infrastructure

* [Auto Scaling](autoscaling/)
* [Elastic Load Balancing (ELB)](elb)
* [Identity and Access Management (IAM)](iam)
* [Virtual Private Cloud (VPC)](vpc)

### Continuous Deployment

* [Using Pulumi from AWS Code Services](/docs/using-pulumi/continuous-delivery/aws-code-services/)

### Other AWS Services

Pulumi supports the entirety of the AWS platform. If your favorite service isn't listed above, check out:

* [AWS Index of Services](aws-index-of-services/)

## Frequently Asked Questions (FAQ)

### What Clouds Does Pulumi Crosswalk Support?

Pulumi Crosswalk supports AWS only at the moment. Support for additional clouds is on the roadmap
([Azure](https://github.com/pulumi/pulumi-azure/issues/277), [Google Cloud](https://github.com/pulumi/pulumi-gcp/issues/165),
and [Kubernetes](https://github.com/pulumi/pulumi-kubernetes/issues/589)).

### What Languages are Supported?

Pulumi Crosswalk for AWS is available for all supported Pulumi languages.

### What Packages Define Pulumi Crosswalk for AWS?

Because Pulumi Crosswalk for AWS is a broader "brand" for our framework spanning multiple packages, there isn't
a single package that contains everything. The [`@pulumi/aws`](/registry/packages/aws/api-docs),
[`@pulumi/awsx`](/registry/packages/awsx/api-docs/), [`@pulumi/aws-apigateway`](/registry/packages/aws-apigateway/api-docs/) and
[`@pulumi/eks`](/registry/packages/eks/api-docs/) packages each has an important role to play.

### Is Pulumi Crosswalk for AWS Free to Use?

Yes, Pulumi Crosswalk for AWS is completely open source and free to use, along with the Individual Edition of Pulumi.
[Pulumi's commercial offerings](/pricing) already fully support Pulumi Crosswalk for AWS.

If you would like to contribute to the packages, please see the relevant repo on GitHub: [`pulumi/pulumi-aws`](
https://github.com/pulumi/pulumi-aws), [`pulumi/pulumi-awsx`](https://github.com/pulumi/pulumi-awsx) [`pulumi/pulumi-aws-apigateway`](https://github.com/pulumi/pulumi-aws-apigateway/), or
[`pulumi/eks`](https://github.com/pulumi/pulumi-eks). Issues and Pull Requests are welcome!

### If I'm an Existing User, What Has Changed?

The primary change is new functionality added to the above packages, and the availability of these User Guides.
Pulumi Crosswalk for AWS continues to work with the standard Pulumi CLI and Pulumi Cloud. If you already use the free Individual
Edition, or paid Team or Enterprise Edition, you can continue to do so now with Pulumi Crosswalk for AWS functionality.

### Upgrading from an old version of Pulumi Crosswalk for AWS?

Previous versions of `@pulumi/awsx` were TypeScript-only. The functionality has changed from these TypeScript-only versions.
We have taken the opportunity to move the existing TypeScript-only functionality into a `classic` namespace. To create a
VPC using the old TypeScript version of Crosswalk for AWS, the following code would work:

```typescript
import * as awsx from "@pulumi/awsx/classic";

const vpc = new awsx.ec2.Vpc("classic-vpc", {});
```

Any resource that you use from the existing library can continue to be used from that `classic` namespace. All of the classic
functionality is available in that namesoace.

### Is Support or Training Available for Pulumi Crosswalk for AWS?

Yes! Please fill out [this form](/contact/) and a Pulumi team member will be in touch.
