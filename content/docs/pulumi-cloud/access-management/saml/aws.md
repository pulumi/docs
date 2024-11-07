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

1. Select **Identity providers** from the sidebar and click **Add provider**.

1. For **Provider Type**, select **SAML**.

1. Enter a descriptive name for **Provider Name** (e.g., `PulumiSAMLProvider`).

1. Upload the metadata document provided by Pulumi or paste the metadata URL.

    ![AWS IAM Add Identity Provider](/images/docs/reference/service/saml-aws/aws-add-identity-provider.png)

1. Click **Add provider** to save the new SAML identity provider.

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
