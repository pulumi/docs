---
title: "Infrastructure as Code in Any Language – Pulumi IaC"
meta_desc: Write infrastructure code using TypeScript, Python, Go, .NET, Java, or YAML. Deploy to any cloud with built-in previews and testing.
meta_image: /images/product/iac/matrix-cards.png
type: page
layout: product-page
aliases:
  - /product/iac
  - /product/pulumi-iac

hero:
  title_primary: Infrastructure as Code
  title_secondary: in any language.
  description: |
    Use the programming languages you already know to build infrastructure on AWS, Azure, Google Cloud, Kubernetes, and thousands of providers.
  cta_primary_text: Get started
  cta_primary_link: /docs/iac/get-started/
  cta_secondary_text: Book a demo
  cta_secondary_link: /contact/?form=request-a-demo
  image: /images/product/iac/matrix-cards.png
  image_alt: Pulumi infrastructure as code in any language
  anchor: hero

product_two_column:
  heading: Write infrastructure code in your favorite language
  description: |
    TypeScript/JavaScript, Python, Go, C#, Java, and YAML. Get autocomplete, type checking, and all your favorite IDE features.

    Build on AWS, Azure, Google Cloud, Kubernetes, and thousands of providers. Our open source engine is Apache 2.0 licensed and will always remain free.
  cards:
    - icon: fa-code
      title: Use real code, not DSLs
      description: |
        Write infrastructure with loops, conditionals, functions, and classes. Reuse code, catch errors at compile time, and refactor with confidence.
    - icon: fa-cloud
      title: Build on any cloud
      description: |
        Access AWS, Azure, Google Cloud, Kubernetes, and thousands of providers through a unified, consistent API. Same-day updates for new cloud features.
    - icon: fa-check
      title: Test before you ship
      description: |
        Preview changes before deploying them. Write unit tests for your infrastructure. Run integration tests against ephemeral environments.
  anchor: languages

