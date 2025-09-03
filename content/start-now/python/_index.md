---
title: Getting Started with Pulumi and Python
meta_desc: Build cloud infrastructure using Python - leverage familiar syntax, rich libraries, and powerful tooling
type: page
layout: language-start

subtitle: Build and deploy cloud infrastructure using Python's simplicity, extensive libraries, and powerful ecosystem.

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
      title: "Create a new Python project"
      code: "pulumi new python"
    - number: 3
      title: "Deploy your infrastructure"
      code: "pulumi up"

resources:
  title: Learn More
  items:
    - text: Python Language Documentation
      link: /docs/iac/concepts/languages/python/
    - text: Pulumi Python SDK Reference
      link: https://www.pulumi.com/registry/
    - text: Join our Community Slack
      link: https://slack.pulumi.com
---

## Why Python for Infrastructure?

- **Simple Syntax**: Write clean, readable infrastructure code with Python's elegant syntax
- **Rich Libraries**: Access thousands of packages from PyPI for any infrastructure need
- **Huge Community**: Join millions of Python developers building infrastructure

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