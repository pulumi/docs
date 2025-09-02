---
title: Getting Started with Pulumi YAML
meta_desc: Define cloud infrastructure using YAML - simple, declarative configuration without programming
layout: language-start
---

# Infrastructure as Code with Pulumi YAML

Define cloud infrastructure using simple, declarative YAML configuration - no programming required.

## Choose Your Cloud Provider

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

```bash
# Install Pulumi
curl -fsSL https://get.pulumi.com | sh

# Create a new YAML project
pulumi new yaml

# Deploy your infrastructure
pulumi up
```

## Example: Create an S3 Bucket

```yaml
name: my-project
runtime: yaml
description: A simple S3 bucket

resources:
  my-bucket:
    type: aws:s3:Bucket
    properties:
      website:
        indexDocument: index.html

outputs:
  bucketName: ${my-bucket.id}
  websiteUrl: ${my-bucket.websiteEndpoint}
```

## Learn More

- [YAML Language Documentation](/docs/iac/concepts/languages/yaml/)
- [Pulumi YAML Reference](https://www.pulumi.com/docs/iac/concepts/languages/yaml/)
- [Join our Community Slack](https://slack.pulumi.com)

