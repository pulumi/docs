---
title: Policies
title_tag: Policies | Pulumi Policies
h1: Policies
meta_desc: Learn what a Pulumi policy is, how resource and stack validation policies differ, and how enforcement levels, remediation, configuration, and metadata work.
menu:
  discovery-governance:
    name: Policies
    parent: dg-concepts-policy-as-code
    weight: 10
---

A policy is a single rule that your infrastructure must follow, such as "S3 buckets must not be public" or "every stack may declare at most three databases." You write policies in TypeScript, JavaScript, Python, or [OPA (Rego)](/docs/discovery-governance/guides/write-a-policy-pack/#opa), and group related policies into a [policy pack](/docs/discovery-governance/concepts/policy-as-code/policy-packs/). [Policy groups](/docs/discovery-governance/concepts/policy-as-code/policy-groups/) then decide which stacks and cloud accounts each pack applies to.

## Resource and stack validation policies

Every policy validates either one resource at a time or a whole stack at once.

- **Resource validation policies** run once for each resource. The policy receives the resource's type, name, and properties, and reports a violation if the resource breaks the rule. Most policies are resource validation policies: checks on encryption, public access, instance types, or required tags all look at one resource.
- **Stack validation policies** run once for each stack, and receive every resource in the stack together. Use them for rules that depend on more than one resource, such as limits on how many resources of a type a stack declares, or requirements about how resources relate to each other.

When a policy finds a problem, it reports a **violation** with a message that explains what's wrong. A policy that reports nothing has found the resource or stack compliant.

In a preventative evaluation, during `pulumi preview` or `pulumi up`, a policy sees the properties your program declares, before any resource is created. Properties that the cloud provider computes, such as IDs and other outputs, aren't known yet. In an audit evaluation, a policy sees the current state of resources that already exist. For when each kind of evaluation happens, see [Policy as code](/docs/discovery-governance/concepts/policy-as-code/#iac-managed-and-discovered-resources).

## Enforcement levels

Each policy has an enforcement level that decides what happens when it reports a violation:

| Level | Effect |
|-------|--------|
| `advisory` | The violation is reported as a warning, and the deployment continues. |
| `mandatory` | The violation stops the deployment. |
| `remediate` | The policy fixes the resource automatically, and the deployment continues with the corrected resource. |
| `disabled` | The policy doesn't run. |

A policy pack sets a default level for its policies, and each policy can override it. The people who apply a pack can also override the level for any policy through [configuration](#configuration), without changing the pack's code. Audit evaluations report violations but never block anything, whatever the level.

The `mandatory` and `remediate` levels require particular editions of Pulumi Cloud when policies are managed centrally. See [pricing](/pricing/#policy-enforcement-modes).

## Remediation

A remediation policy doesn't just report a problem: it returns corrected properties for the resource, and Pulumi deploys the corrected resource instead of the one the program declared. For example, a remediation policy could turn on storage encryption for a database that the program left unencrypted.

Only resource validation policies written in TypeScript, JavaScript, or Python can remediate. A stack validation policy set to `remediate` is treated as `mandatory`, and OPA policies report violations without fixing them. To write one, see [Remediating policy violations](/docs/discovery-governance/guides/write-a-policy-pack/#remediating-policy-violations).

## Configuration

A policy can declare configuration parameters, so one policy pack can serve teams with different requirements. For example, a policy that limits instance sizes can take the maximum size as a parameter instead of hard-coding it. The people who apply the pack set the values, and can also override each policy's enforcement level. See [Configuring policy packs](/docs/discovery-governance/guides/write-a-policy-pack/#configuring-policy-packs).

## Metadata

Besides its validation logic, a policy carries fields that describe it: a unique name and a description, and optionally a display name, a severity, remediation steps, a link to more information, tags, and the compliance framework control it implements. Pulumi Cloud uses these fields when it shows policies and their violations, for example to sort findings by severity. For every field and how to set it in each language, see the [policy fields reference](/docs/discovery-governance/reference/policy-fields/).

## Next steps

- [Use pre-built policy packs](/docs/discovery-governance/guides/pre-built-policy-packs/) to apply policies that Pulumi maintains, with no code to write.
- [Write a policy pack](/docs/discovery-governance/guides/write-a-policy-pack/) in TypeScript, JavaScript, Python, or OPA.
