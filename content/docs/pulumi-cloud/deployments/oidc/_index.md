---
title_tag: OIDC Setup for Pulumi Deployments
meta_desc: This page provides an overview of how to configure OpenID Connect (OIDC) integration between
           Pulumi Deployments and supported cloud providers.
title: OIDC Setup
h1: OIDC Setup for Deployments
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: OIDC Setup
    parent: pulumi-cloud-deployments
    weight: 3
    identifier: pulumi-cloud-deployments-oidc
aliases:
- /docs/pulumi-cloud/oidc/provider/
- /docs/pulumi-cloud/access-management/oidc/provider/
---

{{< notes type="info" >}}
Pulumi ESC should be the preferred approach over the Deployments OIDC integrations since it's more portable and easier to set up. For ESC OIDC setup instructions, see [Configuring OIDC for Pulumi ESC](/docs/esc/environments/configuring-oidc/).
{{< /notes >}}

This page describes how to use OpenID Connect (OIDC) so that your Pulumi Deployments can obtain the necessary cloud credentials to manage resources. If you're looking for information about what permissions a deployment has within the Pulumi Cloud itself, see [Deployment Permissions](/docs/pulumi-cloud/deployments/reference/#deployment-permissions) instead.

OIDC enables secure interactions between Pulumi Deployments and cloud providers by leveraging signed, short-lived tokens issued by the Pulumi Cloud. This mechanism enhances security by eliminating the necessity for hardcoded cloud provider credentials and facilitates the exchange of these tokens for short-term credentials from your cloud provider.

## Overview

Every time a Deployment runs, the Pulumi Cloud issues a new OIDC token specific to that run. The OIDC token is a short-lived, signed [JSON Web Token](https://jwt.io) that contains information about the deployment, and that can be exchanged for credentials from a cloud provider. For AWS, Azure, and Google Cloud, this credential exchange can be done automatically as part of the service setup.

## Token Claims

The token contains the standard audience, issuer, and subject claims:

| Claim | Description                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `aud` | _(Audience)_ The name of the organization associated with the deployment.                                                                                                                                                                                                                                                                                                                                                     |
| `iss` | _(Issuer)_ The issuer of the OIDC token: `https://api.pulumi.com/oidc`.                                                                                                                                                                                                                                                                                                                                                       |
| `sub` | _(Subject)_ The subject of the OIDC token. Because this value is often used for configuring trust relationships, the subject claim contains information about the associated service. Each component of the subject claim is also available as a custom claim. |

## Custom claims

The token contains custom claims that provide additional, deployment-specific information.

The format of the subject claim for deployments is:

`pulumi:deploy:org:<organization name>:project:<project name>:stack:<stack name>:operation:<operation kind>:scope:write`

Valid custom claims are listed in the table below:

| Claim        | Description                                                                     |
|--------------|---------------------------------------------------------------------------------|
| `stackId`    | The fully-qualified identifier of the stack being deployed.                     |
| `operation`  | The deployment operation (one of `preview`, `update`, `refresh`, or `destroy`). |
| `org`        | The name of the organization associated with the deployment.                    |
| `project`    | The name of the project being deployed.                                         |
| `stack`      | The name of the stack being deployed.                                           |
| `deployment` | The deployment version.                                                         |
| `scope`      | The scope of the OIDC token. Always `write`.                                    |

## Configuring trust relationships

As part of the process that exchanges your deployment's OIDC token for cloud provider credentials, the cloud provider must check the OIDC token's claims against the conditions configured in the provider's trust relationship. The configuration of a trust relationship varies depending on the cloud provider, but typically uses at least the Audience, Subject, and Issuer claims. These claims can be used to restrict trust to specific organizations, projects, stacks:

* The Issuer claim is typically used to validate that the token is properly signed. The issuer's public signing key is fetched and used to validate the token's signature.
* The Audience claim for deployments contains the name of the organization associated with the deployment.
* The Subject claim contains information about the deployment. You can use this claim to restrict credentials to a specific organization/project/stack.
* The various custom claims contain the same information as the Subject claim. If your cloud provider supports configuring trust relationships based on custom claims, you can use these claims for the same purposes as the Subject claim.

The Subject and custom claims are particularly useful for configuring trust relationships, as they allow you to set very fine-grained conditions for credentials.

## Configuring OpenID Connect for your cloud provider

To configure OIDC for your cloud provider, refer to one of our guides:

* [Configuring OIDC for AWS](/docs/pulumi-cloud/deployments/oidc/aws/)
* [Configuring OIDC for Azure](/docs/pulumi-cloud/deployments/oidc/azure/)
* [Configuring OIDC for Google Cloud](/docs/pulumi-cloud/deployments/oidc/gcp/)
