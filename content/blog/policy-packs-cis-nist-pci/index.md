---
title: "New Compliance Packs for CIS, NIST, and PCI DSS"
date: 2025-11-05T00:02:00
authors:
  - luke-ward
  - dan-biwer
meta_desc: "Pulumi pre-built policy packs for CIS v8.1, NIST 800-53 Rev. 5, and PCI DSS v4.0 help teams achieve and maintain cloud compliance in minutes, not months."
allow_long_title: true
meta_image: "meta.png"
tags:
  - pulumi-service
  - policy-as-code
  - crossguard
  - features
  - compliance
  - governance
  - security
---

Achieving compliance with industry standards such as **CIS, NIST**, or **PCI DSS** is a foundational step for every organization. Yet for many teams, it's often a manual, months-long process that involves interpreting controls, authoring custom policies, and validating configurations across multiple clouds. These challenges often slow progress toward a known and secure cloud state.

We're changing that. To simplify this journey, Pulumi launched a new suite of **pre-built compliance policy packs** for [CIS Controls v8.1, NIST SP 800-53 Rev. 5, and PCI DSS v4.0](https://www.pulumi.com/docs/insights/policy/policy-packs/pre-built-packs/#available-policy-packs). 

These packs are your accelerator for the "**Get Clean**" journey, allowing you to enforce critical security and compliance baselines across your cloud infrastructure **in minutes, not months**.

<!--more-->

## More Than Just Detection: The Complete Governance Lifecycle

Traditional security tools are reactive, scanning for problems *after* resources have been deployed. With Pulumi, these new compliance packs are the engine for an end-to-end governance lifecycle that integrates directly into your cloud operations.

1. **Audit for Full Coverage:** Run these packs in audit mode to scan your entire cloud estate, including resources managed by Pulumi and those created through other means. This gives you an instant, comprehensive view of your current compliance posture.
2. **Triage and Remediate:** When a pack finds a violation, the finding appears in the new **[Policy Findings hub](https://www.pulumi.com/blog/policy-issue-management/)**. From there, your team can triage, assign, and track the issue through its entire lifecycle. And with our new AI-powered capabilities, you can assign the issue to **Pulumi Neo** to automatically generate a pull request with the fix.
3. **Prevent Non-Compliance:** Once your environment is clean, you use these same packs as preventative guardrails. By running them during `pulumi up`, you block non-compliant resources *before they are ever created*, ensuring you "Stay Clean."

This tri-modal capability—Audit, Remediate, and Prevent—is uniquely powerful, allowing you to fix existing issues while stopping new ones from being introduced.

## New and Expanded Compliance Packs

Our new policy packs provide extensive, out-of-the-box coverage for some of the most widely adopted security frameworks. They are authored and maintained by Pulumi experts and join our existing library to provide a comprehensive toolkit for cloud governance.

| Framework                 | AWS | Azure | Google Cloud |
| ------------------------- |:---:|:-----:|:------------:|
| **CIS Controls v8.1**     | ✅  |   ✅  |      ✅      |
| **NIST SP 800-53 Rev. 5** | ✅  |       |              |
| **PCI DSS v4.0**          | ✅  |       |              |
| **HITRUST CSF v11.5**     | ✅  |   ✅  |      ✅      |
| **Pulumi Best Practices** | ✅  |   ✅  |      ✅      |

## Benefits of Pre-Built Packs

* **Accelerate Compliance:** Implement comprehensive governance controls in minutes without authoring hundreds of policies from scratch.
* **Leverage Expert Knowledge:** Packs are authored and maintained by Pulumi, incorporating deep expertise in cloud and the nuances of each framework.
* **Codify Controls for Audits:** Demonstrate to auditors that specific compliance controls are consistently enforced through code, providing a clear evidence trail.
* **Reduce Risk Proactively:** Catch common security risks and compliance violations before deployment, drastically reducing your organization's exposure.

## Get Started Today

These policy packs are available now and are the perfect way to begin your governance journey with Pulumi.

To get started, head to the **Policies** page in your Pulumi Cloud organization and click on the **All** tab to find these new packs. Add them to an **Audit Policy Group** and run a scan. Within minutes, you'll see a complete picture of your compliance posture in the **Policy Findings hub**, ready for triage and remediation.

Need a compliance pack for a standard that isn't listed here? Please let us know by raising a request on our [GitHub repository](https://github.com/pulumi/pulumi-cloud-requests).

## Try Pulumi Policies

**New to Pulumi? Start your governance journey today.**

* [Sign up for Pulumi Cloud](https://app.pulumi.com/signup) and start compliance task with Neo  
* [Read the Get Started guide](/docs/insights/policy/get-started/) to apply and manage policies across your cloud infrastructure
* [Join the Community Slack](https://slack.pulumi.com/) to share feedback on the new features

For complete documentation, visit our [Policies documentation](https://www.pulumi.com/docs/insights/policy/).
