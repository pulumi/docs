---
title: Policies
title_tag: "Pulumi Policies | Insights & Governance"
meta_desc: Enforce compliance and security across all cloud infrastructure using policy as code with Pulumi Policies—for both IaC stacks and discovered resources.
h1: Policies
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  insights:
    name: Policies
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
- /docs/insights/policy/core-concepts/
- /docs/iac/packages-and-automation/crossguard/core-concepts/
- /docs/iac/using-pulumi/crossguard/core-concepts/
---

Pulumi Policies enables you to implement policy as code across your entire cloud infrastructure. You define guardrails in code and apply them consistently across resources managed by Pulumi IaC, provisioned with Terraform or CloudFormation, or created manually. These codified business and security rules provide automated compliance protections for your organization.

## What is policy as code?

Policy as code applies software engineering practices to infrastructure policies. You write policies in programming languages and manage them alongside your infrastructure code, instead of manually configuring compliance rules through cloud provider consoles or maintaining policy documentation in wikis.

This approach provides several key benefits:

- **Cost control**: Define policies based on resource pricing to prevent expensive deployments before they happen. Set spending limits, identify unused resources, and enforce tagging for cost tracking and allocation across teams.

- **Compliance and security**: Enforce guardrails that prevent common misconfigurations like public S3 buckets, exposed databases, or overly permissive security groups. Apply consistent security standards across development, staging, and production environments.

- **Early validation**: Catch policy violations during `pulumi preview` before resources are created, not after deployment. This prevents non-compliant infrastructure from reaching production and reduces the time and cost of remediation.

- **Best practices as code**: Encode organizational standards and cloud provider best practices as versioned, testable policies. Share policy packs across teams to ensure consistent infrastructure patterns throughout your organization.

- **Integration with cloud-native tools**: Work alongside cloud provider features like AWS IAM Access Analyzer or AWS Organizations tag policies, combining Pulumi's policy enforcement with native cloud governance capabilities.

Pulumi Policies brings these policy as code benefits to both Pulumi-managed infrastructure and resources discovered from other tools or created manually.

{{% notes type="info" %}}
Policy as Code is implemented via [analyzer plugins](/docs/iac/concepts/plugins/#analyzer-plugins), which are installed automatically with the Pulumi CLI.
{{% /notes %}}

## How it works

Pulumi Policies uses a hierarchy of components to enforce compliance rules:

1. **Policies** are individual rules that validate infrastructure configuration (e.g., "S3 buckets must be private" or "VMs must use approved instance types").
1. **Policy packs** are versioned collections of related policies that you publish and manage together. You can use [pre-built policy packs](/docs/insights/policy/policy-packs/pre-built-packs/) for common compliance frameworks (CIS, PCI DSS, SOC 2) or [write custom packs](/docs/insights/policy/policy-packs/authoring/) in TypeScript, JavaScript, or Python.
1. **Policy groups** apply policy packs to specific stacks or cloud accounts. This lets you enforce stricter policies in production and more permissive policies in development environments. Learn more about [policy groups](/docs/insights/policy/policy-groups/).

### Enforcement modes

Policy enforcement works in two modes:

- **Preventative**: Validates Pulumi stack resources during `pulumi preview` and `pulumi up`, blocking deployments when violations are detected. Prevents non-compliant resources from being created.
- **Audit**: Continuously scans resources discovered through [Insights Discovery](/docs/insights/discovery/) to identify violations across all infrastructure—including resources created with Terraform, CloudFormation, or manually. Provides visibility without blocking operations.

Organization administrators configure which enforcement mode applies to each policy group. Policy violations can gate deployments (preventative) or appear in the [Policy Findings](/docs/insights/policy/policy-findings/) dashboard (audit).

## Local execution and Pulumi Cloud

### Local policy execution

The open source Pulumi CLI enables local policy execution:

- Apply policies locally using the `--policy-pack path/to/policy-pack` flag with `pulumi preview` or `pulumi up`
- Run open source policy packs or author your own custom policy packs
- Use with any backend (including the self-managed backend)

**Limitation:** Policy packs must be present on disk locally where you run Pulumi commands.

### Pulumi Cloud integration

Pulumi Cloud extends policy capabilities with centralized management and additional enforcement modes:

**Preventative policies:**

- Centralized management via [Policy Groups](/docs/insights/policy/policy-groups/)
- Access to Pulumi-authored pre-built policy packs for common compliance frameworks
- Support for open source policy packs by publishing them to your organization's private registry
- Automatic policy pack download to local cache
- No need to specify `--policy-pack` flag for each command
- Version control and rollback for policy packs
- Policy violation results visible in the Pulumi Cloud console

**Audit policies:**

- Continuously scan resources discovered through [Insights Discovery](/docs/insights/discovery/)
- Identify violations across all infrastructure—including resources created with Terraform, CloudFormation, or manually
- View violations in the [Policy Findings](/docs/insights/policy/policy-findings/) dashboard
- Monitor compliance trends across your organization
- Only available with Pulumi Cloud (cannot be used with the self-managed backend)

For more information about Pulumi plans and pricing, see the [Pricing page](/pricing/).

## Languages

Policies can be written in TypeScript/JavaScript (Node.js) or Python and can be applied to Pulumi stacks written in any language.

- **[TypeScript/JavaScript](/docs/reference/pkg/nodejs/pulumi/policy/)** - Stable
- **[Python](/docs/reference/pkg/python/pulumi_policy/)** - Stable
- **[Open Policy Agent (OPA)](/blog/opa-support-for-crossguard)** - Experimental
- **.NET** - [Future](https://github.com/pulumi/pulumi-policy/issues/229)
- **Go** - [Future](https://github.com/pulumi/pulumi-policy/issues/230)

## Next steps

Choose your path based on your needs:

- **New to Pulumi Policies?** Start with the [Get Started guide](/docs/insights/policy/get-started/) to configure your first policy group and apply policies to stacks or cloud accounts.
- **Want ready-made compliance rules?** Browse [pre-built policy packs](/docs/insights/policy/policy-packs/pre-built-packs/) for CIS, PCI DSS, HITRUST, NIST, and other frameworks. Enable them directly from Pulumi Cloud with no code required.
- **Need custom policies?** Learn to [write custom policy packs](/docs/insights/policy/policy-packs/authoring/) in TypeScript, JavaScript, or Python. Create organization-specific rules tailored to your requirements.
- **Managing compliance?** View violations and track remediation progress in [Policy Findings](/docs/insights/policy/policy-findings/). Triage issues, assign owners, and monitor compliance trends across your organization.
- **Configuring discovered resources?** Visit the [Insights Get Started tutorial](/docs/insights/discovery/get-started/) for a detailed guide on audit policies for cloud resources discovered outside Pulumi.

For common questions and troubleshooting, see the [FAQ](/docs/support/faq/policies).
