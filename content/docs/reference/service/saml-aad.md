---
title: SAML Configuration > Azure Active Directory
---

This guide explains how to configure your Azure Active Directory (Azure AD) as a SAML SSO identity provider
(IDP) for use with the Pulumi Cloud Console.

## Add an application to your Azure AD tenant

The first step is to add a new Pulumi application to your Azure AD tenant.

1. In the Azure portal, on the left navigation panel, click **Azure Active Directory**.

1. Click **Enterprise applications**. It will show some of the existing applications in your Azure
  AD tenant.

    ![Enterprise applications section](/images/docs/reference/service/saml-aad/enterprise-applications.png)

1. Click **New application** at the top of the **All applications** blade.

    ![New application](/images/docs/reference/service/saml-aad/new-application.png)

1. Click the **Non-gallery application** tile and in the **Add your own application** blade, enter
   _Pulumi Cloud Console_ as the application name and click **Add**.

    ![Non-gallery application](/images/docs/reference/service/saml-aad/non-gallery-application.png)

1. In the new _Pulumi Cloud Console_ application, navigate to the **Single sign-on** section, and
  select **SAML**.

    ![Single sign-on settings](/images/docs/reference/service/saml-aad/single-sign-on.png)

1. Click the **Edit** icon on the **Basic SAML Configuration** panel.

    ![SAML configuration](/images/docs/reference/service/saml-aad/saml-configuration.png)

The next step is to enter Pulumi-specific configuration data into your Azure AD application.
The values you will want to use are dependent upon your organization's name on Pulumi. Be sure
to replace `acmecorp` with whatever your specific Pulumi organization's name is.

| SAML Setting | Value |
| --------------- | ----- |
| Identifier (Entity ID) | https://api.pulumi.com/login/**acmecorp**/sso/saml/metadata |
| Reply URL | https://api.pulumi.com/login/**acmecorp**/sso/saml/acs |
| Relay State | https://api.pulumi.com/login/**acmecorp**/sso |


<p><!-- space between table and image --></p>

![Edited SAML configuration](/images/docs/reference/service/saml-aad/edited-saml-configuration.png)

The final step is to configure the **name identifier format**.

1. Click the **Edit** icon on the **User Attributes & Claims** panel.

![User Attributes & Claims Panel](/images/docs/reference/service/saml-aad/attributes-and-claims-panel.png)

1. Then, click on the **Edit** icon next to **Name identifier value**.

![User Attributes & Claims](/images/docs/reference/service/saml-aad/attributes-and-claims.png)

1. In the **Manage User Claims** panel, expand the **Choose name identifier format** and select **Email address**.

![Manage Name Identifier Format](/images/docs/reference/service/saml-aad/name-identifier-format.png)

1. Finally, click **Save** at the bottom of the **Manage User Claims** panel.

**IMPORTANT:** Do not change the value of Name ID Format value once your users have started using Pulumi; not even switching its value between Email or Persistent.

Now the Azure AD-side of the SAML SSO configuration is complete. The next and final
step is to configure the Pulumi Cloud Console to receive SAML SSO requests from your
Azure AD.

> **NOTE:** Be sure to assign users and groups to use your new _Pulumi Cloud Console_ SAML application.
> That is how you can control access to who can join your Pulumi organization. See the
> [Azure AD documentation](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/configure-single-sign-on-non-gallery-applications#assign-users-and-groups-to-your-saml-application)
> for more information.

## Configuring Your Pulumi Organization

To configure your Pulumi organization to accept SAML SSO requests from Azure AD, you will need to
download the SAML application's configuration data and then pass that to Pulumi.

1. Back on the Azure AD's application settings page, click the **SAML Signing Certificate** panel.
  Then click **Download** next to **Federated Metadata XML** and save the resulting file.

    ![Download XML](/images/docs/reference/service/saml-aad/download-xml.png)

1. Sign into the Pulumi Cloud Console and navigate to your SAML organization. Navigate to the
  **Settings** tab and then select **SAML SSO**.

1. Open up the XML document you downloaded from the Azure AD portal, and paste its full contents
  into the **Identity Provider Metadata** field.

    ![Provide the XML IDP descriptor](/images/docs/reference/service/saml-aad/pulumi-saml-settings-page.png)

1. Click **Save**.

## Signing into Pulumi using Azure AD

Once your Azure AD application is created, and its configuration data passed to Pulumi, you can now
sign into the Pulumi Cloud Console using your SAML SSO credentials.

Navigate to [https://app.pulumi.com/signin/sso/](https://app.pulumi.com/signin/sso/) and enter the
name of your Pulumi organization. If everything is configured correctly, you should be prompted to
sign into to your Azure AD instance, and then immediately redirected back to the Pulumi Cloud Console.

![Pulumi Console](/images/docs/reference/service/saml-aad/pulumi-console-signin.png)

## Troubleshooting

If you have any trouble configuring Azure AD, signing into Pulumi, or need additional assistance, please
[contact us](https://www.pulumi.com/about/#contact-us).
