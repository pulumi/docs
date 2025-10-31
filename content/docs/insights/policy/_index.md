---
title: Policy
title_tag: "Pulumi Policy | Insights & Governance"
meta_desc: Enforce compliance and security policies across all cloud infrastructure with Pulumi Policy as Code—for both IaC stacks and discovered resources.
h1: Policy as Code
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
  - /docs/iac/guides/testing/property-testing/
  - /docs/guides/testing/property-testing/
  - /docs/using-pulumi/testing/property-testing/
  - /docs/iac/concepts/testing/property-testing/
  - /docs/insights/policy/core-concepts/
---

Pulumi Policy empowers you to set guardrails to enforce compliance across your entire cloud infrastructure—whether resources are managed by Pulumi IaC, provisioned by other tools like Terraform or CloudFormation, or created manually. Using Pulumi Policy, you can write flexible business and security policies that protect your organization.

{{% notes type="info" %}}
Policy as Code is implemented via [analyzer plugins](/docs/iac/concepts/plugins/#analyzer-plugins), which are installed automatically with the Pulumi CLI.
{{% /notes %}}

## How it works

Pulumi Policy uses a hierarchy of components to enforce compliance rules:

1. **Policies** are individual rules that validate infrastructure configuration (e.g., "S3 buckets must be private" or "VMs must use approved instance types"). Each policy can report violations or automatically remediate them.

1. **Policy packs** are versioned collections of related policies that you publish and manage together. You can use [pre-built policy packs](/docs/insights/policy/policy-packs/pre-built-packs/) for common compliance frameworks (CIS, PCI DSS, SOC 2) or [write custom packs](/docs/insights/policy/policy-packs/authoring/) in TypeScript, JavaScript, or Python.

1. **Policy groups** apply policy packs to specific stacks or cloud accounts. This lets you enforce stricter policies in production and more permissive policies in development environments. Learn more about [policy groups](/docs/insights/policy/policy-groups/).

### Enforcement modes

Policy enforcement works in two modes:

- **Preventative**: Validates Pulumi stack resources during `pulumi preview` and `pulumi up`, blocking deployments when violations are detected. Prevents non-compliant resources from being created.

- **Audit**: Continuously scans resources discovered through [Insights Discovery](/docs/insights/discovery/) to identify violations across all infrastructure—including resources created with Terraform, CloudFormation, or manually. Provides visibility without blocking operations.

Organization administrators configure which enforcement mode applies to each policy group. Policy violations can gate deployments (preventative) or appear in the [Policy Findings](/docs/insights/policy/policy-findings/) dashboard (audit). Policy remediations can automatically fix violations when enforcement level is set to remediate.

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

## Next steps

Choose your path based on your needs:

- **New to Pulumi Policy?** Start with the [Get Started guide](/docs/insights/policy/get-started/) to configure your first policy group and apply policies to stacks or cloud accounts.

- **Want ready-made compliance rules?** Browse [pre-built policy packs](/docs/insights/policy/policy-packs/pre-built-packs/) for CIS, PCI DSS, HITRUST, NIST, and other frameworks. Enable them directly from Pulumi Cloud with no code required.

- **Need custom policies?** Learn to [write custom policy packs](/docs/insights/policy/policy-packs/authoring/) in TypeScript, JavaScript, or Python. Create organization-specific rules tailored to your requirements.

- **Managing compliance?** View violations and track remediation progress in [Policy Findings](/docs/insights/policy/policy-findings/). Triage issues, assign owners, and monitor compliance trends across your organization.

- **Configuring discovered resources?** Visit the [Insights Get Started tutorial](/docs/insights/discovery/get-started/) for a detailed guide on audit policies for cloud resources discovered outside Pulumi.

For common questions and troubleshooting, see the [FAQ](/docs/insights/policy/faq/).
