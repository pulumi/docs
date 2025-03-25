---
title_tag: Changelog |
meta_desc: Changes related to the self-hosted version of Pulumi Cloud.
title: Changelog
h1: Self-Hosted Changelog
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: Changelog
    parent: pulumi-cloud-admin-self-hosted
    weight: 5
    identifier: pulumi-cloud-admin-self-hosted-changelog
aliases:
  - /docs/pulumi-cloud/self-hosted/changelog/
search:
  keywords:
    - changelog
    - cloud
    - self
    - hosted
    - related
    - changes
    - version
---

{{% notes type="info" %}}
Self-hosting is only available with **Pulumi Business Critical**. If you would like to evaluate the self-hosted Pulumi Cloud, sign up for the [30-day trial](/product/self-hosted#self-hosted-trial) or [contact us](/contact/).
{{% /notes %}}

## 2024

### July

* [Support for Self-Hosted Resource Search and Pulumi Deployments](https://www.pulumi.com/blog/self-hosted-search-and-deploy/)
* [Support for short lived access tokens](https://www.pulumi.com/blog/short-lived-access-tokens/)

### June

* [scim] Add logs when filtering invalid members
* Relax transport validations on the http client used by the oidc client on self hosted
* Honor env proxy variables for oidc metadata requests
* OIDC Trust - Add support for org tokens with admin privileges

### May

* [saml] Add email identity for new SAML admin if none exists
* Decouple GitHub app installation for self hosted
* [scim] Add more flexibility to SCIM user search filter
* [saml] Add more flexibility to saml login process
* Re-enable sign in button after failed login when username changes
* Log SCIM search users response
* Fix [saml] handle corrupted saml identities for existing users
* Rename email change request email
* Stop navbar flickering after visiting the Resources page
* Hide GH App on integrations page for self-hosted
* Fix required marker in delete org dialog

### April

* [Enable OIDC Trust Relationships](/blog/oidc-trust-relationships/)
* Enable otel metrics
* Expose metrics endpoint
* Add url query param for graph view

### March

* Enable SCIM ADD patch ops for given and family names
* Validate SAML display name
* Allow all org admins to delete existing policy groups and remove policy groups
* Do not show billing edition card on self-hosted
* Add lightweight checking of username bounds on SAML user creation
* Hide stack deployments tab on self-hosted
* [Fix Changing stack via breadcrumb menu on app.pulumi.com doesn't show updated Configuration](https://github.com/pulumi/pulumi-cloud-requests/issues/200)
* Fix configuration bug when changing stacks

### February

* Upgrade password hashing complexity
* Log requested SCIM ops when we fail on validation
* Fix overflow title in the onboarding dashboard panel

### January

* Fix: Always allow users to delete existing policies
* Fix: use stack name on provider audit logs
* Fix dropping trailing zeros from numbers in config values
