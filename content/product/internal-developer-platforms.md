---
title: "Internal Developer Platform for Self-Service – Pulumi IDP"
type: page
layout: product-page

meta_desc: Build your internal developer platform with Pulumi. Enable self-service infrastructure with enterprise governance.
meta_image: /images/product/internal-developer-platforms/idp-meta.png

aliases:
  - /solutions/platforms/
  - /product/idp
  - /product/pulumi-idp

sections:
  - type: product_hero
    title_primary: Self-service infrastructure
    title_secondary: at any scale.
    description: Build golden paths with reusable components and templates. Enable self-service provisioning through code, YAML, or developer portals — with governance built in.
    image: /images/product/internal-developer-platforms/idp-hero-image.svg
    image_alt: Pulumi internal developer platform services dashboard
    anchor: hero

  - type: product_two_column
    heading: Everything you need to build your internal developer platform.
    description: |
      Golden paths and guardrails, without the slowdown.

      Create golden paths with reusable components and templates. Enable self-service infrastructure through code, YAML, or developer portals. Enforce standards automatically with policies. Ship infrastructure faster while maintaining control.
    cards:
      - icon: fa-rocket
        title: Ship faster
        description: |
          Golden paths and reusable components get engineers from idea to production in minutes.
      - icon: fa-shield-alt
        title: Engineer-friendly governance
        description: |
          Engineers work how they prefer — in code, YAML, UI, or APIs – all with consistent governance.
      - icon: fa-eye
        title: Day 2-ready
        description: |
          Handle provisioning, updates, drift detection, and compliance beyond initial provisioning.
    anchor: overview

  - type: video_embed
    youtube_id: 3gZmKaAeppc
    title: Pulumi IDP in 3 minutes
    poster_image: /images/product/internal-developer-platforms/idp-poster.png
    poster_alt: Pulumi IDP in 3 minutes – watch the demo
    anchor: demo

  - type: section_header_with_image
    tag_line: Golden Paths
    title: Create golden paths with components and templates
    description: |
      Platform engineers define infrastructure patterns once, engineers use them everywhere:

      - **Components**: Reusable infrastructure building blocks in any language. Package your well-architected patterns.

      - **Templates**: Scaffold entire projects with one command. Applications, microservices, clusters – all standardized.

      - **Policies**: Enforce security and compliance automatically. Block non-compliant infrastructure before it ships.
    image: /images/product/internal-developer-platforms/idp-golden-paths.svg
    image_alt: Golden paths with reusable components and templates
    anchor: golden-paths

  - type: section_header_with_image
    flip: true
    tag_line: Self-Service
    title: "Self-service infrastructure,  \nmultiple interfaces"
    description: |
      Engineers provision infrastructure using their preferred approach:

      - **Code**: Write infrastructure in TypeScript, Python, Go, .NET, or Java. Full programming power.

      - **Low-Code**: Simple YAML for standard patterns. Platform teams create the templates, engineers fill in the values.

      - **No-Code**: Deploy through Pulumi's project wizard or integrate with [Backstage](/docs/idp/concepts/backstage-plugin/). Click to provision.

      - **REST API**: Programmatic access for custom tools and workflows. Build your own interfaces.
    image: /images/product/internal-developer-platforms/idp-self-service.svg
    image_alt: Self-service infrastructure with multiple interfaces
    anchor: self-service

  - type: section_header_with_image
    tag_line: Day 2 Ready
    title: Built for Day 2 operations
    description: |
      Platform engineering doesn't stop at provisioning. Handle the full infrastructure lifecycle.

      - **Drift Detection**: Know when infrastructure diverges from code. Fix drift automatically or alert the team.

      - **Import Existing Resources**: Bring unmanaged infrastructure under control. Generate code from existing resources.

      - **Dependency Management**: Track component usage across teams. Safely deprecate old versions.

      - **Enterprise RBAC**: Fine-grained permissions, SAML/SSO, audit logs. Control who can change what.
    image: /images/product/internal-developer-platforms/idp-day2.svg
    image_alt: Day 2 operations with drift detection and dependency management
    anchor: day2

  - type: two_column
    highlight_first_card: true
    columns:
      - title: Start building your platform today
        description: Build your internal developer platform with Pulumi Cloud. Start with our free tier and scale when you need enterprise features.
        cta_primary_text: Get Started with Pulumi
        cta_primary_link: https://app.pulumi.com/signup
        cta_text: Book a Demo
        cta_link: /contact/?form=request-a-demo
      - title: Platform engineering guide
        description: Learn how to build an IDP with components, templates, policies, and self-service patterns.
        cta_primary_text: Read the Docs
        cta_primary_link: /docs/idp/concepts/
        cta_text: Explore Templates
        cta_link: /docs/idp/concepts/organization-templates/
    anchor: get-started
---
