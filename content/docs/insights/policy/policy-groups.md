---
title: Policy Groups
title_tag: "Policy Groups | Pulumi Policy"
h1: Policy Groups
meta_desc: Learn how to organize and apply policy packs using policy groups to enforce compliance across stacks and cloud accounts.
menu:
  insights:
    parent: insights-policy
    weight: 30
aliases:
  - /docs/insights/policy/preventative-vs-audit-policies/
  - /docs/insights/preventative-vs-audit-policies/
  - /docs/insights/policy/policy-packs/preventative-vs-audit-policies/
---

Policy groups organize one or more policy packs and apply them to specific stacks or cloud accounts. They determine when and where policies are enforced across your organization.

## Types of policy groups

Pulumi Policy provides two types of policy groups, each designed for different enforcement patterns:

### Preventative policy groups

Preventative policy groups apply to Pulumi stacks and run *before* resources are deployed. They act as guardrails during `pulumi up` and `pulumi preview`, blocking non-compliant deployments before they reach your cloud environment.

**Key characteristics:**

- Evaluate resources at deployment time
- Can block deployments with `mandatory` enforcement
- Only see resources managed by Pulumi
- Provide immediate feedback to developers

### Audit policy groups

Audit policy groups provide continuous compliance monitoring for both Pulumi stacks and [cloud accounts](/docs/insights/accounts/). For stacks, they evaluate the latest state whenever the stack updates. For cloud accounts, they scan all resources on a schedule—including resources not managed by Pulumi.

**Key characteristics:**

- Evaluate existing resources continuously
- Cannot block deployments (reporting only)
- See all resources in cloud accounts, not just Pulumi-managed
- Provide compliance visibility and reporting

{{% notes "info" %}}
When you enable Pulumi Policy for your organization, default policy groups are created automatically: `default-preventative-policy-group` for stacks and `default-audit-policy-group` for stacks and cloud accounts.
{{% /notes %}}

## Comparison

| Feature | Preventative Policy Groups | Audit Policy Groups |
|:----------------------|:------------------------------------|:-------------------------------------------|
| **Target** | Pulumi stacks | Pulumi stacks and cloud accounts |
| **When it runs** | During `pulumi up` / `pulumi preview` | On stack updates and scheduled scans |
| **Primary goal** | Prevent non-compliant deployments | Detect and monitor existing non-compliance |
| **Scope** | Pulumi-managed resources | Stack state and all cloud account resources |
| **Blocks deployments?** | **Yes** (with `mandatory` enforcement) | **No** |

## Enforcement levels

Policies within policy groups can have different enforcement levels:

- **Advisory:** Issues warnings but allows deployments to proceed. Useful for testing new policies or providing informational guidance.
- **Mandatory:** Blocks deployments when violations are detected. Use for critical security, compliance, or cost policies.

## When to use each type

### Use preventative policy groups when you want to:

- **Block non-compliant deployments before they happen** — Prevent security issues like public S3 buckets or unencrypted databases from ever reaching production
- **Provide fast feedback to developers** — Catch policy violations during development and testing, before code review or CI/CD
- **Enforce standards for Pulumi-managed infrastructure** — Ensure all resources deployed through Pulumi meet organizational requirements

### Use audit policy groups when you want to:

- **Monitor compliance continuously** — Track policy adherence across your entire cloud footprint, not just at deployment time
- **Include non-Pulumi resources** — Scan resources created manually, through other tools, or by AWS/Azure/GCP services
- **Test new policies safely** — Validate policy behavior in production without risking deployment disruptions
- **Generate compliance reports** — Provide auditors with continuous evidence of policy monitoring and findings

## Best practices

**Start with audit, promote to preventative**: Test new policies in audit mode first to understand their impact, then promote successful policies to preventative enforcement.

**Layer your enforcement**: Use preventative policies for critical "must never violate" rules and audit policies for continuous monitoring and reporting.

**Organize by risk level**: Group high-risk policies (security, compliance) separately from lower-risk policies (optimization, best practices) to manage exceptions more easily.

## Next steps

- [Create and configure policy groups](/docs/insights/policy/get-started/)
- [View and manage policy findings](/docs/insights/policy/policy-findings/)
- [Write custom policy packs](/docs/insights/policy/policy-packs/authoring/)
