---
title_tag: Configuring Auth0 | SAML SSO
meta_desc: Configuring Auth0 as a SAML SSO identity provider (IDP).
title: Auth0
h1: "SAML: Configuring Auth0"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  administration:
    name: Auth0
    parent: administration-access-identity-saml
    weight: 20
    identifier: pulumi-cloud-access-management-saml-auth0
aliases:
- /docs/reference/service/saml-auth0/
- /docs/console/accounts/saml/auth0/
- /docs/guides/saml/auth0/
- /docs/pulumi-cloud/access-management/saml/auth0/
---

This guide walks you through configuring your Auth0 Authentication Platform as a [SAML SSO](/docs/administration/access-identity/saml/) identity provider
(IDP) for Pulumi Cloud.

## Enabling SAML for your Auth0 authentication platform

To enable SAML for your Auth0 Authentication Platform, navigate to the **Applications** section of your Auth0 dashboard. You may
need to create a new application or select an existing application. Next, we need to get the SAML metadata XML to
configure Pulumi. For this, navigate to the **Settings** tab of your application and scroll down to the **Advanced
Settings** section.

![Auth0 Application Settings](/images/docs/reference/service/saml-auth0/auth0-app-advanced-settings.png)

Expand the **Advanced Settings** section and click on the **Endpoints** tab. In the **Endpoints** tab, scroll down to
the **SAML** section. Copy the **SAML Metadata URL** link and download the metadata XML file via
the browser or a command line tool like `curl`.

![Auth0 Application Endpoints](/images/docs/reference/service/saml-auth0/auth0-app-endpoints.png)

Finally, in the **Settings** tab of your application, navigate to the **Application URIs** section. In the **Application
Login URI** field, enter the URL of your Pulumi organization in the following format:

```
https://api.pulumi.com/login/{orgName}/sso/saml/acs
```

where `{orgName}` is the name of your Pulumi organization. Additionally, in the **Allowed Callback URLs** field, enter
the same URL.

## Configuring your Pulumi organization

To configure Pulumi with the SAML metadata:

1. Sign in to Pulumi Cloud and navigate to your organization.
1. Select **Settings** > **Access Management**.
1. Select the **Other** tab.
1. In the **Membership Requirements** section, select **Change requirements**.
1. Select **SAML SSO** and then **Next**.
1. Paste the contents of the downloaded XML file into the text area.
1. Select **Apply changes**.

## Troubleshooting

Auth0 troubleshooting: [SAML app error messages](https://auth0.com/docs/troubleshoot/authentication-issues/troubleshoot-saml-configurations)

For additional help, see the [SAML SSO troubleshooting guide](/docs/administration/access-identity/saml/troubleshooting/) or [contact support](https://support.pulumi.com/).
