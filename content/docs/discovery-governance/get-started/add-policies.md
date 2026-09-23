---
title: Add policies
title_tag: "Add policies | Discovery & governance"
h1: Add policies
meta_desc: Apply the Pulumi Best Practices policy pack to discovered resources as an audit policy and to Pulumi stacks as a preventative policy.
weight: 6
menu:
  discovery-governance:
    name: Add policies
    parent: dg-get-started
    weight: 6
aliases:
  - /docs/insights/get-started/add-policies/
  - /docs/insights/discovery/get-started/add-policies/
  - /docs/discovery-governance/discovery/get-started/add-policies/
---

Now that Discovery has scanned your cloud account, you can check the resources it found against policies. In this step, you'll apply the **Pulumi Best Practices** policy pack, a set of recommended security and governance controls that Pulumi publishes and maintains, in two ways:

- **Audit**: evaluate the resources Discovery found in your cloud account and report any violations.
- **Preventative**: evaluate a Pulumi stack's resources during `pulumi preview` and `pulumi up`, before anything is deployed.

You don't need to write any policy code. To write policies of your own later, see [Write a policy pack](/docs/discovery-governance/guides/write-a-policy-pack/).

{{< pulumi-cloud "policy-enforcement" />}}

## Prerequisites

- The Discovery account you connected in the previous steps.
- For the preventative section: a Pulumi stack that deploys AWS resources, and [Node.js](https://nodejs.org/) installed on the machine where you run `pulumi preview`. Pulumi's pre-built policy packs run on Node.js, whatever language your program uses.

## Find the Pulumi Best Practices pack

In the Pulumi Cloud console, navigate to **Governance** > **Policy configuration**. The **Policy Packs** tab lists every policy pack available to your organization: the ones you've published, and the pre-built packs that Pulumi publishes for your edition. You don't need to add Pulumi's packs to your organization first.

Select **Pulumi Best Practices** for AWS to see the policies it contains, or see its [reference page](/docs/reference/pre-built-policy-packs/pulumi-best-practices/aws/).

## Audit your discovered resources

An audit policy group evaluates the resources in your cloud accounts and reports violations without blocking anything.

{{% notes type="info" %}}
When you connected your account, the wizard added it to `default-accounts-policy-group`, which may already apply a policy pack to it. Creating your own audit group lets you choose exactly which packs apply. See [default policy groups](/docs/discovery-governance/concepts/policy-as-code/policy-groups/#default-policy-groups).
{{% /notes %}}

1. On the **Policy configuration** page, select the **Policy Groups** tab, then select **Create audit policy group**.
1. Enter a name, such as `best-practices-audit`.
1. Under **Entities**, select **Choose accounts** and select the Discovery account you connected, for example `production`.
1. Under **Policy Packs**, select **Select policy packs** and choose **Pulumi Best Practices**.
1. Keep the enforcement level at **Advisory**, then select **Save Policy Group**.

Policies evaluate each time Discovery scans the account. To see results now instead of waiting for the next scheduled scan, run a scan manually:

1. Navigate to **Resources** > **Discovery**.
1. Select the account, then select **Actions**, choose **Scan**, and select **Run**.

## Review policy findings

When the scan finishes, navigate to **Governance** > **Policy findings** to see the results. The page has three tabs:

- **Overview**: compliance metrics across your accounts and policy packs.
- **Compliance**: the failing resources for each policy, organized by policy group.
- **Issues**: each violation as a work item that you can filter by policy, severity, resource type, or account, assign to a teammate, or hand to Pulumi Neo to fix.

Each issue shows the resource that failed, the policy it violated, and how to fix it. For more, see [Review policy findings](/docs/discovery-governance/operations/policy-findings/).

## Prevent violations before deployment

Audit policies find problems after resources exist. A preventative policy group catches the same problems in Pulumi stacks before they're deployed.

1. Navigate to **Governance** > **Policy configuration**, and on the **Policy Groups** tab, select **Create preventative policy group**.
1. Enter a name, such as `best-practices-preventative`.
1. Under **Entities**, select **Choose stacks** and select the stack you want to govern.
1. Under **Policy Packs**, select **Select policy packs** and choose **Pulumi Best Practices**.
1. Keep the enforcement level at **Advisory**, then select **Save Policy Group**.

Now run a preview of that stack:

```bash
pulumi preview
```

Pulumi downloads the policy pack and evaluates it against the resources your program declares. Any violations appear in the preview output as advisory warnings, and the preview still completes. With the `mandatory` enforcement level, available in the Pro and Enterprise editions, a violation would stop `pulumi up` before any resource changes. To choose between the two, see [Choosing an enforcement level](/docs/discovery-governance/concepts/policy-as-code/policy-groups/#choosing-an-enforcement-level).

## Next steps

- [Policy groups](/docs/discovery-governance/concepts/policy-as-code/policy-groups/): how audit and preventative groups work, and how to roll policies out across an organization.
- [Use pre-built policy packs](/docs/discovery-governance/guides/pre-built-policy-packs/): the compliance-framework packs, such as CIS, PCI DSS, and HITRUST.
- [Write a policy pack](/docs/discovery-governance/guides/write-a-policy-pack/): write custom policies for your organization's own rules.

{{< get-started-stepper >}}
