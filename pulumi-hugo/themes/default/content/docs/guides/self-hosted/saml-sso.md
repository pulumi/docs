---
title: Enabling SAML SSO
menu:
    userguides:
        parent: self_hosted
        identifier: self_hosted_sso
        weight: 60
meta_desc: Learn how to make the self-hosted Pulumi ready for SAML SSO with any IdP. Self-hosting is available as part of the Enterprise Edition.
---

The self-hosted option allows you to control various aspects of the Pulumi Service including how users will sign in to the [Pulumi Service]({{< relref "components/console" >}}).

## Creating The Keys

Before you can use SAML SSO to logon to the Console, you will need to ensure that the [API service]({{< relref "components/api" >}}) has a pair of keys that will be used to sign
and validate requests/responses, regardless of the IdP you choose to use.

The credentials are simply a public/private key pair that are supplied as environment variables to the API service.
In the following snippets, we show you how you can generate a key pair by using `openssl`.
The snippet shows the command for a self-hosted API service that is accessible via `api.company.com`.
Be sure to adjust the value accordingly.

> OpenSSL's official [wiki](https://wiki.openssl.org/index.php/Binaries) site contains links to pre-built binaries.

```
# Generate a new 2048-bit RSA key with a validity of 365 days.
openssl \
  req -x509 -newkey rsa:2048 \
  -days 365 -nodes -subj "/CN=api.company.com" \
  -keyout cert.key \
  -out cert.cert
```

If you also want to additionally specify an SAN (Subject Alternative Name) for your public cert, you can do so by passing the `-addext` flag as shown below.

> For this to work, though, you'll need to install _at least_ version 1.1. Once installed ensure that the 1.1 version is on your path when you run the command.
> Otherwise `-addext` will not be recognized as a valid flag.

```
openssl \
  req -x509 -newkey rsa:2048 \
  -days 365 -nodes -subj "/CN=api.company.com" \
  -keyout cert.key \
  -addext "subjectAltName=DNS:anotherdomain.company.com" \
  -out cert.cert
```

## Configure The API Service

Once the key pair has been generated, set the value of the following environment variables for the API service:

`SAML_CERTIFICATE_PUBLIC_KEY` should be set to the value of the `cert.cert` file, i.e. the public key file.
`SAML_CERTIFICATE_PRIVATE_KEY` should be set to the value of the `cert.key` file, i.e. the private key file.

For these values to take effect, you will need to restart the API Service.

> Restart the service only during a planned maintenance window.

## Enabling SAML SSO as an identity option

By default, the SAML SSO signin/signup option is not displayed to end users of the Console service.
To enable this, set the `SAML_SSO_ENABLED` environment variable for the [console]({{< relref "components/console" >}}) container to `true`
and restart the service.
