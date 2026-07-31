---
title: "FedRAMP Remediation Workflows with Pulumi Policies and Neo"
date: 2026-05-28
authors:
    - pablo-seibelt
meta_desc: "Use Pulumi Policies and Neo-assisted remediation to triage FedRAMP findings, review previews, and capture evidence without claiming certification."
meta_image: meta.png
feature_image: feature.png
tags:
    - compliance
    - fedramp
    - policy-as-code
social:
    twitter: |
        FedRAMP remediation is review work, not magic.

        Use Pulumi Policies and Neo-assisted changes to triage findings, preview fixes, and capture evidence.
    linkedin: |
        FedRAMP remediation needs traceable decisions: what failed, what changed, who reviewed it, and what evidence remains.

        This guide shows how Pulumi Policies and Neo-assisted remediation can support that workflow without claiming certification.
    bluesky: |
        FedRAMP remediation needs traceable fixes.

        Pulumi Policies plus Neo-assisted changes can help triage, preview, review, and capture evidence.
---

Achieving [FedRAMP](https://www.fedramp.gov/) readiness is a significant milestone for organizations that need to meet FedRAMP authorization requirements. Compliance work needs to live in the same workflow as infrastructure changes, but the path to FedRAMP readiness is often paved with complex controls, rigorous documentation requirements, and the constant challenge of maintaining a compliant state. Traditional compliance workflows are often reactive, relying on manual audits and late-stage security scans that slow down development cycles.

Pulumi is transforming this process by bringing compliance into the infrastructure as code (IaC) lifecycle. By combining **[Pulumi Policies](/docs/insights/policy/)** for preventative policy enforcement and **[Pulumi Neo](/product/neo/)** for AI-assisted remediation, teams can automate policy checks, triage findings efficiently, and support continuous compliance workflows.

This post outlines a documentation and remediation workflow that assists teams in meeting FedRAMP requirements. Note that while Pulumi tools support compliance efforts, they do not guarantee authorization or provide automated certification.

<!--more-->

## Mapping FedRAMP controls to infrastructure as code

FedRAMP controls, based on [NIST SP 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final), cover a wide range of security requirements. Many of these controls directly relate to how cloud infrastructure is configured. For example, controls related to Access Control (AC), Identification and Authentication (IA), and System and Information Integrity (SI) often translate to specific cloud resource settings.

By expressing these controls as code, you can move from abstract compliance requirements to concrete, enforceable policies. Pulumi Policies allows you to write these policies in familiar languages like TypeScript, JavaScript, or Python, ensuring that every resource deployment is checked against your compliance baseline.

## Preventative guardrails with Pulumi Policies

The most effective way to maintain compliance is to prevent non-compliant resources from being created in the first place. Pulumi Policies enables this by running policy checks during `pulumi preview` and `pulumi up`.

For FedRAMP, this means you can enforce rules such as:

1. **Encryption at rest:** Ensure all S3 buckets, RDS instances, and EBS volumes use approved encryption keys.
1. **Network isolation:** Prevent public access to sensitive databases or internal services.
1. **Identity management:** Enforce multi-factor authentication (MFA) and least-privilege access for IAM roles.

Here is a representative snippet of a Pulumi policy enforcing encryption configuration for S3 buckets:

```typescript
import * as aws from "@pulumi/aws";
import { PolicyPack, validateResourceOfType } from "@pulumi/policy";

new PolicyPack("fedramp-compliance", {
    policies: [{
        name: "s3-bucket-encryption-enabled",
        description: "Ensure S3 encryption configuration resources use AES256 or AWS KMS (FedRAMP SC-28).",
        enforcementLevel: "mandatory",
        validateResource: validateResourceOfType(aws.s3.BucketServerSideEncryptionConfiguration, (config, args, reportViolation) => {
            for (const rule of config.rules ?? []) {
                const algorithm = rule.applyServerSideEncryptionByDefault?.sseAlgorithm;
                if (algorithm !== "AES256" && algorithm !== "aws:kms") {
                    reportViolation("S3 encryption configuration must use AES256 or AWS KMS.");
                }
            }
        }),
    }],
});
```

For broad framework coverage, start with Pulumi's [pre-built compliance policy packs](/docs/insights/policy/policy-packs/pre-built-packs/), then add custom policies for organization-specific controls. [Pulumi Business Critical](/pricing/) includes built-in policies that help organizations evaluate and enforce controls for frameworks such as NIST SP 800-53, then extend them with custom rules for their own environment.

## Neo-assisted remediation workflow

Even with preventative guardrails, existing infrastructure may have compliance gaps, or new policy requirements may be introduced. This is where **[Policy Findings](/docs/insights/policy/policy-findings/)** and **Pulumi Neo** come into play.

When a Pulumi policy identifies a violation in an existing stack, it appears in Policy Findings. This centralized view allows security and platform teams to triage issues, assess risk, and assign remediation tasks.

Instead of manually researching the fix and updating the code, you can use Pulumi Neo to assist with remediation. By providing Neo with the context of the violation, it can suggest the necessary code changes to bring the resource into compliance.

### Example remediation prompt

You can use Pulumi Neo where it is available in your workflow to request a remediation plan:

> "Neo, I have a FedRAMP violation for `s3-bucket-encryption-enabled` on the `production-data` bucket. Update the Pulumi code to enable AES256 server-side encryption for this bucket."

Neo can help analyze your existing program and propose a draft change set. You can then review the proposed changes, run a preview to verify the fix, and deploy the update. This workflow can reduce remediation time while keeping review and deployment under your control.

## Continuous re-validation and evidence

Compliance is not a one-time event; it's a continuous process. Pulumi provides the tools to maintain and prove compliance over time:

1. **Policy Findings triage:** Track the lifecycle of every compliance issue from discovery to resolution.
1. **Advisory enforcement:** Use advisory enforcement, or assign packs to an audit-mode policy group, so violations surface in Policy Findings without blocking deployments.
1. **Evidence generation:** Use the history of policy checks and remediation actions as evidence for auditors, demonstrating that controls are actively enforced or monitored.

## Compliance disclaimer

While Pulumi helps produce evidence and provides powerful guardrails to support your compliance journey, using Pulumi does not guarantee FedRAMP authorization or legal compliance. Organizations are responsible for ensuring their overall system architecture, operational procedures, and documentation meet the specific requirements of the FedRAMP program and their authorizing agency.

## Conclusion

FedRAMP compliance doesn't have to be a bottleneck for innovation. By integrating Pulumi Policies and Neo into your workflow, you can automate policy checks, accelerate remediation, and build a culture of continuous compliance review. Whether you are just starting your FedRAMP journey or looking to optimize your existing processes, start by mapping one FedRAMP finding to a [Pulumi policy](/docs/insights/policy/) and routing the resulting policy findings into your review workflow.
