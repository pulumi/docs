---
title_tag: Configuring Okta | SCIM
meta_desc: This page describes how to support SCIM 2.0 functionality between Pulumi and Okta.
title: Okta
h1: "SCIM: Configuring Okta"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    pulumicloud:
        identifier: okta-scim
        parent: scim
        weight: 2
aliases:
  - /docs/guides/scim/okta/
---

This document outlines the steps required to help you configure automatic provisioning/deprovisioning of your users and groups in Pulumi using SCIM 2.0.

Please note that some advanced SCIM features aren't supported yet. For more information, see [Known Limitations](#known-limitations).

## Prerequisites

* Your organization must already be configured to use [SAML SSO](/docs/pulumi-cloud/access-management/saml/okta/) with Pulumi.
* You must be an admin of your Pulumi organization.
* (Optional, but highly recommended) You should have more than one admin for your Pulumi organization.

## Enabling SCIM For Your Okta Org

In order to configure SCIM for your Okta organization, you may need to email [support@okta.com](mailto:support@okta.com) and request that they enable `SCIM_PROVISIONING` for the organization.

Once the feature is enabled, navigate to the Pulumi application configured in your Okta org. Under the **General** tab, in the **App Settings** dialog box, locate the **Provisioning** section and select **SCIM**. Click **Save** to save your changes and close the **App Settings** dialog box.

![Okta Enabling SCIM](/images/docs/reference/service/scim/okta/general-enable-scim.png)

