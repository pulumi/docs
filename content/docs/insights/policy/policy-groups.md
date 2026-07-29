---
title: Policy Groups
title_tag: "Policy Groups | Pulumi Policies"
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
  - /docs/using-pulumi/crossguard/core-concepts/
---

Policy groups organize one or more policy packs and apply them to specific stacks or cloud accounts. They determine when and where policies are enforced across your organization.

## Types of policy groups

Pulumi Policies provides two types of policy groups, each designed for different enforcement patterns:

### Preventative policy groups

Preventative policy groups apply to Pulumi stacks and run *before* resources are deployed. They act as guardrails during `pulumi up` and `pulumi preview`, blocking non-compliant deployments before they reach your cloud environment.

**Key characteristics:**

- Evaluate resources at deployment time
- Can block deployments with `mandatory` enforcement
- Only see resources managed by Pulumi
- Provide immediate feedback to developers

### Audit policy groups

Audit policy groups provide continuous compliance monitoring for both Pulumi stacks and [cloud accounts](/docs/insights/accounts/). For stacks, they evaluate the latest state whenever the stack updates. For cloud accounts, they scan all resources on a schedule, including resources not managed by Pulumi.

**Key characteristics:**

- Evaluate existing resources continuously
- Cannot block deployments (reporting only)
- See all resources in cloud accounts, not just Pulumi-managed
- Provide compliance visibility and reporting

