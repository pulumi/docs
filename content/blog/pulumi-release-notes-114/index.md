---
title: "The Past 6 Months of Pulumi Releases"
date: 2024-12-24
draft: false
meta_desc: Explore Pulumi's major releases from July to December 2024, featuring Infrastructure
  as Code improvements, ESC enhancements, and AI innovations.
meta_image: meta.png
authors:
  - meagan-cojocar
tags:
  - releases
social:
  twitter: "🚀 From IaC enhancements to expanded ESC capabilities, Pulumi Insights
    2.0 and key AI innovations - walk through the product release notes for a summary
    of what's been shipped this year"
  linkedin: "As we wrap up 2024, let's look back at the significant features and improvements
    Pulumi has delivered- from Infrastructure as Code enhancements to expanded Pulumi
    ESC capabilities to the launch of Pulumi Insights 2.0 and key AI innovations,
    here's what's new in Pulumi:\nKey highlights include: • Visual Studio Code Extension
    • Pulumi ESC General Availability • Pulumi Insights 2.0 with Resource Explorer
    • Enhanced Kubernetes support with Auto Mode & Operator 2.0\nCheck out all the
    new features empowering teams to build better cloud infrastructure."
search:
  keywords:
    - Kubernetes
    - AI
    - Infrastructure as Code
    - Visual Studio Code
---

As we wrap up 2024, let's look back at the significant features and improvements Pulumi has delivered in the last half of the year. Some key highlights:

- Pulumi Visual Studio Code Extension
- Pulumi ESC General Availability
- Pulumi Insights 2.0 with Resource Explorer
- Enhanced Kubernetes support

<!--more-->

## Pulumi Infrastructure as Code

### Kubernetes Enhancements

- **[Pulumi Kubernetes Operator 2.0](/blog/pulumi-kubernetes-operator-2-0/)**  
  Major update introducing a horizontally scalable architecture, enhanced security features, and improved customization for the Pulumi Kubernetes Operator.
- **[EKS Auto Mode](/blog/aws-eks-auto-mode/)**  
  A groundbreaking feature that simplifies EKS cluster management by automatically handling compute, storage, and networking configurations based on AWS’s operational expertise.
- **[Pulumi EKS 3.0 Release](/blog/eks-v3-release/)**  
  Update introducing support for Amazon Linux 2023, Access Entries for IAM integration, EKS managed addons, and enhanced security features.
- **[Pulumi Kubernetes Await Logic](/blog/improved-kubernetes-await-logic/)**
  Better resource dependency tracking, improved error reporting, faster deletions with propagation policies, and custom readiness criteria support.

### Provider Updates

- **[Use Any Terraform Provider](/blog/any-terraform-provider/)**
  Automatic generation of Pulumi providers from any Terraform provider, dramatically expanding the ecosystem of available resources.
- **[AWS CDK On Pulumi 1.0](/blog/aws-cdk-on-pulumi-1.0/)**
  Expanded compatibility with AWS CDK features and construct hub integration, allowing developers to continue using familiar AWS CDK patterns within Pulumi.
- **[Azure v6 Release](/blog/azure-v6-release/)**  
  Major update ensuring compatibility with the latest Azure services, improved error messages, and new resource types.
- **[Google Cloud Provider v8.0.0](/blog/gcp-v8-release/)**
  Comprehensive support for new Google Cloud services and improved resource management capabilities.
- **[AWS Cloud Control Provider GA](/blog/pulumi-aws-cloudcontrol-provider/)**
  Native AWS API support with day-zero coverage for new AWS features and improved consistency in resource management.

### Core Platform Features

- **[Pulumi Visual Studio Code Extension](/blog/pulumi-vscode-extension/)**  
  Enhanced IaC debugging in the IDE, Pulumi YAML support, and ESC management within VS Code.
- **[Pulumi Docker Image Improvements](/blog/docker-containers/)**  
  Versioned images with pre-installed tools for Python, Node.js, and .NET. Pulumi Deployments now supports setting the version of the Node.js and Python runtimes used in the Deployment environment.
