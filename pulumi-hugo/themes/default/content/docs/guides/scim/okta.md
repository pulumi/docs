---
title: Configuring SCIM in Okta
meta_desc: This page describes how to support SCIM 2.0 functionality between Pulumi and Okta.
menu:
    userguides:
        parent: scim
        weight: 1
---

This document outlines the steps required to help you configure automatic provisioning/deprovisioning of your users and groups in Pulumi using SCIM 2.0.

Please note that some advanced SCIM features aren't supported yet. For more information, see [Known Limitations]({{< relref "#known-limitations" >}}).

## Prerequisites

* Your organization must already be configured to use [SAML SSO]({{< relref "/docs/guides/saml/aad" >}}) with Pulumi.
* You must be an admin of your Pulumi organization.
* (Optional, but highly recommended) You should have more than one admin for your Pulumi organization.

## Enabling SCIM For Your Okta Org

In order to configure SCIM for your Okta organization, you may need to email support@okta.com and request that they enable `SCIM_PROVISIONING` for the organization.

Once the feature is enabled, navigate to the Pulumi SAML app configured in your Okta org from the **Classic UI**. Under the **General** tab, in the **App Settings** dialog box, locate the **Provisioning** section and select **SCIM**. Click **Save** to save your changes and close the **App Settings** dialog box.

For more information on how to enable SCIM provisioning in Okta, see [How to Enable SCIM Provisioning in Custom App](https://support.okta.com/help/s/article/SCIM-Provisioning-Enabled-in-Custom-App) in the Okta documentation.

## Changing the SAML SSO Settings For SCIM

As part of the setup process, you need to adjust some of the parameters sent by a SAML SSO request. To make the changes, navigate to the **SAML Settings** section, click **Edit**, and make the following changes:

1. Click **Next** on the first step.
2. On Step 2, in the **General** section, set the application username to **Okta username prefix**.
3. In the **Attribute Statements** section, click **Add Another** and set the **Name** of the property to `email` and the value to be source from `user.email`. The ATTRIBUTE STATEMENTS should now be as follows:

    | Name | Name Format | Value |
    | --- | --- | --- |
    | firstName | Basic | user.firstName |
    | lastName | Basic | user.lastName |
    | email | Basic | user.email |

4. Click **Next** then click **Finish**.

## Configuring the SCIM Connector

To configure the SCIM connector, click the **Provisioning** tab, and then select the **Integration** option in the left nav. Click **Edit**. Fill out the form as follows:

* SCIM connector base URL: `https://api.pulumi.com/scim/v2/{orgName}`, where `{orgName}` must be replaced with your organization’s login name (not display name). If you do not know this, navigate to your SAML settings and look at the SSO URL. It will have your organization’s login name in the URL.
* Supported provisioning actions: Check **Push New Users** and **Push Profile Updates**.
    {{% notes "info" %}}
If you also want to support pushing existing Okta groups, the steps in [Setting up Group Provisioning]({{< relref "#groupprovisioning" >}}) describe how to set that up.
    {{% /notes %}}

* Unique identifier field for users: Set to `userName`.
* Authentication Mode: HTTP Header
* For **HTTP HEADER**, you will use a token from the [Pulumi Service](https://app.pulumi.com) as the authorization bearer token. To generate a token, navigate to your org in the Pulumi Service, click on the **Settings** tab, and then click **SAML SSO**. Scroll down to the **SCIM** section and generate a new token if you have never generated one for your org, or regenerate it if you have already done so in the past.

    {{% notes "info" %}}
Once you generate the token, please save it securely. Neither the Pulumi Service nor Pulumi support can retrieve a token once it's been initially generated. If you lose the SCIM token and need it again, you'll have to generate a new token, which invalidates any previous tokens for your Pulumi organization.
    {{% /notes %}}

* Paste the token from the Pulumi Service into the Okta SCIM configuration for **HTTP HEADER**.

The following shows how your SCIM connection info should be filled in.

![Okta SCIM provisioning](/images/docs/guides/scim/okta-scim-provisioning.png)

## Enabling SCIM Provisioning Actions

To configure the actions that Okta will send to the Pulumi Service, you need to enable them.

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
3. Un-map all but the following attributes:

    * givenName
    * familyName
    * displayName
    * email

4. Click on the **Okta User To …** tab and un-map all but the following attributes:

    * givenName
    * familyName
    * displayName
    * email

5. Click **Save Mappings**.
6. Click **Apply Updates**.

## Setting up Group Provisioning {#groupprovisioning}

The Pulumi Service supports the provisioning of teams within your organization using SCIM. This is done by mapping the groups you have created using SCIM to create teams within your organization in the Pulumi Service. Setting this up allows you to manage your teams' memberships solely in Okta.

To set this up, you need to enable Push Groups as a supported provisioning action under the **Provisioning** settings and then specify which groups you would like to push. To do that, perform the following steps:

1. Navigate to the application that you created above by clicking the on the **Applications** tab and then selecting the application.

    ![Okta application selection.](/images/docs/guides/scim/okta-application-selection-scim.png)

2. Click on **Provisioning** tab, then click on the integrations menu option located on the side navigation.
3. Check the **Push Groups** box under **Supported provisioning actions**.
4. Select the **Push Groups** tab.
5. Select the **Push Groups** drop down menu. Here you will have the option to find groups either by name or rule.

    ![Push Groups drop down menu in Okta](/images/docs/guides/scim/okta-pushgroups-menu-scim.png)

6. Select **Find groups by name**. This will take you to a screen where you can search groups by the group name. Once you find the group(s) that you are looking for, click **Save**.

    You will notice there is a checkbox labeled **Push group memberships immediately**. This will also add all the members that are part of your group to the Pulumi team after your selection has been saved.

7. After clicking **Save**, you should see that your group was pushed and it should say **Active**.

    {{% notes "info" %}}
If there are members in a group that are not yet assigned to the Pulumi Service application in Okta, they will not be added to the team in the Pulumi Service. Ensure that all members in the group have been assigned to the application before pushing the group.
    {{% /notes %}}

## Verifying Group Provisioning

To confirm that the groups were provisioned correctly, sign in to the Pulumi Service and select the **Teams** tab where you should see the team listed.

![SCIM teams.](/images/docs/guides/scim/console.png)

Click on that group and verify its membership. Note that the team’s membership cannot be altered within the Pulumi Service. If any membership changes are needed, they must be done within Okta. This allows the membership to be managed using Okta so your teams on the Pulumi side will always mirror the groups you have configured there.

## Known Limitations

Some SCIM features are currently not supported:

* Secondary emails
* Password sync
* Bulk importing
