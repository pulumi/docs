---
title_tag: SCIM 2.0 Integration Guides
title: SCIM 2.0 Integration
meta_desc: This page provides an overview of how to configure any SCIM 2.0 identity provider with the Pulumi Service.
menu:
    userguides:
        weight: 9
        identifier: scim

---

The [Pulumi Cloud](https://app.pulumi.com) supports System for Cross-domain Identity Management (SCIM) 2.0 integration with different identity providers. SCIM enables you to manage your users and groups centrally in your Identity Provider (IdP) and then synchronize those users and groups to the Pulumi Cloud. This support requires Pulumi Business Critical. To learn more about the capabilities of Pulumi Business Critical, see the [pricing page](/pricing/).

    {{% notes "info" %}}
If desired, in addition to the SCIM-managed teams, one can also configure and manage Pulumi-local teams in the Pulumi Cloud. See [Teams](/docs/intro/pulumi-cloud/teams/) for how to configure teams in the Pulumi Cloud.
    {{% /notes %}}

To set up synchronization between Pulumi and your SAML 2.0 identity provider, refer to one of our example guides:

- [Azure Active Directory](/docs/guides/scim/azuread/)
- [Okta](/docs/guides/scim/okta/)
- [OneLogin](/docs/guides/scim/onelogin/)
- [FAQ](/docs/guides/scim/faq/)
