---
title_tag: Configuring Azure Active Directory | SCIM
meta_desc: This page describes how to support SCIM 2.0 functionality between Pulumi and Azure AD.
title: Azure AD
h1: "SCIM: Configuring Azure Active Directory"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    pulumicloud:
        identifier: azuread-scim
        parent: scim
        weight: 1
aliases:
  - /docs/guides/scim/azuread/
---

This document outlines the steps required to configure automatic provisioning/deprovisioning of your users in Pulumi using SCIM 2.0.

Please note that some advanced SCIM features aren't supported yet. For more information, see [Known Limitations](#known-limitations).

## Prerequisites

* Your organization must already be configured to use [SAML SSO](/docs/pulumi-cloud/access-management/saml/aad/) with Pulumi.
* You must be an admin of your Pulumi organization.
* (Optional, but highly recommended) You should have more than one admin for your Pulumi organization.

## Enabling Automatic Provisioning

1. Navigate to the Azure Active Directory where you have configured Single Sign On using SAML with Pulumi.
2. Select **Enterprise Applications** and select the app in which you configured Single Sign On with Pulumi earlier.
3. Select the **Provisioning** feature, and change the value of **Provisioning Mode** to **Automatic**.

### Admin Credentials

Under the **Admin Credentials** section of the **Provisioning** feature, fill out the form as follows:

* **Tenant URL**: `https://api.pulumi.com/scim/v2/{orgName}`, where `{orgName}` must be replaced with your organization’s login name (not display name). If you do not know this, navigate to your SAML settings and look at the SSO URL. It will have your organization’s login name in the URL.
* **Secret Token**: You will use a token from the [Pulumi Cloud](https://app.pulumi.com) as the authorization bearer token. To generate a token, navigate to your org in the Pulumi Cloud, select **Settings**, then **Access Management**, and then in the **SCIM** section, generate a new token if you have never generated one for your org or regenerate it if you have already done so in the past.

    {{% notes "info" %}}
Once you generate the token, save it securely. Neither the Pulumi Cloud nor Pulumi support can retrieve a token once it's been initially generated. If you lose and need the SCIM token again, you'll have to generate a new token, invalidating any previous tokens for your Pulumi organization.
    {{% /notes %}}

Select **Test Connection**. You should get a success notification once the connection is successful.

### Mappings

Make sure the **Provision Azure Active Directory _Users_** mapping is enabled.

    {{% notes "info" %}}
If you are not yet ready to enable provisioning for Groups, disable that.
    {{% /notes %}}

![mappings](/images/docs/reference/service/scim/azuread/mappings.png)

### Adjust User Attribute Mappings

Update the mapping for **userName** so that is applied **Only during object creation**. In the **Mappings** expansion panel, click **Provision Azure Active Directory _Users_** and then click on the corresponding attribute mapping as shown below.

In the configuration window, change the value of the **Apply this mapping** drop-down to **Only during object creation**.

Make sure the mapping for the **userName** attribute is sourced from **userPrincipalName**, as indicated by the **Source attribute** drop-down.

The mapping should now be updated as shown below:

![userName](/images/docs/reference/service/scim/azuread/userName.png)

### Remove Unused Attributes

Delete all attributes **except** for the following using the **Delete** button:

* userName
* active
* displayName
* emails[type eq "work"].value
* name.givenName
* name.familyName

### Set The Emails Attribute To Required

In the user attribute mappings editor, scroll-down and click the **Show advanced options** checkbox and then the **Edit attribute list for customappsso** link.

![advanced options](/images/docs/reference/service/scim/azuread/advanced_options.png)

Check the **required** checkbox for the **emails** attribute, and click **Save**.

![email required](/images/docs/reference/service/scim/azuread/email_required.png)

You are now done with the Mappings configuration. Click **Save** and close the child windows/blades until you get back to the main **Provisioning** window where you can see the **Provisioning Status** drop-down.

## Enable Group Provisioning

To enable the provisioning of Azure AD groups to Pulumi Cloud, select **Edit Provisioning** and then select the **Provision Azure Active Directory Groups** setting under the **Mappings**
expansion panel and switch the **Enabled** setting to **Yes**.

### Update Group Attribute Mappings

Scroll-down to the Attribute Mappings section while you are editing the group provisioning setup and remove the mapping
between `objectId` and `externalId`. Click **Save** once you are done.

## Enable Provisioning

Under the **Settings** expansion panel, the **Scope** drop-down should be set to **Sync only assigned users and groups**. This ensures that only the users who are assigned to this application are synced with Pulumi, and not everyone in your Azure Active Directory.

![settings scope](/images/docs/reference/service/scim/azuread/settings_scope.png)

Set the **Provisioning Status** to **On** and then click **Save**.

## Assign Users and/or Groups

You must assign users to the Azure AD enterprise application to have them provisioned with an account in Pulumi. Click on the **Users and groups** feature in the left nav, and assign users and/or groups to the application by searching for them.

    {{% notes "info" %}}
If you did not enable group provisioning while you were editing the provisioning setup, click on **Edit Provisioning** and enable the **Provision Azure Active Directory Groups** setting as well under the **Mappings** expansion panel.
    {{% /notes %}}

Review the **Provisioning logs** to ensure there were no errors while provisioning the users. It may take a few minutes for logs to appear. If there were validation errors, you can correct them and try again, or contact Pulumi for support.

## Known Limitations

Some SCIM features are currently not supported:

* Secondary emails
* Password sync
* Bulk importing
