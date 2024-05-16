---
title_tag: pulumi-stacks Pulumi ESC Provider
meta_desc: The pulumi-stacks provider enables you to import Stack outputs from Pulumi into your Environment.
title: pulumi-stacks
h1: pulumi-stacks
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    pulumiesc:
        identifier: pulumi-stacks
        parent: esc-providers
        weight: 7
aliases:
- /docs/pulumi-cloud/esc/providers/pulumi-stacks/
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
