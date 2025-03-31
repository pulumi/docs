---
title: fn::rotate
title_tag: fn::rotate
h1: fn::rotate
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  esc:
    parent: esc-ref-builtin-functions
    identifier: esc-ref-fn-rotate
    weight: 5
---

The `fn::rotate` built-in function invokes a rotator to rotate secrets.

## Declaration

```yaml
fn::rotate:
  provider: name
  inputs: inputs
  state: state
```

### Short form

In addition to the long form syntax, `fn::rotate` can be invoked using the short form `fn::rotate::name`:

```yaml
fn::rotate::name:
  inputs: inputs
  state: state
```

### Parameters

| Property    | Type         | Description                                                       |
|-------------|--------------|-------------------------------------------------------------------|
| `name`      | string       | The name of the rotator to use.
| `inputs`    | any          | The inputs to the rotator. The exact type is rotator-dependent.
| `state`     | any          | The persistent state for the rotator. This value is managed by the rotator and should not be modified.

### Returns

The return value of `fn::rotate` is dependent on the rotator being invoked.

## Example

### Long form

```yaml
values:
  aws:
    iam:
      fn::rotate:
        provider: aws-iam
        inputs:
          region: us-west-2
          login: ${environments.admin.production.aws.login}
          userArn: arn::aws:iam::012345678901:user/my-user
        state:
          current: ...
          previous: ...
```

### Short form

```yaml
values:
  aws:
    iam:
      fn::rotate::aws-iam:
        inputs:
          region: us-west-2
          login: ${environments.admin.production.aws.login}
          userArn: arn::aws:iam::012345678901:user/my-user
        state:
          current: ...
          previous: ...
```

### Evaluated result

```json
{
  "aws": {
    "iam": {
      "current": ...,
      "previous": ...
    }
  }
}
```
