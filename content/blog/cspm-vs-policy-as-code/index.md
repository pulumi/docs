---
title: "Do you need CSPM if you enforce policy in your IaC?"
date: 2026-11-13
draft: false
meta_desc: "CSPM vs policy as code: what deploy-time policy blocks, what posture scanning finds, and how to decide whether your cloud needs both."
feature_image: feature.png
authors:
    - pulumi-content-team
tags:
    - policy-as-code
    - security
    - compliance
    - governance
    - insights
category: general
faq_schema: true
related_posts:
    - best-policy-as-code-tools

# Social media copy — auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter: |
        If you enforce policy in your IaC, do you still need CSPM?

        Policy as code stops bad changes before they deploy. CSPM finds what already exists, including resources no IaC tool ever touched. Here is how to decide.
    linkedin: |
        Teams that block misconfigurations at deploy time often ask whether a CSPM tool is still worth buying. The honest answer depends on how much of your cloud estate your IaC actually manages.

        Policy as code evaluates a proposed change before it exists and can stop it. CSPM scans running accounts on a schedule and reports what it finds, including resources created in the console, by another tool, or by a cloud service itself. Each one has a blind spot the other covers.

        Our new post compares the two on timing, visibility, blocking authority, and where fixes happen, then lays out when you can wait on CSPM and when you cannot.
    bluesky: |
        Do you need CSPM if you enforce policy in your IaC?

        Deploy-time policy blocks bad changes. CSPM finds what already exists, including unmanaged resources. We compare both and say when you need each.
---

Many teams running production workloads in the cloud end up needing both, but enforcing policy in your infrastructure as code changes what you need CSPM for. Policy as code blocks misconfigurations before a managed change deploys. Cloud security posture management (CSPM) continuously finds what already exists, including resources your IaC never touched.

<!--more-->

## What does CSPM do?

CSPM tools connect to your cloud accounts through provider APIs and check the configuration of what they find against rules and compliance frameworks. Microsoft describes [cloud security posture management](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-cloud-security-posture-management) as providing "continuous visibility into the security state of your cloud assets and workloads, offering actionable guidance to improve your security posture in Azure, AWS, and GCP." AWS describes [Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) as providing "a comprehensive view of your security state in AWS" and helping you "assess your AWS environment against security industry standards and best practices."

Three traits define the category:

- **It looks at running infrastructure.** A CSPM tool inspects resources after they exist, whoever or whatever created them.
- **It runs continuously.** Scans repeat on a schedule or react to change events, so a setting changed by hand next week still gets caught.
- **It reports.** The output is findings, scores, and prioritized issues. Someone then decides what to fix and where.

