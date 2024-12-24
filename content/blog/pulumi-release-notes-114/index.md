---
title: "The Past 6 Months of Pulumi Releases"
date: 2024-12-23T13:35:41-08:00
draft: false
meta_desc: Explore Pulumi's major releases from July to December 2024, featuring Infrastructure as Code improvements, ESC enhancements, and AI innovations.
meta_image: meta.png
authors:
  - meagan-cojocar
tags:
  - releases
social:
  twitter: "🚀 From IaC enhancements to expanded ESC capabilities, Pulumi Insights 2.0 and key AI innovations - see what's new in Pulumi since July →"
  linkedin: "From Infrastructure as Code (IaC) enhancements to expanded Environment as Code (ESC) capabilities, the launch of Pulumi Insights 2.0 and key AI innovations, here's what's new in Pulumi since July:

Key highlights include:
• Pulumi ESC General Availability
• Pulumi Insights 2.0 with Resource Explorer
• Enhanced Kubernetes support with Auto Mode & Operator 2.0
• Visual Studio Code Extension

Check out all the new features empowering teams to build better cloud infrastructure."
---

As we wrap up 2024, let's look back at the significant features and improvements Pulumi has delivered in the last half of the year. Some key highlights:

• Pulumi ESC General Availability
• Pulumi Insights 2.0 with Resource Explorer
• Enhanced Kubernetes support
• Pulumi Visual Studio Code Extension

<!--more-->

## Pulumi Infrastructure as Code

### Kubernetes Enhancements

