---
title_tag: Customizing OIDC Claims | Pulumi ESC
meta_desc: This guide provides an overview of how to customize OpenID claims between Pulumi ESC and supported cloud providers.
title: Customizing OIDC Claims
h1: Customizing OIDC claims for ESC
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  esc:
    parent: esc-environments
    weight: 7
---

To securely exchange OIDC tokens for cloud provider credentials, Pulumi ESC must present claims that match the provider’s trust policy. In many cases, the default claims are sufficient. But if you need to restrict access more precisely, such as limiting credentials to a specific environment, user, or project you can customize the subject and other claims.

## Configuring trust relationships

Cloud providers use [OIDC token's claims](https://openid.net/specs/openid-connect-core-1_0.html#Claims) to determine whether to trust and issue credentials. While the exact configuration varies by provider, most rely on core claims like **Audience**, **Subject**, and **Issuer**. Pulumi ESC includes these by default, along with additional custom claims that mirror the subject structure.

If you need to define fine-grained trust policies—such as allowing only a specific environment or user to assume a role—you can customize the subject format or reference custom claims. This gives you more control over how access is granted and ensures that only the right entities can request credentials.

The following claims are commonly used when configuring trust relationships:

- The Issuer claim is typically used to validate that the token is properly signed. The issuer's public signing key is fetched and used to validate the token's signature.
- The Audience claim contains the name of the organization, prefixed with the provider's platform (`aws`, `azure`, `gcp`). You can use this claim to restrict credentials to a specific organization or organizations.
- The Subject claim contains a variety of information about the service. You can use this claim to restrict credentials to a specific organization/scope.
- The various custom claims contain the same information as the Subject claim. If your cloud provider supports configuring trust relationships based on custom claims, you can use these claims for the same purposes as the Subject claim.

## Default token claim

Pulumi ESC's default issued OIDC tokens include the following claims:

| Claim         | Description |
|:--------------|:------------|
| aud           | _(Audience)_ The name of the organization associated with the environment prefixed with the provider's platform name (`aws:{org}`, `azure:{org}`, `gcp:{org}`). |
| iss           | _(Issuer)_ The issuer of the OIDC token: `https://api.pulumi.com/oidc`. |
| current_env   | _(Current Environment)_ The name of the environment where the [ESC OIDC provider configuration](/docs/esc/integrations/) is defined. |
| root_env      | _(Root Environment)_ The name of the environment that is opened first. This Root Environment in turn opens other imported environments. |
| trigger_user  | _(Trigger User)_ The user whose credentials are used to open an environment. |
| sub           | _(Subject)_ The subject of the OIDC token. Often used for configuring trust relationships, it contains information about the associated service. Each component is also available as a custom claim. |

## Custom token claim

To tailor token claims for more granular control, you can modify the default subject claim format by using the `subjectAttributes` property. This allows you to reference specific attributes in your cloud provider’s trust policy. This is especially useful if you plan to reference subject claims within your cloud provider’s trust policy.

Default subject claim format:

`pulumi:environments:pulumi.organization.login:{ORGANIZATION_NAME}`

Additional options for customization include:

- `rootEnvironment.name`: the name of the environment that is opened first. This root environment in turn opens other imported environments
- `currentEnvironment.name`: the name of the environment where the ESC login provider and `subjectAttributes` are defined
- `pulumi.user.login`: the login identifier of the user opening the environment
- `pulumi.organization.login`: the login identifier of the organization

Consider the following example definitions for two environments, `Project/Environment-A` and `Project/Environment-B`:

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
