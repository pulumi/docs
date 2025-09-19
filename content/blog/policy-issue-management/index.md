---
title: "From Insight to Action: Introducing Advanced Policy Issue Management and AI-Powered Remediation"
date: 2025-10-22
authors:
  - alejandro-cotroneo
  - arun-loganathan
meta_desc: "Announcing Pulumi's Policy Findings hub, advanced issue management, and AI-powered remediation with Pulumi Neo to fix compliance issues at scale."
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
---

For any organization serious about cloud governance, identifying a policy violation is only the beginning. The real challenge comes next: managing the flood of alerts, prioritizing what matters most, and actually fixing the issues. Without the right tools, this process quickly leads to alert fatigue, slow remediation times, and a perpetually insecure compliance posture.

Today, as part of the Pulumi Policy v2 launch, we are transforming this experience. We're excited to introduce a completely redesigned **Policy Findings** hub for advanced issue management and, most powerfully, **AI-powered remediation with Pulumi Neo** to help you solve these issues at scale.

<!--more-->

### A New Hub for Policy Insights

We've replaced the old Policy Violations page with a new hub called **Policy Findings**, designed to give every stakeholder—from security leader to auditor to developer—the exact view they need. The Findings page is organized into three distinct tabs.

#### 1. The Overview Tab: Your Compliance Command Center

The Overview tab provides a high-level dashboard of your organization's compliance health. It's designed to give you an instant, at-a-glance understanding of your posture with key metrics:

* **Policy Compliance Score:** The percentage of your enabled policy rules that are currently passing.
* **Resource Compliance Score:** The percentage of your governed resources that are fully compliant.

This view helps leaders track trends, identify macro-level problem areas, and direct strategic efforts. The dashboard provides breakdowns by your Stacks and Cloud Accounts, and we will be adding more options to filter and group data to help you slice and dice the information you need.

#### 2. The Compliance Tab: An Auditor's View

Designed for security and compliance teams, this tab provides a policy-centric view of your findings. It groups results by policy, showing exactly which controls are passing and which are failing across your environment. This is invaluable during audits, where you need to go control-by-control through a standard like CIS or NIST to provide evidence of compliance.

#### 3. The Issues Tab: Your Collaborative Triage Board

This is where your teams turn insight into action. The Issues tab is a collaborative workspace for triaging, assigning, and tracking the remediation of every policy issue. We've significantly enhanced it to support the full lifecycle of an issue:

* **Rich Context:** Every issue now includes a wealth of contextual data and a detailed drill-down screen to help you understand the problem's impact.
* **Ownership and Collaboration:** Assign issues to specific members of your organization to ensure clear ownership and accountability.
* **Prioritization:** Set a priority level from P0 (critical) to P4 (low) to help teams focus on the most important fixes first.
* **Lifecycle Management:** Mark an issue as "Ignored" with a justification. This is critical for cases where a violation is intentional or "by design," allowing you to maintain an accurate compliance picture while acknowledging necessary exceptions.

**Placeholder for a video**

### The Remediation Game-Changer: Pulumi Neo

In any medium-to-large organization, thousands of cloud resources can lead to hundreds or even thousands of policy issues. Manually fixing them all is an impossible task, and in reality, most organizations can't keep up. The backlog grows, and the risk remains.

This is where Pulumi Neo comes to the rescue. Pulumi Neo, our AI agent, is now integrated directly into the issue management workflow to automate the hardest part of the process: the fix itself. When viewing an issue, you can now trigger a Pulumi Neo remediation flow. Neo is smart enough to handle both resources already managed by Pulumi and those discovered via cloud scans.

1. Analyze the non-compliant resource and the policy it's violating.
2. Understand the required configuration to make it compliant.
3. **Generate a pull request with the exact code changes needed to fix the issue.** For a discovered resource, Neo will even generate the code to import it into a Pulumi stack *and* fix the violation in the same pull request, bringing your unmanaged resources under compliant management.

**Placeholder for a video**

This is a revolutionary step forward. It turns a manual task that could take a developer hours into a simple review-and-merge process. With Pulumi Neo, you can finally burn down your issue backlog, drastically reduce your Mean Time to Remediate (MTTR), and achieve a state of continuous compliance at a scale that was previously unimaginable.

### Conclusion

Pulumi Policy is now an end-to-end governance solution that guides you from a high-level compliance overview, through collaborative triage, and all the way to an AI-generated fix.

This powerful new experience is available today. Navigate to the **Policies > Findings** tab in the Pulumi Cloud to explore your new compliance dashboard and start turning your policy insights into action.
