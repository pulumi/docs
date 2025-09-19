---
title: "Announcing New Pre-Built Compliance Packs for CIS, NIST, and PCI DSS"
date: 2025-10-22
authors:
  - luke-ward
  - dan-biwer
meta_desc: "Launching new, pre-built compliance policy packs for CIS. NIST SP 800-53 and PCI DSS to help organizations meet security and regulatory requirements."
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

We're excited to launch a new suite of pre-built compliance policy packs for **CIS Controls v8.1**, **NIST SP 800-53 Rev. 5**, and **PCI DSS v4.0**. These packs codify hundreds of industry-standard controls, allowing you to enforce critical security and compliance baselines across your cloud infrastructure in minutes, not months.

<!--more-->

### The Pulumi Difference: Prevent, Don't Just Detect

Traditional security tools are reactive, scanning for problems *after* resources have been deployed. Pulumi Policy as Code lets you shift left by integrating governance directly into the infrastructure lifecycle, combining prevention with continuous auditing.

* **Prevent Non-Compliance:** Policies act as guardrails during `pulumi up`, blocking non-compliant resources *before they are ever created*. This eliminates risk at the source.
* **Audit for Full Coverage:** The same policies can be used to continuously audit your entire cloud estate, including resources managed by Pulumi and those created through other means.

This dual capability is uniquely powerful, allowing you to stop new issues from being introduced while maintaining complete visibility across your entire cloud footprint.

### New and Expanded Compliance Packs

Our new policy packs provide extensive, out-of-the-box coverage for some of the most widely adopted security and compliance frameworks in the world. They join our existing library to provide a comprehensive toolkit for cloud governance, authored and maintained by Pulumi experts.

| Framework                 | AWS | Azure | Google Cloud |
| ------------------------- |:---:|:-----:|:------------:|
| **CIS Controls v8.1**     | ✅  |   ✅  |      ✅      |
| **NIST SP 800-53 Rev. 5** | ✅  |       |              |
| **PCI DSS v4.0**          | ✅  |       |              |
| **HITRUST CSF v11.5**     | ✅  |   ✅  |      ✅      |
| **Pulumi Best Practices** | ✅  |   ✅  |      ✅      |

### Benefits of Pre-Built Packs

* ***Accelerate Compliance:** Implement comprehensive governance controls in minutes without authoring hundreds of policies from scratch.
* **Leverage Expert Knowledge:** Packs are authored and maintained by Pulumi, incorporating deep expertise in cloud and the specific nuances of each framework.
* **Codify Controls for Audits:** Demonstrate to auditors that specific compliance controls are consistently enforced through code, providing a clear and immutable evidence trail.
* **Reduce Risk Proactively:** Catch common security risks and compliance violations before deployment, drastically reducing your organization's exposure.

### Get Started Today

These policy packs are available now. To get started, head to the **Policies** page in your Pulumi Cloud organization, click on the **Marketplace** tab to find these new packs, and add them to your organization. From there, you can begin using them in your policy rules immediately.

Need a compliance pack for a standard that isn't listed here? Please let us know by raise a request on our [github repository](https://github.com/pulumi/pulumi-cloud-requests).
