---
title_tag: Configuring OneLogin | SCIM
meta_desc: This page describes how to support SCIM 2.0 functionality between Pulumi and OneLogin.
title: OneLogin
h1: "SCIM: Configuring OneLogin"
menu:
    pulumicloud:
        identifier: onelogin-scim
        parent: scim
        weight: 3
aliases:
  - /docs/guides/scim/onelogin/
---

This document outlines the steps required to help you configure automatic provisioning/deprovisioning of your users and groups in Pulumi using SCIM 2.0.

Please note that some advanced SCIM features aren't supported yet. For more information, see [Known Limitations](#known-limitations).

## Prerequisites

* You must be an admin of your Pulumi organization.
* (Optional, but highly recommended) You should have more than one admin for your Pulumi organization.

## Configuring the OneLogin Application

The first step is to create a new OneLogin Application for Pulumi SCIM:

1. From the OneLogin Administration portal, go to the **Applications** page and select the **Add App** button.
1. Search for `SCIM Provisioner with SAML (SCIM v2 Core)` and select it.

1. Enter a _Display Name_ and optionally a logo. See [Pulumi Logos](/brand/#logos).
1. Select **Save**.

### Configuration Settings

Select the **Configuration** view for the application and enter/confirm the values in the following table.

{{< saml-warning >}}

| Configuration Settings     | Value                                                     |
| -------------------------- | --------------------------------------------------------- |
| SAML Audience URL          | `https://api.pulumi.com/login/acmecorp/sso/saml/metadata` |
| SAML Consumer URL          | `https://api.pulumi.com/login/acmecorp/sso/saml/acs`      |
| SCIM Base URL              | `https://api.pulumi.com/scim/v2/acmecorp`      |
| API Connection             | *Enabled*  |

### SSO Settings

Select the **SSO** view for the application and confirm/update the values in the following table.

| SSO Settings     | Value                                                     |
| -------------------------- | --------------------------------------------------------- |
| SAML Signature Algorithm | `SHA-512`

### Provisioning Settings

Select the **Provisioning** view for the application and confirm/update the following settings:

| Provisioning Settings     | Value                                                     |
| ------------------------- | --------------------------------------------------------- |
| Enable provisioning       | box is checked
| Require admin approval ... | *Create user*, *Delete user*, *Update user* boxes are all unchecked.
| When users are deleted in OneLogin ... | **Suspend** (*DO NOT set to Delete*)
| When user accounts  are suspended in OneLogin ... | **Suspend**

### Parameters Settings

Select the **Parameters** view for the application and add the fields as per the following table.

| SCIM Provisioning Field Name | Value                                                     |
| ---------------------------- | --------------------------------------------------------- |
| firstName | `First Name`
| lastName | `Last Name`
| email | `Email`

Be sure to check the *Include in SAML assertion* checkbox for each of the added fields.

Optionally, you can override the default value for *scimusername* and use the `Macro` setting. For example, `{firstname}{lastname}` as per [OneLogin Macros](https://onelogin.service-now.com/kb_view_customer.do?sysparm_article=KB0010609)

Select **Save** to save the application settings.

## Configuring Communications Between Pulumi and OneLogin

These next steps configure the Pulumi Cloud with details on your new OneLogin-based application  and configure OneLogin to be able to authenticate to the Pulumi Cloud.

For the first step, you need to obtain the IDP metadata document from OneLogin and then provide it to Pulumi.

1. Navigate to the OneLogin Application you created above and select the **More Actions** drop down menu button and select _SAML Metadata_ to download the metadata XML file.
1. Open the file and copy the entire block of XML text in your clipboard.
1. Open the Pulumi Cloud and navigate to the organization for which you are enabling SAML/SCIM.
1. Select the **Settings** tab, and then select **Access Management**.
1. In the **Membership Requirements** section, select the **Change requirements** button.
1. Select **SAML SSO** and then select **Next**.
1. Paste the IDP metadata XML into the bottom card titled **SAML SSO Settings**
1. Select **Apply changes** at the bottom of the card.
1. Refresh the browser to see that SAML is configured.

At this point Pulumi is able to accept communications from OneLogin. The next step is to provide OneLogin a token to allow Pulumi to authenticaticate the communications from OneLogin.

1. Navigate to the Pulumi Cloud, then **Settings**, then **Access management**.
1. Scroll to the *SCIM* block at the bottom of the page.
1. Select **Generate new token**
1. Copy the token
1. Navigate back to the OneLogin Application you created.
1. Select the *Configuration* view.
1. Paste the SCIM token copied from Pulumi above into the *SCIM Bearer Token* field.
1. Save the application.

At this point, SCIM provisioning of users into the Pulumi organization will work as you add the OneLogin Pulumi application created above to your OneLogin users.

## Configuring Group Provisioning

Beyond managing users, Pulumi's SCIM support enables you to manage Pulumi Teams and team membership. To set this up, Pulumi supports using OneLogin's Role-Group mapping to manage Pulumi teams membership.

### Set up OneLogin Application to Manage Groups in Pulumi

Navigate to the SCIM application in OneLogin.

1. Select the **Parameters** view for the application and select the `Groups` parameter.
1. Check the *Include in User Provisioning* checkbox.
1. Select the **Rules** view for the application.
1. For each Pulumi Team you want to manage in OneLogin do the following:
   * Select *Add Rule*
   * Name the rule using the Pulumi Team name you are managing (e.g. `AlphaTeam` or `DevEngineers`, etc.)
   * *Conditions*: leave blank so that the rule applies to all users.
   * *Actions*: Set Groups ... Map from OneLogin ... For each role ... with value that matches your team name (e.g. `AlphaTeam`)
   * Save the rule.
    ![Application Rule](/images/docs/guides/scim/onelogin-application-rule.png)

1. Save the Application updates.

### Configure Roles in OneLogin to Map to Groups

These next steps create the Roles that are used to map users to Groups in OneLogin and, by extension, Teams in Pulumi.

1. Navigate to the *Users->Roles* view in OneLogin.
1. For each Group rule you created above for the Application, do the following:
   1. Select **New Role**
   1. Give it a name that matches the Group/Team name you are managing. (e.g. `AlphaTeam`)
   1. Associate the role with the OneLogin SCIM application you created above.
   1. Select **Save**

### Configure Users with Applicable Roles

These next steps associate users with given roles and, by extension, the Pulumi Team they should be added to.

1. Navigate to the *Users->Users* view in OneLogin.
1. For each user, select the user and then select the **Applications** view and select the applicable Role(s).
1. Select **Save User**.

### Removing Users from Group Provisioning

When ready to delete or suspend a user, execute the following steps to  ensure the user is removed from the applicable Pulumi Team as well as the Pulumi Organization:

1. In OneLogin navigate to the user being deleted or suspended.
1. Select the **Applications** view.
1. Deselect the Role(s) that represent Pulumi Team(s) for the given user.
1. Select **Save User**. This will remove the user from the applicable Pulumi Team(s).
1. Now you can suspend or delete the user from OneLogin.
