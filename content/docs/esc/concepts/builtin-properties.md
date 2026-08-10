---
title: Built-in Properties
title_tag: Built-in Properties | Pulumi ESC
h1: Built-in Properties
meta_desc: Reference for the ESC built-in properties — context, environments, and imports — that references can access in addition to an environment's own values.
aliases:
  - /docs/esc/environments/syntax/builtin-properties/
  - /docs/reference/esc-syntax/builtin-properties/
  - /docs/esc/reference/builtin-properties/
  - /docs/esc/environments/syntax/builtin-properties/context/
  - /docs/reference/esc-syntax/builtin-properties/context/
  - /docs/esc/reference/builtin-properties/context/
  - /docs/esc/environments/syntax/builtin-properties/environments/
  - /docs/reference/esc-syntax/builtin-properties/environments/
  - /docs/esc/reference/builtin-properties/environments/
  - /docs/esc/environments/syntax/builtin-properties/imports/
  - /docs/reference/esc-syntax/builtin-properties/imports/
  - /docs/esc/reference/builtin-properties/imports/
menu:
  esc:
    parent: esc-concepts
    identifier: esc-concepts-builtin-properties
    weight: 7
---

In addition to referencing properties defined within an environment, [references](/docs/esc/concepts/interpolations-and-references/) can access several built-in properties: information about the user evaluating an environment (`context`), other environments in the organization (`environments`), and imported environments (`imports`).

## context

The `context` built-in property provides information about the environment being evaluated, the user requesting it, and the access token they used.

{{< esc-context-schema >}}

For a worked example of how `currentEnvironment.name` and `rootEnvironment.name` differ inside an imported environment, see [How attributes resolve across imported environments](/docs/esc/guides/configuring-oidc/#how-attributes-resolve-across-imported-environments).

```yaml
values:
  greeting: Hello, ${context.pulumi.organization.login}/${context.pulumi.user.login}!
```

### Differentiating callers by token

For team and organization tokens, both `user.login` and `organization.login` resolve to the organization name, so neither one distinguishes a team token from an individual user. The `context.pulumi.token` properties are the way to tell those callers apart:

```yaml
values:
  callerType: ${context.pulumi.token.type}
  callerTeam: ${context.pulumi.token.team}
```

`token.type` and `token.team` are also available as OIDC subject attributes, which lets a cloud provider's trust policy scope an assumable role to a specific team. `token.name` is deliberately excluded from subject claims because token names are chosen by the user and could be crafted to forge a subject. See [Custom token claim](/docs/esc/guides/configuring-oidc/#custom-token-claim).

## environments

The `environments` built-in property provides access to other environments within the same organization. This allows the selective use of values from other environments without explicitly importing them. Reference a value as `${environments.<project>.<environment>.<property-path>}`.

```yaml
values:
  other: Hello, ${environments.app.dev.name}!
```

## imports

The `imports` built-in property provides access to imported environments, including those that are imported without participating in the merge stack (`merge: false`). For details on importing environments, see [Imports](/docs/esc/concepts/imports/).

```yaml
imports:
  - app/dev: { merge: false }
values:
  other: Hello, ${imports["app/dev"].name}!
```
