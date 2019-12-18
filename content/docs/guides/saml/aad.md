---
title: Azure Active Directory
meta_desc: This page provides a walkthrough important aspects of configuring
           Azure Active Directory (Azure AD) as a SAML SSO identity provider (IDP).
menu:
    userguides:
        parent: saml
        weight: 2

aliases:
- /docs/reference/service/saml-aad/
- /docs/console/accounts/saml/aad/
---

This guide walks you through configuring your Azure Active Directory (Azure AD) as a SAML SSO identity provider
(IDP) for the Pulumi Console.

## Prerequisites

- [Single Sign-On]({{< relref "sso" >}})

## Configuring Azure AD

### Add an application to your Azure AD tenant

1. In the Azure portal, on the left navigation panel, click **Azure Active Directory**.

1. Click **Enterprise applications**. It will show some of the existing applications in your Azure
  AD tenant.

    ![Enterprise applications section](/images/docs/reference/service/saml-aad/enterprise-applications.png)

1. Click **New application**.

    ![New application](/images/docs/reference/service/saml-aad/new-application.png)

1. Select **Non-gallery application** tile and in the **Add your own application** panel, enter
   _Pulumi Console_ as the application name then click **Add**.

    ![Non-gallery application](/images/docs/reference/service/saml-aad/non-gallery-application.png)

1. In the new _Pulumi Console_ application, navigate to the **Single sign-on** section, and
  select **SAML**.

    ![Single sign-on settings](/images/docs/reference/service/saml-aad/single-sign-on.png)

1. Click the **Edit** icon on the **Basic SAML Configuration** panel.

    ![SAML configuration](/images/docs/reference/service/saml-aad/saml-configuration.png)

### Enter Pulumi configuration into your Azure AD application

{{< saml-warning >}}

| SAML Setting | Value |
| --------------- | ----- |
| Identifier (Entity ID) | `https://api.pulumi.com/login/<acmecorp>/sso/saml/metadata` |
| Reply URL | `https://api.pulumi.com/login/<acmecorp>/sso/saml/acs` |
| Relay State | `https://api.pulumi.com/login/<acmecorp>/sso` |

![Edited SAML configuration](/images/docs/reference/service/saml-aad/edited-saml-configuration.png)

### Configure the name identifier format

1. Click the **Edit** icon on the **User Attributes & Claims** panel.

![User Attributes & Claims Panel](/images/docs/reference/service/saml-aad/attributes-and-claims-panel.png)

1. Then, click on the **Edit** icon next to **Name identifier value**.

![User Attributes & Claims](/images/docs/reference/service/saml-aad/attributes-and-claims.png)

1. In the **Manage User Claims** panel, expand **Choose name identifier format** and select **Email address**.

![Manage Name Identifier Format](/images/docs/reference/service/saml-aad/name-identifier-format.png)

1. Finally, click **Save** at the bottom of the **Manage User Claims** panel.

> **Important:** Do not change the value of Name ID Format value once your users have started using Pulumi---not even switching its value between Email or Persistent.
<br />
> **Note:** Be sure to assign users and groups to use your new _Pulumi Console_ SAML application.
> That is how you can control membership access to your Pulumi organization. See the
> [Azure AD documentation](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/configure-single-sign-on-non-gallery-applications#assign-users-and-groups-to-your-saml-application)
> for more information.

Now that the Azure AD-side of the SAML SSO configuration is complete, you will need
to configure the Pulumi Console to receive SAML SSO requests from your
Azure AD.

## Configuring Your Pulumi Organization

To configure your Pulumi organization to accept SAML SSO requests from Azure AD, you will need to
download the SAML application's configuration data and then pass that to Pulumi.

1. Back on the Azure AD's application settings page, click the **SAML Signing Certificate** panel.
  Then click **Download** next to **Federated Metadata XML** and save the resulting file.

    ![Download XML](/images/docs/reference/service/saml-aad/download-xml.png)

1. Sign into the Pulumi Console and navigate to your SAML organization. Navigate to the
  **Settings** tab and then select **SAML SSO**.

1. Open up the XML document you downloaded from the Azure AD portal, and paste its full contents
  into the **Identity Provider Metadata** field.

    ![Provide the XML IDP descriptor](/images/docs/reference/service/saml-aad/pulumi-saml-settings-page.png)

1. Click **Save**.

## Signing into Pulumi using Azure AD

Once your Azure AD application is created, and its configuration data passed to Pulumi, you can now
sign into the Pulumi Console using your SAML SSO credentials.

Navigate to [https://app.pulumi.com/signin/sso/](https://app.pulumi.com/signin/sso/) and enter the
name of your Pulumi organization. If everything is configured correctly, you should be prompted to
sign into to your Azure AD instance, and then immediately redirected back to the Pulumi Console.

![Pulumi Console](/images/docs/reference/service/saml-aad/pulumi-console-signin.png)

## Troubleshooting

If you have any trouble configuring Azure AD, signing into Pulumi, or need additional assistance, please
[contact us]({{< relref "/about#contact-us" >}}).
