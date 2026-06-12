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

## Prerequisites

- [Pulumi CLI](/docs/iac/download-install/) installed
- [Pulumi account](https://app.pulumi.com/signup) created
- An ESC environment (create one with `pulumi esc init <org>/<project>/<env-name>`)

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
pulumi esc set <org>/<project>/<env-name> apiKey my-secret-value --secret
```

For example:

```bash
pulumi esc set my-org/my-project/dev apiKey demo-secret-123 --secret
```

This encrypts the value before storing it.

### Via the Pulumi Cloud console

1. Navigate to [Pulumi Cloud](https://app.pulumi.com/signin)
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

### Multi-line secrets

For multi-line values such as private keys, TLS certificates, or SSH keys, use a YAML block scalar with `fn::secret`:

```yaml
values:
  tlsCert:
    fn::secret: |
      -----BEGIN CERTIFICATE-----
      MIIDXTCCAkWgAwIBAgIJAMqBbsYRO...
      -----END CERTIFICATE-----
  privateKey:
    fn::secret: |
      -----BEGIN RSA PRIVATE KEY-----
      MIIEowIBAAKCAQEA0Z3VS5JJcds3...
      -----END RSA PRIVATE KEY-----
```

The `|` character tells YAML to preserve newlines, which is required for PEM-formatted values. Using `pulumi esc set` for multi-line secrets is not recommended — use the console editor or edit the environment YAML directly.

## Retrieving secrets

### Via the CLI

Open your environment to retrieve all values, including secrets:

```bash
pulumi esc open <org>/<project>/<env-name>
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
pulumi esc get <org>/<project>/<env-name> apiKey
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
pulumi esc get my-org/my-project/dev database.password
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

ESC supports two approaches to secret rotation:

**Manual update** — Replace a secret value by setting a new one:

```bash
pulumi esc set my-org/my-project/prod apiKey new-secret-value --secret
```

ESC versions every change, so you can audit the history or roll back if needed.

**Automated rotation** — For supported secret types (database passwords, AWS IAM keys, and others), ESC can [automatically rotate credentials on a schedule](/docs/esc/environments/rotation/) using `fn::rotate`. If the rotation target lives in a private network, a [rotation connector](/docs/esc/operations/rotation/) runs the rotation on Pulumi Cloud's behalf. This is the recommended approach over manual updates, as it eliminates manual steps and reduces exposure windows.

### Control access with RBAC

Use [Role-Based Access Control](/docs/esc/administration/access-control/) to limit who can read or write secrets:

- Grant teams read-only access to production secrets
- Allow developers full access to development secrets
- Use service accounts for CI/CD access

## Next steps

- [Integrate with Pulumi IaC](/docs/esc/guides/integrate-with-pulumi-iac/) - Use secrets in your infrastructure code
- [Dynamic secrets](/docs/esc/providers/secrets/) - Pull secrets from AWS, Azure, GCP secret stores
- [Running commands with pulumi esc run](/docs/esc/guides/running-commands/) - Inject secrets into any command
- [Access control reference](/docs/esc/administration/access-control/) - Complete RBAC documentation
