---
title: Policy Packs
title_tag: Policy Packs | Pulumi Policies
h1: Policy Packs
meta_desc: Learn how to use Policy Packs to enforce organizational standards and best practices across your Pulumi infrastructure as code.
menu:
  insights:
    parent: insights-policy
    identifier: policy-packs
    weight: 20
aliases:
  - /docs/insights/policy/configuration/
  - /docs/using-pulumi/crossguard/configuration/
  - /docs/guides/crossguard/configuration/
  - /docs/iac/packages-and-automation/crossguard/configuration/
  - /docs/iac/crossguard/configuration/
  - /docs/iac/using-pulumi/crossguard/configuration/
  - /docs/insights/policy/policy-as-code/configuration/
---

Policy packs are collections of rules that enforce compliance and best practices across your infrastructure. Each policy pack contains one or more policies that validate resource properties, configurations, or relationships between resources.

## Types of policy packs

Pulumi offers two approaches to policy enforcement:

### Pre-built policy packs

Pulumi provides ready-to-use policy packs for common compliance frameworks including CIS, PCI DSS, HITRUST, and NIST. These packs are maintained by Pulumi and cover security, cost, and operational best practices for AWS, Azure, and Google Cloud.

You can enable pre-built packs directly from Pulumi Cloud with no code required.

[Explore pre-built policy packs →](/docs/insights/policy/policy-packs/pre-built-packs/)

### Custom policy packs

Write your own policies in TypeScript or Python to enforce organization-specific requirements. Custom policies can validate individual resources or entire stack configurations, with support for:

- Configurable enforcement levels (advisory, mandatory, disabled)
- Custom configuration schemas for flexible policy behavior
- Local testing before publishing
- Version management and updates

[Learn to author custom policies →](/docs/insights/policy/policy-packs/authoring/)

## Next steps

- [Browse pre-built policy packs](/docs/insights/policy/policy-packs/pre-built-packs/)
- [Write custom policy packs](/docs/insights/policy/policy-packs/authoring/)
- [Configure policy groups](/docs/insights/policy/policy-groups/)
- [View policy findings](/docs/insights/policy/policy-findings/)
