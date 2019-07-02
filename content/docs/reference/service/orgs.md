---
title: Organizations
menu:
  reference:
    parent: teams
    weight: 1
---

There are several editions of the Pulumi Cloud Console available, each offering an expanding set
of features and capabilities.

When you sign into the Pulumi Cloud Console, the organization created for your user account is
automatically enrolled in the Pulumi Community edition. To learn more about other editions of
the Pulumi Cloud Console, see [https://pulumi.com](https://www.pulumi.com/pricing/).

## Adding an Organization

Adding a new Pulumi organization can be done directly from the Pulumi Cloud Console.

<a class="btn" href="https://app.pulumi.com/site/organizations/add" target="_blank">
    ADD ORGANIZATION
</a>

## Imported Organizations

Organizations using Pulumi Team or Enterprise editions may be backed by an external service.
This enables you to manage user access and team permissions by using your existing access controls.

Here's a table that shows you the mapping between the supported 3rd-party services and Pulumi.

| Pulumi | Bitbucket | GitHub | GitLab |
|--------|--------|--------|--------|
| Organization | Team | Organization | Group |

[This](https://about.gitlab.com/2017/09/11/comparing-confusing-terms-in-github-bitbucket-and-gitlab/) post from GitLab explains the similarities and the subtle differences
between each of those cloud source-control providers.

You can learn more about each of the external services using these links:

- [Bitbucket Teams](https://confluence.atlassian.com/bitbucket/teams-321853005.html)
- [GitHub Organizations](https://github.com/collab-uniba/socialcde4eclipse/wiki/How-to-setup-a-GitHub-organization,-project-and-team)
- [GitLab Groups](https://docs.gitlab.com/ce/user/group/)

### GitHub-backed Organizations

To add a GitHub-backed organization to Pulumi, an administrator of the GitHub organization must
first grant the _Pulumi Cloud_ OAuth app the `read:org` scope. This can be done on GitHub by
visiting:
[https://github.com/settings/connections/applications/7cf9078f3c92b17a5f0f](https://github.com/settings/connections/applications/7cf9078f3c92b17a5f0f)

Pulumi requires this scope in order to verify memberships within the GitHub organization. Pulumi
will not have access to any of the organizations source repositories.

### GitLab-backed Organizations

To add a GitLab-backed organization to Pulumi, an administrator of the GitLab group
may add the group to Pulumi, and invite its members to join Pulumi.

GitLab allows group admins to add members with a temporary membership, i.e., with an expiration value. In order to invite
those members to Pulumi, their membership in the GitLab group must still be active.

## SAML 2.0 based Organizations

The Pulumi Enterprise edition provides more options for identity and access, including support for
any SAML 2.0 based identity provider.

We officially support and internally test the following providers:

- [Azure Active Directory]({{< relref "saml-aad.md" >}})
- [G Suite]({{< relref "saml-gsuite.md" >}})
- [Okta]({{< relref "saml-okta.md" >}})

> If you need help configuring or would like us to officially support another SAML identity provider,
> please [contact us](https://www.pulumi.com/about/#contact-us).
