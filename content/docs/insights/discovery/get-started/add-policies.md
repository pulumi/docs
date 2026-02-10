---
title: Using Insights Policies
title_tag: "Policies | Pulumi Insights"
h1: "Pulumi Insights: Using Policies and Policy Remediation"
meta_desc: Learn how to use Pulumi Policy policies to evaluate cloud resources discovered through Pulumi Insights account discovery.
weight: 6
menu:
  insights:
    name: Add Policies
    parent: insights-discovery-get-started
    identifier: insights-get-started-policies
    weight: 6
aliases:
  - /docs/insights/get-started/add-policies/
---

Now that you have scanned your cloud accounts and discovered resources, you can use Pulumi Policy policies to evaluate those resources for compliance, security, and adherence to best practices. Insights runs policy evaluations automatically whenever it discovers new or changed resources, providing continuous visibility into your infrastructure's compliance status.

## Creating a policy pack

First, we'll create a policy pack using the Pulumi CLI. [Policy packs](/docs/insights/policy/policy-packs/) are collections of rules that can evaluate your cloud resources against specific criteria. In this example we'll show you how to use one of Pulumi's policy templates that enforces specific compliance for your AWS resources, in this case an S3 bucket.

{{% notes type="info" %}}
To see the full list of available policy pack templates, check out the [`pulumi/templates-policy`](https://github.com/pulumi/templates-policy) GitHub repository.
{{% /notes %}}

Open your terminal and run:

```bash
pulumi policy new aws-typescript
```

This will initialize your project, creating the necessary files for Pulumi to use as a policy, including module dependencies to the providers that will let us interact with AWS resources.

This template sets up an example resource policy that prevents S3 buckets from being publicly readable:

```typescript
import * as aws from "@pulumi/aws";
import { PolicyPack, validateResourceOfType } from "@pulumi/policy";

new PolicyPack("aws-typescript", {
    policies: [{
        name: "s3-no-public-read",
        description: "Prohibits setting the publicRead or publicReadWrite permission on AWS S3 buckets.",
        enforcementLevel: "mandatory",
        validateResource: validateResourceOfType(aws.s3.Bucket, (bucket, args, reportViolation) => {
            if (bucket.acl === "public-read" || bucket.acl === "public-read-write") {
                reportViolation(
                    "You cannot set public-read or public-read-write on an S3 bucket. " +
                    "Read more about ACLs here: https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html");
            }
        }),
    }],
});
```

Run the following command to publish your policy pack to your Pulumi organization:

```bash
pulumi policy publish
```

{{% notes type="info" %}}
Policy Versions: Pulumi Cloud tracks published policy packs by version. When a policy pack is published, it will automatically receive a monotonically-increasing version number by Pulumi Cloud. The policy pack version can be specified in the package.json file for TypeScript/JavaScript (Node.js) packs and in the PulumiPolicy.yaml file for Python packs. Published policy packs are immutable, meaning that a version number can only be published to one time. Once published, the version can never be used by that policy pack again.
{{% /notes %}}

## Add a policy pack to an account

With your policy pack published, you'll need to create a Policy Group that associates your Insights account with a policy pack.

1. In the Pulumi Cloud console, navigate to **Policies** under the **Pulumi Insights** section.

    ![Insights Policies - New Policy Pack](/docs/insights/assets/policy-groups.png)

1. Click **Create policy group** and provide a descriptive name, such as "s3-security-policy-group". Then click **Add policy group**

1. Click **Add Policy Pack** to configure enforcement:

    Select your newly published policy pack from the dropdown and choose the version you want to enforce.

    Here you can configure the enforcement level at either a global level for all, or a granular level for each individual policy check.

    We'll start with an enforcement level of **advisory** then click **Enable** to confirm your settings.

    ![Insights Policies - New Policy Pack](/docs/insights/assets/enable-policy-pack.png)

1. Now add your insights account to the policy group. Click **Add accounts** and type the name of the account you want to include for Insights policies. (e.g. insights-aws-account/us-west-2) Finally, click **Add account to policy group**

{{% notes type="info" %}}
By default, all accounts and stacks are automatically added to the `default-policy-group`.
{{% /notes %}}

![Insights Policies - New Policy Pack](/docs/insights/assets/new-policy-pack.png)

{{< notes type="info" >}}
When adding accounts to a policy group, make sure to include both the parent account name and the region if you want to evaluate region-specific resources. For example: `insights-aws-account/us-west-2`
{{< /notes >}}

## Running a policy scan

With policies configured, you can now evaluate your discovered resources against these rules:

1. Navigate to the **Accounts** section
2. Select the regional account you want to evaluate (e.g., `us-west-2`)
3. Click **Actions** then select **Scan**
4. Confirm by clicking **Scan**

## Reviewing policy issues

As the scan progresses, you can monitor policy compliance in real-time through the **Policy Findings** page in the Pulumi Cloud Console. This view provides several ways to analyze your compliance status:

![Insights Policies - Policy Findings](/docs/insights/assets/policy-findings.png)

The Policy Findings page includes three tabs:

- **Overview:** View high-level compliance metrics and a heatmap showing compliance across accounts and policy packs
- **Compliance:** Review policy-centric view showing failing resources per policy, organized by policy group
- **Issues:** Manage individual policy violations as work items with status tracking, priority assignment, and remediation workflows

Filter policy issues by:

- Policy pack
- Policy
- Severity
- Priority
- Status
- Assigned team member
- Resource type
- Cloud account

Each issue provides detailed information about:

- The specific resource that triggered the violation
- Which policy rule was violated
- Policy pack, policy group, and enforcement level
- Contextual information to help understand why the resource is non-compliant

{{< get-started-stepper >}}
