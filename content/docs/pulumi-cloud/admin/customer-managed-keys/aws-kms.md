---
title_tag: "AWS KMS"
meta_desc: "Learn how to configure AWS KMS for Pulumi Cloud Customer Managed Keys to enhance security and compliance."
title: "AWS KMS"
h1: "AWS KMS"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: "AWS KMS"
    parent: pulumi-cloud-admin-customer-managed-keys
    weight: 1
    identifier: pulumi-cloud-admin-customer-managed-keys-aws-kms
aliases:
  - /docs/pulumi-cloud/customer-managed-keys/aws-kms/
---

This guide provides step-by-step instructions for configuring AWS Key Management Service (KMS) to use [Customer Managed
Keys (CMKs) with Pulumi Cloud](/docs/pulumi-cloud/admin/customer-managed-keys/). It covers setting up the necessary AWS
IAM roles, trust policies, and KMS key permissions
to enhance the security and compliance of your Pulumi Cloud environment.

## Prerequisites

* You must have sufficient AWS IAM and KMS privileges to create identity providers, IAM roles and KMS keys.

{{< notes type="warning" >}}
Please note that this guide provides step-by-step instructions based on the official provider documentation which is
subject to change. For the most current and precise information, always refer to
the [official AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html).
{{< /notes >}}

## Create the identity provider

1. In the navigation pane of the [IAM console](https://console.aws.amazon.com/iam/), choose **Identity providers**, and
   then choose **Add provider**.
2. In the **Provider type** section, click the radio button next to **OpenID Connect**.
3. For the **Provider URL**, provide the following URL: `https://api.pulumi.com/oidc`
4. For the **Audience** field, the value is the name of your Pulumi organization prefixed with `aws:` (e.g.
   `aws:{org}`). Then click **Add provider**.

## Configure the IAM role

Once you have created the identity provider, you will see a notification at the top of your screen prompting you to
assign an IAM role.

1. Click the **Assign role** button.
2. Select the **Create a new role** option, then click **Next**.
3. On the IAM **Create role** page, ensure the **Web identity** radio button is selected.
4. In the **Web identity** section:
    * Select `api.pulumi.com/oidc` under **Identity provider**.
    * Select the name of your Pulumi organization under **Audience**. Then click **Next**.
5. Skip the **Add permissions** page by clicking **Next**.
6. Provide a name and optional description for the IAM role. Then click **Create role**.

## Review trust policy

Next, select the **trust relationships** tab, which is where the trust policy of the role is defined. Ensure audience
and subject are configured as shown below:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::123456789012:oidc-provider/api.pulumi.com/oidc"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "api.pulumi.com/oidc:aud": "aws:<pulumi-org-name>",
          "api.pulumi.com/oidc:sub": "pulumi:cmk:pulumi.organization.login:<pulumi-org-name>"
        }
      }
    }
  ]
}
```

Before you log out of the AWS console, make sure to make a note of your role’s ARN value as you will need it to set up
the AWS KMS key as well as the Customer Managed Key in Pulumi Cloud.

## Create the AWS KMS key

1. In the navigation pane of the [KMS console](https://console.aws.amazon.com/kms/), choose **Customer managed keys**,
   and then choose **Create key**.
2. Select the **Symmetric** key type, the **Encrypt and decrypt** key usage and click **Next**.
3. Add labels as needed, then click **Next**.
4. Define key administrative permissions as needed, then click **Next**.
5. Select the IAM role you created in the previous step under **Key users**, then click **Next**.
6. Ensure that the **Key policy** defines the correct actions for the selected role, then finish the wizard.

```json
{
  "Statement": [
    {
      "Sid": "Allow use of the key",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:role/<role-name>"
      },
      "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:GenerateDataKey"
      ],
      "Resource": "*"
    }
  ]
}
```

Before you log out of the AWS console, make sure to make a note of your key’s ARN value and or alias ARN value as you
will need it to set up the Customer Managed Key in Pulumi Cloud.

## Add the Customer Managed Key in Pulumi Cloud

Now you can add the Customer Managed Key in Pulumi Cloud as described in
the [Customer Managed Keys documentation](/docs/pulumi-cloud/admin/customer-managed-keys/).
