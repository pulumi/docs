---
title: Organizations
redirect_from: "/reference/service/editions.html"
---

There are several editions of the Pulumi Cloud Console available, each offering an expanding set
of features and capabilities.

When you sign into the Pulumi Cloud Console, the organization created for your user account is
automatically enrolled in the Pulumi Community edition. To learn more about other editions of
the Pulumi Cloud Console, see [https://pulumi.com](https://www.pulumi.com/pricing/).

## Adding an Organization

Adding a new Pulumi organization can be done directly from the Pulumi Cloud Console.

<a href="https://app.pulumi.com/site/organizations/add" target="_blank">
    <button class="button">ADD ORGANIZATION</button>
</a>

## Imported Organizations

Organizations using the Pulumi Team and Enterprise editions may be backed by an external service,
such as GitHub or GitLab. This enables you to manage user access and team permissions by using
your existing access controls.

Here's a table that shows you the mapping between the supported 3rd-party services and Pulumi.

<style>
table {
    margin-bottom: 20px;
}

td, th {
    padding: 8px 8px;
    text-align: center;
    border: 1px solid rgba(0,0,0,0.13);
}

thead tr th {
    color: #00acf2;  /* $primary2, blue */
    font-weight: 800;
}

thead tr th:first-child {
    text-align: left;
}

tbody tr td {
    width: 30px;
}

tbody tr td:first-child {
    text-align: left;
}
</style>

| Pulumi | GitHub | GitLab |
|--------|--------|--------|
| Organization | Organization | Group |

[This](https://about.gitlab.com/2017/09/11/comparing-confusing-terms-in-github-bitbucket-and-gitlab/) post from GitLab explains the similarities between the popular
cloud source-control providers.

### GitHub-backed Organizations
> Learn more about setting up GitHub Organizations [here](https://github.com/collab-uniba/socialcde4eclipse/wiki/How-to-setup-a-GitHub-organization,-project-and-team).

To add a GitHub-backed organization to Pulumi, an administrator of the GitHub organization must
first grant the _Pulumi Cloud_ OAuth app the `read:org` scope. This can be done on GitHub by
visiting:
[https://github.com/settings/connections/applications/7cf9078f3c92b17a5f0f](https://github.com/settings/connections/applications/7cf9078f3c92b17a5f0f)

Pulumi requires this scope in order to verify memberships within the GitHub organization. Pulumi
will not have access to any of the organizations source repositories.

### GitLab-backed Organizations
> Learn more about GitLab Groups [here](https://docs.gitlab.com/ce/user/group/).

To add a GitLab-backed organization to Pulumi, an administrator of the GitLab group
may add the group to Pulumi, and invite its members to join Pulumi.

GitLab allows group admins to add members with a temporary membership, i.e., with an expiration value. In order to invite
those members to Pulumi, their membership in the GitLab group must still be active.

## SAML 2.0 based Organizations

The Pulumi Enterprise edition provides more options for identity and access, including support for
any SAML 2.0 based identity provider. For example Azure Active Directory (Azure AD), Active Directory
Federation Services (AD FS), Okta, and others.

To create a Pulumi organization using SAML SSO, please [contact us](https://www.pulumi.com/about/#contact-us).
