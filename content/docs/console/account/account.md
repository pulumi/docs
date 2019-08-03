---
title: Pulumi Account

menu:
    console:
        parent: account
        weight: 2
---

Your Pulumi account is how you authenticate with the Pulumi Cloud Console, and
are granted access to stacks.

## Profile

Your Pulumi user account has a profile, which is used to identify you across the Pulumi Cloud Console.
This user account has a display name, avatar URL, and email address. All of which you can edit under
[account's profile page](https://app.pulumi.com/chrsmith/settings/profile).

<img class="shadow-2xl lg:max-w-xl" src="/images/docs/reference/service/user-profile-page.png" alt="Pulumi GitHub App">

## Adding New Identities{#adding-new-identities}

Your Pulumi account can be associated with an additional identity, such as a [GitHub](https://github.com) or
[GitLab](https://gitlab.com) account. Connecting these additional identities will enable you to join organizations
that are based on those systems. (Pulumi cannot verify you are a member of a GitHub organization without confirming
you are a GitHub member!)

## Stacks

Your Pulumi account is also linked to a [Pulumi organization]({{< relref "organizations" >}}) with the same name.
So you can manage stacks, updates, and resource history.
