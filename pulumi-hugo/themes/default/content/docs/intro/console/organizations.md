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
- /docs/console/collaboration/organization-roles
- /docs/intro/console/organization-roles
- /docs/console/organization-roles
---

Organizations are a space for you to collaborate on shared projects and stacks.

## Organization Pages

| Console Page | Description |
|--------|--------|
| Dashboard | An overview of the organization including recently updated stacks, recent activity, and a resource count graph. |
| Projects | A searchable list of organization stacks that you can group by project and tag. For more information, see [Project and Stack Management]({{< relref "/docs/intro/console/projects-and-stacks" >}}). |
| Members | A list of active members of your Pulumi organization. |
| Teams | An [Enterprise]({{< relref "/pricing" >}}) feature that provides a way to assign stack permissions to groups of organization members. |
| Policies | Lists of organization policies and policy groups. Policies allow you to set guardrails to enforce best practices and compliance. |
| Settings | Organization settings including subscription and payment information and history, stack permissions, and links to Pulumi's [continuous delivery guides]({{< relref "/docs/guides/continuous-delivery" >}}). |

## Creating an Organization

Creating an organization will start a free trial that has access to all features.
At the end of the trial, you can choose to move to Team or Enterprise.
Learn more about the edition features on the [Pricing Page]({{< relref "/pricing" >}}).

To create an organization:

1. Select the organization menu at the top of the page.
1. Select **New organization...**
1. Provide an organization name, and agree to the terms of service and privacy policy.
1. Select **Start free trial**.

## Joining an Organization

To become a member of a Pulumi organization, you must be invited by an existing Pulumi
organization administrator or submit a request to the administrator for approval.
In addition, you may also need to be a member of the third-party organization or group backing the Pulumi organization.

For example, to become a member of a Pulumi organization backed by a GitLab Group,
you must associate a GitLab identity with your Pulumi account, and also
be a member of that GitLab group.

## Switching Between Organizations

The organization menu displays your individual account and all of the organizations you belong.

To switch to a different organization:

1. Select the organization  menu at the top of the page.
1. Select your organization name.

## Organization Roles

| Role | Description |
|--------|--------|
| Admin | Administrators have full access to the organization including: inviting members, creating teams and policies, managing stack permissions and [role-based access control, adjusting billing information, and controlling the organization settings. |
| Member | Members are able to view and edit stacks they have access to and view members and teams. |

## Organization Identity Providers

A Pulumi organization can use the Pulumi identity provider or a third-party identity provider.
If using a third-party identity provider all members need to belong to the third-party
identity provider in order to join a Pulumi organization.

For example, if a Pulumi organization, is backed by a GitHub organization, then only members
of that GitHub organization may be added to the Pulumi organization. Similarly, as soon as
someone loses access to the GitHub organization, they will no longer have access to the
Pulumi organization.

In addition, a Pulumi organization can be backed by a [SAML 2.0 identity provider]({{<
relref "/docs/guides/saml" >}}).

### Changing Identity Providers

Every organization is backed by an identity that governs the membership to your organization.
By default, when you create a new Pulumi organization, it uses the Pulumi identity provider.

Only organization admins can change the organization identity provider.

To change an organization's identity provider:

1. Navigate to the organization's **Settings**.
1. Navigate to **Access Management**.
1. Select **Change requirements**.

### GitHub Identity Provider

[Setting up a GitHub Organization](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/creating-a-new-organization-from-scratch)

To add a GitHub organization to Pulumi, an admin of the GitHub organization
must first grant the Pulumi OAuth app the [`read:org` scope](https://github.com/settings/connections/applications/7cf9078f3c92b17a5f0f).
This is required to verify memberships within the GitHub organization.
Pulumi will not have access to any of the organization's source code, issues, or other data.

### GitLab Identity Provider

[GitLab Groups](https://docs.gitlab.com/ce/user/group/)

To add a GitLab-backed organization to Pulumi, an admin of the GitLab group
must add the group to Pulumi, and invite its members to join Pulumi.

GitLab allows group admins to add members with a temporary membership, i.e., with an
expiration value. In order to invite those members to Pulumi, their membership in the
GitLab group must still be active. As soon as their GitLab group membership expires,
those users will lose access to Pulumi organization.

### Bitbucket Identity Provider

[BitBucket Workspaces](https://bitbucket.org/blog/introducing-workspaces)

To add a Bitbucket-backed organization to Pulumi, an admin of the Atlassian
Bitbucket workspace
must first grant the Pulumi Oauth app [read
access](https://confluence.atlassian.com/bitbucket/oauth-on-bitbucket-cloud-238027431.html#OAuthonBitbucketCloud-Scopes)
to their Bitbucket account and workspace membership information.

Once the Pulumi organization has been created, the admin can see a list of Bitbucket workspace
members that they can add or invite to the Pulumi organization.

### SAML Single Sign-on (SSO)

Pulumi Enterprise provides support for any SAML 2.0-based identity provider.

* [SAML-based configuration guide]({{< relref "/docs/guides/saml" >}})
* [Azure Active Directory]({{< relref "/docs/guides/saml/aad" >}})
* [G Suite]({{< relref "/docs/guides/saml/gsuite" >}})
* [Okta]({{< relref "/docs/guides/saml/okta" >}})