{{% notes "info" %}}
When you enable Pulumi Policies for your organization, default policy groups are created automatically: `default-preventative-policy-group` for stacks and `default-audit-policy-group` for stacks and cloud accounts. See [Default policy groups](#default-policy-groups) for how they behave and what to consider before adding policy packs to them.
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

- **Block non-compliant deployments before they happen** - Prevent security issues like public S3 buckets or unencrypted databases from ever reaching production
- **Provide fast feedback to developers** - Catch policy violations during development and testing, before code review or CI/CD
- **Enforce standards for Pulumi-managed infrastructure** - Ensure all resources deployed through Pulumi meet organizational requirements

### Use audit policy groups when you want to:

- **Monitor compliance continuously** - Track policy adherence across your entire cloud footprint, not just at deployment time
- **Include non-Pulumi resources** - Scan resources created manually, through other tools, or by AWS/Azure/GCP services
- **Test new policies safely** - Validate policy behavior in production without risking deployment disruptions
- **Generate compliance reports** - Provide auditors with continuous evidence of policy monitoring and findings

## Best practices

**Start with audit, promote to preventative**: Test new policies in audit mode first to understand their impact, then promote successful policies to preventative enforcement.

**Layer your enforcement**: Use preventative policies for critical "must never violate" rules and audit policies for continuous monitoring and reporting.

**Organize by risk level**: Group high-risk policies (security, compliance) separately from lower-risk policies (optimization, best practices) to manage exceptions more easily.

## Default policy groups

Every organization has two default policy groups, created automatically the first time you enable Pulumi Policies:

- **`default-preventative-policy-group`** automatically includes every new stack in the organization.
- **`default-audit-policy-group`** automatically includes every newly connected [cloud account](/docs/insights/discovery/accounts/), alongside all stacks.

You can remove an individual stack or account from a default group the same way you would from any other group. The default groups themselves can't be deleted — every organization always has exactly one default group per entity type.

### Adding policy packs to a default policy group

Because the default preventative policy group covers every stack in the organization, enabling a policy pack there with `mandatory` enforcement starts blocking `pulumi up` and `pulumi preview` for every team immediately, with no gradual rollout. Follow the [audit-first best practice](#best-practices) above before adding a pack to a default group: stage it in an audit policy group, or in the default preventative group with `advisory` enforcement, confirm its findings look right across your stacks, and only then switch it to `mandatory`.

Before enabling any policy pack, also confirm that every environment where `pulumi preview` or `pulumi up` runs — developer machines, CI/CD workers — has the runtime that the pack's [`PulumiPolicy.yaml`](/docs/insights/policy/policy-packs/project-file/) declares. A policy pack evaluates locally, as part of the `pulumi` CLI invocation, so a `nodejs` pack requires Node.js on the client, a `python` pack requires Python, and so on. Because a mandatory pack on the default preventative group applies to every stack, a missing runtime shows up as unexpected `pulumi up` failures across the organization rather than in a single team's pipeline.

## Managing policy groups programmatically

Beyond the console, you can add and remove stacks, cloud accounts, and policy packs from a policy group using the [Pulumi Cloud REST API](/docs/insights/policy/api-reference/) or the `pulumiservice` Pulumi provider, including the default policy groups described above.

### Using the REST API

A single `PATCH` request to a policy group's endpoint can add or remove a stack, a cloud account, or a policy pack, or rename the group, through one or more fields in the request body:

- `addStack` / `removeStack` take a stack's `name` and `routingProject`; both fields are required.
- `addPolicyPack` / `removePolicyPack` take the pack's `name`, `displayName`, `version`, and `versionTag`; all four fields are required. Find the values for a specific pack via the [policy packs endpoint](/docs/reference/cloud-rest-api/policy-packs/) or the output of `pulumi policy publish`.
- `addInsightsAccount` / `removeInsightsAccount` take the account's `name`.

These fields are additive: sending `addStack` doesn't touch the group's existing stacks or policy packs, so requests from multiple automations can run concurrently. A successful request returns `204 No Content`.

{{% notes "warning" %}}
The `stacks`, `policyPacks`, and `insightsAccounts` fields, as opposed to their `add`/`remove` counterparts, replace the group's *entire* membership list whenever you include them in a request. Omit a field you don't want to change; an empty array clears it.
{{% /notes %}}

To apply multiple changes to a group in one round trip, send them to the group's `/batch` endpoint instead, as an array of the same request bodies described above.

### Using the Pulumi provider

The `pulumiservice` provider's `PolicyGroupStackAttachment` and `PolicyGroupInsightsAccountAttachment` resources each manage a single stack's or cloud account's membership in a policy group declaratively, without taking ownership of the group's other members:

```typescript
import * as pulumiservice from "@pulumi/pulumiservice";

new pulumiservice.PolicyGroupStackAttachment("attach-stack", {
    orgName: "my-org",
    policyGroup: "default-preventative-policy-group",
    name: "my-stack",
    routingProject: "my-project",
});
```

Because each resource manages one membership edge, multiple stacks or teams can attach themselves to the same policy group in parallel without one Pulumi program's `pulumi up` clobbering another's. There's no equivalent attachment resource for policy packs; manage those on a policy group through the REST API's `addPolicyPack`/`removePolicyPack` fields instead.

{{% notes "warning" %}}
Avoid running `pulumi import pulumiservice:api:PolicyGroup` against a default policy group to bring it under management. Import only populates the resource's `name`, `orgName`, and `entityType`, so the next `pulumi up` would apply an empty `policyPacks` list and disable every pack already enabled on the group. The resource is also delete-owned, and while the API refuses to delete an organization's default group, a `pulumi destroy` that tries would still fail your operation. If you need to manage a default group's stacks or accounts declaratively, use the attachment resources above instead, and leave the `protect: true` option that `pulumi import` adds by default in place for any `PolicyGroup` you do import.
{{% /notes %}}

## ESC environments

Policy packs in a policy group can reference [Pulumi ESC](/docs/esc/) environments for secrets and configuration. When you attach an ESC environment to a policy pack, values from the environment's [`policyConfig`](/docs/esc/concepts/outputs/#policyconfig) and [`environmentVariables`](/docs/esc/concepts/outputs/#environmentvariables) are available to the policy pack at runtime.

Environment references support [versioning and tagging](/docs/esc/concepts/versioning/). You can pin to a specific revision or tag (e.g., `my-env@stable` or `my-env@v1`) to control when configuration changes take effect.

## Next steps

- [Create and configure policy groups](/docs/insights/policy/get-started/)
- [View and manage policy findings](/docs/insights/policy/policy-findings/)
- [Write custom policy packs](/docs/insights/policy/policy-packs/authoring/)
- [Policy API reference](/docs/insights/policy/api-reference/)
