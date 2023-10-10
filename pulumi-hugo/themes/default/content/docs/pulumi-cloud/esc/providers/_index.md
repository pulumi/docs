---
title_tag: Pulumi ESC Providers
meta_desc: This page provides an overview of the various Pulumi ESC providers.
title: Providers
h1: Pulumi ESC Providers
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    pulumicloud:
        parent: esc
        identifier: esc-providers
---

Pulumi ESC Providers enable you to dynamically import Secrets and Configuration from the provider into your Environment.

To learn more about how to set up and use the various providers, please refer to the following guides:

* [AWS](/docs/pulumi-cloud/esc/providers/aws/)
* [Azure](/docs/pulumi-cloud/esc/providers/azure/)
* [GCP](/docs/pulumi-cloud/esc/providers/gcp/)

## Setting up OIDC

Pulumi ESC supports OpenID Connect (OIDC) integration with cloud providers. OIDC enables your Environments to exchange a signed, short-lived token issued by the Pulumi Cloud for short-term credentials from your cloud provider. This can eliminate the need for hardcoded cloud provider credentials.

The token contains the standard audience, issuer, and subject claims:

| Claim | Description                                                                                                                                                                                                                                                                                       |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `aud` | _(Audience)_ The name of the organization associated with the environment.                                                                                                                                                                                                                        |
| `iss` | _(Issuer)_ The issuer of the OIDC token: `https://api.pulumi.com/oidc`.                                                                                                                                                                                                                           |
| `sub` | _(Subject)_ The subject of the OIDC token. Because this value is often used for configuring trust relationships, the subject claim contains information about the associated Environment. The value is composed as follows: `pulumi:environments:org:<organization name>:env:<environment name>`. |

### Configuring trust relationships

As part of the process that exchanges your Environment's OIDC token for cloud provider credentials, the cloud provider must check the OIDC token's claims against the conditions configured in the provider's trust relationship. The configuration of a trust relationship varies depending on the cloud provider, but typically uses at least the Audience, Subject, and Issuer claims. These claims can be used to restrict trust to specific organizations:

* The Issuer claim is typically used to validate that the token is properly signed. The issuer's public signing key is fetched and used to validate the token's signature.
* The Audience claim contains the name of the organization associated with the Environment. You can use this claim to restrict credentials to a specific organization or organizations.
* The Subject claim contains a variety of information. You can use this claim to restrict credentials to a specific organization or Environment.

The Subject claims are particularly useful for configuring trust relationships, as they allow you to set very fine-grained conditions for credentials.

For information on how to configure OIDC for the individual cloud providers, please refer to one of the guides above.
