---
title: "Centralized Configuration & Secrets Management – Pulumi ESC"
meta_desc: Centralize secrets and configurations with Pulumi ESC. Connect any vault, eliminate secrets sprawl, secure every environment.
meta_image: /images/product/esc-octopus-diagram.png
type: page
layout: product-page
aliases:
  - /esc
  - /product/esc
  - /product/pulumi-esc

hero:
  title_primary: Secrets & Configuration
  title_secondary: Manage all your secrets at scale.
  description: |
    Pulumi ESC (Environments, Secrets, Configuration) centralizes secrets from every vault and cloud provider. Connect HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, 1Password, and more. Dynamic credentials via OIDC. Works with or without Pulumi IaC.
  cta_primary_text: Get Started
  cta_primary_link: /signup
  cta_secondary_text: Book a Demo
  cta_secondary_link: /contact/?form=request-a-demo
  image: /images/product/esc-octopus-diagram.png
  image_alt: Pulumi ESC secrets and configuration
  anchor: hero

section_header:
  title: One interface for all your secrets
  description: |
    No more juggling AWS Secrets Manager, HashiCorp Vault, and Azure Key Vault separately. Connect them all, manage them centrally, access them anywhere.

    **Eliminate secrets sprawl** — Connect to any secrets store (HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, 1Password, and more). One interface for all your secrets. **Secure by default** — Dynamic, short-lived credentials with OIDC. Full RBAC, versioning, and audit logging. No more plaintext secrets anywhere. **Engineer-friendly access** — CLI, API, SDKs, and Kubernetes operators. Access secrets from anywhere without compromising security. **Integrated with Pulumi IaC** — Native integration with Pulumi infrastructure code, or use standalone with any application or workflow.
  anchor: overview

product_two_column:
  heading: Why teams choose Pulumi for secrets management
  description: |
    **Enterprise-grade security.** Dynamic credentials via OIDC replace long-lived keys. RBAC, audit trails, SOC 2 Type II compliant.

    **Composable environments.** Organize secrets into logical environments that inherit from each other. Share common configurations while maintaining isolation.

    **Version everything.** Every change is versioned and auditable. Roll back instantly. Know exactly who changed what and when.
  cards:
    - icon: fa-key
      title: Dynamic Credentials
      description: |
        Generate just-in-time, short-lived credentials via OIDC. Automatically revoke access when leases expire.
    - icon: fa-layer-group
      title: Environment Composition
      description: |
        Build complex configurations from simple, reusable components. Inherit common settings while overriding specific values.
    - icon: fa-clipboard-list
      title: Full Audit Trail
      description: |
        Track every access, every change, every user. Complete visibility into who's using what secrets and when.

three_column:
  anchor: features
  icon_style: black
  icon_layout: above
  columns:
    - icon: fa-sync-alt
      title: Version Control
      description: |
        Every environment change is versioned. Roll back instantly or access previous configurations when needed.
    - icon: fa-users-cog
      title: RBAC & Teams
      description: |
        Fine-grained access controls integrated with your identity provider. SAML/SCIM support for enterprise SSO.
    - icon: fa-puzzle-piece
      title: Extensible Plugin Model
      description: |
        Support for custom secret stores through our plugin architecture. Integrate with any system.

section_header_secondary:
  title: How it works
  description: |
    **1. Define Environments** — Organize secrets and configurations into logical environments. Use composition to share common settings while maintaining separation where needed.

    **2. Connect Sources** — Pull secrets from any store—Vault, AWS Secrets Manager, Azure Key Vault, and more. ESC syncs and manages them centrally.

    **3. Access Anywhere** — Consume secrets via CLI, API, SDKs, or Kubernetes operators. Every platform, every language, every workflow supported.

    **4. Stay Secure** — RBAC controls who can access what. Audit logs track every action. Dynamic credentials expire automatically.
  anchor: how-it-works

three_column_cloud:
  anchor: use-cases
  icon_style: black
  icon_layout: above
  columns:
    - icon: fa-cloud
      title: Multi-Cloud Secrets Management
      description: |
        Manage secrets across AWS, Azure, and GCP from a single interface. Perfect for Pulumi IaC or any multi-cloud application.
    - icon: fa-code-branch
      title: Secure CI/CD Pipelines
      description: |
        Inject secrets into any CI/CD platform without storing them in pipeline configuration. Dynamic credentials that expire after use.
    - icon: fa-cog
      title: Engineering Environment Setup
      description: |
        Engineers get the exact secrets they need, when they need them. No manual configuration or insecure credential sharing.
    - icon: fa-th-large
      title: Kubernetes Configuration
      description: |
        Manage ConfigMaps and Secrets across clusters. Use the ESC Kubernetes operator for seamless integration.

testimonial:
  quote: |
    With Pulumi ESC, our developers get dynamic AWS and Azure credentials on-demand. Onboarding new developers is quick and secure, with no more manually filling in .env templates.
  author: Liam White
  title: Platform Lead
  company: Tetrate
  anchor: testimonial

footer_cta:
  title: Get started with Pulumi secrets management
  cta_primary_text: Start Free
  cta_primary_link: /signup
  cta_secondary_text: Book a Demo
  cta_secondary_link: /contact/?form=request-a-demo
  anchor: get-started
---
