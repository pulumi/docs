---
title: fn::toBase64
title_tag: fn::toBase64
h1: fn::toBase64
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
aliases:
  - /docs/reference/esc-syntax/builtin-functions/fn-to-base64/
  - /docs/esc/reference/builtin-functions/fn-to-base64/
menu:
  esc:
    parent: esc-syntax-builtin-functions
    identifier: esc-syntax-fn-toBase64
    weight: 8
---

The `fn::toBase64` built-in function encodes a binary value using Base64. If the input to `fn::toBase64` is a secret, the encoded value is also a secret.

## Declaration

```yaml
fn::toBase64: value-to-encode
```

### Parameters

| Property          | Type   | Description                                                       |
|-------------------|--------|-------------------------------------------------------------------|
| `value-to-encode` | binary | The value to encode.

### Returns

The encoded data.

## Example

### Definition

```yaml
values:
  binary-data:
    fn::toBase64: hello, world!
```

### Evaluated result

```json
{
  "binary-data": "aGVsbG8sIHdvcmxkIQo="
}
```
