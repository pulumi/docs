---
title: "Pulumi Cloud Now Supports Google Sign-In"
date: 2026-03-06
draft: false
meta_desc: "Pulumi Cloud now supports Google as an identity provider, letting you sign in, sign up, and link your Google account alongside GitHub, GitLab, and Bitbucket."
meta_image: meta.png
authors:
  - pablo-seibelt
  - casey-huang
tags:
  - features
  - security
  - authentication
  - pulumi-cloud
social:
  twitter:
  linkedin:
---

Many developers and platform engineers already use Google accounts daily for email, cloud console access, and collaboration. Until now, signing in to Pulumi Cloud required a [GitHub](https://github.com/), [GitLab](https://gitlab.com/), or [Bitbucket](https://bitbucket.org/) account, or an email/password combination. Today, we're adding Google as a first-class identity provider, so you can sign in to Pulumi Cloud with the same Google account you already use for everything else.

<!--more-->

## Why Google sign-in

Adding Google as an identity provider brings several benefits:

- **Use the account you already have.** If your team lives in [Google Workspace](https://workspace.google.com/), you can sign in to Pulumi Cloud without creating yet another set of credentials.
- **Faster onboarding.** New users can sign up with a single click using their existing Google account, reducing friction when joining an organization.
- **Fewer passwords to manage.** Leverage Google's built-in security features like two-factor authentication instead of maintaining a separate password.
- **Consistent with modern tooling.** Google sign-in is a standard offering across developer platforms, and Pulumi Cloud now meets that expectation.

## How it works

### Signing up or signing in

On the Pulumi Cloud sign-in page, you'll see a new **Sign in with Google** button alongside the existing GitHub, GitLab, and Bitbucket options. Select it, authenticate with your Google account, and you're in.

If you're a new user, Pulumi Cloud will create an account for you automatically using your Google profile information.

![Pulumi Cloud sign-in page showing Google as an identity provider option](sign-in.png)

### Connecting Google to an existing account

If you already have a Pulumi Cloud account, you can link your Google identity from your account settings:

1. Navigate to your [Account Settings](https://app.pulumi.com/account/settings).
1. Scroll to the **Connected identities** section.
1. Select **Connect** next to Google.

Once connected, you can use Google as an alternative way to sign in to your existing account.

![Account settings showing connected identities including Google](connected-identities.png)

### Google sign-in vs. SAML SSO

Google sign-in lets you authenticate to Pulumi Cloud with your individual Google account. It does not allow Google to back a Pulumi organization the way GitHub, GitLab, or Bitbucket can.

If your organization uses Google Workspace and needs centralized membership governance, configure [SAML SSO with Google Workspace](/docs/administration/access-identity/saml/gsuite/) instead. SAML SSO is available on Pulumi Enterprise and Business Critical editions.

## Get started

Google sign-in is available now for all Pulumi Cloud users:

- **New users**: [Sign up with Google](https://app.pulumi.com/signup) on the Pulumi Cloud sign-up page.
- **Existing users**: [Connect your Google account](https://app.pulumi.com/account/settings) in your account settings.

For more details, see the [Pulumi Cloud accounts documentation](/docs/administration/organizations-teams/accounts/).

We'd love to hear your feedback. Join the conversation in the [Pulumi Community Slack](https://slack.pulumi.com) or open an issue on [GitHub](https://github.com/pulumi/pulumi-cloud-requests/issues/new/choose).
