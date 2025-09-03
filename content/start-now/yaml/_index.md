---
title: Getting Started with Pulumi YAML
meta_desc: Define cloud infrastructure using YAML - simple, declarative configuration without programming
type: page
layout: language-start

subtitle: Define cloud infrastructure using simple, declarative YAML configuration - no programming required.

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
      title: "Create a new YAML project"
      code: "pulumi new yaml"
    - number: 3
      title: "Deploy your infrastructure"
      code: "pulumi up"

resources:
  title: Learn More
  items:
    - text: YAML Language Documentation
      link: /docs/iac/concepts/languages/yaml/
    - text: Pulumi YAML Reference
      link: https://www.pulumi.com/docs/iac/concepts/languages/yaml/
    - text: Join our Community Slack
      link: https://slack.pulumi.com
---

## Why YAML for Infrastructure?

- **No Programming Required**: Define infrastructure with simple, declarative YAML syntax
- **Easy to Learn**: Get started immediately if you're familiar with YAML configuration
- **Still Powerful**: Access the full power of Pulumi's resource model and providers

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