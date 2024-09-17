---
title: pulumi-stacks
title_tag: pulumi-stacks Pulumi ESC Provider
meta_desc: The pulumi-stacks provider enables you to import Stack outputs from Pulumi into your Environment.
h1: pulumi-stacks
menu:
    esc:
        identifier: pulumi-stacks
        parent: esc-pulumi-iac-integrations
        weight: 1
aliases:
    - /docs/pulumi-cloud/esc/providers/pulumi-stacks/
    - /docs/esc/providers/pulumi-stacks/
---

The `pulumi-stacks` provider enables you to import Stack outputs from Pulumi into your Environment.

## Example

```yaml
stack-outputs:
  fn::open::pulumi-stacks:
    stacks:
      myNetworkingStack:
        stack: myNetworkingProject/prod
      myDataStack:
        stack: myDataProject/prod
```

## Inputs

| Property | Type                                   | Description                                   |
|----------|----------------------------------------|-----------------------------------------------|
| `stacks` | map[string][PulumiStack](#pulumistack) | A map of names to stacks to get outputs from. |

### PulumiStack

| Property | Type   | Description                                                                       |
|----------|--------|-----------------------------------------------------------------------------------|
| `stack`  | string | The project-qualified name of the stack to get outputs for, e.g. `myProject/dev`. |

## Outputs

The `pulumi-stacks` provider returns a map of names to raw output values for the specified stacks.
