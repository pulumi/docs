---
title_tag: SCIM 2.0 Integration Guides
meta_desc: This page provides an overview of how to configure any SCIM 2.0 identity provider with Pulumi Cloud.
title: SCIM
h1: Pulumi Cloud & SCIM
menu:
  administration:
    parent: administration-access-identity
    weight: 7
    identifier: administration-access-identity-scim
aliases:
  - /docs/guides/scim/
  - /docs/pulumi-cloud/access-management/scim/
pulumi_cloud_feature: scim
---

The [Pulumi Cloud](https://app.pulumi.com/signin) supports System for Cross-domain Identity Management (SCIM) 2.0 integration with different identity providers. SCIM enables you to manage your users and groups centrally in your Identity Provider (IdP) and then synchronize those users and groups to the Pulumi Cloud.

    {{% notes type="info" %}}
If desired, in addition to the SCIM-managed teams, one can also configure and manage Pulumi-local teams in the Pulumi Cloud. See [Teams](/docs/administration/organizations-teams/teams/) for how to configure teams in the Pulumi Cloud.
    {{% /notes %}}

{{% notes type="info" %}}
{{< sso-scim-limits-info idp="your Identity Provider" >}}
{{% /notes %}}

To set up synchronization between Pulumi and your SAML 2.0 identity provider, refer to one of our example guides:

- [Microsoft Entra ID (formerly Azure Active Directory)](/docs/administration/access-identity/scim/entra/)
- [Okta](/docs/administration/access-identity/scim/okta/)
- [OneLogin](/docs/administration/access-identity/scim/onelogin/)
- [FAQ](/docs/support/faq/scim/)
