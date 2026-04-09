---
title_tag: "Choosing a Pulumi AWS Provider"
title: Choosing a provider
h1: Choosing a Pulumi AWS provider
meta_desc: Learn when to use the AWS, AWS Cloud Control, and component library packages for managing AWS infrastructure with Pulumi.
meta_image: /images/docs/meta-images/docs-clouds-aws-meta-image.png
menu:
  iac:
    parent: aws-clouds-guides
    name: Choosing a provider
    identifier: aws-guides-providers
    weight: 1
aliases:
- /docs/clouds/aws/guides/providers/
---

Pulumi offers several packages for working with AWS, each designed for a different level of abstraction or use case.
Most projects use more than one of them together. This guide explains what each package does, how they relate to one
another, and how to choose the right combination for your infrastructure.

{{% notes type="info" %}}
For most AWS infrastructure, start with the **[AWS provider](/registry/packages/aws/)**. It is the primary,
recommended choice and has the broadest coverage, documentation, and community support. Reach for the other packages
to complement it when you have a specific need.
{{% /notes %}}

## Packages at a glance

### Providers

| | [AWS](/registry/packages/aws/) | [AWS Cloud Control](/registry/packages/aws-native/) |
|---|---|---|
| **Node.js** | `@pulumi/aws` | `@pulumi/aws-native` |
| **Python** | `pulumi_aws` | `pulumi_aws_native` |
| **Go** | `github.com/pulumi/pulumi-aws/sdk/v7` | `github.com/pulumi/pulumi-aws-native/sdk/go/aws` |
| **.NET** | `Pulumi.Aws` | `Pulumi.AwsNative` |
| **Java** | `com.pulumi.aws` | `com.pulumi.awsnative` |
| **Built on** | AWS Terraform provider | AWS Cloud Control API |
| **Resource coverage** | Comprehensive (241 service modules) | CloudFormation-backed (Cloud Control API types) |
| **Naming convention** | Terraform-style (e.g., `aws.s3.BucketV2`) | CloudFormation-style (e.g., `awsnative.s3.Bucket`) |
| **Best for** | Most AWS infrastructure | Newly launched resources; CloudFormation migration |
| **Maturity** | Stable | Generally available |

### Component libraries

Component libraries build on top of the AWS provider and package common patterns into higher-level constructs.
They are not separate providers — they do not have their own state and they do not replace the AWS provider.

| | [AWSx](/registry/packages/awsx/) | [AWS API Gateway](/registry/packages/aws-apigateway/) | [Amazon EKS](/registry/packages/eks/) |
|---|---|---|---|
| **Node.js** | `@pulumi/awsx` | `@pulumi/aws-apigateway` | `@pulumi/eks` |
| **Python** | `pulumi_awsx` | `pulumi_aws_apigateway` | `pulumi_eks` |
| **Go** | `github.com/pulumi/pulumi-awsx/sdk/v2/go/awsx` | `github.com/pulumi/pulumi-aws-apigateway/sdk/go/apigateway` | `github.com/pulumi/pulumi-eks/sdk/go/eks` |
| **.NET** | `Pulumi.Awsx` | `Pulumi.AwsApiGateway` | `Pulumi.Eks` |
| **Java** | `com.pulumi.awsx` | `com.pulumi.aws-apigateway` | `com.pulumi.eks` |
| **Covers** | VPC, ECS, ECR, ALB, Lambda, CloudTrail | API Gateway REST APIs | EKS clusters |

## AWS provider

The [AWS provider](/registry/packages/aws/) is the primary and recommended package for managing AWS infrastructure
with Pulumi. It is built on the AWS Terraform provider and exposes a comprehensive, well-tested interface to AWS
services refined by a large community over many years.

The AWS provider covers 241 service namespaces and supports the full breadth of AWS resources: compute, storage,
networking, databases, messaging, security, and more. It follows a predictable naming convention where resource types
map closely to the underlying Terraform resource names (e.g., `aws.ec2.Instance`, `aws.s3.BucketV2`).

For the vast majority of AWS infrastructure, the AWS provider should be your starting point. Its resources are
thoroughly documented, support all Pulumi features (including import, state management, and drift detection), and have
extensive how-to guides written for them.

## AWS Cloud Control provider

The [AWS Cloud Control provider](/registry/packages/aws-native/) is built directly on the
[AWS Cloud Control API](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/what-is-cloudcontrolapi.html),
which AWS uses as the programmatic backing for CloudFormation. Because it derives resources directly from
CloudFormation resource schemas, it can expose new AWS resource types very quickly after they launch.

Resources in the Cloud Control provider follow CloudFormation naming conventions (PascalCase), so the equivalent of
`aws.s3.BucketV2` in the Cloud Control provider is `awsnative.s3.Bucket`.

Despite broad coverage, not every AWS resource is available through the Cloud Control API, and some resources that
are available have restricted operations (e.g., read-only support). For new projects, Pulumi recommends starting
with the primary AWS provider and pulling in Cloud Control resources only when a specific resource is not yet
available there.

## Component libraries

### AWSx

[AWSx](/registry/packages/awsx/) is a higher-level component library that sits on top of the AWS provider and
packages common AWS patterns into opinionated, reusable constructs. Rather than manually assembling many individual
resources, AWSx gives you a single component with sensible defaults that follow AWS well-architected practices.

AWSx includes components for VPC (subnets, route tables, NAT gateways, internet gateways), ECS clusters and
Fargate services, ECR repositories, load balancers (ALB/NLB), Lambda functions, and CloudTrail trails.