For more information on how to enable SCIM provisioning in Okta, see [How to Enable SCIM Provisioning in Custom App](https://support.okta.com/help/s/article/SCIM-Provisioning-Enabled-in-Custom-App) in the Okta documentation.

## Changing the SAML SSO Settings For SCIM

Depending on how you configured the application for SAML, you may need to adjust some of the attributes sent by Okta in SAML SSO requests. To make the changes, navigate to the **SAML Settings** section on the **General** tab, click **Edit**, and make the following changes:

1. Click **Next** on the first step.
2. In the **Attribute Statements** section, click **Add Another** and set the **Name** of the property to `email` and the value to be source from `user.email`. The ATTRIBUTE STATEMENTS should now be as follows:

    | Name | Name Format | Value |
    | --- | --- | --- |
    | firstName | Basic | user.firstName |
    | lastName | Basic | user.lastName |
    | email | Basic | user.email |

3. Click **Next** then click **Finish**.

![Okta SCIM Attributes](/images/docs/reference/service/scim/okta/attributes.png)

## Configuring the SCIM Connector

To configure the SCIM connector, click the **Provisioning** tab, and then select the **Integration** option in the left nav. Click **Edit**. Fill out the form as follows:

1. SCIM connector base URL: `https://api.pulumi.com/scim/v2/<orgName>`, where `<orgName>` must be replaced with your organization’s login name (not display name). If you do not know this, navigate to your SAML settings and look at the SSO URL. It will have your organization’s login name in the URL.
2. Supported provisioning actions: Check **Push New Users** and **Push Profile Updates**.
    {{% notes type="info" %}}
If you also want to support pushing existing Okta groups, the steps in [Setting up Group Provisioning](#groupprovisioning) describe how to set that up.
    {{% /notes %}}

3. Unique identifier field for users: Set to `userName`.
4. Authentication Mode: `HTTP Header`
5. For the **HTTP Header**, you will use a token from the [Pulumi Cloud](https://app.pulumi.com).

    To generate a token, navigate to your org in the Pulumi Cloud, click on the **Settings** tab, and then click **Access Management**. Scroll down to the **SCIM** section and generate a new token if you have never generated one for your org, or regenerate it if you have already done so in the past.

    {{% notes type="info" %}}
Once you generate the token, save it securely. Neither the Pulumi Cloud nor Pulumi support can retrieve a token once it's been initially generated. If you lose and need the SCIM token again, you'll have to generate a new token, invalidating any previous tokens for your Pulumi organization.
    {{% /notes %}}

6. Paste the token from the Pulumi Cloud into the Okta **Authorization** field under the **HTTP Header** section.

The following shows how your SCIM connection info should be filled in.

![Okta SCIM provisioning](/images/docs/reference/service/scim/okta/provisioning.png)

## Enabling SCIM Provisioning Actions

To configure the actions that Okta will send to the Pulumi Cloud, you need to enable them.

1. Under the **Provisioning** tab, click **Edit**.
2. While you are in the **To App** section, check **Enable** on the following:

    * Create Users
    * Update User Attributes
    * Deactivate Users
3. Select **Save**.

## Adjusting the Okta to Pulumi Attribute Mappings

Now that the SCIM connector knows how to connect to Pulumi, you need to adjust the attributes that Okta will send to Pulumi and what it might receive back from Pulumi. To do that, perform the following steps:

1. Under **Provisioning** > **To App**, click **Go to Profile Editor**.
2. Click **Mappings** to open the Attribute Editor dialog box.
3. Click on the **Okta User To …** tab and un-map all but the following attributes:

    * givenName
    * familyName
    * displayName
    * email

4. Click **Save Mappings**.
5. Click **Apply Updates**.

![Okta Profile Mapping](/images/docs/reference/service/scim/okta/profile-mapping.png)

## Adjusting the Okta to Pulumi Username Mappings

Pulumi usernames are immutable and should not be changed after a user is associated with a Pulumi application. To disable Okta from pushing username updates to Pulumi, perform the following steps:

1. Under **Sign On** in the **Settings** module, select **Edit**.
2. Under **Credentials Details**, change **Update application username on** from **Create and update** to **Create only**.
3. Select **Save**.

![Okta Usernames Set on Create Only](/images/docs/reference/service/scim/okta/usernames-set-on-create-only.png)

## Setting up Group Provisioning {#groupprovisioning}

The Pulumi Cloud supports the provisioning of teams within your organization using SCIM. This is done by mapping the groups you have created using SCIM to create teams within your organization in the Pulumi Cloud. Setting this up allows you to manage your teams' memberships solely in Okta.

To set this up, you need to enable Push Groups as a supported provisioning action under the **Provisioning** settings and then specify which groups you would like to push. To do that, perform the following steps:

1. Navigate to the application that you created above by clicking the on the **Applications** tab and then selecting the application.

    ![Okta application selection](/images/docs/reference/service/scim/okta/application-selection.png)

2. Click on **Provisioning** tab, then click on the integrations menu option located on the left side navigation.
3. Check the **Push Groups** box under **Supported provisioning actions**.
4. Select the **Push Groups** tab.
5. Select the **Push Groups** drop down menu. Here you will have the option to find groups either by name or rule.

    ![Push Groups drop down menu in Okta](/images/docs/reference/service/scim/okta/push-groups-menu.png)

6. Select **Find groups by name**. This will take you to a screen where you can search groups by the group name. Once you find the group(s) that you are looking for, click **Save**.

    You will notice there is a checkbox labeled **Push group memberships immediately**. This will also add all the members that are part of your group to the Pulumi team after your selection has been saved.

7. After clicking **Save**, you should see that your group was pushed and it should say **Active**.

    {{% notes type="info" %}}
If there are members in a group that are not yet assigned to the Pulumi Cloud application in Okta, they will not be added to the team in the Pulumi Cloud. Ensure that all members in the group have been assigned to the application before pushing the group.
    {{% /notes %}}

## Verifying Group Provisioning

To confirm that the groups were provisioned correctly, sign in to the Pulumi Cloud and select **Settings** > **Teams** from the left navigation.

![SCIM teams](/images/docs/reference/service/scim/okta/view-teams.png)

Teams provisioned with SCIM will be marked with a blue SSO icon. Select the provisioned team and verify its membership.

    {{% notes type="info" %}}
SCIM provisioned team memberships cannot be altered within the Pulumi Cloud. If any membership changes are needed, they must be done within Okta. This ensures your teams on the Pulumi side will always mirror the groups you have configured in Okta.
    {{% /notes %}}

## Known Limitations

Some SCIM features are currently not supported:

* Secondary emails
* Password sync
* Bulk importing
