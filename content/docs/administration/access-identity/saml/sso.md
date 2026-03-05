---
title_tag: Configuring SAML | SAML SSO
meta_desc:
  This page provides a walkthrough important aspects of configuring any SAML
  (Security Assertion Markup Language) 2.0 identity provider.
title: Using SAML
h1: "SAML: Terminology & concepts"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  administration:
    name: Using SAML
    parent: administration-access-identity-saml
    weight: 10
    identifier: pulumi-cloud-access-management-saml-sso
aliases:
- /docs/intro/pulumi-cloud/accounts/saml/
- /docs/guides/saml/sso/
- /docs/pulumi-cloud/access-management/saml/sso/
---

This document walks through the important aspects of configuring any SAML (Security Assertion Markup Language) 2.0 identity provider to work
with [Pulumi Cloud](/docs/pulumi-cloud/).

{{% notes type="info" %}}
For examples of setting up SAML SSO with popular identity providers, refer to our [integration guides](/docs/administration/access-identity/saml#integration-guides).
{{% /notes %}}

## Terminology

- **IdP** stands for Identity Provider. An IdP is a service that acts as a user directory.
- **SP** stands for Service Provider. A service provider relies on an identity provider for authentication.
- **IdP Metadata XML** is the XML configuration document provided by your IdP. It contains public information about your user directory,
  which can be used by the service provider to make authentication requests.

## Configuration Properties

The following are the only properties you will really be configuring when you set up SAML SSO with your IdP.

| Name                   | Other Names                      | Required |
| ---------------------- | -------------------------------- | -------- |
| Single sign on URL     | ACS URL                          | Yes      |
| Entity ID              | Metadata _or_ Audience URL       | Yes      |
| Default relay state    | Start _or_ Application Start URL | No       |
| Name identifier format | Name Identifier, Name            | Yes      |

### Single Sign On URL

<span class="badge badge-required">required</span>

This is the URL where the IdP can `POST` SAML assertions. The URL format is always:

`https://api.pulumi.com/login/{orgName}/sso/saml/acs`

`{orgName}` in the previous URL is where your Pulumi organization's name must be entered. The org name is case-sensitive. For example, if your Pulumi login name is `ACME-corp`, you must enter the name exactly as is in the above URL as well. You can find your org's Pulumi login name from the URL when you navigate to it in the [Pulumi Cloud](https://app.pulumi.com). Using this example, the URL would be `https://app.pulumi.com/ACME-corp`.

### Entity ID

<span class="badge badge-required">required</span>

The (SP) entity ID is a URL where a service provider publishes public information about its SAML configuration. The metadata document published by the service provider shows its public certificate that can be used to verify the signature of authentication requests initiated from the service itself.

The IdP also has an entity ID. However, the IdP's entity ID is used to uniquely identify the specific tenant/organization within that IdP. When you are configuring SAML SSO, you are almost always asked to enter the SP entity ID, which will be specific to your organization in Pulumi.

### (Default) Relay State

The relay state is a URL, which itself is passed as a query parameter in SSO requests initiated by the identity provider. This is an optional property. This is also known as **deep-linking**. This allows a user to directly navigate to a downstream service by launching the application from the identity provider itself.

### Name ID Format

<span class="badge badge-required">required</span>

The name ID format is one of the most important aspects of your SAML SSO configuration. It defines how an identity provider identifies a user on the downstream service. The value of the format defines what value would be used for the user's `Subject`.

{{% notes type="info" %}}
Pulumi only accepts stable and persistent identifiers for users. Identity providers must be able to set either a persistent randomly unique identifier (`urn:oasis:names:tc:SAML:2.0:nameid-format:persistent`) or the user's email address (`urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress`) as the user's `Subject` value.

**Important:** Once your name ID format is configured and your users have started to use SSO, **DO NOT** change the name identifier. That will prevent your users from being able to sign in.
{{% /notes %}}

## Session Lifetime

Most identity providers support configuring the lifetime of the SAML session by passing the optional `SessionNotOnAfter` attribute in the `AuthnStatement` element in the SAML assertion. Refer to your identity provider for guidance on how to set this attribute.

Example of the `AuthnStatement` element with session lifetime configured:

```xml
<saml:AuthnStatement AuthnInstant="2023-05-23T00:49:39Z" SessionNotOnOrAfter="2023-05-23T10:49:39Z" SessionIndex="...">
```

If `SessionNotOnAfter` isn't specified, then Pulumi Cloud will use the default session lifetime of 12 hours.

## SAML admin

For information on the SAML admin role and how to configure it, see [SAML admin](/docs/administration/access-identity/saml/saml-admin/).

## Troubleshooting

For help resolving SAML SSO configuration issues, see [SAML SSO troubleshooting](/docs/administration/access-identity/saml/troubleshooting/).
