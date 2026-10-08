---
title_tag: "Pulumi ESC: Customer managed keys"
meta_desc: Bring your own encryption keys to protect data within Pulumi Cloud for enhanced security and compliance.
title: Customer managed keys
h1: Customer managed keys
menu:
  esc:
    parent: esc-concepts
    weight: 13
aliases:
  - /docs/esc/administration/customer-managed-keys/
pulumi_cloud_feature: customer-managed-keys
---

## Overview

Pulumi ESC supports customer managed keys (CMKs) to improve the security and compliance of your data. CMKs allow you
to use your own encryption keys to protect secrets in Pulumi ESC through an external
Key Management System (KMS).

CMKs encrypt data keys, which are used to encrypt secrets in Pulumi ESC. When you add your first CMK, all
existing data keys encrypted with the Pulumi-managed key will be automatically re-encrypted with the new CMK. The
encrypted secrets do not change.

Only organization admins can manage CMKs.

{{% notes type="info" %}}
Currently, customer managed keys support keys from AWS KMS and are only used to encrypt data stored in Pulumi ESC.
We are working on adding support for more KMS providers and expanding encryption to additional Pulumi products. If you
have specific requirements, please [contact us](/contact/).
{{% /notes %}}

## Why use customer managed keys?

Customer managed keys (CMKs) give you control over the encryption of your secrets in Pulumi ESC. By using your
own keys, you can:

- Meet strict security and compliance requirements.
- Control key access and auditing.
- Revoke access or disable keys if needed.

This approach enhances data security and aligns with organizational or regulatory policies.

## Customer managed keys documentation

For how customer managed keys work and how to view or disable them, see
[Customer managed keys](/docs/administration/concepts/customer-managed-keys/). To set one up, follow the
[AWS KMS](/docs/administration/guides/customer-managed-keys/aws-kms/) guide.
