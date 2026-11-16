---
title: fn::split
title_tag: fn::split
h1: fn::split
meta_desc: "Use fn::split in Pulumi ESC to split a string into a list of strings with a delimiter. Secret inputs yield a secret result. See syntax and examples."
aliases:
  - /docs/reference/esc-syntax/builtin-functions/fn-split/
  - /docs/esc/reference/builtin-functions/fn-split/
  - /docs/esc/environments/syntax/builtin-functions/fn-split/
menu:
  esc:
    parent: esc-syntax-builtin-functions
    identifier: esc-syntax-fn-split
    weight: 9
---

The `fn::split` built-in function splits a string into a list of strings using a given delimiter. If any input to `fn::split` is a secret, the result is also a secret.

## Declaration

```yaml
fn::split: [ delimiter, value ]
```

### Parameters

| Property    | Type   | Description                                                       |
|-------------|--------|-------------------------------------------------------------------|
| `delimiter` | string | The delimiter to use when splitting the string
| `value`     | string | The string to split

### Returns

A list of strings created by splitting `value` by `delimiter`.
