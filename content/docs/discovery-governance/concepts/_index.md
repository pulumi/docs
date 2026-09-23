---
title: Concepts
title_tag: Discovery & governance concepts
h1: Concepts
meta_desc: Core concepts behind Pulumi Discovery, Pulumi Policies, and the Context API, including cloud accounts, discovered stacks, policy packs, and policy groups.
menu:
  discovery-governance:
    name: Concepts
    parent: discovery-governance-home
    identifier: dg-concepts
    weight: 20
---

These pages explain how Discovery, Pulumi Policies, and the Context API work. To set something up, see [Guides](/docs/discovery-governance/guides/). To try it end to end, start with [Get started](/docs/discovery-governance/get-started/).

## Discovery

- [Discovery](/docs/discovery-governance/concepts/discovery/): How Discovery scans your cloud accounts and organizes the resources it finds.
  - [Cloud accounts](/docs/discovery-governance/concepts/discovery/cloud-accounts/): The accounts Discovery scans, how account hierarchies work, and the credentials each one uses.
  - [Visual Import](/docs/discovery-governance/concepts/discovery/visual-import/): How Visual Import turns discovered resources into Pulumi IaC code.
  - [Discovered stacks](/docs/discovery-governance/concepts/discovery/discovered-stacks/): How Discovery models CloudFormation, AWS CDK, and ARM deployments as stacks.

## Policy as code

- [Policy as code](/docs/discovery-governance/concepts/policy-as-code/): How Pulumi Policies checks IaC-managed and discovered resources, and the enforcement modes.
  - [Policies](/docs/discovery-governance/concepts/policy-as-code/policies/): Resource and stack validation policies, enforcement levels, remediation, and configuration.
  - [Policy packs](/docs/discovery-governance/concepts/policy-as-code/policy-packs/): How policies are packaged, versioned, configured, and run.
  - [Policy groups](/docs/discovery-governance/concepts/policy-as-code/policy-groups/): How policy packs are applied to stacks and cloud accounts in preventative or audit mode.

## Context API

- [Context API](/docs/discovery-governance/concepts/context-api/): How graph queries answer dependency, ownership, and change-impact questions about your infrastructure.
