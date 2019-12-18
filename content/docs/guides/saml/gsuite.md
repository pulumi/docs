---
title: G Suite (Google)
meta_desc: This page provides a walkthrough important aspects of configuring
           G Suite service as a SAML SSO identity provider (IDP).
menu:
    userguides:
        parent: saml
        weight: 2

aliases:
- /docs/reference/service/saml-gsuite/
- /docs/console/accounts/saml/gsuite/
---

This guide walks you through configuring your G Suite service as a SAML SSO identity provider
(IDP) for the Pulumi Console.

## Prerequisites

- [Single Sign-On]({{< relref "sso" >}})

## Creating the SAML Application

1. In the [administrator console](https://admin.google.com/) for your G Suite domain, open the flyout menu
in the upper-left corner and choose **Apps &gt; SAML Apps**.

    ![The G Suite console](/images/docs/reference/service/saml-gsuite/gsuite-console.png)

1. Click the **+** symbol in the lower-right corner to create a new SAML application.

    ![Create a new SAML app](/images/docs/reference/service/saml-gsuite/gsuite-apps-empty.png)

1. In the first step, click **Set Up My Own Custom App**.

    ![Step 1: Set up a custom app](/images/docs/reference/service/saml-gsuite/gsuite-dialog-step-1.png)

1. Next, choose **Option 2: Download IDP Metadata** to download an XML document that identifies
and describes your G Suite domain as a SAML identity provider. You will need this document
to complete the process of configuring your Pulumi organization. For now, note the location of
the downloaded file, then click **Next** to continue.

    ![Step 2: Download IDP metadata](/images/docs/reference/service/saml-gsuite/gsuite-dialog-step-2.png)

1. Give your SAML application a name such as _Pulumi Console_ and an optional description
and logo, then click **Next**.

    ![Step 3: Name the application](/images/docs/reference/service/saml-gsuite/gsuite-dialog-step-3.png)

1. In step 4, for the required **ACS URL** and **Entity ID** fields, enter the fully-qualified
URLs of the `acs` and `metadata` endpoints of the Pulumi API, adjusted for your Pulumi organization name.
{{< saml-warning >}}

    | SAML Setting | Value    |
    | --------------- | ----- |
    | ACS URL | `https://api.pulumi.com/login/<acmecorp>/sso/saml/acs` |
    | Entity ID | `https://api.pulumi.com/login/<acmecorp>/sso/saml/metadata` |
    | Start URL | `https://api.pulumi.com/login/<acmecorp>/sso` |
    | Name ID Format | `EMAIL` or `PERSISTENT` |

    ![Step 4: Provide ACS and metadata URLs](/images/docs/reference/service/saml-gsuite/gsuite-dialog-step-4.png)

    > **Important:** Do not change the value of Name ID Format value once your users have started using Pulumi---not even switching its value between `EMAIL` or `PERSISTENT`.

    Leave the other fields as their default values, then click **Next**.

1. The final step---attribute mapping---is optional, but you may wish to specify proper
first and last names for your Pulumi users, based on their Google account profiles. The Pulumi service
expects to receive these fields as `firstName` and `lastName`, respectively.

    Once you add them, click **Finish** and **OK** to confirm.

    ![Step 5: Map optional attributes](/images/docs/reference/service/saml-gsuite/gsuite-dialog-step-5.png)

1. On the next screen, enable your newly created SAML application for your Google
domain users:

    ![Enable the SAML application](/images/docs/reference/service/saml-gsuite/gsuite-app-enable.png)

   Click **Save** to complete.

   At this point, you're done configuring G Suite, and can move on to completing SAML SSO setup in
   the Pulumi Console.

## Configuring Your Pulumi Organization

The final step in the process consists of associating your Pulumi organization with your SSO identity
provider.

1. Sign into the Pulumi Console where your SAML organization resides, then navigate to the **Settings** tab for that
organization.

1. Scroll to the SAML SSO Settings section, click on the **Identity Provider Metadata** field, and
paste the full contents of the XML IDP document you have previously downloaded.

    ![Provide the XML IDP descriptor](/images/docs/reference/service/saml-gsuite/console-sso-1.png)

    For example:

1. Click **Save**.

Your Pulumi organization is now configured to use Google as a SAML SSO identity provider.

## Signing into Pulumi with Google

Members of your G Suite can now sign into Pulumi. Navigate to
[https://app.pulumi.com/signin/sso/](https://app.pulumi.com/signin/sso/) and enter the
name of your Pulumi organization.

![Pulumi Console](/images/docs/reference/service/saml-gsuite/pulumi-console-signin.png)

## Troubleshooting

If you have any trouble configuring G Suite, signing into Pulumi, or need additional assistance, please
[contact us]({{< relref "/about#contact-us" >}}).
