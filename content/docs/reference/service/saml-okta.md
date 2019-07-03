---
title: SAML Configuration > Okta
---

This guide walks through how to configure Okta as a SAML SSO identity provider (IdP) for use with
the Pulumi Cloud Console.

> **NOTE:** The screen shots below are using the Okta _Classic UI_. You can switch to it by clicking the gear
> icon in the top right of the screen.

## Creating the Okta Application

The first step is to create a new Okta Application Integration. Of the various "sign on methods"
available, choose **SAML 2.0**.

![Creating an Okta Application](/images/docs/reference/service/saml-okta/create-okta-application.png)

### Configuring the Application

Next you will be guided through a wizard to configure the Okta application. The first step is to
give it a name, e.g. _Pulumi Cloud Console_, and an icon.

![Configuring a SAML Integration](/images/docs/reference/service/saml-okta/create-saml-integration.png)

The next step is where you configure the SAML application's settings. The values to provide will
depend on the name of your Pulumi organization, e.g. `acmecorp`.

<style>
td, th {
    padding: 8px 8px;
    border: 1px solid rgba(0,0,0,0.13);
}

thead tr th {
    color: #00acf2;  /* $primary2, blue */
    font-weight: 800;
}

tbody tr td {
    padding-left: 16px;
    padding-right: 16px;
}
</style>

| General Setting | Value |
| --------------- | ----- |
| Single sign on URL | https://api.pulumi.com/login/robot-co/sso/saml/acs |
| Audience URI | https://api.pulumi.com/login/robot-co/sso/saml/metadata |
| Default relay state | https://api.pulumi.com/login/robot-co/sso |
| Name ID format | EmailAddress or Persistent |
| App username | Email |

**IMPORTANT:** Do not change the value of Name ID Format value once your users have started using Pulumi; not even switching its value between Email or Persistent.

<p><!-- space between table and text --></p>
In addition, there are two attribute statements that can optionally be provided so that users
who sign in with their Okta credentials will have proper user names.

| Attribute | Value |
| --------- | ----- |
| firstName | user.firstName |
| lastName  | user.lastName  |

<p><!-- space between table and image --></p>
![Configuration Settings](/images/docs/reference/service/saml-okta/configure-saml-settings.png)

### User Assignments

After the Pulumi SAML application has been created in Okta, the next step is to assign users to it.
This will grant specific users or groups access to sign into Pulumi using their Okta-provided
credentials.

To assign users or groups to the application, navigate to the **Assignments** tab on the application
page.

![User Assignments](/images/docs/reference/service/saml-okta/user-assignments.png)

## Configuring Your Pulumi Organization

The final step is to configure the Pulumi Cloud Console with the details about your new Okta-based
SAML application. To do this, you need to obtain the IDP metadata document from Okta and then provide
it to Pulumi.

First, navigate to the **Sign On** tab on the application page and click the "View Setup Instructions"
button.

![View Setup Instructions](/images/docs/reference/service/saml-okta/view-setup-instructions.png)

Next, scroll to the bottom of the setup instructions and select the value in the large text box
with the heading "Provide the following IDP metadata to your SP provider". That's the full SAML
Identity Provider SSO descriptor, which contains all of the settings Pulumi needs to verify
a user's identity.

![SAML Application Metadata](/images/docs/reference/service/saml-okta/okta-xml-descriptor.png)

With the block of XML text in your clipboard, open the Pulumi Cloud Console and navigate to your SAML
organization. Click the **Settings** tab, and then select **SAML SSO**.

Paste the IDP metadata descriptor into the bottom card
titled **SAML SSO Settings**. Then click the "SAVE" button at the bottom of the card.

![Pulumi Organization Settings](/images/docs/reference/service/saml-okta/pulumi-org-settings.png)

Once the IDP metadata descriptor has been saved, you are all set to log into to Pulumi.

### Signing into Pulumi using Okta

Members of your Okta application can now sign into Pulumi. Navigate to
[https://app.pulumi.com/signin/sso/](https://app.pulumi.com/signin/sso/) and enter the
name of your Pulumi organization.

![Pulumi Console](/images/docs/reference/service/saml-okta/pulumi-console-signin.png)

## Troubleshooting

If you run into any troubles configuring Okta, signing into Pulumi, or need some assistance please
[contact us](https://www.pulumi.com/about/#contact-us).
