---
title: Full support for Terraform state, cross-language modules, and HCL
date: 2026-08-04
meta_desc: Manage your Terraform state, publish and share Terraform modules across languages, and write programs in HCL as a first-class Pulumi language.
label: August 2026 release
short_description: Manage your Terraform state, publish and share Terraform modules across languages, and write programs in HCL as a first-class Pulumi language.
feature_image: /images/releases/august-2026/release-hero-right-light.svg
feature_image_alt: HCL, Terraform state, and Terraform modules converging on the Pulumi mark

# Release detail pages aren't covered by the build-time meta-image generator
# (only /releases/changelog/ entries are), so this card is hand-made and lives
# under static/, which is what a non-blog meta_image path resolves against.
meta_image: /images/releases/august-2026/meta.png

hero:
  breadcrumb_label: August 2026
  heading: Full support for Terraform state, modules, and HCL
  description: |
    Manage your Terraform state with Pulumi Cloud, publish and consume Terraform modules across multiple languages, and author your IaC in HCL as a first-class Pulumi language.
  hero_image: /images/releases/august-2026/release-hero-bottom-dark.svg
  hero_image_alt: HCL, Terraform state, and Terraform modules converging on the Pulumi mark
  hero_image_max_height: 420

intro:
  quote: |
    "You don't have to rip out all your Terraform to move into the agentic era. Pulumi brings agentic infrastructure to the IaC you already have."
  attribution: |
    — Daniel Perlovsky, principal product manager
  link: /blog/bring-your-terraform-estate-into-the-agentic-era/
  link_label: Read the blog post

sections:
  - anchor: terraform-backend
    label: Terraform state and remote execution in Pulumi Cloud
    heading: Terraform state in Pulumi Cloud
    description: |
      Bring your existing Terraform stacks to Pulumi Cloud and keep the workflows and tooling your team already knows. Fully compatible with Terraform and OpenTofu.
    cards:
      - variant: image-left
        image: /images/releases/august-2026/release-terraform-backend.svg
        image_alt: Three infrastructure stacks feeding into the Pulumi mark
        icon: cloud-check
        title: Pulumi Cloud as a Terraform backend
        description: |
          Plans and applies run remotely on Pulumi Cloud-hosted runners, with full visibility from
          your terminal and the Pulumi Cloud console, plus support for manual approvals.
        link: /docs/iac/get-started/terraform/terraform-state-backend/

      - variant: text
        icon: terminal-window
        title: Remote execution
        description: |
          Run Terraform plans and applies in Pulumi-managed containers instead of on developer laptops, with logs streamed back to your terminal and persisted in Pulumi Cloud.
        link: /docs/iac/get-started/terraform/terraform-remote-execution/

      - variant: text
        icon: pulumi-secrets
        title: Config and secrets in ESC
        description: |
          Configure your Terraform stacks seamlessly with Pulumi ESC, which lets you inject OIDC
          credentials at apply time and expose outputs to downstream stacks and services.
        link: /docs/esc/

      - variant: text
        icon: pulumi-insights
        title: Preventive policies
        description: |
          Run policies against a Terraform plan and block non-compliant resources before they ever reach
          your production environments.
        link: /docs/insights/policy/

      - variant: text
        icon: pulumi-neo
        title: Neo code reviews
        description: |
          Pulumi Neo, our infrastructure agent, can review every pull request and tell you whether it's safe to merge. Fully compatible with Terraform and OpenTofu programs.
        link: /docs/ai/neo/code-reviews/

  - anchor: terraform-modules
    label: Terraform modules consumable across languages
    heading: Terraform modules for everyone
    description: |
      Host your team's Terraform modules in the Pulumi Cloud private registry and make them available to any Terraform or Pulumi project, even across language boundaries.
    cards:
      - variant: image-right
        icon: stack
        title: Publish and share modules with Pulumi Cloud
        image: /images/releases/august-2026/release-modules.svg
        image_alt: A Terraform module imported into a Pulumi program
        description: |
          Pulumi Cloud's private registry now has native support for Terraform modules, converting them automatically into Pulumi components for use in any Terraform, OpenTofu, or Pulumi program.
        link: /docs/idp/concepts/private-registry/

      - variant: text
        icon: puzzle-piece
        title: One module, many languages
        description: |
          Pulumi Cloud automatically converts your team's Terraform modules into typed, multi-language components in Pulumi-supported languages — TypeScript, Python, Go, .NET, Java, even YAML.
        link: /docs/idp/concepts/terraform-modules/

      - variant: text
        icon: package
        title: Use the full Terraform ecosystem
        description: |
          Use any Terraform module from the community in your programs, either by generating an SDK in your language of choice or in code with a dynamic module loader.
        link: /docs/iac/get-started/terraform/terraform-modules/

  - anchor: hcl
    label: HCL as a first-class Pulumi language
    heading: HCL joins the family
    description: |
      HCL (HashiCorp Configuration Language) is now a fully supported Pulumi language, alongside TypeScript, Python, Go, .NET, Java, and Pulumi YAML.
    cards:
      - variant: image-left
        image: /images/releases/august-2026/release-hcl.svg
        image_alt: An HCL program running on the Pulumi engine
        icon: file-code
        title: Write and run HCL with Pulumi
        description: |
          HCL programs get access to the full Pulumi ecosystem, including thousands of providers, Pulumi Cloud, ESC, policies, and Neo. Fully compatible with Terraform and OpenTofu with no syntactical differences.
        link: /docs/iac/languages-sdks/hcl/

      - variant: text
        icon: rocket-launch
        title: Bootstrap a new project with a template
        description: |
          Use our HCL starter and architecture templates to get a new HCL project up and running in seconds and then make it your own.
        link: /learn/official-templates/

      - variant: text
        icon: cube
        title: Build reusable components in HCL
        description: |
          With Pulumi, teams that prefer HCL can produce typed, multi-language components ready to use in any Pulumi language.
        link: /docs/iac/languages-sdks/hcl/hcl-component-reference/

# Full event cards in a panel above the blog list. Listed while they're still
# ahead of us, then for as long as there's a recording to watch; an event that has
# run with nothing to watch drops off on its own.
related_events:
  anchor: related-events
  events:
    - /events/pulumi-for-all-your-iac-terraform-hcl

blog_section:
  anchor: from-the-blog
  title: From the blog
  posts:
    - /blog/bring-your-terraform-estate-into-the-agentic-era
    - /blog/terraform-to-pulumi-cloud-hands-on
    - /blog/terraforms-data-model-on-pulumis-engine
    - /blog/compatibility-testing-pulumi-hcl
---
