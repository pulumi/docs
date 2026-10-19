---
title_tag: "Accounts | Pulumi Cloud"
meta_desc: A Pulumi account is the identity you authenticate with. Learn how accounts are created and identified, and how an account differs from an organization.
title: Accounts
h1: Accounts
menu:
  administration:
    name: Accounts
    parent: administration-concepts
    weight: 4
aliases:
- /docs/administration/organizations-teams/accounts/
- /docs/intro/console/accounts/
- /docs/intro/console/accounts/account/
- /docs/intro/console/accounts-and-organizations/
- /docs/intro/console/accounts-and-organizations/accounts/
- /docs/intro/pulumi-service/accounts/
- /docs/intro/pulumi-cloud/accounts/
- /docs/pulumi-cloud/accounts/
- /docs/pulumi-cloud/access-management/accounts/
---

An _account_ is the identity you authenticate with in Pulumi Cloud. It represents a person, it is unique to that person, and it is what the CLI, the console, and the REST API act on your behalf as. Every Pulumi Cloud user has exactly one account, no matter how many organizations they belong to.

An account is not the same thing as an [organization](/docs/administration/concepts/organizations/). Your account is who you are; an organization is where you and your colleagues collaborate. Stacks, environments, teams, policies, and billing belong to an organization — never to an account directly.

## Accounts and organizations

Signing up creates your account, not an organization. Because stacks are addressed as `<organization>/<project>/<stack>`, you need an organization before you can create a stack, so right after signup Pulumi Cloud asks how you plan to use it and creates your first organization from your answer:

- **I'm building a product for work** creates an organization with the name you choose and starts a 14-day free trial that has access to all features. No credit card is required. At the end of the trial, choose the edition that fits your needs.
- **I'm working on a personal project** creates an organization on the Free edition. Its name defaults to one derived from your username, and you can change it before you continue. Note that you can own only one Free organization at a time.

A Free organization supports one member, needs no payment method, and does not expire. To work with other people, upgrade it to a paid edition from the organization's billing settings, or [create another organization](/docs/administration/concepts/organizations/#creating-an-organization), which starts a free trial for a paid edition. See [pricing](/pricing/) for what each edition includes.

{{% notes type="info" %}}
Users provisioned and managed by an organization — through [SCIM](/docs/administration/guides/scim/) or a [SAML identity provider](/docs/administration/guides/saml/) — do not go through signup and do not create an organization of their own. Their account exists only within the organizations that manage it.
{{% /notes %}}

## How accounts are created

An account comes into existence in one of several ways:

