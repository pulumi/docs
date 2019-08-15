---
title: Organizations

menu:
    console:
        parent: accounts
        weight: 3

aliases: [/docs/reference/service/orgs]
---

An organization is the primary grouping unit for stacks within the Pulumi Cloud Console.
When you sign into the Pulumi Cloud Console, an individual organization is created for you and
automatically subscribed to the Pulumi Community edition.

You can however be a member of multiple Pulumi organizations, collaborating with other developers.

## Creating a New Organization{#creating-a-new-organization}

You can create a new Pulumi organization directly from the Pulumi Cloud Console.

<a class="btn" href="https://app.pulumi.com/site/organizations/add" target="_blank">
    CREATE ORGANIZATION
</a>


## Organization Kinds{#organization-kinds}

A Pulumi organization may be linked to a 3rd-party identity provider, offering an additional layer
of security for you and your team. While membership within the Pulumi organization is managed by
an organization administrator, in order to become a member of a Pulumi organization you must also
be a member of the backing 3rd-party identity provider.

For example, if a Pulumi organization (https://app.pulumi.com/robot-co) is backed by a GitHub organization
(https://github.com/robot-co), then only members of the GitHub organization may be added as members to the
Pulumi organization. Similarly, as soon as someone loses access to the GitHub organization, they will no
longer have access to the Pulumi organization it is backing.

> See [organization roles]({{< relref "organization-roles" >}}) or
> [adding new identities]({{< relref "account#adding-new-identities" >}})
> for more information.

The following table shows the relationship between a Pulumi organization and 3rd party groupings.

| Pulumi | Bitbucket | GitHub | GitLab |
|--------|--------|--------|--------|
| Organization | [Team](https://confluence.atlassian.com/bitbucket/teams-321853005.html) | [Organization](https://github.com/collab-uniba/socialcde4eclipse/wiki/How-to-setup-a-GitHub-organization,-project-and-team) | [Group](https://docs.gitlab.com/ce/user/group/) |

In addition, a Pulumi organization may be backed by a [SAML 2.0 identity provider]({{< relref "saml" >}}), or
no identity provider at all. (In which case membership is entirely managed on the Pulumi Cloud Console.)

### GitHub-backed Organizations

To add a GitHub-backed organization to Pulumi, an administrator of the GitHub organization must
first grant the _Pulumi Cloud_ OAuth app the `read:org` scope. This can be done on GitHub by
visiting:
[https://github.com/settings/connections/applications/7cf9078f3c92b17a5f0f](https://github.com/settings/connections/applications/7cf9078f3c92b17a5f0f)

Pulumi requires the [`read:org` scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/#available-scopes)
in order to verify memberships within the GitHub organization. The Pulumi Cloud Console
will not have access to any of the organization's source code, issues, or other data.

### GitLab-backed Organizations

To add a GitLab-backed organization to Pulumi, an administrator of the GitLab group
may add the group to Pulumi, and invite its members to join Pulumi.

GitLab allows group admins to add members with a temporary membership, i.e., with an expiration value. In order to invite
those members to Pulumi, their membership in the GitLab group must still be active. As soon as their
GitLab group membership expires, those users will lose access to the GitLab-backed organization on Pulumi.

## SAML Single Sign-on (SSO)

The Pulumi Enterprise edition provides more options for identity and access, including support for
any SAML 2.0 based identity provider.

[Learn more]({{< relref "saml" >}}) about configuring a SAML-based organization on Pulumi. Or refer to one
of our guides below:

- [Azure Active Directory]({{< relref "aad" >}})
- [G Suite]({{< relref "gsuite" >}})
- [Okta]({{< relref "okta" >}})



> If you need help configuring or would like us to officially support another SAML identity provider,
> please [contact us]({{< ref "/about#contact-us" >}}).
