---
title: Getting Started with Pulumi and Java
meta_desc: Build cloud infrastructure using Java - leverage the JVM ecosystem and enterprise tooling
layout: language-start
---

# Infrastructure as Code with Java

Build robust cloud infrastructure using Java's maturity, extensive libraries, and enterprise tooling.

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

# Create a new Java project
pulumi new java

# Run your program
pulumi up
```

## Learn More

- [Java Language Documentation](/docs/iac/concepts/languages/java/)
- [Pulumi Java SDK Reference](https://www.pulumi.com/registry/)
- [Join our Community Slack](https://slack.pulumi.com)

