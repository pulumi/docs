---
title: Getting Started with Pulumi and TypeScript
meta_desc: Build and deploy cloud infrastructure using TypeScript - get type safety, IntelliSense, and the full Node.js ecosystem
type: page
layout: language-start

subtitle: Build and deploy cloud infrastructure using TypeScript's type safety, IntelliSense, and the full Node.js ecosystem.

cloud_providers:
  title: Choose Your Cloud Provider
  items:
    - name: AWS
      logo: /logos/pkg/aws.svg
      description: Deploy to Amazon Web Services
      link: /docs/iac/get-started/aws/
    - name: Azure
      logo: /logos/pkg/azure.svg
      description: Deploy to Microsoft Azure
      link: /docs/iac/get-started/azure/
    - name: Google Cloud
      logo: /logos/pkg/gcp.svg
      description: Deploy to Google Cloud Platform
      link: /docs/iac/get-started/gcp/
    - name: Kubernetes
      logo: /logos/pkg/kubernetes.svg
      description: Deploy to any Kubernetes cluster
      link: /docs/iac/get-started/kubernetes/

quick_setup:
  title: Quick Setup
  steps:
    - number: 1
      title: "Install Pulumi"
      code: "curl -fsSL https://get.pulumi.com | sh"
    - number: 2
      title: "Create a new TypeScript project"
      code: "pulumi new typescript"
    - number: 3
      title: "Deploy your infrastructure"
      code: "pulumi up"

resources:
  title: Learn More
  items:
    - text: TypeScript Language Documentation
      link: /docs/iac/concepts/languages/typescript/
    - text: Pulumi TypeScript SDK Reference
      link: https://www.pulumi.com/registry/
    - text: Join our Community Slack
      link: https://slack.pulumi.com
---

## Why TypeScript for Infrastructure?

- **Type Safety**: Catch configuration errors at compile time with TypeScript's strong typing system
- **IntelliSense**: Get auto-completion and inline documentation in your favorite IDE  
- **NPM Ecosystem**: Leverage thousands of NPM packages for your infrastructure code

## Example: Deploy a Container to AWS

Here's a simple example of deploying a containerized app using TypeScript:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";

// Create an ECS cluster
const cluster = new aws.ecs.Cluster("app-cluster");

// Build and publish Docker image to ECR
const image = new awsx.ecr.Image("app-image", {
    repositoryUrl: new aws.ecr.Repository("app-repo").repositoryUrl,
    context: "./app",
    dockerfile: "./app/Dockerfile",
});

// Create a load balanced Fargate service
const service = new awsx.ecs.FargateService("app-service", {
    cluster: cluster.arn,
    taskDefinitionArgs: {
        container: {
            name: "app",
            image: image.imageUri,
            cpu: 128,
            memory: 512,
            essential: true,
            portMappings: [{
                containerPort: 80,
            }],
        },
    },
});

// Export the service URL
export const url = service.service.loadBalancers[0].containerName;
```
