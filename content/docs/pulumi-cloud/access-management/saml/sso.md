---
title_tag: Configuring SAML | SAML SSO
meta_desc:
  This page provides a walkthrough important aspects of configuring any SAML
  (Security Assertion Markup Language) 2.0 identity provider.
title: Using SAML
h1: "SAML: Terminology & concepts"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: Using SAML
    parent: pulumi-cloud-access-management-saml
    weight: 1
    identifier: pulumi-cloud-access-management-saml-sso
aliases:
- /docs/intro/pulumi-cloud/accounts/saml/
- /docs/guides/saml/sso/
---

This document walks through the important aspects of configuring any SAML (Security Assertion Markup Language) 2.0 identity provider to work
with the [Pulumi Cloud](/docs/pulumi-cloud/).

> For a specific example, refer to one of our integration guides:
>
> - [Microsoft Entra ID](/docs/pulumi-cloud/access-management/saml/entra/)
> - [Google Workspace](/docs/pulumi-cloud/access-management/saml/gsuite/)
> - [Okta](/docs/pulumi-cloud/access-management/saml/okta/)
> - [Auth0](/docs/pulumi-cloud/access-management/saml/auth0/)
> - [OneLogin](/docs/pulumi-cloud/access-management/saml/onelogin/)

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

**Note**: The IdP also has an entity ID. However, the IdP's entity ID is used to uniquely identify the specific tenant/organization within that IdP. When you are configuring the SAML SSO, you are almost always asked to enter the SP entity ID, which will be specific to your organization in Pulumi.

### (Default) Relay State

The relay state is a URL, which itself is passed as a query parameter in SSO requests initiated by the identity provider. This is an optional property. This is also known as **deep-linking**. This allows a user to directly navigate to a downstream service by launching the application from the identity provider itself.

### Name ID Format

<span class="badge badge-required">required</span>

The name ID format is one of the most important aspects of your SAML SSO configuration. It defines how an identity provider identifies a user on the downstream service. The value of the format defines what value would be used for the user's `Subject`.

> **Note:** Pulumi only accepts stable and persistent identifiers for users. Identity providers must be able to set either a persistent randomly unique identifier (`urn:oasis:names:tc:SAML:2.0:nameid-format:persistent`) or the user's email address (`urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress`) as the user's `Subject` value.
> <br /> > **Important:** Once your name ID format is configured and your users have started to use SSO, **DO NOT** change the name identifier. That will prevent your users from being able to sign in.

## Session Lifetime

Most identity providers support configuring the lifetime of the SAML session by passing the optional `SessionNotOnAfter` attribute in the `AuthnStatement` element in the SAML assertion. Refer to your identity provider for guidance on how to set this attribute.

Example of the `AuthnStatement` element with session lifetime configured:

```xml
<saml:AuthnStatement AuthnInstant="2023-05-23T00:49:39Z" SessionNotOnOrAfter="2023-05-23T10:49:39Z" SessionIndex="...">
```

If `SessionNotOnAfter` isn't specified, then the Pulumi Cloud will use the default session lifetime of 12 hours.

## SAML Admin

A SAML admin can log in to your Pulumi organization using an alternative login method. This ensures someone can always log in to your organization to help resolve errors with the SAML configuration.

Whoever configures SAML for your organization is automatically made the SAML admin. To change the SAML admin:

1. Navigate to **Settings** > **Access Management**.
1. In the **SAML SSO** section, select the **SAML Admin** button.
1. Select a new SAML admin from the list.

{{% notes type="info" %}}
Only organization admins can be SAML admins. If you want to designate a member or billing manager as the SAML admin, you will first need to change their role to admin, then make them a SAML admin.
{{% /notes %}}

{{% notes type="warning" %}}
When a user stops being a SAML admin, they will automatically lose all other login methods.
{{% /notes %}}

Only one SAML admin per organization is supported at this time.

## Troubleshooting

### Validation error while trying to save an IdP-provided metadata XML in the Pulumi Cloud

The Pulumi Cloud typically shows you the reason for the failure. The IdP-provided metadata XML
contains several XML elements, of which the `<IDPSSODescriptor>` is the element of concern to Pulumi. In the `IDPSSODescriptor`, we expect to see a valid `KeyDescriptor` public key certificate, a `NameIDFormat`, an entity ID identifying your organization in the IdP, and an SSO binding.

The failure is typically due to one of the following reasons:

- Malformed XML
- KeyDescriptor public key certificate in the IDPSSODescriptor has expired
- KeyDescriptor public key certificate is missing n the IDPSSODescriptor
- NameIDFormat does not have the expected value or is completely missing. See the next troubleshooting topic for help on this.

> **Tip:** OneLogin has a suite of free [SAML-related tools](https://www.samltool.com/prettyprint.php).

### Name ID Format is invalid

As mentioned in the `Name ID Format` section, Pulumi expects specific values in your IdP metadata XML.
Use [One Login's XML Pretty Print](https://www.samltool.com/prettyprint.php) to pretty print your XML and look for `<NameIDFormat>` under the `<IDPSSODescriptor>` XML element.

If you cannot find an element called `NameIDFormat`, add the following line immediately after the closing tag for `KeyDescriptor`:

`<NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress</NameIDFormat>`

Here's a sample metadata XML. Note that some values were removed for brevity.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<md:EntityDescriptor xmlns:md="urn:oasis:names:tc:SAML:2.0:metadata" entityID="...">
  <md:IDPSSODescriptor WantAuthnRequestsSigned="false" protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol">
    <md:KeyDescriptor use="signing">
      ....
    </md:KeyDescriptor>
    <!--
        In this example, all elements have a namespace of `md`. This is why the NameIDFormat has a prefix of `md:`.
        If the elements in your XML don't have the prefix, then you may skip that.
    -->
    <md:NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress</md:NameIDFormat>
    <md:SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="..."/>
    <md:SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect" Location="..."/>
  </md:IDPSSODescriptor>
</md:EntityDescriptor>
```

If your IdP does not support an emailAddress Name ID Format identifier but supports the `persistent` format identifier, then you may use the following:

`<NameIDFormat>urn:oasis:names:tc:SAML:2.0:nameid-format:persistent</NameIDFormat>`

### The IdP signing certificate expired and I can't login to Pulumi anymore

[Contact us](/about#contact-us) for assistance with getting the IdP metadata XML updated.

### An SSO binding was not found in the XML. Contact your SSO provider.

This error occurs when the metadata XML you are trying to save does not have any `<SingleSignOnService>` elements under the `<IDPSSODescriptor>`. The `<SingleSignOnService>` is used by the Pulumi Cloud to determine the authentication mechanism supported by the IDP. Learn more about [SAML 2.0 Bindings from Wikipedia](https://en.wikipedia.org/wiki/SAML_2.0#SAML_2.0_Bindings). You must contact your IdP support or your system admin to fix the metadata XML.

Here's an example of an SSO binding for `HTTP-POST`:

```xml
<md:SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="..."/>
```

> **Note:** The `Location` attribute is unique to each tenant in your IDP.
