---
title: Getting Started with Pulumi and Go
meta_desc: Build cloud infrastructure using Go - leverage strong typing, concurrency, and performance
type: page
layout: language-start

subtitle: Build high-performance cloud infrastructure using Go's simplicity, concurrency, and strong typing.

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
      title: "Create a new Go project"
      code: "pulumi new go"
    - number: 3
      title: "Deploy your infrastructure"
      code: "pulumi up"

resources:
  title: Learn More
  items:
    - text: Go Language Documentation
      link: /docs/iac/concepts/languages/go/
    - text: Pulumi Go SDK Reference
      link: https://www.pulumi.com/registry/
    - text: Join our Community Slack
      link: https://slack.pulumi.com
---

## Why Go for Infrastructure?

- **Performance**: Build fast, efficient infrastructure automation with Go's compiled performance
- **Concurrency**: Leverage goroutines for parallel infrastructure operations
- **Type Safety**: Catch errors at compile time with Go's strong static typing