section_header:
  title: Open source core.
  title_line_2: Pulumi Cloud built-in.
  description: |
    Get started with Pulumi Cloud for free, state management and secrets included. Our [open source engine](https://github.com/pulumi/pulumi) powers everything underneath. Scale to enterprise features when you need them, or self-host if required.
  image: /images/product/iac/pulumi-concentric-circles.svg
  image_alt: Open source core and Pulumi Cloud
  image_above: true
  anchor: open-source

counter_cards:
  anchor: stats
  cards:
    - number: "350,000+"
      label: engineers building with Pulumi
    - number: "3,700+"
      label: companies in production
    - number: "1,000+"
      label: of cloud and service providers

testimonial:
  quote: |
    Our developers needed a fast, modular, and testable platform for managing cloud infrastructure. Nothing is better than having standard programming languages for building and managing infrastructure.
  author: Austin Byers
  title: Principal Platform Engineer
  company: Panther Labs
  logo: /logos/customers/panther.svg
  anchor: testimonial

section_header_with_code:
  tag_line: Infrastructure building blocks
  title: "Ship faster with  \nreusable components"
  description: |
    Stop copy-pasting and create reusable infrastructure components that can be used in any language. Package common patterns once, use everywhere. Share via Pulumi's registry, npm, PyPI, NuGet, or any package manager.
  cta_text: Explore the registry
  cta_link: /registry/
  image: /images/product/iac/iac-code-block.svg
  image_alt: Pulumi code example
  anchor: packages

three_column:
  anchor: packages-features
  icon_style: black
  icon_layout: above
  columns:
    - icon: fa-check-square
      title: Production-ready patterns
      description: |
        Ship EKS clusters, serverless apps, or entire platforms with one line of code using well-architected components.
    - icon: fa-th-large
      title: Thousands of providers
      description: |
        Full API coverage for AWS, Azure, Google Cloud, Kubernetes, plus Cloudflare, Datadog, GitHub, and thousands more.
    - icon: fa-rocket
      title: From VMs to Kubernetes
      description: |
        Manage traditional infrastructure, containers, serverless, and Kubernetes with one tool, one workflow.

icon_grid:
  tag_line: GitOps & CI/CD Native
  title: Ship infrastructure
  title_line_2: like software
  description: |
    Infrastructure as code means infrastructure in Git. Review changes in pull requests. Run tests in CI. Ship through GitHub Actions, GitLab, Jenkins, or any CI/CD system.
  image: /images/product/iac/iac-logos.svg
  image_alt: GitOps and CI/CD tools
  anchor: gitops

three_column_cicd:
  anchor: cicd-features
  icon_style: black
  icon_layout: above
  columns:
    - icon: fa-code-branch
      title: Git-native workflow
      description: |
        Every infrastructure change is a pull request. Review, comment, approve. Full audit trail built in.
    - icon: fa-bug
      title: Catch bugs before production
      description: |
        Run [unit tests](/docs/iac/guides/testing/unit/) in milliseconds. Spin up ephemeral environments for [integration tests](/docs/iac/guides/testing/integration/). Fail fast, fix fast.
    - icon: fa-cogs
      title: Works with your CI/CD
      description: |
        Integrates with [any CI/CD system](/docs/iac/packages-and-automation/continuous-delivery/). GitHub Actions, GitLab, Jenkins, CircleCI – your choice. Or use the [Kubernetes operator](/docs/iac/packages-and-automation/continuous-delivery/pulumi-kubernetes-operator/) for GitOps.

section_header_scale:
  title: Scale confidently with Pulumi Cloud
  description: |
    Encrypted state storage, secrets management, and collaboration built in. When you scale, enterprise features like RBAC, policy enforcement, and SSO are ready. All powered by our open source engine.
  image: /images/product/iac/iac-stack-example.svg
  image_alt: Pulumi Cloud dashboard
  anchor: scale

three_column_cloud:
  anchor: cloud-features
  icon_style: black
  icon_layout: above
  columns:
    - icon: fa-lock
      title: Encrypted state management
      description: |
        Never lose state again. Automatic versioning and encryption at rest. Pulumi Cloud handles it all, or self-host with S3/Azure Blob.
    - icon: fa-key
      title: Secrets that actually work
      description: |
        No more secrets in plaintext. Automatic encryption for sensitive values. Integrate with AWS Secrets Manager, Azure Key Vault, or use [Pulumi ESC](/product/secrets-management/) for centralized secrets.
    - icon: fa-check-circle
      title: Ship with confidence
      description: |
        Review every change before it ships. Full history and audit logs. Roll back to any previous state when needed.
    - icon: fa-globe
      title: See everything, everywhere
      description: |
        Single pane of glass for all your clouds. Search across AWS, Azure, and GCP. Find that rogue EC2 instance in seconds.
    - icon: fa-plug
      title: Automation API
      description: |
        Infrastructure as code as a library. Embed Pulumi in your app. Build custom CLIs, portals, or platforms. Full programmatic control.
    - icon: fa-users
      title: Self-service infrastructure
      description: |
        Let engineers provision their own infrastructure safely. Templates, guardrails, and approval workflows. Works with Backstage or build your own.
    - icon: fa-shield-alt
      title: Enterprise SSO & RBAC
      description: |
        SAML, SCIM, GitHub, GitLab, Atlassian. Fine-grained permissions. Temporary access tokens. SOC 2 Type II compliant.
    - icon: fa-gavel
      title: Policy as code
      description: |
        Enforce security and compliance automatically. Hundreds of built-in policies or write your own. Block non-compliant infrastructure before it ships.
    - icon: fa-history
      title: Complete audit trail
      description: |
        Every action logged. Who changed what, when, and why. Export to SIEM. Compliance reports at your fingertips.

footer_cta:
  title: The Infrastructure-as-Code platform for any cloud.
  cta_primary_text: Try Pulumi for free
  cta_primary_link: /signup
  cta_secondary_text: Contact sales
  cta_secondary_link: /contact
  anchor: get-started
---
