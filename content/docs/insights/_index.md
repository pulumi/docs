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
  Comprehensive cloud visibility and policy enforcement—discover all infrastructure and ensure compliance, regardless of how resources were created.

link_buttons:
  primary:
    label: Get Started
    link: /docs/insights/get-started/

sections:
- type: flat
  heading: Overview
  description_md: |
    Pulumi Cloud provides complete visibility and control over your cloud infrastructure, whether resources were provisioned by Pulumi, Terraform, CloudFormation, or created manually.

    **Two ways to get started:**
    - **New to Pulumi?** Start with [Discovery](/docs/insights/discovery/accounts/) to scan existing infrastructure, then add Policy enforcement.
    - **Already using Pulumi IaC?** Add [Policy](/docs/insights/policy-as-code/) to enforce compliance before deployments reach production.

- type: button-cards
  heading: Core capabilities
  cards:
  - emoji: 🔍
    heading: Discovery
    link: /docs/insights/discovery/accounts/
    description: Automatically scan and sync cloud accounts to bring all resources under management, regardless of how they were created.
  - emoji: 🛡️
    heading: Policy Enforcement
    description: Prevent and detect security violations with pre-built compliance packs or custom policies in TypeScript, Python, or Go.
    link: /docs/insights/policy-as-code/
  - emoji: 🔎
    heading: Resource Search
    description: Find resources using structured queries or natural language with Pulumi Copilot AI.
    link: /docs/insights/search/
  - emoji: 📊
    heading: Visual Import
    description: Import existing cloud resources into Pulumi management with an intuitive visual interface.
    link: /docs/insights/import/

- type: full-width-cards
  heading: Key features
  cards:
  - emoji: 🎯
    heading: Pre-built Compliance Packs
    description: Enforce CIS Benchmarks, PCI DSS, SOC 2, ISO 27001, and other compliance frameworks out of the box.
    link: /docs/insights/policy/policy-as-code/compliance-ready-policies/
  - emoji: 🔄
    heading: Preventative and Audit Policies
    description: Block violations before deployment (preventative) or scan existing resources (audit mode) for comprehensive coverage.
    link: /docs/insights/policy/preventative-vs-audit-policies/
  - emoji: 🤖
    heading: AI-Powered Insights
    description: Ask Pulumi Copilot questions like "Show me all untagged EC2 instances" or "Find resources violating our tagging policy."
    link: /docs/ai/copilot/
  - emoji: 📤
    heading: Export and Integrate
    description: Export resource data, integrate with webhooks, or use the REST API for custom workflows.
    link: /docs/insights/import/data-export/

- type: flat
  heading: Have questions?
  description: <p>For questions or feedback, reach out on <a href="https://slack.pulumi.com" target="_blank">community Slack</a>, <a href="https://github.com/pulumi" target="_blank">GitHub</a>, or <a href="/support/">contact support</a>.</p>
---
