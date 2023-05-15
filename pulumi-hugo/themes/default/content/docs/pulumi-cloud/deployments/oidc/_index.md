---
title_tag: OpenID Connect Integration for Pulumi Deployments
meta_desc: This page provides an overview of how to configure OpenID Connect integration between
           Pulumi Deployments and supported cloud providers.
title: OpenID Connect
h1: OpenID Connect integration
menu:
    pulumicloud:
        identifier: deployments-oidc
        parent: deployments
        weight: 3

aliases:
- /docs/guides/oidc/
- /docs/intro/deployments/oidc/
---

[Pulumi Deployments](/docs/reference/deployments-rest-api/) supports OpenID Connect (OIDC) integration with cloud providers. OIDC enables your deployments to exchange a signed, short-lived token issued by the Pulumi Cloud for short-term credentials from your cloud provider. This can improve the security of your deployments by eliminating the need for hardcoded cloud provider credentials. If you are unfamiliar with OIDC, GitHub provides a [fine introduction to the topic](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect).

## Overview

Every time a deployment runs, the Pulumi Cloud issues a new OIDC token specific to that deployment. The OIDC token is a short-lived, signed [JSON Web Token](https://jwt.io) that contains information about the deployment and that can be exchanged for credentials from a cloud provider. For AWS, Azure, and Google Cloud, this credential exchange can be done automatically as part of deployment setup. For advanced scenarios or other cloud providers, the token is available in the `PULUMI_OIDC_TOKEN` environment variable as well as in the `/mnt/pulumi/pulumi.oidc` file.

The token contains the standard audience, issuer, and subject claims:

| Claim | Description |
| ----- | ----------- |
| `aud` | _(Audience)_ The name of the organization associated with the deployment. |
| `iss` | _(Issuer)_ The issuer of the OIDC token: `https://api.pulumi.com/oidc`. |
| `sub` | _(Subject)_ The subject of the OIDC token. Because this value is often used for configuring trust relationships, the subject claim contains information about the associated deployment. The value is composed as follows: `pulumi:deploy:org:<organization name>:project:<project name>:stack:<stack name>:operation:<operation kind>:scope:write`. Each component of the subject claim is also available as a custom claim. |

The token also contains custom claims that provide additional, deployment-specific information:

| Claim | Description |
| ----- | ----------- |
| `stackId` | The fully-qualified identifier of the stack being deployed. |
| `operation` | The deployment operation (one of `preview`, `update`, `refresh`, or `destroy`). |
| `org` | The name of the organization associated with the deployment. |
| `project` | The name of the project being deployed. |
| `stack` | The name of the stack being deployed. |
| `deployment` | The deployment version. |
| `scope` | The scope of the OIDC token. Always `write`. |

## Configuring trust relationships

As part of the process that exchanges your deployment's OIDC token for cloud provider credentials, the cloud provider must check the OIDC token's claims against the conditions configured in the provider's trust relationship. The configuration of a trust relationship varies depending on the cloud provider, but typically uses at least the Audience, Subject, and Issuer claims. These claims can be use to restrict trust to specific organizations, projects, stacks, etc.:

- The Issuer claim is typically used to validate that the token is properly signed. The issuer's public signing key is fetched and used to validate the token's signature.
- The Audience claim contains the name of the organization associated with the deployment. You can use this claim to restrict credentials to a specific organizaiton or organizations.
- The Subject claim contains a variety of information about the deployment. You can use this claim to restrict credentials to a specific organization, project, stack, operation, or scope.
- The various custom claims contain the same information as the Subject claim. If your cloud provider supports configuring trust relationships based on custom claims, you can use these claims for the same purposes as the Subject claim.

The Subject and custom claims are particularly useful for configuring trust relationships, as they allow you to set very fine-grained conditions for credentials.

## Configuring OpenID Connect for your cloud provider

To configure OIDC for your cloud provider, refer to one of our guides:

- [Configuring OIDC for AWS](/docs/guides/oidc/aws/)
- [Configuring OIDC for Azure](/docs/guides/oidc/azure/)
- [Configuring OIDC for Google Cloud](/docs/guides/oidc/gcp/)
