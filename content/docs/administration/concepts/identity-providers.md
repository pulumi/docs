---
title_tag: "Pulumi Cloud: Organization Identity Providers"
meta_desc: How Pulumi Cloud organizations are backed by GitHub, GitLab, Bitbucket, or a SAML 2.0 identity provider, and how to set up or change the provider.
title: Identity Providers
h1: Pulumi Cloud organization identity providers
menu:
  administration:
    name: Identity Providers
    parent: administration-concepts
    weight: 2
    identifier: administration-concepts-identity-providers
---

Every Pulumi organization is backed by exactly one identity provider, which governs who is allowed to be a member. New organizations use the Pulumi identity provider, where membership is managed entirely in Pulumi Cloud. You can instead back an organization with a GitHub organization, a GitLab group, a Bitbucket workspace, or a SAML 2.0 identity provider.

When an organization is backed by a third party, membership is the intersection of two things: a user must belong to the Pulumi organization *and* be a current member of the backing organization, group, or workspace. As soon as someone loses access to the backing system, they lose access to the Pulumi organization.

A user who belongs to the backing system but has not been added to the Pulumi organization yet is a *potential member*. Potential members appear on the list of people an organization admin can invite, but they cannot use the organization until they are added.

## Available identity providers

| Identity provider | Membership comes from | Setup |
|---|---|---|
| Pulumi | The Pulumi organization's own member list | The default for new organizations. No third-party configuration required. |
| GitHub | A GitHub organization | [GitHub](#github) |
| GitLab | A top-level GitLab group | [GitLab](#gitlab) |
| Bitbucket | A Bitbucket workspace | [Bitbucket](#bitbucket) |
| SAML 2.0 | The users your identity provider assigns to the Pulumi application | [SAML 2.0](#saml-20) |

These options are mutually exclusive. An organization uses one identity provider at a time, and selecting a new one replaces the old one.

## Before you change identity providers

Changing an organization's identity provider takes effect immediately, and Pulumi does not check in advance whether your existing members can meet the new requirement. Anyone who cannot is locked out until they can.

Before you change providers:

1. Link an identity from the new provider to your own Pulumi account first. You cannot select a provider you have no identity for, and if you lock yourself out you cannot change the setting back.
1. Confirm that every member has linked an identity from the new provider to their Pulumi account, under **Account settings** > **Identity providers**. For the steps, see [Adding new identities](/docs/administration/concepts/accounts/#adding-new-identities).
1. Confirm that every member belongs to the GitHub organization, GitLab group, or Bitbucket workspace you are about to require.

Members who do not meet the new requirement are not deleted. Their membership records remain in place, and they regain access as soon as they link the required identity and belong to the backing organization.

## Permissions

Changing the identity provider requires the `organization:change_backend` permission, shown as **Change organization backend** in Pulumi Cloud. Organization admins have it by default, and you can grant it to a [custom role](/docs/administration/concepts/rbac/roles/). See [Organization settings scopes](/docs/administration/reference/rbac-scopes/org-settings/).

Some providers add a requirement on top of this one. To select a Bitbucket workspace, you must also be an admin of that workspace. See [Bitbucket](#bitbucket).

## Changing your organization's identity provider

1. Navigate to **Settings** > **Access management**.
1. Select the **Other** tab.
1. In the **Membership Requirements** section, select **Change requirements**.
1. On the **Select Requirements** step, choose an identity provider, then choose the specific organization, group, or workspace that should back your Pulumi organization.
1. On the **Confirm Requirements** step, review the change and select **Apply changes**.

The change takes effect immediately and is recorded in your [audit logs](/docs/administration/concepts/audit-logs/). Admins can change the requirement again at any time.

{{% notes type="info" %}}
A given GitHub organization, GitLab group, or Bitbucket workspace can back only one Pulumi organization. If it already backs another one, Pulumi rejects the change.
{{% /notes %}}

The **Membership Requirements** section does not appear for individual accounts or for legacy per-stack organizations, because membership works differently for those.

## GitHub

A GitHub-backed organization draws its membership from a [GitHub organization](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/creating-a-new-organization-from-scratch). Only members of that GitHub organization can belong to the Pulumi organization.

To back your organization with GitHub:

1. Connect a GitHub identity to your Pulumi account under **Account settings** > **Identity providers**.
1. Make sure the Pulumi OAuth app is authorized for the GitHub organization with the [`read:org` scope](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps), which Pulumi uses to verify who belongs to the organization. You can review and grant that access on the [Pulumi OAuth app's page in your GitHub settings](https://github.com/settings/connections/applications/7cf9078f3c92b17a5f0f). Depending on the GitHub organization's third-party application policy, a GitHub organization owner may need to grant or approve this access. Pulumi does not get access to source code, issues, or any other organization data.
1. [Change your organization's identity provider](#changing-your-organizations-identity-provider) and select the GitHub organization.

If the backing GitHub organization enforces its own SAML SSO, each member must also authorize their GitHub credential for that organization. Until they do, GitHub does not report their membership to Pulumi and they cannot access the Pulumi organization.

## GitLab

A GitLab-backed organization draws its membership from a top-level [GitLab group](https://docs.gitlab.com/user/group/). Subgroups cannot back a Pulumi organization.

To back your organization with GitLab:

1. Connect a GitLab identity to your Pulumi account under **Account settings** > **Identity providers**.
1. Make sure the group is visible to your GitLab account.
1. [Change your organization's identity provider](#changing-your-organizations-identity-provider) and select the GitLab group.

GitLab lets group owners grant memberships that expire. A member whose GitLab group membership has expired, or is in any state other than active, loses access to the Pulumi organization.

## Bitbucket

A Bitbucket-backed organization draws its membership from a [Bitbucket workspace](https://support.atlassian.com/bitbucket-cloud/docs/what-is-a-workspace/). Bitbucket identities are labeled **Atlassian** in your account settings.

{{% notes type="info" %}}
Unlike GitHub and GitLab, Bitbucket requires that whoever makes the change be an admin of the target Bitbucket workspace. Bitbucket's member-listing API behaves differently for admins than for other members, so Pulumi verifies this up front rather than failing later.
{{% /notes %}}

To back your organization with Bitbucket:

1. Connect an Atlassian identity to your Pulumi account under **Account settings** > **Identity providers**, granting the Pulumi OAuth app [read access](https://confluence.atlassian.com/bitbucket/oauth-on-bitbucket-cloud-238027431.html#OAuthonBitbucketCloud-Scopes) to your account and workspace membership information.
1. Confirm that you are an admin of the workspace.
1. [Change your organization's identity provider](#changing-your-organizations-identity-provider) and select the Bitbucket workspace.

Once the change is complete, admins can see the list of Bitbucket workspace members and add or invite them to the Pulumi organization.

## SAML 2.0

{{< pulumi-cloud "saml-sso" />}}

A SAML-backed organization draws its membership from the users your identity provider assigns to the Pulumi application. Pulumi Cloud works with any SAML 2.0 identity provider, including Microsoft Entra ID, Google Workspace, Okta, OneLogin, Auth0, and JumpCloud.

Configuring SAML is covered by the [SAML SSO guides](/docs/administration/guides/saml/). Two things are specific to switching your organization to SAML:

- **You become the organization owner.** Pulumi makes the user who applies the SAML configuration the organization owner, so that an error in the identity provider metadata cannot lock everyone out of the organization.
- **Your account cannot have other commitments.** You must not belong to unrelated Pulumi organizations, and your individual account must not own any stacks or environments. Transfer or delete them first.

[SCIM provisioning](/docs/administration/guides/scim/) is available only for SAML-backed organizations, and the **SAML & SCIM** settings tab appears only once your organization is SAML-backed. Switching a SAML organization to another identity provider stops SCIM provisioning.

Members of a SAML organization can sign in with the organization name pre-filled by visiting `https://app.pulumi.com/welcome/<organization-name>/sso`.

## Removing a third-party identity provider

You remove a third-party identity provider by selecting a different one — there is no "none" option. To go back to managing membership entirely in Pulumi Cloud, follow [Changing your organization's identity provider](#changing-your-organizations-identity-provider) and select **Pulumi**.

This is also how you remove a SAML SSO configuration.

## Learn more

- [Accounts](/docs/administration/concepts/accounts/) — linking third-party identities to your individual Pulumi account.
- [Organizations](/docs/administration/concepts/organizations/) — creating organizations, inviting members, and organization roles.
- [SAML SSO](/docs/administration/guides/saml/) — configuring Pulumi Cloud with a SAML 2.0 identity provider.
- [SCIM](/docs/administration/guides/scim/) — automating user and team provisioning from your identity provider.
- [Organization settings scopes](/docs/administration/reference/rbac-scopes/org-settings/) — the full list of organization-level RBAC permissions.
