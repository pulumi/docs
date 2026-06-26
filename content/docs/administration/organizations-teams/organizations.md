---
title_tag: "Pulumi Cloud Organizations"
meta_desc: Organizations are a space for you to collaborate on shared projects and stacks. Learn more about how Organizations work in the Pulumi Cloud.
title: "Organizations"
h1: Pulumi Cloud organizations
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  administration:
        name: Organizations
        parent: administration-organizations-teams
        weight: 1
        
aliases:
- /docs/administration/organizations-teams/organizations/
- /docs/reference/service/orgs/
- /docs/console/accounts/organizations/
- /docs/intro/console/accounts/organizations/
- /docs/console/collaboration/organization-roles/
- /docs/intro/console/organization-roles/
- /docs/console/organization-roles/
- /docs/intro/console/organizations/
- /docs/intro/pulumi-service/organizations/
- /docs/intro/pulumi-cloud/organizations/
- /docs/pulumi-cloud/organizations/
- /docs/pulumi-cloud/admin/organizations/
---

Organizations are a space for you to collaborate on shared projects and stacks.

## Organization Pages

| Page | Description |
|--------|--------|
| Dashboard | An overview of the organization including recently updated stacks, recent activity, and a resource count graph. |
| All stacks | A searchable list of organization stacks that you can group by project and tag. For more information, see [Stacks](/docs/iac/concepts/stacks/). |
| Policies | Lists of organization policies and policy groups. Policies allow you to set guardrails to enforce best practices and compliance. |
| Settings | Organization settings including subscription and payment information and history, Billing Managers, stack permissions, and links to Pulumi's [continuous delivery guides](/docs/using-pulumi/continuous-delivery/). |

## Creating an organization

Creating an organization will start a free trial that has access to all features.
At the end of the trial, you can choose to move to the Pulumi Team Edition, the Pulumi Enterprise Edition or the Pulumi Business Critical Edition.
Learn more about the edition features on the [Pricing Page](/pricing/).

To create an organization:

1. Select the create organization button at the top of the navigation.
1. Provide an organization name, and agree to the terms of service and privacy policy.
1. Select **Start free trial**.

## Joining an organization

To become a member of a Pulumi organization, you must be invited by an existing Pulumi
organization administrator or submit a request to the administrator for approval.
In addition, you also need to be a member of the third-party organization or group backing the Pulumi organization.

For example, to become a member of a Pulumi organization backed by a GitLab Group,
you must associate a GitLab identity with your Pulumi account, and also
be a member of that GitLab group.

