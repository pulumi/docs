---
title: fn::final
title_tag: fn::final
h1: fn::final
meta_desc: "The fn::final built-in function in Pulumi ESC marks a value as final so child environments cannot override it. See the syntax and an example."
aliases:
  - /docs/esc/environments/syntax/builtin-functions/fn-final/
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
