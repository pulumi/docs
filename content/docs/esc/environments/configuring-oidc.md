---
title_tag: Configuring OpenID Connect | Pulumi ESC
meta_desc: This page provides an overview of how to configure OpenID Connect integration between Pulumi ESC and supported cloud providers.
title: Configuring OIDC
h1: Configuring OIDC for ESC
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  esc:
    parent: esc-environments
    weight: 6
---

Pulumi can be configured to act as an OpenID Connect (OIDC) provider, issuing signed, short-lived tokens. These tokens can then be exchanged by external systems for temporary cloud provider credentials, eliminating the need for hardcoded credentials.

## OIDC authentication configuration

Set up OIDC between Pulumi ESC and your cloud provider:

- [Configuring OIDC for AWS](/docs/pulumi-cloud/oidc/provider/aws/)
- [Configuring OIDC for Azure](/docs/pulumi-cloud/oidc/provider/azure/)
- [Configuring OIDC for Google Cloud](/docs/pulumi-cloud/oidc/provider/gcp/)
- [Configuring OIDC for Vault](/docs/pulumi-cloud/oidc/provider/vault/)

### Pulumi ESC token claim

The OIDC token issued by Pulumi ESC includes several claims that you can use to configure trust relationships with your cloud provider. The token contains the following claims:

| Claim         | Description |
|:--------------|:------------|
| aud           | _(Audience)_ The name of the organization associated with the environment prefixed with the provider's platform name (`aws:{org}`, `azure:{org}`, `gcp:{org}`). |
| iss           | _(Issuer)_ The issuer of the OIDC token: `https://api.pulumi.com/oidc`. |
| current_env   | _(Current Environment)_ The name of the environment where the [ESC OIDC provider configuration](/docs/esc/integrations/) is defined. |
| root_env      | _(Root Environment)_ The name of the environment that is opened first. This Root Environment in turn opens other imported environments. |
| trigger_user  | _(Trigger User)_ The user whose credentials are used to open an environment. |
| sub           | _(Subject)_ The subject of the OIDC token. Often used for configuring trust relationships, it contains information about the associated service. Each component is also available as a custom claim. |

### Pulumi ESC custom claim

The default format of the subject claim for this service is:

`pulumi:environments:org:<organization name>:env:<project name>/<environment name>`

To enforce more granular permissions you can customize the OIDC subject claims using the `subjectAttributes` property. This is especially useful if you plan to reference subject claims within your cloud provider’s trust policy. The default prefix when using `subjectAttributes` will be:

`pulumi:environments:pulumi.organization.login:{ORGANIZATION_NAME}`

Additional options for customization include:

- `rootEnvironment.name`: the name of the environment that is opened first. This root environment in turn opens other imported environments
- `currentEnvironment.name`: the name of the environment where the ESC login provider and `subjectAttributes` are defined
- `pulumi.user.login`: the login identifier of the user opening the environment
- `pulumi.organization.login`: the login identifier of the organization

## Example: Resolving rootEnvironment.name and currentEnvironment.name

Consider the following definitions for two environments, `Project/Environment-A` and `Project/Environment-B`:

```yaml
#Project/Environment-A
values:
  enva-rootEnv: ${context.rootEnvironment.name}
  enva-currentEnv: ${context.currentEnvironment.name}

#Project/Environment-B
imports:
- Project/EnvironmentA
values:
  envb-rootEnv: ${context.rootEnvironment.name}
  envb-currentEnv: ${context.currentEnvironment.name}
```

When you open `Project/Environment-B`, the output would be:

```
{
  "enva-currentEnv-name": "Project/Environment-A",
  "enva-rootEnv-name": "Project/Environment-B",
  "envb-currentEnv": "Project/Environment-B",
  "envb-rootEnv": "Project/Environment-B"
}
```

Notice how `enva-rootEnv-name` is resolved to `Project/Environment-B`. That's because Project/Environment-A is opened from Project/Environment-B which is the root, i.e. the top-level environment to be opened.

When importing multiple environments into Pulumi IaC Stack Config, each environment is resolved separately. For example, if you import multiple environments into your Pulumi Stack with `rootEnvironment.name` attribute defined in all of them, then each `rootEnvironment.name` will resolve to the environment name where it is defined.

## Configuring trust relationships

As part of the process that exchanges your service's OIDC token for cloud provider credentials, the cloud provider must check the OIDC token's claims against the conditions configured in the provider's trust relationship. The configuration of a trust relationship varies depending on the cloud provider, but typically uses at least the **Audience**, **Subject**, and **Issuer** claims. These claims can be used to restrict trust to specific organizations, projects, stacks, environments:

- The Issuer claim is typically used to validate that the token is properly signed. The issuer's public signing key is fetched and used to validate the token's signature.
- The Audience claim contains the name of the organization, prefixed with the provider's platform (`aws`, `azure`, `gcp`). You can use this claim to restrict credentials to a specific organization or organizations.
- The Subject claim contains a variety of information about the service. You can use this claim to restrict credentials to a specific organization/scope.
- The various custom claims contain the same information as the Subject claim. If your cloud provider supports configuring trust relationships based on custom claims, you can use these claims for the same purposes as the Subject claim.

The subject and custom claims are particularly useful for configuring trust relationships, as they allow you to set very fine-grained conditions for credentials.

For further details on additional OIDC integration and managing Pulumi Cloud access see our [OIDC Overview documentation](/docs/pulumi-cloud/access-management/oidc/).
