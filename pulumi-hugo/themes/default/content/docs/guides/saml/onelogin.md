---
title: OneLogin
meta_desc: This page provides a walkthrough important aspects of configuring
  OneLogin as a SAML SSO identity provider (IdP).
menu:
  userguides:
    parent: saml
    weight: 2

aliases:
  - /docs/reference/service/saml-onelogin/
  - /docs/console/accounts/saml/onelogin/
---

This guide walks you through configuring OneLogin as a SAML SSO identity provider (IdP) for the Pulumi Service.

## Prerequisites

- [Single Sign-On]({{< relref "sso" >}})

## Creating the OneLogin Application

The first step is to create a new OneLogin Application for Pulumi SSO:

1. From the OneLogin Administration portal, go to the **Applications** page and click the **Add App** button.
1. Search for `SAML Test Connector (Advanced)` and select it.

    ![Finding the SAML Test Connector App](/images/docs/reference/service/saml-onelogin/onelogin-find-app.png)

1. Enter a _Display Name_ and optionally a logo. See [Pulumi Logos](https://www.pulumi.com/brand/#logos).
1. Click **Save**.

    ![Creating a OneLogin Application example](/images/docs/reference/service/saml-onelogin/onelogin-create-saml-app.png)

### Configuring the OneLogin Application

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

#### Configure SSO Settings

Select the **SSO** view for the application and set/confirm the following:

| SSO Settings             | Value     |
| ------------------------ | --------- |
| SAML Signature Algorithm | `SHA-512` |

![SSO Settings](/images/docs/reference/service/saml-onelogin/onelogin-sso-sig-setting.png)

### User Assignments

After the Pulumi SAML application has been created in OneLogin, the next step is to assign users to it.
This will grant specific users or groups access to sign into Pulumi with their OneLogin-provided
credentials.

To assign users or groups to the application, navigate to the **Users** tab in the OneLogin portal to add users and then assign them to the Pulumi SSO application.

![User Assignments](/images/docs/reference/service/saml-onelogin/onelogin-add-user-sso.png)

## Configuring Your Pulumi Organization

The final step is to configure the Pulumi Service with details on your new OneLogin-based
SAML application. To do this, you need to obtain the IDP metadata document from OneLogin and then provide
it to Pulumi.

First, navigate to the OneLogin Application you created above and click the **More Actions** drop down menu button and select _SAML Metadata_ to download the metadata XML file.

![Get Metadata](/images/docs/reference/service/saml-onelogin/onelogin-get-metadata.png)

1. Open the file and copy the entire block of XML text in your clipboard
1. Open the Pulumi Service and navigate to your SAML organization.
1. Select the **Settings** tab, and then select **SAML SSO**.
1. Paste the IDP metadata XML into the bottom card titled **SAML SSO Settings**

    ![Pulumi Organization Settings](/images/docs/reference/service/saml-onelogin/onelogin-pulumi-saml-metadata.png)

1. Select **Save** at the bottom of the card.

Once the IDP metadata descriptor has been saved, you are all set to log into Pulumi.

### Signing into Pulumi using OneLogin

Members of your OneLogin application can now sign into Pulumi. Navigate to
[https://app.pulumi.com/signin/sso/](https://app.pulumi.com/signin/sso/) and enter the
name of your Pulumi organization.

![Pulumi Service](/images/docs/reference/service/saml-okta/pulumi-console-signin.png)

## Troubleshooting

If you run into any troubles configuring OneLogin, signing into Pulumi, or need some assistance, [contact us]({{< relref "/about#contact-us" >}}).
