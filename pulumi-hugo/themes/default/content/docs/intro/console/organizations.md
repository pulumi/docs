---
title: Organizations
meta_desc: An overview of Organizations within the Pulumi Cloud Service.
menu:
  intro:
    parent: console
    weight: 2
aliases:
- /docs/reference/service/orgs/
- /docs/console/accounts/organizations/
- /docs/intro/console/accounts/organizations/
---

An organization is the primary grouping unit for stacks within the Pulumi Console.
When you sign into the Pulumi Console, a personal account is automatically
created for you and subscribed to the Pulumi Community plan.

You can be a member of multiple Pulumi organizations.

If you're a Pulumi organization admin, you have the
ability to:

* [Invite users]({{< relref "/docs/intro/console/organization-roles#organization-membership" >}})
* Manage default stack permissions for the organization
* [Create teams]({{< relref "/docs/intro/console/teams#creating-a-team" >}}) and manage their permissions
* Assign [organization roles]({{< relref "/docs/intro/console/organization-roles" >}}) for role-based access control (RBAC)
to your organization's stacks

## Creating an Organization

To create an organization:

1. Select the organization menu at the top of the page.
1. Select **New organization...**
1. Provide an organization name, and agree to the terms of service and privacy policy.
1. Select **Start free trial**.

You can create a new Pulumi organization directly from the Pulumi Console.

## Organization Types

A Pulumi organization needs to be linked to a third-party identity provider, offering an
additional layer
of security for you and your team. While membership within the Pulumi organization is
managed by
an organization admin, you must be a member of the backing third-party identity
provider in order
to join a Pulumi organization.

For example, if a Pulumi organization, is backed by a GitHub organization, then only members
of that GitHub organization may be added to the Pulumi organization. Similarly, as soon as
someone loses access to the GitHub organization, they will no longer have access to the
Pulumi organization.

{{% notes %}}
See [Organization Roles]({{< relref "/docs/intro/console/organization-roles" >}}) or
[Adding New Identities]({{< relref "/docs/intro/console/accounts#adding-new-identities" >}})
for more information.
{{% /notes %}}

The following table shows the relationship between a Pulumi organization and third-party
groupings.

| Pulumi | GitHub | GitLab | Bitbucket |
|--------|--------|--------|--------|
| Organization | [Organization](https://github.com/collab-uniba/socialcde4eclipse/wiki/How-to-setup-a-GitHub-organization,-project-and-team) | [Group](https://docs.gitlab.com/ce/user/group/)| [Workspace](https://bitbucket.org/blog/introducing-workspaces) |

In addition, a Pulumi organization may be backed by a [SAML 2.0 identity provider]({{<
relref "/docs/guides/saml" >}}).

### GitHub-backed

To add a GitHub-backed organization to Pulumi, an admin of the GitHub organization
must
first grant the Pulumi OAuth app the `read:org` scope. This can be done on GitHub's
[Applications
page](https://github.com/settings/connections/applications/7cf9078f3c92b17a5f0f).

Pulumi requires the [`read:org`
scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/#available-scopes)
in order to verify memberships within the GitHub organization. The Pulumi Console
will not have access to any of the organization's source code, issues, or other data.

### GitLab-backed

To add a GitLab-backed organization to Pulumi, an admin of the GitLab group
may add the group to Pulumi, and invite its members to join Pulumi.

GitLab allows group admins to add members with a temporary membership, i.e., with an
expiration value. In order to invite
those members to Pulumi, their membership in the GitLab group must still be active. As
soon as their
GitLab group membership expires, those users will lose access to the GitLab-backed
organization on Pulumi.

### Bitbucket-backed

To add a Bitbucket-backed organization to Pulumi, an admin of the Atlassian
Bitbucket workspace
must first grant the Pulumi Oauth app [read
access](https://confluence.atlassian.com/bitbucket/oauth-on-bitbucket-cloud-238027431.html#OAuthonBitbucketCloud-Scopes)
to their Bitbucket account and workspace membership information.

Once the Pulumi organization has been created, the admin can see a list of Bitbucket workspace
members
that they can add or invite to the Pulumi organization. See [Switching
Organizations](#switching-organizations)
to learn more.

## SAML Single Sign-on (SSO)

Pulumi Enterprise provides more options for identity and access, including
support for any SAML 2.0-based identity provider.

* [SAML-based configuration guide]({{< relref "/docs/guides/saml" >}})
* [Azure Active Directory]({{< relref "/docs/guides/saml/aad" >}})
* [G Suite]({{< relref "/docs/guides/saml/gsuite" >}})
* [Okta]({{< relref "/docs/guides/saml/okta" >}})

If you need help configuring or would like us to officially support another SAML identity
provider,
please [contact us]({{< relref "/about#contact-us" >}}).

## Changing Membership Requirements

Every organization is backed by an identity. The identity governs the membership to your org.
By default, when you add a new org to Pulumi, it uses the Pulumi identity. This means the membership is
_only_ governed by a user having a Pulumi account and no additional identity requirements are placed on members.

{{% notes %}}
Regardless of the identity your org uses, org membership is always invite-only. Only the creator of the org gets automatic access. Everyone else must be invited by an admin to be admitted into the org.
{{% /notes %}}

However, if you want your org to mirror an org on a third party identity service such as GitHub, GitLab, or Bitbucket, you can
change the backing identity. Enterprises can also choose SAML as the backing identity provider for an org as discussed in [SAML Single Sign-on](#saml-single-sign-on-sso). Changing your org's backing identity essentially changes the membership requirements you place
on your members.

Before you change your org's backing identity, ensure that all of its current members can satisfy the membership
requirement of the org in the new identity service. That is, if you are switching from a GitHub-backed to a GitLab-backed
org, ensure that all of your members are actually a member of the corresponding GitLab Group which your org would be
changed to inherit from.

To switch an organization's backing identity you must be an organization admin.

To change an organization's membership requirements:

1. Navigate to the organization's **Settings**.
1. Navigate to **Access Management**.
1. Select **Change requirements**.

## Switching Organizations

The Organization drop-down list displays all of the organizations your account is
associated with, and lets you add a new organization backed by a third
party identity provider.

To switch to your personal account or a different organization:

1. Select the organization menu at the top of the page.
1. Select your organization name.

<img class="lg:max-w-xl" src="/images/docs/reference/service/organization-view.png" alt="Stack Outputs and Configuration">

  _Members_. Pulumi organization members only see the Stacks and People tabs.

  _Admins_. Pulumi organization admins see the Stacks, People, Teams, Webhooks,
and Settings tabs.

| Console Tab | Description |
|--------|--------|
| Dashboard | An overview of the organization including recently updated stacks, recent activity, and a resource count graph. |
| Projects | A searchable list of organization stacks that you can group by project and tag. For more information, see [Project and Stack Management]({{< relref "/docs/intro/console/project-and-stack-management" >}}). |
| Members | A list of active members of the Pulumi organization. |
| Teams | A [Team Pro]({{< relref "/pricing" >}}) feature that provides a way to assign stack permissions to groups of organization members. |
| Policies | Lists of organization policies and policy groups. Policies allow you to set guardrails to enforce best practices and compliance. |
| Settings | Organization settings including subscription and payment information and history, stack permissions, and links to Pulumi's [continuous delivery guides]({{< relref "/docs/guides/continuous-delivery" >}}). |