- **Someone signs up.** A person creates their own account at [app.pulumi.com](https://app.pulumi.com/signup) using any of the identities listed under [Signing in](#signing-in). This is the common case, and it is the path that ends with creating your first organization.
- **An organization invites them.** An organization admin [invites a member](/docs/administration/concepts/organizations/#inviting-members-to-an-organization) by email address or invite link. The invitee still completes signup themselves; the invitation grants membership once they do.
- **A SAML identity provider provisions them.** When an organization is backed by SAML SSO, a user who signs in through the identity provider for the first time gets an account created for them. Your organization admin configures this, not you.
- **SCIM provisions them.** An organization on the Enterprise edition can [sync users and groups from its identity provider](/docs/administration/guides/scim/). SCIM creates accounts ahead of first login and deactivates them when the user is removed upstream.
- **An AI agent creates one.** The Pulumi CLI can provision an ephemeral [agent account](/docs/administration/concepts/agent-accounts/) when it detects it is running in an agent context with no credentials. A person claims it later to take ownership.

## Account identity

Two attributes identify your account:

- **Username.** Your username is unique across Pulumi Cloud. Pulumi derives it when your account is created — from your handle at the identity provider you signed up with, or from your email address if you signed up with one — and adjusts it if that name is already taken. You do not pick it during signup, but you can [rename your account](#renaming-your-account) afterwards.
- **Email address.** Your email address is how Pulumi reaches you and how organization admins invite you. Your display name, avatar, and email address are taken from the identity provider you signed up with.

Your username and email are separate from the identities you use to sign in. Adding a GitHub identity to your account does not change your Pulumi username.

{{% notes type="info" %}}
For accounts synchronized by SCIM, `userName` is immutable once the account exists, and an identity provider that pushes a changed `userName` on an update gets an error. This is a SCIM-specific rule and is distinct from renaming your own account in the console. See [Usernames cannot change](/docs/administration/concepts/scim/#usernames-cannot-change).
{{% /notes %}}

## Renaming your account

You can rename your account from your account settings in [Pulumi Cloud](https://app.pulumi.com/signin). Renaming your account changes your username only. Organizations have their own names, so no organization or stack is renamed, even an organization whose name was derived from your username.

Renaming is unavailable to users whose accounts are managed by a SAML identity provider — their name comes from the identity provider, so change it there.

## Signing in

You can sign in to Pulumi Cloud with any of the following:

- GitHub
- GitLab
- Google
- Atlassian
- An email address and password
- Single sign-on through a SAML 2.0 identity provider
- A [passkey](#signing-in-with-a-passkey) registered on your device

SAML single sign-on is configured by an organization admin, not by individual users. If your company uses it, your admin sets up the [SAML integration](/docs/administration/guides/saml/) and tells you which organization name to sign in with. Note that Pulumi supports only one Pulumi Cloud organization per SCIM application, so an admin managing several organizations configures each one separately.

### Adding new identities {#adding-new-identities}

You can associate your Pulumi account with more than one identity. In addition to the one you signed up with, you can connect GitHub, GitLab, Google, Atlassian, and SAML SSO identities, and disconnect them again later.

Connecting an additional identity is what lets you join organizations backed by that system. To be invited to an organization, your account must be linked to the organization's backing [identity provider](/docs/administration/concepts/identity-providers/) — only then do you appear in the list of users an organization admin can invite. Connecting the identity doesn't add you to those organizations by itself; an organization admin still has to invite or add you. See [Backing membership doesn't grant Pulumi membership](/docs/administration/concepts/organizations/#backing-membership).

To connect an identity:

1. Select your account avatar in the top right corner.
1. Navigate to **Account settings**.
1. Under the identity providers section, select the provider you want to connect and complete its sign-in flow.

{{% notes type="info" %}}
If you already have an account and try to sign in to a SAML-backed organization directly, you may hit an "Email already in use" error that the sign-in screen cannot resolve. Connect the organization's SAML SSO identity to your existing account instead — see [Connect SAML SSO to an existing account](/docs/administration/guides/saml/#connect-saml-sso-to-an-existing-account).
{{% /notes %}}

#### If the identity options aren't there {#identity-options-missing}

The controls for connecting identities aren't available to every account. Two things remove them:

- **Your account is organization-managed.** An account that an organization created through SAML or SCIM can't connect additional identity providers. See [Organization-managed users](/docs/administration/concepts/org-managed-users/).
- **The provider isn't configured for your deployment.** In [self-hosted Pulumi Cloud](/docs/administration/self-hosting/), a provider only appears if the deployment has been configured with OAuth credentials for it. Ask whoever administers your deployment.

## Verifying your email address

Several operations require a verified email address. Until yours is verified, Pulumi Cloud refuses to let you:

- Enroll in multi-factor authentication
- Connect an additional identity to your account
- Invite members to an organization
- Create organization access tokens
- Configure [OIDC issuers](/docs/administration/guides/oidc-issuers/)
- Run [Pulumi Deployments](/docs/deployments/) or change deployment settings
- Create agent pools, or run Neo agent tasks and automations

If you have not received the verification email, or the link has gone stale, you can send another:

1. Select your account avatar in the top right corner.
1. Navigate to **Account settings**.
1. Under your email address, select the option to resend the verification email.

## Managing your profile

To edit your profile information:

1. Select your account avatar in the top right corner.
1. Navigate to **Account settings**.
1. Select **Edit profile**.
1. Save your changes.

### Resetting your password

If you signed up with an email address, you can change your password:

1. Select your account avatar in the top right corner.
1. Navigate to **Password reset**.
1. Enter a new password.

Your password must be between 10 and 160 characters, and it cannot be the same as your username or your email address.

### Setting up MFA

If you signed up with an email address, you can protect your account with multi-factor authentication using time-based one-time passwords (TOTP). MFA enrollment requires confirming your password, so it is available only to accounts that have one — if you sign in exclusively through GitHub, GitLab, Google, Atlassian, or SAML SSO, enforce multi-factor authentication with that provider instead.

To enroll:

1. Select your account avatar in the top right corner.
1. Navigate to **Account settings**.
1. Scroll to the MFA section and select **Enroll**.
1. Scan the QR code with a TOTP authenticator app, or copy the authentication key into it if you cannot scan.
1. Enter the one-time password your app generates to confirm the enrollment.
1. Store the recovery key somewhere safe. It is your backup if you lose access to your authenticator app.

Your recovery key works once. After you use it to sign in, Pulumi issues a new one, so store the replacement as well.

{{% notes type="info" %}}
To disable multi-factor authentication, select **Reset authentication method** in the MFA section of your account settings.
{{% /notes %}}

### Signing in with a passkey

A passkey is a public-key credential that lets you sign in with Touch ID, Face ID, Windows Hello, or a hardware security key instead of typing a password. The private key stays on your device or in your password manager, and Pulumi Cloud stores only the public half. Passkeys are built on the [WebAuthn](https://www.w3.org/TR/webauthn-3/) standard, which current versions of every major browser and operating system support.

Passkeys are available in every Pulumi Cloud edition at no additional cost.

To register one:

1. Select your account avatar in the top right corner.
1. Navigate to **Account settings**.
1. In the Passkeys section, select **Register a passkey**.
1. Complete your device's prompt: Touch ID, Face ID, Windows Hello, or your hardware key.

Pulumi Cloud names the passkey after the authenticator it recognizes, such as "Windows Hello" or "Chrome on Mac". Select **Rename** to give it a name of your own, or **Remove** to delete it. Removal takes effect immediately, and a deleted passkey can no longer sign you in. It does not end sessions that are already signed in, so sign out of those separately if you have lost the device.

You can register as many passkeys as you want. One per device is common, as is one synced credential plus a hardware key as a backup.

To use one, select the passkey option on the sign-in page. If your browser supports passkey autofill, the email field also offers your registered passkeys as suggestions.

Registering a passkey does not disable any other way of signing in. Your password, if you have one, keeps working, so losing every registered passkey does not lock you out of your account.

An [organization-managed user](/docs/administration/concepts/org-managed-users/) can't register a passkey, because single sign-on through the managing organization is the account's only authentication method. Migrating an account to organization-managed revokes every passkey registered on it, and a passkey registered before the migration can no longer sign you in. The organization's [SAML admin](/docs/administration/guides/saml/saml-admin/) is the exception: they keep an alternative authentication method while they hold the role, so they can register a new passkey after the migration.

{{% notes type="info" %}}
A passkey sign-in does not prompt for a one-time password, even when you have [MFA](#setting-up-mfa) enrolled. Pulumi Cloud requires user verification, a biometric or a PIN, on every passkey ceremony, so the passkey already proves both possession of the device and the factor that unlocks it. Signing in with your password still prompts for your second factor.
{{% /notes %}}

In [self-hosted Pulumi Cloud](/docs/administration/self-hosting/), the Passkeys section appears only if an administrator has set `PULUMI_PASSKEY_CEREMONY_KEY` on the API service to a base64-encoded 32-byte random value.

## Deleting your account

You can delete your account from your [account settings](https://app.pulumi.com/user/account/settings) in Pulumi Cloud. To get there, select your user profile, then **Settings**, in the left navigation bar.

Scroll to the bottom of the account settings page to find the **Delete account** button.

Deleting your account removes your access to every organization you belong to. **This is a permanent operation and cannot be undone.**

### Before you delete your account

Pulumi Cloud deletes your account only when you are not the only admin of any organization, including a Free organization you own. If you are the only admin of one or more organizations, Pulumi Cloud doesn't delete your account and lists the organizations involved. For each one, do one of the following, then try again:

- [Make another member an admin](/docs/administration/concepts/organizations/#organization-roles) of the organization. A Free organization supports only one member, so this option isn't available for it.
- [Delete the organization](/docs/administration/concepts/organizations/#deleting-an-organization). You need to cancel its subscription first.

If you sign in with an email address and password, Pulumi Cloud also asks for your password before it deletes your account.

### What happens when you delete your account

- You are removed from every organization you belong to, along with your team memberships and stack permissions.
- Your access tokens are revoked.
- Stacks you created stay in their organizations.
- Deleting your account does not delete any cloud resources you provisioned.

## See also

- [Organizations](/docs/administration/concepts/organizations/)
- [Agent accounts](/docs/administration/concepts/agent-accounts/)
- [Access tokens](/docs/administration/concepts/access-tokens/)
- [SAML SSO](/docs/administration/guides/saml/)
- [SCIM](/docs/administration/guides/scim/)
