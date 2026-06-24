---
title: pulumi-stacks
title_tag: pulumi-stacks Pulumi ESC Provider
meta_desc: The pulumi-stacks provider enables you to import Stack outputs from Pulumi into your Environment.
h1: pulumi-stacks
menu:
    esc:
        identifier: pulumi-stacks
        parent: esc-providers-iac
        weight: 1
aliases:
    - /docs/esc/providers/secrets/pulumi-stacks/
    - /docs/pulumi-cloud/esc/providers/pulumi-stacks/
    - /docs/esc/providers/pulumi-stacks/
    - /docs/esc/integrations/infrastructure/pulumi-iac/pulumi-stacks/
    - /docs/esc/integrations/pulumi-stacks/
    - /docs/esc/concepts/providers/secrets/pulumi-stacks/
---

The `pulumi-stacks` provider enables you to import stack outputs from Pulumi into your environment. This includes stacks updated via the Pulumi CLI as well as stacks whose [Terraform state is stored in Pulumi Cloud](/docs/iac/get-started/terraform/terraform-state-backend/) — Terraform root module outputs are mapped to stack outputs and accessible here with no additional tokens or credentials required.

## Example

### Pulumi stack

```yaml
values:
  stackRefs:
    fn::open::pulumi-stacks:
      stacks:
        vpcInfra:
          stack: vpc-infra/dev
  pulumiConfig:
    # Consume the stack outputs as Pulumi stack configuration (inputs to your program)
    vpcId: ${stackRefs.vpcInfra.vpcId}
    publicSubnetIds: ${stackRefs.vpcInfra.publicSubnetIds}
    privateSubnetIds: ${stackRefs.vpcInfra.privateSubnetIds}
```

### Terraform state stored in Pulumi Cloud

When a stack's [Terraform state is stored in Pulumi Cloud](/docs/iac/get-started/terraform/terraform-state-backend/), the Terraform root module outputs are exposed as stack outputs (using their original snake_case names) and read here with no additional tokens or credentials. You can then map those outputs to either `pulumiConfig`, to consume them as inputs to a Pulumi program, or `environmentVariables`, to feed them back into a downstream Terraform run:

```yaml
values:
  tfStack:
    fn::open::pulumi-stacks:
      stacks:
        network:
          stack: network-tf/production
  pulumiConfig:
    # Consume the Terraform outputs as Pulumi stack configuration (inputs to your program)
    vpcId: ${tfStack.network.vpc_id}
    subnetIds: ${tfStack.network.subnet_ids}
  environmentVariables:
    # Expose the outputs as TF_VAR_* environment variables to feed a downstream Terraform run
    TF_VAR_vpc_id: ${tfStack.network.vpc_id}
```

## Inputs

| Property | Type                                   | Description                                                                                  |
|----------|----------------------------------------|----------------------------------------------------------------------------------------------|
| `stacks` | map[string][PulumiStack](#pulumistack) | A map of names to stacks to get outputs from. The names contains all outputs from the stack. |

### PulumiStack

| Property | Type   | Description                                                                       |
|----------|--------|-----------------------------------------------------------------------------------|
| `stack`  | string | The project-qualified name of the stack to get outputs for, e.g. `myProject/dev`. |

## Outputs

The `pulumi-stacks` provider returns a map of names to raw output values for the specified stacks.
