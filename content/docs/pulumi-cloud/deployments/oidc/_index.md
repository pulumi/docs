---
title_tag: OIDC Setup for Pulumi Deployments
meta_desc: This page provides an overview of how to set up OIDC for Pulumi Deployments to obtain cloud provider credentials
title: OIDC Setup
h1: OIDC Setup for Pulumi Deployments
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: OIDC Setup
    parent: pulumi-cloud-deployments
    weight: 60
    identifier: pulumi-cloud-deployments-oidc
aliases:
- /docs/pulumi-cloud/oidc/
- /docs/pulumi-cloud/access-management/oidc/
- /docs/pulumi-cloud/oidc/provider/
- /docs/pulumi-cloud/access-management/oidc/provider/
---

Pulumi Deployments supports OpenID Connect (OIDC) integration with popular cloud providers. In order for a Pulumi IaC operation like `update` or `preview` work, the Pulumi CLI must be able to access credentials that will allow it to perform the necessary CRUD operations on the resources in your stack. Pulumi Deployments' OIDC integrations allow your your deployments to use dynamic, short-lived cloud credentials for supported clouds instead of static credentials which are less secure and difficult to rotate. This page explains how to set up OIDC for Pulumi Deployments to access resources in your cloud provider accounts.

{{% notes type="info" %}}
There are multiple approaches for supplying cloud credentials to Pulumi Deployments. For guidance on choosing between Deployments OIDC and Pulumi ESC, see [Supplying Cloud Credentials to Pulumi Deployments](/docs/pulumi-cloud/deployments/cloud-credentials/).
{{% /notes %}}

## Overview

Pulumi Deployments can act as an OIDC provider, issuing signed, short-lived tokens that can be exchanged for temporary credentials with your cloud provider. This eliminates the need to store long-term cloud provider credentials in Pulumi Cloud.

Every time a deployment runs, Pulumi Cloud issues a new OIDC token specific to that run. The OIDC token is a short-lived, signed [JSON Web Token](https://jwt.io) that contains information about the deployment, and that can be exchanged for credentials from a cloud provider. For AWS, Azure, and Google Cloud, this credential exchange can be done automatically as part of the deployment setup.

If you're looking for information about the permissions a deployment has within Pulumi Cloud itself (rather than cloud provider permissions), see the [Deployment Permissions documentation](/docs/pulumi-cloud/deployments/reference/#deployment-permissions).

{{% notes type="info" %}}
Pulumi Cloud can also act as an OIDC client, accepting tokens from trusted identity providers. This is a separate feature from the Deployments OIDC integration and is documented in the [OIDC Client documentation](/docs/pulumi-cloud/access-management/oidc/client/).
{{% /notes %}}

## Token Claims

The token contains the standard audience, issuer, and subject claims:

| Claim | Description                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `aud` | _(Audience)_ The name of the organization associated with the deployment.                                                                                                                                                                                                                                                     |
| `iss` | _(Issuer)_ The issuer of the OIDC token: `https://api.pulumi.com/oidc`.                                                                                                                                                                                                                                                       |
| `sub` | _(Subject)_ The subject of the OIDC token. Because this value is often used for configuring trust relationships, the subject claim contains information about the associated service. Each component of the subject claim is also available as a custom claim. |

## Custom claims

The token also contains custom claims that provide additional, deployment-specific information.

The format of the subject claim for deployments is:

`pulumi:deploy:org:<organization name>:project:<project name>:stack:<stack name>:operation:<operation kind>:scope:write`

Valid custom claims for deployments are listed in the table below:

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

As part of the process that exchanges your deployment's OIDC token for cloud provider credentials, the cloud provider must check the OIDC token's claims against the conditions configured in the provider's trust relationship. The configuration of a trust relationship varies depending on the cloud provider, but typically uses at least the Audience, Subject, and Issuer claims. These claims can be used to restrict trust to specific organizations, projects, stacks, etc:

* The Issuer claim is typically used to validate that the token is properly signed. The issuer's public signing key is fetched and used to validate the token's signature.
* The Audience claim contains the name of the organization associated with the deployment. You can use this claim to restrict credentials to a specific organization.
* The Subject claim contains a variety of information about the deployment. You can use this claim to restrict credentials to a specific organization, project, stack, etc.
* The various custom claims contain the same information as the Subject claim. If your cloud provider supports configuring trust relationships based on custom claims, you can use these claims for the same purposes as the Subject claim.

The Subject and custom claims are particularly useful for configuring trust relationships, as they allow you to set very fine-grained conditions for credentials.

## Cloud Provider Setup

To configure OIDC for your cloud provider with Pulumi Deployments, refer to one of these guides:

* [Configure OpenID Connect for AWS with Pulumi Deployments](/docs/pulumi-cloud/deployments/oidc/provider/aws/)
* [Configure OpenID Connect for Azure with Pulumi Deployments](/docs/pulumi-cloud/deployments/oidc/provider/azure/)
* [Configure OpenID Connect for Google Cloud with Pulumi Deployments](/docs/pulumi-cloud/deployments/oidc/provider/gcp/)
