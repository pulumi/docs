---
title: Pulumi for Terraform users
meta_desc: Run your existing Terraform on Pulumi. Manage Terraform state in Pulumi Cloud, share modules across languages, and write HCL as a first-class Pulumi language.
type: page
layout: template-page
url: /terraform

sections:
  - type: hero
    layout: split
    title: "*Keep your Terraform.*<br>Gain the platform around it."
    description: |
      Pulumi Cloud manages your Terraform state, turns your modules into components any language can consume, and runs HCL as a first-class Pulumi language. Bring the infrastructure you already have.
    badge_text: "New in the August 2026 release"
    badge_link: /releases/terraform-state-backend-modules-hcl/
    cta_primary_text: Get started
    cta_primary_link: /docs/iac/get-started/terraform/terraform-state-backend/
    cta_secondary_text: Compare Pulumi and Terraform
    cta_secondary_link: /docs/iac/comparisons/terraform/
    image: /images/releases/august-2026/release-hero-right-light.svg
    image_alt: HCL, Terraform state, and Terraform modules converging on the Pulumi mark
    image_max_width: 640px
    anchor: hero

  - type: feature_split
    heading: Your Terraform estate, on Pulumi's engine
    description: |
      Adopting Pulumi no longer starts with a rewrite. Your existing state, modules, and HCL are things Pulumi runs, so you can put them on a managed platform first and decide about languages later.
    cta_text: Read the August 2026 release
    cta_link: /releases/terraform-state-backend-modules-hcl/
    cards:
      - icon: database
        title: Terraform state
        description: |
          Point the Terraform CLI at Pulumi Cloud with a standard backend block. Your workflow stays the same.
      - icon: puzzle-piece
        title: Terraform modules
        description: |
          Publish once to the Pulumi Cloud private registry, then consume from Terraform, OpenTofu, or any Pulumi language.
      - icon: file-code
        title: HCL
        description: |
          HCL is a fully supported Pulumi language, with no syntactical differences from the code your team writes today.
    anchor: overview

  - type: section_header_with_image
    tag_line: Terraform state and remote execution
    title: Bring your Terraform state to Pulumi Cloud
    description: |
      Pulumi Cloud implements Terraform's remote backend API, so a standard `backend "remote"` block is the whole migration. Your HCL, your CLI, and your day-to-day workflow are unchanged, and both Terraform and OpenTofu work.

      In return you get encrypted state, automatic locking, update history, role-based access control, and audit policies, plus a single view of Terraform-managed and Pulumi-managed resources together in [resource search](/docs/insights/discovery/search/).
    cta_text: Set up the backend
    cta_link: /docs/iac/get-started/terraform/terraform-state-backend/
    image: /images/releases/august-2026/release-terraform-backend.svg
    image_alt: Three infrastructure stacks feeding into the Pulumi mark
    cards:
      - icon: terminal-window
        title: Remote execution
        description: |
          Plans and applies run in Pulumi-managed containers instead of on laptops, with logs streamed to your terminal.
      - icon: key
        title: Config and secrets in ESC
        description: |
          Pulumi ESC injects OIDC credentials at apply time and exposes outputs to downstream stacks and services.
      - icon: shield-check
        title: Preventative policies
        description: |
          Pulumi Policies evaluates a Terraform plan and blocks non-compliant resources before they reach production.
      - icon: robot
        title: Neo code reviews
        description: |
          Pulumi Neo reviews infrastructure pull requests and tells you whether a change is safe to merge.
    anchor: terraform-state

  - type: section_header_with_image
    flip: true
    tag_line: Terraform modules
    title: One module, every language
    description: |
      The Pulumi Cloud private registry has native support for Terraform modules. Publishing is wire-compatible with HCP Terraform's API, so existing pipelines migrate by repointing the host.

      Once a module is published, Pulumi converts it into a typed component that any team can consume, whether they write Terraform, OpenTofu, TypeScript, Python, Go, .NET, Java, or YAML. One module, maintained once, serves every team.
    cta_text: Explore Terraform modules
    cta_link: /docs/idp/concepts/terraform-modules/
    image: /images/releases/august-2026/release-modules.svg
    image_alt: A Terraform module imported into a Pulumi program
    cards:
      - icon: stack
        title: A private registry
        description: |
          Host your team's modules in Pulumi Cloud with versioning and access control built in.
      - icon: translate
        title: Typed in every language
        description: |
          Pulumi generates a typed SDK per language, so consumers get autocomplete and type checking.
      - icon: package
        title: The community ecosystem
        description: |
          Use any public Terraform module through a generated SDK or a dynamic module loader.
    anchor: terraform-modules

  - type: section_header_with_image
    tag_line: HCL as a Pulumi language
    title: Write HCL, get the whole ecosystem
    description: |
      Set `runtime: hcl` and your existing `.tf` files run on the Pulumi engine, with the same syntax and nothing to convert. Terraform's own state and versioning blocks are the exception: Pulumi manages state itself, so `backend` and `required_version` are ignored with a warning, and a `cloud` block has to be removed. The [language reference](/docs/iac/languages-sdks/hcl/hcl-language-reference/#terraform-compatibility) lists every difference.

      HCL programs reach the full Pulumi ecosystem: thousands of providers, Pulumi Cloud, ESC, policies, and Neo. Teams that prefer HCL can also publish components that colleagues consume from any other Pulumi language.
    cta_text: Read the HCL docs
    cta_link: /docs/iac/languages-sdks/hcl/
    image: /images/releases/august-2026/release-hcl.svg
    image_alt: An HCL program running on the Pulumi engine
    cards:
      - icon: rocket-launch
        title: Start from a template
        description: |
          HCL starter and architecture templates stand up a new project in seconds.
      - icon: cube
        title: Components in HCL
        description: |
          Build typed, multi-language components without leaving HCL.
      - icon: cloud-check
        title: Every provider
        description: |
          The full Pulumi Registry, including any provider bridged from Terraform.
    anchor: hcl

  - type: case_study_grid
    title: Proven at scale
    description: |
      Some of the largest infrastructure estates in the world run on Pulumi.
    cards:
      - slug: wiz
      - slug: bmw
      - slug: mercedes-benz
    anchor: scale

  - type: three_column
    tag_line: Adoption
    title: Adopt at the pace that suits you
    subtitle: |
      These paths combine, and none of them require finishing another first. Most teams start with one and add others over time.
    icon_layout: above
    columns:
      - icon: database
        title: Keep running Terraform
        description: |
          Move state to Pulumi Cloud for governance and visibility while your team keeps using the Terraform or OpenTofu CLI.
        cta_text: Host your state
        cta_link: /docs/iac/get-started/terraform/terraform-state-backend/
      - icon: file-code
        title: Keep your HCL
        description: |
          Run your existing `.tf` files on the Pulumi engine before anyone decides whether to adopt another language.
        cta_text: Read the HCL docs
        cta_link: /docs/iac/languages-sdks/hcl/
      - icon: package
        title: Keep your modules and providers
        description: |
          Use existing Terraform modules and any Terraform provider directly from a Pulumi program.
        cta_text: Use a Terraform module
        cta_link: /docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/
      - icon: arrows-clockwise
        title: Convert when you're ready
        description: |
          `pulumi convert --from terraform` translates HCL into the language of your choice, preserving names and structure.
        cta_text: See the migration guide
        cta_link: /docs/iac/guides/migration/migrating-to-pulumi/from-terraform/
      - icon: git-branch
        title: Run both side by side
        description: |
          Pulumi programs can read outputs from an existing Terraform state file while you adopt Pulumi for new work.
        cta_text: Reference Terraform state
        cta_link: /docs/iac/guides/migration/migrating-to-pulumi/from-terraform/#referencing-terraform-state
      - icon: magnifying-glass
        title: Compare the two in detail
        description: |
          A feature-by-feature comparison of Pulumi and Terraform, including where Terraform is the better fit.
        cta_text: Read the comparison
        cta_link: /docs/iac/comparisons/terraform/
    anchor: adoption

  - type: two_column
    highlight_first_card: true
    columns:
      - title: Put your state in Pulumi Cloud
        description: |
          Add a backend block, run `terraform init`, and keep going. Encrypted state, locking, history, and RBAC come with it.
        cta_text: Get started
        cta_link: /docs/iac/get-started/terraform/terraform-state-backend/
      - title: Talk to us about your estate
        description: |
          Our team helps plan larger moves, from hosting state to converting workspaces and training the engineers who own them.
        cta_text: Contact us
        cta_link: /contact/?form=tf-migration
    anchor: get-started
---
