---
title: fn::concat
title_tag: fn::concat
h1: fn::concat
meta_desc: "The fn::concat built-in function in Pulumi ESC concatenates two or more arrays into one list. See the declaration, parameters, and an example."
aliases:
  - /docs/reference/esc-syntax/builtin-functions/fn-concat/
  - /docs/esc/reference/builtin-functions/fn-concat/
  - /docs/esc/environments/syntax/builtin-functions/fn-concat/
menu:
  esc:
    parent: esc-syntax-builtin-functions
    identifier: esc-syntax-fn-concat
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
