---
title: fn::final
title_tag: fn::final
h1: fn::final
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  esc:
    parent: esc-syntax-builtin-functions
    identifier: esc-syntax-fn-final
    weight: 11
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
