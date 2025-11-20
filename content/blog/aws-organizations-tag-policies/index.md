---
title: "Enforce AWS Organizations Tag Policies with Pulumi"
date: 2025-11-21T00:00:03-08:00
authors:
  - alejandro-cotroneo
meta_desc: "Pulumi partners with AWS to bring AWS Organizations Tag Policies validation to infrastructure as code, enforcing mandatory tagging requirements."
allow_long_title: true
meta_image: "meta.png"
tags:
  - aws
  - pulumi-service
  - policy-as-code
  - crossguard
  - features
  - governance
  - compliance
---

Tags are the foundation of cloud governance, enabling cost allocation, ownership tracking, compliance reporting, and automation across your AWS infrastructure. Yet missing or inconsistent tags remain one of the most common governance challenges. Manual tag enforcement is error-prone, and discovering missing tags after deployment means your cost reports and compliance audits are already operating with incomplete data.

Today, we're excited to announce a new pre-built policy pack created in partnership with AWS: **AWS Organizations Tag Policies**. This pack validates your infrastructure as code against tag policies configured in AWS Organizations, blocking deployments when required tags are missing—shifting tag governance left into your development workflow. This partnership brings together AWS's centralized tag policy management with Pulumi's policy-as-code framework, so you can define your tag requirements once in AWS Organizations and enforce them consistently across all your infrastructure as code deployments.

<!--more-->

## How it works

The AWS Organizations Tag Policies policy pack integrates directly with your AWS Organization's tag policies. Your tag requirements live in AWS Organizations as the single source of truth; you don't need to maintain separate policy configuration in Pulumi or write custom policy code.

When you run `pulumi up`, the policy pack retrieves your tag policy requirements from AWS Organizations and validates that every resource has the required tags. Configure the pack in advisory mode to warn about missing tags, or mandatory mode to block non-compliant deployments entirely.

Start by enabling the pack in advisory mode to surface tagging violations in Pulumi Cloud's [Policy Findings](/docs/insights/policy/policy-findings/) hub without blocking deployments. This collaborative workspace allows your team to triage, prioritize, and systematically remediate missing tags. Once your infrastructure is compliant, switch to mandatory mode to prevent future non-compliant deployments.

## Getting started

The pack works with both AWS Classic and AWS Native Pulumi providers, covering the full range of taggable AWS resources. To get started:

1. **Configure tag policies** in AWS Organizations following the [AWS Tag Policies documentation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html).
1. **Grant required permissions** by adding the `resourcegroupstaggingapi:ListRequiredTags` permission to the IAM role or user that runs your Pulumi deployments.
1. **Enable the pack in Pulumi Cloud**:
   1. From within your organization, navigate to the **Policies** tab
   1. Under Policy Packs, select the **Available** tab
   1. Select **AWS Organizations Tag Policies** and select **Add to organization**
   1. From the Organizations tab, apply the policy to a Policy Group
1. **Configure enforcement level**: Set to advisory for warnings or mandatory to block non-compliant deployments.

Within minutes, every Pulumi deployment in your organization will validate tag compliance, ensuring that no resources are created without required tags.

## Try it today

The AWS Organizations Tag Policies policy pack is now available to all Pulumi Team and Enterprise customers.

- [View the documentation](/docs/reference/pre-built-policy-packs/aws-organizations-tag-policies/aws/)
- [Learn about tag policies in AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html)
- [Sign up for Pulumi Cloud](https://app.pulumi.com/signup) if you're new to Pulumi
- [Join the Community Slack](https://slack.pulumi.com/) to share feedback

We're excited to partner with AWS on this capability and help organizations proactively enforce tag governance. Give it a try and let us know what you think!
