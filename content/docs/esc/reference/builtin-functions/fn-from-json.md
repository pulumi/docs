---
title: fn::fromJSON
title_tag: fn::fromJSON
h1: fn::fromJSON
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  esc:
    parent: esc-ref-builtin-functions
    identifier: esc-ref-fn-from-json
    weight: 1
---

The `fn::fromJSON` built-in function decodes a value from its JSON representation. This can be used to expand JSON values that are stored as scalar strings into complex values. If the input to `fn::fromJSON` is a secret, all of the decoded values are also secrets.

## Declaration

```yaml
fn::fromJSON: value-to-decode
```

### Parameters

| Property          | Type   | Description                                                       |
|-------------------|--------|-------------------------------------------------------------------|
| `value-to-decode` | string | The JSON value to decode.

### Returns

The decoded value.

## Example

### Definition

```yaml
values:
  json-object:
    fn::fromJSON: "{\"hello\": \"world\"}"
```

### Evaluated result

```json
{
  "json-object": {
    "hello": "world"
  }
}
```
