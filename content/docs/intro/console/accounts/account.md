---
title: Accounts

menu:
    console:
        parent: accounts
        weight: 2
---

Your Pulumi account is how you authenticate with the Pulumi Cloud Console, and
are granted access to stacks.

## Profile

Your Pulumi user account has a profile, which is used to identify you across the Pulumi Cloud Console.
The display name, avatar URL, and email address are obtained from the identity provider you use to first
sign up. (e.g. your GitHub account.)

However, you can edit your profile information later by visiting your
[account profile page](https://app.pulumi.com/chrsmith/settings/profile).

<img class="shadow-2xl lg:max-w-xl" src="/images/docs/reference/service/user-profile-page.png" alt="Pulumi GitHub App">

## Adding New Identities{#adding-new-identities}

Your Pulumi account can be associated with multiple identities, such as a [GitHub](https://github.com) or
[GitLab](https://gitlab.com) account. Connecting these additional identities will enable you to join organizations
that are based on those systems.

You are unable to become a member of a GitHub-backed Pulumi organization until you first add a GitHub identity
to your Pulumi account. (So the Pulumi Cloud Console can confirm you are a member of that backing GitHub
organization.)
