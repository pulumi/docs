---
title: Unified Platform for Infrastructure Teams – Pulumi Platform
meta_desc: Build, deploy, and manage cloud infrastructure faster. Write code in any language, automate with AI, and enforce governance at scale.
type: page
layout: product

heading: The Unified Platform for Infrastructure Teams
subheading: |
    Ship infrastructure faster. From IaC in any programming language to AI-powered automation, Pulumi provides the complete platform that platform teams trust and engineers love.

overview:
    title: Built for the AI Era of Infrastructure
    description: |
        Modern infrastructure demands modern tools. Pulumi unifies infrastructure as code, secrets management, policy governance, and AI automation into a single platform. Start with our Apache 2.0 open source core, scale with enterprise features when you need them.

key_features_above:
    items:
        - title: "Infrastructure as Code in Any Language"
          sub_title: "Open Source Foundation, Enterprise Scale"
          description:
            Stop wrestling with DSLs. Write infrastructure in TypeScript, Python, Go, C#, Java, or YAML. Deploy to AWS, Azure, Google Cloud, Kubernetes, and [thousands of providers](/registry/). Our Apache 2.0 open source engine powers everything.
          image: "/images/product/pulumi-iac-code.png"
          button:
            text: "Explore Infrastructure as Code"
            link: "/product/infrastructure-as-code/"
          features:
              - title: Real Programming Languages
                description: |
                    Use loops, conditionals, functions, and classes. Catch errors at compile time. Reuse code across projects.
                icon: code
                color: yellow
              - title: Thousands of Providers
                description: |
                    Full API coverage for AWS, Azure, Google Cloud, plus Cloudflare, Datadog, GitHub, and thousands more.
                icon: global
                color: salmon
              - title: Test Before You Ship
                description: |
                    Write unit tests for infrastructure. Run integration tests against ephemeral environments. Ship with confidence.
                icon: eye
                color: blue

        - title: "Meet Neo, Your AI Platform Engineer"
          sub_title: "Automate Infrastructure with Built-in Governance"
          description:
            The industry's first AI agent built for infrastructure. Neo automates complex tasks end-to-end, debugs deployments instantly, and generates infrastructure code - all while respecting your policies and requiring appropriate approvals.
          image: "/images/product/pulumi-neo-tasks.png"
          button:
            text: "Meet Pulumi Neo"
            link: "/product/neo/"
          features:
              - title: End-to-End Automation
                description: |
                    Delegate complex tasks in plain English. Neo handles dependencies, executes changes, and maintains compliance.
                icon: rocketship
                color: purple
              - title: Instant Cloud Insights
                description: |
                    Ask questions, get answers. Find cost savings, debug failures, check compliance - Neo knows your infrastructure.
                icon: eye
                color: yellow
              - title: Enterprise Controls
                description: |
                    Human-in-the-loop approvals. Respects all RBAC and policies. Complete audit trail for every action.
                icon: shield
                color: salmon

key_features:
    title: Platform Capabilities
    items:
        - title: "Centralized Secrets & Configuration"
          sub_title: "One Interface for All Your Secrets"
          description: |
            Pulumi ESC centralizes secrets from every vault and cloud provider. Connect HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, 1Password, and more. Dynamic credentials via OIDC. Works with or without Pulumi IaC.
          image: "/images/product/esc-octopus-diagram.png"
          button:
            text: "Explore Secrets Management"
            link: "/product/secrets-management/"
          features:
              - title: Eliminate Secrets Sprawl
                description: |
                    Connect to any secrets store. One interface for all your secrets. No more juggling multiple vaults.
              - title: Dynamic Credentials
                description: |
                    Generate just-in-time, short-lived credentials via OIDC. Automatically revoke when leases expire.
              - title: Works Everywhere
                description: |
                    CLI, API, SDKs, Kubernetes operators. Use with any CI/CD platform, any application, any workflow.

        - title: "Complete Visibility & Governance"
          sub_title: "See Everything, Control Everything"
          description: |
            Search across all clouds from a single pane of glass. Enforce policies automatically. Track compliance. Get AI-powered insights. Know exactly what's running where and why.
          image: "/images/product/insights-resource-search.png"
          button:
            text: "Explore Insights & Governance"
            link: "/product/pulumi-insights/"
          features:
              - title: Multi-Cloud Visibility
                description: |
                    Search resources across AWS, Azure, and GCP with AI-powered insights. Find anything in seconds.
              - title: Policy as Code
                description: |
                    Enforce security and compliance automatically. 150+ built-in policies or write your own.
              - title: Complete Audit Trail
                description: |
                    Track every change, every user, every action. Export to SIEM. Compliance reports at your fingertips.

        - title: "Build Your Internal Developer Platform"
          sub_title: "Enable Self-Service Infrastructure at Scale"
          description: |
            Give engineers self-service infrastructure through templates, components, and developer portals. Platform teams maintain control through policies and governance. Ship golden paths that engineers actually want to use.
          image: "/images/product/idp-services-home.jpg"
          button:
            text: "Explore Platform Engineering"
            link: "/product/internal-developer-platforms/"
          features:
              - title: Golden Paths
                description: |
                    Create reusable components and templates. Platform engineers define patterns once, engineers use everywhere.
              - title: Self-Service Options
                description: |
                    Code, low-code YAML, or no-code portals. Engineers work how they prefer with consistent governance.
              - title: Day 2 Operations
                description: |
                    Drift detection, dependency management, enterprise RBAC. Handle the full infrastructure lifecycle.

customer_impact:
    title: Trusted by Platform Teams Everywhere
    stats:
        - metric: "350,000+"
          description: "Engineers building with Pulumi"
        - metric: "3,700+"
          description: "Companies in production"
        - metric: "75%"
          description: "Faster infrastructure delivery"
    quote:
        text: "Pulumi Neo addresses our biggest challenge of eliminating the infrastructure bottleneck that slows down our entire engineering organization. To get to market faster, we require infrastructure intelligence that understands our environment, respects our guardrails, and keeps humans in the loop so we can move faster, safely."
        author: "Richard Genthner"
        role: "Chief Information Security Officer, Boost Insurance"

enterprise_features:
    title: Enterprise-Ready from Day One
    items:
        - icon: shield
          title: Security & Compliance
          description: SAML/SCIM SSO, RBAC, audit logs, SOC 2 Type II compliant. Encrypted state and secrets.
        - icon: global
          title: Any Cloud, Any Scale
          description: AWS, Azure, Google Cloud, Kubernetes, and 160+ providers. Manage millions of resources.
        - icon: team
          title: Built for Teams
          description: Collaborate across projects. Review infrastructure changes in pull requests. Ship through CI/CD.
        - icon: lightning
          title: World-Class Support
          description: 24/7 enterprise support. Solution architects. Migration assistance. Training and workshops.

learn:
    title: Start Building Today
    items:
        - title: Get started in 5 minutes
          description: |
            Deploy your first infrastructure with Pulumi. Choose your language, pick your cloud, ship your code.
          buttons:
            - link: https://app.pulumi.com/signup
              type: primary
              action: Start Free
            - link: /contact/?form=request-a-demo
              type: secondary
              action: Book a Demo
        - title: Migrating from Terraform?
          description: |
            Keep using both or migrate completely. Import existing infrastructure, convert HCL to real code, migrate state.
          buttons:
            - link: /docs/iac/adopting-pulumi/migrating-to-pulumi/from-terraform/
              type: primary
              action: Migration Guide
            - link: /docs/iac/adopting-pulumi/converters/
              type: secondary
              action: Try Converters
---