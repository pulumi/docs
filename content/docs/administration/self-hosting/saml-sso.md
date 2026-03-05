---
title_tag: "Enable SAML SSO for Self-hosted Environments"
meta_desc: Learn how to make the self-hosted Pulumi ready for SAML SSO with any IdP. Self-hosting is available as part of the Enterprise Edition.
title: SAML SSO
h1: SAML SSO for self-hosted Pulumi Cloud
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  administration:
        name: SAML SSO
        parent: administration-self-hosting
        weight: 3
        identifier: administration-security-compliance-self-hosted-saml-sso
aliases:
  - /docs/guides/self-hosted/saml-sso/
  - /docs/pulumi-cloud/self-hosted/saml-sso/
  - /docs/administration/self-hosting/pulumi-cloud/saml-sso/
  - /docs/pulumi-cloud/admin/self-hosted/saml-sso/
---

The self-hosted option allows you to control various aspects of Pulumi Cloud including how users will sign in to the [Pulumi Cloud console](/docs/administration/self-hosting/components/console/).

## Creating the keys

Before you can use SAML SSO to logon to the Console, you will need to ensure that the [API service](/docs/administration/self-hosting/components/api/) has a pair of keys that will be used to sign
and validate requests/responses, regardless of the IdP you choose to use.

The credentials are a public/private key pair that are supplied as environment variables to the API service.
In the following snippets, we show you how you can generate a key pair by using `openssl`.
The snippet shows the command for a self-hosted API service that is accessible via `api.company.com`.
Be sure to adjust the value accordingly.

{{% notes type="info" %}}
OpenSSL's official [wiki](https://wiki.openssl.org/index.php/Binaries) site contains links to pre-built binaries.
{{% /notes %}}

```bash
# Generate a new 2048-bit RSA key with a validity of 365 days.
openssl \
  req -x509 -newkey rsa:2048 \
  -days 365 -nodes -subj "/CN=api.company.com" \
  -keyout cert.key \
  -out cert.cert
```

If you also want to additionally specify an SAN (Subject Alternative Name) for your public cert, you can do so by passing the `-addext` flag as shown below.

{{% notes type="info" %}}
For this to work, you'll need to install _at least_ version 1.1. Once installed, ensure that the 1.1 version is on your path when you run the command. Otherwise `-addext` will not be recognized as a valid flag.
{{% /notes %}}

```bash
openssl \
  req -x509 -newkey rsa:2048 \
  -days 365 -nodes -subj "/CN=api.company.com" \
  -keyout cert.key \
  -addext "subjectAltName=DNS:anotherdomain.company.com" \
  -out cert.cert
```

## Configure the API service

Once the key pair has been generated, set the value of the following environment variables for the API service:

`SAML_CERTIFICATE_PUBLIC_KEY` should be set to the value of the `cert.cert` file, i.e. the public key file.
`SAML_CERTIFICATE_PRIVATE_KEY` should be set to the value of the `cert.key` file, i.e. the private key file.

For these values to take effect, you will need to restart the API Service.

{{% notes type="info" %}}
Restart the service only during a planned maintenance window.
{{% /notes %}}

## Enabling SAML SSO as an identity option

By default, the SAML SSO signin/signup option is not displayed to end users of the Console service.
To enable this, set the `SAML_SSO_ENABLED` environment variable for the [console](/docs/administration/self-hosting/components/console/) container to `true`
and restart the service.

## Next steps

Once your self-hosted infrastructure is configured, complete the SAML SSO setup by configuring your identity provider and Pulumi organization using the [Pulumi Cloud SAML SSO guides](/docs/administration/access-identity/saml/).
