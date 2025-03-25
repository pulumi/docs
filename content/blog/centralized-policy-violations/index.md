---
title: "Introducing the Centralized Policy Violations Page: Streamlined Compliance
  Management"
allow_long_title: true
date: 2024-08-26T09:00:00-07:00
draft: false
meta_desc: The new Centralized Policy Violations page in Pulumi offers enhanced visibility
  and control by consolidating all policy violations.
meta_image: meta.png
authors:
  - meagan-cojocar
tags:
  - releases
  - policy
search:
  keywords:
    - compliance
    - violations
    - policy
    - centralized
    - page
    - streamlined
    - consolidating
---

We’re excited to introduce a new centralized Policy Violations destination in Pulumi Cloud to simplify policy management and compliance. This powerful addition provides a comprehensive view of all policy violations across your organization, helping you maintain visibility and control over your infrastructure.

Pulumi’s Policy as Code (PaC) feature, [CrossGuard](/docs/using-pulumi/crossguard), allows you to define and enforce policies for your infrastructure using familiar programming languages. By integrating these policies directly into your infrastructure code, you can automate compliance checks, gate deployments to ensure security best practices, and maintain governance across all your providers.

**Note:** Pulumi CrossGuard is available in the Pulumi Business Critical edition.

## Centralized Policy Violations: Why It Matters

Ensuring compliance across multiple projects and stacks can be challenging in large and complex environments. The new Policy Violations page addresses this challenge by consolidating all violations into one place. This allows you to quickly assess the overall compliance of your infrastructure and separate signal from noise. This streamlined view saves time and reduces the risk of missing critical issues.

By having all violations on a single page, organization admins can efficiently prioritize remediation efforts and identify patterns in non-compliance. They can triage the violations and send the critical ones to teams to resolve.

{{< video title="Centralized Policy Violations Overview" src="policy-violations.mp4" autoplay="true" loop="true" >}}

## Grouping Violations: Enhanced Insights Across Multiple Dimensions

One of the standout features of the new page is the ability to group violations by various fields, including Policy Pack, Policy, Project, Stack, Resource, and more! This flexibility allows you to gain deeper insights into your infrastructure’s compliance landscape.

Grouping violations based on these fields enables you to answer critical questions such as:

- **Policy Pack and Policy**: Which Policy Packs and Policies have the most frequent violations?
- **Project and Stack**: Are there specific projects or stacks that are more prone to compliance issues?
- **Resource**: Which resources have failed policies?
- **Reason and Enforcement Level**: What are the common reasons for violations, and how critical are they?
- **Violation Date**: When are violations most likely to occur, and are there patterns over time?

These insights empower you to refine your policies, address the most problematic areas, and improve your overall compliance strategy.

## Accessing Policy Violations via API

To further enhance your compliance management, you can leverage the Pulumi Cloud REST API to programmatically access policy violations, trigger automated workflows, and import data into your analytics systems. The API can automate the monitoring of your infrastructure’s compliance status, ensuring that policy violations are promptly detected and addressed. This capability enables you to integrate Pulumi's compliance data with your existing tools, creating a seamless and efficient compliance management process.

For example, you can use the following command to retrieve a list of policy violations:

```bash
curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  https://api.pulumi.com/api/orgs/{organization}/policyresults/violations
```

For more details on how to integrate this API into your workflow, visit the [Pulumi API documentation](/docs/pulumi-cloud/cloud-rest-api/#list-policy-violations).

## Streamlining Compliance with Future Enhancements

Centralizing and surfacing policy violations is just the beginning. Future updates will include additional capabilities like advanced search and filtering, making it even easier to manage violations. We’re committed to providing the tools you need to keep your infrastructure secure, compliant, and running smoothly.

## Wrapping It Up

The Centralized Policy Violations Page to Pulumi is a significant step forward in simplifying policy management and enhancing compliance. By bringing all violations into a single, easily accessible view, we’re making it easier for admins to maintain control and ensure their infrastructure remains secure and compliant.

Try out this new feature today and experience the benefits of streamlined compliance management. For more information, visit our [Policy Violations documentation](/docs/using-pulumi/crossguard/policy-violations/). To use this feature, [start a trial](https://app.pulumi.com/signup) or [contact sales](/contact/) to get a demo or to trial Policy as Code.
