---
title: fn::toJSON
title_tag: fn::toJSON
h1: fn::toJSON
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  esc:
    parent: esc-ref-builtin-functions
    identifier: esc-ref-fn-toJSON
    weight: 8
---

The `fn::toJSON` built-in function encodes a value as its JSON representation. This can be used to encode values for use in positions that only accept strings. If any input to `fn::toJSON` is a secret, the encoded values is also a secret.

## Declaration

```yaml
fn::toJSON: value-to-encode
```

### Parameters

| Property          | Type   | Description                                                       |
|-------------------|--------|-------------------------------------------------------------------|
| `value-to-encode` | any    | The value to encode as JSON.

### Returns

The decoded value.

## Example

### Definition

```yaml
values:
  json-object:
    fn::toJSON:
      hello: world
```

### Evaluated result

```json
{
  "json-object": "{\"hello\": \"world\"}"
}
```
