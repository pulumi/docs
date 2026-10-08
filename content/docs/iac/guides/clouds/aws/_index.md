---
title_tag: "AWS Guides | Pulumi IaC"
title: AWS
h1: AWS Guides
meta_desc: Guides for working with AWS services using Pulumi's AWS providers and component packages.
menu:
    iac:
        name: AWS
        identifier: iac-guides-clouds-aws
        parent: iac-guides-clouds
        weight: 1
aliases:
- /docs/integrations/clouds/aws/guides/
- /docs/iac/clouds/aws/guides/
- /docs/reference/crosswalk/aws/
- /docs/reference/crosswalk/
- /docs/guides/crosswalk/
- /docs/guides/crosswalk/aws/
- /docs/clouds/aws/aws-guides/
- /docs/clouds/aws/guides/
---

This section contains guides for working with AWS services using Pulumi. If you are unsure which AWS package to
use for your project, see [Choosing a Pulumi AWS provider](/docs/iac/guides/clouds/aws/providers/) for a comparison of the available packages
and when to use each one.

The guides use the following packages:

- [AWS provider (`@pulumi/aws`)](/registry/packages/aws/) — the primary provider for managing AWS resources
- [AWSx (`@pulumi/awsx`)](/registry/packages/awsx/) — higher-level components that implement well-architected patterns for common AWS services
- [AWS API Gateway (`@pulumi/aws-apigateway`)](/registry/packages/aws-apigateway/) — components for building and deploying [Amazon API Gateway](https://aws.amazon.com/api-gateway/) REST APIs
- [EKS (`@pulumi/eks`)](/registry/packages/eks/) — components for creating and managing [Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/) clusters
- [AWS Cloud Control (`@pulumi/aws-native`)](/registry/packages/aws-native/) — provider with coverage of all resources in the AWS Cloud Control API

## Getting started

- [Choosing a provider](/docs/iac/guides/clouds/aws/providers/)
- [Pulumi CDK Adapter](/dev/tutorials/aws-cdk/)

## Tutorials and examples

The [Dev Center](/dev/browse/cloud/aws/) has hands-on AWS tutorials, templates, and examples. Browse them by topic:

- [Containers](/dev/browse/?cloud=aws&tag=containers): Amazon ECS, Amazon EKS, and Amazon ECR
- [Serverless](/dev/browse/?cloud=aws&tag=serverless): AWS Lambda and Amazon API Gateway
- [Networking](/dev/browse/?cloud=aws&tag=networking): VPCs, load balancers, and related infrastructure
