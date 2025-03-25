---
title: Policy as Code
title_tag: Enforce Policy as Code on Discovered Resources | Pulumi Insights
h1: Enforce Policy as Code on Discovered Resources
meta_desc: This page describes how to Enforce Policy as Code on Discovered Resources
  with Pulumi Insights.
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  insights:
    parent: insights-home
    weight: 5
search:
  keywords:
    - policy
    - code
    - discovered
    - insights
    - enforce
    - describes
    - page
---

Policy as Code (PaC) for discovered resources extends [Pulumi Crossguard](/docs/iac/using-pulumi/crossguard/) policy enforcement capabilities beyond Pulumi managed infrastructure as code (IaC) to include resources discovered through Pulumi Insights. This feature enables organizations to maintain consistent compliance and governance across their entire cloud infrastructure, regardless of how resources were provisioned.

For a detailed overview of CrossGuard, including supported languages for policy authoring, policy enforcement levels, best practices, API workflows, and integrations, please refer to our comprehensive [CrossGuard documentation](/docs/iac/using-pulumi/crossguard/)

{{% notes type="info" %}}
For a detailed guide on how to get started with Pulumi Insights, including step-by-step instructions to configure your first policy, visit our [Pulumi Insights get started](/docs/insights/get-started/).
{{% /notes %}}

## Configure Policy as Code for discovered resources

To apply policies to your discovered resources, you first need to set up a Policy Group. A Policy Group in Pulumi enforces policies across a group of stacks and accounts in your organization. Each Policy Group can contain multiple of each stack and accounts, and you can assign multiple Policy Packs to these groups.

On the **Policies** page, under Pulumi Insights, you can click the **New policy pack** button to enable a new Policy Pack for use with your Insights accounts.

![Insights Policies - New Policy Pack](/docs/insights/assets/create-policy-group.png)

If the selected Policy Pack has configuration, a dialog will appear for you to enter the configuration such as enforcement level.

![Insights Policies - Policy Pack configuration](/docs/insights/assets/enable-policy-pack.png)

Once your Policy Group is set up, you can add discovered accounts to the group, which will ensure that the resources in those accounts are evaluated against the policies in the group.

Click **Add accounts** and the name of the account you want to include for Insights policies. (e.g. insights-aws-account/us-west-2) Finally, click **Add account to policy group**.

{{% notes type="info" %}}
By default, all accounts and stacks are automatically added to the `default-policy-group`.
{{% /notes %}}

## Running Policies on discovered resources

Pulumi will evaluate each resource in your cloud account against the policies defined in your Policy Pack. Violations will show up on the **Policy Violations** page, which gives you a detailed view of any non-compliant resources.

Violation includes details about the resource and the reason for the violation, helping you quickly identify and address issues

## Policy violations

Policy Violations can be viewed in the Pulumi Cloud via the Policy Violations page. This page provides a centralized view of all violations across your organization, allowing you to filter and group them by various criteria such as Policy Pack, Project, Stack/Account, and Enforcement Level.

![Insights Policy Violations](/docs/insights/assets/insights-policy-violations.png)

Policy Violations can also be accessed programmatically via the Pulumi API for custom workflows and integrations.

For more details on using the API, refer to the [Pulumi API documentation](/docs/pulumi-cloud/cloud-rest-api/#list-policy-violations).
