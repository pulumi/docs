---
title_tag: Troubleshooting SAML SSO | SAML SSO
meta_desc: Troubleshooting guide for SAML SSO configuration issues in Pulumi Cloud.
title: Troubleshooting
h1: SAML SSO troubleshooting
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  administration:
    name: Troubleshooting
    parent: administration-access-identity-saml
    weight: 80
    identifier: pulumi-cloud-access-management-saml-troubleshooting
---

## Locked out of your organization

If you are locked out of your Pulumi organization due to a SAML configuration error or an expired certificate, a [SAML admin](/docs/administration/access-identity/saml/saml-admin/) can log in using an alternative login method to resolve the issue. If your organization does not have a SAML admin configured, [contact support](https://support.pulumi.com/).

## Validation error while trying to save an IdP-provided metadata XML in Pulumi Cloud

Pulumi Cloud typically shows you the reason for the failure. The IdP-provided metadata XML
contains several XML elements, of which the `<IDPSSODescriptor>` is the element of concern to Pulumi. In the `IDPSSODescriptor`, we expect to see a valid `KeyDescriptor` public key certificate, a `NameIDFormat`, an entity ID identifying your organization in the IdP, and an SSO binding.

The failure is typically due to one of the following reasons:

- Malformed XML
- KeyDescriptor public key certificate in the IDPSSODescriptor has expired
- KeyDescriptor public key certificate is missing in the IDPSSODescriptor
- NameIDFormat does not have the expected value or is completely missing. See the next troubleshooting topic for help on this.

{{% notes type="info" %}}
OneLogin has a suite of free [SAML-related tools](https://www.samltool.com/prettyprint.php).
{{% /notes %}}

## Name ID format is invalid

As mentioned in the [Name ID Format](/docs/administration/access-identity/saml/sso/#name-id-format) section, Pulumi expects specific values in your IdP metadata XML.
Use [OneLogin's XML Pretty Print](https://www.samltool.com/prettyprint.php) to pretty print your XML and look for `<NameIDFormat>` under the `<IDPSSODescriptor>` XML element.

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

If your IdP does not support an emailAddress name ID format identifier but supports the `persistent` format identifier, then you may use the following:

`<NameIDFormat>urn:oasis:names:tc:SAML:2.0:nameid-format:persistent</NameIDFormat>`

## SSO binding not found in XML

This error occurs when the metadata XML you are trying to save does not have any `<SingleSignOnService>` elements under the `<IDPSSODescriptor>`. The `<SingleSignOnService>` is used by Pulumi Cloud to determine the authentication mechanism supported by the IdP. Learn more about [SAML 2.0 bindings from Wikipedia](https://en.wikipedia.org/wiki/SAML_2.0#SAML_2.0_Bindings). You must contact your IdP support or your system admin to fix the metadata XML.

Here's an example of an SSO binding for `HTTP-POST`:

```xml
<md:SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="..."/>
```

{{% notes type="info" %}}
The `Location` attribute is unique to each tenant in your IdP.
{{% /notes %}}
