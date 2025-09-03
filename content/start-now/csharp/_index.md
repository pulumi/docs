---
title: Getting Started with Pulumi and C#
meta_desc: Build cloud infrastructure using C# and .NET - leverage the full power of the .NET ecosystem
type: page
layout: language-start

subtitle: Build enterprise-grade cloud infrastructure using C#, .NET, and the rich ecosystem of NuGet packages.

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
      title: "Create a new C# project"
      code: "pulumi new csharp"
    - number: 3
      title: "Deploy your infrastructure"
      code: "pulumi up"

resources:
  title: Learn More
  items:
    - text: C# Language Documentation
      link: /docs/iac/concepts/languages/dotnet/
    - text: Pulumi .NET SDK Reference
      link: https://www.pulumi.com/registry/
    - text: Join our Community Slack
      link: https://slack.pulumi.com
---

## Why C# for Infrastructure?

- **Enterprise Ready**: Build infrastructure with the same language and tools used for enterprise applications
- **.NET Ecosystem**: Access thousands of NuGet packages and integrate with existing .NET libraries
- **Visual Studio Integration**: Full IDE support with IntelliSense, debugging, and refactoring tools