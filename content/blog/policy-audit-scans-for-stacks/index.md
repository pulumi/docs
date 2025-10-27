---
title: "Introducing Audit Policy Scans for Pulumi Stacks"
date: 2025-10-22T00:04:00
authors:
  - levi-blackstone
  - arun-loganathan
meta_desc: "Continuous policy evaluation for IaC stacks based on their last successful deployment state, enabling frictionless adoption and faster CI/CD."
allow_long_title: true
meta_image: "meta.png"
tags:
  - pulumi-service
  - policy-as-code
  - crossguard
  - features
  - compliance
  - governance
---

Today, as part of the next generation of Pulumi Policies, we're introducing **Audit Policy Scans for Pulumi Stacks**. This capability uses policies to run compliance checks against the last successful deployment state of your stacks, providing continuous compliance monitoring without impacting your existing CI/CD workflows.

Until now, Pulumi’s preventative policies have served as a critical "shift-left" gate, blocking non-compliant changes during `pulumi up`. While essential, this created challenges for organizations wanting to roll out new governance across thousands of existing stacks. This new evaluation mode solves that problem, giving you a complete and continuous view of your IaC compliance posture without the friction.

<!--more-->

## A Complete Audit Story: Cloud Accounts and IaC Stacks

Pulumi's audit philosophy is to provide complete visibility across your entire cloud footprint. We achieve this through two complementary audit modes:

1. **Audit Scans for Cloud Accounts (Existing):** This capability scans your live cloud environments (like an AWS account or Azure subscription). Its primary purpose is to give you a holistic view of your security posture by discovering *all* resources, including those not managed by Pulumi, and detecting configuration drift. This is how you find unmanaged, legacy, or manually-created resources that violate your policies.

2. **Audit Scans for Pulumi Stacks (New):** The feature we're launching today extends this audit power to the source of truth for your managed infrastructure: your Pulumi stacks. It evaluates the *last successfully deployed state* of your IaC. This allows you to get an instant compliance baseline of all your managed infrastructure without having to redeploy anything, making it perfect for frictionless policy rollouts at scale.

Together, these two audit modes give you a comprehensive picture of your entire cloud estate, all feeding into one unified **Policy Findings hub**.

## Key Scenarios for Audit Scans for Stacks

This new evaluation mode for IaC stacks is designed to unlock policy adoption at scale and accelerate developer velocity. Key use cases include:

* **Gain an instant compliance overview across all existing stacks:** Apply policies centrally and get immediate visibility into your compliance posture without requiring redeployment of every stack.
* **Accelerate policy rollouts:** By decoupling policy evaluation from the critical deployment path, deployments become faster and developers are unblocked. Teams still get immediate feedback on the compliance of the deployed infrastructure.
* **Ensure continuous compliance:** Evaluation is automatically triggered whenever policy configurations change. This ensures the *latest policies* are always evaluated against the *latest deployed infrastructure*.

## How It Works

This new mechanism runs against the last known successfully deployed state of your IaC Stacks as recorded by Pulumi Cloud.

* **Evaluation is triggered automatically** after a successful `pulumi up` or when a policy pack attached to the stack is updated.
* **Results are unified** into the same **Policy Findings hub** you use today, giving you a single pane of glass for all preventative and audit policy findings.

## How to Get Started

You can enable audit scans for your IaC stacks by adding them to an **Audit Policy Group**.

1. Navigate to the **Policies** tab in the left navigation bar of the Pulumi Cloud console.
2. Create a new **Audit Policy Group** or select an existing one.
3. Select **Pulumi Stacks** and add the specific stacks you want to monitor.
4. **Add Policy Packs** to the group.
5. **Save the policy group**. That's it!

**Placeholder for Video**

The next time any of the selected stacks completes a `pulumi up`, a post-deployment evaluation will be automatically triggered, and the results will populate in the Policy Findings hub.

{{< notes type="info" >}}
Audit policy scans consume workflow minutes from your Pulumi Cloud plan. Each scan counts toward your monthly quota based on the complexity and number of resources evaluated. See pricing documentation for details.
{{< /notes >}}

## A Complete Governance Picture

With the addition of post-deployment evaluation for IaC stacks, you now have a complete, 360-degree view of your cloud environment. You can use audit scans for cloud accounts to get a handle on your entire live footprint, and use audit scans for stacks to easily assess your IaC-managed footprint without adding friction to your development process.

Try it out in the Pulumi Cloud today and check out the documentation to learn more!
