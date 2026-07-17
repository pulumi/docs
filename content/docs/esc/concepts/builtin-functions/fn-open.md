---
title: fn::open
title_tag: fn::open
h1: fn::open
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
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
| `name`      | string       | The name of the provider to open.
| `inputs`    | any          | The inputs to the provider. The exact type is provider-dependent.

### Returns

The return value of `fn::open` is dependent on the provider being opened.
