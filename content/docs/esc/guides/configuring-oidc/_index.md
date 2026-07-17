---
title_tag: Configure OpenID Connect | Pulumi ESC
meta_desc: This page describes how to configure OIDC token exchange with Pulumi ESC
title: Configure OpenID Connect
h1: Configuring OpenID Connect for Pulumi ESC
menu:
  esc:
    name: Configuring OIDC
    identifier: esc-guides-configuring-oidc
    parent: esc-guides
    weight: 50
aliases:
  - /docs/esc/environments/configuring-oidc/
  - /docs/esc/providers/login/oidc-setup/
  - /docs/esc/concepts/providers/login/oidc-setup/
---

Pulumi ESC can be configured to act as an OpenID Connect (OIDC) provider, issuing signed, short-lived tokens. These tokens can then be exchanged by external systems for temporary cloud provider credentials, eliminating the need for hard-coded credentials.

```yaml
values:
  aws:
    login:
      fn::open::aws-login:
        oidc:
          duration: 1h
          roleArn: arn:aws:iam::123456789123:role/aws-role
          sessionName: esc-${context.pulumi.user.login}
  environmentVariables:
    AWS_ACCESS_KEY_ID: ${aws.login.accessKeyId}
    AWS_SECRET_ACCESS_KEY: ${aws.login.secretAccessKey}
    AWS_SESSION_TOKEN: ${aws.login.sessionToken}
```

In this example we have an environment definition and ARN that identifies us to AWS. We're requesting a short term token that will live for 1 hour for the session `sessionName: esc-${context.pulumi.user.login}`. This token will be used to provide access to the AWS services defined in the permissions policies set for the role.

## Configuring OpenID with your cloud provider

To configure OIDC for your cloud provider, refer to one of our guides:

* [Configuring OIDC for AWS](/docs/esc/guides/configuring-oidc/aws/)
* [Configuring OIDC for Azure](/docs/esc/guides/configuring-oidc/azure/)
* [Configuring OIDC for Doppler](/docs/esc/guides/configuring-oidc/doppler/)
* [Configuring OIDC for Google Cloud](/docs/esc/guides/configuring-oidc/gcp/)
* [Configuring OIDC for Infisical](/docs/esc/guides/configuring-oidc/infisical/)
* [Configuring OIDC for Vault](/docs/esc/guides/configuring-oidc/vault/)

## Configuring trust relationships

