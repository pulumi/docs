---
title_tag: OpenID Connect Provider Integration for Pulumi
meta_desc: This page provides an overview of how to configure OpenID Connect integration between
           Pulumi and supported cloud providers.
title: OpenID Provider
h1: OpenID Connect Provider integration
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    pulumicloud:
        parent: openid-connect
        identifier: openid-connect-provider
        weight: 4
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

The token contains the following claims:

| Claim         | Description |
|:--------------|:------------|
| aud           | _(Audience)_ The name of the organization associated with the environment. |
| iss           | _(Issuer)_ The issuer of the OIDC token: `https://api.pulumi.com/oidc`. |
| current_env   | _(Current Environment)_ The name of the environment where the [ESC OIDC provider configuration](/docs/esc/providers/) is defined. |
| root_env      | _(Root Environment)_ The name of the environment that is opened first. This Root Environment in turn opens other imported environments. |
| trigger_user  | _(Trigger User)_ The user whose credentials are used to open an environment. |
| sub           | _(Subject)_ The subject of the OIDC token. Often used for configuring trust relationships, it contains information about the associated service. Each component is also available as a custom claim. |

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

The default format of the subject claim for this service is:

`pulumi:environments:org:<organization name>:env:<environment name>`

If you want to have granular permissions, then we recommend using `subjectAttributes` property to customize the OIDC subject claims if you plan to use subject claims in your cloud provider trust policy. The default prefix when using `subjectAttributes` will be

`pulumi:environments:pulumi.organization.login:{ORGANIZATION_NAME}`

Additional options for customization include:

* `rootEnvironment.name`: the name of the environment that is opened first. This root environment in turn opens other imported environments
* `currentEnvironment.name`: the name of the environment where the ESC login provider and `subjectAttributes` are defined
* `pulumi.user.login`: the login identifier of the user opening the environment
* `pulumi.organization.login`: the login identifier of the organization

Let's explain how `rootEnvironment.name` and `currentEnvironment.name` work with an example. Consider the following definitions for two environments, `Environment-A` and `Environment-B`:

```yaml
#Environment-A
values:
  enva-rootEnv: ${context.rootEnvironment.name}
  enva-currentEnv: ${context.currentEnvironment.name}

#Environment-B
imports:
- EnvironmentA
values:
  envb-rootEnv: ${context.rootEnvironment.name}
  envb-currentEnv: ${context.currentEnvironment.name}
```

If you open `Environment-B`, the output would be:

```
{
  "enva-currentEnv-name": "Environment-A",
  "enva-rootEnv-name": "Environment-B",
  "envb-currentEnv": "Environment-B",
  "envb-rootEnv": "Environment-B"
}
```

Notice how `enva-rootEnv-name` is resolved to `Environment-B`. That's because Environment-A is opened from Environment-B which is the root, i.e. the top-level environment to be opened.

When importing multiple environments into Pulumi IaC Stack Config, each environment is resolved separately. For example, if you import multiple environments into your Pulumi Stack with `rootEnvironment.name` attribute defined in all of them, then each `rootEnvironment.name` will resolve to the environment name where it is defined.

## Configuring trust relationships

As part of the process that exchanges your service's OIDC token for cloud provider credentials, the cloud provider must check the OIDC token's claims against the conditions configured in the provider's trust relationship. The configuration of a trust relationship varies depending on the cloud provider, but typically uses at least the Audience, Subject, and Issuer claims. These claims can be used to restrict trust to specific organizations, projects, stacks, environments etc:

* The Issuer claim is typically used to validate that the token is properly signed. The issuer's public signing key is fetched and used to validate the token's signature.
* The Audience claim contains the name of the organization associated with the deployment. You can use this claim to restrict credentials to a specific organization or organizations.
* The Subject claim contains a variety of information about the service. You can use this claim to restrict credentials to a specific organization/scope.
* The various custom claims contain the same information as the Subject claim. If your cloud provider supports configuring trust relationships based on custom claims, you can use these claims for the same purposes as the Subject claim.

The Subject and custom claims are particularly useful for configuring trust relationships, as they allow you to set very fine-grained conditions for credentials.

## Configuring OpenID Connect for your cloud provider

To configure OIDC for your cloud provider, refer to one of our guides:

* [Configuring OIDC for AWS](/docs/pulumi-cloud/oidc/provider/aws/)
* [Configuring OIDC for Azure](/docs/pulumi-cloud/oidc/provider/azure/)
* [Configuring OIDC for Google Cloud](/docs/pulumi-cloud/oidc/provider/gcp/)
* [Configuring OIDC for Vault](/docs/pulumi-cloud/oidc/provider/vault/)
