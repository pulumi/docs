---
title_tag: "Pulumi Cloud: Create Accounts"
meta_desc: Learn how to create and configure accounts in the Pulumi Cloud in this guide.
title: Accounts
h1: Pulumi Cloud accounts
menu:
  pulumicloud:
    weight: 1
aliases:
- /docs/intro/console/accounts/
- /docs/intro/console/accounts/account/
- /docs/intro/console/accounts-and-organizations/
- /docs/intro/console/accounts-and-organizations/accounts/
- /docs/intro/pulumi-service/accounts/
- /docs/intro/pulumi-cloud/accounts/
---

To create your Pulumi account, navigate to [app.pulumi.com](https://app.pulumi.com) and sign
up. You may use any of the following identities to sign up:

* GitHub
* GitLab
* Atlassian
* [Email](https://app.pulumi.com/signin/email)
* [Single Sign-on](https://app.pulumi.com/signin/sso)

Your account lets you authenticate with the Pulumi Cloud, where you can do the
following:

* Manage your profile settings, including your account password, access tokens, and subscriptions
* [Add an organization](/docs/pulumi-cloud/organizations/) backed by Atlassian, GitHub, GitLab, or a SAML
  2.0-compatible identity provider, such as Active Directory, Okta, or Google Workspace.
* [Manage your projects and stacks](/docs/pulumi-cloud/projects-and-stacks/)

## Profile

Your Pulumi user account profile is used to identify you in the Pulumi
Cloud. Your account display name, avatar URL, and email address are
obtained from the identity provider you used when signing up.

### Editing Your Profile

To edit your profile information:

1. Select your profile picture.
1. Select **Account settings**.
1. Use the **Edit profile** button.
1. Save your changes.

### Adding New Identities{#adding-new-identities}

You can associate your Pulumi account with multiple identities. In addition to the one you have originally configured, you can add your identities with the following third party providers:

{{< identities >}}

Connecting these additional identities will enable
you to join Pulumi organizations that are backed by those systems. Only
organization admins can add members to a Pulumi organization.

In order to be invited as a member of a Pulumi organization, you must connect
your account with the organization's backing identity provider. Once your
account is linked to your third party identity, you will then show up on the
list of users that the organization admin can invite.

## Password Reset

For users who signed up with email, you may change your password by:

1. Use the organization selector to choose your individual account.
1. Navigate to **Settings** > **Account security**
1. Reset your password. Your password must be at least ten characters long.

## Personal Access Tokens

Use access tokens to sign into the Pulumi Cloud via the CLI. On this page there is a list of all your personal access tokens, including a description and last used information for each token.

When you run [`pulumi login`](/docs/cli/commands/pulumi_login) from the command line, you will be prompted for an access token. Once obtained, the access token logs you into the Pulumi Cloud and lets you interact with the Pulumi Cloud and manage your stacks.

These access tokens have the same permission as your user. If  you instead would like to scope the token to an organization, use [Organization Access Tokens](/docs/pulumi-cloud/access-management/organization-access-tokens/).

![Access tokens](/images/docs/reference/service/access-tokens.png)

### Creating Personal Access Tokens

To create an access token:

1. Select **Personal access tokens** from the user menu.
1. Select **Create token**.

### Deleting Personal Access Tokens

To delete an access token:

1. Select **Personal access tokens** from the user menu.
1. Select **Delete token** from the 3-dot menu at the end of the table row.

## Subscription

Your individual account is on the Pulumi Individual Edition and this cannot be changed. To collaborate with others create an organization.

## Integrations

This page provides a list of Pulumi's Continuous Delivery guides. Select your favorite CI/CD platform to learn more about how to integrate it with Pulumi.
