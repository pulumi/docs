---
title: fn::final
title_tag: fn::final
h1: fn::final
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  esc:
    parent: esc-syntax-builtin-functions
    identifier: esc-syntax-fn-final
    weight: 2
---

The `fn::final` built-in function marks a value as final, preventing child environments from overriding it. If a child environment attempts to override a final value, the value is not overridden and a validation warning is raised.

## Declaration

```yaml
fn::final: value
```

### Parameters

| Property | Type | Description                          |
|----------|------|--------------------------------------|
| `value`  | any  | The value to mark as final.

### Returns

The original value, marked as final so that it cannot be overridden by child environments.

## Example

### Parent environment (myproj/parent)

```yaml
values:
  frozen:
    fn::final: frozen_value
  not_final: plain_value
```

### Child environment (myproj/child)

```yaml
imports:
  - myproj/parent
values:
  frozen: overridden    # Warning, cannot override final value
  not_final: new_value  # OK
```

### Evaluated result

```json
{
  "frozen": "frozen_value",
  "not_final": "new_value"
}
```

## Composing fn::final with fn::secret

`fn::final` accepts any value, including other built-in function expressions. Wrapping `fn::secret` in `fn::final` lets platform teams distribute a shared secret to downstream environments while ensuring those environments cannot override it.

### Parent environment (myproj/platform)

```yaml
values:
  frozenSecret:
    fn::final:
      fn::secret: my_plaintext_secret
```

When the environment is saved, ESC encrypts the plaintext argument and replaces it with a ciphertext literal. The stored form becomes:

```yaml
values:
  frozenSecret:
    fn::final:
      fn::secret:
        ciphertext: ZXN...
```

### Child environment (myproj/app)

```yaml
imports:
  - myproj/platform
values:
  frozenSecret: different_value  # Warning, cannot override final value
```

### Evaluated result

```json
{
  "frozenSecret": "[secret]"
}
```

The evaluated value carries both the secret marker (so consumers redact it from output) and the final marker (so child environments cannot override it).
