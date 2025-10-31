---
title: Policy
title_tag: "Pulumi Policy as Code | Insights & Governance"
meta_desc: Enforce compliance and security policies across all cloud infrastructure with Pulumi Policy as Code—for both IaC stacks and discovered resources.
h1: Policy as code
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  insights:
    name: Policy
    parent: insights-home
    weight: 20
    identifier: insights-policy
aliases:
  - /docs/guides/crossguard/
  - /policy-as-code/
  - /docs/using-pulumi/crossguard/
  - /docs/iac/packages-and-automation/crossguard/
  - /docs/iac/using-pulumi/crossguard/
  - /docs/iac/crossguard/
  - /docs/insights/policy-as-code/
---

Pulumi Policy empowers you to set guardrails to enforce compliance across your entire cloud infrastructure—whether resources are managed by Pulumi IaC, provisioned by other tools like Terraform or CloudFormation, or created manually. Using Policy as Code, you can write flexible business and security policies that protect your organization.

{{% notes type="info" %}}
Policy as Code is implemented via [analyzer plugins](/docs/iac/concepts/plugins/#analyzer-plugins), which are installed automatically with the Pulumi CLI.
{{% /notes %}}

Policy enforcement works in two modes:

- **Preventative policies**: Block non-compliant resources before deployment, enforcing compliance on Pulumi stack updates
- **Audit policies**: Scan existing resources discovered through [Insights Discovery](/docs/insights/discovery/) to identify violations across all infrastructure

Organization administrators can apply policies to specific stacks and cloud accounts. When policies execute during deployments, violations can gate or block updates from proceeding. Policy remediations also allow you to automatically fix violations.

Learn more about [Policy as Code core concepts](/docs/insights/policy/deprecated/core-concepts/).

## Languages

Policies can be written in TypeScript/JavaScript (Node.js) or Python and can be applied to Pulumi stacks written in any language.

|                                                        | Language                                                                     | Status                                                                                                                                        |
|--------------------------------------------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| <img src="/logos/tech/logo-ts.png" class="h-10" />     | [TypeScript](/docs/reference/pkg/nodejs/pulumi/policy/)      | Stable                                                                                                                                        |
| <img src="/logos/tech/logo-js.png" class="h-10" />     | [JavaScript](/docs/reference/pkg/nodejs/pulumi/policy/)      | Stable                                                                                                                                        |
| <img src="/logos/tech/logo-python.png" class="h-10" /> | [Python](/docs/reference/pkg/python/pulumi_policy/)          | Stable                                                                                                                                        |
| <img src="/logos/tech/logo-opa.png" class="h-10" />    | [Open Policy Agent (OPA)](/blog/opa-support-for-crossguard) | Preview                                                                                                                                       |
| <img src="/logos/tech/dotnet.png" class="h-10" />      | .NET                                                                         | [Future](https://github.com/pulumi/pulumi-policy/issues/229) |
| <img src="/logos/tech/logo-golang.png" class="h-10" /> | Go                                                                           | [Future](https://github.com/pulumi/pulumi-policy/issues/230) |

## Getting started

To get started with Pulumi Policy, [download and install Pulumi](/docs/install/), then try the [Policy Get Started guide](/docs/insights/policy/get-started/).

For a detailed guide on configuring policies for discovered resources, visit the [Insights Get Started tutorial](/docs/insights/discovery/get-started/).

## How to configure policies

### Prerequisites

Before configuring policies, ensure:

- Appropriate permissions to configure policies
- One or more policy packs ([pre-built](/docs/insights/policy/policy-packs/pre-built-packs/) or custom) added to the organization
- One cloud account or Pulumi Stack:
  - For audit policies: Cloud accounts connected to Pulumi Cloud
  - For preventative policies: One or more Pulumi stacks

### Configuration steps

1. Navigate to the policies tab in the left navigation bar
2. Select policy packs to add to the organization (e.g., `pulumi-best-practices`)
3. Create a new policy group or use the default group
4. Add stacks or accounts to the policy group
5. Add policy packs to the policy group
6. Adjust policy pack configuration settings as needed
7. Save the configuration

{{< video title="Policy Management Configuration Demo" src="/docs/insights/assets/doc-video-2.mp4" autoplay="false" loop="true" controls="true" >}}

For more details about policy configuration and enforcement modes, see [Policy Groups](/docs/insights/policy/policy-groups/).

## Policy findings

Policy findings provide a centralized hub for managing compliance across your organization. The **Policy Findings** page in Pulumi Cloud offers three distinct views:

- **Overview tab:** High-level compliance metrics and trends for your organization
- **Compliance tab:** Policy-centric view for auditing and compliance reporting
- **Issues tab:** Collaborative workspace for triaging, assigning, and resolving policy issues with support for priorities, assignments, and lifecycle management

For organizations using Pulumi Neo, policy issues can be automatically remediated through AI-powered code generation that creates pull requests with the necessary fixes.

![Policy Findings](/images/docs/guides/crossguard/policy-findings-overview.png)

Learn more about [Policy Findings](/docs/insights/policy/policy-findings/) or access them programmatically via the [Policy Results API](/docs/reference/cloud-rest-api/policy-results/).

## Compliance ready policy packs

Pulumi provides comprehensive predefined policies for AWS, Azure, Google Cloud, and Kubernetes through [pre-built policy packs](/docs/insights/policy/policy-packs/pre-built-packs/). These policies help you enforce security frameworks like CIS, PCI DSS, and SOC 2 with minimal configuration.

## AWSGuard

[AWSGuard](/docs/insights/policy/deprecated/awsguard/) is a configurable policy library that codifies best practices for AWS resources. You can adopt and customize AWSGuard policies in your own policy packs to enforce AWS-specific compliance requirements.

## Configuring policy packs

Policy packs support configuration to make them reusable across your organization. By default, fields like enforcement level are configurable, and you can specify custom variables alongside each policy. Learn more about [configurable policy packs](/docs/insights/policy/policy-packs/).

## Examples

Example policy packs for different cloud providers:

{{< chooser language "typescript,python" >}}

{{% choosable language typescript %}}

- [AWS](https://github.com/pulumi/examples/tree/master/policy-packs/aws-ts)
- [Azure](https://github.com/pulumi/examples/tree/master/policy-packs/azure-ts)
- [Google Cloud](https://github.com/pulumi/examples/tree/master/policy-packs/gcp-ts)
- [Kubernetes](https://github.com/pulumi/examples/tree/master/policy-packs/kubernetes-ts)

{{% /choosable %}}
{{% choosable language python %}}

- [AWS](https://github.com/pulumi/examples/tree/master/policy-packs/aws-python)
- [Azure](https://github.com/pulumi/examples/tree/master/policy-packs/azure-python)
- [Google Cloud](https://github.com/pulumi/examples/tree/master/policy-packs/gcp-python)
- [Kubernetes](https://github.com/pulumi/examples/tree/master/policy-packs/kubernetes-python)

{{% /choosable %}}

{{< /chooser >}}

## FAQ

Get answers to [Frequently Asked Questions](/docs/insights/policy/faq/) about Pulumi Policy.
