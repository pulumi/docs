---
title_tag: Managing Secrets in Pulumi ESC
title: Managing Secrets
h1: Managing Secrets in Pulumi ESC
meta_desc: Learn how to store, retrieve, and organize secrets in Pulumi ESC environments using the CLI and Pulumi Cloud console.
menu:
  esc:
    parent: esc-operations
    identifier: esc-guides-managing-secrets
    weight: 30
aliases:
  - /docs/esc/get-started/store-and-retrieve-secrets/
  - /docs/pulumi-cloud/esc/get-started/store-and-retrieve-secrets/
  - /docs/esc/guides/managing-secrets/
---

This guide shows you how to store and retrieve secrets in Pulumi ESC environments. Secrets are encrypted values that ESC stores securely and hides from view by default.

New to ESC? Start with [Get Started](/docs/esc/get-started/) for a five-minute walkthrough, then return here for the full secret-management workflow.

## Understanding ESC values

ESC environments store configuration as key-value pairs in YAML under a top-level `values` key. Any value wrapped in `fn::secret` is encrypted at rest and masked in output:

```yaml
values:
  region: us-west-2 # plaintext configuration
  apiKey:
    fn::secret: my-secret-value # encrypted secret
```

For the full breakdown of static, secret, and dynamic value types, see [Environments](/docs/esc/concepts/environments/).

## Storing secrets

To store a secret, add an [`fn::secret`](/docs/esc/concepts/builtin-functions/fn-secret/) value to your environment — using the CLI (`pulumi env set --secret`), the Pulumi Cloud console, or by editing the environment YAML directly. See [`fn::secret`](/docs/esc/concepts/builtin-functions/fn-secret/#storing-secrets) for the full reference and examples, including multi-line secrets such as PEM-formatted keys and certificates.

## Retrieving secrets

### Via the CLI

Open your environment to retrieve all values, including secrets:

```bash
pulumi env open <org>/<project>/<env-name>
```

This returns all values in JSON format with secrets revealed:

```json
{
  "apiKey": "my-secret-value",
  "region": "us-west-2"
}
```

To retrieve a single value:

```bash
pulumi env get <org>/<project>/<env-name> apiKey
```

### Via the Pulumi Cloud console

1. Select your environment in Pulumi Cloud
1. Select **Open** to evaluate the environment
1. Toggle **Show secrets** to reveal encrypted values

### Via Pulumi IaC or language SDKs

You can also consume ESC secrets programmatically — either through [Pulumi IaC stacks that import the environment](/docs/esc/guides/integrate-with-pulumi-iac/), or directly using the [ESC SDK](/docs/esc/concepts/sdks/).

## Organizing secrets

### Nested structure

Group related secrets using nested keys:

```yaml
values:
  database:
    host: db.example.com
    password:
      fn::secret: db-password-123
    port: 5432
  api:
    key:
      fn::secret: api-key-456
    endpoint: https://api.example.com
```

Access nested values with dot notation:

```bash
pulumi env get my-org/my-project/dev database.password
```

### Multiple environments

Organize secrets by environment (dev, staging, production) using separate ESC environments:

- `my-org/my-project/dev` - Development secrets
- `my-org/my-project/staging` - Staging secrets
- `my-org/my-project/prod` - Production secrets

Each environment can have different RBAC permissions, ensuring production secrets are only accessible to authorized users.

## Best practices

### Rotate secrets regularly

You can replace a secret manually with `pulumi env set ... --secret` (ESC versions every change, so you can audit or roll back). For supported secret types, ESC can also [rotate credentials automatically on a schedule](/docs/esc/concepts/rotators/) — the recommended approach. See [Rotating secrets](/docs/esc/operations/rotation/) for operational guidance and [best practices](/docs/esc/operations/rotation/best-practices/).

### Control access with RBAC

Use [Role-Based Access Control](/docs/administration/access-identity/rbac/scopes/environments/) to limit who can read or write secrets:

- Grant teams read-only access to production secrets
- Allow developers full access to development secrets
- Use service accounts for CI/CD access

## Next steps

- [Integrate with Pulumi IaC](/docs/esc/guides/integrate-with-pulumi-iac/) - Use secrets in your infrastructure code
- [Dynamic secrets](/docs/esc/providers/secrets/) - Pull secrets from AWS, Azure, GCP secret stores
- [Running commands with pulumi env run](/docs/esc/guides/running-commands/) - Inject secrets into any command
- [Access control reference](/docs/administration/access-identity/rbac/) - Complete RBAC documentation
