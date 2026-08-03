---
title: All your IaC, including Terraform and HCL
date: 2026-08-04
meta_desc: Pulumi Cloud is now a backend for Terraform state, HCL is a first-class language in Pulumi IaC, and Terraform modules work in Pulumi programs as is.
label: August 2026 release
short_description: Pulumi Cloud is now a backend for Terraform state, HCL is a first-class language in Pulumi IaC, and your Terraform modules work as is.
feature_image: /images/releases/august-2026/release-hero-right-light.svg
feature_image_alt: HCL, Terraform state, and Terraform modules converging on the Pulumi mark

# TODO: add a 1200x628 PNG social card at /images/releases/august-2026/meta.png
# and set meta_image here. Release detail pages aren't covered by the build-time
# meta-image generator (only /releases/changelog/ entries are).

hero:
  breadcrumb_label: August 2026
  heading: All your IaC, including<br>Terraform and HCL
  description: |
    Pulumi Cloud is now a backend for your Terraform state, HCL is a first-class language in Pulumi IaC,
    and your Terraform modules work in Pulumi programs as is.
  hero_image: /images/releases/august-2026/release-hero-bottom-dark.svg
  hero_image_alt: HCL, Terraform state, and Terraform modules converging on the Pulumi mark
  hero_image_max_height: 420

intro:
  quote: |
    "You don't have to rip out Terraform to enter the agentic era — Pulumi Cloud
    brings agentic infrastructure to the IaC estate you already have."
  attribution: |
    — Daniel Perlovsky, principal product manager, on meeting teams where their infrastructure already is
  link: /blog/bring-your-terraform-estate-into-the-agentic-era/
  link_label: Read the blog post

sections:
  - anchor: terraform-backend
    label: Terraform state in Pulumi Cloud
    heading: Terraform state in Pulumi Cloud
    description: |
      Point your existing Terraform stacks at Pulumi Cloud and keep the workflow your team already knows.
      Nothing about your HCL has to change, and your stacks become first-class entities in Pulumi Cloud.
    cards:
      - variant: image-left
        image: /images/releases/august-2026/release-terraform-backend.svg
        image_alt: Three infrastructure stacks feeding into the Pulumi mark
        icon: cloud-check
        title: Pulumi Cloud as a Terraform backend
        description: |
          Plans and applies run remotely on a Pulumi-hosted runner by default, with full visibility from
          your terminal and the Pulumi Cloud console. Gate production behind manual approvals before
          anything gets applied.
        link: /docs/iac/get-started/terraform/terraform-state-backend/

      - variant: text
        icon: users-three
        title: Access control at scale
        description: |
          Manage who can reach your Terraform stacks with tag-based access control, along with team and
          user role assignments.
        link: /docs/administration/access-identity/rbac/

      - variant: text
        icon: pulumi-neo
        title: Neo code reviews
        description: |
          Neo reviews every pull request against what Pulumi Cloud knows about your running infrastructure
          and tells you whether it's safe to merge. Fully compatible with Terraform and OpenTofu programs.
        link: /docs/ai/neo/code-reviews/

      - variant: text
        icon: pulumi-insights
        title: Preventive policies
        description: |
          Run policies against a Terraform plan and block non-compliant resources before they ever reach
          your cloud accounts.
        link: /docs/insights/policy/

      - variant: text
        icon: pulumi-secrets
        title: Config and secrets in ESC
        description: |
          Terraform state configuration is hosted natively in Pulumi ESC, so you can inject OIDC
          credentials at apply time and expose outputs to downstream stacks and services.
        link: /docs/esc/

  - anchor: hcl
    label: HCL as a Pulumi language
    heading: HCL as a Pulumi language
    description: |
      HCL is now generally available in Pulumi IaC, alongside TypeScript, Python, Go, C#, Java, and YAML.
      If your team prefers HCL, keep writing HCL, and run it on the Pulumi engine.
    cards:
      - variant: image-right
        image: /images/releases/august-2026/release-hcl.svg
        image_alt: An HCL program running on the Pulumi engine
        icon: file-code
        title: Write and run HCL with Pulumi
        description: |
          HCL programs get the whole Pulumi ecosystem: thousands of providers, Pulumi Cloud, ESC,
          policies, and Neo. And HCL in Pulumi is 100% OpenTofu compatible, with no syntactical
          differences.
        link: /docs/iac/get-started/terraform/

      - variant: text
        icon: puzzle-piece
        title: Every provider, out of the box
        description: |
          Thanks to Pulumi's Terraform bridge, any Terraform provider works in an HCL program, alongside
          every native Pulumi provider. Browse what's available in the Pulumi Registry.
        link: /registry/

  - anchor: terraform-modules
    label: Terraform modules in Pulumi programs
    heading: Terraform modules in Pulumi programs
    description: |
      The modules your team has built and maintained for years work in Pulumi programs as is, in whatever
      language you choose to write the program.
    cards:
      - variant: image-left
        image: /images/releases/august-2026/release-modules.svg
        image_alt: A Terraform module imported into a Pulumi program
        icon: package
        title: Import Terraform modules natively
        description: |
          Any Pulumi program, in any language, can import a Terraform module and use it without a single
          change. Start new projects in the language you want without giving up the building blocks you
          already have.
        link: /docs/iac/get-started/terraform/terraform-modules/

      - variant: text
        icon: stack
        title: Modules in the private registry
        description: |
          Pulumi Cloud's private registry now hosts Terraform modules alongside Pulumi packages, so every
          building block your teams reach for lives in one place. Modules hosted there work in both
          Pulumi and Terraform programs.
        link: /docs/idp/concepts/private-registry/

blog_section:
  anchor: from-the-blog
  title: From the blog
  posts:
    # TODO: the fourth post (the HCL walkthrough, pulumi/marketing#1782) doesn't exist
    # yet. Missing pages are skipped by the partial, so this is safe to leave in place —
    # update the slug if it lands under a different one.
    - /blog/bring-your-terraform-estate-into-the-agentic-era
    - /blog/getting-started-with-pulumi-hcl
    - /blog/terraforms-data-model-on-pulumis-engine
    - /blog/pulumi-hcl-building-against-an-oracle
---
