---
title: fn::fromBase64
title_tag: fn::fromBase64
h1: fn::fromBase64
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  esc:
    parent: esc-ref-builtin-functions
    identifier: esc-ref-fn-from-base64
    weight: 2
---

The `fn::fromBase64` built-in function decodes its input into a binary value. This can be used to realize binary values that are stored as Base64-encoded (often for use with the [`files` well-known property](/docs/esc/reference/well-known-properties/files). If the input to `fn::fromBase64` is a secret, the decoded value is also a secret.

## Declaration

```yaml
fn::fromBase64: value-to-decode
```

### Parameters

| Property          | Type   | Description                                                       |
|-------------------|--------|-------------------------------------------------------------------|
| `value-to-decode` | string | The base64-encoded value.

### Returns

The decoded data.

## Example

### Definition

```yaml
values:
  binary-data:
    fn::fromBase64: aGVsbG8sIHdvcmxkIQo=
```

### Evaluated result

```json
{
  "binary-data": "hello, world!"
}
```
