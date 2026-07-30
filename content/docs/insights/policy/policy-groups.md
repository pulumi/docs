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

Pulumi Policies provides two types of policy groups, each designed for a different enforcement pattern:

- <a id="preventative-policy-groups"></a>**Preventative policy groups** apply to Pulumi stacks and run before any resource is deployed. They act as guardrails during `pulumi preview` and `pulumi up`, evaluating the resources your program declares and reporting violations in the same command the developer was already running. Because they run ahead of the deployment, a policy set to `mandatory` enforcement stops a non-compliant change before it reaches your cloud provider. They see only the resources Pulumi manages.

- <a id="audit-policy-groups"></a>**Audit policy groups** continuously monitor compliance for both Pulumi stacks and [cloud accounts](/docs/insights/accounts/). For stacks, they evaluate the latest state each time the stack updates. For cloud accounts, they scan on a schedule and cover every resource in the account, including resources created by hand, by another tool, or by a cloud service itself. Audit groups report violations rather than blocking them, which makes them the safest place to measure a new policy's impact before you enforce it anywhere.

At a glance:

| | Preventative | Audit |
|:-------------------------|:----------------------------------------|:-------------------------------------------------------------|
| **Applies to** | Pulumi stacks | Pulumi stacks and cloud accounts |
| **When it runs** | During `pulumi preview` and `pulumi up` | On stack updates, and on a schedule for cloud accounts |
| **What it sees** | Resources Pulumi manages | Stack state, plus every resource in a connected cloud account |
| **Blocks deployments** | Yes, with `mandatory` enforcement | No, findings are reported for you to act on |

