---
title: SCIM 2.0 Integration
meta_desc: This page provides an overview of how to configure any SAML 2.0 identity provider
           with the Pulumi Console.
menu:
    userguides:
        weight: 9
        identifier: scim

---

The [Pulumi Console](https://app.pulumi.com) supports System for Cross-domain Identity Management (SCIM) 2.0 integration with different identity providers. SCIM enables you to manage your users and groups centrally in your Identity Provider (IdP) and then synchronize those users and groups to the Pulumi Console. This support requires Pulumi Enterprise. To learn more about the capabilities of Pulumi Enterprise, see the [pricing page]({{< relref "/pricing" >}}).

    {{% notes "info" %}}
If desired, in addition to the SCIM-managed teams, one can also configure and manage Pulumi-local teams in the Pulumi console. See [Teams]({{< relref "/docs/intro/console/teams" >}}) for how to configure teams in the Pulumi console.
    {{% /notes %}}

To set up synchronization between Pulumi and your SAML 2.0 identity provider, refer to one of our example guides:

- [Azure Active Directory]({{< relref "/docs/guides/scim/azuread" >}})
- [Okta]({{< relref "/docs/guides/scim/okta" >}})
- [FAQ]({{< relref "/docs/guides/scim/faq" >}})
