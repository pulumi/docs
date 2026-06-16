---
title: Outputs
title_tag: Outputs | Pulumi ESC
h1: Outputs
meta_desc: Reserved properties like environmentVariables, files, pulumiConfig, and policyConfig shape the outputs a Pulumi ESC environment produces.
aliases:
  - /docs/reference/esc-syntax/reserved-properties/
  - /docs/esc/reference/reserved-properties/
  - /docs/esc/environments/syntax/reserved-properties/
  - /docs/esc/environments/syntax/reserved-properties/environment-variables/
  - /docs/reference/esc-syntax/reserved-properties/environment-variables/
  - /docs/esc/reference/reserved-properties/environment-variables/
  - /docs/esc/environments/syntax/reserved-properties/files/
  - /docs/reference/esc-syntax/reserved-properties/files/
  - /docs/esc/reference/reserved-properties/files/
  - /docs/esc/environments/syntax/reserved-properties/pulumi-config/
  - /docs/reference/esc-syntax/reserved-properties/pulumi-config/
  - /docs/esc/reference/reserved-properties/pulumi-config/
  - /docs/esc/environments/syntax/reserved-properties/policy-config/
menu:
  esc:
    parent: esc-concepts
    identifier: esc-syntax-reserved-properties
    weight: 8
---

The [`pulumi` CLI](/docs/iac/download-install/) and other ESC consumers conventionally assign specific semantics to certain top-level properties of an evaluated ESC environment (i.e. properties defined under the [`values` section of the environment definition](/docs/esc/concepts/environments/)). These _reserved properties_ shape the outputs an environment produces when it is opened: environment variables, temporary files, Pulumi IaC stack configuration, and Pulumi policy pack configuration.

## environmentVariables

The `environmentVariables` reserved property contains values that should be exported as environment variables. For example, [`pulumi env run`](/docs/iac/cli/commands/pulumi_env_run) exports each key-value pair in the `environmentVariables` property as an environment variable that is accessible to the command to run.

This property is also used by [Pulumi policy packs](/docs/insights/policy/policy-packs/). When an ESC environment is attached to a policy pack in a policy group, `environmentVariables` are injected into the policy runtime as environment variables.

### Properties

| Property | Type   | Description                                                       |
|----------|--------|-------------------------------------------------------------------|
| name     | string | The value of the environment variable `name`

### Example

```yaml
values:
  environmentVariables:
    GREETING: Hello
```

#### Evaluated result

```json
{
  "environmentVariables": {
    "GREETING": "Hello"
  }
}
```

#### Using `pulumi env run`

```console
$ pulumi env run default/greet -- sh -c '${GREETING}, ${USER}!'
Hello, user!
```

## files

The `files` reserved property contains values that should be written to temporary files. For example, [`pulumi env run`](/docs/iac/cli/commands/pulumi_env_run) writes the contents of each property in the `files` property to a temporary file and exports the file's path in the named environment variable that is accessible to the command to run.

### Properties

| Property | Type              | Description                                                       |
|----------|-------------------|-------------------------------------------------------------------|
| name     | string or binary | The contents of the temporary file whose path will be exported in the environment variable `name`

### Example

```yaml
values:
  files:
    GREETING: Hello, ${context.pulumi.user.login}!
    BINARY:
      fn::fromBase64: ...
```

#### Evaluated result

```json
{
  "files": {
    "GREETING": "Hello, user!",
    "BINARY": ...
  }
}
```

#### Using `pulumi env run`

```console
$ pulumi env run default/greet -- sh -c 'echo ${GREETING} & cat ${GREETING}'
/tmp/tmp.iBApHfcsJ1
Hello, user!
```

## pulumiConfig

The `pulumiConfig` reserved property contains values that should be exported as stack configuration for Pulumi IaC. See the [Pulumi IaC integration guide](/docs/esc/guides/integrate-with-pulumi-iac/) for an overview.

### Properties

| Property | Type   | Description                                                       |
|----------|--------|-------------------------------------------------------------------|
| key      | any    | The value of the Pulumi config value `key`

### Example

```yaml
values:
  pulumiConfig:
    aws:region: us-west-2
    greeting: Hello
```

#### Evaluated result

```json
{
  "pulumiConfig": {
    "aws:region": "us-west-2",
    "greeting": "Hello"
  }
}
```

#### Using `pulumi config`

Assuming a Pulumi IaC stack that is configured to use the environment above:

```console
$ pulumi config
KEY                           VALUE
aws:region                    us-west-2
greeting                      Hello
```

## policyConfig

The `policyConfig` reserved property contains values that should be exported as configuration for [Pulumi policy packs](/docs/insights/policy/policy-packs/). When an ESC environment is attached to a policy pack in a policy group, the values under `policyConfig` are made available to the policy pack at runtime.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| policyName | object | Configuration values for the policy named `policyName` |
| packName:policyName | object | Configuration values for the policy named `policyName` in the pack named `packName` |

Keys can use either format:

- **`policyName`** — when the ESC environment is associated with a single policy pack
- **`packName:policyName`** — to scope configuration to a specific pack, following the same namespacing pattern as [`pulumiConfig`](#pulumiconfig)

### Example

#### Without pack namespace

```yaml
values:
  compliance:
    apiToken:
      fn::secret: xxxxxxxxxxxxxxxx

  policyConfig:
    cost-compliance:
      maxMonthlyCost: 5000
      apiEndpoint: https://compliance.example.com
      apiToken: ${compliance.apiToken}
```

##### Evaluated result

```json
{
  "policyConfig": {
    "cost-compliance": {
      "maxMonthlyCost": 5000,
      "apiEndpoint": "https://compliance.example.com",
      "apiToken": "[secret]"
    }
  }
}
```

#### With pack namespace

```yaml
values:
  policyConfig:
    my-compliance-pack:cost-compliance:
      maxMonthlyCost: 5000
```

##### Evaluated result

```json
{
  "policyConfig": {
    "my-compliance-pack:cost-compliance": {
      "maxMonthlyCost": 5000
    }
  }
}
```
