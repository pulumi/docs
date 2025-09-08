---
title: Platform
linktitle: Platform
capability: platform
docs_home: true
notitle: true
menu:
    platform:
        identifier: platform-home
        weight: 1
expanded_menu_ids:
    - platform-packages
    - platform-templates
meta_desc: Discover and create reusable infrastructure assets. Find packages, templates, components, and patterns to accelerate your cloud development.
meta_image: /images/docs/meta-images/docs-meta.png
h1: Platform<strong> ecosystem</strong> and assets
description: <p>Discover and create reusable infrastructure components, packages, templates, and patterns to accelerate development and ensure consistency across teams.</p>
link_buttons:
  primary:
    label: Browse Registry
    link: /registry/
  secondary:
    label: IDP Templates
    link: /docs/idp/

sections:
- type: full-width-cards
  heading: Platform Assets
  cards:
  - icon: package-blue-21-21
    heading: Packages & Providers
    description: Ready-to-use infrastructure components for AWS, Azure, Google Cloud, and 120+ providers.
    link: /registry/
  - icon: template-blue-21-21
    heading: Templates
    description: Kickstart projects with pre-built templates and scaffolding for common architectures.
    link: /docs/idp/
  - icon: layers-blue-21-21
    heading: Components
    description: Higher-level abstractions that encapsulate best practices and simplify complex deployments.
    link: /docs/iac/concepts/resources/components/
  - icon: blueprint-blue-21-21
    heading: Architecture Patterns
    description: Reference architectures and proven patterns for scalable cloud solutions.
    link: /docs/iac/using-pulumi/
- type: cards-logo-label-link
  heading: Popular Providers
  description: Most-used cloud and service providers in the Pulumi ecosystem.
  cards:
  - label: AWS
    icon: aws-40
    link: /registry/packages/aws/
  - label: Azure
    icon: azure-40
    link: /registry/packages/azure/
  - label: Google Cloud
    icon: google-cloud-40
    link: /registry/packages/gcp/
  - label: Kubernetes
    icon: kubernetes-40
    link: /registry/packages/kubernetes/
  - label: Docker
    icon: docker-40
    link: /registry/packages/docker/
  - label: Terraform
    icon: terraform-40
    link: /registry/packages/terraform/
- type: button-cards
  heading: Platform Capabilities
  description: Tools and services to create, share, and manage reusable infrastructure assets.
  cards:
  - heading: Pulumi Registry
    description: "Discover over 120 cloud and service providers, plus thousands of community packages and components."
    link: /registry/
    primary_button_label: Browse Registry
    primary_button_link: /registry/
  - heading: Internal Developer Platform
    description: "Create templates and self-service infrastructure for your engineering teams with governance guardrails."
    link: /docs/idp/
    primary_button_label: Get Started
    primary_button_link: /docs/idp/get-started/
  - heading: Component Authoring
    description: "Build reusable infrastructure components that encapsulate your organization's best practices."
    link: /docs/iac/concepts/resources/components/
    primary_button_label: Learn More
    primary_button_link: /docs/iac/concepts/resources/components/
- type: full-width-cards
  heading: Platform Engineering
  cards:
  - icon: users-blue-21-21
    heading: Team Collaboration
    description: Share packages, templates, and components across engineering teams.
    link: /docs/pulumi-cloud/
  - icon: shield-blue-21-21
    heading: Governance & Policy
    description: Enforce organizational standards and compliance through code and templates.
    link: /docs/iac/crossguard/
  - icon: workflow-blue-21-21
    heading: Automation & CI/CD
    description: Integrate reusable assets into your deployment pipelines and workflows.
    link: /docs/iac/using-pulumi/continuous-delivery/
  - icon: chart-blue-21-21
    heading: Usage & Analytics
    description: Track adoption and usage of your platform assets across the organization.
    link: /docs/insights/
- type: cards-logo-label-link
  heading: Popular Templates
  description: Get started quickly with proven infrastructure patterns and architectures.
  cards:
  - label: Static Website
    icon: web-40
    link: /templates/static-website/
  - label: Serverless
    icon: lambda-40
    link: /templates/serverless/
  - label: Container Service
    icon: container-40
    link: /templates/container-service/
  - label: Kubernetes App
    icon: kubernetes-40
    link: /templates/kubernetes-application/
- type: flat
  heading: Ready to build your platform?
  description: <p>Start by exploring the <a href="/registry/">Registry</a>, create your first <a href="/docs/idp/">IDP template</a>, or learn about <a href="/docs/iac/concepts/resources/components/">component authoring</a>. Need help? Join us on <a href="https://slack.pulumi.com" target="_blank">Slack</a> or <a href="/support/">contact support</a>.</p>
---