---
title: Platform Overview
meta_desc: The complete infrastructure as code platform. Write in any language, deploy to any cloud, with enterprise-grade security and collaboration.
type: page
layout: product

heading: The Pulumi Platform
subheading: |
    The complete infrastructure as code platform for teams.<br><br>
    Open source at the core. Pulumi Cloud for collaboration, security, and scale.

overview:
    title: Open Source IaC + Managed Platform = Success at Scale
    description: |
        **Pulumi IaC** is our open source engine that lets you write infrastructure as code in any programming language. It's free forever and works with any state backend (local files, S3, Azure Blob, etc.).
        
        **Pulumi Cloud** is the easiest way to use Pulumi in a team. It provides managed state storage, secrets encryption, team collaboration, policy enforcement, and enterprise features. Free for individuals, with team plans starting at $1 per resource.
        
        Think of it like Git (open source) vs GitHub (managed service) - you can use Git alone, but GitHub makes collaboration much easier.

why_pulumi_cloud:
    title: Why Teams Choose Pulumi Cloud
    items:
        - title: "It Just Works"
          description: "No DIY backend to manage. No S3 buckets. No state file corruption. Pulumi Cloud handles it all."
          
        - title: "Secure by Default"
          description: "Encrypted state, encrypted secrets, RBAC, audit logs. Pass compliance audits without the hassle."
          
        - title: "Built for Collaboration"
          description: "See who changed what, when. Review infrastructure changes in PRs. Work together without conflicts."
          
        - title: "Scale Without Limits"
          description: "BMW uses Pulumi Cloud with 11,000+ developers. Our architecture scales with your team."

platform_capabilities:
    title: Platform Capabilities
    subtitle: Available with Pulumi Cloud
    items:
        - title: "Infrastructure as Code"
          icon: code
          description: "The foundation. Write infrastructure in real programming languages. Always open source and free."
          link: "/product/infrastructure-as-code/"
          
        - title: "AI-Powered IaC"
          icon: bot
          description: "Generate infrastructure code with AI. Includes Pulumi AI, Copilot, and Neo agent."
          link: "/product/pulumi-ai/"
          
        - title: "Secrets & Configuration"
          icon: key
          description: "Stop hardcoding secrets. Centralize all configuration with Pulumi ESC. Works with any secrets store."
          link: "/product/secrets-management/"
          
        - title: "Insights & Governance"
          icon: shield
          description: "CSPM, policy as code, asset inventory, and compliance automation."
          link: "/product/pulumi-insights/"
          
        - title: "Internal Developer Platform"
          icon: buildings
          description: "Enable self-service infrastructure. Define golden paths and let developers provision safely."
          link: "/product/internal-developer-platforms/"

customer_proof:
    title: Teams Succeeding with Pulumi
    items:
        - logo: bmw
          stat: "11,000+ developers"
          description: "Built a scalable cloud platform for hybrid environments"
          
        - logo: snowflake
          stat: "3x faster deployments"
          description: "Multi-cloud Kubernetes platform across regions"
          
        - logo: atlassian
          stat: "50% less maintenance"
          description: "Reduced infrastructure management overhead"

getting_started:
    title: Getting started

    get_started:
        title: Get started now
        description: |
            Deploy your first app in just five minutes. Follow our tutorials for AWS, Azure, Google Cloud, Kubernetes, and more.
        cta_text: Get Started

    migrate:
        title: Migrating from other tools
        description: |
            Transition from existing infrastructure tools or continue using both. Pulumi has converter tools for Terraform, AWS CloudFormation, Azure Resource Manager, and Kubernetes.
        cta_text: Explore Converter Tools
---