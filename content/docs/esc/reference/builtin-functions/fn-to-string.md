---
title: fn::toString
title_tag: fn::toString
h1: fn::toString
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  esc:
    parent: esc-ref-builtin-functions
    identifier: esc-ref-fn-toString
    weight: 9
---

The `fn::toString` built-in function encodes a value as its string representation. This can be used to encode values for use in positions that only accept strings. If any input to `fn::toString` is a secret, the encoded values is also a secret.

- Boolean values are encoded as `true` or `false`
- Number values are encoded as the decimal representation of their whole and fractional parts
- Strings are encoded verbatim
- Binary data is encoded as its Base64-encoded representation
- List values are encoded as a comma-separated list of the string representations of their entries
- Mapping values are encoded as a comma-separated list of `key=value` pairs, where `key` and `value` are the string representations of each of the mapping's key-value pairs

## Declaration

```yaml
fn::toString: value-to-encode
```

### Parameters

| Property          | Type   | Description                                                       |
|-------------------|--------|-------------------------------------------------------------------|
| `value-to-encode` | any    | The value to encode as a string.

### Returns

The decoded value.

## Example

### Definition

```yaml
values:
  string-value
    fn::toString:
      hello: world
      from: [ "pulumi", "esc" ]
```

### Evaluated result

```json
{
  "string-value": "hello=world,from=pulumi,esc"
}
```
