---
title: Providers and rotators
title_tag: Pulumi ESC providers and rotators
h1: Providers and rotators
meta_desc: First-party plugins that produce values inside a Pulumi ESC environment — issuing logins, importing secrets, and rotating credentials.
menu:
  esc:
    name: Providers & rotators
    identifier: esc-concepts-providers
    parent: esc-concepts
    weight: 5
---

Providers and rotators are the first-party plugins shipped with Pulumi ESC. They run inside the environment evaluator and produce values you can reference, import, or expose to other tools. There is no separate install step — every plugin ships with ESC and is invoked directly from environment YAML.

For the full catalog of available plugins, see [Providers](/docs/esc/providers/).

## How they differ

A **provider** is invoked under `values:` using `fn::open::<name>`. Each time an environment is opened, the provider runs and its return value is interpolated into the environment. Providers are stateless from one open to the next — they always produce a fresh value.

```yaml
values:
  aws:
    login:
      fn::open::aws-login:
        oidc:
          roleArn: arn:aws:iam::123456789012:role/esc-oidc
```

A **rotator** is invoked under `rotators:` using `fn::rotate::<name>`. Unlike a provider, a rotator is stateful: it stores the credentials it has issued in the environment definition and replaces them on demand (manually via `esc env rotate` or on a schedule). Consumers open the environment to read the current credentials; rotation only happens when explicitly triggered. Most rotators also use a login provider to authenticate the rotation call itself.

```yaml
rotators:
  database:
    fn::rotate::postgres:
      inputs:
        login: ${db.adminLogin}
        username: app
```

The two share an underlying plugin model — same authoring conventions, same evaluation engine — but differ in lifecycle and YAML placement.

## Categories

Providers fall into two functional categories, plus rotators as a third:

- **[Login providers](/docs/esc/providers/login/)** — issue short-lived credentials for downstream services (AWS, Azure, GCP, GitHub, Vault, Doppler, Infisical, Snowflake). Prefer OpenID Connect over static keys where supported. See [OIDC setup](/docs/esc/guides/configuring-oidc/) for per-provider trust configuration.
- **[Secrets and configuration providers](/docs/esc/providers/secrets/)** — pull values from an external system of record (Secrets Manager, Key Vault, 1Password, Vault, Doppler, Infisical, Parameter Store, Pulumi stack outputs, Terraform state, or a custom adapter).
- **[Rotators](/docs/esc/providers/rotators/)** — periodically replace a stored credential with a freshly issued one. Some rotators (e.g. `mysql`, `postgres`) need a [rotation connector](/docs/esc/operations/rotation/) to reach targets in private networks.

If a value can't be produced by a built-in plugin, the [`external` provider](/docs/esc/providers/secrets/external/) and [`external` rotator](/docs/esc/providers/rotators/external/) let you plug in your own service.

## Evaluation model

Providers and rotators both execute inside the ESC evaluator at the moment an environment is opened or rotated — not when the environment is defined. This guarantees that:

- Credentials are fresh at the point of use (never persisted in plaintext beyond the environment-level encryption).
- An open is reproducible: the same environment opened twice in quick succession will return logically equivalent values, modulo any intentional `fn::rotate::*` calls between them.
- Secrets read from a downstream provider are subject to that provider's own access control. ESC does not persist them outside the environment's encrypted state.

For the full evaluation order (providers, imports, interpolations, and how merge semantics work between them), see the [environments reference](/docs/esc/environments/).
