---
title: fn::open
title_tag: fn::open
h1: fn::open
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  esc:
    parent: esc-ref-builtin-functions
    identifier: esc-ref-fn-open
    weight: 4
---

The `fn::open` built-in function invokes a provider to fetch values from outside of ESC.

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

## Example

### Long form

```yaml
values:
  aws:
    login:
      fn::open:
        provider: aws-login
        inputs:
          oidc:
            ...
```

### Short form

```yaml
values:
  aws:
    login:
      fn::open::aws-login:
        oidc:
          ...
```

### Evaluated result

```json
{
  "aws": {
    "login": {
      "AWS_ACCESS_KEY_ID": ...,
      "AWS_SECRET_ACCESS_KEY": ...,
      "AWS_SESSION_TOKEN": ...
    }
  }
}
```
