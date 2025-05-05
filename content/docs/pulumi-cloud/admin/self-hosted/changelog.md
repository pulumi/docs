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
---

{{% notes type="info" %}}
Self-hosting is only available with **Pulumi Business Critical**. If you would like to evaluate the self-hosted Pulumi Cloud, sign up for the [30-day trial](/product/self-hosted#self-hosted-trial) or [contact us](/contact/).
{{% /notes %}}

## 2025

### March

* [Enhanced GitLab integration support](https://www.pulumi.com/blog/gitlab-better-than-ever/)
* Updated pulumi-self-hosted-installers with latest improvements
* Security: Run containers with read-only filesystems
* Added support for de-privileged user for migrations

### February

* [Added AWS IAM credentials rotator functionality for Pulumi ESC](https://www.pulumi.com/blog/esc-rotated-secrets-launch/)
* Security improvements for webhook delivery and validation
* Fixed environment reference handling in stack operations

### January

* Fixed ESC YAML editor validation and preview issues
* Improved OAuth token refresh handling

## 2024

### December

* [Added environment imports discovery with "Imported By" tab](https://www.pulumi.com/blog/esc-imports-discoverability/)
* [Added AWS Systems Manager Parameter Store support for Pulumi ESC](https://www.pulumi.com/blog/pulumi-esc-aws-parameter-store-support/)
* Added HTTPS enforcement for GitHub app in self-hosted environments

### November

* Added support for self-hosted Insights scans
* Fixed policy evaluator for more reliable policy enforcement
* Upgraded pulumi-self-hosted-installers

### October

* [Released redesigned Stacks page with improved performance](https://www.pulumi.com/blog/new-stacks-page-launch/)
* [Added enhanced Resources page with advanced search and filtering](https://www.pulumi.com/blog/insights-resources-v2/)
* Fixed deployment settings migration errors
* Upgraded AWS packages for infrastructure security
* Fixed OIDC and SAML authentication issues

### September

* [General Availability of Pulumi ESC with webhooks, projects, and environment tags](https://www.pulumi.com/blog/pulumi-esc-ga/)
* Added required scopes for Okta integration

### August

* [Added centralized Policy Violations page](https://www.pulumi.com/blog/centralized-policy-violations/)
* Added Kubernetes-native option for Customer-Managed Agents
* Improved performance for Resource Search API queries
* Enhanced logging for OIDC authentication workflows
* Fixed database migration issues for new installations
* Security improvements for token validation and verification

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
