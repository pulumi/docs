---
title: environmentVariables
title_tag: environmentVariables
h1: environmentVariables
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
aliases:
  - /docs/reference/esc-syntax/reserved-properties/environment-variables/
  - /docs/esc/reference/reserved-properties/environment-variables/
menu:
  esc:
    parent: esc-syntax-reserved-properties
    identifier: esc-syntax-reserved-environment-variables
    weight: 1
---

The `environmentVariables` reserved property contains values that should be exported as environment variables. For example, [`pulumi esc run`](/docs/iac/cli/commands/pulumi_env_run) exports each key-value pair in the `environmentVariables` property as an environment variable that is accessible to the command to run.

This property is also used by [Pulumi policy packs](/docs/insights/policy/policy-packs/). When an ESC environment is attached to a policy pack in a policy group, `environmentVariables` are injected into the policy runtime as environment variables.

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

### Using `pulumi esc run`

```console
$ pulumi esc run default/greet -- sh -c '${GREETING}, ${USER}!'
Hello, user!
```
