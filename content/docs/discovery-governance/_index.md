---
title: Discovery & governance
linktitle: Discovery & governance
docs_home: true
notitle: true
norightnav: true
menu:
  discovery-governance:
    identifier: discovery-governance-home
    weight: 1
aliases:
- /docs/insights/
meta_desc: Discover, secure, and govern cloud infrastructure with comprehensive visibility and policy enforcement across all your resources.
h1: Discovery & governance
description: |
  Discovery & governance provides comprehensive cloud visibility and policy enforcement—discover all infrastructure and ensure compliance, regardless of how resources were created.

link_buttons:
  primary:
    label: Get started
    link: /docs/discovery-governance/get-started/

sections:
- type: flat
  heading: Overview
  description_md: |
    Pulumi Cloud provides complete visibility and control over your cloud infrastructure, whether resources were provisioned by Pulumi, Terraform, CloudFormation, or created manually.

    **Ways to get started:**
    - **New to Pulumi?** Start with [Discovery](/docs/discovery-governance/concepts/discovery/) to scan existing infrastructure, then add Policy enforcement.
    - **Already using Pulumi IaC?** Add [Policy](/docs/discovery-governance/concepts/policy-as-code/) to enforce compliance before deployments reach production.
    - **Investigating infrastructure relationships?** Use the [Context API](/docs/discovery-governance/concepts/context-api/) to query dependencies, ownership, stack consumers, and change impact.

- type: button-cards
  heading: Discovery
  cards:
  - icon: rocket-launch
    heading: Get started
    link: /docs/discovery-governance/get-started/
    description: Scan your cloud accounts and discover all infrastructure resources.
  - icon: lightbulb
    heading: How Discovery works
    link: /docs/discovery-governance/concepts/discovery/
    description: Learn how Discovery scans cloud accounts and organizes resources for visibility and import.
  - icon: link
    heading: Cloud accounts
    link: /docs/discovery-governance/concepts/cloud-accounts/
    description: Connect cloud accounts to sync and monitor infrastructure resources.
  - icon: magnifying-glass
    heading: Search resources
    link: /docs/discovery-governance/guides/search-resources/
    description: Find resources using structured queries or natural language.
  - icon: chart-bar
    heading: Visual Import
    link: /docs/discovery-governance/guides/visual-import/
    description: Import existing cloud resources into Pulumi management.
  - icon: upload
    heading: Export resource data
    link: /docs/discovery-governance/guides/export-resource-data/
    description: Export resource data to CSV or integrate via REST API.

- type: button-cards
  heading: Policies
  cards:
  - icon: rocket-launch
    heading: Get started
    link: /docs/discovery-governance/get-started/enforce-policy-as-code/
    description: Configure your first policy group and enforce compliance across Pulumi stacks and discovered cloud resources.
  - icon: lightbulb
    heading: Policy as code
    link: /docs/discovery-governance/concepts/policy-as-code/
    description: Learn how policies, policy packs, and policy groups work together to enforce compliance.
  - icon: package
    heading: Pre-built policy packs
    link: /docs/discovery-governance/guides/pre-built-policy-packs/
    description: Use ready-made compliance rules for CIS, HITRUST, NIST, PCI DSS, ISO 27001, and CMMC with no code required.
  - icon: arrows-clockwise
    heading: Policy groups
    link: /docs/discovery-governance/concepts/policy-groups/
    description: Apply policy packs with preventative enforcement to block non-compliant deployments or audit mode to scan all discovered resources.
  - icon: warning
    heading: Policy findings
    link: /docs/discovery-governance/operations/policy-findings/
    description: View violations, track remediation progress, and monitor compliance trends across all infrastructure.

- type: button-cards
  heading: Context API
  cards:
  - icon: link
    heading: Context API overview
    link: /docs/discovery-governance/concepts/context-api/
    description: Learn how graph queries help people investigate infrastructure dependencies, ownership, consumers, and change impact.
  - icon: code-window
    heading: Query the Context API
    link: /docs/discovery-governance/guides/context-api/
    description: Build selectors, follow relationships, interpret responses, and check whether an answer is complete.

- type: button-cards
  heading: Self-hosted
  cards:
  - icon: buildings
    heading: Self-hosted discovery and policy
    link: /docs/discovery-governance/operations/self-hosted/
    description: Run Discovery scans and policy evaluations in your own environment using customer-managed workflow runners.

- type: flat
  heading: Have questions?
  description: <p>For questions or feedback, reach out on <a href="https://slack.pulumi.com" target="_blank">community Slack</a>, <a href="https://github.com/pulumi" target="_blank">GitHub</a>, or <a href="/support/">contact support</a>.</p>
---
