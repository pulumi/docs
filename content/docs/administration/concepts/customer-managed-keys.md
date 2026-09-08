---
title_tag: "Pulumi Cloud: Customer managed keys"
meta_desc: Bring your own encryption keys to protect data within Pulumi Cloud for enhanced security and compliance.
title: "Customer managed keys"
h1: Customer managed keys
menu:
  administration:
    parent: administration-concepts
    weight: 10
    identifier: administration-concepts-customer-managed-keys
aliases:
  - /docs/pulumi-cloud/customer-managed-keys/
  - /docs/pulumi-cloud/admin/customer-managed-keys/
  - /docs/administration/security-compliance/customer-managed-keys/
pulumi_cloud_feature: customer-managed-keys
---

## Overview

Pulumi Cloud supports customer managed keys (CMKs) to improve the security and compliance of your data. CMKs allow you
to use your own encryption keys to protect sensitive data in Pulumi Cloud through an external
Key Management System (KMS).

CMKs encrypt data keys, which are used to encrypt data in Pulumi Cloud. When you add your first CMK, all
existing data keys encrypted with the Pulumi-managed key will be automatically re-encrypted with the new CMK. The
encrypted data itself does not change.

Only organization admins can manage CMKs.

{{% notes type="info" %}}
Currently, customer managed keys are only used to encrypt data in Pulumi ESC, and only AWS KMS is
supported.
We are working on adding support for more KMS providers and expanding encryption to additional Pulumi products. If you
have specific requirements, please [contact us](/contact/).
{{% /notes %}}

## Viewing customer managed keys

To view customer managed keys:

1. As an admin, expand the organization’s **Settings** menu.
1. Select **Organization**.
1. Select the **Customer Managed Keys** tab.

The Customer Managed Keys page displays the following details for each key:

- **Name**: The unique name of the key provided by an admin.
- **Type**: The encryption key type, such as AWS KMS.
- **Default**: Indicates if the key is the default encryption key for the organization. All new data keys responsible
  for encrypting data created by your organization will be encrypted with this key.
- **Set as default**: A button to set the key as the default encryption key. This option is unavailable for keys already
  set as default or undergoing re-encryption.
- **Disable**: A button to disable the key. This option is unavailable for default keys or keys undergoing
  re-encryption.

## Adding a customer managed key

Adding a customer managed key means preparing a key in your key management system and then registering it with Pulumi
Cloud, so that your own key protects sensitive data. For the full procedure, see
[AWS KMS](/docs/administration/guides/customer-managed-keys/aws-kms/).

{{% notes type="info" %}}
When the first customer managed key is added, all data keys encrypted with the Pulumi-managed key will be automatically
re-encrypted with the new customer managed key. The encrypted data itself does not change.
{{% /notes %}}

## Disabling a customer managed key

Disabling a key prevents it from being used to create new data keys, but existing data keys remain encrypted with the
key until they are re-encrypted. You must specify a re-encryption key to re-encrypt existing data keys.

Disabling a key is not available for default keys or keys undergoing re-encryption.

To disable a customer managed key:

1. Click the three-dot menu next to the key you want to disable.
2. Select **Disable**.
3. Choose a re-encryption key to re-encrypt existing data keys.
4. Click **Disable** to confirm.
5. A banner will appear, showing the re-encryption process status. It disappears once the process is complete.

## Disabling all customer managed keys

Disabling all keys prevents them from being used to create new data keys, but existing data keys remain encrypted with
the keys until they are re-encrypted. All data keys will be re-encrypted with the Pulumi-managed key.

To disable all customer managed keys:

1. Click on the wheel button in the top right corner.
2. Click **Disable all Customer Managed Keys**.
3. Confirm the re-encryption process in the dialog that appears.
4. Click **Disable all** to confirm.
5. A banner will appear, showing the re-encryption process status. It disappears once the process is complete.
