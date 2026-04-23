---
title: policyConfig
title_tag: policyConfig
h1: policyConfig
meta_desc: The policyConfig reserved property provides configuration values to Pulumi policy packs through ESC environments.
menu:
  esc:
    parent: esc-syntax-reserved-properties
    identifier: esc-syntax-reserved-policy-config
    weight: 4
---

The `policyConfig` reserved property contains values that should be exported as configuration for Pulumi policy packs. When an ESC environment is attached to a policy pack in a policy group, the values under `policyConfig` are made available to the policy pack at runtime.

## Properties

| Property | Type | Description |
|----------|------|-------------|
| policyName | object | Configuration values for the policy named `policyName` |
| packName:policyName | object | Configuration values for the policy named `policyName` in the pack named `packName` |

Keys can use either format:

- **`policyName`** — when the ESC environment is associated with a single policy pack
- **`packName:policyName`** — to scope configuration to a specific pack, following the same namespacing pattern as [`pulumiConfig`](/docs/esc/environments/syntax/reserved-properties/pulumi-config/)

## Example

### Without pack namespace

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

#### Evaluated result

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

### With pack namespace

```yaml
values:
  policyConfig:
    my-compliance-pack:cost-compliance:
      maxMonthlyCost: 5000
```

#### Evaluated result

```json
{
  "policyConfig": {
    "my-compliance-pack:cost-compliance": {
      "maxMonthlyCost": 5000
    }
  }
}
```
