---
title_tag: Templates for Deploying Container Services
title: Container Service Templates
layout: overview
schema_type: faq
description: Pulumi templates for container services on AWS, Azure, and Google Cloud. Each template ships predefined infrastructure as code in your language of choice.
meta_desc: Deploy container services on AWS, Azure, or Google Cloud with Pulumi Container Service templates.
meta_image: meta.png
weight: 1
---

## About these templates

### What is a container service?

A container service is a managed cloud offering that runs containerized applications without requiring you to operate the underlying servers. The service handles container scheduling, scaling, networking, and (for Kubernetes-based options) cluster management. Containers themselves are lightweight, isolated runtime environments that package an application together with its dependencies, typically built from a Docker image.

### Which container service should I use on each cloud?

The major clouds each offer several container services with different operational tradeoffs:

- **AWS**: [Amazon ECS](/registry/packages/aws/api-docs/ecs/) for AWS-native orchestration, [Amazon EKS](/registry/packages/eks/) for managed Kubernetes, and [AWS Fargate](/registry/packages/awsx/api-docs/ecs/fargateservice/) for serverless compute behind either.
- **Azure**: [Azure Container Instances (ACI)](/registry/packages/azure-native/api-docs/containerinstance) for serverless single-container workloads, and [Azure Kubernetes Service (AKS)](/registry/packages/azure-native/api-docs/containerservice/managedcluster) for managed Kubernetes.
- **Google Cloud**: [Cloud Run](/registry/packages/gcp/api-docs/cloudrun) for serverless containers, and [Google Kubernetes Engine (GKE)](/registry/packages/gcp/api-docs/container/cluster) for managed Kubernetes.

### How do I deploy a container service with Pulumi?

Use one of the Container Service templates above to scaffold a complete Pulumi project that provisions a container service and the infrastructure it depends on, including a registry for your container image and a load balancer or HTTPS endpoint where applicable. Templates are available in TypeScript, Python, Go, and C#, and each one deploys end to end with `pulumi new` followed by `pulumi up`.

### What languages can I use to define container infrastructure with Pulumi?

Pulumi lets you define container infrastructure in TypeScript or JavaScript, Python, Go, Java, .NET (C#), or YAML. You use the same language for both your application and its infrastructure, with full editor tooling, package management, and testing support.
