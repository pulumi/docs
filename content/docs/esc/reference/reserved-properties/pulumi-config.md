---
title: pulumiConfig
title_tag: pulumiConfig
h1: pulumiConfig
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  esc:
    parent: esc-ref-reserved-properties
    identifier: esc-ref-reserved-pulumi-config
    weight: 3
---

The `pulumiConfig` reserved property contains values that should be exported as stack configuration for Pulumi IaC. See the [Pulumi IaC integration docs](/docs/esc/integrations/infrastructure/pulumi-iac) for an overview.

## Properties

| Property | Type   | Description                                                       |
|----------|--------|-------------------------------------------------------------------|
| key      | any    | The value of the Pulumi config value `key`

## Example

```yaml
values:
  pulumiConfig:
    aws:region: us-west-2
    greeting: Hello
```

### Evaluated result

```json
{
  "pulumiConfig": {
    "aws:region": "us-west-2",
    "greeting": "Hello"
  }
}
```

### Using `pulumi config`

Assuming a Pulumi IaC stack that is configured to use the environment above:

```console
$ pulumi config
KEY                           VALUE
aws:region                    us-west-2
greeting                      Hello
```
