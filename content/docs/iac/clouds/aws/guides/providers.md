---
title_tag: "Choosing a Pulumi AWS Provider"
title: Choosing a provider
h1: Choosing a Pulumi AWS provider
meta_desc: Learn when to use the AWS, AWS Cloud Control, AWSx, and Pulumi CDK packages for managing AWS infrastructure with Pulumi.
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

## Packages at a glance

| | [AWS](/registry/packages/aws/) | [AWS Cloud Control](/registry/packages/aws-native/) | [AWSx](/registry/packages/awsx/) | [Pulumi CDK](/registry/packages/aws-cdk/) |
|---|---|---|---|---|
| **npm package** | `@pulumi/aws` | `@pulumi/aws-native` | `@pulumi/awsx` | `@pulumi/cdk` |
| **PyPI package** | `pulumi_aws` | `pulumi_aws_native` | `pulumi_awsx` | `pulumi_cdk` |
| **Type** | Provider | Provider | Component library | CDK adapter |
| **Built on** | AWS SDK (via Terraform bridge) | AWS Cloud Control API | `@pulumi/aws` | AWS CDK |
| **Resource coverage** | Comprehensive (241 service modules) | 1,300+ Cloud Control types | Common patterns (VPC, ECS, etc.) | All CDK L1/L2/L3 constructs |
| **Naming convention** | Terraform-style (`aws.s3.BucketV2`) | CloudFormation-style (`awsnative.s3.Bucket`) | High-level constructs | CDK construct API |
| **Recommended for** | Most AWS infrastructure | Brand-new AWS resources; CloudFormation migration | Well-architected patterns | Teams migrating from CDK |
| **Maturity** | Stable | Generally available | Stable | Generally available |

## AWS provider

The [AWS provider](/registry/packages/aws/) (`@pulumi/aws`) is the primary and recommended package for managing
AWS infrastructure with Pulumi. It bridges HashiCorp's Terraform AWS provider, which means it exposes a comprehensive,
well-tested interface to AWS services that has been refined by a large community over many years.

The AWS provider covers 241 service namespaces and supports the full breadth of AWS resources: compute, storage,
networking, databases, messaging, security, and more. It follows a predictable naming convention where resource types
map closely to the underlying Terraform resource names (e.g., `aws.ec2.Instance`, `aws.s3.BucketV2`).

For the vast majority of AWS infrastructure, the AWS provider should be your starting point. Its resources are
thoroughly documented, support all Pulumi features (including import, state management, and drift detection), and have
extensive how-to guides written for them.

## AWS Cloud Control provider

The [AWS Cloud Control provider](/registry/packages/aws-native/) (`@pulumi/aws-native`) is built directly on the
[AWS Cloud Control API](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/what-is-cloudcontrolapi.html),
which AWS itself uses as the programmatic backing for CloudFormation. Because it derives resources directly from the
CloudFormation resource schemas, it typically supports new AWS resource types on the day they launch — before they
appear in the Terraform ecosystem that feeds the classic AWS provider.

The AWS Cloud Control provider supports over 1,300 resource types, including third-party resources registered in the
[CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) from vendors
such as MongoDB, Datadog, and Atlassian. Resources follow CloudFormation naming conventions (PascalCase), so the
equivalent of `aws.s3.BucketV2` in the Cloud Control provider is `awsnative.s3.Bucket`.

Despite broad coverage, not every AWS resource is available through the Cloud Control API, and some resources that are
available have restricted operations (e.g., read-only support). For new projects, Pulumi recommends starting with the
primary AWS provider and pulling in Cloud Control resources only when a specific resource is not yet available in the
classic provider.

## AWSx component library

[AWSx](/registry/packages/awsx/) (`@pulumi/awsx`) is not a separate provider in the same sense as the above two
packages. It is a higher-level component library that sits on top of the AWS provider and packages common AWS patterns
into opinionated, reusable constructs. Rather than manually assembling dozens of resources to create a well-architected
VPC or an ECS service, AWSx gives you a single component with sensible defaults that follow AWS best practices.

AWSx includes components for:

- VPC (subnets, route tables, NAT gateways, internet gateways)
- ECS clusters and Fargate services
- Elastic Container Registry (ECR)
- Elastic Load Balancing (ALB/NLB)
- Lambda functions
- CloudTrail trails

Because AWSx builds on top of the AWS provider, you can inspect every underlying resource it creates, override its
defaults, and use it alongside standard `aws.*` resources in the same stack without any conflict.

## Pulumi CDK adapter

