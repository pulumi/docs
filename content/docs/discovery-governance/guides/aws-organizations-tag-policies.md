---
title_tag: "AWS Organizations Tag Policies | Pulumi Policy"
meta_desc: Enforce AWS Organizations Tag Policies on infrastructure as code, blocking deployments with missing required tags.
title: Enforce AWS Organizations tag policies
h1: Enforce AWS Organizations tag policies
menu:
  discovery-governance:
    name: Enforce AWS Organizations tag policies
    parent: dg-guides
    weight: 70
aliases:
- /docs/insights/policy/integrations/aws-organizations-tag-policies/
- /docs/discovery-governance/policy/integrations/aws-organizations-tag-policies/
pulumi_cloud_feature: pre-built-policy-packs
---

## Overview

The [AWS Organizations Tag Policies policy pack](/docs/reference/pre-built-policy-packs/aws-organizations-tag-policies/aws/) is a pre-built policy pack that integrates Pulumi with AWS Organizations. This integration validates your infrastructure as code against Tag Policies configured in AWS Organizations, blocking deployments when required tags are missing. For more information about enforcing tag policies with AWS Organizations Tag Policies, see the [AWS documentation](https://docs.aws.amazon.com/organizations/latest/userguide/enforce-required-tag-keys-iac.html).

## How it works

1. **Configure tag policies in AWS Organizations**: Define your required tags using tag policies, specifying which tags are mandatory for which resource types. The pack reads all tag requirements specified by the `report_required_tag_for` field in your tag policy configuration.
1. **Enable the pack in Pulumi Cloud**: Add the AWS Organizations Tag Policies pack to your Pulumi organization, and configure a policy group. The pack supports two enforcement levels: advisory mode (warns about missing tags without blocking deployments) and mandatory mode (blocks non-compliant deployments).
1. **Validation during deployment**: When you run `pulumi up`, the policy pack retrieves your tag policy requirements from AWS and validates that resources have the specified tags.
1. **Enforcement levels**: Start in advisory mode to surface violations without blocking deployments. All policy violations are displayed in the Pulumi Cloud [Policy Findings](/docs/discovery-governance/operations/policy-findings/) page for monitoring and tracking, enabling a controlled migration to compliance. Once your Pulumi programs are compliant, switch to mandatory mode to block any future non-compliant deployments.

The pack uses AWS Organizations tag policies as the source of truth. Tag requirements are managed in AWS, not in Pulumi configuration.

## Prerequisites

Before using this policy pack, complete the following setup in AWS:

### Configure tag policies in AWS Organizations

Tag policies must be configured in your AWS Organization to define which tags are required for your resources. For detailed instructions, see the [AWS Organizations Tag Policies documentation](https://docs.aws.amazon.com/organizations/latest/userguide/enforce-required-tag-keys-iac.html).

### Grant required permissions

The AWS credentials used by your Pulumi stack must have permission to call the AWS Resource Groups Tagging API. Add the following IAM policy to the role or user running Pulumi deployments:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "resourcegroupstaggingapi:ListRequiredTags",
      "Resource": "*"
    }
  ]
}
```

The policy pack will use the same AWS credentials configured for your stack to fetch the required tags configuration.

## Enabling the pack

To enable this policy pack for your organization:

1. From within your organization, navigate to the **Policies** tab
1. Under Policy Packs, select the **Available** tab
1. Select **AWS Organizations Tag Policies** and select **Add to organization**
1. From the Organizations tab, apply the policy to a Policy Group to enforce tag validation

For more information about enabling policy packs, see [Use pre-built policy packs](/docs/discovery-governance/guides/pre-built-policy-packs/).

## Policy and supported resources

The pack contains one policy, `aws-tag-policies-compliance-validation`, and works with both the AWS (`pulumi/aws`) and AWS Native (`pulumi/aws-native`) providers. For the policy's default enforcement level and severity, and for the full mapping of AWS tag policy resource types to Pulumi resource types, see the [AWS Organizations Tag Policies pack reference](/docs/reference/pre-built-policy-packs/aws-organizations-tag-policies/aws/).

## Related documentation

- [Policy as Code get started guide](/docs/discovery-governance/get-started/enforce-policy-as-code/)
- [Pre-Built Policy Packs](/docs/discovery-governance/guides/pre-built-policy-packs/)
