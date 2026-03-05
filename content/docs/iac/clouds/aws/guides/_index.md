---
title_tag: "AWS Guides | Pulumi IaC"
title: Guides
h1: AWS Guides
meta_desc: Guides for working with AWS services using Pulumi's AWS providers and component packages.
meta_image: /images/docs/meta-images/docs-clouds-aws-meta-image.png
menu:
  iac:
    name: Guides
    identifier: aws-clouds-guides
    parent: aws-clouds
    weight: 1

aliases:
- /docs/reference/crosswalk/aws/
- /docs/reference/crosswalk/
- /docs/guides/crosswalk/
- /docs/guides/crosswalk/aws/
- /docs/clouds/aws/aws-guides/
- /docs/clouds/aws/guides/
---

This section contains guides for working with AWS services using Pulumi. The guides use the following packages:

- [AWS provider (`@pulumi/aws`)](/registry/packages/aws/) — the primary provider for managing AWS resources
- [AWSx (`@pulumi/awsx`)](/registry/packages/awsx/) — higher-level components that implement well-architected patterns for common AWS services
- [AWS API Gateway (`@pulumi/aws-apigateway`)](/registry/packages/aws-apigateway/) — components for building and deploying [Amazon API Gateway](https://aws.amazon.com/api-gateway/) REST APIs
- [EKS (`@pulumi/eks`)](/registry/packages/eks/) — components for creating and managing [Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/) clusters
- [AWS Cloud Control (`@pulumi/aws-native`)](/registry/packages/aws-native/) — provider with coverage of all resources in the AWS Cloud Control API

### Containers

- [Elastic Container Service (ECS)](ecs)
- [Elastic Kubernetes Service (EKS)](eks)
- [Elastic Container Registry (ECR)](ecr)

### Serverless

- [Lambda](lambda/)
- [API Gateway](api-gateway/)

### Core infrastructure

- [Elastic Load Balancing (ELB)](elb)
- [Identity and Access Management (IAM)](iam)
- [Virtual Private Cloud (VPC)](vpc)
