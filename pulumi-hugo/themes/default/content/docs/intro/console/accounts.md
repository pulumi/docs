---
title: Accounts
meta_desc: An overview of Accounts within the Pulumi Cloud Service.
menu:
  intro:
    parent: console
    weight: 1
aliases:
  - /docs/intro/console/accounts/
  - /docs/intro/console/accounts/account/
  - /docs/intro/console/accounts-and-organizations/
  - /docs/intro/console/accounts-and-organizations/accounts/
---

If you haven't created your Pulumi account, navigate to [app.pulumi.com](https://app.pulumi.com) and sign
up. You may use any of the following identities to sign up:

* GitHub
* GitLab
* Atlassian
* [Email](https://app.pulumi.com/signin/email)
* [Single Sign-on](https://app.pulumi.com/signin/sso)

Your account lets you authenticate into the Pulumi Console, where you can do the
following:

* Manage your profile settings, including your account password, access tokens, and subscriptions
* [Add an organization]({{< relref "/docs/intro/console/organizations" >}}) backed by Atlassian, GitHub, GitLab, or a SAML
  2.0-compatible identity provider, such as Active Directory, Okta, or G Suite
* [Manage your projects and stacks]({{< relref "/docs/intro/console/project-and-stack-management" >}})

## Profile

Your Pulumi user account profile is used to identify you across the Pulumi
Console. Your account display name, avatar URL, and email address are
obtained from the identity provider you used for signing up.

### Editing Your Profile

To edit your profile information:

1. Select your profile picture.
1. Select **Settings**.
1. Use the **Edit profile** button.
1. Save your changes.

![User-profile page](/images/docs/reference/service/user-profile-page.png)

### Adding New Identities{#adding-new-identities}

You can associate your Pulumi account with multiple identities. In addition to the one you have originally configured, you can add your identities with the following third party providers:

{{< identities >}}

Connecting these additional identities will enable
you to join Pulumi organizations that are backed by those systems. Note that only
organization admins can add members to a Pulumi organization.

In order to be invited as a member of a Pulumi organization, you must connect
your account with the organization's backing identity provider. Once your
account is linked to your third party identity, you will then show up on the
list of users that the organization admin can invite.

## Account Security

This tab lets you change your password. Note that your password must be at least six characters long.

## Access Tokens

This tab lets you manage the [access tokens](https://en.wikipedia.org/wiki/Access_token) used for logging into the Pulumi service. It provides a list of all the access tokens associated with your account, including a description and last used information for each token.

When you run [`pulumi login`]({{< relref "/docs/reference/cli/pulumi_login" >}}) from the command line, you will be prompted for an access token. Once obtained, the access token logs you into the Pulumi Console and lets you interact with the Pulumi service and manage your stacks.

![Access tokens](/images/docs/reference/service/access-tokens.png)

### Creating Access Tokens

To create an access token:

1. Select your profile picture.
1. Select **Settings**.
1. Navigate to **Access Tokens**.
1. Select **Create token**.

### Deleting Access Tokens

To delete an access token:

1. Select your profile picture.
1. Select **Settings**.
1. Navigate to **Access Tokens**.
1. Use the trash can icon to delete a token.

## Subscription

This tab provides details on your subscription information, which is the Pulumi Community Edition by default. It also provides ways to contact Pulumi for additional support.

## Integrations

This tab provides a list of Pulumi's Continuous Delivery guides. Select your favorite CI/CD platform to learn more about how to integrate it with Pulumi.
