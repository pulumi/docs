---
title: fn::open
title_tag: fn::open
h1: fn::open
meta_desc: "The fn::open built-in function in Pulumi ESC calls a provider to fetch values from outside ESC, such as cloud credentials and secrets. See syntax and examples."
aliases:
  - /docs/reference/esc-syntax/builtin-functions/fn-open/
  - /docs/esc/reference/builtin-functions/fn-open/
  - /docs/esc/environments/syntax/builtin-functions/fn-open/
menu:
  esc:
    parent: esc-syntax-builtin-functions
    identifier: esc-syntax-fn-open
    weight: 6
---

The `fn::open` built-in function invokes a [provider](/docs/esc/concepts/providers/) to fetch values from outside of ESC.

## Declaration

```yaml
fn::open:
  provider: name
  inputs: inputs
```

### Short form

In addition to the long form syntax, `fn::open` can be invoked using the short form `fn::open::name` with the inputs provided directly:

```yaml
fn::open::name: inputs
```

### Parameters

| Property    | Type         | Description                                                       |
|-------------|--------------|-------------------------------------------------------------------|
| `provider`  | string       | The name of the provider to open. In the short form, the name is part of the function key (`fn::open::name`) and this key is omitted.
| `inputs`    | any          | The inputs to the provider. The exact type is provider-dependent.

### Returns

The return value of `fn::open` is dependent on the provider being opened.
