---
title: environmentVariables
title_tag: environmentVariables
h1: environmentVariables
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  esc:
    parent: esc-ref-well-known-properties
    identifier: esc-ref-well-known-environment-variables
    weight: 1
---

The `environmentVariables` well-known property contains values that should be exported as environment variables. For example, [`esc run`](/docs/esc/cli/commands/esc_run) exports each key-value pair in the `environmentVariables` property as an environment variable that is accessible to the command to run.

## Properties

| Property | Type   | Description                                                       |
|----------|--------|-------------------------------------------------------------------|
| name     | string | The value of the environment variable `name`

## Example

```yaml
values:
  environmentVariables:
    GREETING: Hello
```

### Evaluated result

```json
{
  "environmentVariables": {
    "GREETING": "Hello"
  }
}
```

### Using `esc run`

```console
$ esc run default/greet -- sh -c '${GREETING}, ${USER}!'
Hello, user!
```
