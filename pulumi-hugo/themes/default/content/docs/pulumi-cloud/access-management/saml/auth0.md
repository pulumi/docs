---
title_tag: Configuring Auth0 | SAML SSO
meta_desc: Configuring Auth0 as a SAML SSO identity provider (IDP).
title: Auth0
h1: "SAML: Configuring Auth0"
menu:
  pulumicloud:
    parent: saml
    weight: 2

aliases:
- /docs/reference/service/saml-auth0/
- /docs/console/accounts/saml/auth0/
- /docs/guides/saml/auth0/
---

This guide walks you through configuring your Auth0 Authentication Platform as a SAML SSO identity provider
(IDP) for the Pulumi Cloud.

## Prerequisites

* Your organization must already be configured to use [SAML](/docs/pulumi-cloud/access-management/saml/sso/) with Pulumi.
* You must be an admin of your Pulumi organization.
* (Optional, but highly recommended) You should have more than one admin for your Pulumi organization.

## Enabling SAML For Your Auth0 Authentication Platform

To enable SAML for your Auth0 Authentication Platform, navigate to the **Applications** section of your Auth0 dashboard. You may
need to create a new application or select an existing application. Next, we need to get the SAML metadata XML to
configure Pulumi. For this, navigate to the **Settings** tab of your application and scroll down to the **Advanced
Settings** section.

![Auth0 Application Settings](/images/docs/reference/service/saml-auth0/auth0-app-advanced-settings.png)

Expand the **Advanced Settings** section and click on the **Endpoints** tab. In the **Endpoints** tab, scroll down to
the **SAML** section. Copy the **SAML Metadata URL** link and download the metadata XML file via
the browser or a command line tool like `curl`.

![Auth0 Application Endpoints](/images/docs/reference/service/saml-auth0/auth0-app-endpoints.png)

Paste the contents of the downloaded XML file in the **Change Membership Requirements** dialog for setting up Pulumi
SAML SSO.

![Pulumi SAML SSO Configuration](/images/docs/reference/service/saml-auth0/auth0-saml-sso-config.png)

Finally, in the **Settings** tab of your application, navigate to the **Application URIs** section. In the **Application
Login URI** field, enter the URL of your Pulumi organization in following format:

```
https://api.pulumi.com/login/{orgName}/sso/saml/acs
```

where `{orgName}` is the name of your Pulumi organization. Additionally, in the **Allowed Callback URLs** field, enter
the same URL.

## Troubleshooting

Auth0 Troubleshoot SAML Configurations: [SAML app error messages](https://auth0.com/docs/troubleshoot/authentication-issues/troubleshoot-saml-configurations)

If you need additional assistance, [contact us](/about#contact-us).
