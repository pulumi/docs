---
title: fn::toBase64
title_tag: fn::toBase64
h1: fn::toBase64
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
aliases:
  - /docs/reference/esc-syntax/builtin-functions/fn-to-base64/
  - /docs/esc/reference/builtin-functions/fn-to-base64/
  - /docs/esc/environments/syntax/builtin-functions/fn-to-base64/
menu:
  esc:
    parent: esc-syntax-builtin-functions
    identifier: esc-syntax-fn-toBase64
    weight: 10
---

The `fn::toBase64` built-in function encodes a string using standard Base64 encoding. If the input to `fn::toBase64` is a secret, the encoded value is also a secret.

## Declaration

```yaml
fn::toBase64: value-to-encode
```

### Parameters

| Property          | Type   | Description                                                       |
|-------------------|--------|-------------------------------------------------------------------|
| `value-to-encode` | string | The string to encode.

### Returns

The Base64-encoded string.
