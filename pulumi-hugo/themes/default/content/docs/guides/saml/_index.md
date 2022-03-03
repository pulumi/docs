---
title: SAML Single Sign-on (SSO)
meta_desc:
  This page provides an overview of how to configure any SAML 2.0 identity provider
  with the Pulumi Service.
menu:
  userguides:
    weight: 8
    identifier: saml

aliases:
  - /docs/reference/service/saml-overview/
  - /docs/console/accounts/saml/
---

The [Pulumi Service](https://app.pulumi.com) can be configured to work with any SAML 2.0 identity provider. SAML support requires Pulumi Enterprise or Pulumi Business Critical. To learn more about the capabilities of Pulumi Enterprise or Pulumi Business Critical, refer to the [pricing page]({{< relref "/pricing" >}}).

> Looking for information on how to enable SAML SSO for self-hosted Pulumi? Learn more [here]({{< relref "docs/guides/self-hosted/saml-sso" >}}).

## Single Sign-On (SSO)

If you're a member of a SAML-based Pulumi organization, you can sign in to [your account]({{< relref "/docs/intro/pulumi-service/accounts" >}}) via Single Sign-On. To learn about the important aspects of configuring SSO for your IdP, refer to the [SSO page]({{< relref "sso" >}}).

## Integration Guides

If you're looking to integrate Pulumi with your SAML 2.0 identity provider, refer to one of our example guides:

- [Azure Active Directory]({{< relref "aad" >}})
- [G Suite (Google)]({{< relref "gsuite" >}})
- [Okta]({{< relref "okta" >}})
- [OneLogin]({{< relref "onelogin" >}})
