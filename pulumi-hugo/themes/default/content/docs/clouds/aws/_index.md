---
title_tag: "AWS & Pulumi"
meta_desc: Pulumi offers full support for AWS, with two providers, 10+ components, multiple templates, and numerous guides.
title: "AWS"
meta_image: /images/docs/meta-images/docs-clouds-aws-meta-image.png
h1: AWS & Pulumi
menu:
  clouds:
    identifier: aws
    weight: 1
cloud_overview: true
description: Build infrastructure on AWS using TypeScript, Python, Go, C#, Java or YAML. Pulumi supports all AWS services and stays up-to-date with all AWS features.
get_started_guide:
  link: get-started/
  icon: aws
providers:
  description: Provision hundreds of AWS cloud resources with either the AWS Classic or AWS Native provider. The AWS Native provider is in preview status, with same-day access to AWS resources available in the AWS Cloud Control API.  While AWS Classic remains fully supported, try AWS Native if you need AWS resources not available in the classic version.
  provider_list:
  - display_name: AWS Classic
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
  - display_name: AWS Native
    public_preview: true
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
- display_name: AWS IAM
  url: aws-iam/
  description:
- display_name: AWS static website
  url: aws-static-website/
  description:
- display_name: AWS QuickStart Aurora Postgres
  url: aws-quickstart-aurora-postgres/
  description:
- display_name: AWS QuickStart Redshift
  url: aws-quickstart-redshift/
  description:
- display_name: AWS QuickStart VPC
  url: aws-quickstart-vpc/
  description:
- display_name: AWS S3 Replicated Bucket
  url: aws-s3-replicated-bucket/
  description:
- display_name: Metabase (AWS)
  url: metabase/
  description:
convert:
- heading: Convert CloudFormation to Pulumi
  url: /cf2pulumi/
  description: Convert CloudFormation templates to your language of choice with Pulumi's conversion tool.
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
  - display_name: Configuring AWS Auto Scaling
    url: guides/autoscaling/
  - display_name: Using AWS CloudWatch
    url: guides/cloudwatch/
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
  - display_name: AWS index of services
    url: guides/aws-index-of-services/
policy:
  url: awsguard/
  description: Use AWSGuard to configure and enforce best practices for your Pulumi stacks.
---
