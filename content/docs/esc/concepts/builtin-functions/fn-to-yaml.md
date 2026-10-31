---
title: fn::toYAML
title_tag: fn::toYAML
h1: fn::toYAML
meta_desc: "Use fn::toYAML in Pulumi ESC to encode a value as a YAML string for fields that only accept strings. Secret inputs stay secret. See syntax and examples."
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
