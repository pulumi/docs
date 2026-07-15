---
title: fn::toYAML
title_tag: fn::toYAML
h1: fn::toYAML
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
aliases:
  - /docs/reference/esc-syntax/builtin-functions/fn-to-yaml/
  - /docs/esc/reference/builtin-functions/fn-to-yaml/
  - /docs/esc/environments/syntax/builtin-functions/fn-to-yaml/
menu:
  esc:
    parent: esc-syntax-builtin-functions
    identifier: esc-syntax-fn-toYAML
    weight: 13
---

The `fn::toYAML` built-in function encodes a value as its YAML representation. This can be used to encode values for use in positions that only accept strings. If any input to `fn::toYAML` is a secret, the encoded value is also a secret.

## Declaration

```yaml
fn::toYAML: value-to-encode
```

### Parameters

| Property          | Type   | Description                                                       |
|-------------------|--------|-------------------------------------------------------------------|
| `value-to-encode` | any    | The value to encode as YAML.

### Returns

The encoded value.
