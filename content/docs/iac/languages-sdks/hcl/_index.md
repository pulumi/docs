---
title_tag: "HCL | Languages & SDKs"
meta_desc: An overview of Pulumi HCL, a language plugin for writing infrastructure as code in Terraform-like HCL syntax on any cloud.
title: HCL
h1: Pulumi & HCL
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

Pulumi HCL is a superset of Terraform HCL: the `.tf` files are the same code you would write for Terraform or OpenTofu. A project consists of a `Pulumi.yaml` with `runtime: hcl` and one or more `.tf` files in the project directory.

`Pulumi.yaml`:

```yaml
name: simple-hcl
runtime: hcl
description: A simple Pulumi HCL project
```

`main.tf`:

```hcl
terraform {
  required_providers {
    random = {
      source  = "hashicorp/random"
      version = ">= 3.0.0"
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
Providers resolve the same way as OpenTofu: an unqualified source such as `random` (or a fully-qualified `hashicorp/random`) is looked up in the [OpenTofu registry](https://opentofu.org/registry/) and bridged into Pulumi automatically — no `required_providers` entry is required. Prefix a source with `pulumi/` (for example, `pulumi/aws`) to consume a native Pulumi provider instead.
{{% /notes %}}

Further examples are available in the [Pulumi HCL GitHub repository](https://github.com/pulumi-labs/pulumi-hcl/tree/master/examples). The specification for Pulumi HCL programs is in the [Pulumi HCL reference](/docs/iac/languages-sdks/hcl/hcl-language-reference/).

## Pulumi programming model

The Pulumi programming model defines the core concepts you will use when creating infrastructure as code programs using Pulumi. [Concepts](/docs/iac/concepts/) describes these concepts with examples available in all supported languages.

To learn how the Pulumi programming model is implemented for Pulumi HCL, refer to the [Pulumi HCL reference](/docs/iac/languages-sdks/hcl/hcl-language-reference/).

## Terraform compatibility

Pulumi HCL aims to run valid Terraform configurations without changes. Resources, data sources, variables, locals, outputs, modules, expressions, and most built-in functions work as documented by HashiCorp. A small number of behaviors differ:

- Resource replacement creates the new resource before deleting the old one (the opposite of Terraform). Set `create_before_destroy = false` in a `lifecycle` block to opt into delete-first behavior.
- `backend`, `cloud`, and `required_version` in the `terraform` block are accepted but ignored with a warning — Pulumi manages state independently.
- State files are not interchangeable. Import existing resources with `pulumi import` rather than reusing a Terraform state file.

For the full list of differences and unsupported features, see the [Terraform compatibility section](/docs/iac/languages-sdks/hcl/hcl-language-reference/#terraform-compatibility) of the reference.

## HCL packages

By default, providers resolve against the [OpenTofu registry](https://opentofu.org/registry/) and are bridged into Pulumi automatically, just as they are in OpenTofu — so a Terraform codebase that depends on community or internal providers works without changes. Pin a source and version with a `terraform` `required_providers` block when you need to.

The [Pulumi Registry](/registry/) also houses 100+ native Pulumi packages. Consume one instead of the bridged Terraform provider by declaring its source with the `pulumi/` namespace (for example, `pulumi/kubernetes`) in a `required_providers` block.
