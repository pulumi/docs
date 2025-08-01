---
title_tag: "Pulumi ESC: Customer Managed Keys"
meta_desc: Bring your own encryption keys to protect data within Pulumi Cloud for enhanced security and compliance.
title: Customer Managed Keys
h1: Customer Managed Keys
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  esc:
    parent: pulumi-esc-admin
    weight: 3
---

{{% notes "info" %}}
Customer Managed Keys are available for organizations using the Enterprise and Business Critical editions.
Learn more about editions on the [pricing page](/pricing/).
{{% /notes %}}

## Overview

Pulumi ESC supports Customer Managed Keys (CMKs) to improve the security and compliance of your data. CMKs allow you
to use your own encryption keys to protect secrets in Pulumi ESC through an external
Key Management System (KMS).

CMKs encrypt data keys, which are used to encrypt secrets in Pulumi ESC. When you add your first CMK, all
existing data keys encrypted with the Pulumi-managed key will be automatically re-encrypted with the new CMK. The
encrypted secrets do not change.

Only organization admins can manage CMKs.

{{% notes "info" %}}
Currently, Customer Managed Keys support keys from AWS KMS and are only used to encrypt data stored in Pulumi ESC.
We are working on adding support for more KMS providers and expanding encryption to additional Pulumi products. If you
have specific requirements, please [contact us](/contact/).
{{% /notes %}}

## Why use Customer Managed Keys?

Customer Managed Keys (CMKs) give you control over the encryption of your secrets in Pulumi ESC. By using your
own keys, you can:

- Meet strict security and compliance requirements.
- Control key access and auditing.
- Revoke access or disable keys if needed.

This approach enhances data security and aligns with organizational or regulatory policies.

## Customer Managed Keys documentation

See the [Customer Managed Keys](/docs/pulumi-cloud/admin/customer-managed-keys/) documentation for complete usage
instructions.
