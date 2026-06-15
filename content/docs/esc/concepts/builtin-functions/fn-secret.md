---
title: fn::secret
title_tag: fn::secret
h1: fn::secret
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
aliases:
  - /docs/reference/esc-syntax/builtin-functions/fn-secret/
  - /docs/esc/reference/builtin-functions/fn-secret/
  - /docs/esc/environments/syntax/builtin-functions/fn-secret/
menu:
  esc:
    parent: esc-syntax-builtin-functions
    identifier: esc-syntax-fn-secret
    weight: 0
---

The `fn::secret` built-in function decrypts a ciphertext literal into a secret string value.

In addition to its evaluation-time behavior, `fn::secret` has additional behavior at update time. When an environment is saved, any `fn::secret` invocations with plaintext arguments are transformed by encrypting the plaintext and replacing it with a ciphertext literal.

## Storing secrets

To store a secret, add an `fn::secret` value to an environment. ESC encrypts it when the environment is saved, so plaintext is never persisted.

### Via the CLI

Add a secret using the `--secret` flag:

```bash
esc env set <org>/<project>/<env-name> apiKey my-secret-value --secret
```

### Via the Pulumi Cloud console

In the environment editor, wrap a value in `fn::secret` and select **Save**:

```yaml
values:
  apiKey:
    fn::secret: my-secret-value
```

### Multi-line secrets

For multi-line values such as private keys, TLS certificates, or SSH keys, use a YAML block scalar:

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

The `|` character tells YAML to preserve newlines, which is required for PEM-formatted values. Using `esc env set` for multi-line secrets is not recommended — use the console editor or edit the environment YAML directly.

## Declaration

```yaml
fn::secret:
  ciphertext: base64-encoded-ciphertext
```

### Plaintext form

This form is replaced by the ciphertext form when it is present in an environment being saved. ESC never stores plaintext secrets.

```yaml
fn::secret: plaintext-string
```

### Parameters

| Property     | Type         | Description                                                       |
|--------------|--------------|-------------------------------------------------------------------|
| `ciphertext` | string       | The secret's base64-encoded ciphertext.

### Returns

The decrypted plaintext. Decrypted values are marked as secrets by the evaluator so that combining secret and non-secret values can maintain secretness. Consumers of evaluated ESC environments may use secretness information to e.g. redact values from command output.
