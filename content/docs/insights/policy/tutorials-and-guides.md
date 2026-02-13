---
title: Tutorials & Guides
title_tag: "Tutorials & Guides | Pulumi Policies"
h1: Policy Tutorials & Guides
meta_desc: Learn Pulumi policy as code through hands-on tutorials, advanced IDP patterns, and practical guides for enforcing compliance across your infrastructure.
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  insights:
    name: Tutorials & Guides
    parent: insights-policy
    weight: 70
---

Explore hands-on tutorials, advanced patterns, and practical guides for using Pulumi policies to enforce compliance and security across your infrastructure.

## Tutorials

### Creating a custom policy pack

Walk through creating a policy pack that enforces AWS security requirements, including S3 bucket versioning, EC2 instance type restrictions, and resource tagging. Available in TypeScript and Python.

[Start the tutorial](/tutorials/custom-policy-pack/)

### Evaluating Terraform compliance with Pulumi

Learn how to apply Pulumi policies to infrastructure originally provisioned with Terraform. Discover resources and evaluate them against policy packs using Pulumi Insights.

[Start the tutorial](/tutorials/eval-compliance-terraform/)

## IDP patterns

These patterns from the [Internal Developer Platform (IDP)](/docs/idp/) documentation show advanced techniques for using policies in platform engineering workflows.

### Policies as tests

Implement governance and compliance requirements using Pulumi policies that run as automated tests during deployment. Policies act as guardrails that prevent non-compliant infrastructure from being deployed, providing automated enforcement of organizational standards and security rules.

[Read the pattern](/docs/idp/best-practices/patterns/policies-as-tests/)

### Validating component inputs using policy functions

Create reusable policy functions that validate component inputs consistently across both policy packs and component constructors. This pattern ensures the same validation logic runs during policy enforcement and during component creation, catching configuration errors early.

[Read the pattern](/docs/idp/best-practices/patterns/validating-component-inputs-using-policy-functions/)

### Cost control using components, policies, and constrained inputs

Combine Pulumi components with constrained input types and policies to control infrastructure costs. Limit available resource configurations to approved options and enforce cost-related policies to prevent expensive deployments while maintaining developer productivity.

[Read the pattern](/docs/idp/best-practices/patterns/cost-control-using-components-policies-constrained-inputs/)

## Additional resources

- [Policies FAQ](/docs/support/faq/policies/) — Answers to common questions about Pulumi policies, including how policy packs interact, how enforcement works during stack imports and refreshes, and open source licensing.
- [Pre-built policy packs](/docs/insights/policy/policy-packs/pre-built-packs/) — Ready-made packs for CIS, HITRUST, NIST, PCI DSS, and Pulumi best practices.
- [Compliance frameworks reference](/docs/reference/pre-built-policy-packs/) — Detailed per-policy reference documentation for each pre-built compliance framework.
- [Policy as code blog posts](/blog/benefits-of-policy-as-code/) — Read about real-world use cases and best practices for policy as code.
