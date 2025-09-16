---
title: Pre-Built Packs
title_tag: "Pre-built policy packs"
h1: Pre-Built Packs
meta_desc: Use pre-built policy packs to apply industry-standard compliance and security controls to your cloud infrastructure as code.
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  insights:
    parent: policy-as-code
    weight: 5
aliases:
  - /docs/pulumi-cloud/insights/pre-built-packs/
---

Pulumi Cloud comes with pre-built policy packs that codify best practices for common security and compliance frameworks. These packs allow you to quickly evaluate your organization's compliance posture and "shift left," embedding continuous compliance directly into your IaC workflow. Proactively enforce controls, reduce misconfiguration risks before deployment, and help your organization meet its regulatory obligations with confidence.

### Why Use Pre-Built Packs?

- **Accelerate Adoption:** Implement comprehensive governance controls in minutes without having to author policies from scratch.
- **Leverage Expert Knowledge:** Packs are authored and maintained by Pulumi, incorporating deep expertise in cloud security best practices.
- **Enforce Consistency:** Apply a single, version-controlled policy pack across your entire organization to ensure all teams and projects adhere to the same standards.
- **Proactive Risk Reduction:** Catch common security risks and compliance violations during `pulumi preview`, long before they reach your production environments.

### **Available Policy Packs**

The following pre-built policy packs are available today out of the box in Pulumi Cloud.

| Framework | Supported Cloud Providers | Description |
| ----- | ----- | ----- |
| **HITRUST CSF 11.5** | AWS, Azure, Google Cloud | Provides predefined controls that align cloud resources with HITRUST CSF requirements, helping organizations enforce security and compliance baselines across multiple providers. |
| **Pulumi Best Practices** | AWS, Azure, Google Cloud | Offers a foundational set of recommended governance and security controls, serving as a strong starting point for organizations seeking comprehensive security coverage. |

### **Enabling Pulumi Policy Packs for Your Organization**

Pulumi policy packs can be enabled at the **organization level**, allowing you to enforce compliance and governance standards across all projects and stacks within your organization.

1. From within your organization, navigate to the **Policies** tab
2. Under Policy Packs, select the **Available** tab
3. Select the packs to apply to your organization, and select **Add to organization**
4. From the Organizations tab, apply the policies to a Policy Group to enforce compliance controls

{{< video title="Adding policy packs to organization" src="/docs/insights/assets/Adding policy-packs to organization.mp4" autoplay="true" loop="true" >}}

Enabling Pulumi policy packs ensures consistent governance, simplifies compliance management, and reduces the risk of misconfigured resources across your entire organization.

### A Foundation for Your Governance Strategy

Our pre-built packs provide a strong foundation for cloud governance by covering common controls for major frameworks. However, every organization has unique requirements.

We recommend that you enhance these pre-built packs with your own custom policies tailored to your specific business, security, and operational needs. Pulumi's flexible Policy as Code framework allows you to [author your own packs](/docs/iac/crossguard/get-started/#creating-a-policy-pack) and add them to the same Policy Groups alongside pre-built packs, giving you complete and comprehensive coverage.

### Frequently Asked Questions (FAQ)

**How are pre-built packs updated and versioned?**

Policy Packs in the Pulumi Registry follow semantic versioning. We release new versions when we add coverage for new controls or fix existing policies. You can choose when to update to a new version in your Policy Group configuration.

**How do pre-built packs work with my own custom policies?**

They are designed to work together. You can add both a pre-built pack (like Pulumi Best Practices) and your own custom-authored policy pack to the same Policy Group. This allows you to enforce both general best practices and your organization-specific rules on the same set of stacks.

For more information on authoring custom policy packs, see our [Policy as Code get started guide](/docs/iac/crossguard/get-started/).
