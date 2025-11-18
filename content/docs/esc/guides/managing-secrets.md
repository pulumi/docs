---
title_tag: Managing Secrets in Pulumi ESC
title: Managing Secrets
h1: Managing Secrets in Pulumi ESC
meta_desc: Learn how to store, retrieve, and organize secrets in Pulumi ESC environments using the CLI and Pulumi Cloud console.
menu:
  esc:
    parent: esc-guides
    identifier: esc-guides-managing-secrets
    weight: 2
aliases:
  - /docs/esc/get-started/store-and-retrieve-secrets/
  - /docs/pulumi-cloud/esc/get-started/store-and-retrieve-secrets/
---

This guide shows you how to store and retrieve secrets in Pulumi ESC environments. Secrets are encrypted values that ESC stores securely and hides from view by default.

## Prerequisites

- [ESC CLI](/docs/install/esc/) installed
- [Pulumi account](https://app.pulumi.com/signup) created
- An ESC environment (create one with `esc env init <org>/<project>/<env-name>`)

## Understanding ESC values

ESC environments store configuration as key-value pairs in YAML format. All values are defined under a top-level `values` key:

```yaml
values:
  apiEndpoint: https://api.example.com
  region: us-west-2
  apiKey:
    fn::secret: my-secret-value
```

Values can be:

- **Plain text** - Regular configuration values (region, endpoint URLs)
- **Secrets** - Encrypted values marked with `fn::secret`
- **Structured data** - Objects and arrays
- **Dynamic values** - Generated from providers (covered in other guides)

## Storing secrets

### Via the CLI

Add a secret to your environment using the `--secret` flag:

```bash
esc env set <org>/<project>/<env-name> apiKey my-secret-value --secret
```

For example:

```bash
esc env set my-org/my-project/dev apiKey demo-secret-123 --secret
```

This encrypts the value before storing it.

### Via the Pulumi Cloud console

1. Navigate to [Pulumi Cloud](https://app.pulumi.com)
1. Select **Environments** in the left navigation
1. Select your environment
1. In the editor, add your secret using the `fn::secret` function:

```yaml
values:
  apiKey:
    fn::secret: my-secret-value
```

1. Select **Save**

The console will encrypt the secret and replace the plaintext value with a ciphertext reference:

```yaml
values:
  apiKey:
    fn::secret:
      ciphertext: ZXNjeAA...
```

## Retrieving secrets

### Via the CLI

Open your environment to retrieve all values, including secrets:

```bash
esc env open <org>/<project>/<env-name>
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
esc env get <org>/<project>/<env-name> apiKey
```

### Via the Pulumi Cloud console

1. Select your environment in Pulumi Cloud
1. Select **Open** to evaluate the environment
1. Toggle **Show secrets** to reveal encrypted values

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
esc env get my-org/my-project/dev database.password
```

### Multiple environments

Organize secrets by environment (dev, staging, production) using separate ESC environments:

- `my-org/my-project/dev` - Development secrets
- `my-org/my-project/staging` - Staging secrets
- `my-org/my-project/prod` - Production secrets

Each environment can have different RBAC permissions, ensuring production secrets are only accessible to authorized users.

## Best practices

### Use secrets for sensitive data

Mark these values as secrets:

- API keys and tokens
- Database passwords
- Private keys and certificates
- OAuth client secrets

### Use plain text for non-sensitive data

These can be plain text:

- Region names
- Public endpoints
- Feature flags
- Port numbers

### Rotate secrets regularly

Update secrets by setting new values:

```bash
esc env set my-org/my-project/prod apiKey new-secret-value --secret
```

ESC versions every change, allowing you to roll back if needed.

### Control access with RBAC

Use [Role-Based Access Control](/docs/esc/administration/access-control/) to limit who can read or write secrets:

- Grant teams read-only access to production secrets
- Allow developers full access to development secrets
- Use service accounts for CI/CD access

## Next steps

- [Integrate with Pulumi IaC](/docs/esc/guides/integrate-with-pulumi-iac/) - Use secrets in your infrastructure code
- [Dynamic secrets](/docs/esc/integrations/dynamic-secrets/) - Pull secrets from AWS, Azure, GCP secret stores
- [Running commands with esc run](/docs/esc/guides/running-commands-with-esc/) - Inject secrets into any command
- [Access control reference](/docs/esc/environments/access-control/) - Complete RBAC documentation
