---
title: "Bring Your Own Keys With Pulumi ESC"
date: 2025-06-18T13:25:26-03:00
draft: false
meta_desc: "You can Bring Your Own Keys (BYOK) to encrypt secrets on Pulumi ESC."
meta_image: meta.png
canonical_url: "https://www.pulumi.com/docs/pulumi-cloud/admin/customer-managed-keys/"
authors:
    - pablo-terradillos
    - boris-schlosser
tags: ["esc", "aws", "features", "secrets"]
---

Today we’re excited to launch support for Customer-Managed Keys (CMKs) in Pulumi ESC. This feature gives your organization full control over how your secrets and state are encrypted — empowering you to meet the most demanding compliance requirements like HIPAA, GDPR, and FedRAMP, all while maintaining the ease-of-use that Pulumi is known for.

<!--more-->

## Why Customer-Managed Keys?

Pulumi encrypts secrets and other sensitive information stored in ESC using data keys, which are encrypted with Pulumi-Managed Keys using strong security standards. However, customers might need to use their own keys to gain full control over their lifecycle and revocation, maintain a centralized audit trail, and enforce custom rotation policies. This is especially important to meet compliance requirements or specific regulations (e.g., HIPAA, GDPR, FedRAMP, etc).  Customer-Managed Keys give customers that control while keeping these aspects transparent for the consumers of those secrets.

## How It Works

Customer-Managed Keys integrate seamlessly with your Pulumi Cloud Organization. Once enabled, all existing data keys used to encrypt your ESC secrets, previously encrypted with the Pulumi-managed key, will be automatically re-encrypted with the new CMK.

Setting it up takes just a few minutes:

1. **Create** a KMS key in your AWS account.  
2. **Grant Access** to the KMS key using OIDC in your AWS account.  
3. **Configure** your Pulumi Cloud organization to use your new KMS key.

## Available Today

Customer-managed keys with support for AWS KMS are available today for all organizations on the **Pulumi Enterprise** or **Business Critical** plans. You can set it up by following the instructions [in the Pulumi Cloud documentation.](https://www.pulumi.com/docs/pulumi-cloud/admin/customer-managed-keys)

We expect to add support for more cloud providers in the future. Please vote on the following GitHub issues for your favorite to support prioritization:

* [Azure Key Vault](https://github.com/pulumi/pulumi-cloud-requests/issues/521)  
* [Google Cloud KMS](https://github.com/pulumi/pulumi-cloud-requests/issues/522)

## Share Your Feedback

We’re excited to see how Customer-Managed Keys help you and your organization meet your compliance goals with Pulumi Cloud. Your feedback is essential as we continue to evolve this feature:

* Connect with us in the [Pulumi Community Slack](https://slack.pulumi.com)  
* Open an issue on [GitHu](https://github.com/pulumi/pulumi)
* Read the full documentation on [Customer-Managed Keys](https://www.pulumi.com/docs/pulumi-cloud/admin/customer-managed-keys)

Try this today, [Get Started with Pulumi for free](https://pulumi.com/start)
