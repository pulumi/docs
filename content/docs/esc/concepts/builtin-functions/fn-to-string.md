---
title: fn::toString
title_tag: fn::toString
h1: fn::toString
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
aliases:
  - /docs/reference/esc-syntax/builtin-functions/fn-to-string/
  - /docs/esc/reference/builtin-functions/fn-to-string/
  - /docs/esc/environments/syntax/builtin-functions/fn-to-string/
menu:
  esc:
    parent: esc-syntax-builtin-functions
    identifier: esc-syntax-fn-toString
    weight: 12
---

The `fn::toString` built-in function encodes a value as its string representation. This can be used to encode values for use in positions that only accept strings. If any input to `fn::toString` is a secret, the encoded values is also a secret.

- Boolean values are encoded as `true` or `false`
- Number values are encoded as the decimal representation of their whole and fractional parts
- Strings are encoded verbatim
- Null values are encoded as an empty string
- List values are encoded as a comma-separated list of the quoted string representations of their entries. For example, the list `[a, b]` is encoded as `"a","b"`, and the list `[1, 2]` is encoded as `"1","2"`
- Mapping values are encoded as a comma-separated list of `"key"="value"` pairs, sorted by key, where `key` and `value` are the quoted string representations of each of the mapping's key-value pairs. For example, the mapping `{b: y, a: x}` is encoded as `"a"="x","b"="y"`

Quoting is applied to each nested value, so entries that are themselves lists or mappings have their quotation marks escaped.

## Declaration

```yaml
fn::toString: value-to-encode
```

### Parameters

| Property          | Type   | Description                                                       |
|-------------------|--------|-------------------------------------------------------------------|
| `value-to-encode` | any    | The value to encode as a string.

### Returns

The string representation of the value.
