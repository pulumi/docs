---
title_tag: Configuring Azure Active Directory | SAML SSO
meta_desc: This page provides a walkthrough important aspects of configuring
           Azure Active Directory (Azure AD) as a SAML SSO identity provider (IDP).
title: Azure AD
h1: "SAML: Configuring Azure Active Directory"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  pulumicloud:
      parent: saml
      weight: 2

aliases:
- /docs/reference/service/saml-aad/
- /docs/console/accounts/saml/aad/
- /docs/guides/saml/aad/
---

This guide walks you through configuring your Azure Active Directory (Azure AD) as a SAML SSO identity provider
(IDP) for the Pulumi Cloud.

## Prerequisites

- [Single Sign-On](/docs/pulumi-cloud/access-management/saml/sso/)

## Configuring Azure AD

### Add an application to your Azure AD tenant

1. In the Azure portal, on the left navigation panel, select **Azure Active Directory**.

1. Select **Enterprise applications**. It will show some of the existing applications in your Azure
  AD tenant.

    ![Enterprise applications section](/images/docs/reference/service/saml-aad/enterprise-applications.png)

1. Select **New application**.

    ![New application](/images/docs/reference/service/saml-aad/new-application.png)

1. Select **Non-gallery application** tile and in the **Add your own application** panel, enter
   _Pulumi Cloud_ as the application name then select **Add**.

    ![Non-gallery application](/images/docs/reference/service/saml-aad/non-gallery-application.png)

1. In the new _Pulumi Cloud_ application, navigate to the **Single sign-on** section, and
  select **SAML**.

    ![Single sign-on settings](/images/docs/reference/service/saml-aad/single-sign-on.png)

1. Select the **Edit** icon on the **Basic SAML Configuration** panel.

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

1. Select the **Edit** icon on the **User Attributes & Claims** panel.

    ![User Attributes & Claims Panel](/images/docs/reference/service/saml-aad/attributes-and-claims-panel.png)

1. Then, select the **Edit** icon next to **Name identifier value**.

    ![User Attributes & Claims](/images/docs/reference/service/saml-aad/attributes-and-claims.png)

1. In the **Manage User Claims** panel, expand **Choose name identifier format** and select **Email address**.

    ![Manage Name Identifier Format](/images/docs/reference/service/saml-aad/name-identifier-format.png)

1. Finally, select **Save** at the bottom of the **Manage User Claims** panel.

> **Important:** Do not change the value of Name ID Format value once your users have started using Pulumi---not even switching its value between Email or Persistent.
<br />
> **Note:** Be sure to assign users and groups to use your new _Pulumi Cloud_ SAML application.
> That is how you can control membership access to your Pulumi organization. See the
> [Azure AD documentation](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/configure-single-sign-on-non-gallery-applications#assign-users-and-groups-to-your-saml-application)
> for more information.

Now that the Azure AD-side of the SAML SSO configuration is complete, you will need
to configure the Pulumi Cloud to receive SAML SSO requests from your
Azure AD.

## Configuring Your Pulumi Organization

To configure your Pulumi organization to accept SAML SSO requests from Azure AD, you will need to
download the SAML application's configuration data and then pass that to Pulumi.

1. Back on the Azure AD's application settings page, select the **SAML Signing Certificate** panel.
  Then select **Download** next to **Federated Metadata XML** and save the resulting file.

    ![Download XML](/images/docs/reference/service/saml-aad/download-xml.png)

1. Sign into the Pulumi Cloud and navigate to your SAML organization. Navigate to the
  **Settings** tab and then select **Access Management**.

1. Select the **Change Requirements** button and then **SAML SSO**.

1. Open up the XML document you downloaded from the Azure AD portal, and paste its full contents
  into the **Identity Provider Metadata** field.

    ![Provide the XML IDP descriptor](/images/docs/reference/service/saml-aad/pulumi-saml-settings-page.png)

1. Select **Save**.

## Signing into Pulumi using Azure AD

Once your Azure AD application is created, and its configuration data passed to Pulumi, you can now
sign in to the Pulumi Cloud using your SAML SSO credentials.

Navigate to [https://app.pulumi.com/signin/sso/](https://app.pulumi.com/signin/sso/) and enter the
name of your Pulumi organization. If everything is configured correctly, you should be prompted to
sign in to your Azure AD instance, and then immediately be redirected back to the Pulumi Cloud.

![Pulumi Cloud](/images/docs/reference/service/saml-aad/pulumi-console-signin.png)

## Troubleshooting

If you have any trouble configuring Azure AD, signing into Pulumi, or need additional assistance, please
[contact support](https://support.pulumi.com/).
