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

## GitHub-backed Organizations

Organizations using the Pulumi Team and Enterprise editions may be backed by a GitHub organization,
enabling you to manage user access and team permissions by using your existing GitHub access
controls.

To add a GitHub-backed organization to Pulumi, an administrator of the GitHub organization must
first grant the _Pulumi Cloud_ OAuth app the `read:org` scope. This can be done on GitHub by
visiting:
[https://github.com/settings/connections/applications/7cf9078f3c92b17a5f0f](https://github.com/settings/connections/applications/7cf9078f3c92b17a5f0f)

Pulumi requires this scope in order to verify memberships within the GitHub organization. Pulumi
will not have access to any of the organizations source repositories.

## SAML 2.0 based Organizations

The Pulumi Enterprise edition provides more options for identity and access, including support for
any SAML 2.0 based identity provider. For example Azure Active Directory (Azure AD), Active Directory
Federation Services (AD FS), Okta, and others.

To create a Pulumi organization using SAML SSO, please [contact us](https://www.pulumi.com/about/#contact-us).
