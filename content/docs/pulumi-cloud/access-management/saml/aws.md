---
title_tag: Configuring AWS | SAML SSO
meta_desc: This page provides a walkthrough of configuring AWS as a SAML SSO identity provider (IDP).
title: AWS
h1: "SAML: Configuring AWS"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: AWS
    parent: pulumi-cloud-access-management-saml
    weight: 5
    identifier: pulumi-cloud-access-management-saml-aws
  pulumicloud:
    parent: saml
    weight: 3

aliases:
- /docs/reference/service/saml-aws/
- /docs/console/accounts/saml/aws/
- /docs/guides/saml/aws/
---

This guide walks you through configuring your AWS account as a SAML SSO identity provider (IDP) for the Pulumi Cloud.

## Prerequisites

- [Single Sign-On](/docs/pulumi-cloud/access-management/saml/sso/)
- An AWS account with administrative access

## Creating the SAML Identity Provider in AWS

1. In the AWS Management Console, navigate to the **IAM (Identity and Access Management)** service.

1. In the navigation pane, choose **Identity providers**, then choose **Add provider**.

1. For **Configure provider**, choose **SAML**.

1. Enter a **Provider name** (e.g., `PulumiSAMLProvider`).

1. For **Metadata document**, choose **Choose file** and select the SAML metadata document provided by Pulumi.

1. (Optional) For **Add tags**, you can add key-value pairs to help identify and organize your identity providers.

1. Review the information you've entered. When you're ready, choose **Add provider** to create the new SAML identity provider.

1. Proceed to [Creating an IAM Role for SAML Access](#creating-an-iam-role-for-saml-access).

    ![AWS IAM Add Identity Provider](/images/docs/reference/service/saml-aws/aws-add-identity-provider.png)

## Creating an IAM Role for SAML Access

1. Select **Roles** from the sidebar and click **Create role**.

1. Under **Select type of trusted entity**, choose **SAML 2.0 federation**.

1. For **SAML provider**, select the provider you just created (e.g., `PulumiSAMLProvider`).

1. Under **Option**, select **Allow programmatic and AWS Management Console access**.

1. Click **Next: Permissions**.

1. Attach the necessary permissions that Pulumi will require.

1. Click **Next: Tags**.

1. Add any optional tags and click **Next: Review**.

1. Enter a **Role name** (e.g., `PulumiSAMLRole`) and a **Role description**.

1. Review the settings and click **Create role**.

    ![AWS IAM Create Role](/images/docs/reference/service/saml-aws/aws-create-role.png)

## Configuring Your Pulumi Organization

1. Sign in to the Pulumi Cloud where your SAML organization resides, then navigate to the **Settings** tab for that
organization.

1. Select **Access Management** and then **Change requirements**.

1. Select **SAML SSO** and **Next**

    ![Pulumi SAML SSO](/images/docs/reference/service/saml-aws/pulumi-enable-saml-sso.png)

1. Paste the metadata document from AWS into the text box.

    ![Provide the AWS SAML Metadata](/images/docs/reference/service/saml-aws/pulumi-load-sso-xml.png)

1. Select **Apply changes** and refresh your browser page to see the SAML SSO settings.

## Signing in to Pulumi with AWS

Members of your AWS account can now sign into Pulumi. Navigate to
[https://app.pulumi.com/signin/sso/](https://app.pulumi.com/signin/sso/) and enter the
name of your Pulumi organization.

![Pulumi Cloud Sign-In](/images/docs/reference/service/saml-aws/pulumi-console-signin.png)

## Troubleshooting

AWS SAML troubleshooting page: [Troubleshooting SAML 2.0 Federation with AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_saml.html)

If you need additional assistance, [contact us](/about#contact-us).

## Additional Resources

For more information on configuring SAML identity providers and understanding SAML in AWS, refer to the following resources:

- **AWS Documentation:**
  - [Create a SAML Identity Provider in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_saml.html)
  - [About SAML 2.0-based Federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html)
  - [Configure Relying Party Trust and Claims](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_saml_relying-party.html)
  - [Integrate Third-Party SAML Solution Providers with AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml_3rd-party.html)
  - [Troubleshooting SAML 2.0 Federation with AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_saml.html)

- **Understanding SAML:**
  - [SAML Technical Overview](https://wiki.oasis-open.org/security)
  - [SAML 2.0 Specifications](https://docs.oasis-open.org/security/saml/v2.0/)