For more information, see [How do I link an existing Pulumi account to my company's organization?](/docs/support/pulumi-cloud-faq/#how-do-i-link-an-existing-pulumi-account-to-my-companys-organization)

## Inviting members to an organization

Pulumi organization administrators can invite new members to an organization.

To invite a new member:

1. Navigate to **Settings** > **Members**.
1. To invite a new member using their email address, select **Invite members**. After the new member is invited, they will receive an email allowing them to accept the invite.
1. To invite a new member by sharing a link, select **Copy new invite link**. This will copy a link to your clipboard that you can share directly.

New member invitation links never expire and may only be used one time.

Pulumi organization administrators can monitor current organization members and pending invitations on the Members console page. For pending invitations, administrators can re-send email invitations, copy links for both email and link generated invitations, and revoke invitations. The invitation status column in the members table includes the date an invitation was sent, and will note if a potential member encountered an error while attempting to accept an invitation. In this case, a tooltip will share the exact error that was encountered.

## Switching between organizations

The organization menu displays your individual account and all of the organizations you belong.

To switch to a different organization:

1. Select the organization menu at the top of the navigation.
1. Select your organization name.

## Organization roles

| Role | Description |
|--------|--------|
| Admin | Administrators have full access to the organization including: inviting members, creating teams and policies, managing stack permissions and role-based access control, adjusting billing information, and controlling the organization settings. |
| Member | Members are able to view and edit stacks they have access to and view members and teams. |
| Billing Manager | Billing Managers are able to adjust billing information and view other Billing Managers. They do not have read or write access to stacks, teams, or policies. |

## Updating billing information

Organization admins and Billing Managers can update payment details from the organization's **Billing & usage** settings in [Pulumi Cloud](https://app.pulumi.com/signin) under **Payment methods**.

To update billing information:

1. Navigate to **Settings** > **Billing & usage**.
1. Under **Payment methods**, select **Update**.

If you need to delegate billing-only access to a team member without granting full admin rights, see [Billing Managers](/docs/administration/organizations-teams/billing-managers/).

## Changing the company name on invoices

The company name that appears on Pulumi invoices is sourced from your organization's display name. To change it, update the display name and the change will be reflected on your next invoice. Updates take effect within a short time after saving.

To update your organization's display name:

1. Navigate to **Settings** > **General**.
1. Update the **Display Name** field and save your changes.

Updating the display name requires the `organization:rename` permission, which is granted to organization admins.

If you need a legal entity name on invoices that is different from your organization's product-facing display name, [contact support](/support/).

## Transferring stacks

Stack admins can transfer individual stacks between personal accounts and organizations, or between organizations. Organization admins can transfer stacks in bulk.

Transferring a stack requires two permissions: the right to transfer the stack from its current owner, and the right to create stacks in the destination organization. Both are configured through your organization's access controls — see [Role-based access control](/docs/administration/access-identity/rbac/) for details.

To transfer an individual stack:

1. Navigate to the stack and then the stack's **Settings**.
1. Select **Transfer stack**.
1. Provide the destination personal account or organization name and select **Transfer**.

To transfer stacks in bulk:

1. Navigate to the **Stacks** page.
1. Select the three dot menu beside **Create project**.
1. Choose **Transfer stacks** from the dropdown.
1. Choose the **Transfer destination** from the dropdown.
1. Tick the stacks you'd like to transfer (up to 15 at a time) and select **Transfer stacks**.

## Restoring a deleted stack

{{% notes type="info" %}}
The ability to restore a deleted stack is limited to Enterprise and Business Critical editions.
{{% /notes %}}

Restoring a stack recovers a previously deleted stack along with its update history. The 25 most recently deleted stacks in an organization can be restored by an organization admin.

To restore a stack:

1. Navigate to the **Stacks** page.
1. Select the three dot menu beside **Create project**.
1. Choose **Restore deleted stacks** from the dropdown.
1. Use the three dot menu on the stack you want to restore and select **Restore stack**.

## Deleting an organization

Organization deletion is a permanent action and can only be performed by an organization admin.

To delete an organization:

1. Navigate to **Settings**.
1. Select **Delete organization**.

Before deleting an organization, make sure you have transferred any stacks you want to keep to another organization or individual account.

For more information, see [How can I delete a Pulumi organization?](/docs/support/pulumi-cloud-faq/#how-can-i-delete-a-pulumi-organization)

## Deleting your account

You can delete your personal Pulumi account from your account settings in [Pulumi Cloud](https://app.pulumi.com/signin).

Before deleting your account, make sure you have transferred any stacks you want to keep and that you are no longer required as an admin in any organization.

For more information, see [How can I delete my Pulumi account?](/docs/support/pulumi-cloud-faq/#how-can-i-delete-my-pulumi-account)

## Organization identity providers

A Pulumi organization can use the Pulumi identity provider or a third-party identity provider.
If using a third-party identity provider all members need to belong to the third-party
identity provider in order to join a Pulumi organization.

For example, if a Pulumi organization, is backed by a GitHub organization, then only members
of that GitHub organization may be added to the Pulumi organization. As soon as
someone loses access to the GitHub organization, they will no longer have access to the
Pulumi organization.

A Pulumi organization can also be backed by a [SAML 2.0 identity provider](/docs/administration/access-identity/saml/).

### Changing identity providers

Every organization is backed by an identity that governs the membership to your organization.
By default, when you create a new Pulumi organization, it uses the Pulumi identity provider.

Only organization admins can change the organization identity provider.

Organization members must first add the new identity provider to their individual accounts before changing the organization identity provider, or members will be locked out of the organization.

To change an organization's identity provider:

1. Navigate to **Settings** > **Access Management**.
1. Select the **Other** tab.
1. In the **Membership Requirements** section, select **Change requirements**.

### Disconnecting identity providers

In order to disconnect an identity provider you need to select another identity provider. This is also true for SAML SSO. To remove SAML SSO configuration, select a new identity provider.

Organization members must first add the new identity provider to their individual accounts before changing the organization identity provider, or members will be locked out of the organization.

1. Navigate to **Settings** > **Access Management**.
1. Select the **Other** tab.
1. In the **Membership Requirements** section, select **Change requirements**.
1. Select a new identity provider.

### GitHub identity provider

[Setting up a GitHub Organization](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/creating-a-new-organization-from-scratch)

To add a GitHub organization to Pulumi, an admin of the GitHub organization
must first grant the Pulumi OAuth app the [`read:org` scope](https://github.com/settings/connections/applications/7cf9078f3c92b17a5f0f).
This is required to verify memberships within the GitHub organization.
Pulumi will not have access to any of the organization's source code, issues, or other data.

### GitLab identity provider

[GitLab Groups](https://docs.gitlab.com/user/group/)

To add a GitLab-backed organization to Pulumi, an admin of the GitLab group
must add the group to Pulumi, and invite its members to join Pulumi.

GitLab allows group admins to add members with a temporary membership, i.e., with an
expiration value. In order to invite those members to Pulumi, their membership in the
GitLab group must still be active. As soon as their GitLab group membership expires,
those users will lose access to Pulumi organization.

### Bitbucket identity provider

[BitBucket Workspaces](https://support.atlassian.com/bitbucket-cloud/docs/what-is-a-workspace/)

To add a Bitbucket-backed organization to Pulumi, an admin of the Atlassian
Bitbucket workspace
must first grant the Pulumi Oauth app [read access](https://confluence.atlassian.com/bitbucket/oauth-on-bitbucket-cloud-238027431.html#OAuthonBitbucketCloud-Scopes)
to their Bitbucket account and workspace membership information.

Once the Pulumi organization has been created, the admin can see a list of Bitbucket workspace
members that they can add or invite to the Pulumi organization.

### SAML Single Sign-on (SSO)

Pulumi Enterprise and Business Critical provide support for any SAML 2.0-based identity provider.

* [SAML-based configuration guide](/docs/administration/access-identity/saml/)
* [Microsoft Entra ID](/docs/administration/access-identity/saml/entra/)
* [Google Workspace](/docs/administration/access-identity/saml/gsuite/)
* [Auth0](/docs/administration/access-identity/saml/auth0/)
* [Okta](/docs/administration/access-identity/saml/okta/)

Members of SSO organizations can login to Pulumi with the organization name auto-filled in the UI by visiting `https://app.pulumi.com/welcome/<organization-name>/sso`.
