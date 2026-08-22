---
title: Pulumi Security
meta_desc: Pulumi's security posture — SOC 2 Type II attestation, what we do and don't certify, platform architecture, and how to report a vulnerability.
aliases:
  - /trust/
  - /trust-center/
---

Pulumi takes security and privacy matters very seriously. We appreciate that our customers and users place a high degree of confidence and trust in our products and services and we strive to meet those expectations.

## Certifications and attestations

Pulumi Cloud is covered by an annual **SOC 2 Type II** audit performed by an independent CPA firm against the AICPA Trust Services Criteria. The report is shared under NDA — request it from your account team or email [security@pulumi.com](mailto:security@pulumi.com).

Pulumi does not currently hold ISO 27001, HITRUST, or PCI DSS certification. Customers in regulated industries do run Pulumi under those frameworks, because Pulumi Cloud never receives your cloud credentials and never has standing access to your cloud accounts — the architecture that makes this true is described in the [security whitepaper](/security/pulumi-cloud-security-whitepaper/).

Pulumi also publishes [pre-built policy packs](/docs/insights/policy/policy-packs/pre-built-packs/) for CIS, ISO/IEC 27001, NIST SP 800-53, CMMC, HITRUST, and PCI DSS. Those help you assess *your* infrastructure against a framework; they are not a statement about Pulumi's own certification status.

## Government and federal programs

Pulumi holds **no FedRAMP authorization**. There is no Pulumi ATO and no listing in the FedRAMP Marketplace. A program that requires a FedRAMP-authorized service cannot use hosted Pulumi Cloud to satisfy that requirement.

[Self-hosted Pulumi Cloud](/product/self-hosted/) changes who owns the boundary. Because you install and operate it in your own environment, it is a software component in your inventory, and the controls that apply to it are yours. It can run fully [air-gapped](/docs/administration/self-hosting/airgapped/), with no egress to the public internet.

## Architecture and controls

The [security whitepaper](/security/pulumi-cloud-security-whitepaper/) is the technical reference for how Pulumi Cloud is built and operated. It covers the service architecture and data storage model, the three-tier encryption key hierarchy and its KMS integration, organizational key isolation and key rotation, transport security, how secrets are handled in stack state, diagnostic log protection, audit logging, monitoring, incident detection and response, vulnerability management, and backup, recovery, and business continuity.

## Data processing

Pulumi's [Privacy Statement](/privacy/) describes what personal data we collect and how it is handled, including transfers out of the EEA under standard contractual clauses. For a Data Processing Addendum, or for questions about data processing in a procurement review, contact [privacy@pulumi.com](mailto:privacy@pulumi.com).

## Vulnerability Reporting

If you believe you’ve discovered a potential vulnerability in Pulumi’s security, please contact us at [security@pulumi.com](mailto:security@pulumi.com). For non-critical matters please file an issue with [Pulumi support](https://support.pulumi.com/).

When reporting a potential vulnerability, please include as much of the following information as possible.

* A description of the vulnerability
* The impacted software or service and its version
* Proof-of-concept code and/or detailed steps to reproduce

## Secure Communications

If you're a security researcher and you believe that you have found a security issue within any of our services, email the details of your findings to [security@pulumi.com](mailto:security@pulumi.com). Use PGP to protect the message by using our public PGP key.

```
-----BEGIN PGP PUBLIC KEY BLOCK-----

mDMEaTdfzRYJKwYBBAHaRw8BAQdAMI5zxX4G2lJFFjz9M5n/t6WUpnu9FW2kDiXQ
XjRQTgG0QFB1bHVtaSBTZWN1cml0eSAoVXNlZCBmb3Igc2VjdXJpdHkgZW1haWxz
KSA8c2VjdXJpdHlAcHVsdW1pLmNvbT6IkAQTFgoAOBYhBFXmCEjgBWlIOhKlENLN
ObkHnPHMBQJpN1/NAhsjBQkSzAMAAgsJAhUKBRYCAwEAAh4FAheAAAoJENLNObkH
nPHMSs0A/3MFjjOvfFRadgEI14oCK/D6VL3Aa9WU372j178mthnHAP9jlRTjmxYP
peC2V9ay2Yy/xn9FvlcJhBmeAgRXbAFKD7g4BGk3X80SCisGAQQBl1UBBQEBB0Dy
vnyK9rDvBeTz3vThDB3pUt6cRIZGfQ87X/MRSHxfUwMBCAeIfgQYFgoAJhYhBFXm
CEjgBWlIOhKlENLNObkHnPHMBQJpN1/NAhsMBQkSzAMAAAoJENLNObkHnPHMz7cA
/1Wf80ySXPLjXlw6r8KfGIdwvwHgCKzy5dQmWZzHBGRWAP9FVQpmGtZLZHWZcSxG
bwot7iZeSNSh5+MyteVaez6pAQ==
=GU0r
-----END PGP PUBLIC KEY BLOCK-----
```

## Public Notifications

Public security notifications are posted in the **#announcements** channel of the [Pulumi Community on Slack](https://slack.pulumi.com/).
