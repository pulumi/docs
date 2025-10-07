---
title: fn::concat
title_tag: fn::concat
h1: fn::concat
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  reference:
    parent: esc-ref-builtin-functions
    identifier: esc-ref-fn-concat
    weight: 1
---

The `fn::concat` built-in function concatenates two or more arrays.

## Declaration

```yaml
fn::concat: array-of-arrays
```

### Parameters

| Property          | Type   | Description                                                       |
|-------------------|--------|-------------------------------------------------------------------|
| `array-of-arrays` | array  | The arrays to concatenate.

### Returns

A new array that concatenates those passed as arguments.

## Example

### Definition

```yaml
values:
  foo:
    - 1
    - 2
  bar:
    - 3
    - 4
  baz:
    fn::concat:
        - ${foo}
        - ${bar}
```

### Evaluated result

```json
{
  "bar": [
    3,
    4
  ],
  "baz": [
    1,
    2,
    3,
    4
  ],
  "foo": [
    1,
    2
  ]
}
```
