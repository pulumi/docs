---
title: Providers
title_tag: Pulumi ESC providers
h1: Providers
meta_desc: First-party plugins that produce values inside a Pulumi ESC environment — issuing logins and importing secrets and configuration.
aliases:
  - /docs/esc/environments/syntax/providers/
  - /docs/reference/esc-syntax/providers/
  - /docs/esc/reference/providers/
menu:
  esc:
    identifier: esc-concepts-providers
    parent: esc-concepts
    weight: 3
---

Providers are first-party plugins shipped with Pulumi ESC. They run inside the environment evaluator and produce values you can reference, import, or expose to other tools. There is no separate install step — every plugin ships with ESC and is invoked directly from environment YAML.

## How providers work

A provider is invoked under `values:` using `fn::open::<name>`. Each time an environment is opened, the provider runs and its return value is interpolated into the environment. Providers are stateless from one open to the next — they always produce a fresh value.

```yaml
values:
  aws:
    login:
      fn::open::aws-login:
        oidc:
          roleArn: arn:aws:iam::123456789012:role/esc-oidc
```

For stateful plugins that store and replace credentials on demand or on a schedule, see [Rotators](/docs/esc/concepts/rotators/).

## Categories

Providers fall into two functional categories. For the complete list of plugins in each — along with their configuration options — see the [provider reference](/docs/esc/providers/).

- **[Login providers](/docs/esc/providers/login/)** — authenticate to a downstream service and issue short-lived credentials for it, typically through OpenID Connect. See [OIDC setup](/docs/esc/guides/configuring-oidc/) for per-provider trust configuration.
- **[Secrets and configuration providers](/docs/esc/providers/secrets/)** — pull configuration and secrets from an external system of record into your environment at open time.

If no built-in plugin produces the value you need, a custom adapter lets you plug in your own service.

## Evaluation model

Providers execute inside the ESC evaluator at the moment an environment is opened — not when the environment is defined. This guarantees that:

- Credentials are fresh at the point of use (never persisted in plaintext beyond the environment-level encryption).
- An open is reproducible: the same environment opened twice in quick succession will return logically equivalent values.
- Secrets read from a downstream provider are subject to that provider's own access control. ESC does not persist them outside the environment's encrypted state.

For the full evaluation order (providers, imports, interpolations, and how merge semantics work between them), see the [Environments reference](/docs/esc/concepts/environments/).
