---
title: Pulumi Security
meta_desc: A summary of security topics and how they relate to the Pulumi platform.
layout: security
---

Pulumi takes security and privacy matters very seriously. We appreciate that our customers and users place a high degree of confidence and trust in our products and services and we strive to meet those expectations.

## Pulumi Service Security

<!-- markdownlint-disable url -->
Pulumi Service, our managed service for using Pulumi open source, is multi-tenanted and runs within an AWS Virtual Private Cloud (VPC), whose only Internet-addressable endpoints are https://api.pulumi.com or https://app.pulumi.com. All communications between Pulumi clients and the server are encrypted using TLS. Pulumi is SOC 2 Type II certified.
<!-- markdownlint-enable url -->

For more details on Pulumi’s product architecture and security practices, please read our [security whitepaper](/security/pulumi-cloud-security-whitepaper.pdf) (last updated October 24, 2022).

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
