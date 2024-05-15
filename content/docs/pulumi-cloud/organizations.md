---
title_tag: "Pulumi Cloud Organizations"
meta_desc: Organizations are a space for you to collaborate on shared projects and stacks. Learn more about how Organizations work in the Pulumi Cloud.
title: "Organizations"
h1: Pulumi Cloud organizations
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  pulumicloud:
    weight: 2
aliases:
- /docs/reference/service/orgs/
- /docs/console/accounts/organizations/
- /docs/intro/console/accounts/organizations/
- /docs/console/collaboration/organization-roles/
- /docs/intro/console/organization-roles/
- /docs/console/organization-roles/
- /docs/intro/console/organizations/
- /docs/intro/pulumi-service/organizations/
- /docs/intro/pulumi-cloud/organizations/
---

Organizations are a space for you to collaborate on shared projects and stacks.

## Organization Pages

| Page | Description |
|--------|--------|
| Dashboard | An overview of the organization including recently updated stacks, recent activity, and a resource count graph. |
| All stacks | A searchable list of organization stacks that you can group by project and tag. For more information, see [Project and Stack Management](/docs/pulumi-cloud/projects-and-stacks/). |
| Policies | Lists of organization policies and policy groups. Policies allow you to set guardrails to enforce best practices and compliance. |
| Settings | Organization settings including subscription and payment information and history, Billing Managers, stack permissions, and links to Pulumi's [continuous delivery guides](/docs/using-pulumi/continuous-delivery/). |

## Creating an Organization

Creating an organization will start a free trial that has access to all features.
At the end of the trial, you can choose to move to the Pulumi Team Edition, the Pulumi Enterprise Edition or the Pulumi Business Critical Edition.
Learn more about the edition features on the [Pricing Page](/pricing/).

To create an organization:

1. Select the create organization button at the top of the  navigation.
1. Provide an organization name, and agree to the terms of service and privacy policy.
1. Select **Start free trial**.

## Joining an Organization

To become a member of a Pulumi organization, you must be invited by an existing Pulumi
organization administrator or submit a request to the administrator for approval.
In addition, you also need to be a member of the third-party organization or group backing the Pulumi organization.

For example, to become a member of a Pulumi organization backed by a GitLab Group,
you must associate a GitLab identity with your Pulumi account, and also
be a member of that GitLab group.

## Inviting Members to an Organization

Pulumi organization administrators can invite new members to an organization.

To invite a new member:

1. Navigate to **Settings** > **Members**.
2. To invite a new member using their email address, select **Invite members**. After the new member is invited, they will receive an email allowing them to accept the invite.
3. To invite a new member by sharing a link, select **Copy new invite link**. This will copy a link to your clipboard that you can share directly.

New member invitation links never expire and may only be used one time.

Pulumi organization administrators can monitor current organization members and pending invitations on the Members console page. For pending invitations, administrators can re-send email invitations, copy links for both email and link generated invitations, and revoke invitations. The invitation status column in the members table includes the date an invitation was sent, and will note if a potential member encountered an error while attempting to accept an invitation. In this case, a tooltip will share the exact error that was encountered.

## Switching Between Organizations

The organization menu displays your individual account and all of the organizations you belong.

To switch to a different organization:

1. Select the organization menu at the top of the navigation.
1. Select your organization name.

## Organization Roles

| Role | Description |
|--------|--------|
| Admin | Administrators have full access to the organization including: inviting members, creating teams and policies, managing stack permissions and [role-based access control, adjusting billing information, and controlling the organization settings. |
| Member | Members are able to view and edit stacks they have access to and view members and teams. |
| Billing Manager | Billing Managers are able to adjust billing information and view other Billing Managers. They do not have read or write access to stacks, teams, or policies. |

## Organization Identity Providers

A Pulumi organization can use the Pulumi identity provider or a third-party identity provider.
If using a third-party identity provider all members need to belong to the third-party
identity provider in order to join a Pulumi organization.

For example, if a Pulumi organization, is backed by a GitHub organization, then only members
of that GitHub organization may be added to the Pulumi organization. Similarly, as soon as
someone loses access to the GitHub organization, they will no longer have access to the
Pulumi organization.

In addition, a Pulumi organization can be backed by a [SAML 2.0 identity provider](/docs/pulumi-cloud/access-management/saml/).

### Changing Identity Providers

Every organization is backed by an identity that governs the membership to your organization.
By default, when you create a new Pulumi organization, it uses the Pulumi identity provider.

Only organization admins can change the organization identity provider.

Organization members must first add the new identity provider to their individual accounts before changing the organization identity provider, or members will be locked out of the organization.

To change an organization's identity provider:

1. Navigate to **Settings** > **Access Management**.
1. Select **Change requirements**.

### Disconnecting Identity Providers

In order to disconnect an identity provider you need to select another identity provider. This is also true for SAML SSO. To remove SAML SSO configuration, selected a new identity provider.

Organization members must first add the new identity provider to their individual accounts before changing the organization identity provider, or members will be locked out of the organization.

1. Navigate to **Settings** > **Access Management**.
1. Select **Change requirements**.
1. Select a new identity provider.

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
must first grant the Pulumi Oauth app [read access](https://confluence.atlassian.com/bitbucket/oauth-on-bitbucket-cloud-238027431.html#OAuthonBitbucketCloud-Scopes)
to their Bitbucket account and workspace membership information.

Once the Pulumi organization has been created, the admin can see a list of Bitbucket workspace
members that they can add or invite to the Pulumi organization.

### SAML Single Sign-on (SSO)

Pulumi Enterprise and Business Critical provide support for any SAML 2.0-based identity provider.

* [SAML-based configuration guide](/docs/pulumi-cloud/access-management/saml/)
* [Azure Active Directory](/docs/pulumi-cloud/access-management/saml/aad/)
* [Google Workspace](/docs/pulumi-cloud/access-management/saml/gsuite/)
* [Auth0](/docs/pulumi-cloud/access-management/saml/auth0/)
* [Okta](/docs/pulumi-cloud/access-management/saml/okta/)

Members of SSO organizations can login to Pulumi with the organization name auto-filled in the UI by visiting `https://app.pulumi.com/welcome/<organization-name>/sso`.
