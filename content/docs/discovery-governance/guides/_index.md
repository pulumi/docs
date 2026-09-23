---
title: Guides
title_tag: Discovery & governance guides
h1: Guides
meta_desc: Task-oriented guides for Discovery & governance, including connecting cloud accounts, importing resources, writing policy packs, and querying the Context API.
menu:
  discovery-governance:
    name: Guides
    parent: discovery-governance-home
    identifier: dg-guides
    weight: 30
aliases:
  - /docs/insights/policy/integrations/
  - /docs/discovery-governance/policy/integrations/
---

These guides walk through common Discovery & governance tasks. Each one is self-contained, so start with whichever matches what you're trying to do.

## Discovery

- [Connect cloud accounts](/docs/discovery-governance/guides/connect-cloud-accounts/): Onboard AWS, Azure, and Google Cloud accounts in bulk with the connection wizard.
- [Search resources](/docs/discovery-governance/guides/search-resources/): Find resources with structured queries or natural language.
- [Import resources with Visual Import](/docs/discovery-governance/guides/visual-import/): Generate Pulumi IaC code for discovered resources.
- [Migrate a discovered stack](/docs/discovery-governance/guides/migrate-discovered-stack/): Move CloudFormation and ARM resources from a discovered stack to Pulumi IaC.
- [Export resource data](/docs/discovery-governance/guides/export-resource-data/): Export resource data to CSV or read it through the REST API.

## Policies

- [Use pre-built policy packs](/docs/discovery-governance/guides/pre-built-policy-packs/): Apply ready-made compliance packs for frameworks such as CIS, PCI DSS, and HITRUST.
- [Enforce AWS Organizations tag policies](/docs/discovery-governance/guides/aws-organizations-tag-policies/): Block deployments that are missing the tags your AWS Organizations tag policies require.
- [Write a policy pack](/docs/discovery-governance/guides/write-a-policy-pack/): Author custom policies in TypeScript, Python, or OPA.
- [Enforce policies in CI/CD](/docs/discovery-governance/guides/policies-in-ci-cd/): Run policy checks in your pipelines before changes deploy.

## Context API

- [Query the Context API](/docs/discovery-governance/guides/context-api/): Build selectors, follow relationships, and interpret graph query results.
