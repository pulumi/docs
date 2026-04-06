---
title: Documentation
linktitle: Docs
meta_desc: Learn how to create, deploy, and manage infrastructure on any cloud using Pulumi's open source infrastructure as code SDK.
meta_image: /images/docs/meta-images/docs-meta.png
aliases:
- /docs/reference/
layout: main-home
notitle: true
docs_home: true
nobreadcrumb: true
h1: Pulumi Docs
description: <p>Pulumi is an <a href="https://github.com/pulumi/pulumi" target="_blank">open source</a> platform for building, deploying, and managing cloud infrastructure using your favorite <a href="/docs/iac/languages-sdks/">programming languages</a>. Manage infrastructure, secrets, and configuration with a unified workflow across any cloud.</p>
outputs:
- HTML
- markdown
- clisitemap
- cliconfig
cascade:
  meta_image: /images/docs/meta-images/docs-meta.png
  outputs:
  - HTML
  - markdown
link_buttons:
  primary:
    label: Get Started
    link: /docs/get-started/
sections:
- type: quick-starts
  heading: Common tasks
  cards:
  - icon: rocket
    label: Deploy your first app
    link: /docs/get-started/
  - icon: arrows-clockwise
    label: Migrate from Terraform
    link: /docs/iac/adopting-pulumi/migrating-to-pulumi/from-terraform/
  - icon: robot
    label: Use Pulumi AI
    link: /docs/ai/
- type: capability-cards
  heading: Capabilities
  cards:
  - icon: code
    heading: Infrastructure as Code
    description: Define and manage cloud infrastructure using TypeScript, Python, Go, .NET, Java, and YAML.
    link: /docs/iac/
    featured: true
  - icon: cloud-arrow-up
    heading: Deployments & Workflows
    description: Cloud-hosted deployments, drift detection, state management, and automation.
    link: /docs/deployments/
  - icon: lock-key
    heading: Secrets & Configuration
    description: Centralized secrets and configuration management with environments.
    link: /docs/esc/
  - icon: shield-check
    heading: Insights & Governance
    description: Search, compliance, and policy enforcement across your cloud infrastructure.
    link: /docs/insights/
  - icon: git-branch
    heading: Version Control
    description: Connect Pulumi with GitHub, GitLab, and Azure DevOps using Pulumi-maintained version control integrations.
    link: /docs/version-control/
  - icon: layout
    heading: Internal Developer Platform
    description: Self-service infrastructure with templates, guardrails, and developer portals.
    link: /docs/idp/
  - icon: robot
    heading: Infrastructure AI
    description: Infrastructure automation with Pulumi Neo and natural language assistance.
    link: /docs/ai/
- type: link-cards
  heading: More
  cards:
  - icon: graduation-cap
    heading: Tutorials
    description: Step-by-step guides for building real-world infrastructure.
    link: /tutorials/
  - icon: buildings
    heading: Administration
    description: Manage organizations, access, security, and self-hosting.
    link: /docs/administration/
  - icon: package
    heading: Registry
    description: Browse 150+ cloud providers and services.
    link: /registry/
  - icon: book-open-text
    heading: Reference
    description: CLI, SDK, and API reference documentation.
    link: /docs/reference/
  - icon: arrows-clockwise
    heading: Migration
    description: Migrate from Terraform, CloudFormation, and other tools.
    link: /docs/iac/guides/migration/
  - icon: lifebuoy
    heading: Support
    description: Troubleshooting guides, FAQs, and community resources.
    link: /docs/support/

---
