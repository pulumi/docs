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

quick_comparison:
    title: What You Get
    columns:
        - title: "Open Source IaC"
          badge: "Always Free"
          items:
            - "Write infrastructure in TypeScript, Python, Go, C#, Java, YAML"
            - "Deploy to AWS, Azure, GCP, Kubernetes, 1000s of providers"
            - "Preview changes before deploying"
            - "Unit test your infrastructure"
            - "Self-manage state (S3, Azure Blob, etc.)"
            - "Community support"
        - title: "With Pulumi Cloud"
          badge: "Free for Individuals"
          items:
            - "Everything in open source, plus..."
            - "Managed, encrypted state storage"
            - "Automatic secrets encryption"
            - "Team collaboration with RBAC"
            - "Full audit logs and history"
            - "Policy enforcement (CrossGuard)"
            - "AI assistant (Pulumi Copilot)"
            - "CI/CD integrations"
            - "SAML SSO for enterprises"
            - "Premium support available"

platform_capabilities:
    title: Platform Capabilities
    subtitle: Build on top of the core IaC engine
    items:
        - title: "Infrastructure as Code"
          icon: code
          description: "The foundation. Write infrastructure in real programming languages. Always open source and free."
          link: "/product/infrastructure-as-code/"
          
        - title: "Secrets & Configuration"
          icon: key
          description: "Stop hardcoding secrets. Centralize all configuration with Pulumi ESC. Works with any secrets store."
          link: "/product/secrets-management/"
          
        - title: "Policy & Governance"
          icon: shield
          description: "Enforce security and compliance automatically. Write policies in code with CrossGuard."
          link: "/crossguard/"
          
        - title: "Cloud Intelligence"
          icon: brain
          description: "AI-powered insights, recommendations, and code assistance. Understand and optimize your cloud."
          link: "/product/pulumi-insights/"
          
        - title: "Internal Developer Platform"
          icon: cubes
          description: "Enable self-service infrastructure. Define golden paths and let developers provision safely."
          link: "/product/internal-developer-platforms/"

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
    title: Start Building Today
    cta_primary:
        text: "Sign Up for Pulumi Cloud"
        description: "Free for individuals, full platform access"
        link: "https://app.pulumi.com/signup"
    cta_secondary:
        text: "Download Open Source CLI"
        description: "Start with self-managed state"
        link: "/docs/iac/download-install/"
    learn_more:
        text: "Compare open source vs Pulumi Cloud in detail →"
        link: "/docs/pulumi-cloud/get-started/what-is-it/"

---