For guidance on which type to use, how to set enforcement levels, and how to roll policies out across an organization, see [Best practices](#best-practices).

## Default policy groups

Every organization has two policy groups that Pulumi creates and maintains for you, one of each type:

| Policy group | Type | Joins automatically |
|:--------------------------------|:----------------|:-------------------------------------------|
| `default-policy-group` | Preventative | Every stack in the organization |
| `default-accounts-policy-group` | Audit | Every cloud account connected to Insights |

<<<<<<< HEAD
{{% notes "info" %}}
When you enable Pulumi Policies for your organization, default policy groups are created automatically: `default-preventative-policy-group` for stacks and `default-audit-policy-group` for stacks and cloud accounts. See [Default policy groups](#default-policy-groups) for how they behave and what to consider before adding policy packs to them.
=======
New stacks and newly connected cloud accounts join the matching default group as they are created. You can remove a stack or account from its default group at any time, the same way you would with any other policy group. Because `default-accounts-policy-group` is an audit group, you can also add stacks to it, though none are added automatically.

In the Pulumi Cloud console, the Policy Groups tab lists both default groups with a badge marking them as defaults. From the CLI, [`pulumi policy enable`](/docs/iac/cli/commands/pulumi_policy_enable/) and [`pulumi policy disable`](/docs/iac/cli/commands/pulumi_policy_disable/) act on the default policy group when you omit `--policy-group`.

### Adding policy packs to the default preventative group

{{% notes type="warning" %}}
Be careful when changing the default policy group. `default-policy-group` is a preventative group that contains every stack in your organization. A policy pack added there takes effect on the next `pulumi preview` or `pulumi up` for every stack, and any policy set to `mandatory` starts blocking deployments immediately. There is no gradual rollout, and you cannot soften the impact afterward by converting the group to an audit group. The pack's runtime also becomes a requirement for everyone: because Pulumi's pre-built policy packs all run on Node.js, adding one means every machine that runs Pulumi needs Node.js installed.
>>>>>>> origin/master
{{% /notes %}}

To roll out a new policy pack safely, add it to a purpose-built audit policy group first, review the findings, then move it to `default-policy-group` once you understand its impact. See [Best practices](#best-practices).

Adding a policy pack to `default-policy-group` also makes that pack's [runtime](/docs/insights/policy/policy-packs/#runtime-requirements) a prerequisite for everyone who runs Pulumi against any stack in your organization. Pulumi's pre-built policy packs all run on Node.js, so enabling one for every stack means every developer machine and CI runner needs Node.js installed, whatever language the Pulumi programs themselves are written in.

### Managing the default policy groups programmatically

The default groups are fixed in identity and mutable only in membership. You can change what is in them; you cannot change what they are. These limits apply no matter how you make the change, including from the Pulumi Cloud console.

| Operation | [REST API](/docs/reference/cloud-rest-api/policy-groups/) | [Pulumi Cloud provider](/registry/packages/pulumiservice/) |
|:-----------------------------|:--------------------------------------------|:---------------------------------------------------------------------------------------------------------------|
| Add or remove stacks | Yes: [`addStack` and `removeStack`](/docs/reference/cloud-rest-api/policy-groups/#patch-apiorgsorgnamepolicygroupspolicygroup) | Yes: [`PolicyGroupStackAttachment`](/registry/packages/pulumiservice/api-docs/api/policygroupstackattachment/) |
| Add or remove cloud accounts | Yes: [`addInsightsAccount` and `removeInsightsAccount`](/docs/reference/cloud-rest-api/policy-groups/#patch-apiorgsorgnamepolicygroupspolicygroup) | Yes: [`PolicyGroupInsightsAccountAttachment`](/registry/packages/pulumiservice/api-docs/api/policygroupinsightsaccountattachment/) |
| Add or remove policy packs | Yes: [`addPolicyPack` and `removePolicyPack`](/docs/reference/cloud-rest-api/policy-groups/#patch-apiorgsorgnamepolicygroupspolicygroup) | No |
| Rename the group | No | No |
| Change the group's type, for example from audit to preventative | No: [an update request](/docs/reference/cloud-rest-api/policy-groups/#patch-apiorgsorgnamepolicygroupspolicygroup) has no field for it | No |
| Delete the group | No: [`DELETE`](/docs/reference/cloud-rest-api/policy-groups/#delete-apiorgsorgnamepolicygroupspolicygroup) rejects a default group | No |

With the REST API, a single [`PATCH`](/docs/reference/cloud-rest-api/policy-groups/#patch-apiorgsorgnamepolicygroupspolicygroup) request adds or removes stacks, accounts, and policy packs. Note that the `stacks`, `policyPacks`, and `insightsAccounts` fields replace the group's entire list, so use the `add*` and `remove*` fields to change one membership at a time. To apply several changes at once, [`PATCH .../batch`](/docs/reference/cloud-rest-api/policy-groups/#patch-apiorgsorgnamepolicygroupspolicygroupbatch) accepts an array of the same request bodies.

With Pulumi IaC, each attachment resource manages a single membership, so you can declare one against a default group without taking ownership of the group itself. The provider has no resource for attaching a policy pack to an existing policy group, so policy pack membership on a default group has to be managed from the console, the CLI, or the REST API. The provider also cannot rename a default group or change its type: both properties force a replacement on the `PolicyGroup` resource, and replacing a group means deleting it first, which Pulumi Cloud rejects for a default group.

Because `default-policy-group` cannot be deleted, renamed, or converted to an audit group, what you change to stop it from blocking deployments is its policy packs: remove them, disable them with [`pulumi policy disable`](/docs/iac/cli/commands/pulumi_policy_disable/), or set their policies to advisory.

{{% notes type="warning" %}}
Do not manage a default policy group with the [`PolicyGroup`](/registry/packages/pulumiservice/api-docs/policygroup/) resource. That resource owns the group's lifecycle, so `pulumi destroy` attempts to delete it, and its `policyPacks` property replaces the group's entire list of policy packs. Use the attachment resources to manage membership instead.
{{% /notes %}}

## Enforcement levels

Policies within policy groups can have different enforcement levels:

- **Advisory:** Issues warnings but allows deployments to proceed. Useful for testing new policies or providing informational guidance.
- **Mandatory:** Blocks deployments when violations are detected. Use for critical security, compliance, or cost policies.

## Managing policy groups at scale with ESC

<a id="esc-environments"></a>Once you have more than a handful of policy groups, keeping their configuration in sync becomes the hard part. Policy packs in a policy group can reference [Pulumi ESC](/docs/esc/) environments, which lets you define that configuration once and share it across every group that needs it, instead of editing each group separately.

When you attach an ESC environment to a policy pack, values from the environment's [`policyConfig`](/docs/esc/concepts/outputs/#policyconfig) and [`environmentVariables`](/docs/esc/concepts/outputs/#environmentvariables) are available to the policy pack at runtime. Updating the environment updates every policy group that references it.

Environment references support [versioning and tagging](/docs/esc/concepts/versioning/), so a configuration change does not have to reach every group at once. Pin a reference to a specific revision or tag, such as `my-env@stable` or `my-env@v1`, to control when the change takes effect. This pairs well with tiered policy groups: point production at a pinned tag and lower environments at the moving one, so changes are exercised before they reach the stacks that matter most.

## Best practices

### Choosing a policy group type

<a id="when-to-use-each-type"></a>Prefer preventative policy groups wherever you can. Catching a problem before the resource is provisioned is the cheapest possible outcome: nothing is created, nothing has to be remediated, and no insecure resource ever exists, even briefly. The developer also sees the violation in the `pulumi preview` or `pulumi up` they were already running, rather than in a report someone reads days later.

Audit policy groups are the right choice in three situations:

<<<<<<< HEAD
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
=======
- **Your infrastructure isn't all managed by Pulumi.** Preventative policies only see resources that Pulumi manages, so if people in your organization still make changes by hand in the cloud console with any regularity, or use other infrastructure tools, an audit group is the only way to evaluate those resources at all.
>>>>>>> origin/master

- **You are adopting policy for the first time.** An audit group gives you a full catalog of what is already non-compliant before you decide what to enforce. That is a far better starting point than turning on preventative policies and discovering the same backlog one blocked deployment at a time.

- **The teams hitting the policy may not be able to act on it.** A preventative policy is only useful if the person it blocks knows what to do next. Blocking a deployment on a violation a team lacks the context to resolve produces confusion and workarounds rather than compliance.

### Choosing an enforcement level

Match the [enforcement level](#enforcement-levels) to what the environment actually requires, rather than applying the same strictness everywhere.

In development, test, and other lower environments, advisory enforcement is usually the better default. The warnings still tell developers what the standards are, but nobody is blocked from trying something out. Strict controls in these environments are often unnecessary and sometimes counterproductive, since discouraging experimentation costs more than the risk it removes.

Reserve mandatory enforcement for environments that genuinely need strong controls: those holding sensitive data, serving production traffic, or falling within the scope of an audit. There, the cost of a violation reaching the environment is high enough to justify stopping the deployment.

Because enforcement levels are set per policy pack, and per policy within a pack, the usual way to express this is with a separate policy group for each environment tier: one group covering lower-environment stacks where the packs are advisory, and another covering production stacks where the critical packs are mandatory.

### Adopting policy across an organization

Rolling policy out in stages gives teams time to absorb each change and gives you a chance to find noisy rules before they block anyone:

1. **Start with an audit policy group.** Add the packs you are considering to an audit group covering your cloud accounts and stacks. Nothing is blocked, and after the first scan you have a complete inventory of what would be flagged. Work through the highest-severity findings before enforcing anything.

1. **Move to a preventative policy group with everything advisory.** Once the backlog is manageable, add the packs to a preventative group with every policy set to advisory. Developers begin seeing violations at deployment time, and you learn which rules are noisy or produce false positives without anyone being stopped.

1. **Make specific policies mandatory.** Promote policies to mandatory selectively, starting with the ones where a violation is genuinely unacceptable and the fix is well understood. Expand from there as teams build familiarity.

## Next steps

- [Create and configure policy groups](/docs/insights/policy/get-started/)
- [View and manage policy findings](/docs/insights/policy/policy-findings/)
- [Check policy pack runtime requirements](/docs/insights/policy/policy-packs/#runtime-requirements)
- [Write custom policy packs](/docs/insights/policy/policy-packs/authoring/)
- [Policy API reference](/docs/insights/policy/api-reference/)
