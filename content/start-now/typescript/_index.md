---
title: Getting Started with Pulumi and TypeScript
meta_desc: Build and deploy cloud infrastructure using TypeScript - get type safety, IntelliSense, and the full Node.js ecosystem
layout: language-start
---

Build and deploy cloud infrastructure using TypeScript's type safety, IntelliSense, and the full Node.js ecosystem.

## Why TypeScript for Infrastructure?

<div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
    <div class="p-6 bg-blue-50 rounded-lg">
        <i class="fas fa-shield-alt text-2xl text-blue-600 mb-3"></i>
        <h3 class="font-semibold mb-2">Type Safety</h3>
        <p class="text-sm text-gray-700">Catch configuration errors at compile time with TypeScript's strong typing system</p>
    </div>
    <div class="p-6 bg-blue-50 rounded-lg">
        <i class="fas fa-lightbulb text-2xl text-blue-600 mb-3"></i>
        <h3 class="font-semibold mb-2">IntelliSense</h3>
        <p class="text-sm text-gray-700">Get auto-completion and inline documentation in your favorite IDE</p>
    </div>
    <div class="p-6 bg-blue-50 rounded-lg">
        <i class="fas fa-cube text-2xl text-blue-600 mb-3"></i>
        <h3 class="font-semibold mb-2">NPM Ecosystem</h3>
        <p class="text-sm text-gray-700">Leverage thousands of NPM packages for your infrastructure code</p>
    </div>
</div>

## Choose Your Cloud Provider

Select your cloud provider to get started with TypeScript:

<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mt-8 mb-12">
    <a href="/docs/iac/get-started/aws/" class="block p-6 bg-white rounded-lg shadow hover:shadow-lg transition-shadow border border-gray-200">
        <img src="/logos/pkg/aws.svg" alt="AWS" class="h-12 mb-4">
        <h3 class="text-lg font-semibold mb-2">AWS</h3>
        <p class="text-sm text-gray-600">Deploy to Amazon Web Services</p>
        <div class="mt-4 text-blue-600 font-medium">Get Started →</div>
    </a>
    <a href="/docs/iac/get-started/azure/" class="block p-6 bg-white rounded-lg shadow hover:shadow-lg transition-shadow border border-gray-200">
        <img src="/logos/pkg/azure.svg" alt="Azure" class="h-12 mb-4">
        <h3 class="text-lg font-semibold mb-2">Azure</h3>
        <p class="text-sm text-gray-600">Deploy to Microsoft Azure</p>
        <div class="mt-4 text-blue-600 font-medium">Get Started →</div>
    </a>
    <a href="/docs/iac/get-started/gcp/" class="block p-6 bg-white rounded-lg shadow hover:shadow-lg transition-shadow border border-gray-200">
        <img src="/logos/pkg/gcp.svg" alt="Google Cloud" class="h-12 mb-4">
        <h3 class="text-lg font-semibold mb-2">Google Cloud</h3>
        <p class="text-sm text-gray-600">Deploy to Google Cloud Platform</p>
        <div class="mt-4 text-blue-600 font-medium">Get Started →</div>
    </a>
    <a href="/docs/iac/get-started/kubernetes/" class="block p-6 bg-white rounded-lg shadow hover:shadow-lg transition-shadow border border-gray-200">
        <img src="/logos/pkg/kubernetes.svg" alt="Kubernetes" class="h-12 mb-4">
        <h3 class="text-lg font-semibold mb-2">Kubernetes</h3>
        <p class="text-sm text-gray-600">Deploy to any Kubernetes cluster</p>
        <div class="mt-4 text-blue-600 font-medium">Get Started →</div>
    </a>
</div>

## Quick Setup

Install Pulumi and set up your TypeScript environment:

```bash
# Install Pulumi
curl -fsSL https://get.pulumi.com | sh

# Create a new TypeScript project
pulumi new typescript

# Install dependencies
npm install
```

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

## TypeScript Templates

Get started quickly with these TypeScript templates:

<div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-8">
    <a href="/templates/container-service/aws/" class="flex items-center p-4 bg-gray-50 rounded-lg hover:bg-gray-100">
        <i class="fas fa-ship text-xl text-blue-500 mr-4"></i>
        <div>
            <h4 class="font-semibold">Container Service</h4>
            <p class="text-sm text-gray-600">Deploy containers with ECS or Kubernetes</p>
        </div>
    </a>
    <a href="/templates/serverless-application/aws/" class="flex items-center p-4 bg-gray-50 rounded-lg hover:bg-gray-100">
        <i class="fas fa-bolt text-xl text-yellow-500 mr-4"></i>
        <div>
            <h4 class="font-semibold">Serverless API</h4>
            <p class="text-sm text-gray-600">Build APIs with Lambda and API Gateway</p>
        </div>
    </a>
    <a href="/templates/static-website/aws/" class="flex items-center p-4 bg-gray-50 rounded-lg hover:bg-gray-100">
        <i class="fas fa-globe text-xl text-purple-500 mr-4"></i>
        <div>
            <h4 class="font-semibold">Static Website</h4>
            <p class="text-sm text-gray-600">Deploy sites with S3 and CloudFront</p>
        </div>
    </a>
    <a href="/templates/kubernetes/aws/" class="flex items-center p-4 bg-gray-50 rounded-lg hover:bg-gray-100">
        <i class="fas fa-dharmachakra text-xl text-green-500 mr-4"></i>
        <div>
            <h4 class="font-semibold">Kubernetes Cluster</h4>
            <p class="text-sm text-gray-600">Create production-ready EKS clusters</p>
        </div>
    </a>
</div>

## Learn More

- [TypeScript Language Documentation](/docs/iac/concepts/languages/typescript/)
- [Pulumi TypeScript SDK Reference](https://www.pulumi.com/registry/)
- [Video: Getting Started with TypeScript](https://www.youtube.com/watch?v=example)
- [Join our Community Slack](https://slack.pulumi.com)
