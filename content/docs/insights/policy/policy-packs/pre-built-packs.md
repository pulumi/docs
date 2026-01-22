---
title: Pre-Built Packs
title_tag: "Pre-built policy packs"
h1: Pre-Built Packs
meta_desc: Use pre-built policy packs to apply industry-standard compliance and security controls to your cloud infrastructure as code.
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  insights:
    parent: policy-packs
    weight: 10
aliases:
  - /docs/insights/policy/policy-as-code/pre-built-packs/
  - /docs/pulumi-cloud/insights/pre-built-packs/
  - /docs/iac/crossguard/pre-built-packs/
  - /docs/insights/pre-built-packs/
---

Pulumi Cloud comes with pre-built policy packs that codify best practices for common security and compliance frameworks. These packs allow you to quickly evaluate your organization's compliance posture and "shift left," embedding continuous compliance directly into your IaC workflow. Proactively enforce controls, reduce misconfiguration risks before deployment, and help your organization meet its regulatory obligations with confidence.

### Why use pre-built packs?

- **Accelerate Adoption:** Implement comprehensive governance controls in minutes without having to author policies from scratch.
- **Leverage Expert Knowledge:** Packs are authored and maintained by Pulumi, incorporating deep expertise in cloud security best practices.
- **Enforce Consistency:** Apply a single, version-controlled policy pack across your entire organization to ensure all teams and projects adhere to the same standards.
- **Proactive Risk Reduction:** Catch common security risks and compliance violations during `pulumi preview`, long before they reach your production environments.

### Available policy packs

The following pre-built policy packs are available out of the box in Pulumi Cloud. Availability varies by plan—see [Pricing](/pricing/) for details.

| Framework | Supported Cloud Providers | Description |
| ----- | ----- | ----- |
| **CIS 8.1** | [AWS](/docs/reference/pre-built-policy-packs/cis/aws/), [Azure](/docs/reference/pre-built-policy-packs/cis/azure/), [Google Cloud](/docs/reference/pre-built-policy-packs/cis/google-cloud/) | Enforces CIS 8.1 controls to help organizations implement industry-recognized security best practices and benchmarks across multiple cloud providers. |
| **CIS Kubernetes** | [AWS (EKS)](/docs/reference/pre-built-policy-packs/cis-kubernetes/aws/), [Azure (AKS)](/docs/reference/pre-built-policy-packs/cis-kubernetes/azure/), [Google Cloud (GKE)](/docs/reference/pre-built-policy-packs/cis-kubernetes/google-cloud/) | Enforces CIS Kubernetes Benchmark controls for managed Kubernetes services, helping organizations secure their container orchestration platforms with industry-recognized best practices. |
| **HITRUST CSF 11.5** | [AWS](/docs/reference/pre-built-policy-packs/hitrust/aws/), [Azure](/docs/reference/pre-built-policy-packs/hitrust/azure/), [Google Cloud](/docs/reference/pre-built-policy-packs/hitrust/google-cloud/) | Provides predefined controls that align cloud resources with HITRUST CSF requirements, helping organizations enforce security and compliance baselines across multiple providers. |
| **NIST SP 800-53** | [AWS](/docs/reference/pre-built-policy-packs/nist/aws/) | Enforces NIST SP 800-53 rev. 5 security and privacy controls for AWS resources, helping federal agencies and organizations meet rigorous compliance requirements. |
| **PCI DSS v4.0.1** | [AWS](/docs/reference/pre-built-policy-packs/pci-dss/aws/) | Enforces PCI DSS v4.0.1 compliance controls for AWS resources, ensuring payment card data security and helping organizations meet payment card industry standards. |
| **Pulumi Best Practices** | [AWS](/docs/reference/pre-built-policy-packs/pulumi-best-practices/aws/), [Azure](/docs/reference/pre-built-policy-packs/pulumi-best-practices/azure/), [Google Cloud](/docs/reference/pre-built-policy-packs/pulumi-best-practices/google-cloud/) | Offers a foundational set of recommended governance and security controls, serving as a strong starting point for organizations seeking comprehensive security coverage. |
| **AWS Organizations Tag Policies** | [AWS and AWS-Native](/docs/reference/pre-built-policy-packs/aws-organizations-tag-policies/aws/) | Integrates with AWS Organizations Tag Policies to validate that infrastructure as code resources have required tags before deployment. [Learn more](/docs/insights/policy/integrations/aws-organizations-tag-policies/). |

### A foundation for your governance strategy

Our pre-built packs provide a strong foundation for cloud governance by covering common controls for major frameworks. However, every organization has unique requirements.

We recommend that you enhance these pre-built packs with your own custom policies tailored to your specific business, security, and operational needs. Pulumi's flexible Policy as Code framework allows you to [author your own packs](/docs/insights/policy/get-started/#creating-a-policy-pack) and add them to the same Policy Groups alongside pre-built packs, giving you complete and comprehensive coverage.

### Frequently asked questions (FAQ)

**How are pre-built packs updated and versioned?**

Policy Packs in the Pulumi Registry follow semantic versioning. We release new versions when we add coverage for new controls or fix existing policies. You can choose when to update to a new version in your Policy Group configuration.

**How do pre-built packs work with my own custom policies?**

They are designed to work together. You can add both a pre-built pack (like Pulumi Best Practices) and your own custom-authored policy pack to the same Policy Group. This allows you to enforce both general best practices and your organization-specific rules on the same set of stacks.

For more information on authoring custom policy packs, see our [Policy as Code get started guide](/docs/insights/policy/get-started/).
