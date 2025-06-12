---
title_tag: "Pulumi Cloud: Customer Managed Keys"
meta_desc: Bring your own encryption keys to protect data within Pulumi Cloud for enhanced security and compliance.
title: "Customer Managed Keys"
h1: Customer Managed Keys
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: Customer Managed Keys
    parent: pulumi-cloud-admin
    weight: 4
    identifier: pulumi-cloud-admin-customer-managed-keys
aliases:
  - /docs/pulumi-cloud/customer-managed-keys/
---

{{% notes "info" %}}
Customer Managed Keys are available for organizations using the Enterprise and Business Critical editions.
Learn more about editions on the [pricing page](/pricing/).
{{% /notes %}}

## Overview

Pulumi Cloud supports Customer Managed Keys (CMKs) to improve the security and compliance of your data. CMKs allow you
to use your own encryption keys to protect sensitive data in Pulumi Cloud through an external
Key Management System (KMS).

Customer Managed Keys encrypt data keys, which are used to secure secrets in Pulumi Cloud. When you add your first CMK,
all existing data keys encrypted with the Pulumi-managed key will be re-encrypted with the new CMK automatically.

## Viewing Customer Managed Keys

Customer Managed Keys are available in the Enterprise and Business Critical editions. Only organization admins can view
them.

To view Customer Managed Keys:

1. Go to the organization’s **Settings**.
2. Select **Customer Managed Keys**.

The Customer Managed Keys page displays the following details for each key:

- **Name**: The unique name of the key provided by an admin.
- **Type**: The encryption key type, such as AWS KMS or Azure Key Vault.
- **Default**: Indicates if the key is the default encryption key for the organization. Means it is used to encrypt new
  data keys.
- **Set as default**: A button to set the key as the default encryption key. This option is unavailable for keys already
  set as default or undergoing re-encryption.
- **Disable**: A button to disable the key. This option is unavailable for default keys or keys undergoing
  re-encryption.

## Adding a Customer Managed Key

To add a Customer Managed Key, you must be an organization admin. Ensure the key is created in the external KMS and
access is configured using OIDC.

{{% notes "info" %}}
When the first CMK is added, all data keys encrypted with the Pulumi-managed key will be re-encrypted with the new CMK
automatically.
{{% /notes %}}

### AWS KMS

1. Set up a role in AWS IAM and a key in AWS KMS as
   described [here](/docs/pulumi-cloud/admin/customer-managed-keys/aws-kms/).
2. Go to the **Customer Managed Keys** settings page in Pulumi Cloud.
3. Click **Add Customer Managed Key**.
4. Enter a unique name for the key.
5. Provide the **Role ARN** with access to the AWS KMS key.
6. Provide the **Key ARN** of the AWS KMS key. Alias ARNs are also supported.

## Disabling a Customer Managed Key

To disable a Customer Managed Key, you must be an organization admin. Disabling a key prevents it from being used to
create new data keys, but existing data keys remain encrypted with the key. You must specify a re-encryption key to
re-encrypt existing data keys.

Disabling a key is not available for default keys or keys undergoing re-encryption.

To disable a Customer Managed Key:

1. Click the three-dot menu next to the key you want to disable.
2. Select **Disable**.
3. Choose a re-encryption key to re-encrypt existing data keys.
4. Click **Disable** to confirm.
5. A banner will appear, showing the re-encryption process status. It disappears once the process is complete.

## Disabling All Customer Managed Keys

To disable all Customer Managed Keys, you must be an organization admin. Disabling all keys prevents them from being
used to create new data keys, but existing data keys remain encrypted with the keys. All data keys will be re-encrypted
with the Pulumi-managed key.

To disable all Customer Managed Keys:

1. Click **Disable all Customer Managed Keys**.
2. Confirm the re-encryption process in the dialog that appears.
3. Click **Disable all** to confirm.
4. A banner will appear, showing the re-encryption process status. It disappears once the process is complete.

## Restrictions

Currently, Customer Managed Keys have the following limitations:

1. They are only used to encrypt data keys for secrets in Pulumi ESC.
2. Only AWS KMS is supported.

We are working on adding support for more KMS providers and expanding encryption to additional Pulumi products. If you
have specific requirements, please [contact us](/contact/).
