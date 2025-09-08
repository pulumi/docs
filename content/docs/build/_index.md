---
title: Build
linktitle: Build
capability: build
docs_home: true
notitle: true
menu:
    build:
        identifier: build-home
        weight: 1
meta_desc: Build and deploy cloud infrastructure with Pulumi. Manage stacks, environments, resources, and services for your daily engineering work.
meta_image: /images/docs/meta-images/docs-meta.png
h1: Build with Pulumi
description: <p>Everything you need for daily engineering work - creating stacks, managing environments, deploying resources, and building cloud services.</p>
link_buttons:
  primary:
    label: Get Started
    link: /docs/iac/get-started/
  secondary:
    label: Create Environment
    link: /docs/esc/get-started/

sections:
- type: full-width-cards
  heading: Core Building Blocks
  cards:
  - icon: stack-blue-21-21
    heading: Stacks
    description: Create and manage isolated deployments of your infrastructure across environments.
    link: /docs/iac/concepts/stack/
  - icon: gear-blue-21-21
    heading: Environments
    description: Configure secrets, settings, and variables across your infrastructure and applications.
    link: /docs/esc/environments/
  - icon: cube-blue-21-21
    heading: Resources
    description: Provision and manage cloud resources with infrastructure as code.
    link: /docs/iac/concepts/resources/
  - icon: layers-blue-21-21
    heading: Components
    description: Build reusable infrastructure components for consistent deployments.
    link: /docs/iac/concepts/resources/components/
- type: cards-logo-label-link
  heading: Get Started Building
  description: Jump into creating infrastructure on your preferred cloud platform.
  cards:
  - label: AWS Quick Start
    icon: aws-40
    link: /docs/iac/get-started/aws/
  - label: Azure Quick Start
    icon: azure-40
    link: /docs/iac/get-started/azure/
  - label: Google Cloud Quick Start
    icon: google-cloud-40
    link: /docs/iac/get-started/gcp/
  - label: Kubernetes Quick Start
    icon: kubernetes-40
    link: /docs/iac/get-started/kubernetes/
- type: full-width-cards
  heading: Essential Build Tasks
  cards:
  - icon: terminal-blue-21-21
    heading: Deploy Your First Stack
    description: Learn the fundamentals of creating and deploying infrastructure stacks.
    link: /docs/iac/get-started/
  - icon: key-blue-21-21
    heading: Manage Secrets & Config
    description: Securely handle configuration and secrets across environments.
    link: /docs/esc/get-started/
  - icon: cloud-blue-21-21
    heading: Connect to Cloud Services
    description: Build applications that integrate with cloud databases, storage, and APIs.
    link: /docs/iac/concepts/
  - icon: layers-blue-21-21
    heading: Organize Stacks
    description: Structure your infrastructure across development, staging, and production.
    link: /docs/pulumi-cloud/stacks/
- type: button-cards
  heading: Popular Build Workflows
  description: Common patterns for building and deploying cloud infrastructure.
  cards:
  - heading: Serverless Applications
    description: "Deploy functions, APIs, and event-driven architectures on AWS Lambda, Azure Functions, and Google Cloud Functions."
    link: /docs/iac/clouds/aws/guides/lambda/
    primary_button_label: View Examples
    primary_button_link: /docs/iac/clouds/aws/guides/lambda/
  - heading: Container Workloads
    description: "Deploy containerized applications on Kubernetes, AWS ECS, Azure Container Apps, and Google Cloud Run."
    link: /docs/iac/clouds/kubernetes/
    primary_button_label: Get Started
    primary_button_link: /docs/iac/clouds/kubernetes/get-started/
  - heading: Static Websites
    description: "Build and deploy static sites with CDNs, SSL certificates, and custom domains."
    link: /docs/iac/clouds/aws/guides/static-website/
    primary_button_label: Deploy Now
    primary_button_link: /docs/iac/clouds/aws/guides/static-website/
- type: cards-logo-label-link
  heading: Build in Your Language
  description: Use familiar programming languages for infrastructure as code.
  cards:
  - label: TypeScript/JavaScript
    icon: icon-32-32 node-color-32-32
    link: /docs/iac/languages-sdks/javascript/
  - label: Python
    icon: icon-32-32 python-color-32-32
    link: /docs/iac/languages-sdks/python/
  - label: Go
    icon: icon-32-32 go-color-32-32
    link: /docs/iac/languages-sdks/go/
  - label: .NET
    icon: icon-32-32 dotnet-color-32-32
    link: /docs/iac/languages-sdks/dotnet/
  - label: Java
    icon: icon-32-32 java-color-32-32
    link: /docs/iac/languages-sdks/java/
  - label: YAML
    icon: icon-32-32 yaml-color-32-32
    link: /docs/iac/languages-sdks/yaml/
- type: flat
  heading: Ready to build?
  description: <p>Start with our <a href="/docs/iac/get-started/">Get Started guide</a>, explore <a href="/tutorials/">tutorials</a>, or jump into <a href="/docs/esc/get-started/">environment configuration</a>. Need help? Join us on <a href="https://slack.pulumi.com" target="_blank">Slack</a> or <a href="/support/">contact support</a>.</p>
---