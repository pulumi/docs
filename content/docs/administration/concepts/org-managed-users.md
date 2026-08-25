---
title_tag: "Organization-Managed Users | Pulumi Cloud"
meta_desc: What an organization-managed Pulumi Cloud account is, how SAML and SCIM create one, and the restrictions that apply to it.
title: Organization-Managed Users
h1: Organization-Managed Users
menu:
    administration:
        name: Organization-Managed Users
        parent: administration-concepts
        weight: 3
pulumi_cloud_feature: saml-sso
---

An organization-managed user is a Pulumi Cloud account that belongs to an organization rather than to an individual. The organization's identity provider creates the account and remains the source of truth for it.

For an administrator, this is what makes your Pulumi organization a closed system. Accounts are created, updated, and deactivated from your identity provider, so your Pulumi roster matches your directory and deprovisioning a user in the identity provider revokes their Pulumi access. An account you provision can't be carried into unrelated Pulumi organizations, can't accumulate login methods you don't control, and can't be used to create organizations outside your billing and governance.

## How an account becomes organization-managed

An account becomes organization-managed in one of three ways:

- **Signing in to a SAML organization for the first time.** If you have no Pulumi account and you authenticate through an organization's [SAML single sign-on](/docs/administration/guides/saml/), Pulumi creates one for you. That account is managed by the organization from the moment it exists.
- **SCIM provisioning.** An organization that uses [SCIM](/docs/administration/guides/scim/) provisions accounts from its identity provider. Every account SCIM creates is organization-managed.
- **Migrating an existing account.** If you already have an ordinary Pulumi account, you can hand it over to an organization yourself with the **Migrate to Org-Managed Account** control in **Account settings**. The migration is opt-in, and it's [destructive](#migrating-an-existing-account).

## Organization-managed is not the same as SAML membership

Belonging to a SAML-backed organization does not make an account organization-managed. Members of either kind sign in through the same identity provider, so what distinguishes them is where the account came from:

| How the account came to be | Organization-managed |
|---|---|
| The organization created it: the user signed in through its SAML SSO with no prior Pulumi account, or SCIM provisioned them | Yes |
| The user created it, and later joined the organization by [connecting its SAML identity](/docs/administration/guides/saml/#connect-saml-sso-to-an-existing-account) or accepting an invitation | No |

An ordinary account that joins a SAML organization keeps everything an ordinary account has. It gains a SAML identity, and nothing else changes: it can still belong to other organizations, connect other identity providers, and create organizations.

## Restrictions

An organization-managed user is subject to three restrictions that an ordinary Pulumi account isn't:

- **Organization membership.** The account can belong to the organization that manages it, and to organizations related to that one as part of a multi-organization arrangement. Invitations to any other organization are rejected. A user who needs access to an unrelated Pulumi organization has to create a separate Pulumi account that isn't organization-managed.
- **Additional identities.** The account can't connect the identity providers described in [Adding new identities](/docs/administration/concepts/accounts/#adding-new-identities). GitHub, GitLab, Atlassian, and Google identities are unavailable. A user managed by a multi-organization is the one exception, and a narrow one: they can connect the SAML identities of related organizations.
- **Creating organizations.** The account can't [create an organization](/docs/administration/concepts/organizations/#creating-an-organization).

## Migrating an existing account

Migrating an ordinary account to an organization-managed one is permanent and destructive, and it takes effect immediately.

{{% notes type="warning" %}}
Migrating an account removes it from every organization other than the one taking it over and that organization's related organizations, and deletes every linked identity except the managing organization's SAML identity. Any authentication method that depended on a deleted identity, such as GitHub or Google, stops working. Single sign-on through the managing organization becomes the account's only authentication method.
{{% /notes %}}

Before you migrate:

1. [Transfer any stacks](/docs/administration/concepts/organizations/#transferring-stacks) you want to keep out of the organizations you're about to leave.
1. Confirm that you don't hold an admin role that another organization depends on.
1. Make sure you can sign in through the managing organization's identity provider.

To migrate the account:

1. Navigate to **Account settings**.
1. Under your email address, select **Migrate to Org-Managed Account**.

The [SAML admin](/docs/administration/guides/saml/saml-admin/) role is the exception to the single-authentication-method rule. It exists so that at least one person can still sign in if the SAML configuration breaks, so a SAML admin keeps an alternative login method for as long as they hold the role, and loses it when the role passes to someone else.

## Learn more

- [Accounts](/docs/administration/concepts/accounts/)
- [Organizations](/docs/administration/concepts/organizations/)
- [SAML single sign-on](/docs/administration/guides/saml/)
- [SCIM](/docs/administration/guides/scim/)