- **[Pulumi Kubernetes Operator 2.0](https://www.pulumi.com/blog/pulumi-kubernetes-operator-2-0/)**  
  Major update introducing a horizontally scalable architecture, enhanced security features, and improved customization for the Pulumi Kubernetes Operator.
- **[EKS Auto Mode](https://www.pulumi.com/blog/aws-eks-auto-mode/)**  
  A groundbreaking feature that simplifies EKS cluster management by automatically handling compute, storage, and networking configurations based on AWS’s operational expertise.
- **[Pulumi EKS V3 Release](https://www.pulumi.com/blog/eks-v3-release/)**  
  Update introducing support for Amazon Linux 2023, Access Entries for IAM integration, EKS managed addons, and enhanced security features.
- **[Improved Kubernetes Await Logic](https://www.pulumi.com/blog/improved-kubernetes-await-logic/)**  
  Better resource dependency tracking, improved error reporting, faster deletions with propagation policies, and custom readiness criteria support.

### Provider Updates

- **[AWS Cloud Control Provider GA](https://www.pulumi.com/blog/aws-cloud-control-provider-ga/)**  
  Native AWS API support with day-zero coverage for new AWS features and improved consistency in resource management.
- **[Azure v6 Release](https://www.pulumi.com/blog/azure-v6-release/)**  
  Major update ensuring compatibility with the latest Azure services, improved error messages, and new resource types.
- **[Google Cloud Provider v8.0.0](https://www.pulumi.com/blog/gcp-v8-release/)**  
  Comprehensive support for new Google Cloud services and improved resource management capabilities..
- **[AWS CDK On Pulumi 1.0](https://www.pulumi.com/blog/aws-cdk-on-pulumi-1.0/)**  
  Expanded compatibility with AWS CDK features and construct hub integration, allowing developers to continue using familiar AWS CDK patterns within Pulumi.
- **[Use Any Terraform Provider](https://www.pulumi.com/blog/terraform-providers-preview/)**  
  Automatic generation of Pulumi providers from any Terraform provider, dramatically expanding the ecosystem of available resources.

### Core Platform Features

- **[Import Improvements](https://www.pulumi.com/blog/import-improvements/)**  
  Simplify bringing existing cloud resources under Pulumi management.
- **[Pulumi Visual Studio Code Extension](https://www.pulumi.com/blog/pulumi-vscode-extension/)**  
  Enhanced debugging in the IDE, Pulumi YAML support, and ESC management within VS Code.
- **[Pulumi Docker Image Improvements](https://www.pulumi.com/blog/docker-containers/)**  
  Versioned images with pre-installed tools for Python, Node.js, and .NET. Pulumi Deployments now supports setting the version of the Node.js and Python runtimes used in the Deployment environment.
- **DependsOn for Provider Functions**  
  Manage explicit dependencies between provider functions for more accurate execution in complex deployments.

---

## Pulumi Environments, Secrets and Configuration (Pulumi ESC)

### General Availability & Key Enhancements

- **[ESC General Availability](https://www.pulumi.com/blog/pulumi-esc-ga/)**  
  GA of Pulumi ESC -redefining secrets management with features like dynamic credentials, hierarchical environments, a secrets broker with external stores like AWS Secrets Manager, and Kubernetes operators for runtime integration.
- **[ESC Projects & Environment Tags](https://www.pulumi.com/blog/esc-projects-environment-tags-launch/)**  
  Organize secrets and configurations at scale with new grouping capabilities.
- **[ESC Webhooks](https://www.pulumi.com/blog/esc-webhooks-launch/)**  
  Real-time notifications and automated actions based on environment changes.

### Deployment Improvements

- **[Dependency Caching](https://www.pulumi.com/blog/announcing-dependency-caching-deployments/)**  
  Speed up deployments by up to 80% by caching dependencies between runs, with support for npm, pip, and go modules.
- **[Kubernetes-native Agent](https://www.pulumi.com/blog/customer-managed-agents-kubernetes/)**  
  Purpose-built agent for Kubernetes environments, enabling self-hosted deployment agents within your Kubernetes clusters without requiring Docker in Docker or privileged execution.

---

## Pulumi AI and Insights

### Pulumi Insights 2.0

- **[Resource Explorer](https://www.pulumi.com/blog/insights-resources-v2/)**  
  Enhanced visual interface for exploring cloud resources with new features like customizable columns, nested grouping capabilities, advanced filtering, and shareable saved views across your organization.
- **[Account Discovery Preview](https://www.pulumi.com/blog/insights-cloud-account-discovery/)**  
  New capability to discover and manage all cloud resources regardless of how they were created, with AI-powered search and comprehensive resource visibility across your infrastructure.

### Pulumi Pulumi Copilot Enhancements

- **[REST API Integration](https://www.pulumi.com/blog/pulumi-copilot-rest/)**: Enabling programmatic access to Pulumi Copilot's AI capabilities through a REST API, supporting multi-user interactions, automation of queries, and integration with workplace collaboration platforms.
- **[System Prompts](https://www.pulumi.com/blog/copilot-system-prompts/)**: New organization-level customization allowing teams to set default preferences for programming languages, cloud providers, compliance guidelines, and infrastructure standards.
- **One-Click Update Analysis**: Debug failed updates instantly with Copilot by analyzing logs and suggesting fixes directly from the update page or from the CLI.
- **[Documentation Integration](https://www.pulumi.com/blog/copilot-in-docs/)**: Integrated throughout Pulumi's website and documentation, providing contextual assistance and documentation search capabilities to help users find relevant resources and answers to their questions.

### Pulumi Cloud Console Improvements

- **[Organization-wide Policies](https://www.pulumi.com/blog/centralized-policy-violations/)**  
  New centralized Policy Violations page providing comprehensive visibility of compliance across projects, with the ability to group violations by Policy Pack, Project, Stack, and Resource, plus API access for automation.
- **[Stacks Page Redesign](https://www.pulumi.com/blog/new-stacks-page-launch/)**  
  Major redesign offering improved performance with thousands of stacks, flexible grouping up to three levels, enhanced sorting options, shareable views via URL parameters, and personalized preferences that persist between sessions.

---

That’s a wrap for July through December 2024! From major IaC updates to advanced Pulumi ESC features to the launch of Pulumi Insights 2.0 and powerful AI integrations, Pulumi continues to innovate across the cloud engineering space. Be sure to check out the linked blog posts and docs for more details on each release. Happy building!
