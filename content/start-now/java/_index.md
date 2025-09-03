---
title: Getting Started with Pulumi and Java
meta_desc: Build cloud infrastructure using Java - leverage the JVM ecosystem and enterprise tooling
type: page
layout: language-start

subtitle: Build robust cloud infrastructure using Java's maturity, extensive libraries, and enterprise tooling.

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
      title: "Create a new Java project"
      code: "pulumi new java"
    - number: 3
      title: "Deploy your infrastructure"
      code: "pulumi up"

resources:
  title: Learn More
  items:
    - text: Java Language Documentation
      link: /docs/iac/concepts/languages/java/
    - text: Pulumi Java SDK Reference
      link: https://www.pulumi.com/registry/
    - text: Join our Community Slack
      link: https://slack.pulumi.com
---

## Why Java for Infrastructure?

- **Enterprise Proven**: Build infrastructure with the language trusted by enterprises worldwide
- **JVM Ecosystem**: Leverage the vast ecosystem of Java libraries and frameworks
- **IDE Support**: Full support in IntelliJ IDEA, Eclipse, and other Java IDEs