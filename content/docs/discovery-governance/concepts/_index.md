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
- [Cloud accounts](/docs/discovery-governance/concepts/cloud-accounts/): The accounts Discovery scans, how account hierarchies work, and the credentials each one uses.
- [Discovered stacks](/docs/discovery-governance/concepts/discovered-stacks/): How Discovery models CloudFormation, AWS CDK, and ARM deployments as stacks.

## Policies

- [Policy as code](/docs/discovery-governance/concepts/policy-as-code/): How policies validate resources, the enforcement modes, and running policies locally or through Pulumi Cloud.
- [Policy packs](/docs/discovery-governance/concepts/policy-packs/): How policies are packaged, versioned, configured, and run.
- [Policy groups](/docs/discovery-governance/concepts/policy-groups/): How policy packs are applied to stacks and cloud accounts in preventative or audit mode.

## Context API

- [Context API](/docs/discovery-governance/concepts/context-api/): How graph queries answer dependency, ownership, and change-impact questions about your infrastructure.
