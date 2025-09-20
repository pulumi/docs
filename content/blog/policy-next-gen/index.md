--- 
title: "Announcing the Next Generation of Pulumi Policies: AI-Accelerated Governance for the Cloud"
date: 2025-10-22T8:59:00-00:00
authors: 
- craig-symonds
- tyler-dunkel
- arun-loganathan
meta_desc: "Launching the next generation of Pulumi Governance, powered by Pulumi Policies. Turn governance from a blocker into a business accelerator." 
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

The era of AI-accelerated development is here. AI coding assistants are making developers 55% faster and halving merge times. But this incredible velocity has created a paradox: platform teams, the very people meant to enable this speed, are being overwhelmed. Every line of code shipped faster creates new demands for infrastructure, security, and compliance. Traditional, manual governance has become a velocity trap—a bottleneck that stifles the very innovation it's meant to protect.

For the last couple of years, engineering leaders have faced a false choice: move fast with AI and accept the risk, or lock down the platform and sacrifice speed. Today, we end that compromise.

We are thrilled to announce a massive leap forward with the **next generation of Pulumi Policies**, the engine that powers our comprehensive **Pulumi Governance** solution. This is not just an update; it's a new paradigm for cloud governance. We’re moving beyond reactive enforcement to proactive enablement, with AI-accelerated guardrails designed to scale *with* developer velocity, not restrict it. As you build faster with AI, you can now govern smarter, safer, and more efficiently.

<!--more-->

## The Governance Crisis in the Age of AI

As we discussed when we [introduced Pulumi Neo](<ins>/blog/meet-neo-your-newest-platform-engineer/</ins>), the success of developer AI has become a critical challenge for platform teams. They are caught between the relentless pace of development and the absolute need for control. This leads to unwinnable situations:

* **Platform Bottlenecks:** 45% of platform teams report they can't even measure their governance effectiveness. Lacking the right tools, they struggle to create the "golden paths" that developers actually want to use, leading to slow, manual review cycles that kill productivity.
* **Reactive Security Postures:** Security teams are drowning in alerts from CSPM tools that only find misconfigurations *after* deployment. It's a constant cycle of detection and remediation that leaves the organization perpetually exposed.
* **Innovation vs. Risk Trade-off:** 68% of CIOs cite AI risks as a major concern. Without a way to embed governance directly into the AI-driven workflow, leadership is forced to slow down innovation to manage risk.

## The Pulumi Difference: Policy as Real Code

Unlike other solutions that rely on restrictive DSLs or complex YAML, Pulumi Policies uses general-purpose programming languages like TypeScript and Python. This isn't just a language choice; it's a fundamental advantage that provides unmatched power and flexibility. You can express complex, nuanced rules that reflect your actual business logic. This approach allows you to:

* **Use conditional logic** to create sophisticated policies that can't be expressed in simple configuration files.
* **Build reusable functions and abstractions** to create a shared, version-controlled library of your organization's governance rules.
* **Write unit tests** to validate your policy behavior before you ever roll it out, ensuring your guardrails are reliable and correct.

This "Policy as *Real* Code" approach provides a robust foundation that is essential for governing modern, complex cloud environments.

## Pulumi Governance: The Unified Control Plane for Your Organization

Pulumi Governance is a core pillar of the entire Pulumi platform, designed to solve these challenges with a unified control plane. It’s what makes a secure and compliant platform possible. **Pulumi Policies** is the feature that brings this vision to life, creating a web of trust that connects the entire platform:

* **Pulumi IaC:** Policies are applied directly to your infrastructure code, preventing non-compliant resources from ever being created. It's the ultimate shift-left, enforcing standards at the source.
* **Pulumi IDP:** Policies are the built-in guardrails for your "golden path" components and templates. They ensure that every piece of infrastructure developers self-service—whether through a template or a no-code workflow—is compliant by design.

Most importantly, these policies become the operational guardrails for **Pulumi Neo**. When our AI agent automates infrastructure tasks, it runs within the bounds you've already defined, ensuring every AI-generated change is secure, compliant, and trustworthy by default. Your investment in governance directly accelerates safe AI adoption.

## What's New: The Next Generation of Pulumi Policies

Today’s launch bundles several powerful new capabilities into a single, cohesive experience designed for the AI era.

* **Simplified Policy Management & In-Console Marketplace****: As announced in September, Policy as Code is now available to all Team and Enterprise customers. Discovering, applying, and managing policies is radically simpler with a new marketplace directly in the Pulumi Cloud. You can browse, add, and configure expert-authored policy packs without ever touching the CLI.
* **New Pre-Built Compliance Packs**: Accelerate your compliance journey from months to minutes. We are launching a new suite of expert-authored packs for **CIS Controls v8.1**, **NIST SP 800-53 Rev. 5**, and **PCI DSS v4.0**. These codify hundreds of controls, allowing you to enforce industry-standard baselines immediately.

| Framework                 | AWS | Azure | Google Cloud |
| ------------------------- |:---:|:-----:|:------------:|
| **CIS Controls v8.1**      | ✅  |   ✅  |      ✅      |
| **NIST SP 800-53 Rev. 5**  | ✅  |       |              |
| **PCI DSS v4.0**           | ✅  |       |              |
| **HITRUST CSF v11.5**      | ✅  |   ✅  |      ✅      |
| **Pulumi Best Practices**  | ✅  |   ✅  |      ✅      |

* **Audit Scans for IaC Stacks**: Gain complete compliance visibility without sacrificing developer speed. You can now run policy checks against the last successful deployment state of any stack, completely decoupled from your CI/CD pipeline. This provides an instant compliance baseline and ensures developer workflows remain fast.
* **The New Policy Findings Hub**: Move from alerts to action. We’ve replaced the old violations view with a powerful **Policy Findings** hub. It provides an executive overview with compliance scores, an auditor-friendly view grouped by controls, and a collaborative issue management workspace to triage, assign, and track every finding.
* **The Remediation Engine: AI-Powered Fixes with Pulumi Neo**: This is the game-changer. Finding thousands of issues is useless if you can't fix them. **Pulumi Neo is now integrated directly into our issue management workflow to provide AI-powered remediation.** Instead of just telling you what's wrong, Neo generates a pull request with the exact code needed to fix it. For discovered resources, Neo will even generate the code to **import the resource into Pulumi and apply the fix in a single PR**, closing the loop from detection to remediation and turning unmanaged infrastructure into governed code.

## Embrace Governance That Accelerates You

The age of AI-driven development demands AI-driven governance. With this new generation of Pulumi Policies, we are providing the essential infrastructure for platform engineering teams to not just survive, but thrive. You can finally build golden paths with guardrails that developers love, secure your cloud at scale, and transform governance from a cost center into a competitive advantage.

This powerful new experience is available today. Navigate to the **Policies** tab in the Pulumi Cloud to explore your new governance capabilities and meet the future of platform engineering.
