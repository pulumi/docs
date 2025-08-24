---
title: Platform Overview
meta_desc: The complete infrastructure as code platform. Write in any language, deploy to any cloud, with enterprise-grade security and collaboration.
type: page
layout: product

heading: The Pulumi Platform
subheading: |
    Everything you need to manage infrastructure as code at scale.<br><br>
    Start with our open source engine. Add Pulumi Cloud for team collaboration, security, and compliance.

overview:
    title: Two Ways to Use Pulumi
    description: |
        **Open Source (Free Forever)**: Use the Pulumi CLI and SDK to write and deploy infrastructure as code. Manage state yourself with any backend (local files, S3, Azure Blob, etc.).<br><br>
        **Pulumi Cloud (Free for Individuals, Paid for Teams)**: Everything in open source PLUS managed state storage, secrets management, team collaboration, policy enforcement, and enterprise features.

core_components:
    title: Core Components
    items:
        - title: "Pulumi IaC Engine"
          badge: "Open Source"
          sub_title: "Write infrastructure in any programming language"
          description: |
            The heart of Pulumi. Write infrastructure as code in TypeScript, Python, Go, C#, Java, or YAML. Deploy to AWS, Azure, Google Cloud, Kubernetes, and thousands of providers. Always free and open source.
          features:
              - title: Real Programming Languages
                description: Use loops, conditionals, functions, classes, and packages. Full IDE support with autocomplete and type checking.
                icon: code
              - title: Any Cloud Provider
                description: Single workflow for AWS, Azure, Google Cloud, Kubernetes, and thousands more through our provider ecosystem.
                icon: global
              - title: Test Like Software
                description: Unit test your infrastructure. Preview changes before deploying. Catch errors at compile time, not runtime.
                icon: check
          button:
            text: "Learn more about Pulumi IaC"
            link: "/product/infrastructure-as-code/"

        - title: "Pulumi Cloud"
          badge: "Managed Service"
          sub_title: "Everything you need for teams and enterprises"
          description: |
            Fully managed service that builds on the open source engine. Secure state storage, secrets management, team collaboration, policy enforcement, and more. Free for individuals, with team and enterprise plans available.
          features:
              - title: Managed State & Secrets
                description: Encrypted, versioned state storage with built-in secrets management. No more S3 buckets or Terraform Cloud.
                icon: lock
              - title: Team Collaboration
                description: RBAC, audit logs, concurrent deployments, and stack permissions. Work together without stepping on toes.
                icon: users
              - title: Enterprise Ready
                description: SAML SSO, SCIM, SOC2 compliance, self-hosting options, and premium support.
                icon: building
          button:
            text: "Start free with Pulumi Cloud"
            link: "https://app.pulumi.com/signup"

platform_features:
    title: Platform Features
    subtitle: Available with Pulumi Cloud
    items:
        - title: "Secrets & Configuration"
          description: "Never hardcode secrets again. Centralize all secrets and config with Pulumi ESC."
          link: "/product/secrets-management/"
          icon: key
        - title: "Policy & Governance"
          description: "Enforce security and compliance rules automatically with CrossGuard policies."
          link: "/crossguard/"
          icon: shield
        - title: "Cloud Intelligence"
          description: "AI-powered insights, cost analysis, and recommendations for your infrastructure."
          link: "/product/pulumi-insights/"
          icon: brain
        - title: "Internal Developer Platform"
          description: "Enable self-service infrastructure with golden paths and guardrails."
          link: "/product/internal-developer-platforms/"
          icon: cubes

comparison:
    title: Open Source vs Pulumi Cloud
    headers:
        - "Feature"
        - "Open Source"
        - "Pulumi Cloud"
    rows:
        - ["Write infrastructure as code", "✓", "✓"]
        - ["Deploy to any cloud", "✓", "✓"]
        - ["Use any programming language", "✓", "✓"]
        - ["State management", "Self-managed", "Fully managed"]
        - ["Secrets encryption", "Manual", "Automatic"]
        - ["Team collaboration", "Git-based", "Built-in RBAC"]
        - ["Audit logs", "—", "✓"]
        - ["Policy enforcement", "—", "✓"]
        - ["CI/CD integrations", "Basic", "Advanced"]
        - ["Support", "Community", "Premium available"]
        - ["Price", "Free forever", "Free for individuals"]

getting_started:
    title: Get Started in Minutes
    items:
        - title: Open Source
          description: Install the CLI and start deploying
          cta_text: Download CLI
          cta_link: /docs/iac/download-install/
        - title: Pulumi Cloud
          description: Sign up for free and get full platform access
          cta_text: Start for Free
          cta_link: https://app.pulumi.com/signup

---