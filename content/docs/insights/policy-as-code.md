---
title: Policy as Code
title_tag: Enforce Policy as Code on Discovered Resources | Pulumi Insights
h1: Enforce Policy as Code on Discovered Resources
meta_desc: This page describes how to Enforce Policy as Code on Discovered Resources with Pulumi Insights.
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  insights:
    name: Policy
    parent: insights-home
    weight: 15
    identifier: insights-policy
---

Policy as Code (PaC) for discovered resources extends [Pulumi Policy](/docs/iac/using-pulumi/crossguard/) policy enforcement capabilities beyond Pulumi managed infrastructure as code (IaC) to include resources discovered through Pulumi Insights. This feature enables organizations to maintain consistent compliance and governance across their entire cloud infrastructure, regardless of how resources were provisioned.

For a detailed overview of Pulumi Policy, including supported languages for policy authoring, policy enforcement levels, best practices, API workflows, and integrations, please refer to our comprehensive [Pulumi Policy documentation](/docs/iac/using-pulumi/crossguard/)

{{% notes type="info" %}}
For a detailed guide on how to get started with Pulumi Insights, including step-by-step instructions to configure your first policy, visit our [Pulumi Insights get started](/docs/insights/get-started/).
{{% /notes %}}

## How to Configure Policies

### Prerequisites

Before configuring policies, ensure the following requirements are met:

* Appropriate permissions to configure Policies
* One or more policy packs ([pre-built](/docs/insights/pre-built-packs/) or custom) added to the organization.
* One cloud account or Pulumi Stack
  * For audit policies: Cloud accounts connected to Pulumi Cloud.
  * For preventative policies: One or more Pulumi stacks.

### Configuration Steps

1. Navigate to the policies tab in the left navigation bar.
2. Here is the new policy management panel. Here, policy packs can be selected to add to the organization. Let's add one of the `pulumi-best-practices` policy packs.
3. Create a new policy group instead of using the default group.
4. Add the stack to the newly created policy group.
5. Add the newly added policy pack to the policy group.
6. Adjust the policy pack's configuration settings as needed.
7. Save the policy pack configuration.
8. Save the policy group to apply the changes.
9. The policy pack is now applied to the policy group with the configured settings.

{{< video title="Policy Management Configuration Demo" src="/docs/insights/assets/doc-video-2.mp4" autoplay="false" loop="true" controls="true" >}}

For more detailed information about policy configuration and the differences between preventative and audit policies, see [Preventative vs. Audit Policies](/docs/insights/preventative-vs-audit-policies/).

## Running Policies on discovered resources

Pulumi will evaluate each resource in your cloud account against the policies defined in your Policy Pack. Violations will show up on the **Policy Violations** page, which gives you a detailed view of any non-compliant resources.

Violation includes details about the resource and the reason for the violation, helping you quickly identify and address issues.

To learn more about choosing between preventative and audit enforcement approaches and when to use each one, see our guide on [Preventative vs. Audit Policies](/docs/insights/preventative-vs-audit-policies/).

## Policy violations

Policy Violations can be viewed in the Pulumi Cloud via the Policy Violations page. This page provides a centralized view of all violations across your organization, allowing you to filter and group them by various criteria such as Policy Pack, Project, Stack/Account, and Enforcement Level.

![Insights Policy Violations](/docs/insights/assets/insights-policy-violations.png)

Policy Violations can also be accessed programmatically via the Pulumi API for custom workflows and integrations.

For more details on using the API, refer to the [Pulumi API documentation](/docs/pulumi-cloud/cloud-rest-api/#list-policy-violations).
