---
title: fn::join
title_tag: fn::join
h1: fn::join
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
aliases:
  - /docs/reference/esc-syntax/builtin-functions/fn-join/
  - /docs/esc/reference/builtin-functions/fn-join/
menu:
  reference:
    parent: esc-ref-builtin-functions
    identifier: esc-ref-fn-join
    weight: 4
---

The `fn::join` built-in function joins the elements of a list of strings using a given delimiter. If any input to `fn::join` is a secret, the result is also a secret.

## Declaration

```yaml
fn::join: [ delimiter, values ]
```

### Parameters

| Property    | Type         | Description                                                       |
|-------------|--------------|-------------------------------------------------------------------|
| `delimiter` | string       | The delimiter to use when joining values
| `values`    | List<string> | The list of strings to join

### Returns

The elements of `values` joined by `delimiter`.

## Example

### Definition

```yaml
values:
  list-of-strings:
    - one
    - two
    - three
  joined:
    fn::join: [ ", ", ${list-of-strings} ]
```

### Evaluated result

```json
{
  "list-of-strings": [
    "one",
    "two",
    "three"
  ],
  "joined": "one, two, three"
}
```
