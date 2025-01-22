---
title_tag: Configuring Microsoft Entra ID | SAML SSO
meta_desc: This page provides a walkthrough important aspects of configuring 
           Entra ID as a SAML SSO identity provider (IDP).
title: Microsoft Entra ID
h1: "SAML: Configuring Microsoft Entra ID"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: Entra ID
    parent: pulumi-cloud-access-management-saml
    weight: 3
    identifier: pulumi-cloud-access-management-saml-entra
aliases:
- /docs/reference/service/saml-aad/
- /docs/console/accounts/saml/aad/
- /docs/guides/saml/aad/
- /docs/pulumi-cloud/access-management/saml/aad/
---

This guide walks you through configuring Microsoft Entra ID as a SAML SSO identity provider
(IDP) for the Pulumi Cloud.

## Prerequisites

- [Single Sign-On](/docs/pulumi-cloud/access-management/saml/sso/)

## Configuring Microsoft Entra ID

### Add an application to your Entra ID tenant

1. In the Azure portal, on the left navigation panel, select **Microsoft Entra ID**.

1. Select **Add** then in the dropdown, select **Enterprise application**. It will take you to the Microsoft Entra Gallery.

    ![New application](/images/docs/reference/service/saml-aad/new-application.png)

1. Select **Create your own application** and in the **Create your own application** panel, enter
   _Pulumi Cloud_ as the application name. Make sure the **Non-gallery** option is selected, then select **Create**.

    ![Non-gallery application](/images/docs/reference/service/saml-aad/non-gallery-application.png)

1. In the new _Pulumi Cloud_ application, navigate to the **Single sign-on** section, and
  select **SAML**.

    ![Single sign-on settings](/images/docs/reference/service/saml-aad/single-sign-on.png)

1. Select the **Edit** icon on the **Basic SAML Configuration** panel.

    ![SAML configuration](/images/docs/reference/service/saml-aad/saml-configuration.png)

### Enter Pulumi configuration into your Entra ID application

{{< saml-warning >}}

| SAML Setting | Value |
| --------------- | ----- |
| Identifier (Entity ID) | `https://api.pulumi.com/login/<acmecorp>/sso/saml/metadata` |
| Reply URL | `https://api.pulumi.com/login/<acmecorp>/sso/saml/acs` |
| Relay State | `https://api.pulumi.com/login/<acmecorp>/sso` |

![Edited SAML configuration](/images/docs/reference/service/saml-aad/edited-saml-configuration.png)

### Configure the name identifier format

1. Select the **Edit** icon on the **Attributes & Claims** panel.

    ![User Attributes & Claims Panel](/images/docs/reference/service/saml-aad/attributes-and-claims-panel.png)

1. Then, select **Unique User Identifier (Name ID)** under **Required claim**.

    ![User Attributes & Claims](/images/docs/reference/service/saml-aad/attributes-and-claims.png)

1. In the **Manage User Claims** panel, expand **Choose name identifier format** and select **Email address**.

    ![Manage Name Identifier Format](/images/docs/reference/service/saml-aad/name-identifier-format.png)

1. Finally, select **Save** at the bottom of the **Manage User Claims** panel.

> **Important:** Do not change the value of Name ID Format value once your users have started using Pulumi---not even switching its value between Email or Persistent.
<br />
> **Note:** Be sure to assign users and groups to use your new _Pulumi Cloud_ SAML application.
> That is how you can control membership access to your Pulumi organization. See the
> [Entra ID documentation](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/assign-user-or-group-access-portal)
> for more information.

Now that the Entra ID side of the SAML SSO configuration is complete, you will need
to configure the Pulumi Cloud to receive SAML SSO requests from your
Entra ID application.

## Configuring Your Pulumi Organization

To configure your Pulumi organization to accept SAML SSO requests from Entra ID, you will need to
download the SAML application's configuration data and then pass that to Pulumi.

1. Back on the Entra ID application's settings page, select the **SAML Certificates** panel.
  Then select **Download** next to **Federated Metadata XML** and save the resulting file.

    ![Download XML](/images/docs/reference/service/saml-aad/download-xml.png)

1. Sign into the Pulumi Cloud and navigate to your SAML organization. Navigate to the
  **Settings** tab and then select **Access Management**.

1. Select the **Change Requirements** button and then **SAML SSO**.

1. Open up the XML document you downloaded from the Entra ID portal, and paste its full contents into the text box.

    ![Provide the XML IDP descriptor](/images/docs/reference/service/saml-aad/pulumi-saml-settings-page.png)

1. Select **Apply changes**.

## Signing into Pulumi using Entra ID

Once your Entra ID application is created, and its configuration data passed to Pulumi, you can now
sign in to the Pulumi Cloud using your SAML SSO credentials.

Navigate to [https://app.pulumi.com/signin/sso/](https://app.pulumi.com/signin/sso/) and enter the
name of your Pulumi organization. If everything is configured correctly, you should be prompted to
sign in to your Entra ID instance, and then immediately be redirected back to the Pulumi Cloud.

![Pulumi Cloud](/images/docs/reference/service/saml-aad/pulumi-console-signin.png)

## Troubleshooting

If you have any trouble configuring Entra ID, signing into Pulumi, or need additional assistance, please
[contact support](https://support.pulumi.com/).
