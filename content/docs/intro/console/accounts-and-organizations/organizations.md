---
title: Organizations
meta_desc: An overview of Organizations within the Pulumi Cloud Service.
aliases:
- /docs/reference/service/orgs/
- /docs/console/accounts/organizations/
- /docs/intro/console/accounts/organizations/
---

An organization is the primary grouping unit for stacks within the Pulumi Console.
When you sign into the Pulumi Console, an individual organization is automatically
created for you and subscribed to the Pulumi Community edition.

You can however be a member of multiple Pulumi organizations, and collaborate
with other developers.

If you're an admin of a Pulumi organization, you have the
ability to:

* [Add users]({{< relref "../collaboration/organization-roles/#organization-membership" >}})
* Manage default stack permissions for the organization
* Create [teams]({{< relref "../collaboration/teams" >}}) and manage their permissions
* Assign [organization roles]({{< relref "../collaboration/organization-roles" >}}) for role-based access control (RBAC)
to your organization's stacks

## Creating a New Organization

You can create a new Pulumi organization directly from the Pulumi Console.

<a class="btn btn-secondary" href="https://app.pulumi.com/site/organizations/add"
target="_blank">
    CREATE ORGANIZATION
</a>

## Organization Types

A Pulumi organization needs to be linked to a third-party identity provider, offering an
additional layer
of security for you and your team. While membership within the Pulumi organization is
managed by
an organization administrator, you must be a member of the backing third-party identity
provider in order
to join a Pulumi organization.

For example, if a Pulumi organization, `https://app.pulumi.com/robot-co`, is backed by
a GitHub organization,
`https://github.com/robot-co`, then only members of `https://github.com/robot-co` may be
added to `https://app.pulumi.com/robot-co`.
Similarly, as soon as someone loses access to the GitHub organization, they will no
longer have access to the Pulumi organization it is backing.

{{% notes %}}
See <a href="{{< relref "organization-roles" >}}">Organization Roles</a> or
<a href="{{< relref "accounts#adding-new-identities" >}}">Adding New Identities</a>
for more information.
{{% /notes %}}

The following table shows the relationship between a Pulumi organization and third-party
groupings.

| Pulumi | GitHub | GitLab | Bitbucket |
|--------|--------|--------|--------|
| Organization | [Organization](https://github.com/collab-uniba/socialcde4eclipse/wiki/How-to-setup-a-GitHub-organization,-project-and-team) | [Group](https://docs.gitlab.com/ce/user/group/)| [Team](https://confluence.atlassian.com/bitbucket/teams-321853005.html) |

In addition, a Pulumi organization may be backed by a [SAML 2.0 identity provider]({{<
relref "/docs/guides/saml" >}}).

### GitHub-backed

To add a GitHub-backed organization to Pulumi, an administrator of the GitHub organization
must
first grant the Pulumi OAuth app the `read:org` scope. This can be done on GitHub's
[Applications
page](https://github.com/settings/connections/applications/7cf9078f3c92b17a5f0f).

Pulumi requires the [`read:org`
scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/#available-scopes)
in order to verify memberships within the GitHub organization. The Pulumi Console
will not have access to any of the organization's source code, issues, or other data.

### GitLab-backed

To add a GitLab-backed organization to Pulumi, an administrator of the GitLab group
may add the group to Pulumi, and invite its members to join Pulumi.

GitLab allows group admins to add members with a temporary membership, i.e., with an
expiration value. In order to invite
those members to Pulumi, their membership in the GitLab group must still be active. As
soon as their
GitLab group membership expires, those users will lose access to the GitLab-backed
organization on Pulumi.

### Bitbucket-backed

To add a Bitbucket-backed organization to Pulumi, an administrator of the Atlassian
Bitbucket team
must first grant the Pulumi Oauth app [read
access](https://confluence.atlassian.com/bitbucket/oauth-on-bitbucket-cloud-238027431.html#OAuthonBitbucketCloud-Scopes)
to their Bitbucket account and team membership information.

Once the Pulumi organization has been created, the admin can see a list of BitBucket team
members
that they can add or invite to the Pulumi organization. See [Switching
Organizations](#switching-organizations)
to learn more.

## SAML Single Sign-on (SSO)

The Pulumi Enterprise edition provides more options for identity and access, including
support for
any SAML 2.0-based identity provider.

[Learn more]({{< relref "/docs/guides/saml" >}}) about configuring a SAML-based
organization on Pulumi. Or refer to one
of our guides:

* [Azure Active Directory]({{< relref "/docs/guides/saml/aad" >}})
* [G Suite]({{< relref "/docs/guides/saml/gsuite" >}})
* [Okta]({{< relref "/docs/guides/saml/okta" >}})

If you need help configuring or would like us to officially support another SAML identity
provider,
please [contact us]({{< relref "/about#contact-us" >}}).

## Switching Organizations

The Organization drop-down list displays all of the organizations your account is
associated with, and lets you add a new organization backed by a third
party identity provider. To switch to a different organization:

1. Click on the organization drop-down list on the upper left corner of the Console screen
next to the Pulumi logo.
1. Select your organization name. The organization page view is dependent on your role within the Pulumi organization.

<img class="lg:max-w-xl" src="/images/docs/reference/service/organization-view.png" alt="Stack Outputs and Configuration">

  _Members_. Pulumi organization members only see the Stacks and People tabs.

  _Admins_. Pulumi organization administrators see the Stacks, People, Teams, Webhooks,
and Settings tabs.

| Console Tab | Description |
|--------|--------|
| Stacks | A searchable list of organization stacks that you can group by project and tag. See [Project and Stack Management]({{< relref "../collaboration/project-and-stack-management"
>}}) to learn more. |
| People | A list of active members of the Pulumi organization. |
| Teams | A [Team Pro](https://www.pulumi.com/pricing/) feature that provides a way to assign stack permissions to groups of organization members. |
| Webhooks | A [Team Pro](https://www.pulumi.com/pricing/) feature that allows external services to be notified about events happening on an organization, including events occurring on organization stacks. |
| Settings | A place for you to manage your organization settings including subscription and payment information and history, base permissions to all of the organization's stacks (including stack creation and deletion), and links to Pulumi's [continuous delivery guides]({{< relref "/docs/guides/continuous-delivery" >}}). |

## Next Steps

* [Organization Roles]({{< relref "../collaboration/organization-roles" >}})
