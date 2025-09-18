---
title: "Introducing Audit Policy Scans for IaC Stacks"
date: 2025-10-22
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

Today, as part of the Pulumi Policy as Code v2 launch, we're introducing a new capability: **Audit Policy Scans for IaC Stacks**. This feature allows you to run policy checks in Pulumi Cloud against the last successful deployment state, i.e., post-deployment of your stacks, completely independent of your CI/CD pipeline.

Until now, Pulumi’s preventative policies have served as a critical "shift-left" gate, blocking non-compliant changes during `pulumi up`. While essential, this created challenges for organizations wanting to roll out new governance across thousands of existing stacks or for teams looking to speed up deployment times. This new evaluation mode solves both problems, giving you a complete and continuous view of your IaC compliance posture without the friction.

<!--more-->

### Key Scenarios for Audit Scans

Audit scans for IaC stacks are designed to unlock policy adoption at scale and accelerate developer velocity. Key use cases include:

* **Gain an instant compliance overview across all existing stacks.** Organizations with hundreds of existing Pulumi stacks can apply policies centrally without performing a `pulumi up` on all of them. This gives an immediate, organization-wide compliance baseline without disrupting development.
* **Accelerate developer workflows.** By decoupling policy evaluation from the critical deployment path, deployments become faster and developers are unblocked. Teams still get immediate feedback on the compliance of the deployed infrastructure without slowing down CI/CD pipelines.
* **Ensure continuous compliance.** Post-deployment evaluation is automatically triggered whenever policy configurations change. This ensures the *latest policies* are always evaluated against the *latest deployed infrastructure*, providing a truly continuous, up-to-date view of your security posture.

### How It Works

This new mechanism runs against the last known successfully deployed state of your IaC Stacks as recorded by Pulumi Cloud.

* **Evaluation is triggered automatically** after a successful `pulumi up` or when a policy pack attached to the stack is updated.
* **Results are unified** into the same Policy Issues dashboard you use today, giving you a single pane of glass for all preventative and audit policy findings.

### How to Get Started

You can enable audit scans for your IaC stacks by adding them to an **Audit Policy Group**. This uses the same intuitive workflow you already use for managing policies.

1. **Navigate to the Policies tab** in the left navigation bar of the Pulumi Cloud console.
2. **Create a new Audit Policy Group** or select an existing one.
3. Select **Pulumi Stacks** and add the specific stacks you want to monitor.
4. **Add Policy Packs** to the group.
5. **Save the policy group**. That's it!

**Placeholder for Video**

The next time any of the selected stacks completes a `pulumi up`, a post-deployment evaluation will be automatically triggered. The results will populate in the Policy Issues tab, ready for triage and remediation.

**Add a note that this will consume workflow minutes**

### A Complete Governance Picture

With the addition of post-deployment evaluation for IaC stacks, you gain continuous visibility into your entire cloud estate and can easily audit your IaC-managed footprint without adding friction to your development process.

Try it out in the Pulumi Cloud today and check out the documentation to learn more!
