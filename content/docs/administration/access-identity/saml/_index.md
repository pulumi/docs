---
title_tag: SAML Single Sign-On (SSO) Guides
meta_desc:
  This page provides an overview of how to configure any SAML 2.0 identity provider
  with Pulumi Cloud.
title: SAML(SSO)
h1: Pulumi Cloud SAML(SSO)
menu:
  administration:
    parent: administration-access-identity
    weight: 6
    identifier: administration-access-identity-saml
aliases:
- /docs/reference/service/saml-overview/
- /docs/console/accounts/saml/
- /docs/guides/saml/
- /docs/pulumi-cloud/access-management/saml/
pulumi_cloud_feature: saml-sso
---

The [Pulumi Cloud](https://app.pulumi.com/signin) can be configured to work with any SAML 2.0 identity provider.

{{% notes type="info" %}}
Running self-hosted Pulumi Cloud? You'll first need to [configure your self-hosted infrastructure for SAML SSO](/docs/administration/self-hosting/saml-sso/) (API service keys and environment variables), then return here to complete IdP configuration.
{{% /notes %}}

## Single Sign-On (SSO)

If you're a member of a SAML-based Pulumi organization, you can sign in to [your account](/docs/administration/organizations-teams/accounts/) via Single Sign-On. To learn about the important aspects of configuring SSO for your IdP, refer to the [SSO page](sso/).

{{% notes type="info" %}}
{{< sso-scim-limits-info >}}
{{% /notes %}}

## Connect SAML SSO to an existing account

If you already have a Pulumi account and need to access a SAML-based organization, connect that organization's SAML SSO identity to your existing account rather than signing in to the organization directly. Signing in directly can produce an "Email already in use" error when your email already belongs to an account, and that screen cannot resolve the conflict on its own.

To connect a SAML SSO identity to your existing account:

1. Sign in to [Pulumi Cloud](https://app.pulumi.com/signin) with your existing account.
1. Navigate to **Account Settings > Connect SAML SSO**.
1. Enter the name of the organization you want to access, then complete the single sign-on prompt with your identity provider.

After your identity provider confirms your identity, Pulumi adds the organization's SAML identity to your existing account and grants you access to the organization.

If the connection fails, confirm with your organization administrator that your identity provider assigns you to the Pulumi application for that organization and that the SAML `NameID` it sends is stable. An unstable `NameID` can create duplicate identities and repeat the conflict.

## Integration Guides

If you're looking to integrate Pulumi with your SAML 2.0 identity provider, refer to one of our example guides:

- [Microsoft Entra ID (formerly Azure Active Directory)](entra/)
- [Google Workspace (formerly G Suite)](gsuite/)
- [JumpCloud](jumpcloud/)
- [Okta](okta/)
- [Auth0](auth0/)
- [OneLogin](onelogin/)
