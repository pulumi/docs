---
title: Google Workspace
meta_desc: This page provides a walkthrough important aspects of configuring
           Google Workspace as a SAML SSO identity provider (IDP).
menu:
    userguides:
        parent: saml
        weight: 2

aliases:
- /docs/reference/service/saml-gsuite/
- /docs/console/accounts/saml/gsuite/
---

This guide walks you through configuring your Google Workspace (formerly known as G Suite) service as a SAML SSO identity provider
(IDP) for the Pulumi Service.

## Prerequisites

- [Single Sign-On]({{< relref "sso" >}})

## Creating the SAML Application

1. In the [administrator console](https://admin.google.com/) for your Google Workspace domain, open the flyout menu
in the upper-left corner and choose **Apps &gt; Web and mobile apps**.

    ![The Google Workspace console](/images/docs/reference/service/saml-gsuite/gsuite-console.png)

1. Select **Add app &gt; Add custom SAML app** to create a new SAML application.

    ![Create a new SAML app](/images/docs/reference/service/saml-gsuite/gsuite-apps-empty.png)

1. In the first step, give the SAML app a name (e.g., *Pulumi-SSO*), and optionally add an App Icon, and select **Continue**. [Pulumi Logos](https://www.pulumi.com/brand/) has PNG logos available.

    ![Step 1: Set up a custom app](/images/docs/reference/service/saml-gsuite/gsuite-dialog-step-1.png)

1. Next, choose **Option 1: Download Metadata** to download an XML document that identifies
and describes your Google Workspace domain as a SAML identity provider. You will need this document
to complete the process of configuring your Pulumi organization. For now, note the location of
the downloaded file, then select **Continue** to continue.

    ![Step 2: Download IDP metadata](/images/docs/reference/service/saml-gsuite/gsuite-dialog-step-2.png)

1. In step 3, for the required **ACS URL** and **Entity ID** and **Start URL** fields, enter the fully-qualified
URLs of the `acs` and `metadata` and `sso` endpoints of the Pulumi API, adjusted for your Pulumi organization name.
{{< saml-warning >}}

    | SAML Setting | Value    |
    | --------------- | ----- |
    | ACS URL | `https://api.pulumi.com/login/<acmecorp>/sso/saml/acs` |
    | Entity ID | `https://api.pulumi.com/login/<acmecorp>/sso/saml/metadata` |
    | Start URL | `https://api.pulumi.com/login/<acmecorp>/sso` |
    | Name ID Format | `EMAIL` or `PERSISTENT` |

    ![Step 3: Provide ACS and metadata URLs](/images/docs/reference/service/saml-gsuite/gsuite-dialog-step-3.png)

    Set `Name ID format` to *EMAIL* or *PERSISTENT*. Leave the other fields as their default values, then select **Continue**.
    > **Important:** Do not change the value of Name ID Format value once your users have started using Pulumi---not even switching its value between `EMAIL` or `PERSISTENT`.

1. The final step---attribute mapping---is optional, but you may wish to specify proper
first and last names for your Pulumi users, based on their Google account profiles. The Pulumi service
expects to receive these fields as `firstName` and `lastName`, respectively.

    Once you add them, select **Finish**.

    ![Step 4: Map optional attributes](/images/docs/reference/service/saml-gsuite/gsuite-dialog-step-4.png)

1. On the next screen, enable your newly created SAML application for your Google
domain users by selecting the down arrow in the **User access** panel:

    ![Enable the SAML application](/images/docs/reference/service/saml-gsuite/gsuite-app-enable.png)

   Select **ON for everyone** and **Save**.

    ![Enable the SAML application part 2](/images/docs/reference/service/saml-gsuite/gsuite-app-enable-2.png)

   At this point, you're done configuring Google Workspace, and can move on to completing SAML SSO setup in
   the Pulumi Service.

## Configuring Your Pulumi Organization

The final step in the process consists of associating your Pulumi organization with your SSO identity
provider.

1. Sign in to the Pulumi Service where your SAML organization resides, then navigate to the **Settings** tab for that
organization.

1. Select **Access Management** and then **Change requirements**.

1. Select **SAML SSO** and **Next**

     ![Pulumi SAML SSO](/images/docs/reference/service/saml-gsuite/pulumi-enable-saml-sso.png)

1. Paste the full contents of the XML IDP document you have previously downloaded into the text box.

    ![Provide the XML IDP descriptor](/images/docs/reference/service/saml-gsuite/pulumi-load-sso-xml.png)

1. Select **Apply changes** and refresh your browser page to see the SAML SSO settings.

Your Pulumi organization is now configured to use Google as a SAML SSO identity provider.

## Signing in to Pulumi with Google

Members of your Google Workspace can now sign into Pulumi. Navigate to
[https://app.pulumi.com/signin/sso/](https://app.pulumi.com/signin/sso/) and enter the
name of your Pulumi organization.

![Pulumi Service](/images/docs/reference/service/saml-gsuite/pulumi-console-signin.png)

## Troubleshooting

Google Workspace SAML troubleshooting page: [SAML app error messages](https://support.google.com/a/answer/6301076)

If you need additional assistance, [contact us]({{< relref "/about#contact-us" >}}).
