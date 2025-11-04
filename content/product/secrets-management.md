---
title: "Centralized Configuration & Secrets Management – Pulumi ESC"
layout: secrets-management

meta_desc: Centralize secrets and configurations with Pulumi ESC. Connect any vault, eliminate secrets sprawl, secure every environment.
meta_image: "/images/product/esc-octopus-diagram.png"
aliases:
    - /esc
    - /product/esc
    - /product/pulumi-esc

heading: Secrets & Configuration
subheading: |
    Manage all your secrets and configuration at scale

overview:
    header: One interface for all your secrets
    body: |
      Pulumi ESC (Environments, Secrets, Configuration) centralizes secrets from every vault and cloud provider. No more juggling AWS Secrets Manager, HashiCorp Vault, and Azure Key Vault separately. Connect them all, manage them centrally, access them anywhere.

      - **Eliminate secrets sprawl.** Connect to any secrets store—HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, 1Password, and more. One interface for all your secrets.
      - **Secure by default.** Dynamic, short-lived credentials with OIDC. Full RBAC, versioning, and audit logging. No more plaintext secrets anywhere.
      - **Engineer-friendly access.** CLI, API, SDKs, and Kubernetes operators. Access secrets from anywhere without compromising security.
      - **Integrated with Pulumi IaC.** Native integration with Pulumi infrastructure code, or use standalone with any application or workflow.

key_benefits:
    title: Why teams choose Pulumi for secrets management
    items:
        - icon: shield
          icon_color: purple
          title: Enterprise-Grade Security
          description: |
            Dynamic credentials via OIDC replace long-lived keys. RBAC for fine-grained access control, complete audit trails. SOC 2 Type II compliant.
        - icon: layers
          icon_color: blue
          title: Composable Environments
          description: |
            Organize secrets into logical environments that inherit from each other. Share common configurations while maintaining isolation where needed.
        - icon: refresh-cw
          icon_color: salmon
          title: Version Everything
          description: |
            Every change is versioned and auditable. Roll back instantly when needed. Know exactly who changed what and when.

integrations:
    header: Connect to your entire secrets ecosystem
    description: ESC acts as a universal adapter for all your secrets stores and platforms.
    categories:
        - title: Secret Stores
          items:
            - HashiCorp Vault
            - AWS Secrets Manager
            - Azure Key Vault
            - Google Secret Manager
            - 1Password
            - Doppler
        - title: Cloud Providers
          items:
            - AWS (via OIDC)
            - Microsoft Azure
            - Google Cloud
            - Kubernetes
        - title: Developer Tools
          items:
            - GitHub Actions
            - GitLab CI
            - CircleCI
            - Jenkins
            - Terraform
            - Docker

how_it_works:
    title: Centralized secrets, distributed access
    steps:
        - number: 1
          title: Define Environments
          description: Organize secrets and configurations into logical environments. Use composition to share common settings while maintaining separation where needed.
        - number: 2
          title: Connect Sources
          description: Pull secrets from any store—Vault, AWS Secrets Manager, Azure Key Vault, and more. ESC syncs and manages them centrally.
        - number: 3
          title: Access Anywhere
          description: Consume secrets via CLI, API, SDKs, or Kubernetes operators. Every platform, every language, every workflow supported.
        - number: 4
          title: Stay Secure
          description: RBAC controls who can access what. Audit logs track every action. Dynamic credentials expire automatically.

use_cases:
    title: Trusted by platform engineering teams
    items:
        - title: Multi-Cloud Secrets Management
          description: Manage secrets across AWS, Azure, and GCP from a single interface. Perfect for Pulumi IaC or any multi-cloud application.
          icon: cloud
        - title: Secure CI/CD Pipelines
          description: Inject secrets into any CI/CD platform without storing them in pipeline configuration. Dynamic credentials that expire after use.
          icon: git-branch
        - title: Engineering Environment Setup
          description: Engineers get the exact secrets they need, when they need them. No manual configuration or insecure credential sharing.
          icon: code
        - title: Kubernetes Configuration
          description: Manage ConfigMaps and Secrets across clusters. Use the ESC Kubernetes operator for seamless integration.
          icon: kubernetes

customer_quotes:
  tetrate:
    text: |
      "With Pulumi ESC, our developers get dynamic AWS and Azure credentials on-demand. Onboarding new developers is quick and secure, with no more manually filling in .env templates."
    author: Liam White, Platform Lead
    logo: tetrate
  mysten:
    text: |
      "Pulumi ESC has been a lifesaver for us. It's nice to throw everything behind an ESC environment and eliminate one-off granting IAM permissions and other issues related to static credentials."
    author: JK Jensen, Software Engineering Team Lead
    logo: mysten-labs
  werner:
    text: |
      "We reduced our secrets management overhead by 80% while improving security. ESC's dynamic credentials mean we never have long-lived secrets sitting around."
    author: Jason Harris, Cloud Architecture Lead
    logo: werner-enterprises

features:
  - header: Dynamic Credentials
    body: Generate just-in-time, short-lived credentials via OIDC. Automatically revoke access when leases expire.
  - header: Environment Composition
    body: Build complex configurations from simple, reusable components. Inherit common settings while overriding specific values.
  - header: Full Audit Trail
    body: Track every access, every change, every user. Complete visibility into who's using what secrets and when.
  - header: Version Control
    body: Every environment change is versioned. Roll back instantly or access previous configurations when needed.
  - header: RBAC & Teams
    body: Fine-grained access controls integrated with your identity provider. SAML/SCIM support for enterprise SSO.
  - header: Extensible Plugin Model
    body: Support for custom secret stores through our plugin architecture. Integrate with any system.

pricing:
    title: Simple, transparent pricing
    description: ESC is included with Pulumi Cloud subscriptions. Pay only for what you use.
    tiers:
        - name: Individual
          price: Free
          description: For individual developers
          features:
            - Unlimited environments
            - 1,000 environment reads/month
            - Community support
        - name: Team
          price: Scales with usage
          description: For growing teams
          features:
            - Everything in Individual
            - Unlimited environment reads
            - RBAC and audit logging
            - Standard support
        - name: Enterprise
          price: Custom
          description: For organizations at scale
          features:
            - Everything in Team
            - SAML/SCIM SSO
            - Advanced compliance features
            - Premium support

learn:
    title: Get started with Pulumi secrets management
    items:
        - title: Start managing secrets today
          description: Experience enterprise-grade secrets management with Pulumi Cloud's free tier.
          buttons:
            - link: https://app.pulumi.com/signup
              type: primary
              action: Start Free
            - link: /contact/?form=request-a-demo
              type: secondary
              action: Book a Demo
        - title: Learn more
          description: Explore the documentation and Get Started guides to implement ESC in your infrastructure.
          buttons:
            - link: /docs/esc/
              type: primary
              action: Read the Docs
            - link: /docs/esc/get-started/
              type: secondary
              action: Get Started

---
