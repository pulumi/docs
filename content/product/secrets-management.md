---
title: "Centralized Configuration & Secrets Management – Pulumi ESC"
meta_desc: Centralize secrets and configurations with Pulumi ESC. Connect any vault, eliminate secrets sprawl, secure every environment.
meta_image: /images/product/secrets-management/esc-meta.png
type: page
layout: product-page
aliases:
  - /esc
  - /product/esc
  - /product/pulumi-esc

sections:
  - type: product_hero
    title_primary: "Zero sprawl."
    title_secondary: "One place for every secret."
    title_reversed: true
    description: Manage all your secrets and configuration at scale with Pulumi ESC.
    cta_primary_text: Get Started
    cta_primary_link: https://app.pulumi.com/signup
    cta_secondary_text: Contact Us
    cta_secondary_link: /contact/
    image: /images/product/secrets-management/esc-hero-image.png
    image_alt: Pulumi ESC secrets management — connect any secrets store
    anchor: hero

  - type: product_two_column
    heading: One interface for all your secrets
    description: |
      **Connect any secrets store and control everything centrally.**

      Pulumi ESC (Environments, Secrets, Configuration) centralizes secrets from every vault and cloud provider. No more juggling AWS Secrets Manager, HashiCorp Vault, and Azure Key Vault separately. Connect them all, manage them centrally, access them anywhere.
    cards:
      - icon: fa-code
        title: Eliminate secrets sprawl
        description: |
          Connect to HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, 1Password, and more, with full RBAC, versioning, and audit logging built in.
      - icon: fa-shield-alt
        title: Secure by default
        description: |
          Dynamic, short-lived credentials via OIDC. No plaintext secrets, anywhere, ever.
      - icon: fa-cogs
        title: Flexible access, anywhere
        description: |
          CLI, API, SDKs, Kubernetes operators, and native Pulumi IaC integration. Or use standalone with any workflow.
    anchor: overview

  - type: video_embed
    youtube_id: JY3Cm1UUIYE
    title: Pulumi ESC overview
    poster_image: /images/product/secrets-management/esc-poster.png
    poster_alt: Pulumi ESC overview — Watch Now
    anchor: esc-overview

  - type: testimonial_product
    quote: |
      With Pulumi ESC, our developers get dynamic AWS and Azure credentials on-demand. Onboarding new developers is quick and secure, with no more manually filling in .env templates.
    author: Liam White
    title: Platform Lead
    company: Tetrate
    logo: /logos/tech/tetrate.svg
    anchor: testimonial-tetrate

  - type: section_header
    tag_line: Secrets management
    title: Centrally manage every environment
    description: |
      Manage secrets across every environment and service from a single control plane
    image: /images/product/secrets-management/esc-screenshot-code.png
    image_alt: Pulumi ESC environment management and code
    anchor: environments

  - type: three_column
    icon_style: black
    icon_layout: above
    columns:
      - icon: fa-hourglass-end
        title: Dynamic credentials
        description: |
          Generate just-in-time, short-lived credentials via OIDC. Automatically revoke access when leases expire.
      - icon: fa-cubes
        title: Environment composition
        description: |
          Build complex configurations from simple, reusable components. Inherit common settings while overriding specific values.
      - icon: fa-shield-alt
        title: Full audit trail
        description: |
          Track every access, every change, every user. Complete visibility into who's using what secrets and when.
      - icon: fa-code-branch
        title: Version control
        description: |
          Every environment change is versioned. Roll back instantly or access previous configurations when needed.
      - icon: fa-users
        title: RBAC & teams
        description: |
          Fine-grained access controls integrated with your identity provider. SAML/SCIM support for enterprise SSO.
      - icon: fa-puzzle-piece
        title: Extensible plugin model
        description: |
          Support for custom secret stores through our plugin architecture. Integrate with any system.
    anchor: features

  - type: testimonial_product
    background: 2
    quote: |
      Pulumi ESC has been a lifesaver for us. It's nice to throw everything behind an ESC environment and eliminate one-off granting IAM permissions and other issues related to static credentials.
    author: Jk Jensen
    title: Software Engineering Team Lead
    company: Mysten Labs
    logo: /logos/tech/mysten-labs.svg
    anchor: testimonial-mysten

  - type: two_column
    highlight_first_card: true
    columns:
      - title: Start managing secrets today
        description: Experience enterprise-grade secrets management with Pulumi Cloud's free tier.
        cta_primary_text: Start Free
        cta_primary_link: https://app.pulumi.com/signup
        cta_text: Book a Demo
        cta_link: /contact/?form=request-a-demo
      - title: Learn more
        description: Explore the documentation and Get Started guides to implement ESC in your infrastructure.
        cta_primary_text: Read the Docs
        cta_primary_link: /docs/esc/
        cta_text: Get Started
        cta_link: /docs/esc/get-started/
    anchor: get-started

---