Cloud providers use [OIDC token's claims](https://openid.net/specs/openid-connect-core-1_0.html#Claims) to determine whether to trust and issue credentials. While the exact configuration varies by provider, most rely on core claims like **Audience**, **Subject**, and **Issuer**. Pulumi ESC includes these by default, along with additional custom claims that mirror the subject structure.

If you need to define fine-grained trust policies (such as allowing only a specific environment or user to assume a role), you can customize the subject format or reference custom claims. This gives you more control over how access is granted and ensures that only the right entities can request credentials.

The following claims are commonly used when configuring trust relationships:

* The Issuer claim is typically used to validate that the token is properly signed. The issuer's public signing key is fetched and used to validate the token's signature.
* The Audience claim contains the name of the organization, prefixed with the provider's platform (`aws`, `azure`, `gcp`). You can use this claim to restrict credentials to a specific organization or organizations.
* The Subject claim contains a variety of information about the service. You can use this claim to restrict credentials to a specific organization/scope.
* The various custom claims contain the same information as the Subject claim. If your cloud provider supports configuring trust relationships based on custom claims, you can use these claims for the same purposes as the Subject claim.

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

To securely exchange OIDC tokens for cloud provider credentials, Pulumi ESC must present claims that match the provider's trust policy. In many cases the default claims are sufficient, but if you need to restrict access more precisely (for example, limiting credentials to a specific environment, user, or project), you can modify the subject claim format by using the `subjectAttributes` property. This is especially useful when you plan to reference the subject within your cloud provider's trust policy to restrict which environments, users, or organizations may request credentials.

By default (when `subjectAttributes` is not set), the subject claim has the format:

`pulumi:environments:org:<organization name>:env:<project name>/<environment name>`

When you set `subjectAttributes`, the subject instead begins with the fixed prefix `pulumi:environments:pulumi.organization.login:{ORGANIZATION_NAME}`, and each configured attribute is appended to it as a `:<attribute>:<value>` pair, in the order listed.

The following attributes are available:

* `rootEnvironment.name`: the name of the environment that is opened first. This root environment in turn opens other imported environments
* `currentEnvironment.name`: the full name (including the project) of the environment where the ESC login provider and `subjectAttributes` are defined
* `pulumi.user.login`: the login identifier of the user opening the environment
* `pulumi.organization.login`: the login identifier of the organization

{{< notes type="info" >}}

The set of attributes that may be encoded into the subject claim is deliberately restricted to this fixed list. Because the subject is consumed by the cloud provider's trust policy to make authorization decisions, only values that are determined and attested by the Pulumi platform (rather than supplied by the requesting caller) are permitted. Admitting arbitrary or user-controllable values would allow a caller to forge a subject that satisfies a trust policy and thereby obtain credentials they are not entitled to. Each supported attribute therefore reflects a non-spoofable, platform-derived identity or environment value; attributes that a caller could influence are intentionally excluded.

{{< /notes >}}

### Example

Consider the `project/development` environment, opened by the user `personA` in the `contoso` organization, with the following login configuration:

```yaml
values:
  aws:
    login:
      fn::open::aws-login:
        oidc:
          roleArn: arn:aws:iam::123456789123:role/aws-role
          sessionName: esc-${context.pulumi.user.login}
          subjectAttributes:
            - currentEnvironment.name
            - pulumi.user.login
```

The resulting subject claim is:

`pulumi:environments:pulumi.organization.login:contoso:currentEnvironment.name:project/development:pulumi.user.login:personA`

To restrict a role to this environment and user, configure your cloud provider's trust policy so that its subject (`sub`) condition matches this value exactly. The syntax for expressing that condition is provider-specific. See the corresponding provider guide for a complete trust-policy example, such as [Configuring OIDC for AWS](/docs/esc/guides/configuring-oidc/aws/#subject-claim-example).

{{< notes type="warning" >}}

For environments within the legacy `default` project, the project is **not** present in the subject, to preserve backwards compatibility. This affects the subject claim in two ways:

* When `subjectAttributes` is not set, the default subject claim omits the project: `pulumi:environments:org:<organization name>:env:<environment name>` (rather than the usual `pulumi:environments:org:<organization name>:env:<project name>/<environment name>`).
* When `subjectAttributes` is set, the `currentEnvironment.name` attribute resolves to only the environment name (for example, `development`) rather than the usual `project/development`. So for an environment named `development` opened by `personA`, the subject is `pulumi:environments:pulumi.organization.login:contoso:currentEnvironment.name:development:pulumi.user.login:personA`.

For this reason, we recommend moving your environments out of the `default` project for best security practices.

{{< /notes >}}

### How attributes resolve across imported environments

The `rootEnvironment.name` and `currentEnvironment.name` attributes resolve relative to the environment that opens the chain. `currentEnvironment.name` resolves to the environment in which it is defined, while `rootEnvironment.name` resolves to the top-level environment that was opened. Consider the following definitions for two environments, `Project/Environment-A` and `Project/Environment-B`:

```yaml
#Project/Environment-A
values:
  enva-rootEnv: ${context.rootEnvironment.name}
  enva-currentEnv: ${context.currentEnvironment.name}

#Project/Environment-B
imports:
- Project/Environment-A
values:
  envb-rootEnv: ${context.rootEnvironment.name}
  envb-currentEnv: ${context.currentEnvironment.name}
```

When you open `Project/Environment-B`, the output is:

```json
{
  "enva-currentEnv": "Project/Environment-A",
  "enva-rootEnv": "Project/Environment-B",
  "envb-currentEnv": "Project/Environment-B",
  "envb-rootEnv": "Project/Environment-B"
}
```

Notice how `enva-rootEnv` resolves to `Project/Environment-B`. That's because `Project/Environment-A` is opened from `Project/Environment-B`, which is the root (the top-level environment to be opened).

When importing multiple environments into Pulumi IaC stack config, each environment is resolved separately. For example, if you import multiple environments into your Pulumi stack with the `rootEnvironment.name` attribute defined in all of them, then each `rootEnvironment.name` resolves to the environment name where it is defined.
