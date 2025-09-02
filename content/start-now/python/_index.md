---
title: Getting Started with Pulumi and Python
meta_desc: Build cloud infrastructure using Python - leverage familiar syntax, rich libraries, and powerful tooling
---

Build and deploy cloud infrastructure using Python's simplicity, extensive libraries, and powerful ecosystem.

## Why Python for Infrastructure?

<div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
    <div class="p-6 bg-blue-50 rounded-lg">
        <i class="fas fa-code text-2xl text-blue-600 mb-3"></i>
        <h3 class="font-semibold mb-2">Simple Syntax</h3>
        <p class="text-sm text-gray-700">Write clean, readable infrastructure code with Python's elegant syntax</p>
    </div>
    <div class="p-6 bg-blue-50 rounded-lg">
        <i class="fas fa-layer-group text-2xl text-blue-600 mb-3"></i>
        <h3 class="font-semibold mb-2">Rich Libraries</h3>
        <p class="text-sm text-gray-700">Access thousands of packages from PyPI for any infrastructure need</p>
    </div>
    <div class="p-6 bg-blue-50 rounded-lg">
        <i class="fas fa-users text-2xl text-blue-600 mb-3"></i>
        <h3 class="font-semibold mb-2">Huge Community</h3>
        <p class="text-sm text-gray-700">Join millions of Python developers building infrastructure</p>
    </div>
</div>

## Choose Your Cloud Provider

Select your cloud provider to get started with Python:

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

Install Pulumi and set up your Python environment:

```bash
# Install Pulumi
curl -fsSL https://get.pulumi.com | sh

# Create a new Python project
pulumi new python

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Example: Deploy a Web App to AWS

Here's a simple example of deploying a web application using Python:

```python
import pulumi
import pulumi_aws as aws
import pulumi_awsx as awsx

# Create an S3 bucket for static content
bucket = aws.s3.Bucket("my-bucket",
    website={
        "index_document": "index.html",
    })

# Create a CloudFront distribution
cdn = aws.cloudfront.Distribution("cdn",
    origins=[{
        "origin_id": bucket.arn,
        "domain_name": bucket.website_endpoint,
        "custom_origin_config": {
            "http_port": 80,
            "https_port": 443,
            "origin_protocol_policy": "http-only",
            "origin_ssl_protocols": ["TLSv1.2"],
        },
    }],
    enabled=True,
    default_root_object="index.html",
    default_cache_behavior={
        "allowed_methods": ["GET", "HEAD"],
        "cached_methods": ["GET", "HEAD"],
        "target_origin_id": bucket.arn,
        "viewer_protocol_policy": "redirect-to-https",
    },
    restrictions={
        "geo_restriction": {
            "restriction_type": "none",
        },
    },
    viewer_certificate={
        "cloudfront_default_certificate": True,
    })

# Export the CDN URL
pulumi.export("cdn_url", cdn.domain_name)
```

## Python Templates

Get started quickly with these Python templates:

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

- [Python Language Documentation](/docs/iac/concepts/languages/python/)
- [Pulumi Python SDK Reference](https://www.pulumi.com/registry/)
- [Video: Getting Started with Python](https://www.youtube.com/watch?v=example)
- [Join our Community Slack](https://slack.pulumi.com)
