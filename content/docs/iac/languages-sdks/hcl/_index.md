---
title_tag: "HCL | Languages & SDKs"
meta_desc: An overview of Pulumi HCL, a language plugin for writing infrastructure as code in Terraform-like HCL syntax on any cloud.
title: HCL
h1: Pulumi & HCL
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: HCL
        parent: iac-languages
        weight: 7
        identifier: iac-languages-hcl
    languages:
        identifier: hcl-language
        weight: 7

aliases:
- /docs/languages-sdks/hcl/
---

Pulumi supports writing your infrastructure as code using Pulumi HCL, a language plugin that lets you author Pulumi programs in [Terraform](https://developer.hashicorp.com/terraform)-like HCL syntax. You get familiar HCL blocks, expressions, and built-in functions while using Pulumi's state management, secrets handling, and deployment engine.

Pulumi HCL is developed in the [pulumi-labs/pulumi-hcl](https://github.com/pulumi-labs/pulumi-hcl) repository.

## Prerequisites

All you need to use Pulumi HCL is the [Pulumi CLI](/docs/install/), version 3.235.0 or later. The HCL language and converter plugins ship with the CLI.

## Example

A Pulumi HCL project consists of a `Pulumi.yaml` with `runtime: hcl` and one or more `.hcl` files in the project directory.

`Pulumi.yaml`:

```yaml
name: simple-hcl
runtime: hcl
description: A simple Pulumi HCL project
```

`main.hcl`:

```hcl
pulumi {
  required_providers {
    random = {
      source  = "pulumi/random"
      version = ">= 4.0.0"
    }
  }
}

variable "prefix" {
  type    = string
  default = "test"
}

resource "random_pet" "my_pet" {
  prefix = var.prefix
  length = 2
}

output "pet_name" {
  value = random_pet.my_pet.id
}
```

{{% notes "info" %}}
Provider sources must use the `pulumi/` namespace (for example, `pulumi/aws`), not `hashicorp/`.
{{% /notes %}}

Further examples are available in the [Pulumi HCL GitHub repository](https://github.com/pulumi-labs/pulumi-hcl/tree/master/examples). The specification for Pulumi HCL programs is in the [Pulumi HCL reference](/docs/iac/languages-sdks/hcl/hcl-language-reference/).

## Pulumi programming model

The Pulumi programming model defines the core concepts you will use when creating infrastructure as code programs using Pulumi. [Concepts](/docs/iac/concepts/) describes these concepts with examples available in all supported languages.

To learn how the Pulumi programming model is implemented for Pulumi HCL, refer to the [Pulumi HCL reference](/docs/iac/languages-sdks/hcl/hcl-language-reference/).

## Terraform compatibility

Pulumi HCL is broadly compatible with Terraform-like HCL syntax. Resources, data sources, variables, locals, outputs, modules, expressions, and most built-in functions work as documented by HashiCorp, with two notable behavioral differences:

- Provider sources must use the `pulumi/` namespace, not `hashicorp/`.
- Resource replacement creates the new resource before deleting the old one (the opposite of Terraform). Set `create_before_destroy = false` in a `lifecycle` block to opt into delete-first behavior.

For the full list of differences and unsupported features, see the [Terraform compatibility section](/docs/iac/languages-sdks/hcl/hcl-language-reference/#terraform-compatibility) of the reference.

## HCL packages

The [Pulumi Registry](/registry/) houses 100+ packages that can be consumed from Pulumi HCL programs by declaring them in a `pulumi` `required_providers` block.

For Terraform or OpenTofu providers that aren't published in the Pulumi Registry, use [Any Terraform Provider](/docs/iac/concepts/providers/any-terraform-provider/) to generate a local package on the fly. This is especially relevant for Pulumi HCL users who are bringing existing programs from a Terraform codebase that depends on community or internal providers without bridged Pulumi equivalents.
