---
title: fn::secret
title_tag: fn::secret
h1: fn::secret
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  esc:
    parent: esc-ref-builtin-functions
    identifier: esc-ref-fn-secret
    weight: 6
---

The `fn::secret` built-in function decrypts a ciphertext literal into a secret string value.

In addition to its evaluation-time behavior, `fn::secret` has additional behavior at update time. When an environment is saved, any `fn::secret` invocations with plaintext arguments are transformed by encrypting the plaintext and replacing it with a ciphertext literal.

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

## Example

```yaml:
values:
  password:
    fn::secret:
      ciphertext: ...
```

### Evaluted result

```json
{
  "password": "hunter2"
}
```
