---
title_tag: Configuring Okta | SAML SSO
meta_desc: This page provides a walkthrough important aspects of configuring
           Okta as a SAML SSO identity provider (IdP).
title: Okta
h1: "SAML: Configuring Okta"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  pulumicloud:
    parent: saml
    weight: 2

aliases:
- /docs/reference/service/saml-okta/
- /docs/console/accounts/saml/okta/
- /docs/guides/saml/okta/
---

This guide walks you through configuring Okta as a SAML SSO identity provider (IdP) for the Pulumi Cloud.

## Prerequisites

- [Single Sign-On](/docs/pulumi-cloud/access-management/saml/sso/)

## Creating the Okta Application

The first step is to create a new Okta Application Integration. Of the various "sign-in methods"
available, choose **SAML 2.0**.

![Creating an Okta Application](/images/docs/reference/service/saml-okta/create-okta-application.png)

### Configuring the Application

Next you will be guided through a wizard to configure the Okta application. The first step is to
give it a name---Pulumi Cloud for example---and an [icon](https://www.pulumi.com/brand/).

![Configuring a SAML Integration](/images/docs/reference/service/saml-okta/create-saml-integration.png)

The next step is to configure the SAML application's settings.

    {{% notes type="info" %}}
The values you need to use are dependent upon your Pulumi organization name. Be sure to replace `<orgName>` with your actual organization name.
    {{% /notes %}}

| SAML Setting | Value |
| --------------- | ----- |
| Single Sign-on URL | `https://api.pulumi.com/login/<orgName>/sso/saml/acs` |
| Audience URI | `https://api.pulumi.com/login/<orgName>/sso/saml/metadata` |
| Default Relay State | `https://api.pulumi.com/login/<orgName>/sso` |
| Name ID Format | `Persistent` |
| App username | `Email` |

    {{% notes type="warning" %}}
> **Important:** Do not change the value of the Name ID Format once your users have started using Pulumi. Once a given SAML identity has been associated with a user, any change to the username sent by Okta will result in login failures for that user.
    {{% /notes %}}

In addition, you can optionally provide two attribute statements so that users
who sign in with their Okta credentials will have proper user names.

| Attribute | Value |
| --------- | ----- |
| firstName | user.firstName |
| lastName  | user.lastName  |

If you plan on using [SCIM](/docs/pulumi-cloud/access-management/scim/okta/), you will need to provide the above attributes, in addition to the `email` attribute.

| Attribute | Value |
| --------- | ----- |
| email     | user.email |

![Configuration Settings](/images/docs/reference/service/saml-okta/configure-saml-settings.png)

### User Assignments

After the Pulumi SAML application has been created in Okta, the next step is to assign users to it.
This will grant specific users or groups access to sign into Pulumi with their Okta-provided
credentials.

To assign users or groups to the application, navigate to the **Assignments** tab on the application
page.

![User Assignments](/images/docs/reference/service/saml-okta/user-assignments.png)

## Configuring Your Pulumi Organization

The final step is to configure the Pulumi Cloud with details on your new Okta-based
SAML application. To do this, you need to obtain the IDP metadata document from Okta and then provide
it to Pulumi.

First, navigate to the **Sign On** tab on the application page and click the
**"View SAML setup instructions"** link in the right column.

![View Setup Instructions](/images/docs/reference/service/saml-okta/view-setup-instructions.png)

Next, scroll to the bottom of the setup instructions and select the value in the large text box
with the heading "Provide the following IDP metadata to your SP provider". That's the full SAML
Identity Provider SSO descriptor, which contains all of the settings Pulumi needs to verify
a user's identity.

![SAML Application Metadata](/images/docs/reference/service/saml-okta/okta-xml-descriptor.png)

With the block of XML text in your clipboard, open the Pulumi Cloud and navigate to your SAML
organization. Select the **Settings** tab, and then select **Access Management**.

In the **Membership Requirements** section, select the **Change requirements** button.

Select **SAML SSO** for the IDP and then **Next**.

Paste the IDP metadata descriptor into the bottom card
titled **SAML SSO Settings**. Then select **Save** at the bottom of the card.

![Pulumi Organization Settings](/images/docs/reference/service/saml-okta/pulumi-org-settings.png)

Once the IDP metadata descriptor has been saved, you are all set to log into Pulumi.

## Configuring Session Lifetime

The Pulumi Cloud uses the `SessionNotOnOrAfter` attribute in the `AuthnStatement` element to configure the session lifetime. To configure this in Okta, you must use a [SAML assertion inline hook](https://developer.okta.com/docs/guides/saml-inline-hook/main/).

The JSON payload the inline hook sends to Okta should contain the following:

```json
{
  "commands": [
    {
      "type": "com.okta.assertion.patch",
      "value": [
        {
          "op": "add",
          "path": "/authentication/sessionLifetime",
          "value": 21600 // lifetime in seconds
        }
      ]
    }
  ]
}

```

### Signing into Pulumi using Okta

Members of your Okta application can now sign into Pulumi. Navigate to
[https://app.pulumi.com/signin/sso/](https://app.pulumi.com/signin/sso/) and enter the
name of your Pulumi organization.

![Pulumi Cloud](/images/docs/reference/service/saml-okta/pulumi-console-signin.png)

## Troubleshooting

If you run into any troubles configuring Okta, signing into Pulumi, or need some assistance, [contact us](/about#contact-us).
