---
title_tag: Configuring JumpCloud | SAML SSO
meta_desc: This page provides a walkthrough of the important aspects of configuring
  JumpCloud as a SAML SSO identity provider (IdP) for Pulumi Cloud.
meta_image: /images/docs/meta-images/docs-meta.png
title: JumpCloud
h1: "SAML: Configuring JumpCloud"
menu:
  administration:
    name: JumpCloud
    parent: administration-access-identity-saml
    weight: 45
    identifier: pulumi-cloud-access-management-saml-jumpcloud
aliases:
- /docs/pulumi-cloud/access-management/saml/jumpcloud/
---

This guide walks you through configuring JumpCloud as a [SAML SSO](/docs/administration/access-identity/saml/) identity provider (IdP) for Pulumi Cloud.

{{% notes type="info" %}}
JumpCloud SAML SSO requires the **SSO Package** or higher, or the SSO add-on feature. Confirm your subscription includes SSO access before proceeding.
{{% /notes %}}

## Creating the JumpCloud application

1. Sign in to the [JumpCloud Admin Portal](https://console.jumpcloud.com/).
1. Navigate to **Access** > **SSO Applications**.
1. Select **+ Add New Application**.
1. Search for **Pulumi** to use the pre-built connector, or select **Custom Application** if a pre-built connector is not available, then select **Next**.
1. On the **Select Options** page, choose the applicable options and select **Next**.
1. On the **Enter General Info** page, enter a display name (for example, _Pulumi Cloud_), an optional description, and a user portal image. See [Pulumi Logos](/brand/#logos) for official artwork.
1. Optionally expand **Advanced Settings** to set a custom value for the IdP URL endpoint. JumpCloud uses this to construct your SSO IdP URL in the format `https://sso.jumpcloud.com/saml2/<custom_value>`.

    {{% notes type="warning" %}}
    The SSO IdP URL cannot be changed after the application is created. Choose the custom value carefully.
    {{% /notes %}}

1. Select **Save Application**, then **Configure Application**.

## Configuring the JumpCloud application

After saving the application, JumpCloud opens the application configuration panel. Select the **SSO** tab and fill in the SAML settings.

{{< saml-warning >}}

| JumpCloud SSO Setting | Value |
| --------------------- | ----- |
| SP Entity ID | `https://api.pulumi.com/login/acmecorp/sso/saml/metadata` |
| ACS URL | `https://api.pulumi.com/login/acmecorp/sso/saml/acs` |
| Default RelayState | `https://api.pulumi.com/login/acmecorp/sso` |
| SAMLSubject NameID | `email` |
| SAMLSubject NameID Format | `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress` |
| Signature Algorithm | `RSA-SHA256` |

{{% notes type="warning" %}}
Do not change the **SAMLSubject NameID Format** after users have already signed in via SAML SSO. Changing it will break existing user sessions.
{{% /notes %}}

When you are done, select **Save**.

## Assigning users to the application

Assign users to the JumpCloud application before they can sign in with SSO.

1. From the application configuration panel, select the **User Groups** tab.
1. Check the box next to each user group you want to grant access.
1. Select **Save**.

## Exporting the JumpCloud metadata file

Pulumi requires the IdP metadata XML from JumpCloud to complete SSO configuration.

1. From the **SSO** tab of the application, select **Export Metadata** to download the metadata XML file.

    Alternatively, navigate to **Access** > **SSO Applications**, check the box next to your Pulumi application in the **Configured Applications** list, and select **Export Metadata** in the top-right corner.

1. Save the downloaded `JumpCloud-<applicationname>-metadata.xml` file; you will need it in the next step.

## Configuring your Pulumi organization

1. Sign in to [Pulumi Cloud](https://app.pulumi.com) and navigate to your organization.
1. Select the **Settings** tab, then **Access Management**.
1. Under **Membership Requirements**, select **Change requirements**.
1. Select **SAML SSO** and select **Next**.
1. Paste the contents of the JumpCloud metadata XML file into the **Identity Provider Metadata** field.
1. Select **Apply changes**.

## Signing in with JumpCloud

Once SAML SSO is configured, members of your Pulumi organization can sign in using either of the following methods:

- **IdP-initiated:** Select the Pulumi tile in the JumpCloud User Console. JumpCloud authenticates the user and redirects them to Pulumi Cloud automatically.
- **SP-initiated:** Navigate to `https://app.pulumi.com/signin/sso/`, enter your Pulumi organization name, and you will be redirected to JumpCloud to authenticate.

## Optional: automated user provisioning with SCIM

JumpCloud supports SCIM 2.0, which can automatically provision, update, and deprovision users and groups in Pulumi Cloud based on JumpCloud directory state. SAML SSO must be fully configured before enabling SCIM.

To retrieve the SCIM token from Pulumi Cloud:

1. Navigate to your organization in Pulumi Cloud.
1. Select the **Settings** tab, then **SAML SSO**.
1. Scroll to the **SCIM** section and generate a new token. Copy it immediately—it is only shown once.

When configuring SCIM in JumpCloud, use the following values:

| SCIM Setting | Value |
| ------------ | ----- |
| Base URL | `https://api.pulumi.com/scim/v2/acmecorp` |
| Token Key | The token generated from the Pulumi SAML SSO settings page |

For full SCIM configuration steps on the JumpCloud side, refer to JumpCloud's [Integrate with Pulumi](https://jumpcloud.com/support/integrate-with-pulumi) support article. For Pulumi's SCIM provisioning documentation, see [SCIM](/docs/administration/access-identity/scim/).

{{% notes type="info" %}}
SCIM provisioning supports creating, updating, and deactivating users, as well as creating and managing groups. Secondary emails, password sync, and bulk importing are not supported.
{{% /notes %}}

## Troubleshooting

If you encounter issues with your JumpCloud SAML configuration, refer to the [SAML troubleshooting guide](/docs/administration/access-identity/saml/troubleshooting/) for common error patterns and remediation steps.