Vendors package this differently. As of November 2026, [Wiz](https://www.wiz.io/solutions/cspm) describes agentless scanning mapped onto a security graph, with more than 2,800 cloud configuration rules and over 250 built-in frameworks such as PCI DSS and the CIS Benchmarks, plus attack path analysis. [Orca](https://orca.security/platform/cloud-security-posture-management-cspm/) describes its CSPM as detecting "misconfigurations and compliance risks across cloud environments," and [Palo Alto Networks Cortex Cloud](https://www.paloaltonetworks.com/cortex/cloud) describes unifying posture, identity, data, and AI security. In addition, the large clouds ship their own posture tooling, including Microsoft Defender for Cloud, AWS Security Hub CSPM, and [Google Security Command Center](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview).

Disclosure: Wiz is a Pulumi customer and uses Pulumi to run its own infrastructure. This post describes Wiz's products only from Wiz's public pages, and Wiz has not endorsed it.

## What does policy as code in your IaC do?

Policy as code means writing your infrastructure rules as version-controlled code and having an engine evaluate each proposed change against them. When the engine runs inside your IaC workflow, it sees the exact set of resources a change would create, modify, or delete before anything happens.

With Pulumi Policies, [preventative policy groups](/docs/discovery-governance/concepts/policy-as-code/policy-groups/) run during `pulumi preview` and `pulumi up`. A policy at the mandatory level stops the deployment when it fails. Policies can be written in TypeScript, JavaScript, Python, or OPA Rego, and they apply to any change that runs through Pulumi, whether an engineer, a CI job, or an AI coding agent authored it. For Terraform and OpenTofu, remote execution [evaluates the plan before apply](/docs/discovery-governance/concepts/policy-as-code/). The [policy as code tools roundup](/blog/best-policy-as-code-tools/) covers OPA, Sentinel, Kyverno, Checkov, Harness, and others if you work with a different engine.

The key property is timing. A violation caught in a preview never becomes a live resource, an alert, or an incident.

## How do deploy-time policy and posture scanning compare?

| | Policy as code in IaC | CSPM |
| --- | --- | --- |
| When it runs | Before a change is applied | After resources exist, repeatedly |
| What it sees | Resources the IaC tool is about to change | Resources in connected cloud accounts, whatever created them |
| Can it block? | Yes, at the mandatory enforcement level (advisory policies only warn) | Mostly reports findings; some products add auto-remediation, so check yours |
| Where the fix happens | In code, at the source | In the console, a ticket, or a pull request after the fact |
| Who writes the rules | Your team, plus pre-built packs | A vendor rule library, plus custom rules where the product supports them |
| Typical output | Pass, warn, or block on a change | Findings, risk scores, compliance reports |
| Main blind spot | Anything the IaC tool does not manage | Cannot stop a change that already happened |

## What does CSPM catch that IaC policy cannot?

A policy engine inside your IaC tool only evaluates what that tool manages. Pulumi's documentation puts it plainly: preventative groups "see only the resources Pulumi manages." Several real situations sit outside that boundary:

- **Console changes.** An engineer opens a security group during an incident and forgets to close it. No IaC run ever sees the change.
- **Resources from other tools.** Teams that run Terraform, CloudFormation, scripts, or a legacy pipeline next to Pulumi have infrastructure the Pulumi policy engine never evaluates.
- **Resources a cloud service creates.** Managed services spin up their own buckets, roles, and network interfaces. Nobody wrote code for them.
- **Drift.** A resource that passed policy at deploy time can change afterward. See [what infrastructure drift is](/topics/infrastructure-as-code/what-is-infrastructure-drift/) for how this happens.
- **Context across resources.** Products such as Wiz and Defender CSPM add attack path analysis and risk prioritization, which weigh how exposed resources connect to each other.

If your estate includes any of these in meaningful numbers, deploy-time policy leaves a gap that only scanning running accounts can close.

## What does IaC policy do that CSPM cannot?

CSPM reports on a misconfiguration after it exists. Even a fast finding means the resource ran in that state for some period, and someone has to chase the fix. IaC policy changes the sequence:

- **It blocks before the resource exists.** A public storage bucket that fails a mandatory policy never gets created.
- **It fixes at the source.** The failure shows up in the pull request or preview, next to the code that caused it. Pulumi can surface [policy violations as comments and checks](/docs/releases/changelog/) (added in September 2026) on GitHub, GitLab, Bitbucket, and Azure DevOps pull requests.
- **It gates agents.** When AI agents propose infrastructure changes, a mandatory policy applies the same standard to their changes as to anyone else's.
- **It can remediate in flight.** The remediate enforcement level adjusts a resource's properties so the deployment proceeds compliant.

A posture finding on a resource that should never have shipped is a ticket someone has to work, and a mandatory policy removes that ticket.

## When can you wait on a separate CSPM, and when do you need one?

Use this as a guide.

**You can probably wait if:**

- Nearly all your cloud resources are defined in IaC, and console write access is restricted or audited.
- You run a small number of accounts in one cloud.
- Your compliance needs are covered by policy packs, and you cover the gaps with your cloud provider's native posture tool, which is itself a basic CSPM.
- Your security team does not yet need runtime threat detection or workload vulnerability scanning.

**You likely need CSPM, or an audit capability, if:**

- Auditors ask you to show the compliance state of every resource in every account, including ones outside IaC.
- You operate many accounts, subscriptions, or projects across clouds, with teams that create resources independently.
- Part of your estate is unmanaged: ClickOps, acquired companies, or a migration in progress.
- Your security team needs attack paths, identity analysis, data exposure findings, or runtime signals.

Cloud providers' native tools offer a low-cost starting point. Microsoft notes that foundational CSPM in Defender for Cloud is [available at no cost](https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-cloud-security-posture-management), while its paid Defender CSPM plan adds attack path analysis and risk prioritization. Check each provider's current packaging before you decide.

## How does Pulumi Policies cover both ends?

Pulumi Policies includes preventative and audit policy groups. Preventative groups run in `pulumi preview` and `pulumi up` and can block. [Audit groups](/docs/discovery-governance/concepts/policy-as-code/policy-groups/) attach to cloud accounts, "scan on a schedule and cover every resource in the account, including resources created by hand, by another tool, or by a cloud service itself," and report without blocking. [Cloud account discovery](/docs/discovery-governance/concepts/discovery/cloud-accounts/) supports AWS, Azure, Google Cloud, Oracle Cloud, and Kubernetes, and scans every 24 hours by default, with a 12-hour option. Those scans are scheduled rather than event-driven, so check that cadence against your requirements.

[Pre-built policy packs](/docs/discovery-governance/guides/pre-built-policy-packs/) on the Enterprise edition cover CIS 8.1 for AWS, Azure, and GCP, CIS Kubernetes for EKS, AKS, and GKE, CMMC 2.0, HITRUST CSF 11.5, ISO/IEC 27001:2022, NIST SP 800-53 rev 5, and PCI DSS v4.0.1. Packs such as Pulumi Best Practices and AWS Organizations Tag Policies are available from Essentials. Results appear in [policy findings](/docs/discovery-governance/operations/policy-findings/), with compliance scores, framework views, prioritized issues, and a Remediate action that hands a finding to [Neo](/blog/10-more-things-you-can-do-with-neo/) for AI-assisted remediation.

Pulumi Policies is a policy and compliance product. It does not provide runtime threat detection, workload vulnerability scanning, or an attack path graph. A team that needs those capabilities still needs a CNAPP or a dedicated security platform next to it. Audit groups cover the configuration-and-compliance role of CSPM for connected accounts. One practical split is Pulumi Policies for prevention and compliance across managed and unmanaged resources, and a security platform for runtime and threat context.

## Frequently asked questions

### Is CSPM the same as policy as code?

No. CSPM scans running cloud resources and reports findings after the fact. Policy as code evaluates a proposed change against rules before it applies and can block it. They overlap on rules such as CIS controls, but they act at different points in the lifecycle and fail in different ways.

### Can policy as code replace CSPM for compliance audits?

Only when the estate is fully managed by IaC. Auditors usually want evidence about every resource in an account, including ones created by hand. Policy as code gives strong evidence for managed changes. To cover the rest, you need scheduled account scans, which is what audit policy groups or a CSPM tool provide.

### What is the difference between CSPM and CNAPP?

A cloud-native application protection platform (CNAPP) generally bundles CSPM with other capabilities, such as workload protection, vulnerability management, and runtime detection. CSPM is the configuration-and-compliance part. Check each vendor's own definition, because products package these capabilities differently.

### Does shifting policy left reduce CSPM alerts?

It reduces alerts about managed resources, because misconfigurations that fail a mandatory policy never deploy. Alerts about hand-made resources, drift, and resources from other tools remain. Expect the remaining alerts to come from those unmanaged sources.

## Start with prevention, then add visibility

Try a pack locally with `pulumi preview --policy-pack <path>` against any backend, and follow the [enforce policy as code guide](/docs/discovery-governance/get-started/enforce-policy-as-code/) to move from advisory to mandatory. Then [connect a cloud account](/docs/discovery-governance/guides/connect-cloud-accounts/) to see what an audit scan finds outside your stacks. Learn more about the [Pulumi Policies product](/product/discovery-governance/) and [what policy as code is](/topics/secrets-and-security/what-is-policy-as-code/).
