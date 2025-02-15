---
title_tag: OpenID Connect provider integration for Pulumi
meta_desc: This page provides an overview of how to configure OpenID Connect integration between
           Pulumi and supported cloud providers.
title: OpenID provider
h1: OpenID Connect provider integration
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: OpenID provider
    parent: pulumi-cloud-access-management-oidc
    weight: 3
    identifier: pulumi-cloud-access-management-oidc-provider
aliases:
- /docs/pulumi-cloud/oidc/provider/
---

Pulumi supports OpenID Connect (OIDC) integration across various services. OIDC enables secure interactions between Pulumi services and cloud providers by leveraging signed, short-lived tokens issued by the Pulumi Cloud. This mechanism enhances security by eliminating the necessity for hardcoded cloud provider credentials and facilitates the exchange of these tokens for short-term credentials from your cloud provider.

## Overview

For Pulumi services that make use of OIDC, every time that service runs, the Pulumi Cloud issues a new OIDC token specific to that run. The OIDC token is a short-lived, signed [JSON Web Token](https://jwt.io) that contains information about the service, and that can be exchanged for credentials from a cloud provider. For AWS, Azure, and Google Cloud, this credential exchange can be done automatically as part of the service setup.

## Token Claims

### Pulumi Deployments

The token contains the standard audience, issuer, and subject claims:

| Claim | Description                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `aud` | _(Audience)_ The name of the organization associated with the deployment.                                                                                                                                                                                                                                                                                                                                                     |
| `iss` | _(Issuer)_ The issuer of the OIDC token: `https://api.pulumi.com/oidc`.                                                                                                                                                                                                                                                                                                                                                       |
| `sub` | _(Subject)_ The subject of the OIDC token. Because this value is often used for configuring trust relationships, the subject claim contains information about the associated service. Each component of the subject claim is also available as a custom claim. |

### Pulumi ESC

For details on how Pulumi ESC environments interact with OIDC token claims, see [Configuring OIDC for Pulumi ESC](/docs/esc/access-management/oidc/).

## Custom claims

For some services, the token also contains custom claims that provide additional, service-specific information. You can find more details about the available custom claims below.

### Pulumi Deployments

The format of the subject claim for this service is:

`pulumi:deploy:org:<organization name>:project:<project name>:stack:<stack name>:operation:<operation kind>:scope:write`

Valid custom claims for this service are listed in the table below:

| Claim        | Description                                                                     |
|--------------|---------------------------------------------------------------------------------|
| `stackId`    | The fully-qualified identifier of the stack being deployed.                     |
| `operation`  | The deployment operation (one of `preview`, `update`, `refresh`, or `destroy`). |
| `org`        | The name of the organization associated with the deployment.                    |
| `project`    | The name of the project being deployed.                                         |
| `stack`      | The name of the stack being deployed.                                           |
| `deployment` | The deployment version.                                                         |
| `scope`      | The scope of the OIDC token. Always `write`.                                    |

### Pulumi ESC

For details on how Pulumi ESC environments interact with OIDC custom claims, see [Configuring OIDC for Pulumi ESC](/docs/esc/access-management/oidc/).

## Configuring trust relationships

As part of the process that exchanges your service's OIDC token for cloud provider credentials, the cloud provider must check the OIDC token's claims against the conditions configured in the provider's trust relationship. The configuration of a trust relationship varies depending on the cloud provider, but typically uses at least the Audience, Subject, and Issuer claims. These claims can be used to restrict trust to specific organizations, projects, stacks, environments etc:

* The Issuer claim is typically used to validate that the token is properly signed. The issuer's public signing key is fetched and used to validate the token's signature.
* The Audience claim can vary between Deployment and ESC. For deployments this claim contains the name of the organization associated with the deployment. For ESC this claim contains the name of the organization, prefixed with the provider's platform (`aws`, `azure`, `gcp`). You can use this claim to restrict credentials to a specific organization or organizations.
* The Subject claim contains a variety of information about the service. You can use this claim to restrict credentials to a specific organization/scope.
* The various custom claims contain the same information as the Subject claim. If your cloud provider supports configuring trust relationships based on custom claims, you can use these claims for the same purposes as the Subject claim.

The Subject and custom claims are particularly useful for configuring trust relationships, as they allow you to set very fine-grained conditions for credentials.

## Configuring OpenID Connect for your cloud provider

To configure OIDC for your cloud provider, refer to one of our guides:

* [Configuring OIDC for AWS](/docs/pulumi-cloud/oidc/provider/aws/)
* [Configuring OIDC for Azure](/docs/pulumi-cloud/oidc/provider/azure/)
* [Configuring OIDC for Google Cloud](/docs/pulumi-cloud/oidc/provider/gcp/)
* [Configuring OIDC for Vault](/docs/pulumi-cloud/oidc/provider/vault/)