- **[Python UV Support](/blog/python-uv-toolchain/)**  
  Built-in support for uv, an extremely fast Python package manager that speeds up dependency installation by up to 100x compared to traditional tools.
- **DependsOn for Provider Functions**  
  Manage explicit dependencies between provider functions for more accurate execution in complex deployments.

---

## Pulumi Environments, Secrets and Configuration (Pulumi ESC)

### General Availability & Key Enhancements

- **[ESC General Availability](/blog/pulumi-esc-ga/)**  
  GA of Pulumi ESC - redefining secrets management with features like dynamic credentials, hierarchical environments, a secrets broker with external stores like AWS Secrets Manager, and Kubernetes operators for runtime integration.
- **[ESC Projects & Environment Tags](/blog/esc-projects-environment-tags-launch/)**  
  Organize secrets and configurations at scale with new grouping capabilities.
- **[ESC Webhooks](/blog/esc-webhooks-launch/)**  
  Real-time notifications and automated actions based on environment changes.
- **[AWS Parameter Store Integration](/blog/pulumi-esc-aws-parameter-store-support/)**  
  Native integration with AWS Systems Manager Parameter Store for seamless import of parameters and secrets into ESC environments.
- **[Environment Import Discovery](/blog/esc-imports-discoverability/)**  
  Enhanced visibility into environment dependencies with new features to track downstream usage, version tags, and impact analysis for configuration changes.

### Deployment Improvements

- **[Dependency Caching](/blog/announcing-dependency-caching-deployments/)**  
  Speed up deployments by up to 80% by caching dependencies between runs, with support for npm, pip, and go modules.
- **[Kubernetes-native Agent](/blog/customer-managed-agents-kubernetes/)**  
  Purpose-built agent for Kubernetes environments, enabling self-hosted deployment agents within your Kubernetes clusters without requiring Docker in Docker or privileged execution.

---

## Pulumi AI and Insights

### Pulumi Insights 2.0

- **[Resource Explorer](/blog/insights-resources-v2/)**  
  Enhanced visual interface for exploring cloud resources with new features like customizable columns, nested grouping capabilities, advanced filtering, and shareable saved views across your organization.
- **[Account Discovery Preview](/blog/insights-cloud-account-discovery/)**  
  New capability to discover and manage all cloud resources regardless of how they were created, with AI-powered search and comprehensive resource visibility across your infrastructure.

### Pulumi Copilot Enhancements

- **[REST API Integration](/blog/pulumi-copilot-rest/)**: Enabling programmatic access to Pulumi Copilot's AI capabilities through a REST API, supporting multi-user interactions, automation of queries, and integration with workplace collaboration platforms.
- **[System Prompts](/blog/copilot-system-prompts/)**: New organization-level customization allowing teams to set default preferences for programming languages, cloud providers, compliance guidelines, and infrastructure standards.
- **One-Click Update Analysis**: Debug failed updates instantly with Copilot by analyzing logs and suggesting fixes directly from the update page or from the CLI.
- **[Documentation Integration](/blog/copilot-in-docs/)**: Integrated throughout Pulumi's website and documentation, providing contextual assistance and documentation search capabilities to help users find relevant resources and answers to their questions.

### Pulumi Cloud Console Improvements

- **[Organization-wide Policies](/blog/centralized-policy-violations/)**
  New centralized Policy Violations page providing comprehensive visibility of compliance across projects, with the ability to group violations by Policy Pack, Project, Stack, and Resource, plus API access for automation.
- **[Stacks Page Redesign](/blog/new-stacks-page-launch/)**
  Major redesign offering improved performance with thousands of stacks, flexible grouping up to three levels, enhanced sorting options, shareable views via URL parameters, and personalized preferences that persist between sessions.

---

That’s a wrap for July through December 2024! From major IaC updates to advanced Pulumi ESC features to the launch of Pulumi Insights 2.0 and powerful AI integrations, Pulumi continues to innovate across the cloud engineering space. Be sure to check out the linked blog posts and docs for more details on each release. Happy building!
