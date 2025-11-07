---
title: "Announcing the Next Generation of Pulumi Policies: AI-Accelerated Governance for the Cloud"
authors: 
- craig-symonds  
- tyler-dunkel  
- arun-loganathan
date: 2025-11-05T00:05:00
meta_desc: "Launching the governance lifecycle: AI-powered remediation, pre-built compliance packs, continuous auditing, and a new Policy Findings hub."
allow_long_title: true
meta_image: "meta.png"
tags:
- policy-as-code
- features
- compliance
- governance
- pulumi-neo
- ai
- platform-engineering
---

The era of AI-accelerated development has created a paradox: the faster developers move, the bigger the governance challenge becomes. For years, security and platform teams have worked to "shift left," but the tools available have been incomplete. Most focus on detection, which is necessary but not sufficient. They identify thousands of policy violations across an organization's infrastructure but leave teams with an overwhelming backlog and no scalable way to remediate it. This creates a persistent gap between finding a problem and fixing it. The result is an impossible choice between development velocity and organizational control, forcing leadership to slow down innovation to manage risk.

Today, we end that compromise.

<!--more-->

We are thrilled to announce the next generation of Pulumi Policies, a comprehensive governance solution that moves beyond detection to deliver AI-powered remediation at scale. We’re introducing a new lifecycle to secure your cloud: first, **Get Clean** by using AI to fix your existing policy violations. Second, **Stay Clean** by using policy as a universal guardrail that makes AI-driven development not just fast, but fundamentally safe. These are not strictly sequential steps; you can begin enforcing "Stay Clean" policies for all new infrastructure while you simultaneously work on the "Get Clean" process for your existing footprint.

Watch our Launch Video:

{{< youtube "mwcrOTEf1EQ?rel=0" >}}

## Part 1: Get Clean - From Thousands of Issues to a Compliant State

The first step to a secure cloud is tackling the mountain of existing misconfigurations spread across your environments.

### First, Gain Complete Visibility with the New Policy Findings Hub

To fix your issues, you first need to see them clearly. We have introduced a powerful **[Policy Findings Hub](https://www.pulumi.com/blog/policy-issue-management/)** designed to give every stakeholder the exact view they need.

* **The Overview Tab:** A high-level dashboard with compliance scores for leadership to track trends and measure your organization's posture.
* **The Compliance Tab:** A control-centric view for auditors and infosec teams, grouping findings by policy (e.g., CIS, NIST) to simplify evidence gathering and prove compliance.
* **The Issues Tab:** A collaborative workspace for platform and development teams to triage, assign, prioritize, and track the remediation of every policy issue.

This hub is powered by our flexible audit capabilities. With **[Audit Scans for IaC Stacks](https://www.pulumi.com/blog/policy-audit-scans-for-stacks/)**, you can get an instant compliance baseline on all your existing Pulumi-managed infrastructure without blocking developers or re-deploying thousands of stacks. This is combined with discovery scans of your cloud accounts to give you a single, unified view of every resource, whether managed by Pulumi or not.

### The Solution to Remediation at Scale: AI-Powered Fixes with Pulumi Neo

Visibility creates a new problem: an overwhelming backlog. Manually fixing thousands of issues is an impossible task.

This is where Pulumi Neo provides a powerful solution.

Pulumi Neo, our AI platform engineer, is now integrated directly into the Policy Findings hub to automate the most difficult part of the process: the fix itself. From the Issues tab, your teams can now select a group of policy issues, assign them to Neo, and trigger a remediation flow.

Neo is smart. It will:

1. Analyze the non-compliant resources and the policies they are violating.
2. Understand the required configuration to make them compliant.
3. **Generate a pull request with the exact code changes needed to fix the issues.**

Most powerfully, for an unmanaged resource discovered via a cloud scan, Neo will generate the code to **import the resource into a Pulumi stack and apply the fix.** This "Import and Fix" workflow transforms unmanaged infrastructure into governed, compliant code, turning a task that could take a developer hours into a simple review-and-merge process. Your teams can finally burn down their issue backlog and achieve a state of continuous compliance.

## Part 2: Stay Clean - The Universal Guardrail for Humans and AI

Once you begin cleaning your environment, the next challenge is to *stay* clean. As AI accelerates infrastructure creation, you need robust guardrails to ensure it doesn't also accelerate the creation of security risks.

The answer is **Policy as *Real* Code.** Pulumi Policies uses general-purpose languages like TypeScript and Python to create sophisticated guardrails that govern every change. To help you establish these controls immediately, we are launching a new suite of pre-built compliance packs authored and maintained by Pulumi experts.

| Framework                 | AWS | Azure | Google Cloud |
| ------------------------- |:---:|:-----:|:------------:|
| **CIS Controls v8.1**      | ✅  |   ✅  |      ✅      |
| **NIST SP 800-53 Rev. 5**  | ✅  |       |              |
| **PCI DSS v4.0**           | ✅  |       |              |
| **HITRUST CSF v11.5**      | ✅  |   ✅  |      ✅      |
| **Pulumi Best Practices**  | ✅  |   ✅  |      ✅      |

These policies act as a universal guardrail for your entire organization by blocking non-compliant changes during `pulumi up`, before they are ever created. Learn more about our [compliance packs](https://www.pulumi.com/blog/policy-packs-cis-nist-pci/).

And now, you can even use **Neo to author new policies**. You can ask Neo in plain English to "create a policy that prevents overly permissive IAM roles," and it will generate the code for you. This creates a powerful, dynamic governance system where AI can help you build the very rules that then govern its own actions. If you then ask Neo to create an admin role, the deployment will be blocked by the policy it just helped write. This is how we make AI safe to go fast.

## A New Era of Collaboration

This "Get Clean, Stay Clean" lifecycle transforms how teams work together:

* **Platform Teams** lead prevention by building real-code guardrails, proving their value with measurable compliance scores.
* **Security Teams** drive the "Get Clean" process with continuous, non-blocking audit scans and use the Findings hub to manage compliance without slowing development.

## Governance That Accelerates You

The age of AI-driven development demands AI-powered governance. With this new generation of Pulumi Policies, we are providing the essential infrastructure for platform engineering teams to not just survive, but thrive. You can finally build preventative guardrails that developers love, secure your cloud at scale, and transform governance from a blocker into a business accelerator. Learn more about [Pulumi Insights & Governance capabilities](https://www.pulumi.com/product/insights-governance/).

This powerful new experience is available today. Navigate to the **Policies** and **Policy Findings** tab in Pulumi Cloud to explore your new governance capabilities and meet the future of platform engineering.

## Try Pulumi Policies

**Ready to try these features?**

* [Sign in to Pulumi Cloud](https://app.pulumi.com/signup) and start a Neo task  
* [Read the Get Started guide](/docs/insights/policy/get-started/) to configure and apply your first policy group to stacks and cloud accounts.
* [Join the Community Slack](https://slack.pulumi.com/) to share feedback on the new features

For complete documentation, visit our [Policy documentation](https://www.pulumi.com/docs/insights/policy/).
