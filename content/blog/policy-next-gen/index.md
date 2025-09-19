---
title: "Announcing the Next Generation of Pulumi Policies: AI-Accelerated Governance for the Cloud"
date: 2025-10-22T8:59:00-00:00
authors:
  - craig-symonds
  - tyler-dunkel
  - arun-loganathan
meta_desc: "Launching the next generation of Pulumi Policies, the engine for Pulumi Governance, with AI-powered remediation and tools for AI-accelerated development."
allow_long_title: true
meta_image: "meta.png"
tags:
  - pulumi-service
  - policy-as-code
  - features
  - compliance
  - governance
  - pulumi-neo
  - ai
  - platform-engineering
---

The era of AI-accelerated development is here. Research shows that AI assistance makes developers 55% faster at completing tasks and halves merge times. But this incredible velocity comes with a challenge: a 15-20% increase in infrastructure costs and governance complexity. Traditional, manual approval workflows simply cannot scale to keep pace, creating bottlenecks that stifle innovation and increase risk.

Today, we are thrilled to announce a massive leap forward for **Pulumi Policies**, the engine that powers our comprehensive **Pulumi Governance** solution. This next-generation release is designed to provide golden paths with guardrails that scale with developer velocity, not restrict it. This is not just an update; it's a transformation of your approach from reactive enforcement to proactive enablement, ensuring that as you build faster with AI, you also build smarter, safer, and more efficiently.

<!--more-->

### The Governance Challenge in the Age of AI

In today's cloud-native world, organizations are building Internal Developer Platforms (IDPs) to standardize and accelerate development. But without a robust governance layer, these platforms can't deliver on their promise. This creates major challenges for security and engineering teams:

*   **Platform Bottlenecks:** 45% of platform teams report they can't even measure their governance effectiveness. Lacking the right tools, they struggle to create golden paths that developers actually want to use, leading to slow, manual review cycles that kill productivity.
*   **Reactive Security Postures:** Security teams are overwhelmed. With AI generating infrastructure at an unprecedented rate, traditional CSPM tools that only detect misconfigurations *after* deployment are no longer sufficient. It's a constant, unwinnable cycle of finding and fixing, leaving the organization perpetually exposed.
*   **Innovation vs. Risk Trade-off:** 68% of CIOs cite AI risks as a serious concern. Engineering leadership is forced into a false choice between moving fast and staying compliant, often sacrificing one for the other.

### Pulumi Governance: A Unified Approach

Pulumi Governance is a core pillar of the Pulumi platform, designed to solve these challenges. It’s more than just a policy engine; it's a control plane that integrates across the entire Pulumi IDP to enable a complete, end-to-end governance lifecycle. **Pulumi Policies** is the feature that brings this vision to life, working in concert with the entire platform:

*   **Pulumi IaC:** Define infrastructure and policies in standard programmaing languages.
*   **Pulumi IDP:** Publish and discover compliant templates and reusable "golden path" components that conforms to the policies defined 
*   **Pulumi ESC:** Securely manage the secrets and configuration that your governed infrastructure depends on.

The new generation of Pulumi Policies enhances every part of this lifecycle, turning governance from a blocker into an accelerator.

### What's New: The Next Generation of Pulumi Policies

This launch represents a fundamental leap forward in user experience, capability, and scale. We've been enhancing our policy engine significantly over the past year, and today, we're bringing it all together. Here are the highlights:

*   **Simplified Policy Management & In-Console Marketplace**: Policy management is now available to all Team and Enterprise customers. Discovering and applying policies is radically simpler. You can now browse a rich library of pre-built policy packs directly within the Pulumi Cloud—no CLI required. You can apply them on a preventative basis or continuosly audit the state of your cloud resources, allowing you to scale governance across your entire infrastructure.

*   **New Pre-Built Compliance Packs**: We have expanded our library of expert-authored compliance packs to help you meet your regulatory goals immediately. We are launching new packs for **CIS Controls v8.1**, **NIST SP 800-53 Rev. 5**, and **PCI DSS v4.0**.

| Framework                 | AWS | Azure | Google Cloud |
| ------------------------- |:---:|:-----:|:------------:|
| **CIS Controls v8.1**     | ✅  |   ✅  |      ✅      |
| **NIST SP 800-53 Rev. 5** | ✅  |       |              |
| **PCI DSS v4.0**          | ✅  |       |              |
| **HITRUST CSF v11.5**     | ✅  |   ✅  |      ✅      |
| **Pulumi Best Practices** | ✅  |   ✅  |      ✅      |

*   **Audit Scans for IaC Stacks**: You can now run policy checks against the last successful deployment state of your stacks, completely independent of your CI/CD pipeline. This is a game-changer for decoupling policy evaluation from the critical deployment path, speeding up developer workflows and allowing you to get an instant compliance baseline across all existing stacks without disruption.

*   **The New Policy Findings Hub**: We’ve replaced the old violations view with a powerful **Policy Findings** hub. It features three tabs: **Overview** (for at-a-glance dashboards and compliance scores), **Compliance** (an auditor-friendly view grouped by policy control), and **Issues** (a collaborative workspace to triage, assign, and manage the lifecycle of every issue).

*   **The Remediation Engine: AI-Powered Fixes with Pulumi Neo**: Finding thousands of issues is useless if you can't fix them. **Pulumi Neo is now integrated directly into our issue management workflow to provide AI-powered remediation.** Instead of just telling you what's wrong, Neo generates a pull request with the exact code needed to fix it. For discovered resources, Neo will even generate the code to **import the resource into Pulumi and apply the fix in a single PR**, bringing your unmanaged infrastructure under compliant control.

### Embrace Governance That Accelerates You

Pulumi Governance, powered by this new generation of Pulumi Policies, is an essential platform engineering infrastructure that enables you to mature your governance posture without sacrificing the velocity that AI promises. It transforms governance from a cost center into a competitive advantage.

This powerful new experience is available today. Navigate to the **Policies** tab in the Pulumi Cloud to explore your new governance capabilities.
