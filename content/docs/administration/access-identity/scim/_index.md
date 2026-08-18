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

SCIM provisions two things in Pulumi Cloud:

- **Users** become [members of your Pulumi organization](/docs/administration/organizations-teams/organizations/), able to sign in through your identity provider.
- **Groups** become [teams](/docs/administration/access-identity/rbac/teams/), and group membership becomes team membership. Grant those teams access to stacks, environments, and other entities with [RBAC](/docs/administration/access-identity/rbac/).

Pulumi implements a single SCIM 2.0 endpoint. Every identity provider uses the same routes, schemas, and attributes, so only the IdP-side setup differs from one provider to the next. The guides at the end of this page cover popular providers, and everything documented on this page applies to each of them.

{{% notes type="info" %}}
{{< sso-scim-limits-info idp="your Identity Provider" >}}
{{% /notes %}}

## Capabilities

| Capability | Support |
|---|---|
| User provisioning | Yes (create, read, update, and search) |
| User deprovisioning | Yes, but soft only (see [Deprovisioning never deletes a user](#deprovisioning-never-deletes-a-user)) |
| Group-to-team synchronization | Yes (create, read, update, delete, and membership changes) |
| `PATCH` | Yes, for both users and groups |
| Filtering | `userName eq` for users and `displayName eq` for groups. `eq` is the only supported operator |
| Pagination | Users only, up to 100 results per page. A group search returns every match in a single response |

## Supported attributes

The lists below are complete. Pulumi implements the core SCIM 2.0 schemas only, so a request that adds or updates any attribute not listed here fails with a `400 invalidPath` response. See [Unknown path](/docs/support/faq/scim/#unknown-path) in the SCIM FAQ.

For users:

- `userName` (immutable after creation, see [Usernames cannot change](#usernames-cannot-change))
- `displayName`
- `name.givenName`
- `name.familyName`
- `emails[type eq "work"].value`
- `active`

For groups:

- `displayName`
- `members`

## What SCIM does not manage

| Feature | Notes |
|---|---|
| Roles and administrator status | Pulumi does not implement the `roles` or `entitlements` attributes. A user provisioned through SCIM is always created as an organization member, and a group member is always added to the team as a plain member. Promote users to admin in the Pulumi Cloud console |
| `externalId` | Accepted on users but never stored, and not part of the group schema at all. Remove any `externalId` mapping for groups in your IdP |
| Bulk operations | Not supported. Provision resources one request at a time |
| Sorting | Not supported |
| ETags | Not supported |
| Password synchronization | Not supported. Credentials stay in your IdP |
| Enterprise User extension | Not supported. Only the core SCIM 2.0 user and group schemas are implemented |
| Secondary emails | Not supported. Only the primary work email is used |

## Behavior to plan for

These apply to every identity provider, regardless of which guide you follow.

### Deprovisioning never deletes a user

Pulumi has no endpoint for deleting a user through SCIM. Deprovisioning sets `active` to `false`, which removes the user's access to the organization while preserving their account and its history. Configure your IdP to suspend or deactivate users rather than delete them.

Teams are different: a group deleted in your IdP does delete the corresponding Pulumi team.

### Usernames cannot change

A Pulumi username is immutable once the account exists, because it identifies the user across every organization they belong to. If your IdP pushes a changed `userName` on an update, the request fails with a `400 immutability` response. Map `userName` so that it applies only when the account is created, not on later updates. Each provider guide covers where to set this.

### Group members must already be provisioned

Pulumi validates every member of a group before creating or updating the corresponding team. If any member has not yet been provisioned into your organization, or has been deactivated, the entire request fails with a `400` response and no membership changes are applied. Provision users before pushing the groups that contain them.

Member validation reads up to 3000 identities per request, which is a practical ceiling on the size of a SCIM-managed team.

{{% notes type="warning" %}}
A group search returns every team in your organization whose display name matches the filter, not only the teams that SCIM created. Pulumi-local teams and teams backed by a GitHub organization appear in the results alongside SCIM-provisioned ones. If your IdP reconciles group state, it may see teams it does not own.
{{% /notes %}}

## Next steps

To set up synchronization between Pulumi and your SAML 2.0 identity provider, refer to one of our example guides:

- [Microsoft Entra ID (formerly Azure Active Directory)](/docs/administration/access-identity/scim/entra/)
- [Okta](/docs/administration/access-identity/scim/okta/)
- [OneLogin](/docs/administration/access-identity/scim/onelogin/)

For the provisioning errors you are most likely to hit and how to resolve them, see the [SCIM FAQ](/docs/support/faq/scim/).
