---
title: Unified Platform for Infrastructure Teams – Pulumi
meta_desc: Build, deploy, and manage cloud infrastructure faster. Write code in any language, automate with AI, and enforce governance at scale.
meta_image: /images/product/overview/overview-meta.png
type: page
layout: product-page

sections:
  - type: product_hero
    title_primary: The unified platform
    title_secondary: for infrastructure teams.
    description: |
      Infrastructure as code with modern languages, centralized secrets and governance, and AI built for infrastructure — all in one platform. Everything teams need to move fast and scale with confidence.
    image: /images/product/overview/overview-diagram.svg
    image_alt: Pulumi platform overview diagram
    image_max_width: 800px
    anchor: hero

  - type: product_two_column
    heading: Open source foundation, enterprise scale
    description: |
      Build infrastructure like you build software.

      Compose your infrastructure code with the languages and tools your team already uses — TypeScript, Python, Go, C#, or Java. Our Apache 2.0-licensed engine gives you a foundation to scale from small project to large organization.
    cta_text: Explore Pulumi IaC
    cta_link: /product/infrastructure-as-code/
    cards:
      - icon: ph-code
        title: Real programming languages
        description: |
          Use loops, conditionals, functions, and classes, catch errors at compile time, reuse code across projects, and refactor with confidence.
      - icon: ph-squares-four
        title: Hundreds of providers
        description: |
          Full API coverage for all major clouds: AWS, Azure, Google Cloud, and Kubernetes — plus service providers like Cloudflare, Datadog, GitHub.
      - icon: ph-eye
        title: Test before you ship
        description: |
          Write unit tests for your infra code, integration tests for pre-prod environments, smoke tests for releases — all with industry standard tools.
    anchor: languages

  - type: section_header_with_image
    tag_line: Infrastructure AI
    title: Meet Neo, your AI platform engineer
    description: |
      The industry's first AI agent purpose-built for infrastructure. Neo handles complex tasks, debugs deployments, and generates code for new and existing cloud resources.
    cta_text: Meet Pulumi Neo
    cta_link: /product/neo/
    image: /images/product/overview/overview-neo.svg
    image_alt: Pulumi Neo AI assistant
    cards:
      - icon: ph-gear-six
        title: End-to-end automation
        description: |
          Describe what you need in plain English. Neo breaks it into steps, makes a plan, executes the changes, and keeps everything compliant.
      - icon: ph-lightbulb
        title: Instant cloud insights
        description: |
          Ask questions, get answers. Identify cost savings, failure patterns, and compliance violations with an AI agent that understands your infrastructure.
      - icon: ph-shield
        title: Enterprise controls
        description: |
          Neo respects your RBAC roles and policies, and human-in-the-loop approvals keep you in control — with full audit trails from prompt to deployment.
    anchor: neo

  - type: section_header
    tag_line: Centralized secrets & configuration
    title: One interface for all your secrets and config
    description: |
      Pulumi ESC brings secrets and configuration from every major vault and cloud provider into a single interface. Use it with Pulumi IaC or on its own.
    cta_text: Explore Pulumi ESC
    cta_link: /product/secrets-management/
    image: /images/product/overview/overview-esc.svg
    image_alt: Pulumi ESC centralizing secrets from multiple providers
    cards:
      - icon: ph-key
        title: Eliminate secrets sprawl
        description: |
          Fetch secret values from any supported store with a single Pulumi Cloud access token. No more juggling multiple credentials manually.
      - icon: ph-hourglass
        title: Dynamic credentials
        description: |
          Generate short-lived credentials with OpenID Connect (OIDC). Credentials are automatically revoked when their leases expire.
      - icon: ph-globe
        title: Meets you where you are
        description: |
          Use it at the command line, in app code, or in CI/CD pipelines. Our CLI, APIs, SDKs, and Kubernetes operator ensure your config is always accessible.
    anchor: secrets

  - type: section_header_with_image
    tag_line: Insights & governance
    title: See everything, control everything
    description: |
      Search across all clouds from a single pane of glass in Pulumi Cloud. Enforce policies automatically, track compliance, and get AI-powered insights. Know exactly what's running where and why.
    cta_text: Explore Pulumi Insights & Governance
    cta_link: /product/pulumi-insights/
    image: /images/product/overview/overview-governance.svg
    image_alt: Pulumi Insights resource search across clouds
    cards:
      - icon: ph-hard-drives
        title: Multi-cloud visibility
        description: |
          Run resource queries across AWS, Azure, and Google Cloud with AI-powered insights. Find what you're looking for in seconds.
      - icon: ph-gavel
        title: Policy as code
        description: |
          Enforce security and compliance rules automatically with over 150 built-in policies — or write your own in your language of choice.
      - icon: ph-file-text
        title: Complete audit trail
        description: |
          Track every change, every action, and every user. Export to security and event management systems (SIEMs) for compliance reports.
    anchor: insights

  - type: section_header
    tag_line: Internal developer platform
    title: Enable self-service infrastructure at scale
    description: |
      Give your engineers the ability to provision infrastructure through templates, components, and developer portals, while platform teams maintain control through guardrails and governance.
    cta_text: Explore Pulumi IDP
    cta_link: /product/internal-developer-platforms/
    image: /images/product/overview/overview-idp.svg
    image_alt: Internal developer platform dashboard
    cards:
      - icon: ph-cube
        title: Golden paths
        description: |
          Platform engineers define reusable components and templates once, and every team gets proven, compliant patterns out of the box.
      - icon: ph-sliders-horizontal
        title: Self-service options
        description: |
          Code, low-code YAML, or no-code portals. Engineers can work the way they prefer with consistent governance.
      - icon: ph-tree-structure
        title: Day-two operations
        description: |
          Drift detection, dependency management, and enterprise RBAC give you visibility and control across the full infrastructure lifecycle.
    anchor: idp

  - type: two_column
    anchor: get-started
    highlight_first_card: true
    columns:
      - title: Get started in 5 minutes
        description: |
          Deploy your first infrastructure with Pulumi. Choose your language, pick your cloud, ship your code.
        cta_primary_text: Start Free
        cta_primary_link: https://app.pulumi.com/signup
        cta_text: Book a Demo
        cta_link: /contact/?form=request-a-demo
      - title: Migrating to Pulumi?
        description: |
          Our tools can help you migrate your code and resource state from Terraform, AWS CloudFormation, Azure Resource Manager, and others to Pulumi. Use Neo to make the process even easier.
        cta_primary_text: Migrate from Terraform
        cta_primary_link: /docs/iac/adopting-pulumi/migrating-to-pulumi/from-terraform/
        cta_text: Explore Converters
        cta_link: /docs/iac/adopting-pulumi/converters/
---
