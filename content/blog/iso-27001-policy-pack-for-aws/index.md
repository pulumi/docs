---
title: "Enforce ISO 27001 Across Your AWS Infrastructure"
date: 2026-06-30
authors:
    - dan-biwer
meta_desc: "Align your AWS infrastructure to ISO/IEC 27001:2022 with a pre-built Pulumi policy pack of 238 ready-to-run security policies."
meta_image: meta.png
feature_image: feature.png
tags:
    - pulumi-cloud
    - policy-as-code
    - crossguard
    - features
    - compliance
    - governance
    - security
category: product
schema_type: auto
social:
    twitter: |
        ISO 27001 compliance on AWS has always meant months of work: interpret each governance control, decide what it means for an S3 bucket or RDS instance, then author a custom check.

        We built a pack of 238 policies that does the interpretation for you.
    linkedin: |
        ISO/IEC 27001 is the international benchmark for information security management, and one of the most common hard requirements in enterprise procurement and cross-border deals.

        The problem has always been translation. The standard's controls are written in the language of governance and risk, not in the language of cloud resources. Every team has had to interpret each control and decide what it means for an S3 bucket, an RDS instance, a CloudTrail trail.

        We built a policy pack to remove that work.

        Today we're shipping iso-27001-aws, a pre-built pack of 238 policies, live in Pulumi Cloud now. Each policy maps back to the relevant ISO 27001 control, so findings connect directly to the standard instead of leaving you to make the connection yourself.

        The pack works two ways: one to get compliant, one to stay that way. The details are in the post.

        The link is in the comments.
    bluesky: |
        ISO 27001 compliance on AWS has meant months of mapping governance controls to actual cloud resources, interpreting each one for S3, RDS, CloudTrail.

        We built 238 policies to handle that mapping. Live today in Pulumi Cloud.
---

ISO/IEC 27001 is the international standard for information security management. Proving you meet it usually means months of mapping abstract security controls to concrete cloud configuration, then authoring custom checks one resource at a time. We're changing that.

<!--more-->

Today we're shipping a pre-built ISO/IEC 27001:2022 policy pack for AWS, live now in Pulumi Cloud as `iso-27001-aws`. It encodes the standard's security expectations as 238 ready-to-run policies, so you can align your AWS estate to ISO 27001 in minutes, not months.

## Why ISO 27001 matters

ISO/IEC 27001 is the globally recognized standard for an information security management system (ISMS). Unlike a regional regulation, it's a worldwide benchmark, which is why it shows up so often as a hard requirement in enterprise procurement and cross-border deals. It's SOC 2-adjacent in spirit, since both attest that you manage security risk systematically, but ISO 27001 carries broader international recognition that buyers around the world already trust.

## How the pack maps to ISO 27001

The hard part of ISO 27001 has always been translation: its controls are written in the language of governance and risk management, not in the language of AWS resources. Every team has had to interpret each control and decide what it means for an S3 bucket or an RDS instance.

The pack does that interpretation for you. Its 238 policies are aligned to the relevant ISO 27001 controls, so each result connects back to the standard instead of leaving you to map it yourself. You can browse the full pack in the [pack reference](/docs/reference/pre-built-policy-packs/iso-27001/aws/).

## Audit and prevent

The same pack works two ways, so you can both reach compliance and stay there:

1. **Audit.** Scan your existing AWS estate against the pack, including resources that Pulumi doesn't manage. You get an honest baseline of where you stand against ISO 27001 today, with every finding tied back to the control it affects.
1. **Prevent.** Run the same pack as a preventative policy during `pulumi up` to block non-compliant resources before they're ever created. New infrastructure is born aligned to the standard.

Audit gets you clean. Preventative policies keep you clean.

## A growing library of pre-built packs

ISO 27001 joins a growing library of pre-built packs for AWS, each authored and maintained by Pulumi and kept current with its source standard:

- **ISO/IEC 27001:2022** (new)
- **CIS Controls v8.1**
- **NIST SP 800-53 Rev. 5**
- **PCI DSS v4.0**
- **HITRUST CSF v11.5**
- **Pulumi Best Practices**

Adopting any pack means you skip the authoring work entirely, inherit framework mappings maintained by Pulumi, and apply a consistent baseline across every stack and account.

## Get started today

The ISO 27001 pack is available now to every Pulumi Cloud user:

1. Browse the [pack reference](/docs/reference/pre-built-policy-packs/iso-27001/aws/) to see all 238 policies and how they map to the standard's controls.
1. Explore the full [pre-built packs index](/docs/insights/policy/policy-packs/pre-built-packs/).
1. Follow the [get-started guide](/docs/insights/policy/get-started/) to run your first audit.

## Try Pulumi policies

Ready to align your AWS infrastructure to ISO 27001? [Sign up for Pulumi Cloud](https://app.pulumi.com/signup) and run the pack against your estate, or read the [policy get-started guide](/docs/insights/policy/get-started/) to dig in.

Need a compliance pack for a framework that isn't listed here? Open a request in [pulumi/pulumi-cloud-requests](https://github.com/pulumi/pulumi-cloud-requests) or come tell us in the [community Slack](https://slack.pulumi.com/). We're listening.
