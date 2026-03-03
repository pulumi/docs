---
title_tag: Configuring OneLogin | SAML SSO
meta_desc: This page provides a walkthrough important aspects of configuring
  OneLogin as a SAML SSO identity provider (IdP).
title: OneLogin
h1: "SAML: Configuring OneLogin"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  administration:
    name: OneLogin
    parent: administration-access-identity-saml
    weight: 60
    identifier: pulumi-cloud-access-management-saml-onelogin
aliases:
- /docs/reference/service/saml-onelogin/
- /docs/console/accounts/saml/onelogin/
- /docs/guides/saml/onelogin/
- /docs/pulumi-cloud/access-management/saml/onelogin/
---

This guide walks you through configuring OneLogin as a [SAML SSO](/docs/administration/access-identity/saml/) identity provider (IdP) for Pulumi Cloud.

## Creating the OneLogin application

The first step is to create a new OneLogin Application for Pulumi SSO:

1. From the OneLogin Administration portal, go to the **Applications** page and select the **Add App** button.
1. Search for `SAML Custom Connector (Advanced)` and select it.

    ![Finding the SAML Test Connector App](/images/docs/reference/service/saml-onelogin/onelogin-find-app.png)

1. Enter a _Display Name_ and optionally a logo. See [Pulumi Logos](/brand/#logos).
1. Select **Save**.

    ![Creating a OneLogin Application example](/images/docs/reference/service/saml-onelogin/onelogin-create-saml-app.png)

### Configuring the OneLogin application

Now configure the OneLogin Application with the SAML settings for Pulumi SSO.

#### Configure SAML URLs

Select the **Configuration** view for the application and enter/confirm the values in the following table.

{{< saml-warning >}}

| Configuration Settings     | Value                                                     |
| -------------------------- | --------------------------------------------------------- |
| Relay State                | `https://api.pulumi.com/login/acmecorp/sso`               |
| Audience (EntityID)        | `https://api.pulumi.com/login/acmecorp/sso/saml/metadata` |
| Recipient                  | `https://api.pulumi.com/login/acmecorp/sso/saml/acs`      |
| ACS Consumer URL Validator | `.*`                                                      |
| ACS Consumer URL           | `https://api.pulumi.com/login/acmecorp/sso/saml/acs`      |
| SAML initiator             | `OneLogin`                                                |
| SAML nameID format         | `Email`                                                   |
| SAML issuer type           | `Specific`                                                |
| SAML signature element     | `Response`                                                |
| SAML encryption method     | `TRIPLEDES-CBC`                                           |

{{% notes type="warning" %}}
Do not change the value of SAML nameID format once your users have started using Pulumi---not even switching its value between `EmailAddress` or `Persistent`.
{{% /notes %}}

![Configuration settings example ](/images/docs/reference/service/saml-onelogin/onelogin-configure-app.png)

#### Configure SSO settings

Select the **SSO** view for the application and set/confirm the following:

| SSO Settings             | Value     |
| ------------------------ | --------- |
| SAML Signature Algorithm | `SHA-512` |

![SSO Settings](/images/docs/reference/service/saml-onelogin/onelogin-sso-sig-setting.png)

### User assignments

After the Pulumi SAML application has been created in OneLogin, the next step is to assign users to it.
This will grant specific users or groups access to sign into Pulumi with their OneLogin-provided
credentials.

To assign users or groups to the application, navigate to the **Users** tab in the OneLogin portal to add users and then assign them to the Pulumi SSO application.

![User Assignments](/images/docs/reference/service/saml-onelogin/onelogin-add-user-sso.png)

## Configuring your Pulumi organization

To configure Pulumi Cloud with details on your new OneLogin-based SAML application, you need to obtain
the IdP metadata document from OneLogin and then provide it to Pulumi.

Navigate to the OneLogin Application you created above and select the **More Actions** drop down menu button and select _SAML Metadata_ to download the metadata XML file.

![Get Metadata](/images/docs/reference/service/saml-onelogin/onelogin-get-metadata.png)

1. Open the file and copy the entire block of XML text to your clipboard.
1. Sign in to Pulumi Cloud and navigate to your organization.
1. Select **Settings** > **Access Management**.
1. Select the **Other** tab.
1. In the **Membership Requirements** section, select **Change requirements**.
1. Select **SAML SSO** and then **Next**.
1. Paste the IdP metadata XML into the text area.
1. Select **Apply changes**.

## Signing in to Pulumi using OneLogin

Members of your OneLogin application can now sign in to Pulumi. Navigate to
[https://app.pulumi.com/signin/sso/](https://app.pulumi.com/signin/sso/) and enter the
name of your Pulumi organization.

## Troubleshooting

For help resolving SAML SSO configuration issues, see the [SAML SSO troubleshooting guide](/docs/administration/access-identity/saml/troubleshooting/) or [contact support](https://support.pulumi.com/).
