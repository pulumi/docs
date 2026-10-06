---
title_tag: SCIM 2.0 Integration Guides
meta_desc: This page provides an overview of how to configure any SCIM 2.0 identity provider with Pulumi Cloud.
title: SCIM
h1: Pulumi Cloud & SCIM
menu:
  administration:
    parent: administration-guides
    weight: 2
    identifier: administration-guides-scim
aliases:
  - /docs/guides/scim/
  - /docs/pulumi-cloud/access-management/scim/
  - /docs/administration/access-identity/scim/
pulumi_cloud_feature: scim
---

[Pulumi Cloud](https://app.pulumi.com/signin) supports System for Cross-domain Identity Management (SCIM) 2.0 integration with different identity providers. SCIM enables you to manage your users and groups centrally in your Identity Provider (IdP) and then synchronize those users and groups to Pulumi Cloud.

SCIM provisions two things in Pulumi Cloud:

- **Users** become [members of your Pulumi organization](/docs/administration/concepts/organizations/), able to sign in through your identity provider.
- **Groups** become [teams](/docs/administration/concepts/rbac/teams/), and group membership becomes team membership. Grant those teams access to stacks, environments, and other entities with [RBAC](/docs/administration/concepts/rbac/).

Pulumi implements a single SCIM 2.0 endpoint. Every identity provider uses the same routes, schemas, and attributes, so only the IdP-side setup differs from one provider to the next. The guides at the end of this page cover popular providers.

{{% notes type="info" %}}
{{< sso-scim-limits-info idp="your Identity Provider" >}}
{{% /notes %}}

## Before you start

SCIM changes how accounts and teams behave in ways that matter before you connect an identity provider: deprovisioning deactivates users rather than deleting them, deleting a group deletes its team, usernames can't change after an account is created, and provisioned accounts become organization-managed. Read [SCIM provisioning](/docs/administration/concepts/scim/) for the capabilities, supported attributes, and [behavior to plan for](/docs/administration/concepts/scim/#behavior-to-plan-for).

## Next steps

To set up synchronization between Pulumi and your SAML 2.0 identity provider, refer to one of our example guides:

- [Microsoft Entra ID (formerly Azure Active Directory)](/docs/administration/guides/scim/entra/)
- [Okta](/docs/administration/guides/scim/okta/)
- [OneLogin](/docs/administration/guides/scim/onelogin/)

For the provisioning errors you are most likely to hit and how to resolve them, see [Troubleshooting](/docs/administration/guides/scim/troubleshooting/).
