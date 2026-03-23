---
title: Unified Platform for Infrastructure Teams – Pulumi
meta_desc: Build, deploy, and manage cloud infrastructure faster. Write code in any language, automate with AI, and enforce governance at scale.
meta_image: /images/product/overview/overview-meta.png
type: page
layout: product-page

hero:
  title_primary: The unified platform
  title_secondary: for infrastructure teams.
  description: |
    Built for the AI Era of Infrastructure. Modern infrastructure demands modern tools. Pulumi unifies infrastructure as code, secrets management, policy governance, and AI automation into a single platform. Start with our Apache 2.0 open source core, scale with enterprise features when you need them.
  image: /images/product/overview/overview-diagram.svg
  image_alt: Pulumi platform overview diagram
  image_max_width: 780px
  anchor: hero

product_two_column:
  heading: Open source foundation, enterprise scale
  description: |
    Stop wrestling with DSLs.

    Write infrastructure in TypeScript, Python, Go, C#, Java, or YAML. Deploy to AWS, Azure, Google Cloud, Kubernetes, and thousands of providers. Our Apache 2.0 open source engine powers everything.
  cta_text: Explore Infrastructure as Code
  cta_link: /product/infrastructure-as-code/
  cards:
    - icon: fa-code
      title: Real programming languages
      description: |
        Use loops, conditionals, functions, and classes. Catch errors at compile time. Reuse code across projects.
    - icon: fa-th-large
      title: Thousands of providers
      description: |
        Full API coverage for AWS, Azure, Google Cloud, plus Cloudflare, Datadog, GitHub, and thousands more.
    - icon: fa-eye
      title: Test before you ship
      description: |
        Write unit tests for infrastructure. Run integration tests against ephemeral environments. Ship with confidence.
  anchor: languages

neo_section:
  tag_line: Infrastructure AI
  title: "Meet Neo, your AI<br>platform engineer"
  description: |
    The industry's first AI agent built for infrastructure. Neo automates complex tasks end-to-end, debugs deployments instantly, and generates infrastructure code — all while respecting your policies and requiring appropriate approvals.
  cta_text: Meet Pulumi Neo
  cta_link: /product/neo/
  image: /images/product/overview/overview-neo.svg
  image_alt: Pulumi Neo AI assistant
  cards:
    - icon: fa-cogs
      title: End-to-end automation
      description: |
        Delegate complex tasks in plain English. Neo handles dependencies, executes changes, and maintains compliance.
    - icon: fa-lightbulb
      title: Instant cloud insights
      description: |
        Ask questions, get answers. Find cost savings, debug failures, check compliance — Neo knows your infrastructure.
    - icon: fa-shield-alt
      title: Enterprise controls
      description: |
        Human-in-the-loop approvals. Respects all RBAC and policies. Complete audit trail for every action.
  anchor: neo

secrets_section:
  tag_line: "Centralized secrets & configuration"
  title: One interface for all your secrets
  description: |
    Pulumi ESC centralizes secrets from every vault and cloud provider. Connect HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, 1Password, and more. Dynamic credentials via OIDC. Works with or without Pulumi IaC.
  cta_text: Explore Secrets Management
  cta_link: /product/secrets-management/
  image: /images/product/overview/overview-esc.svg
  image_alt: Pulumi ESC centralizing secrets from multiple providers
  cards:
    - icon: fa-key
      title: Eliminate secrets sprawl
      description: |
        Connect to any secrets store. One interface for all your secrets. No more juggling multiple vaults.
    - icon: fa-hourglass-half
      title: Dynamic credentials
      description: |
        Generate just-in-time, short-lived credentials via OIDC. Automatically revoke when leases expire.
    - icon: fa-globe
      title: Works everywhere
      description: |
        CLI, API, SDKs, Kubernetes operators. Use with any CI/CD platform, any application, any workflow.
  anchor: secrets

insights_section:
  tag_line: "Insights & governance"
  title: See everything, control everything
  description: |
    Search across all clouds from a single pane of glass. Enforce policies automatically. Track compliance. Get AI-powered insights. Know exactly what's running where and why.
  cta_text: "Explore Insights & Governance"
  cta_link: /product/pulumi-insights/
  image: /images/product/overview/overview-governance.svg
  image_alt: Pulumi Insights resource search across clouds
  cards:
    - icon: fa-server
      title: Multi-cloud visibility
      description: |
        Search resources across AWS, Azure, and GCP with AI-powered insights. Find anything in seconds.
    - icon: fa-gavel
      title: Policy as code
      description: |
        Enforce security and compliance automatically. 150+ built-in policies or write your own.
    - icon: fa-file-alt
      title: Complete audit trail
      description: |
        Track every change, every user, every action. Export to SIEM. Compliance reports at your fingertips.
  anchor: insights

idp_section:
  tag_line: Internal developer platform
  title: Enable self-service infrastructure at scale
  description: |
    Give engineers self-service infrastructure through templates, components, and developer portals. Platform teams maintain control through policies and governance. Ship golden paths that engineers actually want to use.
  cta_text: Explore Platform Engineering
  cta_link: /product/internal-developer-platforms/
  image: /images/product/overview/overview-idp.svg
  image_alt: Internal developer platform dashboard
  anchor: idp

three_column_idp:
  anchor: idp-features
  icon_style: black
  icon_layout: above
  columns:
    - icon: fa-cubes
      title: Golden paths
      description: |
        Create reusable components and templates. Platform engineers define patterns once, engineers use everywhere.
    - icon: fa-sliders-h
      title: Self-service options
      description: |
        Code, low-code YAML, or no-code portals. Engineers work how they prefer with consistent governance.
    - icon: fa-sitemap
      title: Day 2 operations
      description: |
        Drift detection, dependency management, enterprise RBAC. Handle the full infrastructure lifecycle.

split_cta:
  anchor: get-started
  columns:
    - title: Get started in 5 minutes
      description: |
        Deploy your first infrastructure with Pulumi. Choose your language, pick your cloud, ship your code.
      cta_primary_text: Start Free
      cta_primary_link: https://app.pulumi.com/signup
      cta_text: Book a Demo
      cta_link: /contact/?form=request-a-demo
    - title: Migrating from Terraform?
      description: |
        Keep using both or migrate completely. Import existing infrastructure, convert HCL to real code, migrate state.
      cta_primary_text: Migration Guide
      cta_primary_link: /docs/iac/adopting-pulumi/migrating-to-pulumi/from-terraform/
      cta_text: Try Converters
      cta_link: /docs/iac/adopting-pulumi/converters/
---
