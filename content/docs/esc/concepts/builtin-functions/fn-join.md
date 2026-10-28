---
title: fn::join
title_tag: fn::join
h1: fn::join
meta_desc: "Use fn::join in Pulumi ESC to join a list of strings with a delimiter into a single string. Secret inputs yield a secret result. See syntax and examples."
aliases:
  - /docs/reference/esc-syntax/builtin-functions/fn-join/
  - /docs/esc/reference/builtin-functions/fn-join/
  - /docs/esc/environments/syntax/builtin-functions/fn-join/
menu:
  esc:
    parent: esc-syntax-builtin-functions
    identifier: esc-syntax-fn-join
    weight: 5
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
