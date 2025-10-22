---
title: Preventative vs. Audit
title_tag: "Preventative vs. Audit Policies"
h1: Preventative vs. Audit Policies
meta_desc: Learn the difference between preventative and audit policy enforcement in Pulumi to shift left and maintain continuous compliance.
menu:
  insights:
    parent: insights-policy
    weight: 30
aliases:
  - /docs/insights/preventative-vs-audit-policies/
---

Pulumi Policies enables organizations to enforce compliance and best practices using various policy packs. There are two main approaches to policy enforcement: preventative and audit. This guide explains the differences between them and provides guidance on when to use each.

## Policy groups

A Policy Group is a container for one or more policy packs that you apply to a specific set of Pulumi Entities, such as stacks and accounts. There are two main types of policy groups in Pulumi Policies:

* **Preventative Policy Groups:** These apply to your Pulumi Stacks and are run *before* a stack is deployed to the cloud (during `pulumi up`). They act as guardrails to prevent non-compliant resources from being provisioned. These policies are evaluated at deployment time and can block deployments that violate your organization's policies.
* **Audit Policy Groups:** These apply to [cloud accounts](/docs/insights/accounts/) for continuous policy evaluation through discovery scans. They scan your existing cloud resources to give you a snapshot of your compliance posture across all resources in your cloud accounts, including those not managed by Pulumi.

{{% notes "info" %}}
When Pulumi Policies is first enabled for an organization, Pulumi automatically creates default policy groups. This includes a `default-preventative-policy-group` for stacks and a `default-audit-policy-group` for cloud accounts, making it easy to get started with policy management.
{{% /notes %}}

### Comparison at a glance

| Feature | Preventative Policies | Audit Policies |
|:----------------------|:------------------------------------|:-------------------------------------------|
| **Target** | Pulumi Stacks | Cloud Accounts |
| **When it Runs** | During `pulumi up` / `pulumi preview` | On a schedule (continuous scan) |
| **Primary Goal** | Prevent non-compliant deployments | Detect existing non-compliant resources |
| **Scope** | Pulumi-managed resources in a stack | All resources within a cloud account |
| **Blocks Deployments?** | **Yes** (with `mandatory` enforcement) | **No** |

## Types of enforcement

Pulumi provides different enforcement levels for policies. These determine what happens when a policy violation is detected.

* **Advisory:** This enforcement level issues a warning when a policy violation is detected, but does not stop the deployment. This is useful for policies that are informational or when starting to roll out a new policy.
* **Mandatory:** This enforcement level stops the deployment if a policy violation is detected, preventing non-compliant resources from being created or updated. This is ideal for critical security, compliance, or cost-related policies.
* **Remediate:** This enforcement level allows inclusion of remediation resource functions that automatically remediate policy violations. When a violation is detected, Pulumi attempts to fix the non-compliant resource automatically. For more information, see the blog post on [Remediation Policies](https://www.pulumi.com/blog/remediation-policies/).

## When to use preventative vs. audit policies

Choosing the right policy approach depends on specific use cases and organizational needs:

### Use preventative policies when:

* **Enforcing critical compliance rules:** To prevent non-compliant resources from ever being created (e.g., public S3 buckets or unencrypted databases).
* **Managing Pulumi-deployed infrastructure:** To ensure all resources deployed through Pulumi stacks meet organizational standards

### Use audit policies when:

* **Authoring new policy packs:** To test and validate policies during development before rolling them out broadly
* **Getting a compliance snapshot:** To understand the current compliance posture of the entire cloud environment including resources not managed by Pulumi
* **Continuous compliance monitoring:** To maintain ongoing visibility into compliance across all cloud accounts
* **Reporting and governance:** To generate compliance reports for auditors or stakeholders and demonstrate continuous monitoring of cloud environments