The [Pulumi CDK adapter](/registry/packages/aws-cdk/) (`@pulumi/cdk`) allows you to use AWS CDK constructs — including
CDK's rich library of L2 and L3 constructs — directly within a Pulumi program. It is primarily aimed at teams that
have existing CDK constructs or CDK expertise and want to adopt Pulumi without rewriting their infrastructure
definitions from scratch.

The Pulumi CDK adapter is covered in detail in the [Pulumi CDK guide](cdk/).

## Choosing the right package

### Start with the AWS provider

For any new project on AWS, begin with `@pulumi/aws`. It has the broadest community support, the most extensive
documentation and examples, and the most predictable behavior. If the resource you need exists in the AWS provider,
use it there.

### When to reach for AWS Cloud Control

Reach for `@pulumi/aws-native` when:

- A newly launched AWS service or resource type is not yet available in the classic AWS provider. AWS Cloud Control
  support typically arrives on the same day AWS announces the resource.
- You are migrating an existing CloudFormation template to Pulumi and want resource types that map closely to their
  CloudFormation equivalents, with matching property names and structure.
- You need a third-party resource type registered in the CloudFormation Registry that has no equivalent in the classic
  provider.

Because the Cloud Control API itself is still maturing, some resource types have limited operation support. Check the
[supported types list](https://github.com/pulumi/pulumi-aws-native/blob/master/provider/cmd/pulumi-resource-aws-native/supported-types.txt)
before designing your stack around a specific resource.

### When to use AWSx

Use `@pulumi/awsx` whenever you need AWS infrastructure that follows well-established patterns and you want Pulumi to
handle the details. AWSx is particularly valuable for:

- Creating VPCs with correctly configured public and private subnets and appropriate gateway routing
- Running containers on ECS Fargate without writing the task definition, service, load balancer, and target group by
  hand
- Packaging and pushing Docker images to ECR as part of a `pulumi up` run

AWSx is best thought of as a complement to the AWS provider rather than a replacement. It handles common patterns
while the AWS provider is available for anything AWSx does not cover.

### Pulumi CDK

Choose `@pulumi/cdk` if your team is already invested in CDK's ecosystem — whether that means internal construct
libraries, L2/L3 constructs from third parties, or existing CDK stacks. For greenfield Pulumi projects, the native
Pulumi providers generally offer a more natural experience.

## Using multiple packages in a single stack

All of Pulumi's AWS packages can be used together in a single stack. Because Pulumi tracks all resources in a unified
state, there is no penalty for mixing providers or component libraries. A common pattern is to use AWSx for
networking and container infrastructure, the classic AWS provider for the majority of other resources, and the Cloud
Control provider selectively for newer resource types not yet available elsewhere.

The following example demonstrates this approach in TypeScript:

```typescript
import * as aws from "@pulumi/aws";
import * as awsnative from "@pulumi/aws-native";
import * as awsx from "@pulumi/awsx";

// AWSx handles the VPC with well-architected defaults.
const vpc = new awsx.ec2.Vpc("main", {
    natGateways: { strategy: "Single" },
});

// The classic AWS provider manages the S3 bucket.
const bucket = new aws.s3.BucketV2("app-data");

// The Cloud Control provider is used for a resource type not yet
// available in the classic provider.
const myNewResource = new awsnative.applicationsignals.ServiceLevelObjective("api-slo", {
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
    goal: { attainmentGoal: 99, warningThreshold: 99.5, interval: { rollingInterval: { durationUnit: "DAY", duration: 30 } } },
});
```

When you run `pulumi up`, Pulumi's engine coordinates all three providers, resolves cross-resource dependencies, and
records the combined state in your [Pulumi Cloud](https://app.pulumi.com) backend.

## A note on naming: AWS Native and AWS Cloud Control

You may encounter references to the "AWS Native provider" in older blog posts, community discussions, or the
`@pulumi/aws-native` npm package name. The AWS Native provider was renamed to the **AWS Cloud Control provider** when
it reached general availability, reflecting its underlying use of the AWS Cloud Control API. The npm package name
(`@pulumi/aws-native`) and registry path (`/registry/packages/aws-native/`) remain unchanged to avoid breaking
existing users.

## Next steps

- [AWS provider documentation](/registry/packages/aws/)
- [AWS Cloud Control provider documentation](/registry/packages/aws-native/)
- [AWSx documentation](/registry/packages/awsx/)
- [Pulumi CDK adapter guide](cdk/)
- [Get started with AWS](/docs/iac/get-started/aws/)
