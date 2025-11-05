---
title: Insights & Governance
linktitle: Insights & Governance
docs_home: true
notitle: true
norightnav: true
menu:
  insights:
    identifier: insights-home
    weight: 1
meta_desc: Discover, secure, and govern cloud infrastructure with comprehensive visibility and policy enforcement across all your resources.
meta_image: /images/docs/meta-images/insights-meta.png
h1: Insights & Governance
description: |
  Pulumi Insights & Governance provides comprehensive cloud visibility and policy enforcement—discover all infrastructure and ensure compliance, regardless of how resources were created.

link_buttons:
  primary:
    label: Get Started
    link: /docs/insights/discovery/get-started/

sections:
- type: flat
  heading: Overview
  description_md: |
    Pulumi Cloud provides complete visibility and control over your cloud infrastructure, whether resources were provisioned by Pulumi, Terraform, CloudFormation, or created manually.

    **Two ways to get started:**
    - **New to Pulumi?** Start with [Discovery](/docs/insights/discovery/) to scan existing infrastructure, then add Policy enforcement.
    - **Already using Pulumi IaC?** Add [Policy](/docs/insights/policy/) to enforce compliance before deployments reach production.

- type: button-cards
  heading: Discovery
  cards:
  - emoji: 🚀
    heading: Get Started
    link: /docs/insights/discovery/get-started/
    description: Scan your cloud accounts and discover all infrastructure resources.
  - emoji: 💡
    heading: How Discovery Works
    link: /docs/insights/discovery/
    description: Learn how Discovery scans cloud accounts and organizes resources for visibility and import.
  - emoji: 🔗
    heading: Accounts
    link: /docs/insights/discovery/accounts/
    description: Connect cloud accounts to sync and monitor infrastructure resources.
  - emoji: 🔎
    heading: Resource Search
    link: /docs/insights/discovery/search/
    description: Find resources using structured queries or natural language.
  - emoji: 📊
    heading: Visual Import
    link: /docs/insights/discovery/visual-import/
    description: Import existing cloud resources into Pulumi management.
  - emoji: 📤
    heading: Data Export
    link: /docs/insights/discovery/data-export/
    description: Export resource data to CSV or integrate via REST API.

- type: button-cards
  heading: Policy
  cards:
  - emoji: 🚀
    heading: Get Started
    link: /docs/insights/policy/get-started/
    description: Configure your first policy group and enforce compliance across Pulumi stacks and discovered cloud resources.
  - emoji: 💡
    heading: Policy Concepts
    link: /docs/insights/policy/
    description: Learn how policies, policy packs, and policy groups work together to enforce compliance.
  - emoji: 📦
    heading: Pre-built Policy Packs
    link: /docs/insights/policy/policy-packs/pre-built-packs/
    description: Use ready-made compliance rules for CIS, PCI DSS, SOC 2, and other frameworks with no code required.
  - emoji: 🔄
    heading: Policy Groups
    link: /docs/insights/policy/policy-groups/
    description: Apply policy packs with preventative enforcement to block non-compliant deployments or audit mode to scan all discovered resources.
  - emoji: ⚠️
    heading: Policy Findings
    link: /docs/insights/policy/policy-findings/
    description: View violations, track remediation progress, and monitor compliance trends across all infrastructure.

- type: flat
  heading: Have questions?
  description: <p>For questions or feedback, reach out on <a href="https://slack.pulumi.com" target="_blank">community Slack</a>, <a href="https://github.com/pulumi" target="_blank">GitHub</a>, or <a href="/support/">contact support</a>.</p>
---