Because AWSx builds on top of the AWS provider, you can inspect every underlying resource it creates, override its
defaults, and use it alongside standard `aws.*` resources in the same stack without any conflict.

### AWS API Gateway

[AWS API Gateway](/registry/packages/aws-apigateway/) provides higher-level components for defining and deploying
Amazon API Gateway REST APIs. It handles the boilerplate of API Gateway stage, deployment, and integration
configuration, letting you focus on the routes and business logic of your API.

### Amazon EKS

[Amazon EKS](/registry/packages/eks/) provides components for creating and managing Amazon Elastic Kubernetes
Service clusters. It handles the complexity of node groups, VPC configuration, IAM roles, and add-ons, making it
significantly easier to stand up a production-ready EKS cluster.

## Pulumi CDK adapter

The [Pulumi CDK adapter](cdk/) allows you to use AWS CDK constructs — including CDK's L2 and L3 constructs —
directly within a Pulumi program. It is useful when your organization has existing CDK constructs you want to
leverage, or when a particular CDK construct library provides exactly what you need and you do not yet have a
Pulumi equivalent. For greenfield Pulumi projects, the native Pulumi providers and component libraries generally
offer a more idiomatic experience.

See the [Pulumi CDK guide](cdk/) for more detail.

## Choosing the right package

### Start with the AWS provider

For any new project on AWS, begin with the AWS provider. It has the broadest community support, the most extensive
documentation and examples, and the most predictable behavior. If the resource you need exists in the AWS provider,
use it there.

### When to reach for AWS Cloud Control

Reach for the AWS Cloud Control provider when:

- A newly launched AWS service or resource type is not yet available in the classic AWS provider.
- You are migrating an existing CloudFormation template to Pulumi and want resource types that map closely to their
  CloudFormation equivalents, with matching property names and structure.
- A resource type you need is only available through the Cloud Control API.

Because the Cloud Control API itself is still maturing, some resource types have limited operation support. Check the
[supported types list](https://github.com/pulumi/pulumi-aws-native/blob/master/provider/cmd/pulumi-resource-aws-native/supported-types.txt)
before designing your stack around a specific resource.

### When to use component libraries

Use the component libraries (AWSx, AWS API Gateway, Amazon EKS) when you need to stand up well-established AWS
patterns quickly and want Pulumi to handle the low-level resource wiring. They are particularly valuable for teams
who want sensible defaults without becoming experts in every service's configuration details.

For teams with strong infrastructure opinions or custom requirements — for example, an organization with specific
VPC design standards — you may prefer to use the AWS provider directly and build your own [Pulumi components](/docs/iac/concepts/resources/components/).
The component libraries and the AWS provider work well alongside one another in the same stack, so you can adopt
them selectively.

### Pulumi CDK adapter

Reach for the Pulumi CDK adapter when your team has existing CDK constructs you want to reuse during a migration to
Pulumi, or when a specific CDK construct library solves a problem for which there is no equivalent Pulumi component
yet. For new infrastructure, use the native providers and component libraries.

## Using multiple packages in a single stack

All of Pulumi's AWS packages can be used together in a single stack. Because Pulumi tracks all resources in a unified
state, there is no penalty for mixing providers or component libraries. A common pattern is to use AWSx for
networking and container infrastructure, the classic AWS provider for the majority of other resources, and the Cloud
Control provider selectively for newer resource types not yet available elsewhere.

The following TypeScript example demonstrates this pattern:

```typescript
import * as aws from "@pulumi/aws";
import * as awsnative from "@pulumi/aws-native";
import * as awsx from "@pulumi/awsx";

// AWSx handles the VPC with well-architected defaults.
const vpc = new awsx.ec2.Vpc("main", {
    natGateways: { strategy: "Single" },
});

// The classic AWS provider manages the majority of resources.
const bucket = new aws.s3.BucketV2("app-data");

// The Cloud Control provider is used for a resource type not yet
// available in the classic provider.
const slo = new awsnative.applicationsignals.ServiceLevelObjective("api-slo", {
    name: "api-latency-slo",
    sli: {
        sliMetric: {
            metricType: "LATENCY",
            operationName: "GET /api",
            metricDataQueries: [],
        },
        comparisonOperator: "LessThanOrEqualTo",
        metricThreshold: 500,
    },
    goal: {
        attainmentGoal: 99,
        warningThreshold: 99.5,
        interval: { rollingInterval: { durationUnit: "DAY", duration: 30 } },
    },
});
```

When you run `pulumi up`, Pulumi's engine coordinates all providers, resolves cross-resource dependencies, and
records the combined state in your [Pulumi Cloud](https://app.pulumi.com) backend.

## A note on naming: AWS Native and AWS Cloud Control

You may encounter references to the "AWS Native provider" in older blog posts, community discussions, or the
`@pulumi/aws-native` npm package name. This provider was renamed to the **AWS Cloud Control provider** when it
reached general availability, reflecting its underlying use of the AWS Cloud Control API. The npm package name
and registry path remain unchanged to avoid breaking existing users.

## Next steps

- [AWS provider documentation](/registry/packages/aws/)
- [AWS Cloud Control provider documentation](/registry/packages/aws-native/)
- [AWSx documentation](/registry/packages/awsx/)
- [AWS API Gateway documentation](/registry/packages/aws-apigateway/)
- [Amazon EKS documentation](/registry/packages/eks/)
- [Pulumi CDK adapter guide](cdk/)
- [Get started with AWS](/docs/iac/get-started/aws/)
