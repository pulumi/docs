---
title_tag: "AWS & Pulumi"
meta_desc: Provision and manage AWS infrastructure using TypeScript, Python, Go, C#, Java, or YAML with Pulumi's AWS providers, components, and guides.
title: "AWS"
meta_image: /images/docs/meta-images/docs-clouds-aws-meta-image.png
h1: AWS & Pulumi
menu:
  iac:
    name: AWS
    identifier: aws-clouds
    parent: iac-clouds
    weight: 1
cloud_overview: true
description: Build infrastructure on AWS using TypeScript, Python, Go, C#, Java, or YAML. Pulumi supports all AWS services and stays up-to-date with all AWS features.
get_started_guide:
  link: /docs/iac/get-started/aws/
  icon: aws
providers:
  description: |
    The Amazon Web Services (AWS) provider for Pulumi can provision cloud resources in AWS. It uses the AWS SDK to manage resources and should be your default choice for managing AWS resources. The AWS Cloud Control provider provides coverage of all resources in the AWS Cloud Control API, but not all resources are available yet.

  provider_list:
  - display_name: AWS
    recommended: true
    content_links:
    - display_name: Overview
      icon: page-small-black
      url: aws/
    - display_name: Install & config
      icon: gear-small-black
      url: aws/installation-configuration/
    - display_name: API docs
      icon: book-small-black
      url: aws/api-docs/
    - display_name: How-to guides
      icon: question-small-black
      url: aws/how-to-guides/
  - display_name: AWS Cloud Control
    content_links:
    - display_name: Overview
      icon: page-small-black
      url: aws-native/
    - display_name: Install & config
      icon: gear-small-black
      url: aws-native/installation-configuration/
    - display_name: API docs
      icon: book-small-black
      url: aws-native/api-docs/

components:
- display_name: AWSx
  url: awsx/
  description:
- display_name: AWS API Gateway
  url: aws-apigateway/
  description:

templates:
- display_name: Container service on AWS
  url: container-service/aws/
- display_name: AWS Serverless application
  url: serverless-application/aws/
- display_name: AWS static website
  url: static-website/aws/
- display_name: Virtual machine on AWS
  url: virtual-machine/aws/
- display_name: Kubernetes cluster on AWS
  url: kubernetes/aws/

guides:
  description: Learn how to use AWS & Pulumi together.
  guides_list:
  - display_name: Configuring AWS API Gateway
    url: guides/api-gateway/
  - display_name: Using AWS Elastic Container Registry (ECR)
    url: guides/ecr/
  - display_name: Using AWS Elastic Container Service (ECS)
    url: guides/ecs/
  - display_name: Using Elastic Kubernetes Service (EKS)
    url: guides/eks/
  - display_name: Using Elastic Load Balancing (ELB)
    url: guides/elb/
  - display_name: Using AWS Identity & Access Management (IAM)
    url: guides/iam/
  - display_name: Using AWS Lambda & Serverless Events
    url: guides/lambda/
  - display_name: Using AWS Virtual Private Cloud (VPC)
    url: guides/vpc/
policy:
  url: policy/
  description: Use Pulumi Policies to configure and enforce best practices for your Pulumi stacks.
aliases:
  - /docs/clouds/aws/
---
